# DeviceType4vcenterSettingDetailList

Vcenter settings for the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**description** | **str** | Vcenter description | [optional] 
**friendly_cert** | [**DeviceType4friendlyCert**](DeviceType4friendlyCert.md) |  | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | Unique identifier of the vcenter settings. | [optional] 
**inetaddress** | **str** | Address of the vcenter. | [optional] 
**name** | **str** | Name of vcenter. | [optional] 
**port** | **int** | port number of vcenter. | [optional] 
**resource_uri** | **str** | resourceUri for detailed vcenter setting object | [optional] 
**status** | [**DeviceType4vcenterStatus**](DeviceType4vcenterStatus.md) |  | [optional] 
**system_id** | **str** | SystemID of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 
**username** | **str** | User of the vcenter configured | [optional] 
**vm_manager_type** | **str** | Type of the vmmanager settings. | [optional] 

## Example

```python
from dscc.models.device_type4vcenter_setting_detail_list import DeviceType4vcenterSettingDetailList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4vcenterSettingDetailList from a JSON string
device_type4vcenter_setting_detail_list_instance = DeviceType4vcenterSettingDetailList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4vcenterSettingDetailList.to_json())

# convert the object into a dict
device_type4vcenter_setting_detail_list_dict = device_type4vcenter_setting_detail_list_instance.to_dict()
# create an instance of DeviceType4vcenterSettingDetailList from a dict
device_type4vcenter_setting_detail_list_from_dict = DeviceType4vcenterSettingDetailList.from_dict(device_type4vcenter_setting_detail_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


