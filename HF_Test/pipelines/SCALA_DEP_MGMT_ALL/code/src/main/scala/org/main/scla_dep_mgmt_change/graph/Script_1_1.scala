package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.udfs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Script_1_1 {
  def apply(context: Context, in0: DataFrame): DataFrame = {
    val spark = context.spark
    val Config = context.config
    // Import Spark.ml libraries
    import org.apache.spark.ml.regression.LinearRegression
    import org.apache.spark.ml.feature.VectorAssembler
    
    // Prepare the data by assembling features into a single vector column
    
    val assembler = new VectorAssembler()
      .setInputCols(Array("Crime_Rate", "Residential_Land_Zone", "Non_retail_Business_acres", "Charles_River", "Nitric_Oxide", "Average_Rooms", "Owner_Occupied_Units", "Distance_to_Employment_Centers", "Accessibility_to_Highways", "Property_Tax_Rate", "Pupil_Teacher_Ratio", "Lower_Status"))
      .setOutputCol("features")
    
    val df = assembler.transform(in0)
    
    // Split data into training and test
    val Array(train, test) = df.randomSplit(Array(0.7, 0.3))
    
    // create linear regression model
    val lr = new LinearRegression()
      .setLabelCol("Y_Value_of_Occupied_Homes")
      .setFeaturesCol("features")
    
      // fit the model to the training data
    val model = lr.fit(train)
    
    // Make predictions on the test data
    val predictions = model.transform(test)
    
    //Dropping "features" vector column will result in dataframe output working
    // val predictions2 = predictions.drop("features")
    
    val out0 = predictions
    
    // val out0=in0
    out0
  }

}
