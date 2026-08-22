---
title: "Example 4: Adding a Dynamic UDS"
id: 1500009564262
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564262-Example-4-Adding-a-Dynamic-UDS
updated_at: 2021-07-24T05:55:44Z
---

# Example 4: Adding a Dynamic UDS

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585261-Example-3-Adding-a-Java-Object-Data-Source-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585301-Oracle-Stored-Procedure-UDS)

# Example 4: Adding a Dynamic UDS

Logi JReport Designer supports the Dynamic UDS feature. This feature improves performance by retrieving only the selected fields and not all the fields. At runtime, an option is provided for you to pick up the columns you want to see in the report. In this way, Logi JReport Designer generates a dynamic report according to your selection.

In this example, SQLDataSource is used to illustrate the usage and effect of the Dynamic UDS feature. Assume that you have generated SQLDataSource.class, start Logi JReport Designer with the modified batch file (for details, see [Compiling and running SQLDataSource](https://devnet.logianalytics.com/hc/en-us/articles/1500009564242-Example-2-Adding-an-SQL-Data-Source-UDS#Compile)).

1. Open an existing catalog.
2. In the Catalog Manager resource tree, expand the data source to which the UDS is to be added.
3. [Create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter) with the following information:
   * **Name**: sql
   * **Value Type**: String
   * **Prompt Values**:

     select \* from employee   
      select salary from employee  
      select employeeid, employeeposition, hiredate, notes, salary, photo from employee
4. Right-click the data source node, and then select **New User Defined Data Source** from the shortcut menu.
5. In the New User Defined Data Source dialog, enter the following information:
   * **Name**: employees
   * **Class Name**: SQLDataSource
   * **Parameter**: `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\Logi JReport\\Designer\\Demo\\db\\JRDemo"&USER=sa&PSWD=&SQL=@sql`
6. Select **OK** to add the UDS.

Next, we will create a page report directly on the UDS to test the Dynamic UDS feature. If you want to create web reports and library components on this UDS, you need to first [create a business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562602-Creating-a-Business-View) using this UDS.

1. Select **Home**/**File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog, specify the report name and choose the **Table (Group Left)** layout. Select **OK**.
3. In the Data screen of the Table Wizard, choose the UDS **employees** from the User Defined node. Then, select **Next**.
4. In the Display screen, add the fields EMPLOYEEID, employees\_NOTES, employees\_SALARY and HIREDATE to be displayed in the table, edit their display names to **ID**, **Notes**, **Salary**, **Hire Date**, and then select **Next**.
5. In the Group screen, specify to group on the field **EMPLOYEEPOSITION**.
6. Skip the Summary, Chart and filter screens, and in the Style screen, specify to display the report in the Warm style.
7. Select **Finish** to create the report.
8. Select the **View** tab to view the report. You will then be prompted to enter a parameter.
9. Select **select \* from employee** as the parameter, and you will see that data for all fields has been retrieved.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893965463/cnctn_uds_add_exmpl4_all.gif)
10. Go back and run this report again. This time, choose **select salary from employee**. You will notice that no groups are displayed and the group name changes to NULL. This is because only the field employees\_SALARY has been selected this time. Logi JReport Designer will make no reference to the employees\_Position column, on which the group is based.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889395991/cnctn_uds_add_exmpl4_null.gif)

**Note:** To make a dynamic UDS work, if the SQL statement at runtime doesn't include all the UDS columns, you need to make sure that none of the UDS columns' properties were edited, that is the Specify Columns option in the New User Defined Data Source dialog should be unchecked, otherwise exceptions will be produced when the SQL statement is used to generate a dynamic report from the UDS.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585261-Example-3-Adding-a-Java-Object-Data-Source-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585301-Oracle-Stored-Procedure-UDS)
