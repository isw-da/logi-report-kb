---
title: "Importing Parameter Values"
id: 1500010061262
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061262-Importing-Parameter-Values
updated_at: 2021-07-23T19:16:19Z
---

# Importing Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061282-Specifying-Parameter-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060962-Working-with-Formulas)

# Importing Parameter Values

When you run a report with parameters, Logi Report prompts you to specify the parameter values. The values shown in the UIs for specifying the parameter values are fixed at development time; however, showing a default, fixed value at runtime is often not useful to the report users. Therefore, Logi Report provides you the interface jet.util.ImportParamValues for importing different default values from outside class files, so that you can specify the default values flexibly. This topic describes how you can implement the interface to import parameter values.

The interface jet.util.ImportParamValues contains only one method: *public Hashtable promptValues(String paramsName[])* (for more information about its usage, refer to the Logi Report Javadoc).

The following shows the general procedure to implement the interface to import parameter values from a class file:

1. Define a Java class file. Refer to the sample program **ParamTest.java** and **TestParamList.java** in `<install_root>\help\samples\APIParameter` for additional information. To import parameter values, implement the interface jet.util.ImportParamValues in your Java file. The class definition may be as follows:

   ```
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
   ```

   The following explains the code:

   * You can define the package name by yourself. In the sample code, we use "help" as the package name.
   * Since the interface ImportParamValues is in the package jet.util, you have to import the class package jet.util.\*.
   * A public constructor method without parameters is required.
2. Compile the Java file to generate the class file.
3. Append the class path to the ADDCLASSPATH variable of the file **setenv.bat**/**setenv.sh** in `<install_root>\bin` for both Designer and Server.
4. Start Designer.
5. Open the report with the parameter value that you want to import.
6. In the Report Inspector, set the property **Import Parameter Values** of the report to be the class name that you just generated with the package name, and set **Parameter List Auto** to **false**.

The following two examples explain how to import parameter values and what you should be aware of while using this feature in further detail:

**Example 1: Importing from a database**

In the sample program ParamTest.java in `<install_root>\help\samples\APIParameter`, different values are assigned to the parameter "p\_StartDate" by accessing values from an HSQL database. In the example, we create a report based on a query using this parameter in the query condition and use this report to explain how to import parameter values from a database, so that you do not need to type in the values one by one while specifying the parameter default value.

Note that in the sample ParamTest.java, the method *compareToIgnoreCase()* is used to compare the parameter name in the class file with the one in your report. This method is not case sensitive when performing the comparison.

Assume that you have installed your Designer in the default path, that is `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer`), take the following steps to create the report and import the parameter values.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a group above table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) based on the query CascadeParameter in Data Source 1, which displays the following detail fields: Order Date and Order ID, is grouped by Shipper Territory, and applies the Basic (Default) report style. Save the report as **Report1.cls**.
3. Compile ParamTest.java to generate **ParamTest.class**, and store the class file in `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help`.  
     
   `javac -classpath C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\JREngine.jar; ParamTest.java`
4. Append `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help` to the ADDCLASSPATH variable of setenv.bat in `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\bin`.
5. Restart Designer and open Report1.cls.
6. In the Report Inspector, find the report property **Import Parameter Values** and specify the class name with the full package name. In this example, type **help.ParamTest**, and then set the property **Parameter List Auto** to **false**.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You cannot see the report node in the resource tree of the Report Inspector by default. To have it shown, select the report tab node in the tree (in this example, the **report 1** node), and then select the **Up** button ![Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848374679/btn_up.gif) on the Report Inspector toolbar.
7. Save the report and catalog.
8. Select the **View** tab to preview the report result.
9. In the Enter Parameter Values dialog box, select the drop-down list of the parameter. You can find that Designer imports all the values you have specified in ParamTest.java into the list.
10. Select one of the values with which to view the report.
11. [Publish the report](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#Remotely) to Server.
12. Append `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help` to the ADDCLASSPATH variable of setenv.bat in `<server_install_root>\bin`.
13. Start Server.
14. In the Server Console, run the report and you then have the same parameter values as you did in Designer.

**Example 2: Importing from a class file**

Another example of applying the feature of importing parameter values is to specify your required default values. When you group/sort data dynamically with a parameter, when viewing the report, you may get many default values in the dialog box for specifying the parameter values. However, since you do not need so many values with which to group/sort, you can specify your required default values in a Java class, and then import them. For additional information, refer to the sample program TestParamList.java in `<install_root>\help\samples\APIParameter`.

To specify the default parameter values in a class file and then import them, follow the steps below:

1. Compile TestParamList.java to generate **TestParamList.class**, and store the class file in `<install_root>\help`.
2. Append `<install_root>` to the ADDCLASSPATH variable of setenv.bat in `<install_root>\bin`.
3. Start Designer.
4. Create a report with a [dynamic group/sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#DynamicData) using the parameter **ImportPara**.
5. Set the report property **Parameter List Auto** to **true** in the Report Inspector.
6. Select the **View** tab to preview the report. In the Enter Parameter Values dialog box, you can see many values in the parameter value drop-down list.
7. Set Parameter List Auto to **false** and **Import Parameter Value** to **TestParamList**.
8. Preview the report again. This time you can see that there are only four values listed in the Enter Parameter Values dialog box as defined in TestParamList.java.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* You need to ensure that the parameter format in the class file is consistent with that in Logi Report, specifically, that the parameter format used in the class file is parsed when viewing the report so that Logi Report Engine can return the correct data records.
* When you implement the interface jet.util.ImportParamValues and use its function *promptValues()*, ensure that:
  + The parameter of this function is a String array which contains the names of the parameters.
  + The return value of this method is a Hashtable, its keys are parameter names used in the report and its values are vector objects which contain the parameter values.
* When there are subreports in a primary report, setting the properties Import Parameter Value and Parameter List Auto does not affect the subreports. That is, you have to set these properties in the primary report and subreports separately.
* If you want to use a parameter as the grouping/sorting criteria, you need to make sure that the parameter values are within the columns used in the report's query. In addition, the name should be consistent with the column names defined in the catalog. For example, the query of the report joins two tables: Orders and Orders Detail. In the Catalog Manager, expand the query used by the report. You then see all the columns from the two tables. Make sure that the returned values are within them and consistent with the column names.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061282-Specifying-Parameter-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060962-Working-with-Formulas)
