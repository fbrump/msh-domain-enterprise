# enterprise/persona/models.py
from django.db import models

import uuid

from position.models import Position
from company.models import Company

class Persona(models.Model):
	created = models.DateTimeField(auto_now_add=True, editable=False)
	code = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
	name = models.CharField(max_length=100)
	position = models.ForeignKey(Position, null=True, blank=True, on_delete=models.SET_NULL)
	company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)

	class Meta:
		abstract = True

	def __str__(self):
		return self.name

class Employee(Persona):
	"""
	Description: Model that mapper employee propoerties
	"""
	birth_date = models.DateTimeField()

	class Meta:
		verbose_name = "Employee"
		verbose_name_plural = "Employees"
		ordering = ('created',)