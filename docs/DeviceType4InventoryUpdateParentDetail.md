# DeviceType4InventoryUpdateParentDetail

Identiying details of the parent component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_number** | **str** | part-number of the parent component | [optional] 
**serial_number** | **str** | serial-number of the parent component | [optional] 

## Example

```python
from dscc.models.device_type4_inventory_update_parent_detail import DeviceType4InventoryUpdateParentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4InventoryUpdateParentDetail from a JSON string
device_type4_inventory_update_parent_detail_instance = DeviceType4InventoryUpdateParentDetail.from_json(json)
# print the JSON string representation of the object
print(DeviceType4InventoryUpdateParentDetail.to_json())

# convert the object into a dict
device_type4_inventory_update_parent_detail_dict = device_type4_inventory_update_parent_detail_instance.to_dict()
# create an instance of DeviceType4InventoryUpdateParentDetail from a dict
device_type4_inventory_update_parent_detail_from_dict = DeviceType4InventoryUpdateParentDetail.from_dict(device_type4_inventory_update_parent_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


