# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.number_field_type_settings_unit_money import NumberFieldTypeSettingsUnitMoney

class TestNumberFieldTypeSettingsUnitMoney(unittest.TestCase):
    """NumberFieldTypeSettingsUnitMoney unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NumberFieldTypeSettingsUnitMoney:
        """Test NumberFieldTypeSettingsUnitMoney
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NumberFieldTypeSettingsUnitMoney`
        """
        model = NumberFieldTypeSettingsUnitMoney()
        if include_optional:
            return NumberFieldTypeSettingsUnitMoney(
                currency = ''
            )
        else:
            return NumberFieldTypeSettingsUnitMoney(
                currency = '',
        )
        """

    def testNumberFieldTypeSettingsUnitMoney(self):
        """Test NumberFieldTypeSettingsUnitMoney"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
