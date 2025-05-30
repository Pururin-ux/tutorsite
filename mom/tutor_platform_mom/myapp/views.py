from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tutor, Student
from .serializers import TutorSerializer, StudentSerializer

class TutorList(APIView):
    def get(self, request):
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)
        return Response(serializer.data)

class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
