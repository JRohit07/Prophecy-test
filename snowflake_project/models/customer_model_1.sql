WITH customer_orders_1 AS (

  SELECT * 
  
  FROM {{ ref('customer_orders_1')}}

),

dummy_seed AS (

  SELECT * 
  
  FROM {{ ref('dummy_seed')}}

)

SELECT *

FROM dummy_seed
