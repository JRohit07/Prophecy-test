{{
  config({    
    "severity": 'warn'
  })
}}

WITH raw_customers AS (

  SELECT * 
  
  FROM {{ ref('raw_customers')}}

),

Join_1 AS (

  SELECT 
    in0.id AS id,
    in0.first_name AS first_name,
    in0.last_name AS last_name
  
  FROM raw_customers AS in0
  JOIN raw_customers AS in1
     ON in0.first_name = in1.first_name

)

SELECT 
  ID * ID AS SQID,
  FIRST_NAME,
  LAST_NAME

FROM Join_1
