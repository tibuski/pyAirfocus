# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.workspace_group_bulk_update import WorkspaceGroupBulkUpdate

class TestWorkspaceGroupBulkUpdate(unittest.TestCase):
    """WorkspaceGroupBulkUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceGroupBulkUpdate:
        """Test WorkspaceGroupBulkUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceGroupBulkUpdate`
        """
        model = WorkspaceGroupBulkUpdate()
        if include_optional:
            return WorkspaceGroupBulkUpdate(
                id = '',
                resource = openapi_client.models.workspace_group.WorkspaceGroup(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    default_permission = 'comment', 
                    id = '', 
                    last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    team_id = '', ),
                type = 'update'
            )
        else:
            return WorkspaceGroupBulkUpdate(
                id = '',
                resource = openapi_client.models.workspace_group.WorkspaceGroup(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    default_permission = 'comment', 
                    id = '', 
                    last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    team_id = '', ),
                type = 'update',
        )
        """

    def testWorkspaceGroupBulkUpdate(self):
        """Test WorkspaceGroupBulkUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
