WITH customerData AS (

  SELECT * 
  
  FROM {{ ref('customerData')}}

)

{#Retrieves all available customer data for analysis.#}
SELECT *

FROM customerData
