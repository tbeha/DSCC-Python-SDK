# NICDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ip** | **str** | Data IP address. | [optional] 
**name** | **str** | Name of NIC. | [optional] 
**subnet_label** | **str** | Subnet label for this NIC. | [optional] 
**tagged** | **bool** | Identify whether the NIC is tagged. | [optional] 

## Example

```python
from dscc.models.nic_details import NICDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NICDetails from a JSON string
nic_details_instance = NICDetails.from_json(json)
# print the JSON string representation of the object
print(NICDetails.to_json())

# convert the object into a dict
nic_details_dict = nic_details_instance.to_dict()
# create an instance of NICDetails from a dict
nic_details_from_dict = NICDetails.from_dict(nic_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


