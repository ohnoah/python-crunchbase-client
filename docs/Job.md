# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**employee_featured_order** | **float** | These are the featured employees of an organization\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**ended_on** | **AllOfJobEndedOn** | End date of the Person&#x27;s Job\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * job - Job  | [optional] 
**identifier** | **AllOfJobIdentifier** | Position name field (e.g. Steve Jobs, Founder @ Pixar)\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**is_current** | **bool** | This indicates whether the Job is current or not\\ Field Type: boolean\\ Searchable: Yes\\ Search Operators: blank, eq  | [optional] 
**job_type** | **str** | Select a job type that best represent your role at the organization\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * advisor - Advisor  * board_member - Board Member  * board_observer - Board Observer  * employee - Non-Executive Employee  * executive - Executive  | [optional] 
**name** | **str** | Field Type: text_blob\\ Searchable: No  | [optional] 
**organization_identifier** | **AllOfJobOrganizationIdentifier** | This is the name of the organization\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**permalink** | **str** | Field Type: permalink\\ Searchable: No  | [optional] 
**person_identifier** | **AllOfJobPersonIdentifier** | First and last name of a Person\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**short_description** | **str** | Text of Job Description\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**started_on** | **AllOfJobStartedOn** | Start date of the Person&#x27;s Job\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**title** | **str** | Title of a Person&#x27;s Job\\ Field Type: text_short\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

