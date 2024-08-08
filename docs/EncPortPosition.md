# EncPortPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** |  | [optional] 
**port** | **int** |  | [optional] 
**slot** | **int** |  | [optional] 

## Example

```python
from dscc.models.enc_port_position import EncPortPosition

# TODO update the JSON string below
json = "{}"
# create an instance of EncPortPosition from a JSON string
enc_port_position_instance = EncPortPosition.from_json(json)
# print the JSON string representation of the object
print(EncPortPosition.to_json())

# convert the object into a dict
enc_port_position_dict = enc_port_position_instance.to_dict()
# create an instance of EncPortPosition from a dict
enc_port_position_from_dict = EncPortPosition.from_dict(enc_port_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


