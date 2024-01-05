from django.db import models

# Create your models here.
class CUSTOMER_INFO(models.Model):
    customer_name = models.CharField(max_length=50)
    Email_id = models.EmailField()
    Phone_number = models.IntegerField()
    Password = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    
    def __str__(self):
        return self.customer_name