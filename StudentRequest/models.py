import imp
from django.db import models
from Account.models import CustomUser
# Create your models here.







class TutorRequest(models.Model):
    Choices = (("ONLINE", 'ONLINE'), ("PHYSICAL", "PHYSICAL"))
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    Last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    state_of_Residence = models.CharField(max_length=200, )
    Class_type = models.CharField(choices=Choices, max_length=20)
    created_At = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    lesson_starting_date = models.DateTimeField()
    Approved = models.BooleanField(default=False)




