from django.db import models

# Create your models here.
class CUSTOMER_INFO(models.Model):
    customer_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    phone_number = models.IntegerField()
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    created_time = models.DateTimeField()
    
    def __str__(self):
        return self.customer_name