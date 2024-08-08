# PortPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | Port position node number &#x60;Filter, Sort&#x60; | [optional] 
**port** | **int** | Port position port number &#x60;Filter, Sort&#x60; | [optional] 
**slot** | **int** | Port position slot number &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.port_position import PortPosition

# TODO update the JSON string below
json = "{}"
# create an instance of PortPosition from a JSON string
port_position_instance = PortPosition.from_json(json)
# print the JSON string representation of the object
print(PortPosition.to_json())

# convert the object into a dict
port_position_dict = port_position_instance.to_dict()
# create an instance of PortPosition from a dict
port_position_from_dict = PortPosition.from_dict(port_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


