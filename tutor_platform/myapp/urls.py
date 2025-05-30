from django.urls import path
from .views import TutorList, StudentList

urlpatterns = [
    path('tutors/', TutorList.as_view(), name='tutor-list'),
    path('students/', StudentList.as_view(), name='student-list'),
]
