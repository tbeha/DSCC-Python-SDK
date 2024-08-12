# DeviceType4InventoryUpdate

HPE Alletra Storage MP InventoryUpdate details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[DeviceType4InventoryUpdateChange]**](DeviceType4InventoryUpdateChange.md) | List of inventory changes for the component | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**generation** | **int** | generation | [optional] 
**last_modified_epoch** | **int** | last modified epoch | [optional] 
**parent** | [**DeviceType4InventoryUpdateParentDetail**](DeviceType4InventoryUpdateParentDetail.md) |  | [optional] 
**sub_component** | **str** | Sub component | [optional] 
**system_id** | **str** | systemId | [optional] 
**system_wwn** | **str** | System wwn  | [optional] 
**type** | **str** | type | [optional] 
**uid** | **str** | UID of the update | [optional] 
**uri** | **str** | Uri | [optional] 

## Example

```python
from dscc.models.device_type4_inventory_update import DeviceType4InventoryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4InventoryUpdate from a JSON string
device_type4_inventory_update_instance = DeviceType4InventoryUpdate.from_json(json)
# print the JSON string representation of the object
print(DeviceType4InventoryUpdate.to_json())

# convert the object into a dict
device_type4_inventory_update_dict = device_type4_inventory_update_instance.to_dict()
# create an instance of DeviceType4InventoryUpdate from a dict
device_type4_inventory_update_from_dict = DeviceType4InventoryUpdate.from_dict(device_type4_inventory_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


