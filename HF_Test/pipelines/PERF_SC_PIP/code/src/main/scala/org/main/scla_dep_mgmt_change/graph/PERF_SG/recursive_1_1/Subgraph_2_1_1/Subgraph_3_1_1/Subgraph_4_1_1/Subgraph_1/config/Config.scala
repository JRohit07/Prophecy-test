package org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.config

import org.apache.spark.sql._
import io.prophecy.libs._
import pureconfig._
import pureconfig.generic.ProductHint
import org.apache.spark.sql.SparkSession
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.config.{
  Config => Subgraph_2_Config
}

object Config {

  implicit val confHint: ProductHint[Config] =
    ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))

  implicit val interimOutput: InterimOutput = InterimOutputHive2("")
}

case class Config(
  @Description("this is jdbc user") JDBC_USER:       String = "test_user",
  @Description("this is source table") SOURCE_TABLE: String = "test_table",
  db_secrets:                                        Option[DatabricksSecret] = None,
  JDBC_URL:                                          String = "jdbc:mysql://18.144.156.219:3306/test_database",
  JDBC_SOURCE_TABLE:                                 String = "test_table",
  CONFIG_STR:                                        String = "jdbc_url-${JDBC_URL}",
  CONFIG_BOOLEAN:                                    Boolean = true,
  CONFIG_DOUBLE:                                     Double = 123123.12321321d,
  CONFIG_INT:                                        Int = 3243423,
  CONFIG_FLOAT:                                      Float = 3454.3455f,
  c_limit_11:                                        Int = 11,
  c_st_expr:                                         String = "concat(`c_struct-c_short`, `c_struct-c_decimal`)",
  c_st_long:                                         String = "c_array_long",
  c_st_rename:                                       String = "c_array_boolean_renamed",
  c_dedup_expr:                                      String = "concat(c_array_float, `c_array_int`)",
  c_dedup_col:                                       String = " c_array_date",
  c_rd_expr:                                         String = "`c -  boolean _  ` in (true,false)",
  c_12321:                                           Int = 12321,
  c_0:                                               Int = 0,
  c_1:                                               Int = 1,
  c_join_expr:                                       String = "in0.`-- c-long`=in1.`-- c-long`",
  c_join_cshort:                                     String = "in0.`c   short  --`",
  c_orderby_expr:                                    String = "concat(`c  date`, c_timestamp)",
  c_orderby_int:                                     String = "`c-int-column type`",
  c_filter_expression:                               String = "customer_id >5",
  c_reformat_complex: String =
    "case     when c_int > 10 then         case              when NOT (NOT (c_string like '%1%')) then 'A'             when NOT (NOT (trim(trim(c_string)) = '')) then 'B'             else 'X'         end     when c_int <= 10 then         case             when NOT (NOT (c_string like '%1%')) then 'C'             when NOT (NOT (c_string not like '%2%')) then 'D'             else 'Z'         end     else null end",
  c_repartition_colname: String = "`c_float-__  `",
  c_repartition_expr: String =
    "concat(`c  - int`, `c_struct -- _  `.`c_string - of a struct -- _`)",
  c_agg_expr:  String = "first(c1)",
  c_agg_group: String = "concat(c1, c2, c3)",
  c_agg_c3:    String = "c3",
  c_row:       String = "row_number()",
  c_bool:      String = "`c -  boolean _  `",
  c_short:     String = "`c- short`",
  c_sql_expr:  String = "%[^aeiou]@%",
  c_sql_c8c1:  Int = -1,
  c_regex1: String =
    "^[_A-Za-z0-9-]+(\\\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9]+(\\\\.[A-Za-z0-9]+)*(\\\\.[A-Za-z]{2,})",
  c_regex2: String = "((?=.*)(?=.*[a-z$$])(?=.*[A-Z])(?=.*[@#%]).{6,20})",
  c_str:    String = "stringwith$$one#%^&*()-=!@#",
  c_new_sqlexpr: String =
    "select * from in0 where cast(SUBSTRING(in0.c9_udf1_c2, 1,2) as int) > -1",
  @Description("c array complex") c_array_complex: List[C_array_complex] = List(
    C_array_complex(
      car_array_spark_expression =
        List("concat(first_name, last_name)",
             "concat(first_name, last_name, last_name)"
        ),
      car_record = Car_record(carr_double = 2.2132312e7d, carr_short = 22),
      car_string = "test string",
      car_array_float = List(10.12f, -10.12f, 0.0f),
      car_int = -5446
    ),
    C_array_complex(
      car_array_spark_expression = List("concat(first_name, 'a')"),
      car_record = Car_record(carr_double = 2.2344234e7d, carr_short = 12),
      car_string = "this is another item",
      car_array_float = List(22.23432f),
      car_int = 234234
    )
  ),
  @Description("c record complex") c_record_complex: C_record_complex =
    C_record_complex(),
  c_config_1:  String = "test config 12#%^&*()-=",
  c_config_2:  String = "test config 12#%^&*()-=",
  c_config_3:  String = "test config 12#%^&*()-=",
  c_config_4:  String = "test config 12#%^&*()-=",
  c_config_5:  String = "test config 12#%^&*()-=",
  c_config_6:  String = "test config 12#%^&*()-=",
  c_config_7:  String = "test config 12#%^&*()-=",
  c_config_8:  String = "test config 12#%^&*()-=",
  c_config_9:  String = "test config 12#%^&*()-=",
  c_config_10: String = "test config 12#%^&*()-=",
  c_config_11: String = "test config 12#%^&*()-=",
  c_config_12: String = "test config 12#%^&*()-=",
  c_config_13: String = "test config 12#%^&*()-=",
  c_config_14: String = "test config 12#%^&*()-=",
  c_config_15: Option[String] = None,
  c_config_16: String = "test config 12#%^&*()-=",
  c_config_17: String = "test config 12#%^&*()-=",
  c_config_18: String = "test config 12#%^&*()-=",
  c_config_19: String = "test config 12#%^&*()-=",
  c_config_20: String = "test config 12#%^&*()-=",
  c_config_21: String = "test config 12#%^&*()-=",
  c_config_22: String = "test config 12#%^&*()-=",
  c_config_23: String = "test config 12#%^&*()-=",
  c_config_24: String = "test config 12#%^&*()-=",
  c_config_25: String = "test config 12#%^&*()-=",
  c_config_26: String = "test config 12#%^&*()-=",
  c_config_27: String = "test config 12#%^&*()-=",
  c_config_28: String = "test config 12#%^&*()-=",
  c_config_29: String = "test config 12#%^&*()-=",
  c_config_30: String = "test config 12#%^&*()-=",
  c_config_31: String = "test config 12#%^&*()-=",
  c_config_32: String = "test config 12#%^&*()-=",
  c_config_33: String = "test config 12#%^&*()-=",
  c_config_34: String = "test config 12#%^&*()-=",
  c_config_35: String = "test config 12#%^&*()-=",
  c_config_36: String = "test config 12#%^&*()-=",
  c_config_37: String = "test config 12#%^&*()-=",
  c_config_38: String = "test config 12#%^&*()-=",
  c_config_39: String = "test config 12#%^&*()-=",
  @Description(
    "this is random configs description long running this is random configs description long runningthis is random configs description long runningthis is random configs description long runningthis is random configs description long runningthis is random configs description long runningthis is random configs description long runningthis is random configs description long running"
  ) c_config_40:   String = "test config 12#%^&*()-=",
  c_config_41:     String = "test config 12#%^&*()-=",
  c_config_42:     String = "test config 12#%^&*()-=",
  c_config_43:     String = "test config 12#%^&*()-=",
  c_config_44:     String = "test config 12#%^&*()-=",
  c_config_45:     String = "test config 12#%^&*()-=",
  c_config_46:     String = "test config 12#%^&*()-=",
  c_config_47:     String = "test config 12#%^&*()-=",
  c_config_48:     String = "test config 12#%^&*()-=",
  c_config_49:     String = "test config 12#%^&*()-=",
  c_config_50:     String = "this is test string",
  AI_MIN_DATETIME: String = "2019-06-24 12:01:19",
  Subgraph_2:      Subgraph_2_Config = Subgraph_2_Config()
) extends ConfigBase

object C_array_complex {

  implicit val confHint: ProductHint[C_array_complex] =
    ProductHint[C_array_complex](ConfigFieldMapping(CamelCase, CamelCase))

}

case class C_array_complex(
  car_string:                 String,
  car_array_float:            List[Float],
  car_record:                 Car_record,
  car_array_spark_expression: List[String],
  car_int:                    Int
)

object Car_record {

  implicit val confHint: ProductHint[Car_record] =
    ProductHint[Car_record](ConfigFieldMapping(CamelCase, CamelCase))

}

case class Car_record(carr_double: Double, carr_short: Short)

object C_record_complex {

  implicit val confHint: ProductHint[C_record_complex] =
    ProductHint[C_record_complex](ConfigFieldMapping(CamelCase, CamelCase))

}

case class C_record_complex(
  cr_string:        String = "this is me son another complex",
  cr_array_boolean: List[Boolean] = List(true, false),
  cr_record:        Cr_record = Cr_record(),
  cr_array_record: List[Cr_array_record] = List(
    Cr_array_record(
      crar_int = 234234,
      crar_bool = true,
      crar_string = "this is my string lift",
      crar_spark_expression = "concat(first_name, first_name)",
      crar_short = 12,
      crar_float = 2343.234f,
      crar_long = 234324L,
      crar_double = 3.4543523e7d
    )
  )
)

object Cr_record {

  implicit val confHint: ProductHint[Cr_record] =
    ProductHint[Cr_record](ConfigFieldMapping(CamelCase, CamelCase))

}

case class Cr_record(
  crr_float:            Option[Float] = None,
  crr_spark_expression: String = "concat(first_name, last_name)",
  crr_array_short:      List[Short] = List(33, 44, 55, 66, 0)
)

object Cr_array_record {

  implicit val confHint: ProductHint[Cr_array_record] =
    ProductHint[Cr_array_record](ConfigFieldMapping(CamelCase, CamelCase))

}

case class Cr_array_record(
  crar_bool:             Boolean,
  crar_double:           Double,
  crar_float:            Float,
  crar_int:              Int,
  crar_long:             Long,
  crar_short:            Short,
  crar_string:           String,
  crar_spark_expression: String
)

object DatabricksSecret {

  implicit val myIntReader: ConfigReader[DatabricksSecret] =
    ConfigReader[String].map { s =>
      val Array(scope, key) = s.split(":")
      DatabricksSecret(scope, key)
    }

}

case class DatabricksSecret(scope: String, key: String) {

  override def toString: String = {
    import com.databricks.dbutils_v1.DBUtilsHolder.dbutils
    dbutils.secrets.get(scope = scope, key = key)
  }

}

case class Context(spark: SparkSession, config: Config)
