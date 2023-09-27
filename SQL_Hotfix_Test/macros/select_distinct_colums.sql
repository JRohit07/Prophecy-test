{% macro select_distinct_colums(table, col) %}
select * from {{table}} where {{col}} > 10
{% endmacro %}

 