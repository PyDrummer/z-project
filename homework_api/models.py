from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your API models here.
class Driver(models.Model):
    # Replace these variable names as needed
    driver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    work_clock = models.IntegerField(default=14)
    drive_clock = models.IntegerField(default=10)
    status = models.CharField(max_length=100, default="OK")

    def __str__(self):
        return f'{self.driver}'
    
    def get_absolute_url(self):
        return reverse('', args=[str(self.driver)])

    # def work_hours(self, hours):
    #     if self.work_clock > hours:
    #         self.work_clock -= hours
    #         return f'{self.work_clock} work hours left'
    #     else:
    #         self.work_clock = 0
    #         self.status = 'In Violation'
    #         return f'{self.work_clock} work hours, {self.status}'
    
    # def drive_hours(self, hours):
    #     if self.work_clock > 0 and self.drive_clock > 0:

