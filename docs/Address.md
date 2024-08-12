# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_node** | **int** | Active node ID | [optional] 
**auto_sense** | **bool** | Specifies if the autosense is enabled for network port | [optional] 
**full_duplex** | **bool** | Is network port full duplex | [optional] 
**ip_address** | **str** | IP Address of the network port | [optional] 
**net_mask** | **str** | Net mask of the network port | [optional] 
**speed** | **int** | Speed of the network port | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**status** | **str** | Status of the network port | [optional] 

## Example

```python
from dscc.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


