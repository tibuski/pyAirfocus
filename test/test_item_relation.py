# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.item_relation import ItemRelation

class TestItemRelation(unittest.TestCase):
    """ItemRelation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemRelation:
        """Test ItemRelation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemRelation`
        """
        model = ItemRelation()
        if include_optional:
            return ItemRelation(
                child_id = '',
                child_order = 56,
                id = '',
                parent_id = '',
                parent_order = 56
            )
        else:
            return ItemRelation(
                child_id = '',
                child_order = 56,
                id = '',
                parent_id = '',
                parent_order = 56,
        )
        """

    def testItemRelation(self):
        """Test ItemRelation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
