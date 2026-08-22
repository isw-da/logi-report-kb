---
title: "Built-in UDOs: JHyperLink and JRotator"
id: 1500009629341
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629341-Built-in-UDOs-JHyperLink-and-JRotator
updated_at: 2021-07-24T16:05:11Z
---

# Built-in UDOs: JHyperLink and JRotator

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629361-Inserting-UDOs-into-a-Page-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605522-Barcodes)

# Built-in UDOs: JHyperLink and JRotator

Logi Report provides two built-in UDOs: JHyperLink and JRotator. JHyperLink is used to create hyperlinks in reports, and JRotator to rotate text or images.

This topic includes the following sections:

> * [Creating Links with JHyperLink](#JHyperLink)
>   + [Example 1: Building Hyperlinks Using JHyperLink](#BuildLink)
>   + [Example 2: Linking Reports Using Parameters with JHyperLink](#LinkReport)
> * [Rotating Text/Image with JRotator](#JRotator)
>   + [Using JRotator to Rotate Text](#Text)
>   + [Using JRotator to Rotate an Image](#Image)
>   + [Using JRotator to Rotate a DBField](#DBField)

## Creating Links with JHyperLink

JHyperLink can be used to create hyperlinks in page reports that are created using query resources. The following shows two specific examples about using JHyperLink.

### Example 1: Building Hyperlinks Using JHyperLink

Sometimes you have a number of reports that contain different views of the same data. You may want to build a summary report to organize these reports together. For example, Report A is Summary Information for Orders, while Report B is an Invoice Report showing the detail line items of the order. When you select on the Order ID in Report A, it will go to the detail page of that order in Report B. With this hyperlink feature, you can build hyperlinks among reports. In addition, you can also insert any hyperlink to be invoked. In any case, a web browser will be displayed to view the specified pages.

1. Start Logi Report Designer and open the report in which you want to build a hyperlink.
2. Select **Insert** > **UDO** to display the Insert UDO dialog.
3. Select **JHyperLink** from the UDO drop-down list, and then select **OK**. You will then be able to insert a hyperlink into the report.

   ![Insert UDO - JHyperlink](https://devnet.logianalytics.com/hc/article_attachments/4404904422935/cmpnt_udo_bltin_jhylk.gif)
4. Keep the JHyperLink focused, and then go to the Report Inspector.
5. Type **http://localhost:8888** in the value cell of the URL property as the Logi Report Server address, make sure the Executer Class Name value is jet.udos.IEExecuter, and then type **Logi ReportServer**  in the Display Value property value cell as the display name of the hyperlink.
6. Insert another hyperlink using the same way and define its properties in the Report Inspector as follows:
   * **URL**: http://www.logianalytics.com
   * **Executer Class Name**: jet.udos.IEExecuter (the default value)
   * **Display Value**: Website

   Two hyperlinks have been successfully built into the report.
7. In view mode, select the **Logi ReportServer**  hyperlink that you just made. It will bring out a browser session to connect with Logi Report Server. Make sure that you have launched Logi Report Server and that the URL corresponds with your server configuration.
8. Select the **Website** hyperlink. You will then see the [http://www.logianalytics.com](http://www.logianalytics.com/) home page in a web browser.

**Note:** After you insert a JHyperLink into a report which is to be exported to PDF, Excel, or HTML, you can specify whether to make the hyperlink effective by setting a property which corresponds to the format type. Respectively, they are: Enable Hyperlink in PDF for PDF, Enable Hyperlink in Excel for Excel, and Enable Hyperlink in HTML for HTML.

### Example 2: Linking Reports Using Parameters with JHyperLink

JHyperLink can be used to link reports similar to master and detail reports to show related information, such as Order detail to higher level Year to Date Sales. You can use the JHyperLink object to control the URL to show the information in the linked reports on Logi Report Server. It is similar to [master/detail](https://devnet.logianalytics.com/hc/en-us/articles/1500009613322-Adding-Links-in-Reports#Detail) but does not have the ability to navigate through the detail and return to the master. The key to using JHyperlink is learning how to use URLs to call page reports. For additional information, refer to Running Reports in the *Logi Report Server Guide*.

An example is provided for your better understanding about how to use JHyperLink to link reports using a URL. All the needed materials for this example, including the reports and catalog are in `<install_root>\help\samples\UDODemo`.

1. In Logi Report Designer, open the catalog for this example Demo.cat in `<install_root>\help\samples\UDODemo\reports`.
2. Select one of the existing reports and ensure the reports in this catalog can run. If there is a problem, open the Catalog Manager, highlight the connection node, then in the Properties sheet, modify the value of the URL property to connect to the demo database, which is **jdbc:hsqldb:<install\_root>\help\samples\UDODemo\db\demo**.

**Linking the master report to the detail report**

Formulas will be used to control the property values URL and Display Value of JHyperLink to make it link the master and detail reports.

1. Open the report that contains the master report - mainreport.cls.

   A JHyperLink is inserted in the Detail panel of the report. The URL and Display Value property values of the UDO are as follows:

   * **URL**: Controlled by the formula linkToSalesYearly, which is defined as follows:

     `"http://localhost:8888/jrserver?jrs.cmd=jrs.web_vw&jrs.catalog=/USERFOLDERPATH/admin/Demo.cat&jrs.report=/USERFOLDERPATH/admin/SalesPerformancebyYear.cls&jrs.result_type=8&jrs.param$pEmployeeID="+@"Employee_Employee ID"`

     This URL value enables you to drill down to the detail report and also make a link for this detail report on the top of the page for you to drill up and down.
   * **Display Value**: Determined by the DBField EmployeeName to show the Employee Name in the master report.
2. Open the report that contains the detail report SalesPerformancebyYear.cls.

   In the Group Header panel, the value of Total is a JHyperLink, whose property values URL and Display Value are both controlled by formulas.

   * **URL**: Controlled by the formula linkToQuarter, which is defined as follows:

     `"http://localhost:8888/jrserver?jrs.cmd=jrs.web_vw&jrs.catalog=/USERFOLDERPATH/admin/Demo.cat&jrs.report=/USERFOLDERPATH/admin/SalesYearPerformancebyQuarter.cls&jrs.result_type=8&jrs.param$pEmployeeID="+@"Employee_Employee ID"+"&jrs.param$pYear="+@getYear;`

     Where, the URL is used to access the detail report SalesYearPerformancebyQuarter.cls, and the records of the detail report are filtered by the parameters pEmployeeID and pYear.
   * **Display Value**: Controlled by the formula getSalesByYear, which is defined as follows:

     `"$"+ToText(@Sum_TotalSales0)`

     This formula returns the total sales amount for the year.
   * **Target**: The options are self, parent, top and blank. Use self to replace the current report with the linked report. Use blank if you want to open a new browser tab so you can return to the master report window.

**Running the reports on Logi Report Server**

This example requires you to access the report by URL. You can drill down through the reports.

1. Start Logi Report Server.
2. Publish the reports and catalog to Logi Report Server as admin into the root level of My Reports.
3. Run the master report mainreport.cls in Page Report Studio.

   ![Master Report in Page Report Studio](https://devnet.logianalytics.com/hc/article_attachments/4404916827159/cmpnt_udo_bltin_jhylk2.gif)
4. Select any name in the Employee Name column, and the year's performance of the employee will be displayed.

   ![Detail Report Result](https://devnet.logianalytics.com/hc/article_attachments/4404916827415/cmpnt_udo_bltin_jhylk3.gif)
5. Select the **Total** number, and it will drill down to the next detail report.

   ![Detail Report Result](https://devnet.logianalytics.com/hc/article_attachments/4404904423319/cmpnt_udo_bltin_jhylk4.gif)

**Note:** When using JHyperLink to link reports as master and detail reports, if a parameter with its value containing special characters such as "\" and "&" is used in the URL, you need to add "\" before the special character. For example, if the parameter value is "a&b", you need to type it as "a\&b".

## Rotating Text/Image with JRotator

JRotator is used to rotate text or images. Since Logi Report currently supports rotating only images but not text, using JRotator to achieve text rotation becomes a feasible solution. JRotator rotates the text inside the JRotator object but not the object itself so if you rotate text or DBFields you may have to change the size of the container in order to see the full value.

The following introduces three cases of using JRotator:

### Using JRotator to Rotate Text

1. Start Logi Report Designer and open the report in which you want to insert some rotated text.
2. Select **Insert** > **UDO** to display the Insert UDO dialog.
3. Select **JRotator** from the UDO drop-down list, and then select **OK**.
4. Keep the JRotator focused and go to the Report Inspector.
5. Locate the Display Value property and type in the required text in the value cell, then select outside of the cell. You will then see the typed text displayed in the JRotator.
6. Specify a rotation degree in the value cell of the Rotate property, for example, 180, then select outside of the cell. You will then find the text in the JRotator upside down.
7. Save the report.

### Using JRotator to Rotate an Image

1. Start Logi Report Designer and open the report in which you want to insert a rotated image.
2. Select **Insert** > **UDO**.
3. In the Insert UDO dialog, select **JRotator** from the drop-down list, and then select **OK**.
4. Keep the JRotator focused and go to the Report Inspector.
5. Specify the local path of the required image in the value cell of the Display Image property, for example, *C:\image.jpg*, then select outside of the cell. You will then see the image displayed in the JRotator.
6. Specify a rotation degree in the value cell of the Rotate property, for example, 45, then select outside of the cell. You will then find the image in the JRotator at a 45 degree angle.
7. Resize the JRotator container as needed to view the entire image.
8. Save the report.

### Using JRotator to Rotate a DBField

1. Start Logi Report Designer and open the report in which you want to insert a rotated DBField.
2. Select **Insert** > **UDO**.
3. In the Insert UDO dialog, select **JRotator** from the drop-down list, and then select **OK**.
4. Keep the JRotator focused and go to the Report Inspector.
5. In the Display Value value cell, select the required DBField or create a formula for a calculated field and select the formula from the dropdown list. Then select outside of the cell and you will see the DBField displayed in the JRotator.
6. Specify a rotation degree in the Rotate value cell, for example, 90, then select outside of the value cell. You will then find the DBField in the JRotator at a 90 degree angle.
7. Change the size of the JRotator container as needed to view the entire text.
8. Save the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629361-Inserting-UDOs-into-a-Page-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605522-Barcodes)
