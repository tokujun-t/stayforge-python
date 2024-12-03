# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.room_type_input import RoomTypeInput

class TestRoomTypeInput(unittest.TestCase):
    """RoomTypeInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoomTypeInput:
        """Test RoomTypeInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoomTypeInput`
        """
        model = RoomTypeInput()
        if include_optional:
            return RoomTypeInput(
                name = '',
                description = '',
                price = None,
                price_policy = '',
                price_max = None,
                price_min = None
            )
        else:
            return RoomTypeInput(
                name = '',
                price = None,
                price_min = None,
        )
        """

    def testRoomTypeInput(self):
        """Test RoomTypeInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
