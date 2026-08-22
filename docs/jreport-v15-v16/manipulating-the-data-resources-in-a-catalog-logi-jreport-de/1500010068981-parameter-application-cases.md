---
title: "Parameter Application Cases"
id: 1500010068981
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases
updated_at: 2021-07-24T10:38:09Z
---

# Parameter Application Cases

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033422-Specifying-Parameter-Values)

# Parameter Application Cases

In Logi JReport, parameters can be used in many situations. The usage of parameters can greatly facilitate your reporting work.

Below is a list of the sections covered in this topic:

* [Dynamically Filtering Queries](#FilterQuery)
* [Dynamically Grouping/Sorting Report Data](#DynamicData)
  + [Grouping Data Dynamically](#Group)
  + [Sorting Data Dynamically](#Sort)

* [Filtering a Parameter with Another Parameter](#FilterParam)
* [Controlling Multiple Parameters in a Report](#Control)
* [Applying RLS to Parameters](#RLS)
* [Supplementing WHERE Portions](#Portion)

## Dynamically Filtering Queries

You can use a parameter in a WHERE clause so that the query result can vary each time according to the entered parameter value. This is the most common usage of parameters.

The feature works the same for [Logi JReport queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Filter) created with the Query Editor, [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010034562-Creating-Business-Views-in-a-Catalog#Filter), [datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets#Filter), [imported SQL files](https://devnet.logianalytics.com/hc/en-us/articles/1500010064341-Imported-SQL-Files#Create) and [imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/1500010064441-Imported-APEs#Expression) (it is *$match* stage instead of WHERE clause for APE). When using imported SQL, simply put *@Parameter* or *:Parameter Name* directly into the SQL file to be imported; for imported APE, put *@Parameter* or *?Parameter Name* in the JSON file to be imported. Logi JReport will provide the default values when you import the file so the database recognizes the syntax.

The following example shows using a parameter to filter a Logi JReport query dynamically.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the desired data source and create a type-in parameter named IDSet of Integer type with the default values 1, 10, and 20, and enable the Allow Multiple Values option.
3. In the same data source, [create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog) CustomersInfo on the table Customers. Select all the fields contained in the table.
4. In the Query Editor, select **Menu** > **Query** > **Filter**.
5. Filter the records of the query by adding a condition as follows in the Search Condition dialog (for details, see [Filtering with the filter format](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Filter)):

   ![Add a condition in the Search Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901150487/prmtr_app_fltrqry1.gif)
6. [Create a page report with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) based on the query as follows: have the fields Customer ID, Customer Name, City and Phone displayed in the table and apply the Commercial style.
7. View the report. In the Enter Parameter Values dialog, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the value field of IDSet.
8. In the Enter Values dialog, uncheck the **All** option, add the listed values 1, 10, and 20 to the right box, and then select **OK**. You will find that the records with Customer ID equal to 1, 10 and 20 have been retrieved.

   ![Table records of certain Customer ID](https://devnet.logianalytics.com/hc/article_attachments/4404909139735/prmtr_app_fltrqry2.gif)
9. View the report again. This time, in the Enter Values dialog, remove 1, 10, and 20 from the Selected Values box first. Enter the values 3, 7, 9, 11, 15, and 25 in the Enter Values field and add them into the Selected Values box one by one. Then select **OK**. Now, the records for the specified Customer IDs are displayed.

   ![Table records of specified Customer IDs](https://devnet.logianalytics.com/hc/article_attachments/4404909139991/prmtr_app_fltrqry3.gif)

   To view the report with full data, select the **All** option and then select **OK** in the Enter Values dialog.

**Notes:**

* The parameter's data type must be set according to the field type and the manner in which you use the parameter. For example, if the field is a number, define a parameter to be Number type also.
* When specifying the value for a parameter used in a filter condition, if the parameter is of String type:
  + When the parameter is used for a Logi JReport query, imported SQL file, business view or dataset:
    - If it is used in the format *:ParameterName*, the parameter value you type should be with single quotation marks, for example, 'USA'.
    - If it is used in the format *@ParameterName*, the parameter value should be without single quotation marks, for example, USA. Once you input a parameter value with single quotation marks, the quotation marks will be recognized as a part of the parameter value.
  + When it is used for an imported APE, the parameter value should be with double quotation marks, for example, "USA".

  If the parameter is not of String type, you can type the parameter value directly, for example, 1234.

## Dynamically Grouping/Sorting Report Data

An important usage of parameters is to use them to dynamically group and sort data in a report, which enables the end users to specify the grouping and sorting conditions at runtime.

The Dynamic Group and Dynamic Sort features only apply to [tables](https://devnet.logianalytics.com/hc/en-us/articles/1500010063901-Tables) and [banded objects](https://devnet.logianalytics.com/hc/en-us/articles/1500010063281-Banded-Objects) created using query resources in page reports.

### Grouping Data Dynamically

You can make a multi-level group report by selecting a field as grouping criterion for the report. However, because the grouping criteria are definite, if you want to group several times according to different grouping criteria but based on the same query it is cumbersome. For example, you want to make three employee list reports with different grouping criteria, the first one is grouped by their first name, the second one is by the hire date and the third one is by their salary, then you have to repeat the steps of setting query, selecting fields as grouping criteria, and so on, which is not efficient.

For this case you can use the Dynamic Group feature of Logi JReport Designer, which means grouping criteria is a dynamic process. You don't need to repeat the same steps to make multiple reports with different grouping criteria. You can just predefine a parameter using String value type and add it to the group list. Then when you run the report, the parameter dialog prompts the end user to select a field to group by. All the acceptable group-by fields are listed in a drop-down list. You can select any of them as grouping criterion.

You can create a table in a page report as follows to achieve the goal:

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog, select the **Table (Group Left Above)** component type and select **OK**.
4. In the Data screen of the Table Wizard, select the query **EmployeeInformation** in Data Source 1. Select **Next**.
5. In the Display screen, add the following fields in the selected query to the table: Hire Date, Name, Home Phone and Salary. Select **Next**.
6. In the Resources box of the Group screen, select **<New Parameter...>** in the Parameters node to create a type-in parameter named pGroupBy of String type (leave the other settings to their default).
7. Specify to group the report on the just created parameter **pGroupBy** and use **Ascend** as the sorting order.

   ![Specify Parameter as Group-by Field](https://devnet.logianalytics.com/hc/article_attachments/4404901150743/prmtr_app_grp1.gif)
8. Select **Finish** in the Table Wizard to create the table.
9. Select the **View** tab to preview the report. The Enter Parameter Values dialog appears for you to specify the grouping criterion.

   ![Enter Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901150999/prmtr_app_grp2.gif)

   All the DBFields in the query the table uses and the valid formulas for these DBFields are listed in the pGroupBy drop-down list. You can select a field by which to group data in the table.
10. Select **Employee Position**  as the parameter value. Data in the table is then grouped by positions of the employees.

    ![Dynamic Grouped Table based on query](https://devnet.logianalytics.com/hc/article_attachments/4404901151255/prmtr_app_grp3.gif)
11. To group the data by hire date or salary, select **Hire Date** or **Salary** from the value drop-down list of pGroupBy.

### Sorting Data Dynamically

The following takes an example to show how to use the Dynamic Sort feature.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog, select the **Table (Group Above)** component type and select **OK**.
4. In the Data screen of the Table Wizard, select the query **EmployeeInformation** in Data Source 1. Select **Next**.
5. In the Display screen, add the following fields in the selected query to the table: Hire Date, Name, Home Phone and Salary.
6. Select the **Sort Fields By** button.
7. In the Sort Fields By dialog, select **<New Parameter...>** in the Parameters node in the Resources box to create a type-in parameter named pSortBy of String type (leave the other settings to their default).
8. Add the just created parameter **pSortBy** as the sort-by field.

   ![Specify Parameter as Sort-by Field](https://devnet.logianalytics.com/hc/article_attachments/4404901151639/prmtr_app_srt1.gif)
9. Select **Dynamic Sort** from the sort order drop-down list in the Sort column.
10. In the Specify Sort Order for dialog, input **SortBy Order**, then select **OK** to close the dialog.

    ![Specify Sort Order](https://devnet.logianalytics.com/hc/article_attachments/4404901151895/prmtr_app_srt2.gif)
11. Select **OK** in the Sort Fields By dialog to accept the changes.
12. Select **Finish** in the Create Table wizard to create the table.
13. Select the **View** tab to preview the table. The Enter Parameter Values dialog appears for you to specify the sort manner.

    ![Entrer Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901152151/prmtr_app_srt3.gif)
14. All the DBFields in the query the table uses and the valid formulas for these DBFields are listed in the pSortBy drop-down list. You can select a field by which to sort the data and then specify the sort order in the SortBy Order drop-down list.

    Here, we choose **Salary** from the pSortBy list and **DESCENDING** from the SortBy Order list. The records within each group are displayed in descending order according to their salary values.

    ![Sort the Table by Salary](https://devnet.logianalytics.com/hc/article_attachments/4404909140503/prmtr_app_srt4.gif)
15. Preview the table again and this time select **Name** from the pSortBy list and **ASCENDING** from the SortBy Order list. The table displays like this:

    ![Sort the Table by Name](https://devnet.logianalytics.com/hc/article_attachments/4404901152535/prmtr_app_srt5.gif)

## Filtering a Parameter with Another Parameter

You can use the value of one parameter to filter another one. In this way you can create your own cascading parameters such as using pCountry to filter the values returned by a parameter listing available states.

The following examples show you the two methods that you can use to achieve this purpose.

**Method 1** (Use this method when the SQL needed to select the parameter values is very simple.)

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the desired data source node.
3. Right-click the **Parameters**  node and then select **New Parameter**. The New Parameter dialog appears.
4. Enter **CasParam** in the Name field, select **Bind with Cascading Columns** from the Value Setting drop-down list, and then select **Customers** of the Tables type from the Data Source drop-down list.
5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) to add a parameter row, select **Region** as the Bind Column and Display Column, and then select in the Parameter cell to create the parameter in the cascading group.
6. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) to add another parameter row, select **Country** as the Bind Column and Display Column, and then select in the Parameter cell.
7. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) to add one more parameter row, select **City** as the Bind Column and Display Column, select in the Parameter cell, and then select **OK** in the dialog.

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901152791/prmtr_app_fltrprm3.gif)
8. In the same data source, [create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog) CustomersInfo on the table Customers and select all the fields in the table.
9. Filter the records of the query by adding a condition as follows in the Search Condition dialog (for details, see [Filtering with the filter format](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Filter)):

   ![Add a condition in the Search Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901153047/prmtr_app_fltrprm1.gif)
10. [Create a page report with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) based on the query, and have the fields Customer Name, City, Country and Region displayed in the report.
11. View the report and the Enter Parameter Values dialog appears.
12. From the region drop-down list, select a region, then only the countries in the selected region will be displayed in the country drop-down list. Choose a country from the list, and then only the cities in the selected country will be displayed in the city drop-down list.

    ![Enter parameter values](https://devnet.logianalytics.com/hc/article_attachments/4404909140759/prmtr_app_fltrprm2.gif)
13. Select **OK**. You will now find that only the specified records are shown.

**Method 2** (Use this method when you need more customized SQL to show the correct values.)

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the desired data source node.
3. Right-click the **Parameters**  node and then select **New Parameter**.
4. Create a parameter named ParamRegion, select **Bind with Single Column** from the Value Setting drop-down list, select **Tables and Views** from the Source drop-down list, select **Region** as the Bind Column and Display Column. Then in the value cell of the Import SQL option, you can see the following statement:

   `Select DISTINCT CUSTOMERS.REGION FROM CUSTOMERS`

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909141015/prmtr_app_fltrprm4.gif)
5. Create another parameter named ParamCountry. Bind it with the column Country, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) in the value cell of Import SQL and edit its SQL statement as follows:

   `Select DISTINCT CUSTOMERS.COUNTRY FROM CUSTOMERS WHERE (Customers.Region=@ParamRegion and Customers.YTDSALES > 0 )`
6. Create one more parameter named ParamCity. Bind it with the column City, and then edit its SQL statement as follows:

   `Select DISTINCT CUSTOMERS.City FROM CUSTOMERS WHERE (Customers.Country=@ParamCountry and Customers.YTDSALES > 0 )`
7. In the same data source, create a query CustomersInfo on the table Customers and select all the fields in the table, and filter the records of the query by adding a condition as follows:

   `CUSTOMERS.CITY=@ParamCity`
8. [Create a page report with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) based on the query, and have the fields Customer Name, City, Country and Region displayed in the report.
9. View the report. In the Enter Parameter Values dialog, you can use the value of ParamRegion to filter the value of ParamCounty, and use the value of ParamCounty to filter the value of ParamCity. You will not see any countries and cities where their are no sales.

## Controlling Multiple Parameters in a Report

When multiple parameters are used in a report, but you only want to show some of them when running it, you can group them and then select the parameter you want for the report. The parameter values not entered will use their default value. See the example below:

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand **Data Source 1**, then right-click the **Parameters** node and select **New Parameter**.
3. In the New Parameter dialog, enter **GroupParam** in the Name field, select **Parameters** from the Value Type drop-down list, then add three parameters as the default values of GroupParam as shown in the following image:

   ![New parameter](https://devnet.logianalytics.com/hc/article_attachments/4404909141271/prmtr_app_cntrl1.gif)
4. Open an existing page report. Insert the parameters P\_Category, P\_Month, P\_Country, and GroupParam into a report tab of the report.
5. View the report, and the Enter Parameter Values dialog appears. You can select the parameter you want from the GroupParam drop-down list.

   ![Enter Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909141527/prmtr_app_cntrl2.gif)

   Select @P\_Category, the P\_Category parameter is displayed in the dialog and you can select or type in a value for the parameter. If you select @P\_Month,@P\_Country, then both the parameters P\_Month and P\_Country will be displayed for you to specify values with which to run the report.

## Applying RLS to Parameters

For parameters [bound with DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog#Bind), you can apply [record level security (RLS) policies](https://devnet.logianalytics.com/hc/en-us/articles/1500010063241-Record-Level-and-Column-Level-Security#Data) of data source scope to them. The security policy is specified on the DBField that is bound to the parameter. At runtime, end users will only see parameter values which the security identifier allows to view in the parameter value drop-down list.

The following example explains how to apply RLS to the value drop-down list of a parameter in detail.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the data source where you want to create the parameter.
3. Right-click **Security Entry**  in the Security node, select **New Security Entry** on the shortcut menu, then name the security policy **CusCountry**.
4. In the Security dialog, make sure Valid RLS is checked at the bottom left.
5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) and select **Add User**. In the Add User dialog, enter **John** in the User text box and select **OK**.
6. In the Record Level Security tab, edit the security condition as below to make John has the permission to view records in Canada only (for details about how to compose a security condition, [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010063241-Record-Level-and-Column-Level-Security#Condition)).

   ![Set Permission for John](https://devnet.logianalytics.com/hc/article_attachments/4404901153303/prmtr_app_rls1.gif)
7. Add another user David which has the permission to view records in the United Kingdom only.
8. Select **OK** to exit the Security dialog.
9. In the same data source, right-click the **Parameters**  node and select **New Parameter** on the shortcut menu.
10. In the New Parameter dialog, enter **pCountry** in the Name field, select **Bind with Single Column** from the Value Setting drop-down list, and bind the parameter with the **Country** column. In the Options box, select **CusCountry** as value of Record Level Security, and then set the Distinct option to **true**. Select **OK**.

    ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901153559/prmtr_app_rls3.gif)
11. [Create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog) CustomersInfo on the table Customers. Select all the fields contained in the table.
12. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page)  based on the query, and have the fields Customer ID, Customer Name, Country and Phone displayed in the report.
13. In the Data panel, right-click the node that represents the query, and then select **Edit Query** from the shortcut menu.
14. In the Query Editor, select **Menu** > **Query** > **Filter**.
15. In the Search Condition dialog, add a condition for the query as follows (for details, see [Filtering with the filter format](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Filter)):

    ![Add a condition in the Search Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901153815/prmtr_app_rls2.gif)
16. Select **OK** to apply the changes to the query.
17. Select **File** > **Options**, in the General category of the Options dialog, set the User Name as **John**.
18. View the report, and the Enter Parameter Values dialog is displayed.
19. Select the parameter value drop-down list, and you can see that only Canada is displayed for the user name.

    ![Enter Parameter Value dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901154071/prmtr_app_rls4.gif)
20. Set the user name as **David** in the Options dialog and view the report again. You will find that only the value United Kingdom is displayed in the parameter value drop-down list this time.

**Notes:**

* When applying an RLS policy to a parameter bound with a column, you must make sure the parameter's bound column and the column used to set conditions in the RLS policy are in the same table. In addition, if the RLS policy also contains conditions defined on other columns, all the columns must be in the same table, and the RLS policy cannot contain parameters and formulas; otherwise, when you apply the RLS to the parameter, the RLS would not work properly.
* When you have applied an RLS policy to a parameter and then you edit the SQL statement of the parameter via the Import SQL option in the parameter dialog, the parameter value drop-down list may be Null because the changed SQL statement may not match the permissions of the RLS.
* When previewing a report that contains parameters applied with RLS in the Page Report Result or Web Report Result format in Logi JReport Designer, you need to make sure your RLS policy contains the user Jinfonet. That is because the user Jinfonet is the default and only user of the preview server. Any other users in the RLS policy cannot be recognized by the preview server.

## Supplementing WHERE Portions

Logi JReport allows you to change a query at runtime using the API. To do this, you can call the method *setWherePortion()* from your Java application. However, by calling this method, the original WHERE portion of the query will be replaced. If you want to append the runtime WHERE portion to the original one instead of replacing it/them, you can do it in the following way without using the Java API:

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the desired data source and create a type-in parameter named p\_Portion of String type (leave the other settings to their default).
3. In the same data source, [create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog) CustomersInfo on the table Customers. Select all the fields contained in the table.
4. [Create a page report with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) based on the query, and have the fields Customer ID, Customer Name, City and Phone displayed in the report, then apply the Commercial style.
5. In the Data panel, right-click the node that represents the query, and then select **Edit Query** from the shortcut menu.
6. In the Query Editor, select **Menu** > **Query** > **Filter**.
7. In the Search Condition dialog, add two condition lines (WHERE portions) for the query as follows (for details, see [Filtering with the filter format](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Filter)):

   **![Add conditions in the Search Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901154327/prmtr_app_prtn1.gif)**

   The colon is used to append the parameter value (of String type) to the first condition line instead of replacing it.
8. Select **OK** to apply the change to the query.
9. View the report, and in the Enter Parameter Values dialog, write a WHERE portion in standard SQL syntax as value of p\_Portion, for example, CUSTOMERID<20. Then, both of the two WHERE portions will be used to filter the query.

   ![Report Result](https://devnet.logianalytics.com/hc/article_attachments/4404909141783/prmtr_app_prtn2.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033422-Specifying-Parameter-Values)
