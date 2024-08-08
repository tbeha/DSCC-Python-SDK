# DeviceType4enclosureCardCpuDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bus_speed** | **int** | Speed of the cpu bus | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**cpu_cores** | **int** | Number of Cpu Cores | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_card_id** | **int** | Numeric value for enclosure card | [optional] 
**enclosure_card_uid** | **str** | Unique Identifier of the enclosure card. | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure. | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | id | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**slot** | **int** | Enclosure card CPU slot number | [optional] 
**speed** | **int** | speed | [optional] 
**system_id** | **str** | systemId | [optional] 
**threads** | **int** | Number of threads | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_card_cpu_details import DeviceType4enclosureCardCpuDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureCardCpuDetails from a JSON string
device_type4enclosure_card_cpu_details_instance = DeviceType4enclosureCardCpuDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureCardCpuDetails.to_json())

# convert the object into a dict
device_type4enclosure_card_cpu_details_dict = device_type4enclosure_card_cpu_details_instance.to_dict()
# create an instance of DeviceType4enclosureCardCpuDetails from a dict
device_type4enclosure_card_cpu_details_from_dict = DeviceType4enclosureCardCpuDetails.from_dict(device_type4enclosure_card_cpu_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


