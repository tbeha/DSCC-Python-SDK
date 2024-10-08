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


class DeviceType4SYSTEMLEDSINGLE(str, Enum):
    """
    LED state.
    """

    """
    allowed enum values
    """
    LED_UNKNOWN = 'LED_UNKNOWN'
    LED_OFF = 'LED_OFF'
    LED_GREEN = 'LED_GREEN'
    LED_GREEN_BLNK = 'LED_GREEN_BLNK'
    LED_AMBER = 'LED_AMBER'
    LED_AMBER_BLNK = 'LED_AMBER_BLNK'
    LED_BLUE = 'LED_BLUE'
    LED_BLUE_BLNK = 'LED_BLUE_BLNK'
    NULL = 'null'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeviceType4SYSTEMLEDSINGLE from a JSON string"""
        return cls(json.loads(json_str))


