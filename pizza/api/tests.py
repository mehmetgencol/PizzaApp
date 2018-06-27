# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Pizza
import requests
# Create your tests here.

class PizzaApiTest(TestCase):
	def setUp(self):
		self.url = 'http://localhost:8000/api/%s/'
		self.pizza_size=50
		self.customer_name='Azer'
		self.customer_address='Azer Home!'

	def test_add_pizza(self):
		resp = requests.post(self.url % 'add_pizza', data={'pizza_size': self.pizza_size, 'customer_name': self.customer_name, 'customer_address': self.customer_address})
		self.assertEqual(resp.status_code, 200)

	def test_update_pizza(self):
		pizza = Pizza.objects.filter()[0]
		resp = requests.post(self.url % 'update_pizza', data={'pizza_id': pizza.pizza_id, 'pizza_size': pizza.pizza_size, 'customer_name': pizza.customer_name + ' New Name', 'customer_address': pizza.customer_address})
		self.assertEqual(resp.status_code, 200)


	def test_delete_pizza(self):
		resp = requests.post(self.url % 'delete_pizza', data={'pizza_id': 0})
		self.assertEqual(resp.status_code, 200)
