# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_payment(self):
        """Test case for payment

        Informs server that payment has been made
        """
        response = self.client.open(
            '//checkout/{checkoutId}'.format(checkoutId=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_cart(self):
        """Test case for save_cart

        Saves cart items to database and create a checkout
        """
        products = [List[object]()]
        response = self.client.open(
            '//checkout',
            method='PUT',
            data=json.dumps(products),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search(self):
        """Test case for search

        Get products for sale
        """
        query_string = [('category', 'category_example')]
        response = self.client.open(
            '//search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
