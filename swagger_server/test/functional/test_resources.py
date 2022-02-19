

def test_product_resource(test_client, init_database):
    # response = test_client.get('/product')
    response = test_client.get('/product?category=home appliances')
    product = response.json[0]
    assert product['name'] == 'refrigerator'
    assert product['price'] == 999.99


def test_checkout_resource(new_user, test_client, init_database):
    test_client.set_cookie('localhost', 'userId', str(new_user.id))
    response = test_client.put(
        "/checkout",
        json={
            'products': [
                {
                    'productId': 1,
                    'quantity': 1
                },
                {
                    'productId': 2,
                    'quantity': 2
                }
            ]
        }
    )
    assert response.status_code == 201
    assert isinstance(response.json['checkoutId'], int)
