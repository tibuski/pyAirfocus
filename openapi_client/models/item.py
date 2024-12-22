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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.item_color import ItemColor
from openapi_client.models.rich_text import RichText
from typing import Optional, Set
from typing_extensions import Self

class Item(BaseModel):
    """
    Item
    """ # noqa: E501
    archived: StrictBool
    assignee_user_ids: Optional[List[StrictStr]] = Field(default=None, alias="assigneeUserIds")
    color: ItemColor
    created_at: datetime = Field(alias="createdAt")
    description: RichText
    fields: Dict[str, Any] = Field(description="Values of custom fields, where each key is a custom-field ID and each value is a JSON-formatted value of the corresponding field.")
    id: StrictStr
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    name: StrictStr
    number: Optional[StrictInt] = None
    order: StrictInt
    status_category_updated_at: Optional[datetime] = Field(default=None, alias="statusCategoryUpdatedAt")
    status_id: StrictStr = Field(alias="statusId")
    status_updated_at: Optional[datetime] = Field(default=None, alias="statusUpdatedAt")
    workspace_id: StrictStr = Field(alias="workspaceId")
    __properties: ClassVar[List[str]] = ["archived", "assigneeUserIds", "color", "createdAt", "description", "fields", "id", "lastUpdatedAt", "name", "number", "order", "statusCategoryUpdatedAt", "statusId", "statusUpdatedAt", "workspaceId"]

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
        """Create an instance of Item from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Item from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archived": obj.get("archived"),
            "assigneeUserIds": obj.get("assigneeUserIds"),
            "color": obj.get("color"),
            "createdAt": obj.get("createdAt"),
            "description": RichText.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "fields": obj.get("fields"),
            "id": obj.get("id"),
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "name": obj.get("name"),
            "number": obj.get("number"),
            "order": obj.get("order"),
            "statusCategoryUpdatedAt": obj.get("statusCategoryUpdatedAt"),
            "statusId": obj.get("statusId"),
            "statusUpdatedAt": obj.get("statusUpdatedAt"),
            "workspaceId": obj.get("workspaceId")
        })
        return _obj


