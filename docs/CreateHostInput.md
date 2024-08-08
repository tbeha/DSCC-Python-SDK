# CreateHostInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**contact** | **str** | Contact information | [optional] 
**fqdn** | **str** | Fully qualified domain name of the host. | [optional] 
**host_group_ids** | **List[str]** | List of hostgroup IDs | [optional] 
**initiator_ids** | **List[str]** | List of ids of existing initiators | [optional] 
**initiators_to_create** | [**List[InitiatorInput]**](InitiatorInput.md) | List of initiators to be created and added to this host | [optional] 
**ip_address** | **str** | IP address of the host. | [optional] 
**is_vvol_host** | **bool** | Set this value to true if you want to use this host to export the VASA vVOLs using NVMe protocol. | [optional] 
**location** | **str** | location. | [optional] 
**model** | **str** | Model | [optional] 
**name** | **str** | Name of the host. | 
**operating_system** | **str** | Host operating system. Possible Values are: - AIX - Apple - Citrix Hypervisor(XenServer) - HP-UX - IBM VIO Server - InForm - NetApp/ONTAP - OE Linux UEK - OpenVMS - Oracle VM x86 - RHE Linux - RHE Virtualization - Solaris - SuSE Linux - SuSE Virtualization - Ubuntu - VMware (ESXi) - Windows Server | 
**persona** | **str** | Host persona details. | [optional] 
**protocol** | **str** | protocol | [optional] 
**subnet** | **str** | subnet. | [optional] 
**user_created** | **bool** | Indicates whether user created host or discovered host. value should always be set as \&quot;true\&quot;. API will internally override the passed value to set it as \&quot;true\&quot;. | [optional] 

## Example

```python
from dscc.models.create_host_input import CreateHostInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostInput from a JSON string
create_host_input_instance = CreateHostInput.from_json(json)
# print the JSON string representation of the object
print(CreateHostInput.to_json())

# convert the object into a dict
create_host_input_dict = create_host_input_instance.to_dict()
# create an instance of CreateHostInput from a dict
create_host_input_from_dict = CreateHostInput.from_dict(create_host_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


