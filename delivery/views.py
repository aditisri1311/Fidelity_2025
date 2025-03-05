from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ItemModel
from bson.json_util import dumps
 

@csrf_exempt
def create_item(request):
    """Create a new item"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item_id = ItemModel.create_item(data)
            return JsonResponse({"message": "Item created", "id": str(item_id)}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def get_item(request, item_id):
    """Get an item by ID"""
    if request.method == "GET":
        item = ItemModel.get_item(item_id)
        if item:
            return JsonResponse(json.loads(dumps(item)), safe=False)
        return JsonResponse({"error": "Item not found"}, status=404)

@csrf_exempt
def get_all_items(request):
    """Get all items"""
    if request.method == "GET":
        items = ItemModel.get_all_items()
        return JsonResponse(json.loads(dumps(items)), safe=False)

@csrf_exempt
def update_item(request, item_id):
    """Update an item by ID"""
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            result = ItemModel.update_item(item_id, data)
            if result.modified_count:
                return JsonResponse({"message": "Item updated"}, status=200)
            return JsonResponse({"message": "No changes made"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def delete_item(request, item_id):
    """Delete an item by ID"""
    if request.method == "DELETE":
        result = ItemModel.delete_item(item_id)
        if result.deleted_count:
            return JsonResponse({"message": "Item deleted"}, status=200)
        return JsonResponse({"error": "Item not found"}, status=404)
