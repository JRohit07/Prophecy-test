WITH all_type_table AS (

  SELECT * 
  
  FROM {{ source('"qa_database"."qa_SCHEMA"', '"all_type_table"') }}

)

SELECT *

FROM all_type_table
