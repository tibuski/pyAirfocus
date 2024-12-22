# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.comment_bulk_action import CommentBulkAction

class TestCommentBulkAction(unittest.TestCase):
    """CommentBulkAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommentBulkAction:
        """Test CommentBulkAction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommentBulkAction`
        """
        model = CommentBulkAction()
        if include_optional:
            return CommentBulkAction(
                resource = openapi_client.models.comment.Comment(
                    content = openapi_client.models.rich_text.RichText(
                        blocks = [
                            null
                            ], ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    item_id = '', 
                    last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    reactions = [
                        openapi_client.models.comment_reaction.CommentReaction(
                            emoji = 'blue_heart', 
                            user_ids = [
                                ''
                                ], )
                        ], 
                    user_id = '', ),
                type = 'create',
                id = '',
                transform = [
                    null
                    ]
            )
        else:
            return CommentBulkAction(
                resource = openapi_client.models.comment.Comment(
                    content = openapi_client.models.rich_text.RichText(
                        blocks = [
                            null
                            ], ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    item_id = '', 
                    last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    reactions = [
                        openapi_client.models.comment_reaction.CommentReaction(
                            emoji = 'blue_heart', 
                            user_ids = [
                                ''
                                ], )
                        ], 
                    user_id = '', ),
                type = 'create',
                id = '',
                transform = [
                    null
                    ],
        )
        """

    def testCommentBulkAction(self):
        """Test CommentBulkAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
