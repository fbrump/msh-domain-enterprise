# enterprise/position/tests/test_models.py

from django.test import TestCase
from ..models import Position

class PositionTest(TestCase):
	""" Tests module for Position model """
	def setUp(self):
		Position.objects.create(
			name='Web Developer', 
			description='Working developing new web sites and systems for Web plataform with Python, Node, Ruby and C#.')

		Position.objects.create(name='Backend Developer', 
								description= 'Building new feature and better performace for systems with Python and C#.')

		Position.objects.create(name='Frontend Developer', 
								description= 'Apply usability with UI and UX using Angular and React')

		def test_position_repr(self):
			positionName = 'Web Developer'
			webDeveloper = Position.objects.get(name=positionName)
			self.assertEqual(
				webDeveloper.__repr__(), webDeveloper.code + " - " + positionName)
