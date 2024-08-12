# IPAddressObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addr** | **str** | An IP Address. | [optional] 

## Example

```python
from dscc.models.ip_address_object import IPAddressObject

# TODO update the JSON string below
json = "{}"
# create an instance of IPAddressObject from a JSON string
ip_address_object_instance = IPAddressObject.from_json(json)
# print the JSON string representation of the object
print(IPAddressObject.to_json())

# convert the object into a dict
ip_address_object_dict = ip_address_object_instance.to_dict()
# create an instance of IPAddressObject from a dict
ip_address_object_from_dict = IPAddressObject.from_dict(ip_address_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


