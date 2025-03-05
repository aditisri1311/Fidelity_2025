from django.urls import path
from .views import create_item, get_item, get_all_items, update_item, delete_item

urlpatterns = [
    path('items/', get_all_items, name="get_all_items"),
    path('items/create/', create_item, name="create_item"),
    path('items/<str:item_id>/', get_item, name="get_item"),
    path('items/update/<str:item_id>/', update_item, name="update_item"),
    path('items/delete/<str:item_id>/', delete_item, name="delete_item"),
]
