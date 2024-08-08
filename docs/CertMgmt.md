# CertMgmt

Certificate management mode of the VASA Provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Text in the default language | [optional] 
**key** | **str** | Key of the message | [optional] 

## Example

```python
from dscc.models.cert_mgmt import CertMgmt

# TODO update the JSON string below
json = "{}"
# create an instance of CertMgmt from a JSON string
cert_mgmt_instance = CertMgmt.from_json(json)
# print the JSON string representation of the object
print(CertMgmt.to_json())

# convert the object into a dict
cert_mgmt_dict = cert_mgmt_instance.to_dict()
# create an instance of CertMgmt from a dict
cert_mgmt_from_dict = CertMgmt.from_dict(cert_mgmt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


