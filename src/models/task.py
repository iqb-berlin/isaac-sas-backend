# coding: utf-8

"""
    Coding-Service-API

    Coding-Service-API

    The version of the OpenAPI document: 0.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from models.data_chunk import DataChunk
from models.task_events_inner import TaskEventsInner
from models.task_instructions import TaskInstructions
from models.task_type import TaskType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Task(BaseModel):
    """
    Task
    """ # noqa: E501
    id: StrictStr
    label: StrictStr
    type: TaskType
    events: List[TaskEventsInner]
    instructions: Optional[TaskInstructions] = None
    data: List[DataChunk]
    __properties: ClassVar[List[str]] = ["id", "label", "type", "events", "instructions", "data"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Task from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['events'] = _items
        # override the default output from pydantic by calling `to_dict()` of instructions
        if self.instructions:
            _dict['instructions'] = self.instructions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Task from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "type": obj.get("type"),
            "events": [TaskEventsInner.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None,
            "instructions": TaskInstructions.from_dict(obj.get("instructions")) if obj.get("instructions") is not None else None,
            "data": [DataChunk.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None
        })
        return _obj


