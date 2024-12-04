# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge) ![PyPI Downloads](https://img.shields.io/pypi/dm/stayforge) ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from stayforge.models.order import Order
from stayforge.models.stayforge import Stayforge
from typing import Optional, Set
from typing_extensions import Self

class OrderResponses(BaseModel):
    """
    OrderResponses
    """ # noqa: E501
    data: Optional[List[Order]]
    detail: Optional[StrictStr] = 'Successfully.'
    status: Optional[StrictInt] = 200
    used_time: Optional[Union[StrictFloat, StrictInt]] = None
    stayforge: Optional[Stayforge] = None
    __properties: ClassVar[List[str]] = ["data", "detail", "status", "used_time", "stayforge"]

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
        """Create an instance of OrderResponses from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of stayforge
        if self.stayforge:
            _dict['stayforge'] = self.stayforge.to_dict()
        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if used_time (nullable) is None
        # and model_fields_set contains the field
        if self.used_time is None and "used_time" in self.model_fields_set:
            _dict['used_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderResponses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [Order.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "detail": obj.get("detail") if obj.get("detail") is not None else 'Successfully.',
            "status": obj.get("status") if obj.get("status") is not None else 200,
            "used_time": obj.get("used_time"),
            "stayforge": Stayforge.from_dict(obj["stayforge"]) if obj.get("stayforge") is not None else None
        })
        return _obj


