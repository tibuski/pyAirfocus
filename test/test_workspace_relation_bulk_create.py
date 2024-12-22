# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.workspace_relation_bulk_create import WorkspaceRelationBulkCreate

class TestWorkspaceRelationBulkCreate(unittest.TestCase):
    """WorkspaceRelationBulkCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceRelationBulkCreate:
        """Test WorkspaceRelationBulkCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceRelationBulkCreate`
        """
        model = WorkspaceRelationBulkCreate()
        if include_optional:
            return WorkspaceRelationBulkCreate(
                resource = openapi_client.models.workspace_relation.WorkspaceRelation(
                    child_id = '', 
                    id = '', 
                    parent_id = '', ),
                type = 'create'
            )
        else:
            return WorkspaceRelationBulkCreate(
                resource = openapi_client.models.workspace_relation.WorkspaceRelation(
                    child_id = '', 
                    id = '', 
                    parent_id = '', ),
                type = 'create',
        )
        """

    def testWorkspaceRelationBulkCreate(self):
        """Test WorkspaceRelationBulkCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
