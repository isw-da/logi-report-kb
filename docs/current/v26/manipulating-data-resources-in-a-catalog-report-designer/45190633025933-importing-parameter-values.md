---
title: "Importing Parameter Values"
id: 45190633025933
section: "Manipulating Data Resources in a Catalog - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190633025933-Importing-Parameter-Values
updated_at: 2026-04-30T15:15:21Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Importing Parameter Values

When you run a report with parameters, Report prompts you to specify the parameter values. The values shown in the UIs for specifying the parameter values are fixed at development time. However, showing a default, fixed value at runtime is often not useful to users. Therefore, Report provides you the jet.util.ImportParamValues interface for importing different default values from outside class files, so that you can specify the default values flexibly. This topic describes how you can implement the interface to import parameter values.

The jet.util.ImportParamValues interface contains only one method: public Hashtable promptValues(String paramsName[]). See the Report Java API Documentation for more information about its usage.

The following shows the general procedure to implement the interface to import parameter values from a class file.

- Define a Java class file. Refer to the sample program ParamTest.java and TestParamList.java in <install_root>\help\samples\APIParameter for additional information. To import parameter values, implement the jet.util.ImportParamValues interface in your Java file. The class definition may be:
			package help.;

import java.util.*;

import jet.util.*;

public class ParamTest implements ImportParamValues

{

     public ParamTest()

    {

        //Class body
    }

    public Hashtable promptValues(String paramsName[])
    {

        //Class body

    }

}

The following explains more about the code:

- You can define the package name by yourself. In the sample code, we use "help" as the package name.

- Because the ImportParamValues interface is in the jet.util package, you have to import the class package jet.util.*.

- A public constructor method without parameters is required.

- Compile the Java file to generate the class file.

- Append the class path to the ADDCLASSPATH variable of setenv.bat/setenv.sh in <install_root>\bin for both Designer and Server. 

- Start Designer.

- Open the report with the parameter value that you want to import.

- In the Report Inspector, set the property Import Parameter Values of the report to be the class name that you just generated with the package name, and set Parameter List Auto to false.

The following two examples explain how to import parameter values and what you should be aware of while using this feature in further detail.

Example 1: Importing from a database

In the ParamTest.java sample program in <install_root>\help\samples\APIParameter, different values are assigned to the p_StartDate parameter by accessing values from an HSQL database. In the example, we create a report based on a query using this parameter in the query condition and use this report to explain how to import parameter values from a database, so that you do not need to type in the values one by one while specifying the parameter default value.

Note that in the sample program, the compareToIgnoreCase() method is used to compare the parameter name in the class file with the one in your report. This method is not case sensitive when performing the comparison.

Assume that you have installed your Designer in the default path, that is C:\LogiReport\Designer), take the following steps to create the report and import the parameter values.

- Make sure SampleReports.cat is the currently open catalog file. If not, navigate to File > Open Catalog to open it from <install_root>\Demo\Reports\SampleReports.

- 
Create a page report with a Group Above table in it based on the query CascadeParameter in Data Source 1, which displays Order Date and Order ID as the detail fields, and is grouped by Shipper Territory.

- Save the report as Report1.cls. 

- Compile ParamTest.java to generate ParamTest.class, and store the class file in C:\LogiReport\Designer\help. javac -classpath C:\LogiReport\Designer\lib\JREngine.jar; ParamTest.java

- Append C:\LogiReport\Designer\help to the ADDCLASSPATH variable of setenv.bat in C:\LogiReport\Designer\bin.

- Restart Designer and open Report1.cls.

- In the Report Inspector, find the report property Import Parameter Values and specify the class name with the full package name. In this example, type help.ParamTest, and then set the property Parameter List Auto to false.
     You cannot see the report node  in the resource tree of the Report Inspector by default. To show it, select the report tab node in the tree (in this example, the report 1 node), and then select Up on the Report Inspector toolbar.

- Save the report and catalog.

- Select the View tab to preview the report.

- In the Enter Parameter Values dialog box, select the drop-down list of the parameter. You can find that Designer imports all the values you have specified in ParamTest.java  into the list.

- Select one of the values with which to view the report.

- 
Publish the report to Server.

- Append C:\LogiReport\Designer\help to the ADDCLASSPATH variable of setenv.bat in <server_install_root>\bin.

- Start Server.

- On the Server Console, run the report and you then have the same parameter values as you did in Designer.

Example 2: Importing from a class file

Another example of applying the feature of importing parameter values is to specify your required default values. When you group/sort data dynamically with a parameter, when viewing the report, you may get many default values in the dialog box for specifying the parameter values. However, since you do not need so many values with which to group/sort, you can specify your required default values in a Java class, and then import them. For additional information, refer to the TestParamList.java sample program in <install_root>\help\samples\APIParameter.

To specify the default parameter values in a class file and then import them, take the following steps:

- Compile TestParamList.java to generate TestParamList.class, and store the class file in <install_root>\help.

- Append <install_root> to the ADDCLASSPATH variable of setenv.bat in <install_root>\bin.

- Start Designer.

- Create a report with a dynamic group/sort using the parameter ImportPara.

- Set the report property Parameter List Auto to true in the Report Inspector.

- Select the View tab to preview the report. In the Enter Parameter Values dialog box,  you can see many values in the parameter value drop-down list.

- Set Parameter List Auto to false and Import Parameter Value to TestParamList.

- Preview the report again. This time you can see that there are only four values listed in the Enter Parameter Values dialog box as defined in TestParamList.java.

- You need to ensure that the parameter format in the class file is consistent with that in Report, specifically, that the parameter format used in the class file is parsed when viewing the report so that Report Engine can return the correct data.

- When you implement the jet.util.ImportParamValues interface and use its promptValues() function, ensure that:
      
- The parameter of this function is a String array which contains the names of the parameters.

- The return value of this method is a Hashtable, its keys are parameter names used in the report and its values are vector objects which contain the parameter values.

- When there are subreports in a primary report, setting the properties Import Parameter Value and Parameter List Auto does not affect the subreports. That is, you have to set these properties in the primary report and subreports separately.

- If you want to use a parameter as the grouping/sorting criteria, you need to make sure that the parameter values are within the columns used in the report's query. In addition, the name should be consistent with the column names defined in the catalog. For example, the query of the report joins two tables: Orders and Orders Detail. In the Catalog Manager, expand the query used by the report. You then see all the columns from the two tables. Make sure that the returned values are within them and consistent with the column names.
