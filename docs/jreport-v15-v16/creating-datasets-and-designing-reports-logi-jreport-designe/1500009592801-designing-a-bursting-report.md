---
title: "Designing a Bursting Report"
id: 1500009592801
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592801-Designing-a-Bursting-Report
updated_at: 2021-07-24T05:53:48Z
---

# Designing a Bursting Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571002-Opening-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570922-Configuring-Page-Reports-for-Specific-Page-Report-Studio-Features)

# Designing a Bursting Report

Report bursting is a technique which enables running a page report once and distributing the report results to multiple users who each will receive a subset of the results related only to them. It is useful in handling both large amounts of data as well as a large number of users. Logi JReport can distribute any report result to multiple recipients with each receiving a subset, subject to security rules. Report bursting allows you to burst the report to multiple levels of grouping, for example, you may want to give individual salesmen a report of just their sales, the sales manager a report for all salesmen in his division and a complete report with all the data for all salesmen in the company for the VP Sales.

Bursting report results can be distributed to any destination, including email, FTP, and Logi JReport’s versioning system, among others. Multiple criteria and rules can act simultaneously to perform multiple distributions from a single report run.

Report bursting is only supported in page reports that are created using query resources.

Below is a list of the sections covered in this topic:

> * [Bursting Schema](#Schema)
> * [Creating a Bursting Report](#Create)
> * [Built-in Functions for Bursting](#Function)

## Bursting Schema

A bursting schema defines how data is split and who receives each subset of the split data. The most important part for a bursting schema is that there should be a recipient query to contain these data fields:

* Data fields that define recipients. They are known as [bursting recipients](#Recipient).
* At least one data field that is able to map to the [bursting key](#Key). So that the report data can be split by the bursting key and then distributed to the recipients in the query according to the mapping relationship.

For example, to send salary report to the employees in the company by e-mails and to make each employee see his own salary information only, you can use Employee ID as the bursting key. Then you need to create a recipient query and add at least these two data fields in it:

* A data field that contains the e-mail addresses of the employees.
* A data field that contains the IDs of the employees which is used to map to the bursting key Employee ID.

**Bursting key**

Bursting key is one or more distinguishing fields according to which report data is split. For example, sending a credit card bill to every consumer according to the credit card ID. The credit card ID here is the bursting key. When multiple fields are used as bursting key, Logi JReport will split the data according to each unique combination of the fields.

Bursting key fields should come from a dataset used in the current page report.

**Bursting recipients**

Bursting recipients are data fields that contain recipient information in a query. The following types of recipients are supported:

* Principals in the Logi JReport Server security system (user, role and group): e-mail addresses or private folders of the users.
* E-mail addresses.
* Disk: directories or full paths with file name. If it is a directory, Logi JReport will add the bursting result with the default name into the directory. If it is a full path, Logi JReport will generate the result with the specified file name and add it into the path.

  If Logi JReport finds that there is a file with the same name as the generated bursting result file, it will not send the result file into the path and will record a message into the log.
* FTP.
* Versioning system: directories in the resource system of the Logi JReport Server.

## Creating a Bursting Report

A page report that can do bursting should contain one or more bursting schemas and is called a bursting report. A bursting report cannot run in Page Report Studio, it only supports exporting to formats that can be viewed by an external viewer such as PDF and Excel.

**To create a bursting report:**

1. [Design a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) using a query resource and then select **Report** > **Bursting**. The [Bursting](https://devnet.logianalytics.com/hc/en-us/articles/1500009585761-Bursting-Dialog) dialog appears.

   ![Bursting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893810583/burst.gif)
2. Check the **Enable Bursting Report** option.
3. Select the **Add** button next to the Schema Name box to add a bursting schema for the report. By selecting the schema name you can rename it as required.
4. In the Mapping section, first specify the bursting key to split report data by. The datasets used in the report are listed. Select one from the Dataset drop-down list and then select a a bursting key from the dataset.   

   ![Bursting - Bursting Key](https://devnet.logianalytics.com/hc/article_attachments/4404889290519/rpt_pgrpt_burst_key.gif)

   Make sure the data fields used for the bursting key are sortable in the DBMS, otherwise the bursting results may be unpredictable.

   The following data types can be used for a bursting key:

   * **Integer**: INT, SMALLINT, TINYINT, BIGINT
   * **Float**: REAL, FLOAT, DECIMAL, NUMERIC
   * **Character**: CHAR, NCHAR, VARCHAR, NVARCHAR
   * **Date and Time**: DATETIME, SMALLDATETIME
   * **Currency**: MONEY, SMALLMONEY
5. Specify a
   data field in a query that contains data fields of recipient information to map
   to the bursting key. Select the data source, the query, and then the mapping field from the corresponding drop-down list one by one.
   You can set up more mapping relationships by using the
   Add button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif).
   To remove an unwanted mapping row, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)
   on the right.

   ![Bursting - Recipient](https://devnet.logianalytics.com/hc/article_attachments/4404893810839/rpt_pgrpt_burst_rcp.gif)
6. In the Recipient section, specify the recipient addresses. The data fields that define recipient information in the specified query will be available on the drop-down lists for selection. For example, to distribute report results to e-mail addresses, select the E-mail check box and then select a data field that defines e-mail addresses from the drop-down list.
7. If you want to create another schema for the report, repeat steps 3 - 6.
8. Select **OK** to apply the settings.
9. Save the report and [publish the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources#Remotely) to Logi JReport Server, where you can submit a schedule task to generate the bursting results (for details, see Scheduling a Task Containing a Bursting Report in the *Logi JReport Server User's Guide)*.

**Notes:**

* The bursting report always means the primary report. If both the primary report and its subreport are bursting reports, Logi JReport will only execute the bursting task according to the primary report, and the subreport will be processed as a normal report.
* If you load a report which was created in V8.2 containing only one bursting schema, Logi JReport will create a default name for the schema, which is BurstingSchema.

**Tip:** When you finish designing a bursting report, you may want to check it with data. However, when you preview bursting report in Logi JReport Designer, Logi JReport runs the bursting report with all of the data, and if a large dataset is involved it may take a long time or run out of memory before completing. To avoid this from happening, you can limit the number of records by setting the [Maximum Rows](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager#Limit) property of the query.

**Reference:** A sample report containing a bursting report tab named SaleStatForRegion.cls is provided in `<install_root>\Demo\Reports\SampleReports`.

## Built-in Functions for Bursting

Two built-in functions are added in formulas for controlling bursting report result.

* [Boolean isRunBursting()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#isRunBursting)Returns true if the report is running based on bursting schema, else returns false.
* [String currentBurstingSchema()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#currentBurstingSchema)Returns the names of the currently applied bursting schemas. When isRunBursting() returns false, the returned value for currentBurstingSchema() is NULL.

**Note:** Formulas referring either of the two functions are not allowed to be used in queries or datasets.

The following example shows the usage of the functions. It is supposed that a report is first grouped by VP, and next by Manager as follows:

Group by VP,

Group by Manager,

detail

To distribute relative results to all VPs and managers, you can define two schemas as follows and apply them together in a task:

| Bursting Schema | Bursting Key | Recipient |
| --- | --- | --- |
| VP | VP | VPs |
| Manager | VP, Manager | Managers |

Then write a formula:

`if ( isRunBursting() && currentBurstingSchema() != "VP" )  
return true  
else  
return false;`

Next use the formula to control the Suppress property of the group headers and group footers in the VP group panel.

Then all results to the managers will hide the VP level.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571002-Opening-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570922-Configuring-Page-Reports-for-Specific-Page-Report-Studio-Features)
