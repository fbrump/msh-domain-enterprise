# enterprise/position/tests/test_views.py

import json
import uuid
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Position
from ..serializers import PositionSerializer

# initialize the API client app
client = Client()

class GetAllPositionsTest(TestCase):
	""" Test module for GET all positions API """
	
	def setUp(self):
		Position.objects.create(name='Web Developer', description='Developer web solutions')
		Position.objects.create(name='Frondent Developer')
		Position.objects.create(name='Backend Developer', description='Working with Python, Node and C#')
		Position.objects.create(name='DBA')
		Position.objects.create(name='Tester')
		Position.objects.create(name='BI', description='Build solution for marketing with datas')

	def test_get_all_positions(self):
		# arrange
		response = client.get(reverse('get_post_position'))
		positions = Position.objects.all()
		# act
		serializers = PositionSerializer(positions, many=True)
		# asserts
		self.assertEqual(response.data, serializers.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePositionTest(TestCase):
	""" Test module for GET single position API """
	
	def setUp(self):
		self.webDeveloper = Position.objects.create(name='Web Developer', description='Developer web solutions')
		self.frontendDeveloper = Position.objects.create(name='Frontend Developer')
		self.backendDeveloper = Position.objects.create(name='Backend Developer', description='Working with Python, Node and C#')
		self.dba = Position.objects.create(name='DBA')
		self.tester = Position.objects.create(name='Tester')
		self.bi = Position.objects.create(name='BI', description='Build solution for marketing with datas')

	def test_get_valid_single_position(self):
		# arrange
		response = client.get(reverse('get_delete_update_postion', kwargs={'code': self.frontendDeveloper.code}))
		position = Position.objects.get(code=self.frontendDeveloper.code)
		# act
		serializer = PositionSerializer(position)
		# asserts
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid_single_position(self):
		# arrange
		# act
		response = client.get(reverse('get_delete_update_postion', kwargs={'code': uuid.uuid4()}))
		# asserts
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewPositionTest(TestCase):
	""" Test module for inserting a new position """
	
	def setUp(self):
		self.valid_payload = {
			'name': 'P.O.',
			'description': 'Product Owner of project'
		}
		self.invalid_payload = {
			'name': '',
			'description': ''
		}

	def test_create_valid_position(self):
		response = client.post(
			reverse('get_post_position'),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_invalid_position(self):
		response = client.post(
			reverse('get_post_position'),
			data=json.dumps(self.invalid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSinglePositionTest(TestCase):
	""" Test module for updating an existing position record """
	def setUp(self):
		self.webDeveloper = Position.objects.create(name='Web Developer', description='Developer web solutions')
		self.frontendDeveloper = Position.objects.create(name='Frontend Developer')

		self.valid_payload = {
			'name': 'Angular Developer',
			'description': 'Frontend working with Angular 4+'
		}
		self.invalid_payload = {
			'name': ''
			'description': 'Anonimo'
		}

	def test_valid_update_position(self):
		response = client.put(
			reverse('get_delete_update_postion'),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_update_position(self):
		response = client.put(
			reverse('get_delete_update_postion'),
			data=json.dumps(self.invalid_payload),
			content_type='application/json'
		)