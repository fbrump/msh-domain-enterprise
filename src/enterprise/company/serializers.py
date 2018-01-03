# enterprise/company/serializers.py

from rest_framework import serializers
from company.models import Company

class CompanySerializer(serializers.Serializer):
    code = serializers.UUIDField(default=uuid.uuid4, editable=False)
    name = serializers.CharField(min_length=3, max_length=100)
    cnpj = serializers.CharField(max_length=15)
    description = serializers.CharField()
    