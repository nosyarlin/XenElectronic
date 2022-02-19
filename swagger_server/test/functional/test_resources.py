

def test_product_resource(test_client, init_database):
    # response = test_client.get('/product')
    response = test_client.get('/product?category=home appliances')
    product = response.json[0]
    assert product['name'] == 'refrigerator'
    assert product['price'] == 999.99
