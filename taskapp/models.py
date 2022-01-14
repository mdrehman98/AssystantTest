from django.db import models
from django.db.models.fields import URLField
from django.contrib.postgres.fields import ArrayField
from django.db.models import IntegerField, Model

# Create your models here.
class testModel(models.Model):
	title = models.CharField(max_length=255, default='',null=False, blank=False)
	desc=models.CharField(max_length=255)

	def __str__(self):
		return self.title

class student(models.Model):
	student_id=IntegerField(primary_key=True)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)

	def get_full_name(self):
		full_name="{} {}".format(self.first_name, self.last_name)
		return full_name.strip()


class Department(models.Model):
	department_id=models.IntegerField(primary_key=True)
	department_name=models.CharField(max_length=100)
	department_head=models.CharField(max_length=100)
	std=models.ForeignKey(student,related_name="departments",on_delete=models.CASCADE)
