# enterprise/persona/models.py
from django.db import models

import uuid

class Persona(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	code = models.UUIDField(default=uuid.uuid4, editable=False)
	
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        abstract = True
