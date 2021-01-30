from rest_framework import serializers
from .models import *


# validatiors
def start_with_s(value):
    if value[0].lower() != 's':
        raise serializers.ValidationError('Name start with s')


### first method of serializer class for our views
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()  # if u want to show id in json data then add this line in our serializer
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # field level validations
    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'shrijeet' and ct.lower() != 'nesari':
            raise serializers.ValidationError('City must be Nesari')
        return data

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.roll = validate_data.get('roll', instance.roll)
        instance.city = validate_data.get('city', instance.city)
        instance.save()
        return Student.objects.create(**validate_data)


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        # fields=['name','subject','city']
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields=['name','subject','city']
        fields = '__all__'
