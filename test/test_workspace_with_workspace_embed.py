# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed

class TestWorkspaceWithWorkspaceEmbed(unittest.TestCase):
    """WorkspaceWithWorkspaceEmbed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceWithWorkspaceEmbed:
        """Test WorkspaceWithWorkspaceEmbed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceWithWorkspaceEmbed`
        """
        model = WorkspaceWithWorkspaceEmbed()
        if include_optional:
            return WorkspaceWithWorkspaceEmbed(
                embedded = openapi_client.models.workspace_embed.WorkspaceEmbed(
                    apps = {
                        'key' : openapi_client.models.app.App(
                            id = '', 
                            settings = null, 
                            team_id = '', 
                            type_id = '', )
                        }, 
                    children = [
                        openapi_client.models.workspace_embed_relation.WorkspaceEmbedRelation(
                            relation_id = '', 
                            workspace = openapi_client.models.workspace.Workspace(
                                alias = '', 
                                archived = True, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                default_permission = 'comment', 
                                description = openapi_client.models.rich_text.RichText(
                                    blocks = [
                                        null
                                        ], ), 
                                id = '', 
                                item_color = 'amber', 
                                item_type = 'bug', 
                                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                legacy_id = '', 
                                metadata = openapi_client.models.workspace_workspace_metadata.WorkspaceWorkspaceMetadata(
                                    duplicated = True, 
                                    template_id = '', 
                                    template_workspace_ref = '', 
                                    version = '', ), 
                                name = '', 
                                namespace = 'main', 
                                progress_mode = 'count', 
                                team_id = '', ), 
                            workspace_id = '', )
                        ], 
                    current_permission = 'comment', 
                    fields = {
                        'key' : null
                        }, 
                    integrations = {
                        'key' : openapi_client.models.integration_summary.IntegrationSummary(
                            capabilities = openapi_client.models.integration_capabilities.IntegrationCapabilities(
                                debug = True, 
                                hierarchy = True, 
                                push = True, 
                                sync = True, ), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '', 
                            last_sync_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_sync_state = openapi_client.models.integration_sync_state.IntegrationSyncState(
                                error_count = 56, 
                                success_count = 56, ), 
                            settings = null, 
                            type_id = '', )
                        }, 
                    item_count = 56, 
                    item_status_count = {
                        'key' : 56
                        }, 
                    item_status_count_archived = {
                        'key' : 56
                        }, 
                    parents = [
                        openapi_client.models.workspace_embed_relation.WorkspaceEmbedRelation(
                            relation_id = '', 
                            workspace_id = '', )
                        ], 
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
                    views = {
                        'key' : openapi_client.models.view.View(
                            description = '', 
                            id = '', 
                            item_filter = null, 
                            item_sort = [
                                null
                                ], 
                            name = '', 
                            order = 56, 
                            pinned_to_position = 56, 
                            private_owner_id = '', 
                            required_permission = 'comment', 
                            settings = null, 
                            type_id = '', 
                            workspace_id = '', )
                        }, ),
                alias = '',
                archived = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                default_permission = 'comment',
                description = openapi_client.models.rich_text.RichText(
                    blocks = [
                        null
                        ], ),
                id = '',
                item_color = 'amber',
                item_type = 'bug',
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                legacy_id = '',
                metadata = openapi_client.models.workspace_workspace_metadata.WorkspaceWorkspaceMetadata(
                    duplicated = True, 
                    template_id = '', 
                    template_workspace_ref = '', 
                    version = '', ),
                name = '',
                namespace = 'main',
                progress_mode = 'count',
                team_id = ''
            )
        else:
            return WorkspaceWithWorkspaceEmbed(
                embedded = openapi_client.models.workspace_embed.WorkspaceEmbed(
                    apps = {
                        'key' : openapi_client.models.app.App(
                            id = '', 
                            settings = null, 
                            team_id = '', 
                            type_id = '', )
                        }, 
                    children = [
                        openapi_client.models.workspace_embed_relation.WorkspaceEmbedRelation(
                            relation_id = '', 
                            workspace = openapi_client.models.workspace.Workspace(
                                alias = '', 
                                archived = True, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                default_permission = 'comment', 
                                description = openapi_client.models.rich_text.RichText(
                                    blocks = [
                                        null
                                        ], ), 
                                id = '', 
                                item_color = 'amber', 
                                item_type = 'bug', 
                                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                legacy_id = '', 
                                metadata = openapi_client.models.workspace_workspace_metadata.WorkspaceWorkspaceMetadata(
                                    duplicated = True, 
                                    template_id = '', 
                                    template_workspace_ref = '', 
                                    version = '', ), 
                                name = '', 
                                namespace = 'main', 
                                progress_mode = 'count', 
                                team_id = '', ), 
                            workspace_id = '', )
                        ], 
                    current_permission = 'comment', 
                    fields = {
                        'key' : null
                        }, 
                    integrations = {
                        'key' : openapi_client.models.integration_summary.IntegrationSummary(
                            capabilities = openapi_client.models.integration_capabilities.IntegrationCapabilities(
                                debug = True, 
                                hierarchy = True, 
                                push = True, 
                                sync = True, ), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '', 
                            last_sync_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_sync_state = openapi_client.models.integration_sync_state.IntegrationSyncState(
                                error_count = 56, 
                                success_count = 56, ), 
                            settings = null, 
                            type_id = '', )
                        }, 
                    item_count = 56, 
                    item_status_count = {
                        'key' : 56
                        }, 
                    item_status_count_archived = {
                        'key' : 56
                        }, 
                    parents = [
                        openapi_client.models.workspace_embed_relation.WorkspaceEmbedRelation(
                            relation_id = '', 
                            workspace_id = '', )
                        ], 
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
                    views = {
                        'key' : openapi_client.models.view.View(
                            description = '', 
                            id = '', 
                            item_filter = null, 
                            item_sort = [
                                null
                                ], 
                            name = '', 
                            order = 56, 
                            pinned_to_position = 56, 
                            private_owner_id = '', 
                            required_permission = 'comment', 
                            settings = null, 
                            type_id = '', 
                            workspace_id = '', )
                        }, ),
                archived = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = openapi_client.models.rich_text.RichText(
                    blocks = [
                        null
                        ], ),
                id = '',
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                namespace = 'main',
                progress_mode = 'count',
                team_id = '',
        )
        """

    def testWorkspaceWithWorkspaceEmbed(self):
        """Test WorkspaceWithWorkspaceEmbed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
