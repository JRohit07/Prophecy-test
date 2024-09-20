{{
  config({    
    "materialized": "table"
  })
}}

WITH rohit_seed AS (

  SELECT * 
  
  FROM {{ ref('rohit_seed')}}

),

customerData AS (

  SELECT * 
  
  FROM {{ ref('customerData')}}

)

{#Retrieves all data from the specified seed dataset for testing purposes.#}
SELECT *

FROM rohit_seed
