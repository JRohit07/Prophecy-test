WITH CUSTOMER_1 AS (

  SELECT * 
  
  FROM {{ source('QA_DATABASE.QA_SCHEMA', 'CUSTOMER') }}

),

Aggregate_1 AS (

  {#Aggregates customer data to retrieve the full name by concatenating the first name and last name.#}
  SELECT 
    any_value(LAST_NAME) AS LAST_NAME,
    any_value(FIRST_NAME) AS FIRST_NAME,
    CONCAT(FIRST_NAME, ' ', LAST_NAME) AS full_name
  
  FROM CUSTOMER_1 AS in0
  
  GROUP BY 
    FIRST_NAME, LAST_NAME

),

OrderBy_1 AS (

  {#Sorts the results of Aggregate_1 in ascending order based on the full name, with null values appearing last.#}
  SELECT * 
  
  FROM Aggregate_1 AS in0
  
  ORDER BY FULL_NAME ASC NULLS LAST

)

SELECT *

FROM OrderBy_1
