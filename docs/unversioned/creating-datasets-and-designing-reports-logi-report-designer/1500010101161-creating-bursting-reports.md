---
title: "Creating Bursting Reports"
id: 1500010101161
section: "Creating Datasets and Designing Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101161-Creating-Bursting-Reports
updated_at: 2021-11-16T07:30:52Z
---

# Creating Bursting Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101321-Designing-the-Report-Pages)

# Creating Bursting Reports

Report bursting is a technique which enables running a page report once and distributing the report result to multiple users who each receives a subset of the results related only to them. You can distribute the bursting report result to any destination, including e-mail, FTP, disk, the versioning system of Server, and principals in the security system of Server. Logi Report allows for multiple criteria and rules to act simultaneously to perform multiple distributions from a single report run. Report bursting is useful in handling both large amounts of data as well as a large number of users. It enables you to burst the page report to multiple levels of grouping based on the bursting schemas. For example, you may want to give individual salesmen a report of just their sales, the sales manager a report for all salesmen in his division, and a complete report with all the data for all salesmen in the company for the VP Sales. This topic introduces what a bursting schema is, how you can creating a bursting report, and use the built-in functions for report bursting.

This topic contains the following sections:

* [Bursting Schema](#Schema)
* [Creating a Bursting Report](#Create)
* [Built-in Functions for Bursting](#Function)

## Bursting Schema

A bursting schema defines how to split data and who receives each subset of the split data. The most important part for a bursting schema is that there should be a recipient query to contain these data fields:

* Data fields that define recipients, which are the [bursting recipients](#Recipient).
* At least one data field that is able to map to the [bursting key](#Key), so that Logi Report can split the report data by the bursting key and then distribute it to the recipients in the query according to the mapping relationship.

For example, to send salary report to the employees in a company by e-mails and to make each employee see his own salary information only, you can use Employee ID as the bursting key, then you need to create a recipient query and add at least these two data fields in it:

* A data field that contains the e-mail addresses of the employees.
* A data field that contains the IDs of the employees that Logi Report can use to map to the bursting key Employee ID.

**Bursting key**

Bursting key is one or more distinguishing fields according to which Logi Report splits the report data. For example, in the case of sending a credit card bill to every consumer according to the credit card ID, the credit card ID is the bursting key. When you apply multiple fields as bursting key, Logi Report splits the data according to each unique combination of the fields.

Bursting key fields should come from a dataset that the current page report uses. If the dataset is based on a business view, the bursting keys can only be group objects and dynamic formulas used as Group.

**Bursting recipients**

Bursting recipients are data fields that contain recipient information in a query. The following types of recipients are supported:

* Principals (user, role, and group) in the security system of Server: e-mail addresses or private folders of the users.
* E-mail addresses.
* Disk: directories or full paths with file name. If it is a directory, Logi Report adds the bursting result with the default name into the directory; if it is a full path, Logi Report generates the result with the specified file name and adds it into the path.

  If Logi Report finds that there is a file with the same name as the generated bursting result file, it will not send the result file into the path and will instead record a message into the log.
* FTP.
* Versioning system: directories in the resource system of Server.

## Creating a Bursting Report

A page report that can perform bursting should contain one or more bursting schemas and is called a bursting report. You cannot run a bursting report in Page Report Studio; you can only export it to formats that can be viewed by an external viewer such as PDF and Excel.

**To create a bursting report:**

1. [Design a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) and then select **Report** > **Bursting**. Designer displays the [Bursting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058102-Bursting-Dialog-Box).

   ![Bursting dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856839447/burst.gif)
2. Select the **Enable Bursting Report** checkbox.
3. Designer provides a default busting schema named "BurstingSchema". You can select the schema name and rename it.
4. In the **Mapping** section, first specify the bursting key by which to split the report data. Designer lists the datasets that the page report uses in the Dataset drop-down list. Select a dataset and then select a bursting key from the dataset.   

   ![Bursting - Bursting Key](https://devnet.logianalytics.com/hc/article_attachments/4404856839703/rpt_burst_key.gif)

   Make sure that the data fields you select for the bursting key are sortable in the DBMS; otherwise, the bursting results may be unpredictable.

   You can use the following data types for a bursting key:

   * **Integer**: INT, SMALLINT, TINYINT, BIGINT
   * **Float**: REAL, FLOAT, DECIMAL, NUMERIC
   * **Character**: CHAR, NCHAR, VARCHAR, NVARCHAR
   * **Date and Time**: DATETIME, SMALLDATETIME
   * **Currency**: MONEY, SMALLMONEY
5. Specify a data field in a query that contains data fields of recipient information to map to the bursting key as follows: select the data source, the query, and then the mapping field from the corresponding drop-down list one by one. You can select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to set up more mapping relationships. To delete an unwanted mapping row, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).

   ![Bursting - Recipient](https://devnet.logianalytics.com/hc/article_attachments/4404856839959/rpt_burst_rcp.gif)
6. In the **Recipient** section, specify the recipient addresses. The data fields that define recipient information in the specified query are available in the drop-down lists. For example, to distribute the report result to e-mail addresses, select the **E-mail** checkbox and then double-click a data field that defines e-mail addresses from the drop-down list.
7. When you select **E-mail** or Logi Report **Server User**/**Logi Report **Server** Group**/**Logi Report **Server** Role** > **User E-mail** in the Recipient section, the **E-mail Settings button** is activated. You can select it to further define the e-mail settings.

   **To define more information of the e-mail:**

   1. Select the **E-mail Settings** button. Designer displays the [E-mail Settings dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096541-E-mail-Settings-Dialog-Box).

      ![E-mail Settings dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848420375/emlst.gif)
   2. From the **Cc**/**Bcc** drop-down list, double-click the data field in the specified query which you want to use for retrieving the e-mail addresses to send additional copies of the e-mail to. The people in the Bcc list is known to the sender and himself only.
   3. Specify the subject and comments of the e-mail in the **Subject** and **Comments** boxes. If you want to compose the subject/comments dynamically, select the **Add Dynamic Field** button, then in the [Select Field dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098661-Select-Field-Dialog-Box), select the required fields to insert into the text.
   4. Select **OK** to accept the e-mail settings.
8. You can select the **Add** button next to the **Schema Name** box and repeat the above steps to create more bursting schemas for the report.

   To delete an unwanted schema, select it in the Schema Name box and select **Remove**.
9. Select **OK** to apply the settings.
10. Save the report and [publish it to Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#Remotely), where you can submit a schedule task to generate the bursting results (for more information, see Scheduling Bursting Reports in the *Logi Report Server Guide)*.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) The bursting report always means the primary report. If both the primary report and its subreport are bursting reports, Logi Report Engine only executes the bursting task according to the primary report, and processes the subreport as a normal report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When you finish designing a bursting report, you may want to check it with data. However, when you preview bursting report in Designer, Designer runs the bursting report with all of the data, and if a large dataset is involved, Designer may need a long time or run out of memory before completing. To avoid this from happening, you can limit the number of records by setting the [Maximum Rows](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries#Limit) property of the query.

**Reference:** Designer provides a sample report which contains a bursting report tab. You can find the report tab in Sales Statistics by Region Report.cls, in `<install_root>\Demo\Reports\SampleReports`.

## Built-in Functions for Bursting

Logi Report provides two built-in functions for controlling bursting report result.

* [Boolean isRunBursting()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#isRunBursting)  
  Returns true if the report is running based on bursting schema, else returns false.
* [String currentBurstingSchema()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#currentBurstingSchema)  
  Returns the names of the currently applied bursting schemas. When *isRunBursting()* returns false, the return value for *currentBurstingSchema()* is NULL.

The following example shows the usage of the functions. It is supposed that a report is first grouped by VP, and next by Manager as follows:

Group by VP,

Group by Manager,

detail

To distribute relative results to all VPs and managers, you can define two schemas as follows and apply them together in a task:

| Bursting Schema | Bursting Key | Recipient |
| --- | --- | --- |
| VP | VP | VPs |
| Manager | VP, Manager | Managers |

Then write a formula as follows:

`if ( isRunBursting() && currentBurstingSchema() != "VP" )  
return true  
else  
return false;`

Next, use the formula to control the Suppress property of the group headers and group footers in the VP group panel. Logi Report then hides the VP level for all results delivered to the managers.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101321-Designing-the-Report-Pages)
