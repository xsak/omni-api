import connexion
import six
from swagger_server.models.apiresponse import Apiresponse

from swagger_server.models.rekettye import Rekettye  # noqa: E501
from swagger_server import util


def alma_fun(body=None):  # noqa: E501
    """Create a new planet

    Create new planet object # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    print(f"body: {type(body)}")
    if connexion.request.is_json:
        rekettye = Rekettye.from_dict(connexion.request.get_json())  # noqa: E501
    print(f"body: {type(body)}")
    return Apiresponse(rekettye,42)


def create_post(body=None):  # noqa: E501
    """Create a new planet

    Create new planet object # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
