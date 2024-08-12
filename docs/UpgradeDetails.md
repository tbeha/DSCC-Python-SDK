# UpgradeDetails

Array upgrade data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[NimbleErrorWithArguments]**](NimbleErrorWithArguments.md) | List of error or info messages. | [optional] 
**stage** | **str** | Array upgrade stage. Possible values: &#39;prepare&#39;, &#39;finish&#39;, &#39;none&#39;. | [optional] 
**state** | **str** | Array upgrade state. Possible values: &#39;abort_failed&#39;, &#39;precheck&#39;, &#39;in_progress&#39;, &#39;paused&#39;, &#39;aborted&#39;, &#39;aborting&#39;, &#39;started&#39;, &#39;none&#39;, &#39;failed&#39;, &#39;awaiting_next_stage&#39;, &#39;complete&#39;. | [optional] 
**type** | **str** | Array upgrade type. Possible values: &#39;offline&#39;, &#39;invalid&#39;. | [optional] 

## Example

```python
from dscc.models.upgrade_details import UpgradeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeDetails from a JSON string
upgrade_details_instance = UpgradeDetails.from_json(json)
# print the JSON string representation of the object
print(UpgradeDetails.to_json())

# convert the object into a dict
upgrade_details_dict = upgrade_details_instance.to_dict()
# create an instance of UpgradeDetails from a dict
upgrade_details_from_dict = UpgradeDetails.from_dict(upgrade_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


