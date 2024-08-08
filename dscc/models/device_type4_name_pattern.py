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


class DeviceType4NamePattern(str, Enum):
    """
    name pattern
    """

    """
    allowed enum values
    """
    PARENT_TIMESTAMP = 'PARENT_TIMESTAMP'
    PARENT_SEC_SINCE_EPOCH = 'PARENT_SEC_SINCE_EPOCH'
    CUSTOM = 'CUSTOM'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeviceType4NamePattern from a JSON string"""
        return cls(json.loads(json_str))


