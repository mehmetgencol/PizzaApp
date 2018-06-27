# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Pizza
import mimetypes
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import traceback
from django.core import serializers



from django.shortcuts import render

# Create your views here.

@csrf_exempt 
def get_pizza(request):
	if request.method == 'POST':
		try:
			data = Pizza.objects.get(pizza_id=int(request.POST['pizza_id']))
			data = serializers.serialize('json', [data, ])
			return HttpResponse(data, content_type="application/json", status=200)
		except:
			return HttpResponse(json.dumps({'status':'No pizza found with given id!'}), content_type="application/json", status=400)


@csrf_exempt
def add_pizza(request):
	if request.method == 'POST':
		pizza_size = int(request.POST['pizza_size'])
		customer_name = request.POST['customer_name']
		customer_address = request.POST['customer_address']
		pizza = Pizza(pizza_size=pizza_size, customer_name=customer_name, customer_address=customer_address)
		try:
			pizza.save()
			return HttpResponse(json.dumps({'status':'SUCCESS'}), content_type="application/json", status=200)
		except:
			return HttpResponse(json.dumps({'status':'ERROR'}), content_type="application/json", status=400)

@csrf_exempt
def update_pizza(request):
	if request.method == 'POST':
		pizza_id=request.POST['pizza_id']
		pizza = Pizza.objects.get(pizza_id=pizza_id)
		if pizza is None:
			return HttpResponse(json.dumps({'status':'No pizza found with given id!'}), content_type="application/json", status=400)

		if int(request.POST['pizza_size']) not in (30, 50):
			return HttpResponse(json.dumps({'status':'Pizza sizes: 30, 50.'}), content_type="application/json", status=400)

		pizza.pizza_size = int(request.POST['pizza_size'])
		pizza.customer_name = request.POST['customer_name']
		pizza.customer_address = request.POST['customer_address']

		try:
			pizza.save()
			return HttpResponse(json.dumps({'status':'SUCCESS'}), content_type="application/json", status=200)
		except:
			return HttpResponse(json.dumps({'status':'ERROR'}), content_type="application/json", status=400)


@csrf_exempt
def delete_pizza(request):
	if request.method == 'POST':
		pizza_id=request.POST['pizza_id']
		try:
			Pizza.objects.filter(pizza_id=pizza_id).delete()
			return HttpResponse(json.dumps({'status':'SUCCESS'}), content_type="application/json", status=200)
		except:
			return HttpResponse(json.dumps({'status':'ERROR'}), content_type="application/json", status=400)