# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.field_server_endpoints_install_field_request import FieldServerEndpointsInstallFieldRequest

class TestFieldServerEndpointsInstallFieldRequest(unittest.TestCase):
    """FieldServerEndpointsInstallFieldRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FieldServerEndpointsInstallFieldRequest:
        """Test FieldServerEndpointsInstallFieldRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FieldServerEndpointsInstallFieldRequest`
        """
        model = FieldServerEndpointsInstallFieldRequest()
        if include_optional:
            return FieldServerEndpointsInstallFieldRequest(
                description = '',
                is_team_field = True,
                name = '',
                type_id = '',
                workspace_ids = [
                    ''
                    ],
                settings = None
            )
        else:
            return FieldServerEndpointsInstallFieldRequest(
                name = '',
                type_id = '',
                settings = None,
        )
        """

    def testFieldServerEndpointsInstallFieldRequest(self):
        """Test FieldServerEndpointsInstallFieldRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
