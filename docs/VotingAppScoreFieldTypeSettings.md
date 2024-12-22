# VotingAppScoreFieldTypeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum** | **float** |  | [optional] 
**minimum** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.voting_app_score_field_type_settings import VotingAppScoreFieldTypeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of VotingAppScoreFieldTypeSettings from a JSON string
voting_app_score_field_type_settings_instance = VotingAppScoreFieldTypeSettings.from_json(json)
# print the JSON string representation of the object
print(VotingAppScoreFieldTypeSettings.to_json())

# convert the object into a dict
voting_app_score_field_type_settings_dict = voting_app_score_field_type_settings_instance.to_dict()
# create an instance of VotingAppScoreFieldTypeSettings from a dict
voting_app_score_field_type_settings_from_dict = VotingAppScoreFieldTypeSettings.from_dict(voting_app_score_field_type_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


