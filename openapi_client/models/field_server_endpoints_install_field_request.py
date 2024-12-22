# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.install_boolean_field_request import InstallBooleanFieldRequest
from openapi_client.models.install_date_field_request import InstallDateFieldRequest
from openapi_client.models.install_date_range_field_request import InstallDateRangeFieldRequest
from openapi_client.models.install_number_field_request import InstallNumberFieldRequest
from openapi_client.models.install_people_field_request import InstallPeopleFieldRequest
from openapi_client.models.install_select_field_request import InstallSelectFieldRequest
from openapi_client.models.install_text_field_request import InstallTextFieldRequest
from openapi_client.models.install_time_period_field_request import InstallTimePeriodFieldRequest
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

FIELDSERVERENDPOINTSINSTALLFIELDREQUEST_ONE_OF_SCHEMAS = ["InstallBooleanFieldRequest", "InstallDateFieldRequest", "InstallDateRangeFieldRequest", "InstallNumberFieldRequest", "InstallPeopleFieldRequest", "InstallSelectFieldRequest", "InstallTextFieldRequest", "InstallTimePeriodFieldRequest"]

class FieldServerEndpointsInstallFieldRequest(BaseModel):
    """
    FieldServerEndpointsInstallFieldRequest
    """
    # data type: InstallBooleanFieldRequest
    oneof_schema_1_validator: Optional[InstallBooleanFieldRequest] = None
    # data type: InstallDateFieldRequest
    oneof_schema_2_validator: Optional[InstallDateFieldRequest] = None
    # data type: InstallDateRangeFieldRequest
    oneof_schema_3_validator: Optional[InstallDateRangeFieldRequest] = None
    # data type: InstallNumberFieldRequest
    oneof_schema_4_validator: Optional[InstallNumberFieldRequest] = None
    # data type: InstallPeopleFieldRequest
    oneof_schema_5_validator: Optional[InstallPeopleFieldRequest] = None
    # data type: InstallSelectFieldRequest
    oneof_schema_6_validator: Optional[InstallSelectFieldRequest] = None
    # data type: InstallTextFieldRequest
    oneof_schema_7_validator: Optional[InstallTextFieldRequest] = None
    # data type: InstallTimePeriodFieldRequest
    oneof_schema_8_validator: Optional[InstallTimePeriodFieldRequest] = None
    actual_instance: Optional[Union[InstallBooleanFieldRequest, InstallDateFieldRequest, InstallDateRangeFieldRequest, InstallNumberFieldRequest, InstallPeopleFieldRequest, InstallSelectFieldRequest, InstallTextFieldRequest, InstallTimePeriodFieldRequest]] = None
    one_of_schemas: Set[str] = { "InstallBooleanFieldRequest", "InstallDateFieldRequest", "InstallDateRangeFieldRequest", "InstallNumberFieldRequest", "InstallPeopleFieldRequest", "InstallSelectFieldRequest", "InstallTextFieldRequest", "InstallTimePeriodFieldRequest" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = FieldServerEndpointsInstallFieldRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: InstallBooleanFieldRequest
        if not isinstance(v, InstallBooleanFieldRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InstallBooleanFieldRequest`")
        else:
            match += 1
        # validate data type: InstallDateFieldRequest
        if not isinstance(v, InstallDateFieldRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InstallDateFieldRequest`")
        else:
            match += 1
        # validate data type: InstallDateRangeFieldRequest
        if not isinstance(v, InstallDateRangeFieldRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InstallDateRangeFieldRequest`")
        else:
            match += 1
        # validate data type: InstallNumberFieldRequest
        if not isinstance(v, InstallNumberFieldRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InstallNumberFieldRequest`")
        else:
            match += 1
        # validate data type: InstallPeopleFieldRequest
        if not isinstance(v, InstallPeopleFieldRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InstallPeopleFieldRequest`")
        else:
            match += 1
        # validate data type: InstallSelectFieldRequest
        if not isinstance(v, InstallSelectFieldRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InstallSelectFieldRequest`")
        else:
            match += 1
        # validate data type: InstallTextFieldRequest
        if not isinstance(v, InstallTextFieldRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InstallTextFieldRequest`")
        else:
            match += 1
        # validate data type: InstallTimePeriodFieldRequest
        if not isinstance(v, InstallTimePeriodFieldRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InstallTimePeriodFieldRequest`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in FieldServerEndpointsInstallFieldRequest with oneOf schemas: InstallBooleanFieldRequest, InstallDateFieldRequest, InstallDateRangeFieldRequest, InstallNumberFieldRequest, InstallPeopleFieldRequest, InstallSelectFieldRequest, InstallTextFieldRequest, InstallTimePeriodFieldRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in FieldServerEndpointsInstallFieldRequest with oneOf schemas: InstallBooleanFieldRequest, InstallDateFieldRequest, InstallDateRangeFieldRequest, InstallNumberFieldRequest, InstallPeopleFieldRequest, InstallSelectFieldRequest, InstallTextFieldRequest, InstallTimePeriodFieldRequest. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into InstallBooleanFieldRequest
        try:
            instance.actual_instance = InstallBooleanFieldRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InstallDateFieldRequest
        try:
            instance.actual_instance = InstallDateFieldRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InstallDateRangeFieldRequest
        try:
            instance.actual_instance = InstallDateRangeFieldRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InstallNumberFieldRequest
        try:
            instance.actual_instance = InstallNumberFieldRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InstallPeopleFieldRequest
        try:
            instance.actual_instance = InstallPeopleFieldRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InstallSelectFieldRequest
        try:
            instance.actual_instance = InstallSelectFieldRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InstallTextFieldRequest
        try:
            instance.actual_instance = InstallTextFieldRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InstallTimePeriodFieldRequest
        try:
            instance.actual_instance = InstallTimePeriodFieldRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into FieldServerEndpointsInstallFieldRequest with oneOf schemas: InstallBooleanFieldRequest, InstallDateFieldRequest, InstallDateRangeFieldRequest, InstallNumberFieldRequest, InstallPeopleFieldRequest, InstallSelectFieldRequest, InstallTextFieldRequest, InstallTimePeriodFieldRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FieldServerEndpointsInstallFieldRequest with oneOf schemas: InstallBooleanFieldRequest, InstallDateFieldRequest, InstallDateRangeFieldRequest, InstallNumberFieldRequest, InstallPeopleFieldRequest, InstallSelectFieldRequest, InstallTextFieldRequest, InstallTimePeriodFieldRequest. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], InstallBooleanFieldRequest, InstallDateFieldRequest, InstallDateRangeFieldRequest, InstallNumberFieldRequest, InstallPeopleFieldRequest, InstallSelectFieldRequest, InstallTextFieldRequest, InstallTimePeriodFieldRequest]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


