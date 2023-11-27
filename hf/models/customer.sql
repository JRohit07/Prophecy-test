WITH seed AS (

  SELECT * 
  
  FROM {{ ref('seed')}}

),

Reformat_1 AS (

  SELECT 
    id AS id,
    first_name AS first_name,
    last_name AS last_name
  
  FROM seed AS in0

)

SELECT *

FROM Reformat_1
