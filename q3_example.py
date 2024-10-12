# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyModel(models.Model):
    name = models.CharField(max_length=100)


class RelatedModel(models.Model):
    description = models.CharField(max_length=100)


@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    # Modify RelatedModel in the signal
    RelatedModel.objects.create(description=f"Created for {instance.name}")


# Testing transaction behavior in Django shell

# Run these commands in the Django shell to verify transaction rollback behavior:
# >>> from django.db import transaction
# >>> from myapp.models import MyModel, RelatedModel
# 
# >>> try:
# ...     with transaction.atomic():
# ...         instance = MyModel.objects.create(name="Test")
# ...         # Intentionally raise an error after the signal is triggered
# ...         raise Exception("Simulating a transaction failure")
# ... except Exception as e:
# ...     print(e)

# # Check if the RelatedModel entry was created
# >>> print("RelatedModel entries:", RelatedModel.objects.all())

# Expected output:
# Simulating a transaction failure
# RelatedModel entries: <QuerySet []>

# If RelatedModel remains empty, it confirms that the signal ran in the same transaction.
