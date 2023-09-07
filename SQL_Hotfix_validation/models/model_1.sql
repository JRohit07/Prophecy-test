WITH customer_seed AS (

  SELECT * 
  
  FROM {{ ref('customer_seed')}}

)

SELECT *

FROM customer_seed
