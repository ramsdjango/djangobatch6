# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.models import StudyHall, Expenses, Enquiry, Course, Student, Expenses
# Create your views here.
def study(request):
	if request.method=="POST":
		data = request.POST
		if data.get("enquiry"):
			course_inst = Course.objects.get(pk=data.get("enq_course"))
			stdudent_inst = Student.objects.get(pk=data.get("enq_student"))
			enq = Enquiry(
				name = data.get("enq_name"),
				student = stdudent_inst,
				course = course_inst
				)
			enq.save()
		elif data.get("expense"):
			studyhall_inst = StudyHall.objects.get(pk=data.get("exp_studyhall"))
			exp = Expenses(
				studyhall = studyhall_inst,
				date = data.get("exp_date"),
				name = data.get("exp_name"),
				desc = data.get("exp_desc"),
				value = data.get("exp_value"),
				)
			exp.save()
		elif data.get("studyhall"):
			hall = StudyHall(name=data.get("hall_name"), 
				area=data.get("hall_area"))
			hall.save()
		elif data.get("student"):
			stud_inst=Student(name=data.get("name"),address=data.get("address"),phone=data.get("Phone"),email=data.get("email"))
			stud_inst.save()
		else:
			cour_inst=Course(name=data.get("coursename"))
			cour_inst.save()
	studyhalls = StudyHall.objects.all()
	expenses = Expenses.objects.all()
	enquiries = Enquiry.objects.all()
	courses = Course.objects.all()
	students = Student.objects.all()
	return render(request,"app1/index.html",{
		"halls": studyhalls,
		"exps": expenses,
		"enqs": enquiries,
		"students": students,
		"courses": courses 
		})
def studyhalls(request):
	studyhalls = StudyHall.objects.all()
	return render(request,"app1/index.html",{"studyhalls":studyhalls})
