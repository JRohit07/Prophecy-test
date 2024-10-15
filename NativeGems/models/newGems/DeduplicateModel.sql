WITH COMPLEX_VARIANT_MORE_ROWS AS (

  SELECT * 
  
  FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_MORE_ROWS') }}

),

Deduplicate_1 AS (

  {#Removes duplicate records to ensure unique entries for employees based on various attributes.#}
  SELECT * 
  
  FROM COMPLEX_VARIANT_MORE_ROWS AS in0
  
  QUALIFY COUNT(*) OVER (PARTITION BY MY_STRUCT_VAR:complex_name.additional_name, 
  LAST_NAME, 
  AGE, 
  MY_STRUCT_VAR, 
  EMAIL, 
  PHONE_NUMBER, 
  ADDRESS, 
  JOIN_DATE, 
  SALARY, 
  IS_ACTIVE, 
  DEPARTMENT, 
  HIRE_DATE, 
  LAST_LOGIN_TIME, 
  LOGIN_TIMESTAMP, 
  HOURLY_RATE) = 1

),

Reformat_1 AS (

  {#Extracts and formats business address and status information for clarity.#}
  SELECT 
    MY_STRUCT_VAR:business[0]:address AS address,
    CAST(MY_STRUCT_VAR:business[0]:address[0]:is_still_active AS BOOLEAN) AS is_still_active,
    CAST(MY_STRUCT_VAR:business[0]:name AS STRING) AS name,
    CAST(MY_STRUCT_VAR:complex_name:c_middle_name AS STRING) AS c_middle_name
  
  FROM Deduplicate_1 AS in0

),

structured_boolean_tests AS (

  {#Extracts boolean test values from a structured variable for analysis.#}
  SELECT 
    MY_STRUCT_VAR['boolean_test'] AS c1,
    MY_STRUCT_VAR:boolean_test AS c2
  
  FROM COMPLEX_VARIANT_MORE_ROWS AS in0

),

COMPLEX_VARIANT_NESTED_JSON AS (

  SELECT * 
  
  FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_NESTED_JSON') }}

),

Deduplicate_2 AS (

  SELECT DISTINCT *
  
  FROM COMPLEX_VARIANT_NESTED_JSON AS in0

)

SELECT *

FROM Reformat_1
