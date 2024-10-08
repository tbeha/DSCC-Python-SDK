# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.common_resource_attributes import CommonResourceAttributes
from dscc.models.device_type4_certificate_details_enddate import DeviceType4CertificateDetailsEnddate
from dscc.models.device_type4_certificate_details_startdate import DeviceType4CertificateDetailsStartdate
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4CertificateDetails(BaseModel):
    """
    DeviceType4CertificateDetails
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    cert_type: Optional[StrictStr] = Field(default=None, description="Type of array certificate", alias="certType")
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    commonname: Optional[StrictStr] = Field(default=None, description="Commonname of the resource")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object ", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="The customer application identifier", alias="customerId")
    displayname: Optional[StrictStr] = Field(default=None, description="Displayname of the resource")
    domain: Optional[StrictStr] = Field(default=None, description="Domain of the resource")
    enddate: Optional[DeviceType4CertificateDetailsEnddate] = None
    fingerprint: Optional[StrictStr] = Field(default=None, description="Fingerprint of the resource")
    generation: Optional[StrictInt] = Field(default=None, description="A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource")
    issuer: Optional[StrictStr] = Field(default=None, description="Issuer of the resource")
    pem: Optional[StrictStr] = Field(default=None, description="array certificate pem")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed certificate object", alias="requestUri")
    serial: Optional[StrictStr] = Field(default=None, description="Serial of the resource")
    service: Optional[StrictStr] = Field(default=None, description="Service name of the resource")
    signaturetype: Optional[StrictStr] = Field(default=None, description="Signature type of the resource")
    startdate: Optional[DeviceType4CertificateDetailsStartdate] = None
    subject: Optional[StrictStr] = Field(default=None, description="Subject of the resource")
    subjectaltname: Optional[StrictStr] = Field(default=None, description="Subjectaltname of the resource")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemID of the array", alias="systemId")
    text: Optional[StrictStr] = Field(default=None, description="array certificate text")
    type: Optional[StrictStr] = Field(default=None, description="The type of resource.")
    uri: Optional[StrictStr] = Field(default=None, description="URI of the resource")
    vc_guid: Optional[StrictStr] = Field(default=None, description="vcGuid of the vCenter", alias="vcGuid")
    __properties: ClassVar[List[str]] = ["associatedLinks", "certType", "commonResourceAttributes", "commonname", "consoleUri", "customerId", "displayname", "domain", "enddate", "fingerprint", "generation", "id", "issuer", "pem", "requestUri", "serial", "service", "signaturetype", "startdate", "subject", "subjectaltname", "systemId", "text", "type", "uri", "vcGuid"]

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
        """Create an instance of DeviceType4CertificateDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in associated_links (list)
        _items = []
        if self.associated_links:
            for _item in self.associated_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associatedLinks'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enddate
        if self.enddate:
            _dict['enddate'] = self.enddate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of startdate
        if self.startdate:
            _dict['startdate'] = self.startdate.to_dict()
        # set to None if cert_type (nullable) is None
        # and model_fields_set contains the field
        if self.cert_type is None and "cert_type" in self.model_fields_set:
            _dict['certType'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if commonname (nullable) is None
        # and model_fields_set contains the field
        if self.commonname is None and "commonname" in self.model_fields_set:
            _dict['commonname'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if enddate (nullable) is None
        # and model_fields_set contains the field
        if self.enddate is None and "enddate" in self.model_fields_set:
            _dict['enddate'] = None

        # set to None if fingerprint (nullable) is None
        # and model_fields_set contains the field
        if self.fingerprint is None and "fingerprint" in self.model_fields_set:
            _dict['fingerprint'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if issuer (nullable) is None
        # and model_fields_set contains the field
        if self.issuer is None and "issuer" in self.model_fields_set:
            _dict['issuer'] = None

        # set to None if pem (nullable) is None
        # and model_fields_set contains the field
        if self.pem is None and "pem" in self.model_fields_set:
            _dict['pem'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if serial (nullable) is None
        # and model_fields_set contains the field
        if self.serial is None and "serial" in self.model_fields_set:
            _dict['serial'] = None

        # set to None if service (nullable) is None
        # and model_fields_set contains the field
        if self.service is None and "service" in self.model_fields_set:
            _dict['service'] = None

        # set to None if signaturetype (nullable) is None
        # and model_fields_set contains the field
        if self.signaturetype is None and "signaturetype" in self.model_fields_set:
            _dict['signaturetype'] = None

        # set to None if startdate (nullable) is None
        # and model_fields_set contains the field
        if self.startdate is None and "startdate" in self.model_fields_set:
            _dict['startdate'] = None

        # set to None if subject (nullable) is None
        # and model_fields_set contains the field
        if self.subject is None and "subject" in self.model_fields_set:
            _dict['subject'] = None

        # set to None if subjectaltname (nullable) is None
        # and model_fields_set contains the field
        if self.subjectaltname is None and "subjectaltname" in self.model_fields_set:
            _dict['subjectaltname'] = None

        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if uri (nullable) is None
        # and model_fields_set contains the field
        if self.uri is None and "uri" in self.model_fields_set:
            _dict['uri'] = None

        # set to None if vc_guid (nullable) is None
        # and model_fields_set contains the field
        if self.vc_guid is None and "vc_guid" in self.model_fields_set:
            _dict['vcGuid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4CertificateDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "certType": obj.get("certType"),
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "commonname": obj.get("commonname"),
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "enddate": DeviceType4CertificateDetailsEnddate.from_dict(obj["enddate"]) if obj.get("enddate") is not None else None,
            "fingerprint": obj.get("fingerprint"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "issuer": obj.get("issuer"),
            "pem": obj.get("pem"),
            "requestUri": obj.get("requestUri"),
            "serial": obj.get("serial"),
            "service": obj.get("service"),
            "signaturetype": obj.get("signaturetype"),
            "startdate": DeviceType4CertificateDetailsStartdate.from_dict(obj["startdate"]) if obj.get("startdate") is not None else None,
            "subject": obj.get("subject"),
            "subjectaltname": obj.get("subjectaltname"),
            "systemId": obj.get("systemId"),
            "text": obj.get("text"),
            "type": obj.get("type"),
            "uri": obj.get("uri"),
            "vcGuid": obj.get("vcGuid")
        })
        return _obj


