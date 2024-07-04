import datetime

from rest_framework import generics, viewsets, status
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import UserData
from accounts.serializers import RegistrationSerializer, TotalUsersSerializer, ResultSerializer, VoteSerializer
from api.models import Vote


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()

    serializer_class = TotalUsersSerializer
    permission_classes = (IsAdminUser,)

class ResultViewSet(viewsets.ModelViewSet):
    today = datetime.date.today()
    serializer_class = ResultSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        today = datetime.date.today()
        queryset = Vote.objects.filter(date=today)
        return queryset


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_object(self):
        return self.request.user


class VoteViewSet(viewsets.ModelViewSet):
    today = datetime.date.today()
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    lookup_field = "id"
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)