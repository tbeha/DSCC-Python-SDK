# DeviceType4InventoryHistory

List of HPE Alletra Storage MP Inventory Updates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4InventoryUpdate]**](DeviceType4InventoryUpdate.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Total number of Inventory Updates | [optional] 

## Example

```python
from dscc.models.device_type4_inventory_history import DeviceType4InventoryHistory

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4InventoryHistory from a JSON string
device_type4_inventory_history_instance = DeviceType4InventoryHistory.from_json(json)
# print the JSON string representation of the object
print(DeviceType4InventoryHistory.to_json())

# convert the object into a dict
device_type4_inventory_history_dict = device_type4_inventory_history_instance.to_dict()
# create an instance of DeviceType4InventoryHistory from a dict
device_type4_inventory_history_from_dict = DeviceType4InventoryHistory.from_dict(device_type4_inventory_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


