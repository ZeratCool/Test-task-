import pytest
@pytest.mark.django_db
def test_admin_functions(test_admin, clean):
    register_response = test_admin.post("/api/registration/",
                                          dict(email='ivan@me.com',
                                               username='Ivan123',
                                               password='ivan4567'))  # User registration

    restaurant_response = test_admin.post("/api/restaurant/add/", dict(name='McDonalds',
                                                                                  address='Kiltseva Road, 1, Kiev, 02000'))

    id = restaurant_response.data['id']

    updating_restaurant_response = test_admin.put(f"/api/restaurant/{id}/update/", dict(name='McDonalds',
                                                                                               address='Independence Square, 1, Kiev, 02000'))

    with open('img.png', 'rb') as image:
        creating_menu_response = test_admin.post('/api/add_menu/',
                                                   {'restaurant': id,
                                                    'image': image})

    assert register_response.status_code == 200
    assert restaurant_response.status_code == 201
    assert updating_restaurant_response.status_code == 200
    assert creating_menu_response.status_code == 201
@pytest.mark.django_db
def test_vote(test_case, test_user, clean):
    vote_response = test_user.post("/accounts/vote/", dict(restaurant=test_case))
    assert vote_response.status_code == 201

@pytest.mark.django_db
def test_voting_result(test_case, test_user, clean):


    test_user.post("/accounts/vote/", dict(restaurant=test_case))
    vote_res_response = test_user.get("/api/result/")
    assert vote_res_response.status_code == 200
    print(vote_res_response.data)

@pytest.mark.django_db
def test_menu(test_case, test_user, clean):
    menus_response = test_user.get("/api/menus/")
    assert menus_response.status_code == 200


