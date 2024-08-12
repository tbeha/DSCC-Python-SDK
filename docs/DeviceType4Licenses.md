# DeviceType4Licenses

System licenses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[DeviceType4AssociatedLinksInner]**](DeviceType4AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**disk_count** | **str** | The disk count from the system license | [optional] 
**features** | **Dict[str, List[LicenseFeature]]** | The raw list of individual licensed features | [optional] 
**issue_date** | [**DeviceType4Calendar**](DeviceType4Calendar.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed licenses object | [optional] 
**resource_uri** | **str** | Resource Uri | [optional] 
**type** | **str** | Type of resource | [optional] 
**version** | **int** | The version number of the system licenses | [optional] 

## Example

```python
from dscc.models.device_type4_licenses import DeviceType4Licenses

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4Licenses from a JSON string
device_type4_licenses_instance = DeviceType4Licenses.from_json(json)
# print the JSON string representation of the object
print(DeviceType4Licenses.to_json())

# convert the object into a dict
device_type4_licenses_dict = device_type4_licenses_instance.to_dict()
# create an instance of DeviceType4Licenses from a dict
device_type4_licenses_from_dict = DeviceType4Licenses.from_dict(device_type4_licenses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


