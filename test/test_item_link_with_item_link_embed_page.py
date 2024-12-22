# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.item_link_with_item_link_embed_page import ItemLinkWithItemLinkEmbedPage

class TestItemLinkWithItemLinkEmbedPage(unittest.TestCase):
    """ItemLinkWithItemLinkEmbedPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemLinkWithItemLinkEmbedPage:
        """Test ItemLinkWithItemLinkEmbedPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemLinkWithItemLinkEmbedPage`
        """
        model = ItemLinkWithItemLinkEmbedPage()
        if include_optional:
            return ItemLinkWithItemLinkEmbedPage(
                items = [
                    openapi_client.models.item_link_with_item_link_embed.ItemLinkWithItemLinkEmbed(
                        _embedded = openapi_client.models.item_link_embed.ItemLinkEmbed(
                            apps = {
                                'key' : openapi_client.models.item_link_embed_app.ItemLinkEmbedApp(
                                    data = null, 
                                    id = '', 
                                    type_id = '', )
                                }, 
                            constraints = [
                                null
                                ], 
                            from_workspace_id = '', 
                            to_workspace_id = '', ), 
                        from_item_id = '', 
                        from_order = 56, 
                        id = '', 
                        to_item_id = '', 
                        to_order = 56, 
                        type = 'dependency', )
                    ],
                total_items = 56
            )
        else:
            return ItemLinkWithItemLinkEmbedPage(
                total_items = 56,
        )
        """

    def testItemLinkWithItemLinkEmbedPage(self):
        """Test ItemLinkWithItemLinkEmbedPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
