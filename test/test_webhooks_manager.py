# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.webhooks_manager import WebhooksManager

class TestWebhooksManager(unittest.TestCase):
    """WebhooksManager unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhooksManager:
        """Test WebhooksManager
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhooksManager`
        """
        model = WebhooksManager()
        if include_optional:
            return WebhooksManager(
                id = '674f7eee58103c1ed7a444eb',
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                webhook_name = '',
                endpoint = '',
                catch_path = '',
                catch_method = '',
                catch_status = 56
            )
        else:
            return WebhooksManager(
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                webhook_name = '',
                endpoint = '',
                catch_path = '',
                catch_method = '',
        )
        """

    def testWebhooksManager(self):
        """Test WebhooksManager"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
