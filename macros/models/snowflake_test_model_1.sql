WITH ALL_TYPE_TABLE AS (

  SELECT * 
  
  FROM {{ source('QA_DATABASE.QA_SCHEMA', 'ALL_TYPE_TABLE') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM ALL_TYPE_TABLE AS in0

)

SELECT *

FROM Reformat_1
