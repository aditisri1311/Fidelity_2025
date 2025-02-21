from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import Price
from .serializers import PriceSerializer


import requests
class PriceViewSet(ViewSet):
    """
    A ViewSet for listing, creating, retrieving, and deleting Price instances.
    """

    def list(self, request):
        prices = Price.objects.all()
        serializer = PriceSerializer(prices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                price = Price.objects.get(pk=pk)
                serializer = PriceSerializer(price)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Price.DoesNotExist:
                return Response({"error": "Price not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            try:
                price = Price.objects.get(pk=pk)
                price.delete()
                return Response({"message": "Price deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            except Price.DoesNotExist:
                return Response({"error": "Price not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)




# Create your views here.
def get_price(request):
    price= Price.objects.all()
    location = request.GET.get('location')
    location_response = requests.get('http://127.0.0.1:8001/location/app/', params={'location': location})

    if location_response.status_code == 200:
        location_data = location_response.json()
    else:
        location_data = {"error": "Unable to fetch location data"}

    # Combine price and location data
    price_data = [price.to_dict() for price in price]  # Assuming Price model has a to_dict method

    response_data = {
        'prices': price_data,
        'location': location_data
    }

    return Response(response_data)
    