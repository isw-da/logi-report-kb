---
title: "Creating Bursting Reports"
id: 5735534125591
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735534125591-Creating-Bursting-Reports
updated_at: 2022-11-02T08:17:50Z
---

# Creating Bursting Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735576827671-Delivering-Messages-Between-Library-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages)

# Creating Bursting Reports

Report bursting is a technique which enables running a page report once and distributing the report to multiple users who each receives a subset of the results related only to them. You can distribute a bursting report to any destination, including email, FTP, disk, the versioning system of Server, and principals in the security system of Server. Logi Report allows for multiple criteria and rules to act simultaneously to perform multiple distributions from a single report run. Report bursting is useful in handling both large amounts of data and a large number of users. It enables you to burst the page report to multiple levels of grouping based on the bursting schemas. For example, you may want to give individual salesmen a report of just their sales, the sales manager a report for all salesmen in his division, and a complete report with all the data for all salesmen in the company for the VP Sales. This topic introduces what a bursting schema is, how you can creating a bursting report, and use the built-in functions for report bursting.

This topic contains the following sections:

* [Bursting Schema](#Schema)
* [Creating a Bursting Report](#Create)
* [Built-in Functions for Bursting](#Function)

## Bursting Schema

A bursting schema defines how to split data and who receives each subset of the split data. The most important part for a bursting schema is that there should be a recipient query to contain these data fields:

* Data fields that define recipients, which are the [bursting recipients](#Recipient).
* At least one data field that is able to map to the [bursting key](#Key), so that Logi Report can split the report data by the bursting key and then distribute it to the recipients in the query according to the mapping relationship.

For example, to send salary report to the employees in a company by emails and to make each employee see his own salary information only, you can use Employee ID as the bursting key, then you need to create a recipient query and add at least these two data fields in it:

* A data field that contains the email addresses of the employees.
* A data field that contains the IDs of the employees that Logi Report can use to map to the bursting key Employee ID.

**Bursting key**

Bursting key is one or more distinguishing fields according to which Logi Report splits the report data. For example, in the case of sending a credit card bill to every consumer according to the credit card ID, the credit card ID is the bursting key. When you apply multiple fields as bursting key, Logi Report splits the data according to each unique combination of the fields.

Bursting key fields should come from a dataset that the current page report uses. If the dataset is based on a business view, the bursting keys can only be group objects and dynamic formulas used as Group.

**Bursting recipients**

Bursting recipients are data fields that contain recipient information in a query. You can use the following types of recipients:

* Principals (user, role, and group) in the security system of Server, including email addresses and private folders of the users.
* Email addresses.
* Disk, including directories and full paths with file name. If it is a directory, Logi Report adds the bursting result with the default name into the directory; if it is a full path, Logi Report generates the result with the specified file name and adds it into the path.

  If Logi Report finds that there is a file with the same name as the generated bursting result file, it will not send the result file into the path and will instead record a message into the log.
* FTP
* Versioning system, that is, directories in the resource system of Server.

## Creating a Bursting Report

A page report that can perform bursting should contain one or more bursting schemas and is called a bursting report. You cannot run a bursting report in Page Report Studio; you can only export it to formats that can be viewed by an external viewer such as PDF and Excel.

**To create a bursting report**

1. [Design a page report](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports#Page).
2. Navigate to **Report** > **Bursting**. Designer displays the [Bursting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513195031-Bursting-Dialog-Box).

   ![Bursting dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898457672471/burst.gif)
3. Select **Enable Bursting Report**.
4. Designer provides a default busting schema **BurstingSchema**. You can select the schema name and rename it.
5. In the **Mapping** section, first specify the bursting key by which to split the report data. Designer lists the datasets the page report applies in the Dataset drop-down list. Select a dataset and then select a bursting key from the dataset.   

   ![Bursting - Bursting Key](https://devnet.logianalytics.com/hc/article_attachments/9898474756887/rpt_burst_key.gif)

   You should make sure the data fields you select for the bursting key are sortable in the database; otherwise, the bursting results may be unpredictable. You can use the following data types for a bursting key:

   * **Integer**: INT, SMALLINT, TINYINT, BIGINT
   * **Float**: REAL, FLOAT, DECIMAL, NUMERIC
   * **Character**: CHAR, NCHAR, VARCHAR, NVARCHAR
   * **Date and Time**: DATETIME, SMALLDATETIME
   * **Currency**: MONEY, SMALLMONEY
6. Specify a data field in a query that contains data fields of recipient information to map to the bursting key as follows: select the data source, the query, and then the mapping field from the corresponding drop-down list one by one. You can select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to set up more mapping relationships. To delete a mapping row, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).

   ![Bursting - Recipient](https://devnet.logianalytics.com/hc/article_attachments/9898457701015/rpt_burst_rcp.gif)
7. In the **Recipient** section, specify the recipient addresses. The data fields that define recipient information in the specified query are available in the drop-down lists. For example, to distribute the report to email addresses, select **E-mail** and then double-click a data field that defines email addresses from the drop-down list.
8. If you select **E-mail** or **Logi Report Server User**/**Logi Report Server Group**/**Logi Report Server Role** > **User E-mail** in the Recipient section, Designer enables the **E-mail Settings** button. You can select the button to further define the email settings.

   **To define more information of the email**

   1. Select **E-mail Settings**. Designer displays the [E-mail Settings dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522745495-E-mail-Settings-Dialog-Box).

      ![E-mail Settings dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898457755287/emlst.gif)
   2. From the **Cc**/**Bcc** drop-down list, double-click the data field in the specified query which you want to use for retrieving the email addresses to send additional copies of the email to. The people in the Bcc list is known to the sender and himself only.
   3. Specify the subject and comments of the email in the **Subject** and **Comments** boxes. If you want to compose the subject/comments dynamically, select **Add Dynamic Field**, then in the [Select Field dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524747927-Select-Field-Dialog-Box), select the required fields to insert into the text.
   4. Select **OK** to accept the email settings.
9. You can select **Add** next to the **Schema Name** box and repeat the preceding steps to create more bursting schemas for the report. To delete an unwanted schema, select it in the Schema Name box and select **Remove**.
10. Select **OK** to apply the settings.
11. Save the report.
12. [Publish the report to Server](https://devnet.logianalytics.com/hc/en-us/articles/5735576653207-Publishing-and-Downloading-Resources#Remotely). You can then submit a schedule task to generate the bursting results. For more information, see Scheduling Bursting Reports in the *Logi Report Server Guide*.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* The bursting report always means the primary report. If both the primary report and its subreport are bursting reports, Logi Report Engine only executes the bursting task according to the primary report, and processes the subreport as a normal report.
* When you finish designing a bursting report, you may want to check it with data. However, when you preview bursting report in Designer, Designer runs the bursting report with all data, and if a large dataset is involved, Designer may need a long time or run out of memory before completing. To avoid this from happening, you can limit the number of records by setting the [Maximum Rows](https://devnet.logianalytics.com/hc/en-us/articles/5735555374103-Managing-the-Data-Retrieval-of-Queries#Limit) property of the query.

**Reference:** Designer provides a sample report which contains a bursting report tab. You can find the report tab in Sales Statistics by Region Report.cls, in `<install_root>\Demo\Reports\SampleReports`.

## Built-in Functions for Bursting

Logi Report provides two built-in functions for controlling bursting reports.

* [Boolean isRunBursting()](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions#isRunBursting)  
  The function returns "true" if the report is running based on bursting schema; otherwise, it returns "false".
* [String currentBurstingSchema()](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions#currentBurstingSchema)  
  The function returns the names of the currently applied bursting schemas. When *isRunBursting()* returns "false", the return value for *currentBurstingSchema()* is "NULL".

Suppose you have a report that is first grouped by VP and then by Manager, to distribute relative results to all VPs and managers, you can define two schemas as follows and apply them together in a task:

| Bursting Schema | Bursting Key | Recipient |
| --- | --- | --- |
| VP | VP | VPs |
| Manager | VP, Manager | Managers |

Then you can write a formula using the bursting functions as follows:

`if ( isRunBursting() && currentBurstingSchema() != "VP" )  
return true  
else  
return false;`

And use the formula to control the Suppress property of the group headers and group footers in the VP group panel. Logi Report Engine then hides the VP group level for all results delivered to the managers.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735576827671-Delivering-Messages-Between-Library-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages)
