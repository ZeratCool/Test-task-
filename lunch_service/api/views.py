import datetime

from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from api.models import Restaurant, Menu, Vote
from .serializers import (MenuSerializer,
                          RestaurantMenuSerializer,
                          AddRestaurantSerializer,
                          AddingMenuSerializer,
                          RestaurantSerializer)


class AddingRestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = AddRestaurantSerializer
    permission_classes = (IsAdminUser,)


class AddingMenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = AddingMenuSerializer
    lookup_field = "id"


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantMenuSerializer
    lookup_field = 'id'


class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        today = datetime.date.today()
        queryset = Menu.objects.filter(date__gte=today)
        return queryset



# class VoteViewSet(viewsets.ModelViewSet):
#     queryset = Vote.objects.all()
#     permission_classes = (IsAdminUser, )I
#     # serializer_class =
#     lookup_field = "id"
