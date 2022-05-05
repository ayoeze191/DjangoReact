from unicodedata import name
from django.urls import path
from .views import TeacherRegistrationViews, TeacherLoginView
urlpatterns = [
    path('register', TeacherRegistrationViews.as_view(), name='Teacher_register'),
    path('login', TeacherLoginView.as_view(), name = "Teacher_login")

]