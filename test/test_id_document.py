# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.id_document import IDDocument

class TestIDDocument(unittest.TestCase):
    """IDDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IDDocument:
        """Test IDDocument
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IDDocument`
        """
        model = IDDocument()
        if include_optional:
            return IDDocument(
                mrz = '',
                photocopy = None
            )
        else:
            return IDDocument(
        )
        """

    def testIDDocument(self):
        """Test IDDocument"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
