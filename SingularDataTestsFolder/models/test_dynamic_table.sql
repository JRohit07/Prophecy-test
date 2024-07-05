{{
  config({    
    "materialized": "dynamic_table",
    "snowflake_warehouse": "QA_WAREHOUSE",
    "target_lag": "1 minute"
  })
}}

WITH raw_customers AS (

  SELECT * 
  
  FROM {{ ref('raw_customers')}}

),

Reformat_1 AS (

  SELECT 
    id AS id,
    first_name AS first_name,
    last_name AS last_name,
    CONCAT(first_name, ' ', last_name) AS full_name
  
  FROM raw_customers AS in0

)

SELECT *

FROM Reformat_1
