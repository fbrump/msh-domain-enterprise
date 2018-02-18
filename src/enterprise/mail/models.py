from django.db import models
# from dj.choices import Choices
import uuid

class Mail(models.Model):
	"""
	Description: Model for mail object

		Type of Mail - Personal, Professional
	"""
	TYPE_PERSONAL = 1
	TYPE_PROFESSIONAL = 2
	TYPES_CHOICES = (
		(TYPE_PERSONAL, "Personal"),
		(TYPE_PROFESSIONAL, "Progessional"),
	)

	created = models.DateTimeField(auto_now_add=True)
	code = models.UUIDField(default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100)
	type_mail = models.IntegerField(
		choices=TYPES_CHOICES,
		default=TYPE_PERSONAL,
	)
	
	class Meta:
		abstract = True
