import connexion
import six

from swagger_server import util


def payment(checkoutId):  # noqa: E501
    """Informs server that payment has been made

     # noqa: E501

    :param checkoutId: The order to pay for
    :type checkoutId: int

    :rtype: None
    """
    return 'do some magic!'


def save_cart(products):  # noqa: E501
    """Saves cart items to database and create a checkout

    Saves what items this user is purchasing alongside the quantity of each item # noqa: E501

    :param products: The checkout to create
    :type products: List[]

    :rtype: object
    """
    return 'do some magic!'


def search(category=None):  # noqa: E501
    """Get products for sale

    Searches for products matching given filters. # noqa: E501

    :param category: category of products for filter; repeated
    :type category: str

    :rtype: List[object]
    """
    return 'do some magic!'
