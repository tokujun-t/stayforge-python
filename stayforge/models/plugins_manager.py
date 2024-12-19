# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Contact: support@stayforge.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PluginsManager(BaseModel):
    """
    PluginsManager
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default='6764296424e87a8e05b788c1', description="Reference ID of the key.")
    create_at: Optional[datetime]
    update_at: Optional[datetime] = None
    plugin: StrictStr = Field(description="The host URL of the plugin. This is used to generate webhook URLs and other plugin-related paths.")
    plugin_version: Optional[StrictStr] = Field(default='latest', description="The version of the plugin. This helps in tracking updates and ensuring compatibility.")
    local_name: Optional[StrictStr] = None
    permissions: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["id", "create_at", "update_at", "plugin", "plugin_version", "local_name", "permissions"]

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
        """Create an instance of PluginsManager from a JSON string"""
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
        # set to None if create_at (nullable) is None
        # and model_fields_set contains the field
        if self.create_at is None and "create_at" in self.model_fields_set:
            _dict['create_at'] = None

        # set to None if update_at (nullable) is None
        # and model_fields_set contains the field
        if self.update_at is None and "update_at" in self.model_fields_set:
            _dict['update_at'] = None

        # set to None if local_name (nullable) is None
        # and model_fields_set contains the field
        if self.local_name is None and "local_name" in self.model_fields_set:
            _dict['local_name'] = None

        # set to None if permissions (nullable) is None
        # and model_fields_set contains the field
        if self.permissions is None and "permissions" in self.model_fields_set:
            _dict['permissions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PluginsManager from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id") if obj.get("id") is not None else '6764296424e87a8e05b788c1',
            "create_at": obj.get("create_at"),
            "update_at": obj.get("update_at"),
            "plugin": obj.get("plugin"),
            "plugin_version": obj.get("plugin_version") if obj.get("plugin_version") is not None else 'latest',
            "local_name": obj.get("local_name"),
            "permissions": obj.get("permissions")
        })
        return _obj


