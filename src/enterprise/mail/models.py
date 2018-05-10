from django.db import models
import uuid

from persona.models import Employee

class Mail(models.Model):
	"""
	Description: Model for mail object

		Type of Mail - Personal, Professional
	"""
	TYPE_PERSONAL = 1
	TYPE_PROFESSIONAL = 2
	TYPES_CHOICES = (
		(TYPE_PERSONAL, "Personal"),
		(TYPE_PROFESSIONAL, "Professional"),
	)

	created = models.DateTimeField(auto_now_add=True)
	code = models.UUIDField(default=uuid.uuid4, editable=False)
	address = models.EmailField(max_length=100)
	type_mail = models.IntegerField(
		choices=TYPES_CHOICES,
		default=TYPE_PERSONAL,
	)
	
	class Meta:
		abstract = True

class MailManager(Mail):
	"""
	Description: Model for mail of Manager
	"""
	

	class Meta:
		ordering = ('created',)
	def __str__(self):
		return self.address

class MailEmployeer(Mail):
	"""
	Description: Model for mail of employeer
	"""
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

	class Meta:
		ordering = ('created',)
	def __str__(self):
		return self.address
