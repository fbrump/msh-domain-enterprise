# enterprise/position/models.py
from django.db import models
import uuid

class Position(models.Model):
	"""
	Description: Position of the employeer in company
	"""
	created = models.DateTimeField(auto_now_add=True)
	code = models.UUIDField(default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)

	class Meta:
		ordering = ('created',)
	def __repr__(self):
		return str(self.code) + ' - ' + self.name