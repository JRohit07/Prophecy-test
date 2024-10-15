WITH COMPLEX_VARIANT_NESTED_JSON AS (

  SELECT * 
  
  FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_NESTED_JSON') }}

),

Filter_1 AS (

  {#Identifies discrepancies between business address names and employee names in complex data structures.#}
  SELECT * 
  
  FROM COMPLEX_VARIANT_NESTED_JSON AS in0
  
  WHERE CAST(MY_STRUCT_VAR:business[0]:address[0]:name AS VARIANT) != MY_STRUCT_VAR:business[0]:employees[0]:name

),

COMPLEX_VARIANT_MORE_ROWS AS (

  SELECT * 
  
  FROM {{ source('ROHIT.VARIANT_SCHEMA', 'COMPLEX_VARIANT_MORE_ROWS') }}

),

Reformat_1 AS (

  {#Reformats employee data for clearer presentation and analysis.#}
  SELECT 
    FIRST_NAME AS FIRST_NAME,
    LAST_NAME AS LAST_NAME,
    AGE AS AGE,
    MY_STRUCT_VAR AS MY_STRUCT_VAR,
    EMAIL AS EMAIL,
    PHONE_NUMBER AS PHONE_NUMBER,
    ADDRESS AS ADDRESS,
    JOIN_DATE AS JOIN_DATE,
    SALARY AS SALARY,
    IS_ACTIVE AS IS_ACTIVE,
    DEPARTMENT AS DEPARTMENT,
    HIRE_DATE AS HIRE_DATE,
    LAST_LOGIN_TIME AS LAST_LOGIN_TIME,
    LOGIN_TIMESTAMP AS LOGIN_TIMESTAMP,
    HOURLY_RATE AS HOURLY_RATE,
    CAST(MY_STRUCT_VAR:business[0]:name AS STRING) AS name
  
  FROM COMPLEX_VARIANT_MORE_ROWS AS in0

),

Join_1 AS (

  {#Combines contact information with business addresses for targeted outreach.#}
  SELECT 
    in0.EMAIL AS EMAIL,
    in0.PHONE_NUMBER AS PHONE_NUMBER,
    in0.MY_STRUCT_VAR AS MY_STRUCT_VAR,
    in0.MY_STRUCT_VAR:business[0]:address AS MY_STRUCT_VAR_business_address
  
  FROM Filter_1 AS in0
  INNER JOIN Reformat_1 AS in1
     ON in1.FIRST_NAME = in0.FIRST_NAME

),

Deduplicate_1 AS (

  SELECT DISTINCT *
  
  FROM COMPLEX_VARIANT_NESTED_JSON AS in0

)

SELECT *

FROM Join_1
