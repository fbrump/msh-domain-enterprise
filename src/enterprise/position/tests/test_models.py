# enterprise/position/tests/test_models.py

from django.test import TestCase
from position.models import Position

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
		"""
			Test method __repr__ for position.
		"""
		# arrange
		positionName = 'Web Developer'
		# act
		webDeveloper = Position.objects.get(name=positionName)
		# assert
		self.assertEqual(
			webDeveloper.__repr__(), str(webDeveloper.code) + " - " + positionName)
	
	def test_create_position_without_descritpion(self):
		"""
			Verify process to create an object without description
		"""
		# arrange
		position = Position.objects.create(name='BI')
		# act
		position.save()
		position_saved = Position.objects.get(name='BI')
		#assert
		self.assertIsNotNone(position_saved)
		self.assertEqual(position.code,  position_saved.code)
		self.assertIsNotNone(position.created)

	def test_create_position_with_descritpion(self):
		"""
			Verify process to create an object with description
		"""
		# arrange
		position = Position.objects.create(name='DBA', description='Data base administrator')
		# act
		position.save()
		position_saved = Position.objects.get(name='DBA')
		#assert
		self.assertIsNotNone(position_saved)
		self.assertEqual(position.code,  position_saved.code)
		self.assertEqual('Data base administrator',  position_saved.description)
		self.assertIsNotNone(position.created)

