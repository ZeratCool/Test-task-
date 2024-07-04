from django.urls import path
from .views import (AddingMenuViewSet,
                    RestaurantViewSet,
                    AddingRestaurantViewSet,
                    MenuViewSet, UpdateView
                    )
urlpatterns = [
    path('restaurants/', RestaurantViewSet.as_view({'get': 'list'}), name='restaurants'),
    path('restaurants/add', AddingRestaurantViewSet.as_view({'post': 'create'}), name='restaurant_add'),
    path('add_menu/', AddingMenuViewSet.as_view({'post': 'create'}), name='add_menu'),
    path('menu_list/', MenuViewSet.as_view({'get': 'list'}), name='menu_list'),
    path('restaurant/<uuid:id>/update/', UpdateView.as_view(), name='restaurant_updating'),
]