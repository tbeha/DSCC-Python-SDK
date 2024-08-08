# VcenterSettingsSumarryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[VcenterSettingDetailList]**](VcenterSettingDetailList.md) |  | [optional] 
**page_limit** | **int** | Page Limit | [optional] 
**page_offset** | **int** | Page Offset | [optional] 
**request_uri** | **str** | requestUri for vcenter settings per system | [optional] 
**total** | **int** | Number of vcenters. | [optional] 

## Example

```python
from dscc.models.vcenter_settings_sumarry_list import VcenterSettingsSumarryList

# TODO update the JSON string below
json = "{}"
# create an instance of VcenterSettingsSumarryList from a JSON string
vcenter_settings_sumarry_list_instance = VcenterSettingsSumarryList.from_json(json)
# print the JSON string representation of the object
print(VcenterSettingsSumarryList.to_json())

# convert the object into a dict
vcenter_settings_sumarry_list_dict = vcenter_settings_sumarry_list_instance.to_dict()
# create an instance of VcenterSettingsSumarryList from a dict
vcenter_settings_sumarry_list_from_dict = VcenterSettingsSumarryList.from_dict(vcenter_settings_sumarry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


