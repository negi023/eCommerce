from django.db import models
# from account.models import AbstractTime, MyUser
from account.static_vars import ADDRESS_TYPE


# class Profile(AbstractTime):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='customer')
#     full_name = models.CharField(max_length=256, null=True, blank=True)
#     gender = models.CharField(Choices=GENDER, max_length=2, null=True, blank=True)
#     profile_image = models.ImageField(upload_to='customer/profile/%Y-%m-%d/')
#     alternate_mobile = models.CharField(max_length=20, blank=True, null=True)


# class Address(AbstractTime):
#     customer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='address')
#     name = models.CharField(max_length=256)
#     mobile = models.CharField(max_length=20)
#     pincode = models.IntegerField()
#     state = models.CharField(max_length=256)
#     city_district = models.CharField(max_length=256)
#     address = models.CharField(max_length=256)
#     locality_town = models.CharField(max_length=256)
#     address_type = models.CharField(choices=ADDRESS_TYPE, max_length=5)
#     is_default = models.BooleanField(default=False)
#     is_mobile_verified = models.BooleanField(default=False)


# class OfficeWorkingDays(AbstractTime):
#     address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, related_name='office_days')
#     is_saturday_open = models.BooleanField(default=False)
#     is_sunday_open = models.BooleanField(default=False)