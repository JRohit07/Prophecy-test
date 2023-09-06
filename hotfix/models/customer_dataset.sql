WITH customer_seed AS (

  SELECT * 
  
  FROM {{ ref('customer_seed')}}

),

testseed_lt_50 AS (

  SELECT * 
  
  FROM customer_seed AS testseed
  
  WHERE id < 50

),

filter_by_first_name AS (

  SELECT * 
  
  FROM testseed_lt_50
  
  ORDER BY first_name ASC NULLS LAST

),

limit_50 AS (

  SELECT * 
  
  FROM filter_by_first_name
  
  LIMIT 50

)

SELECT *

FROM limit_50
