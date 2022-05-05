from django.urls import path
from .views import AllTutors
urlpatterns = [
    path('alltutors', AllTutors.as_view(), name="get_all_tutors")
]