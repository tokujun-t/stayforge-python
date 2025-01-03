# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Contact: support@stayforge.io
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
