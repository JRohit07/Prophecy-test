WITH seed AS (

  SELECT * 
  
  FROM {{ ref('seed')}}

)

SELECT *

FROM seed
