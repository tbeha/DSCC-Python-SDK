# DeviceType4enclosureCardBootDriveDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_card_id** | **int** | ID of enclosure card. | [optional] 
**enclosure_card_uid** | **str** | Unique Identifier of the enclosure card. | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure | [optional] 
**eui_wwn** | **str** | EUI/WWN | [optional] 
**fw_version** | **str** | Firmware version | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**manufacturing** | [**DeviceType4manufacturing**](DeviceType4manufacturing.md) |  | [optional] 
**path** | **str** | path | [optional] 
**sed_status** | **str** | SED state of disk | [optional] 
**size_mi_b** | **int** | Size in MiB | [optional] 
**slot** | **int** | Slot this boot drive reside in | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_card_boot_drive_details import DeviceType4enclosureCardBootDriveDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureCardBootDriveDetails from a JSON string
device_type4enclosure_card_boot_drive_details_instance = DeviceType4enclosureCardBootDriveDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureCardBootDriveDetails.to_json())

# convert the object into a dict
device_type4enclosure_card_boot_drive_details_dict = device_type4enclosure_card_boot_drive_details_instance.to_dict()
# create an instance of DeviceType4enclosureCardBootDriveDetails from a dict
device_type4enclosure_card_boot_drive_details_from_dict = DeviceType4enclosureCardBootDriveDetails.from_dict(device_type4enclosure_card_boot_drive_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


