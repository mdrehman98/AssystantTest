from django.shortcuts import render

import datetime

from uuid import uuid4

from django.forms import model_to_dict

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.core.paginator import Paginator
from django.db.models import Count
from .models import *
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import messaging
from .serializers import *

class CustomResponse():
    def successResponse(self, data, status=status.HTTP_200_OK, description="SUCCESS"):
        return Response(
            {
                "success": True,
                "errorCode": 0,
                "description": description,
                "info": data
            }, status=status)

    def errorResponse(self, data={}, description="ERROR", errorCode=1, status=status.HTTP_200_OK):
        return Response(
            {
                "success": False,
                "errorCode": errorCode,
                "description": description,
                "info": data
            }, status=status)
# Create your views here.
class StudentDetails(APIView):
	permission_classes = [AllowAny, ]
	def post(self,request):
		"""
		Request body:
		{
    "student_id":1,
    "first_name":"Sam",
    "last_name":"fisher"
}
		"""
		student_id=request.data['student_id']
		first_name=request.data['first_name']
		last_name=request.data['last_name']
		Student=student()
		Student.student_id=student_id
		Student.first_name=first_name
		Student.last_name=last_name
		Student.save()
		return CustomResponse().successResponse(description="Student details created", data=model_to_dict(Student))

	def put(self,request,student_id):
		"""
	REQUEST BODY, please include student id in url
	{
    "first_name":"Rahul",
    "last_name":"Hindupuri"
}		"""
		Student = student.objects.filter(student_id=student_id).first()
		if student:
			Student.first_name = request.data["first_name"]
			Student.last_name=request.data["last_name"]
			Student.save()
			return CustomResponse().successResponse(description="Student Details has been updated", data=model_to_dict(Student))
		else:
			return CustomResponse().errorResponse(description="Studnent not found with given id")

	def get(self,request):
		Student=student.objects.all()
		if Student:
			return CustomResponse().successResponse(description="Student Details has been updated", data=Student.values())
		return CustomResponse().errorResponse(description="Student Details not found")


	def delete(self,request,student_id):
		Student=student.objects.filter(student_id=student_id).first()
		if Student:
			Student.delete()
			return CustomResponse().successResponse(description="Student Details has been deleted", data=[])
		return CustomResponse().errorResponse(description="Student Details not found")

class getFullName(APIView):
	permission_classes = [AllowAny, ]
	def get(self,request,student_id):
		Student=student.objects.filter(student_id=student_id).first()
		first_name=Student.first_name
		last_name=Student.last_name		
		full_name=Student.get_full_name()
		json={"first_name":first_name,"last_name":last_name,"full_name":full_name}
		return CustomResponse().successResponse(description="Student Details are", data=json)


class getNestedOutput(APIView):	
	permission_classes = [AllowAny, ]
	"""
	REQUEST BODY  CREATE NESTED SERILIZER
	{
    "student_id":7,"first_name":"Saif","last_name":"Khan",
    "departments":[{"department_name":"physics","department_id":6,"department_head":"atul kumar"},{"department_name":"chemistry","department_id":7,"department_head":"Ajay Kumar"}]
}
	"""
	def post(self,request):
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	#VIEW NESTED SERIALIZER
	def get(self, request):
		List = student.objects.all()
		serializer = StudentSerializer(instance=List, many=True)
		if serializer:
			return CustomResponse().successResponse(description="Lists", data=serializer.data)
		else:
			return CustomResponse().errorResponse(description="Error Viewing Lists")
class updateNestedSerializer(APIView):
	permission_classes = [AllowAny, ]
	def put(self,request):
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class countDepartments(APIView):
	permission_classes = [AllowAny, ]
	def get(self,request):
		lists=[]
		depart=student.objects.annotate(number_of_departments=Count('departments'))
		for i in range(0,len(depart.values())):
			student_name=depart.values()[i]['first_name']
			department_count=depart.values()[i]['number_of_departments']
			tuple=(student_name,department_count)
			lists.append(tuple)
			#lists.append({"student":student_name,"department_count":department_count})
		return CustomResponse().successResponse(description="Number of Departments counted", data=lists)