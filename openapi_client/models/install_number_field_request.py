# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.number_field_type_settings import NumberFieldTypeSettings
from typing import Optional, Set
from typing_extensions import Self

class InstallNumberFieldRequest(BaseModel):
    """
    InstallNumberFieldRequest
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default='', description="User-readable field description.")
    is_team_field: Optional[StrictBool] = Field(default=False, description="Whether the field should be installed as a team-field or a workspace-specific field.", alias="isTeamField")
    name: StrictStr = Field(description="User-readable field name.")
    settings: NumberFieldTypeSettings = Field(description="Field settings.")
    type_id: StrictStr = Field(alias="typeId")
    workspace_ids: Optional[List[StrictStr]] = Field(default=None, description="If isTeamField=false then exactly one workspace ID should be provided. If isTeamField=true then any amount of workspace IDs can be provided to be linked to the newly installed field.", alias="workspaceIds")
    __properties: ClassVar[List[str]] = ["description", "isTeamField", "name", "settings", "typeId", "workspaceIds"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of InstallNumberFieldRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InstallNumberFieldRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description") if obj.get("description") is not None else '',
            "isTeamField": obj.get("isTeamField") if obj.get("isTeamField") is not None else False,
            "name": obj.get("name"),
            "settings": NumberFieldTypeSettings.from_dict(obj["settings"]) if obj.get("settings") is not None else None,
            "typeId": obj.get("typeId"),
            "workspaceIds": obj.get("workspaceIds")
        })
        return _obj


