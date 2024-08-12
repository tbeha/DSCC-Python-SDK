# Dc4data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_status** | **str** |  | [optional] 
**fw_status** | **str** |  | [optional] 
**fw_version** | **bool** |  | [optional] 

## Example

```python
from dscc.models.dc4data import Dc4data

# TODO update the JSON string below
json = "{}"
# create an instance of Dc4data from a JSON string
dc4data_instance = Dc4data.from_json(json)
# print the JSON string representation of the object
print(Dc4data.to_json())

# convert the object into a dict
dc4data_dict = dc4data_instance.to_dict()
# create an instance of Dc4data from a dict
dc4data_from_dict = Dc4data.from_dict(dc4data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


