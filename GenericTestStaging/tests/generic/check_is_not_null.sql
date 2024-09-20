{% test check_is_not_null(model, column_name, threshold=10) %}

select * from {{ model }} where {{ column_name }} is not null
{% endtest %}

 