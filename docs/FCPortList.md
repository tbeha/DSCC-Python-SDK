# FCPortList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of FC Port | [optional] 

## Example

```python
from dscc.models.fc_port_list import FCPortList

# TODO update the JSON string below
json = "{}"
# create an instance of FCPortList from a JSON string
fc_port_list_instance = FCPortList.from_json(json)
# print the JSON string representation of the object
print(FCPortList.to_json())

# convert the object into a dict
fc_port_list_dict = fc_port_list_instance.to_dict()
# create an instance of FCPortList from a dict
fc_port_list_from_dict = FCPortList.from_dict(fc_port_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


