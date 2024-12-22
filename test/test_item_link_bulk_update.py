# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.item_link_bulk_update import ItemLinkBulkUpdate

class TestItemLinkBulkUpdate(unittest.TestCase):
    """ItemLinkBulkUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemLinkBulkUpdate:
        """Test ItemLinkBulkUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemLinkBulkUpdate`
        """
        model = ItemLinkBulkUpdate()
        if include_optional:
            return ItemLinkBulkUpdate(
                id = '',
                resource = openapi_client.models.item_link.ItemLink(
                    from_item_id = '', 
                    from_order = 56, 
                    id = '', 
                    to_item_id = '', 
                    to_order = 56, 
                    type = 'dependency', ),
                type = 'update'
            )
        else:
            return ItemLinkBulkUpdate(
                id = '',
                resource = openapi_client.models.item_link.ItemLink(
                    from_item_id = '', 
                    from_order = 56, 
                    id = '', 
                    to_item_id = '', 
                    to_order = 56, 
                    type = 'dependency', ),
                type = 'update',
        )
        """

    def testItemLinkBulkUpdate(self):
        """Test ItemLinkBulkUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
