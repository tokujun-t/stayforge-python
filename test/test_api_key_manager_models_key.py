# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.api_key_manager_models_key import ApiKeyManagerModelsKey

class TestApiKeyManagerModelsKey(unittest.TestCase):
    """ApiKeyManagerModelsKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiKeyManagerModelsKey:
        """Test ApiKeyManagerModelsKey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiKeyManagerModelsKey`
        """
        model = ApiKeyManagerModelsKey()
        if include_optional:
            return ApiKeyManagerModelsKey(
                id = '674f7eee58103c1ed7a444eb',
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                num = '',
                effective_at = '2024-12-03T21:58:06.308548Z',
                ineffective_at = '2024-12-04T21:58:06.308580Z'
            )
        else:
            return ApiKeyManagerModelsKey(
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
        )
        """

    def testApiKeyManagerModelsKey(self):
        """Test ApiKeyManagerModelsKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
