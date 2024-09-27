{{
  config({    
    "materialized": "table"
  })
}}

WITH customer AS (

  SELECT * 
  
  FROM {{ ref('customer')}}

)

{#Retrieves all customer data for testing purposes.#}
SELECT *

FROM customer
