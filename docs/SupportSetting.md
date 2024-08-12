# SupportSetting

Support settings for the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**connect_to_hpe** | **str** | Enable remote support by allowing sending of files from device to HPE. Allowed values: enabled or disabled. | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**email_notifications** | **str** | Receive email notifications. Allowed values: enabled or disabled. | [optional] 
**enterprise_server_url** | **str** | Callhome collection server URL | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | Unique identifier of the support settings. | [optional] 
**mini_insplore_enabled** | **str** | Enables/Disable scheduled Mini-Insplore collection. Allowed values: enabled or disabled. | [optional] 
**rap_forwarding** | **str** | Enable/Disable RAP forwarding. Allowed values: enabled or disabled. | [optional] 
**remote_access** | **str** | Enable/Disable Remote Access. Allowed values: DISABLE or ENABLE_NONROOT or ENABLE_ROOT. It is mandatory. | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**rts_enabled** | **str** | Enable/Disable Real time data scrubbing. Allowed values: enabled or disabled. | [optional] 
**type** | **str** | The type of resource. | [optional] 

## Example

```python
from dscc.models.support_setting import SupportSetting

# TODO update the JSON string below
json = "{}"
# create an instance of SupportSetting from a JSON string
support_setting_instance = SupportSetting.from_json(json)
# print the JSON string representation of the object
print(SupportSetting.to_json())

# convert the object into a dict
support_setting_dict = support_setting_instance.to_dict()
# create an instance of SupportSetting from a dict
support_setting_from_dict = SupportSetting.from_dict(support_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


