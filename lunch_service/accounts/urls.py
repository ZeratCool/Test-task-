from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from accounts.views import RegistrationAPIView, UserViewSet, ResultViewSet, ProfileViewSet, VoteViewSet

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationAPIView.as_view(), name='sign_up'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='users-list'),
    path('result/', ResultViewSet.as_view({'get': 'list'}), name='result'),
    path('profile/', ProfileViewSet.as_view({'get': 'retrieve'}), name='profile'),
    path('vote/', VoteViewSet.as_view({'post': 'create'}), name='voting'),
]