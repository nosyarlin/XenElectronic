

def test_product_resource(test_client):
    # response = test_client.get('/product')
    response = test_client.get(
        '/search',
        query_string={'category': 'home appliances'}
    )
    product = response.json[0]
    assert product['name'] == 'refrigerator'
    assert product['price'] == 999.99


def test_checkout_resource(test_client):
    # Test put
    test_client.set_cookie('localhost', 'userId', '1')
    checkout_product_1 = {'productId': 1, 'quantity': 1}
    checkout_product_2 = {'productId': 2, 'quantity': 2}
    params = {'products': [checkout_product_1, checkout_product_2]}
    response = test_client.put("/checkout", json=params)
    assert response.status_code == 201
    assert isinstance(response.json['checkoutId'], int)

    # Test get
    resource_uri = "/checkout/{}".format(response.json['checkoutId'])
    response = test_client.get(resource_uri)
    assert response.status_code == 200
    assert response.json['userId'] == 1
    assert response.json['status'] == 'created'
    assert len(response.json['products']) == 2
    assert checkout_product_1 in response.json['products']
    assert checkout_product_2 in response.json['products']

    # test post
    response = test_client.post(resource_uri, json={'status': 'paid'})
    assert response.status_code == 200
    response = test_client.get(resource_uri)
    assert response.json['status'] == 'paid'


def test_user_resource(test_client):
    # Test login
    response = test_client.post('/login', json={
        'credentials': {
            'username': 'TestUser',
            'password': 'password'
        }
    })
    cookie = next(
        (cookie for cookie in test_client.cookie_jar if cookie.name == "userId"),
        None
    )
    assert response.status_code == 200
    assert cookie is not None
    assert cookie.value == '1'
