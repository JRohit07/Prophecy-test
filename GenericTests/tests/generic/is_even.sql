{% test is_even(model=modelSecond, column_name=defalt) %}

with validation as (

    select
        {{ column_name }} as even_field

    from {{ model }}

),

validation_errors as (

    select
        even_field

    from validation
    where (even_field % 2) = 1
)

select *
from validation_errors
{% endtest %}

 