{% test check_is_not_null(model=sd, column_name=sdf, threshold=10) %}


select * from {{ model }} where {{ column_name }} is not null
{% endtest %}

 