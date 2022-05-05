from django.contrib import admin
from .models import CustomUser, Teacher, TeachersBankDetails
# Register your models here.
admin.site.register((CustomUser, Teacher, TeachersBankDetails))