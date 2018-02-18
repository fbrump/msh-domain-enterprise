# enterprise/mail/tests/test_model.py

from django.test import TestCase
from ..models import Mail, MailEmployeer, MailManager

class MailEmployeerTest(TestCase):
	"""
		Suite case for tests in mail employer
	"""
	def setUp(self):
		# employeer 1
		MailEmployeer.objects.create(
			address='joaquim.perine@gmail.com',
			type_mail=Mail.TYPE_PERSONAL)
		MailEmployeer.objects.create(
			address='joaquim.perine@company.com',
			type_mail=Mail.TYPE_PROFESSIONAL)
		# employeer 2
		MailEmployeer.objects.create(
			address='mery.banks@outlook.com',
			type_mail=Mail.TYPE_PERSONAL)
		MailEmployeer.objects.create(
			address='mery.banks@company.com',
			type_mail=Mail.TYPE_PROFESSIONAL)
		# employeer 3
		MailEmployeer.objects.create(
			address='piedro.carmelo@company.com',
			type_mail=Mail.TYPE_PROFESSIONAL)

	def test_find_one_object(self):
		# arrange
		mail_address = 'mery.banks@company.com'
		# act
		mail_find = MailEmployeer.objects.get(address=mail_address)
		# assert
		self.assertIsNotNone(mail_find)
		self.assertEqual(mail_find.type_mail, Mail.TYPE_PROFESSIONAL)
	def test_find_one_object_not_exists(self):
		# arrange
		mail_address = 'margarita.banks@company.com'
		# act
		mail_find = MailEmployeer.objects.filter(address=mail_address)
		# assert
		self.assertIsNotNone(mail_find)
		self.assertEqual(len(mail_find), 0)
	def test_find_list_by_type(self):
		# arrange
		type_mail = Mail.TYPE_PERSONAL
		# act
		mails = MailEmployeer.objects.filter(type_mail=type_mail)
		# assert
		self.assertTrue(len(mails) > 0)

class MailManagerTest(TestCase):
	"""
		Suite case for tests in mail manager
	"""
	def setUp(self):
		# Manager 1
		MailManager.objects.create(
			address='joaquim.perine@gmail.com',
			type_mail=Mail.TYPE_PERSONAL)
		MailManager.objects.create(
			address='joaquim.perine@company.com',
			type_mail=Mail.TYPE_PROFESSIONAL)
		# Manager 2
		MailManager.objects.create(
			address='mery.banks@outlook.com',
			type_mail=Mail.TYPE_PERSONAL)
		MailManager.objects.create(
			address='mery.banks@company.com',
			type_mail=Mail.TYPE_PROFESSIONAL)
		# Manager 3
		MailManager.objects.create(
			address='piedro.carmelo@company.com',
			type_mail=Mail.TYPE_PROFESSIONAL)

	def test_find_one_object(self):
		# arrange
		mail_address = 'mery.banks@company.com'
		# act
		mail_find = MailManager.objects.get(address=mail_address)
		# assert
		self.assertIsNotNone(mail_find)
		self.assertEqual(mail_find.type_mail, Mail.TYPE_PROFESSIONAL)
	def test_find_one_object_not_exists(self):
		# arrange
		mail_address = 'margarita.banks@company.com'
		# act
		mail_find = MailManager.objects.filter(address=mail_address)
		# assert
		self.assertIsNotNone(mail_find)
		self.assertEqual(len(mail_find), 0)
	def test_find_list_by_type(self):
		# arrange
		type_mail = Mail.TYPE_PERSONAL
		# act
		mails = MailManager.objects.filter(type_mail=type_mail)
		# assert
		self.assertTrue(len(mails) > 0)
