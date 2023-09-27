WITH customer_seed AS (

  SELECT * 
  
  FROM {{ ref('customer_seed')}}

),

seeds_customer_seed AS (

  SELECT 
    id,
    first_name
  
  FROM customer_seed

),

id_lt_50 AS (

  SELECT * 
  
  FROM seeds_customer_seed
  
  WHERE id < 50

),

first_name_filter AS (

  SELECT first_name AS FIRST_NAME
  
  FROM id_lt_50

),

by_first_name AS (

  SELECT * 
  
  FROM first_name_filter
  
  ORDER BY FIRST_NAME ASC

),

limit_50 AS (

  SELECT * 
  
  FROM by_first_name
  
  LIMIT 50

)

SELECT *

FROM limit_50
