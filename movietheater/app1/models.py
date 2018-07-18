# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MovieTheater(models.Model):
	name   =models.CharField(max_length=50)
	address=models.TextField(max_length=250)


class Peoples(models.Model):
	name   =models.CharField(max_length=50)
	address=models.TextField(max_length=250)
	phone  =models.CharField(max_length=250)
	email  =models.CharField(max_length=250)

class Enquiry(models.Model):
	name =models.CharField(max_length=50)
	date =models.DateTimeField()
	price=models.IntegerField()
