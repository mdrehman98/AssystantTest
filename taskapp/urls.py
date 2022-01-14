from django.urls import path
from . import views


urlpatterns = [
    #category apis
    path("createstudentDetails", views.StudentDetails.as_view()),
	path("updatestudentDetails/<str:student_id>/", views.StudentDetails.as_view()),
	path("getstudentDetails", views.StudentDetails.as_view()),
	path("deletestudentDetails/<str:student_id>/", views.StudentDetails.as_view()),
	path("getFullName/<str:student_id>/", views.getFullName.as_view()),
	path("createNestedSerializer", views.getNestedOutput.as_view()),
	path("countDepartments",views.countDepartments.as_view()),
	path("updateNestedSerializer", views.updateNestedSerializer.as_view()),


]