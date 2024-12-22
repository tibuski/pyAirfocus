# TeamCompanyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**TeamCompanyInfoRole**](TeamCompanyInfoRole.md) |  | 
**size** | [**TeamCompanyInfoSize**](TeamCompanyInfoSize.md) |  | 
**telephone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.team_company_info import TeamCompanyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TeamCompanyInfo from a JSON string
team_company_info_instance = TeamCompanyInfo.from_json(json)
# print the JSON string representation of the object
print(TeamCompanyInfo.to_json())

# convert the object into a dict
team_company_info_dict = team_company_info_instance.to_dict()
# create an instance of TeamCompanyInfo from a dict
team_company_info_from_dict = TeamCompanyInfo.from_dict(team_company_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


