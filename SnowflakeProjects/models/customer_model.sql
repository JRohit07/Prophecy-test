WITH raw_customer AS (

  SELECT * 
  
  FROM {{ ref('raw_customer')}}

),

Reformat_1 AS (

  SELECT 
    id AS id,
    first_name AS first_name,
    last_name AS last_name
  
  FROM raw_customer AS in0

),

Limit_1 AS (

  SELECT * 
  
  FROM Reformat_1 AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
