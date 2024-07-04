import pytest
from rest_framework.test import APIClient
from accounts.models import UserData
import os
from lunch_service import settings


client = APIClient()

@pytest.fixture
def test_admin():
    admin = UserData.objects.create_user(email='admin@test.com',
                                         username='admin_test',
                                         password='admin_test', is_staff=True, is_superuser=True)
    token_responce = client.post('/accounts/login/', dict(email='admin@test.com',
                                                                password='admin_test'))
    admin_token = token_responce.data['access']
    client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(admin_token))
    return client


@pytest.fixture
def test_user():
    token_responce = client.post('/accounts/login/', dict(email='test@gmail.com',
                                                                password='test'))
    user_token = token_responce.data['access']
    client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(user_token))
    return client

@pytest.fixture
def test_case():
    UserData.objects.create_user(email='admin@test.com', password='admin',
                                         is_staff=True, is_superuser=True)
    token = client.post('/accounts/login/', dict(email='admin@test.com', password='test'))

    client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token))

    client.post('/accounts/register/', dict(email='testuser@test.com', password='test', username='test_user'))


    create_restaurant = client.post('/restaurants/add/', dict(name='test_restaurant', address='test_address',))

    id = create_restaurant.data['id']

    with open('img.png', 'rb') as image:
        client.post('api/add_menu/', {'restaurant': id, 'image': image} )

    return id
@pytest.fixture
def clean():
    for months, days, images in os.walk(settings.MEDIA_ROOT + settings.MEDIA_URL + "files/"):
        for image in images:
            if str(image).startswith("test_image"):
                os.remove(months + "/" + image)
            if len(os.listdir(months)) == 0:
                os.rmdir(months)
