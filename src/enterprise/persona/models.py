# enterprise/persona/models.py
from django.db import models
from position.models import Position

import uuid

class Persona(models.Model):
	created = models.DateTimeField(auto_now_add=True, editable=False)
	code = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
	name = models.CharField(max_length=100)
	birth_date = models.DateTimeField()
	position = models.ForeignKey(Position, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Persona"
		verbose_name_plural = "Personas"

	def __str__(self):
		return self.name
