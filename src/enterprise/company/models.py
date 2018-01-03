# enterprise/company/models.py

import uuid
from django.db import models

class Company(models.Model):
	"""
	Description: Company
	"""
	created = models.DateTimeField(auto_now_add=True)
	code = models.UUIDField¶(default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100)
	cnpj = models.CharField(max_length=15)
	description = models.TextField(blank=True)
	url = models.URLField(max_length=500, blank=True)

	class Meta:
		odering = ('name',)