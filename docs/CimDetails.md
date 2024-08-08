# CimDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**cim** | [**Cim**](Cim.md) |  | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 

## Example

```python
from dscc.models.cim_details import CimDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CimDetails from a JSON string
cim_details_instance = CimDetails.from_json(json)
# print the JSON string representation of the object
print(CimDetails.to_json())

# convert the object into a dict
cim_details_dict = cim_details_instance.to_dict()
# create an instance of CimDetails from a dict
cim_details_from_dict = CimDetails.from_dict(cim_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


