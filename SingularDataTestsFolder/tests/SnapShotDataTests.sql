WITH customer_snapshot AS (

  SELECT * 
  
  FROM {{ ref('customer_snapshot')}}

)

SELECT *

FROM customer_snapshot
