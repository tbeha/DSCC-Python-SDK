# NimbleShelfLocateInput

Input to locate a Nimble shelf.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **str** | Which controller this sensor applies to. Possible values:&#39;A&#39;, &#39;B&#39;. | 
**status** | **bool** | Status value of identifier to set. Possible values: &#39;true&#39;, &#39;false&#39;. | 

## Example

```python
from dscc.models.nimble_shelf_locate_input import NimbleShelfLocateInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleShelfLocateInput from a JSON string
nimble_shelf_locate_input_instance = NimbleShelfLocateInput.from_json(json)
# print the JSON string representation of the object
print(NimbleShelfLocateInput.to_json())

# convert the object into a dict
nimble_shelf_locate_input_dict = nimble_shelf_locate_input_instance.to_dict()
# create an instance of NimbleShelfLocateInput from a dict
nimble_shelf_locate_input_from_dict = NimbleShelfLocateInput.from_dict(nimble_shelf_locate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


