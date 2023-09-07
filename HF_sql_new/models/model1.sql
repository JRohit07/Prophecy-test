WITH newSeed AS (

  SELECT * 
  
  FROM {{ ref('newSeed')}}

)

SELECT *

FROM newSeed
