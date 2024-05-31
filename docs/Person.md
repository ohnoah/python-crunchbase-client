# Person

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **list[str]** | Alternate or previous names for the individual\\ Field Type: text_short_multi\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts  | [optional] 
**born_on** | **date** | The birthdate of the person\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**description** | **str** | Text from a Person&#x27;s biography\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**died_on** | **date** | The date when a person died\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * person - Person  | [optional] 
**facebook** | **AllOfPersonFacebook** | Link to a Person&#x27;s Facebook page\\ Field Type: link\\ Searchable: No  | [optional] 
**facet_ids** | **list[str]** | Field Type: enum_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**first_name** | **str** | First name of a Person\\ Field Type: text_short\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts  | [optional] 
**gender** | **str** | A Person&#x27;s gender\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * agender - Agender  * androgyne - Androgyne  * androgynous - Androgynous  * bigender - Bigender  * female - Female  * ftm - Female to Male (FTM)  * gender_fluid - Gender Fluid  * gender_nonconforming - Gender Nonconforming  * gender_questioning - Gender Questioning  * gender_variant - Gender Variant  * genderqueer - Genderqueer  * male - Male  * mtf - Male to Female (MTF)  * neutrois - Neutrois  * non_binary - Non-Binary  * not_provided - Prefer not to identify  * other - Other  * pangender - Pangender  * transfeminine - Transfeminine  * transgender_female - Transgender Female  * transgender_male - Transgender Male  * transgender_man - Transgender Man  * transgender_person - Transgender Person  * transgender_woman - Transgender Woman  * transmasculine - Transmasculine  * transsexual_female - Transsexual Female  * transsexual_male - Transsexual Male  * transsexual_man - Transsexual Man  * transsexual_person - Transsexual Person  * transsexual_woman - Transsexual Woman  * two_spirit - Two-Spirit  | [optional] 
**identifier** | **AllOfPersonIdentifier** | First and last name of a Person\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**image_id** | **str** | The profile image of the person on Crunchbase\\ Field Type: image_id\\ Searchable: No  | [optional] 
**image_url** | **str** | The cloudinary url of the profile image\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**investor_stage** | **list[str]** | This describes the stage of investor this person is (e.g. Angel, Fund of Funds, Venture Capital)\\ Field Type: enum_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**investor_type** | **list[str]** | This describes the type of investor the person is (e.g. Angel, Fund of Funds, Venture Capital)\\ Field Type: enum_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**last_name** | **str** | Last name of a Person\\ Field Type: text_short\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts  | [optional] 
**layout_id** | **str** | This is the auto-generated layout for the profile\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * investor - Investor Layout  | [optional] 
**linkedin** | **AllOfPersonLinkedin** | Link to a Person&#x27;s LinkedIn page\\ Field Type: link\\ Searchable: No  | [optional] 
**location_group_identifiers** | [**list[EntityIdentifier]**](EntityIdentifier.md) | Where the person is located (e.g. San Francisco Bay Area, Silicon Valley)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**location_identifiers** | [**list[LocationIdentifier]**](LocationIdentifier.md) | Where the person is located (e.g. Europe, Menlo Park, China)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**middle_name** | **str** | Middle name of a Person\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**name** | **str** | Full name of a Person\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**num_articles** | **float** | Number of news articles that reference the Person\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_current_advisor_jobs** | **float** | Total number of current Advisors and Board roles the person has\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_current_jobs** | **float** | Total number of current Jobs the person has\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_diversity_spotlight_investments** | **float** | Total number of diversity investments made by an investor\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_event_appearances** | **float** | Total number of events the individual appeared in\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_exits** | **float** | Total number of Exits\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_exits_ipo** | **float** | Total number of Exits (IPO)\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_founded_organizations** | **float** | Number of Organizations that the person founded\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_investments** | **float** | Number of Investments the Individual has participated in\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_jobs** | **float** | Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_lead_investments** | **float** | Number of Investments led by the Individual\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_partner_investments** | **float** | Number of Investments the Individual has partnered in\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_past_advisor_jobs** | **float** | Total number of past Board and Advisor roles the person has\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_past_jobs** | **float** | Total number of past Jobs the person has\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_portfolio_organizations** | **float** | Number of portfolio companies associated to the Person\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**override_layout_id** | **str** | Override the layout of the Entity Profile\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * default - Default Layout  * investor - Investor Layout  | [optional] 
**permalink** | **str** | Field Type: permalink\\ Searchable: No  | [optional] 
**permalink_aliases** | **list[str]** | These are the alternative aliases to the primary permalink of the Organization\\ Field Type: text_exact_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**primary_job_title** | **str** | The person&#x27;s primary job title\\ Field Type: text_short\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts  | [optional] 
**primary_organization** | **AllOfPersonPrimaryOrganization** | The organization associated to the person&#x27;s primary job\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**rank_delta_d30** | **float** | Movement in Rank over the last 30 days using a score from -10 to 10\\ Field Type: decimal\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**rank_delta_d7** | **float** | Movement in Rank over the last 7 days using a score from -10 to 10\\ Field Type: decimal\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**rank_delta_d90** | **float** | Movement in Rank over the last 90 days using a score from -10 to 10\\ Field Type: decimal\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**rank_person** | **float** | Algorithmic rank assigned to the top 100,000 most active People\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**rank_principal** | **float** | Algorithmic rank assigned to the top 100,000 most active Organizations and People\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**short_description** | **str** | Text of Person Description, Industries, and Industry Groups\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**twitter** | **AllOfPersonTwitter** | Link to a Person&#x27;s Twitter page\\ Field Type: link\\ Searchable: No  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 
**website** | **AllOfPersonWebsite** | Link to a Person&#x27;s website. note: website_url has replaced this field; this field will be deprecated in the near future\\ Field Type: link\\ Searchable: No  | [optional] 
**website_url** | **str** | Link to a Person&#x27;s website\\ Field Type: url\\ Searchable: Yes\\ Search Operators: domain_blank, domain_eq, domain_includes, not_domain_eq, not_domain_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
