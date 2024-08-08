# NimbleDiskSmartAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cur_value** | **int** | Current value. | [optional] 
**flags** | **int** | Smart flags. | [optional] 
**last_updated_epoch_secs** | **int** | Last update time in epoch seconds. | [optional] 
**name** | **str** | Name of the Smart attribute. | [optional] 
**raw_value** | **int** | Raw value. | [optional] 
**smart_id** | **int** | Smart attribute ID. | [optional] 
**threshold** | **int** | Smart threshold. | [optional] 
**worst_value** | **int** | Worst value. | [optional] 

## Example

```python
from dscc.models.nimble_disk_smart_attributes import NimbleDiskSmartAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleDiskSmartAttributes from a JSON string
nimble_disk_smart_attributes_instance = NimbleDiskSmartAttributes.from_json(json)
# print the JSON string representation of the object
print(NimbleDiskSmartAttributes.to_json())

# convert the object into a dict
nimble_disk_smart_attributes_dict = nimble_disk_smart_attributes_instance.to_dict()
# create an instance of NimbleDiskSmartAttributes from a dict
nimble_disk_smart_attributes_from_dict = NimbleDiskSmartAttributes.from_dict(nimble_disk_smart_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


