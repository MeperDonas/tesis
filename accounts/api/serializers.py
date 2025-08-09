from rest_framework import serializers
from accounts.models import UserAdministrator, UserEmployee, UserCustomer, UserSupplier

class UserAdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdministrator
        fields = '__all__'

class UserEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmployee
        fields = '__all__'

class UserCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomer
        fields = '__all__'

class UserSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSupplier
        fields = '__all__'
        read_only_fields = ('created', 'updated', )