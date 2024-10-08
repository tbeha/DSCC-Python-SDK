# NimbleNsShelfPortInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_errors** | **str** | Comma separated list of integers to indicate error conditions. | [optional] 
**port_idx** | **int** | Index of the port, starting from 0. | [optional] 
**port_name** | **str** | Name of the port. | [optional] 
**port_status** | **str** | Status of the port. Possible values:&#39;connected&#39;, &#39;disconnected&#39;, &#39;unknown&#39;,&#39;disabled&#39;. | [optional] 
**port_type** | **str** | Type of the sas port (e.g. upstream/downstream). Possible values:&#39;upstream&#39;, &#39;downstream&#39;, &#39;unknown&#39;. | [optional] 
**remote_loc_id** | **int** | The location ID of the controller that connects to this port. | [optional] 
**remote_port_id** | **int** | The pord_id of the remote SAS port that connects to this port. | [optional] 
**remote_sas_addr** | **str** | SAS address for the connected. | [optional] 
**remote_sas_domain** | **str** | The sas domain (A or B side) it connects to. Possible values:&#39;A&#39;, &#39;B&#39;, &#39;unknown&#39;. | [optional] 
**remote_sas_phy_id** | **str** | Comma separated list of phy ids that this port connects to. | [optional] 

## Example

```python
from dscc.models.nimble_ns_shelf_port_info import NimbleNsShelfPortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsShelfPortInfo from a JSON string
nimble_ns_shelf_port_info_instance = NimbleNsShelfPortInfo.from_json(json)
# print the JSON string representation of the object
print(NimbleNsShelfPortInfo.to_json())

# convert the object into a dict
nimble_ns_shelf_port_info_dict = nimble_ns_shelf_port_info_instance.to_dict()
# create an instance of NimbleNsShelfPortInfo from a dict
nimble_ns_shelf_port_info_from_dict = NimbleNsShelfPortInfo.from_dict(nimble_ns_shelf_port_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


