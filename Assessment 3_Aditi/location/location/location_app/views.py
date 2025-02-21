from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import Location
from .serializers import LocationSerializer

class LocationViewSet(ViewSet):
    """
    A ViewSet for listing, creating, retrieving, and deleting Location instances.
    """

    def list(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                location = Location.objects.get(pk=pk)
                serializer = LocationSerializer(location)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Location.DoesNotExist:
                return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            try:
                location = Location.objects.get(pk=pk)
                location.delete()
                return Response({"message": "Location deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            except Location.DoesNotExist:
                return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

