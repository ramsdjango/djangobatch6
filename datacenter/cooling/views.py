# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ram(requast):
	return HttpResponse("heloo ram")
def fun(requast):
	return HttpResponse("25.67")
def fun1(requast):
	resp="""
<html>
<head>
	<title>
		title tag information
	</title>
</head>
<!--<body bgcolor ="#58D68D">-->
<body bg color ="#58D68D">
	this is body pard
	<h1>
		this is h1 tag
	</h1>
	<h2>
		this is h2 tag
	</h2>
	<h3>
		this is h3 tag
	</h3>
	<h4>
		this is h4 tag
	</h4>
	<h5>
		this is h5 tag
	</h5>
	<h6>
		this is h6 tag
	</h6>
	<a href="http://www.google.com"> go to google</a><br>
	<a href="http://www.youtube.com"> go to youtube</a><br>
	<form>
		username:<input type="text"></input><br>
		password:<input type="password"></input><br>
		email:<input type="email"></input><br>
		Gender:male:<input type="radio"></input><br>gender:female:<input type="radio"></input><br>
		submit:<input type="submit"></input><br>


	</form>

</body>
</html>"""
	return HttpResponse(resp)
  
def fun2(request):
	return render(request,"ram.html")