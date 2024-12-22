# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.item_with_item_embed import ItemWithItemEmbed

class TestItemWithItemEmbed(unittest.TestCase):
    """ItemWithItemEmbed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemWithItemEmbed:
        """Test ItemWithItemEmbed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemWithItemEmbed`
        """
        model = ItemWithItemEmbed()
        if include_optional:
            return ItemWithItemEmbed(
                embedded = openapi_client.models.item_embed.ItemEmbed(
                    alias = '', 
                    apps = {
                        'key' : openapi_client.models.item_embed_app.ItemEmbedApp(
                            data = null, 
                            id = '', 
                            type_id = '', )
                        }, 
                    attachment_count = 56, 
                    children = [
                        openapi_client.models.item_embed_relative_item.ItemEmbedRelativeItem(
                            alias = '', 
                            child_order = 56, 
                            item = openapi_client.models.item.Item(
                                archived = True, 
                                assignee_user_ids = [
                                    ''
                                    ], 
                                color = 'amber', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                description = openapi_client.models.rich_text.RichText(
                                    blocks = [
                                        null
                                        ], ), 
                                fields = {
                                    'key' : null
                                    }, 
                                id = '', 
                                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '', 
                                number = 56, 
                                order = 56, 
                                status_category_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                status_id = '', 
                                status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                workspace_id = '', ), 
                            item_id = '', 
                            item_type = 'bug', 
                            parent_order = 56, 
                            relation_id = '', 
                            workspace_id = '', )
                        ], 
                    comment_count = 56, 
                    constraints = [
                        null
                        ], 
                    integration = openapi_client.models.item_embed_integration.ItemEmbedIntegration(
                        data = null, 
                        id = '', 
                        type_id = '', ), 
                    link_count = 56, 
                    parents = [
                        openapi_client.models.item_embed_relative_item.ItemEmbedRelativeItem(
                            alias = '', 
                            child_order = 56, 
                            item_id = '', 
                            parent_order = 56, 
                            relation_id = '', 
                            workspace_id = '', )
                        ], 
                    progress = openapi_client.models.item_embed_progress.ItemEmbedProgress(
                        closed = 56, 
                        total = 56, ), 
                    watched = True, 
                    workspace_item_type = 'bug', ),
                archived = True,
                assignee_user_ids = [
                    ''
                    ],
                color = 'amber',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = openapi_client.models.rich_text.RichText(
                    blocks = [
                        null
                        ], ),
                fields = {
                    'key' : null
                    },
                id = '',
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                number = 56,
                order = 56,
                status_category_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status_id = '',
                status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                workspace_id = ''
            )
        else:
            return ItemWithItemEmbed(
                embedded = openapi_client.models.item_embed.ItemEmbed(
                    alias = '', 
                    apps = {
                        'key' : openapi_client.models.item_embed_app.ItemEmbedApp(
                            data = null, 
                            id = '', 
                            type_id = '', )
                        }, 
                    attachment_count = 56, 
                    children = [
                        openapi_client.models.item_embed_relative_item.ItemEmbedRelativeItem(
                            alias = '', 
                            child_order = 56, 
                            item = openapi_client.models.item.Item(
                                archived = True, 
                                assignee_user_ids = [
                                    ''
                                    ], 
                                color = 'amber', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                description = openapi_client.models.rich_text.RichText(
                                    blocks = [
                                        null
                                        ], ), 
                                fields = {
                                    'key' : null
                                    }, 
                                id = '', 
                                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '', 
                                number = 56, 
                                order = 56, 
                                status_category_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                status_id = '', 
                                status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                workspace_id = '', ), 
                            item_id = '', 
                            item_type = 'bug', 
                            parent_order = 56, 
                            relation_id = '', 
                            workspace_id = '', )
                        ], 
                    comment_count = 56, 
                    constraints = [
                        null
                        ], 
                    integration = openapi_client.models.item_embed_integration.ItemEmbedIntegration(
                        data = null, 
                        id = '', 
                        type_id = '', ), 
                    link_count = 56, 
                    parents = [
                        openapi_client.models.item_embed_relative_item.ItemEmbedRelativeItem(
                            alias = '', 
                            child_order = 56, 
                            item_id = '', 
                            parent_order = 56, 
                            relation_id = '', 
                            workspace_id = '', )
                        ], 
                    progress = openapi_client.models.item_embed_progress.ItemEmbedProgress(
                        closed = 56, 
                        total = 56, ), 
                    watched = True, 
                    workspace_item_type = 'bug', ),
                archived = True,
                color = 'amber',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = openapi_client.models.rich_text.RichText(
                    blocks = [
                        null
                        ], ),
                fields = {
                    'key' : null
                    },
                id = '',
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                order = 56,
                status_id = '',
                workspace_id = '',
        )
        """

    def testItemWithItemEmbed(self):
        """Test ItemWithItemEmbed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
