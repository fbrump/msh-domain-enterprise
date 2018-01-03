# enterprise/company/models.py

from django.db import models

class Company(models.Model):
	"""
	Description: Company in the company
	"""
	created = models.DateTimeField(auto_now_add=True)
	code = models.UUIDField¶(max_length=20)
	name = models.CharField(max_length=100)
	cnpj = models.CharField(max_length=15)
	description = models.TextField(blank=True)
	url = models.URLField(max_length=500)

	class Meta:
		odering = ('name',)