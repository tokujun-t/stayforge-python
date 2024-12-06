# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from apis.key_manager_api import KeyManagerApi


class TestKeyManagerApi(unittest.TestCase):
    """KeyManagerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = KeyManagerApi()

    def tearDown(self) -> None:
        pass

    def test_create_key_api_key_post(self) -> None:
        """Test case for create_key_api_key_post

        Create Key
        """
        pass

    def test_delete_key_api_key_id_delete(self) -> None:
        """Test case for delete_key_api_key_id_delete

        Delete Key
        """
        pass

    def test_get_key_api_key_id_get(self) -> None:
        """Test case for get_key_api_key_id_get

        Get Key
        """
        pass

    def test_get_key_by_num_api_key_num_num_get(self) -> None:
        """Test case for get_key_by_num_api_key_num_num_get

        Get Key By Num
        """
        pass

    def test_put_key_api_key_id_put(self) -> None:
        """Test case for put_key_api_key_id_put

        Put Key
        """
        pass


if __name__ == '__main__':
    unittest.main()
