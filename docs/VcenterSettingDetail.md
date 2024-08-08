# VcenterSettingDetail

Vcenter settings for the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**description** | **str** | Vcenter description | [optional] 
**friendly_cert** | [**FriendlyCert**](FriendlyCert.md) |  | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | Unique identifier of the vcenter settings. | [optional] 
**inetaddress** | **str** | Address of the vcenter. | [optional] 
**name** | **str** | Name of vcenter. | [optional] 
**port** | **int** | port number of vcenter. | [optional] 
**request_uri** | **str** | requestUri for vcenter setting details per system | [optional] 
**resource_uri** | **str** | resourceUri for detailed vcenter setting object | [optional] 
**status** | [**VcenterStatus**](VcenterStatus.md) |  | [optional] 
**system_id** | **str** | SystemID of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 
**username** | **str** | User of the vcenter configured. | [optional] 
**vm_manager_type** | **str** | Type of the vmmanager settings. | [optional] 

## Example

```python
from dscc.models.vcenter_setting_detail import VcenterSettingDetail

# TODO update the JSON string below
json = "{}"
# create an instance of VcenterSettingDetail from a JSON string
vcenter_setting_detail_instance = VcenterSettingDetail.from_json(json)
# print the JSON string representation of the object
print(VcenterSettingDetail.to_json())

# convert the object into a dict
vcenter_setting_detail_dict = vcenter_setting_detail_instance.to_dict()
# create an instance of VcenterSettingDetail from a dict
vcenter_setting_detail_from_dict = VcenterSettingDetail.from_dict(vcenter_setting_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


