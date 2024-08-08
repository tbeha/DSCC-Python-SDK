# Dc4dataSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hpl_led** | [**HPLLEDSINGLE**](HPLLEDSINGLE.md) |  | [optional] 
**left** | **bool** |  | [optional] 
**right** | **bool** |  | [optional] 
**system_led** | [**SYSTEMLEDSINGLE**](SYSTEMLEDSINGLE.md) |  | [optional] 

## Example

```python
from dscc.models.dc4data_single import Dc4dataSingle

# TODO update the JSON string below
json = "{}"
# create an instance of Dc4dataSingle from a JSON string
dc4data_single_instance = Dc4dataSingle.from_json(json)
# print the JSON string representation of the object
print(Dc4dataSingle.to_json())

# convert the object into a dict
dc4data_single_dict = dc4data_single_instance.to_dict()
# create an instance of Dc4dataSingle from a dict
dc4data_single_from_dict = Dc4dataSingle.from_dict(dc4data_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


