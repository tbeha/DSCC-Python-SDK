# NimbleAccessControlRecordDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_to** | **str** | External management agent type. Possible values:&#39;volume&#39;, &#39;pe&#39;, &#39;vvol_volume&#39;, &#39;vvol_snapshot&#39;, &#39;snapshot&#39;, &#39;both&#39;. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**pe_ids** | **List[Optional[str]]** | List of candidate protocol endpoints that may be used to access the Virtual Volume. One of them will be selected for the access control record. This field is required only when creating an access control record for a Virtual Volume. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**snapluns** | [**List[NimbleNsSnapLunInfo]**](NimbleNsSnapLunInfo.md) | Information about the snapshot LUNs associated with this access control record. This field is meaningful when the online snapshot can be accessed as a LUN in the group. | [optional] 
**type** | **str** | type | [optional] 
**vol_agent_type** | **str** | External management agent type. Possible values:&#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;, &#39;openstackv2&#39;, &#39;none&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_access_control_record_details import NimbleAccessControlRecordDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleAccessControlRecordDetails from a JSON string
nimble_access_control_record_details_instance = NimbleAccessControlRecordDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleAccessControlRecordDetails.to_json())

# convert the object into a dict
nimble_access_control_record_details_dict = nimble_access_control_record_details_instance.to_dict()
# create an instance of NimbleAccessControlRecordDetails from a dict
nimble_access_control_record_details_from_dict = NimbleAccessControlRecordDetails.from_dict(nimble_access_control_record_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


