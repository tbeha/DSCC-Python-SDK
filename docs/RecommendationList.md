# RecommendationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_info** | [**CapacityInfoSolo**](CapacityInfoSolo.md) |  | [optional] 
**id** | **str** | uid of the array | [optional] 
**mgmt_ip** | **str** | management Ip of the array | [optional] 
**name** | **str** | name of the array | [optional] 
**product_family** | **str** | Storage device type. Possible values: deviceType1 and deviceType2 | [optional] 
**state** | **str** | For deviceType1 State derived from ports, enclosure, disk and node state for deviceType2 state is state reported by deviceType2 array | [optional] 
**system_wwn** | **str** | WWN of the array | [optional] 

## Example

```python
from dscc.models.recommendation_list import RecommendationList

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationList from a JSON string
recommendation_list_instance = RecommendationList.from_json(json)
# print the JSON string representation of the object
print(RecommendationList.to_json())

# convert the object into a dict
recommendation_list_dict = recommendation_list_instance.to_dict()
# create an instance of RecommendationList from a dict
recommendation_list_from_dict = RecommendationList.from_dict(recommendation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


