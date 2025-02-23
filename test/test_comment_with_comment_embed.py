# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.comment_with_comment_embed import CommentWithCommentEmbed

class TestCommentWithCommentEmbed(unittest.TestCase):
    """CommentWithCommentEmbed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommentWithCommentEmbed:
        """Test CommentWithCommentEmbed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommentWithCommentEmbed`
        """
        model = CommentWithCommentEmbed()
        if include_optional:
            return CommentWithCommentEmbed(
                embedded = openapi_client.models.comment_embed.CommentEmbed(),
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
                user_id = ''
            )
        else:
            return CommentWithCommentEmbed(
                embedded = openapi_client.models.comment_embed.CommentEmbed(),
                content = openapi_client.models.rich_text.RichText(
                    blocks = [
                        null
                        ], ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                item_id = '',
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user_id = '',
        )
        """

    def testCommentWithCommentEmbed(self):
        """Test CommentWithCommentEmbed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
