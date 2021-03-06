# enterprise/company/serializers.py

from rest_framework import serializers
from company.models import Company

class CompanySerializer(serializers.Serializer):
	code = serializers.UUIDField(format='hex', read_only=True)
	name = serializers.CharField(min_length=3, max_length=100)
	cnpj = serializers.CharField(max_length=15)
	description = serializers.CharField(allow_blank=True)
	url = serializers.URLField(max_length=500, allow_blank=True)
	
	def create(self, validated_data):
		"""
			Created new object and return validation.
		"""
		return Company.objects.create(**validated_data)
	def update(self, instance, validated_data):
		"""
			Updated object instance and given validated data.
		"""
		instance.name = validated_data.get('name', instance.name)
		instance.cnpj = validated_data.get('cnpj', instance.cnpj)
		instance.description = validated_data.get('description', instance.description)
		instance.url = validated_data.get('url', instance.url)
		instance.save()
		return instance