# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.workspace_search_embed import WorkspaceSearchEmbed

class TestWorkspaceSearchEmbed(unittest.TestCase):
    """WorkspaceSearchEmbed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceSearchEmbed:
        """Test WorkspaceSearchEmbed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceSearchEmbed`
        """
        model = WorkspaceSearchEmbed()
        if include_optional:
            return WorkspaceSearchEmbed(
                current_permission = 'comment',
                item_count = 56,
                permissions = {
                    'key' : 'comment'
                    },
                statuses = {
                    'key' : openapi_client.models.status.Status(
                        category = 'active', 
                        color = 'blue', 
                        default = True, 
                        id = '', 
                        name = '', 
                        order = 56, 
                        workspace_id = '', )
                    }
            )
        else:
            return WorkspaceSearchEmbed(
                item_count = 56,
                permissions = {
                    'key' : 'comment'
                    },
                statuses = {
                    'key' : openapi_client.models.status.Status(
                        category = 'active', 
                        color = 'blue', 
                        default = True, 
                        id = '', 
                        name = '', 
                        order = 56, 
                        workspace_id = '', )
                    },
        )
        """

    def testWorkspaceSearchEmbed(self):
        """Test WorkspaceSearchEmbed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
