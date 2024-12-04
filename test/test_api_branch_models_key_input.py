# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge) ![PyPI Downloads](https://img.shields.io/pypi/dm/stayforge) ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg) 

    The version of the OpenAPI document: 1.0.0
    Contact: support@stayforge.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.api_branch_models_key_input import ApiBranchModelsKeyInput

class TestApiBranchModelsKeyInput(unittest.TestCase):
    """ApiBranchModelsKeyInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiBranchModelsKeyInput:
        """Test ApiBranchModelsKeyInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiBranchModelsKeyInput`
        """
        model = ApiBranchModelsKeyInput()
        if include_optional:
            return ApiBranchModelsKeyInput(
                name = '',
                postcode = '000-0000',
                address = '000-0000',
                telephone = ''
            )
        else:
            return ApiBranchModelsKeyInput(
                name = '',
                telephone = '',
        )
        """

    def testApiBranchModelsKeyInput(self):
        """Test ApiBranchModelsKeyInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
