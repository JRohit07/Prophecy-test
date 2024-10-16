{{
  config({    
    "materialized": "table"
  })
}}

WITH COMPLEX_VARIANT_MORE_ROWS AS (

  SELECT * 
  
  FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_MORE_ROWS') }}

),

structured_boolean_tests AS (

  {#Extracts and organizes contact information from complex data structures for better accessibility.#}
  SELECT 
    FIRST_NAME AS FIRST_NAME,
    MY_STRUCT_VAR:business[0]:address AS address,
    MY_STRUCT_VAR:business[0]:address[0]:contact AS contact,
    CAST(MY_STRUCT_VAR:business[0]:address[0]:contact[0]:content AS STRING) AS content,
    CAST(MY_STRUCT_VAR:business[0]:address[0]:contact[0]:type AS STRING) AS type
  
  FROM COMPLEX_VARIANT_MORE_ROWS AS in0

),

COMPLEX_VARIANT_NESTED_JSON AS (

  SELECT * 
  
  FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_NESTED_JSON') }}

),

Subgraph_1 AS (

  WITH COMPLEX_VARIANT_NESTED_JSON_1 AS (
  
    SELECT * 
    
    FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_NESTED_JSON') }}
  
  ),
  
  distinct_businesses_1 AS (
  
    {#Extracts unique business contacts along with employee details for better relationship management.#}
    SELECT 
      DISTINCT FIRST_NAME AS c1,
      MY_STRUCT_VAR:array_test AS c2,
      MY_STRUCT_VAR:business AS c3,
      CAST(MY_STRUCT_VAR:business[0]:address[0]:contact[0]:content AS STRING) AS c4,
      CAST(MY_STRUCT_VAR:business[0]:address[0]:contact[0]:content AS STRING) AS c5,
      CAST(MY_STRUCT_VAR:business[0]:address[0]:is_still_active AS BOOLEAN) AS c6,
      FIRST_NAME,
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
      HOURLY_RATE
    
    FROM COMPLEX_VARIANT_NESTED_JSON_1 AS in0
  
  ),
  
  Subgraph_2 AS (
  
    WITH distinct_businesses_1_1 AS (
    
      {#Identifies unique businesses associated with distinct first names from complex data.#}
      SELECT 
        DISTINCT FIRST_NAME,
        MY_STRUCT_VAR:array_test,
        MY_STRUCT_VAR:business
      
      FROM COMPLEX_VARIANT_NESTED_JSON_1 AS in0
    
    )
    
    SELECT * 
    
    FROM distinct_businesses_1_1
  
  )
  
  SELECT * 
  
  FROM distinct_businesses_1

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

distinct_businesses AS (

  {#Identifies unique businesses along with their contact details from a complex dataset.#}
  SELECT 
    DISTINCT FIRST_NAME,
    MY_STRUCT_VAR:array_test,
    MY_STRUCT_VAR:business,
    CAST(MY_STRUCT_VAR:business[0]:address[0]:contact[0]:type AS STRING),
    EMAIL
  
  FROM COMPLEX_VARIANT_NESTED_JSON AS in0

)

SELECT *

FROM COMPLEX_VARIANT_MORE_ROWS
