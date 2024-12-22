# UpdateStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**StatusCategory**](StatusCategory.md) |  | 
**color** | [**StatusColor**](StatusColor.md) |  | [optional] 
**default** | **bool** | Whether this status should be applied by default to newly created items. There can be only one default status in each workspace. | 
**id** | **str** |  | 
**name** | **str** | Name of this status in UI. | 
**order** | **int** | Order of this status comparing to other statuses in the same workspace. | 

## Example

```python
from openapi_client.models.update_status import UpdateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStatus from a JSON string
update_status_instance = UpdateStatus.from_json(json)
# print the JSON string representation of the object
print(UpdateStatus.to_json())

# convert the object into a dict
update_status_dict = update_status_instance.to_dict()
# create an instance of UpdateStatus from a dict
update_status_from_dict = UpdateStatus.from_dict(update_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


