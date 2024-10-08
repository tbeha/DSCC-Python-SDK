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


class DeviceType4enclosureType(str, Enum):
    """
    Enclosure Type. `Filter, Sort`
    """

    """
    allowed enum values
    """
    ENCLOSURE_UNKNOWN = 'ENCLOSURE_UNKNOWN'
    ENCLOSURE_DC0 = 'ENCLOSURE_DC0'
    ENCLOSURE_DC1 = 'ENCLOSURE_DC1'
    ENCLOSURE_DC2 = 'ENCLOSURE_DC2'
    ENCLOSURE_DC3 = 'ENCLOSURE_DC3'
    ENCLOSURE_DC4 = 'ENCLOSURE_DC4'
    ENCLOSURE_DCS1 = 'ENCLOSURE_DCS1'
    ENCLOSURE_DCS2 = 'ENCLOSURE_DCS2'
    ENCLOSURE_DCN1 = 'ENCLOSURE_DCN1'
    ENCLOSURE_DCS3 = 'ENCLOSURE_DCS3'
    ENCLOSURE_DCS4 = 'ENCLOSURE_DCS4'
    ENCLOSURE_DCS5 = 'ENCLOSURE_DCS5'
    ENCLOSURE_DCS6 = 'ENCLOSURE_DCS6'
    ENCLOSURE_DCS7 = 'ENCLOSURE_DCS7'
    ENCLOSURE_DCS8 = 'ENCLOSURE_DCS8'
    ENCLOSURE_DCN2 = 'ENCLOSURE_DCN2'
    ENCLOSURE_DCN3 = 'ENCLOSURE_DCN3'
    ENCLOSURE_DCN4 = 'ENCLOSURE_DCN4'
    ENCLOSURE_DCS9 = 'ENCLOSURE_DCS9'
    ENCLOSURE_DCS10 = 'ENCLOSURE_DCS10'
    ENCLOSURE_DCS11 = 'ENCLOSURE_DCS11'
    ENCLOSURE_DCN5 = 'ENCLOSURE_DCN5'
    ENCLOSURE_DCS12 = 'ENCLOSURE_DCS12'
    ENCLOSURE_DCN6 = 'ENCLOSURE_DCN6'
    ENCLOSURE_DCN7 = 'ENCLOSURE_DCN7'
    ENCLOSURE_DCF1 = 'ENCLOSURE_DCF1'
    ENCLOSURE_DCF2 = 'ENCLOSURE_DCF2'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeviceType4enclosureType from a JSON string"""
        return cls(json.loads(json_str))


