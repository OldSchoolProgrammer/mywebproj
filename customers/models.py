from django.db import models


class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(blank=False, unique=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    phone = models.IntegerField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
