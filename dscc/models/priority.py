# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Priority(str, Enum):
    """
    Priority of the task for promoting the snapshot. Defualts to PRIORITYTYPE_MED.
    """

    """
    allowed enum values
    """
    PRIORITYTYPE_HIGH = 'PRIORITYTYPE_HIGH'
    PRIORITYTYPE_MED = 'PRIORITYTYPE_MED'
    PRIORITYTYPE_LOW = 'PRIORITYTYPE_LOW'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Priority from a JSON string"""
        return cls(json.loads(json_str))


