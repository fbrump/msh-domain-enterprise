from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from company.models import Company
from company.serializers import CompanySerializer

@csrf_exempt
def company_list(request):
	"""
		Method that list all companies and add new company.
	"""
	if request.method == 'GET':
		companies = Company.objects.all()
		serializer = CompanySerializer(companies, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = CompanySerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=200)
		return JsonResponse(serializer.errors, status=400)
