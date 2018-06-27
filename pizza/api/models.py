# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Pizza(models.Model):
	pizza_id = models.AutoField(primary_key=True, default=0)
	pizza_size = models.IntegerField()
	customer_name = models.TextField()
	customer_address = models.TextField()



