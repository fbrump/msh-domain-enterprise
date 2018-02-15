# enterprise/position/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Position
from .serializers import PositionSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_postion(request, code):
	try:
		position = Position.objects.get(code=code)
	except Position.DoesNotExist as e:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serialiser = PositionSerializer(position)
		return Response(serialiser.data)
	elif request.method == 'DELETE':
		return Response({})
	elif request.method == 'PUT':
		return Response({})

@api_view(['GET', 'POST'])
def get_post_position(request):
	if request.method == 'GET':
		positions = Position.objects.all()
		serializers = PositionSerializer(positions, many=True)
		return Response(serializers.data)
	elif request.method == 'POST':
		data = {
			'name': request.data.get('name'),
			'description': request.data.get('description')
		}
		serializer = PositionSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
