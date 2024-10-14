WITH COMPLEX_VARIANT_MORE_ROWS AS (

  SELECT * 
  
  FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_MORE_ROWS') }}

),

FlattenSchema_1 AS (

  {#Extracts and organizes contact information from complex business data for better accessibility.#}
  SELECT 
    CAST(contact.value:content AS STRING) AS content,
    CAST(contact.value:type AS STRING) AS type
  
  FROM COMPLEX_VARIANT_MORE_ROWS AS in0, 
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

)

SELECT *

FROM Filter_1
