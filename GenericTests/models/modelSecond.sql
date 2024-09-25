{{
  config({    
    "schema": "rohit"
  })
}}

WITH customerData AS (

  SELECT * 
  
  FROM {{ ref('customerData')}}

)

{#Retrieves all customer data for comprehensive analysis.#}
SELECT *

FROM customerData
