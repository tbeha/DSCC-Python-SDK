# DeviceType4VcenterSettingsSumarryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4vcenterSettingDetailList]**](DeviceType4vcenterSettingDetailList.md) |  | [optional] 
**page_limit** | **int** | Page Limit | [optional] 
**page_offset** | **int** | Page Offset | [optional] 
**request_uri** | **str** | requestUri for vcenter settings per system | [optional] 
**total** | **int** | Number of vcenters. | [optional] 

## Example

```python
from dscc.models.device_type4_vcenter_settings_sumarry_list import DeviceType4VcenterSettingsSumarryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VcenterSettingsSumarryList from a JSON string
device_type4_vcenter_settings_sumarry_list_instance = DeviceType4VcenterSettingsSumarryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VcenterSettingsSumarryList.to_json())

# convert the object into a dict
device_type4_vcenter_settings_sumarry_list_dict = device_type4_vcenter_settings_sumarry_list_instance.to_dict()
# create an instance of DeviceType4VcenterSettingsSumarryList from a dict
device_type4_vcenter_settings_sumarry_list_from_dict = DeviceType4VcenterSettingsSumarryList.from_dict(device_type4_vcenter_settings_sumarry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


