from functools import partial
from rest_framework import serializers
from .models import *
from rest_framework.response import Response


class DepartmentSerializer(serializers.ModelSerializer):
	department_name=serializers.CharField(max_length=100)
	department_id = serializers.IntegerField(read_only=True)
	#id = serializers.IntegerField(read_only=True)
	class Meta:
		model = Department
		fields = ('department_id','department_name','department_head')


class StudentSerializer(serializers.ModelSerializer):
	student_id = serializers.IntegerField(required=False)
	departments=DepartmentSerializer(many=True)
	#id = serializers.IntegerField(read_only=True)
	def create(self, validated_data):
		department_details= validated_data.pop('departments')
		new_student = student.objects.create(**validated_data)
		for i in department_details:
			Department.objects.create(**i,std=new_student)
		return new_student

	def update(self, instance, validated_data):
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.save()

		departments = validated_data.get('departments')

		for department in departments:
			department_id = department.get('department_id', None)
			if department_id:
				dept = Department.objects.get(department_id=department_id, Department=instance)
				dept.department_name = department.get('department_name', dept.department_name)
				dept.department_head = department.get('department_head', dept.department_head)
				dept.save()
			else:
				pass
				#Department.objects.create(account=instance, **item)

		return instance
	
	
	
	class Meta:
		model = student
		fields = '__all__'