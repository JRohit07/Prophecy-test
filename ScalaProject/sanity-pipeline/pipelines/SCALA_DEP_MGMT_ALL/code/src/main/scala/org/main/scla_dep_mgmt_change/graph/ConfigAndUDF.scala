package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object ConfigAndUDF {

  def apply(context: Context, in: DataFrame): DataFrame = {
    val Config = context.config
    in.select(
      col("customer_id"),
      col("first_name"),
      col("last_name"),
      col("phone"),
      col("email"),
      col("country_code"),
      col("account_open_date"),
      col("account_flags"),
      concat(
        col("customer_id"),
        lit(Config.c_config_45),
        lit(Config.CONFIG_STR),
        lit(Config.CONFIG_BOOLEAN),
        lit(Config.CONFIG_DOUBLE),
        lit(Config.CONFIG_INT),
        lit(Config.CONFIG_FLOAT)
      ).as("config_values"),
      udf_multiply(col("customer_id").cast(IntegerType))
        .as("udf_multiply_usage"),
      udf_string_null_safe(col("first_name")).as("udf_string_null_safe_usage"),
      concat(lit(Config.c_str), col("first_name")).as("c_config"),
      concat(lit(Config.c_array_complex(0).car_record.carr_double),
             lit(Config.c_record_complex.cr_array_record(0).crar_double)
      ).as("c_complex_config"),
      expr(Config.c_record_complex.cr_array_record(0).crar_spark_expression)
        .as("c_complex_expr"),
      c_another_complex_expression(context).as("c_another_complex_expression"),
      expr(
        "named_struct('a', named_struct('test1', named_struct('test- another', 2)), 'b', named_struct('test1', named_struct('test- another', 2)))"
      ).as("c_struct.test1.mainstruct"),
      col("customer_id").as("nested.field.customer_id"),
      col("first_name").as("nested.field.first_name")
    )
  }

  def c_another_complex_expression(context: Context) = {
    val spark  = context.spark
    val Config = context.config
    when(
      !when(
        coalesce(
          (string_length(col("first_name").cast(StringType)) === lit(8))
            .and(string_length(col("first_name").cast(StringType)) === lit(8))
            .and(
              (string_length(col("first_name").cast(StringType)) === lit(8))
                .and(
                  string_length(col("first_name").cast(StringType)) === lit(
                    Config.c_record_complex.cr_array_record(0).crar_int
                  ).cast(IntegerType)
                )
            )
            .and(
              (!when(
                length(trim(col("first_name").cast(StringType))) === lit(8),
                date_format(to_date(trim(col("first_name").cast(StringType)),
                                    "yyyyMMdd"
                            ),
                            "yyyyMMdd"
                )
              ).isNull === lit(10))
                .and(
                  !when(
                    length(trim(col("first_name").cast(StringType))) === lit(8),
                    date_format(
                      to_date(trim(col("first_name").cast(StringType)),
                              "yyyyMMdd"
                      ),
                      "yyyyMMdd"
                    )
                  ).isNull === lit(10)
                )
                .and(
                  !when(
                    length(trim(col("first_name").cast(StringType))) === lit(8),
                    date_format(
                      to_date(trim(col("first_name").cast(StringType)),
                              "yyyyMMdd"
                      ),
                      "yyyyMMdd"
                    )
                  ).isNull === lit(10)
                )
            ),
          lit(0).cast(BooleanType)
        ),
        lit(1).cast(BooleanType)
      ).when(
          coalesce(
            array_contains(array(lit(6), lit(7)),
                           string_length(col("first_name").cast(StringType))
            ).and(
                array_contains(array(lit(6), lit(7)),
                               string_length(col("first_name").cast(StringType))
                )
              )
              .and(
                !when(
                  length(
                    trim(
                      (lit(19000000) + col("first_name")
                        .cast(DecimalType(9, 0))).cast(StringType)
                    )
                  ) === lit(8),
                  date_format(to_date(trim(
                                        (lit(19000000) + col("first_name").cast(
                                          DecimalType(9, 0)
                                        )).cast(StringType)
                                      ),
                                      "yyyyMMdd"
                              ),
                              "yyyyMMdd"
                  )
                ).isNull === lit(1)
              ),
            lit(0).cast(BooleanType)
          ),
          lit(1).cast(BooleanType)
        )
        .otherwise(lit(0).cast(BooleanType))
        .cast(BooleanType),
      date_format(to_timestamp(lit(Config.AI_MIN_DATETIME),
                               "yyyy-MM-dd HH:mm:ss"
                  ),
                  "yyyyMMdd"
      )
    ).when(
        coalesce(
          (string_length(col("first_name").cast(StringType)) === lit(8)).and(
            !when(length(trim(col("first_name").cast(StringType))) === lit(8),
                  date_format(to_date(trim(col("first_name").cast(StringType)),
                                      "yyyyMMdd"
                              ),
                              "yyyyMMdd"
                  )
            ).isNull === lit(1)
          ),
          lit(0).cast(BooleanType)
        ),
        col("first_name").cast(StringType)
      )
      .when(
        coalesce(
          array_contains(array(lit(6), lit(7)),
                         string_length(col("first_name").cast(StringType))
          ).and(
            !when(
              length(
                trim(
                  (lit(19000000) + col("first_name").cast(DecimalType(9, 0)))
                    .cast(StringType)
                )
              ) === lit(8),
              date_format(to_date(trim(
                                    (lit(19000000) + col("first_name")
                                      .cast(DecimalType(9, 0))).cast(StringType)
                                  ),
                                  "yyyyMMdd"
                          ),
                          "yyyyMMdd"
              )
            ).isNull === lit(1)
          ),
          lit(0).cast(BooleanType)
        ),
        (lit(19000000) + col("first_name").cast(DecimalType(9, 0)))
          .cast(StringType)
      )
      .otherwise(
        concat(lit(Config.c_array_complex(0).car_record.carr_double),
               lit(Config.c_record_complex.cr_array_record(0).crar_double)
        )
      )
  }

}
