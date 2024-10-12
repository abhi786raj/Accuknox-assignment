
# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading


class MyModel(models.Model):
    name = models.CharField(max_length=100)


@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler thread ID:", threading.get_ident())


# Testing in Django shell to confirm synchronous thread execution

# Run these commands in the Django shell:
# >>> from myapp.models import MyModel
# >>> import threading

# # Print the caller thread ID
# >>> print("Caller thread ID:", threading.get_ident())
# >>> MyModel.objects.create(name="Test")

# Expected output:
# Caller thread ID: <some_thread_id>
# Signal handler thread ID: <same_thread_id_as_caller>

# This confirms that Django signals run in the same thread as the caller by default.
