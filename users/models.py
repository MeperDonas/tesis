from django.db import models
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class BaseUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(("Phone Number"), unique=True, blank=True, null=True)
    password = models.CharField(max_length=128, default='', blank=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class UserAdministrator(BaseUser):
    pass
    def __str__(self):
        return self.username

class UserEmployee(BaseUser):
    pass                                                        
    def __str__(self):
        return self.username

class UserCustomer(BaseUser):
    vehicle = models.CharField(max_length=100, blank=True, null=True)
    vehicle_number = models.CharField(max_length=20, blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.username

class UserSupplier(BaseUser):
    catalog = models.FileField(upload_to='supplier_catalogs/', blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'csv'])])
    def __str__(self):
        return self.username