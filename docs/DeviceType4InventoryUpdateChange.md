# DeviceType4InventoryUpdateChange

HPE Alletra Storage MP InventoryUpdate details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change** | **str** | Added or Removed | [optional] 
**index** | **int** | index of the update | [optional] 
**log_time** | **int** | log time | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_inventory_update_change import DeviceType4InventoryUpdateChange

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4InventoryUpdateChange from a JSON string
device_type4_inventory_update_change_instance = DeviceType4InventoryUpdateChange.from_json(json)
# print the JSON string representation of the object
print(DeviceType4InventoryUpdateChange.to_json())

# convert the object into a dict
device_type4_inventory_update_change_dict = device_type4_inventory_update_change_instance.to_dict()
# create an instance of DeviceType4InventoryUpdateChange from a dict
device_type4_inventory_update_change_from_dict = DeviceType4InventoryUpdateChange.from_dict(device_type4_inventory_update_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


