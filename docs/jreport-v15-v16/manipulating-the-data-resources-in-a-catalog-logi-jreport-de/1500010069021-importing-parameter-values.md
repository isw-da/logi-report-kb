---
title: "Importing Parameter Values"
id: 1500010069021
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010069021-Importing-Parameter-Values
updated_at: 2021-07-24T10:38:08Z
---

# Importing Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033422-Specifying-Parameter-Values) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068521-Formulas)

# Importing Parameter Values

When you run a report with parameters, Logi JReport will prompt you the Enter Parameter Values dialog to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500010033422-Specifying-Parameter-Values). The default values shown in the dialog are fixed at development time. However showing a default, fixed value often is not useful to users.

Logi JReport provides an interface for importing different default values from an outside class file so that the default values can be specified flexibly. There is only one method in this interface: *public Hashtable promptValues(String paramsName[])*. For detailed information about its usage, refer to the jet.util.ImportParamValues interface in the Logi JReport Javadoc located in `<install_root>\help\api`.

The following are the general steps for importing parameter values from a class file:

1. Define a Java class file. For help, see the sample program ParamTest.java and TestParamList.java in `<install_root>\help\samples\APIParameter`. To import parameter values, implement the interface jet.util.ImportParamValues in your Java file. The class definition may be as follows:

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

   * The package name can be defined by yourself. In our sample code, we use help as the package name.
   * Since the interface ImportParamValues is in the package jet.util, you will have to import the class package jet.util.\*.
   * A public constructor method without parameters is required.
2. Compile the Java file to generate the class file.
3. Append the class path to the ADDCLASSPATH variable of the file setenv.bat/setenv.sh in `<install_root>\bin` for both Logi JReport Designer and Logi JReport Server.
4. Start Logi JReport Designer with the modified batch file.
5. Open the report with the parameter value that you want to import.
6. In the Report Inspector, set the property Import Parameter Values of the report to be the class name that you just generated with the package name, and set Parameter List Auto to **false**.

The following two examples explain how to import parameter values and what you should be aware of while using this feature.

**Example 1: Importing from a database**

In the sample program ParamTest.java in `<install_root>\help\samples\APIParameter`, different values were assigned to the parameter p\_StartDate by accessing values from an HSQL database. We will create a report based on a query using this parameter in the query condition and use this report to explain how to import parameter values from a database, so that you do not need to type in the values one by one while specifying the parameter default value (note that in this example we assume your Logi JReport Designer is installed in the default path, that is `C:\JReport\Designer`).

Note that in the sample ParamTest.java, the method *compareToIgnoreCase()* is used to compare the parameter name in the class file with the one in your report. This method is not case sensitive when performing the comparison.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a group above table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) based on the query CascadeParameter in Data Source 1. The table displays the following detail fields: Order Date and Order ID, is grouped by Shipper Territory, and takes the Basic (Default) report style. Save the report as Report1.
3. Compile ParamTest.java to generate ParamTest.class, and store the class file in `C:\JReport\Designer\help`.  
     
   `javac -classpath c:\JReport\Designer\lib\JREngine.jar; ParamTest.java`
4. Append `C:\JReport\Designer\help` to the ADDCLASSPATH variable of setenv.bat in `C:\JReport\Designer\bin`.
5. Restart Logi JReport Designer and open Report1.
6. In the Report Inspector, find the report property **Import Parameter Values**, and input the class name with the full package name. In this example, input **help.ParamTest**, and then set the property Parameter List Auto to **false**.

   **Tip:** The report node is not shown in the resource tree of the Report Inspector by default. To have it shown, select the report tab node in the tree (in this example, the report 1 node), and then select the **Up** button ![Up button](https://devnet.logianalytics.com/hc/article_attachments/4404901115671/btn_up.gif) on the Report Inspector toolbar.
7. Save the report and catalog, and then view the report result.
8. In the Enter Parameter Values dialog, select the drop-down list of the parameter. You will find that all the values you specified in ParamTest.java have been imported into the list.
9. Select one of the values with which to view the report.
10. [Publish the saved report](https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources#Remotely) Report1 to Logi JReport Server.
11. Append `C:\JReport\Designer\help` to the ADDCLASSPATH variable of setenv.bat in `<server_install_root>\bin`.
12. Start Logi JReport Server with the modified batch file.
13. Load your web browser to access the Logi JReport Server console. You will then have the same parameter values as you did in Logi JReport Designer.

**Example 2: Importing from a class file**

In addition to Example 1, another example of applying the feature of importing parameter values is to specify your required default values. When you group/sort data dynamically with a parameter, when viewing the report, a dialog will be displayed, in which you will find many default values in the drop-down list. However, since you do not need so many values with which to group/sort, you can specify your required default values in a Java class, and then import them. For addidtional information, refer to the sample program TestParamList.java in `<install_root>\help\samples\APIParameter`.

To specify the default parameter values in a class file and then import them, follow the steps below:

1. Compile TestParamList.java to generate TestParamList.class, and store the class file in `<install_root>\help`.
2. Append `<install_root>` to the ADDCLASSPATH variable of setenv.bat in `<install_root>\bin`.
3. Start Logi JReport Designer.
4. Create a report with a [dynamic group/sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases#DynamicData) using the parameter ImportPara.
5. Set the report property Parameter List Auto to **true** in the Report Inspector, and view the report. Many values will be listed in the Enter Parameter Values dialog.
6. Set Parameter List Auto to **false**, Import Parameter Value to **TestParamList**, and view the report again. You will now see that only four values are displayed as defined in TestParamList.java.

**Notes:**

* You need to ensure that the parameter format in the class file is consistent with that in Logi JReport, specifically, that the parameter format used in the class file is parsed when viewing the report so that the correct data records will be returned.
* When you implement the interface jet.util.ImportParamValues and use its function *promptValues()*, ensure that:
  + The parameter of this function is a String array which contains the names of the parameters.
  + The return value of this method is a Hashtable, its keys are parameter names used in the report and its values are vector objects which contain the parameter values.
* When there are subreports in a primary report, setting the properties Import Parameter Value and Parameter List Auto will not affect them. That is, you have to set these properties in the primary report and subreports separately.
* If you want to use a parameter as grouping/sorting criteria, you will need to make sure that the parameter values are within the columns used in the report's query. In addition, the name should be consistent with the column names defined in the catalog. For example, the query of the report joins two tables: Orders and Orders Detail. In the Catalog Manager, expand the query used by the report. You will then see all the columns from the two tables. Make sure that the values returned are within them and consistent with the column names.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033422-Specifying-Parameter-Values) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068521-Formulas)
