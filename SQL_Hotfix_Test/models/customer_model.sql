WITH new_seed AS (

  SELECT * 
  
  FROM {{ ref('new_seed')}}

),

Reformat_1 AS (

  SELECT 
    id AS id,
    first_name AS first_name,
    last_name AS last_name,
    {{ SQL_HOTFIX_TESTING_DB_2.generic_round() }} AS id
  
  FROM new_seed AS in0

),

seeds_lt_100 AS (

  SELECT * 
  
  FROM new_seed
  
  WHERE id < 100

),

filter_by_first_name AS (

  SELECT * 
  
  FROM seeds_lt_100
  
  ORDER BY first_name ASC NULLS LAST

),

limit_50 AS (

  SELECT * 
  
  FROM filter_by_first_name
  
  LIMIT 50

),

select_distinct_colums_1 AS (

  {{ SQL_HOTFIX_TESTING_DB_2.select_distinct_colums(table = 'new_seed', col = 'id') }}

)

SELECT *

FROM limit_50
