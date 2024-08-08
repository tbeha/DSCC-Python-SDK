# CapacityInfoSolo

Device capacity details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_summary** | [**CapacitySummary**](CapacitySummary.md) |  | [optional] 

## Example

```python
from dscc.models.capacity_info_solo import CapacityInfoSolo

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityInfoSolo from a JSON string
capacity_info_solo_instance = CapacityInfoSolo.from_json(json)
# print the JSON string representation of the object
print(CapacityInfoSolo.to_json())

# convert the object into a dict
capacity_info_solo_dict = capacity_info_solo_instance.to_dict()
# create an instance of CapacityInfoSolo from a dict
capacity_info_solo_from_dict = CapacityInfoSolo.from_dict(capacity_info_solo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


