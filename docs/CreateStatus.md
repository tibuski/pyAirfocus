# CreateStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**StatusCategory**](StatusCategory.md) |  | 
**color** | [**StatusColor**](StatusColor.md) |  | [optional] 
**default** | **bool** | Whether this status should be applied by default to newly created items. There can be only one default status in each workspace. | 
**name** | **str** | Name of this status in UI. | 
**order** | **int** | Order of this status comparing to other statuses in the same workspace. | 

## Example

```python
from openapi_client.models.create_status import CreateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStatus from a JSON string
create_status_instance = CreateStatus.from_json(json)
# print the JSON string representation of the object
print(CreateStatus.to_json())

# convert the object into a dict
create_status_dict = create_status_instance.to_dict()
# create an instance of CreateStatus from a dict
create_status_from_dict = CreateStatus.from_dict(create_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


