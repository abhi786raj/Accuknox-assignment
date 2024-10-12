
# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time


class MyModel(models.Model):
    name = models.CharField(max_length=100)


@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulate a time-consuming task
    print("Signal handler finished.")


# Testing the synchronous behavior in Django shell

# Run these commands in Django shell to verify synchronous behavior:
# >>> from myapp.models import MyModel
# >>> import time

# # Record the start time
# >>> start_time = time.time()
# >>> MyModel.objects.create(name="Test")

# # Record the end time
# >>> end_time = time.time()
# >>> print("Total time taken:", end_time - start_time)

# Expected output:
# Signal handler started.
# Signal handler finished.
# Total time taken: ~5.0 seconds
