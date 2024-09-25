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

{#Retrieves all records from the rohit_seed dataset for analysis.#}
SELECT *

FROM rohit_seed
