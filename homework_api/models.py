from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your API models here.
class Driver(models.Model):
    # Replace these variable names as needed
    driver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    work_clock = models.IntegerField(default=14)
    drive_clock = models.IntegerField(default=10)
    work_status = models.CharField(max_length=100, default="OK")
    drive_status = models.CharField(max_length=100, default="OK")

    def __str__(self):
        return f'{self.driver}'
    
    def get_absolute_url(self):
        return reverse('', args=[str(self.driver)])

