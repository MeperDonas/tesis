from django.contrib import admin
from users.models import UserAdministrator, UserEmployee, UserCustomer, UserSupplier

# Register your models here.
admin.site.register(UserAdministrator)
admin.site.register(UserEmployee)
admin.site.register(UserCustomer)
admin.site.register(UserSupplier)
