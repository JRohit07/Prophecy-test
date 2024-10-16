WITH COMPLEX_VARIANT_MORE_ROWS AS (

  SELECT * 
  
  FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_MORE_ROWS') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM COMPLEX_VARIANT_MORE_ROWS AS in0

),

FlattenSchema_1 AS (

  {#Extracts and organizes contact information from complex business data for better accessibility.#}
  SELECT 
    CAST(contact.value:content AS STRING) AS content,
    CAST(contact.value:type AS STRING) AS type
  
  FROM Reformat_1 AS in0, 
  LATERAL flatten(input => MY_STRUCT_VAR:business) AS business, 
  LATERAL flatten(input => business.value:address) AS address, 
  LATERAL flatten(input => address.value:contact) AS contact

),

Filter_1 AS (

  {#Extracts and organizes contact information from complex business data for better accessibility.#}
  SELECT * 
  
  FROM FlattenSchema_1 AS in0
  
  WHERE CONTENT = 'kishore@prophecy.io'

),

COMPLEX_VARIANT_NESTED_JSON AS (

  SELECT * 
  
  FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_NESTED_JSON') }}

),

nested_json_structure AS (

  {#Extracts specific fields from a complex nested JSON structure for streamlined data analysis.#}
  SELECT 
    LAST_NAME AS LAST_NAME,
    MY_STRUCT_VAR AS MY_STRUCT_VAR,
    'avcssdsadasd'
  
  FROM COMPLEX_VARIANT_NESTED_JSON AS in0

)

SELECT *

FROM Filter_1
