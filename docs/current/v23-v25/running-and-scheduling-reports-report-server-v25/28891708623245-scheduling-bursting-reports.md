---
title: "Scheduling Bursting Reports"
id: 28891708623245
section: "Running and Scheduling Reports Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891708623245-Scheduling-Bursting-Reports
updated_at: 2026-02-26T02:13:44Z
source_host: docs-report.zendesk.com
---
# 
Scheduling Bursting Reports

This topic describes bursting reports and how you can schedule bursting reports to generate bursting output and non-bursting output.

This topic contains the following sections:

- An Introduction to Bursting Reports

- 
Scheduling a Bursting Report to Generate Bursting Output-  Default Name for Bursting Output

- Scheduling a Bursting Report to Generate Non-bursting Output

## 
An Introduction to Bursting Reports

In a large enterprise reporting deployment, it is important to handle both large amounts of data as well as a large number of users. Report bursting enables running a report once and distributing it to multiple recipients who each will receive a subset of the report, subject to security rules.

You can distribute bursting reports to email or FTP addresses, to disk, to the Report versioning system, or to the security system members such as users, groups, and roles.

You can submit a schedule task to contain only one bursting report on Server. When Serve r activates a bursting task, it will create a main bursting task and some sub bursting tasks. Report guarantees that bursting tasks compete with normal tasks for system resources. You can give bursting tasks lower priority by setting queue.policy to 1.

- 
Main bursting task: It is responsible for getting/splitting data and distributing work to the sub tasks. There can be only one main bursting task for a sub bursting task.

- 
Sub bursting task: It is responsible for generating the report output according to split data and sending the output to the addresses of the bursting recipients.

For more information, see Creating Bursting Reports in the Report Designer Guide.

On Server, Server supports the Run and Advanced Run actions for normal reports but not for bursting reports. You cannot run a page report containing only bursting report tabs directly or in the Advanced mode but can schedule it.

Server supports scheduling for both types of reports excluding the combination of the two types: for normal reports, you can schedule multiple reports at a time; however, for bursting reports, you can schedule only one report. For a scheduled bursting task, you can use seven kinds of file formats: HTML, PDF, Excel, Text, RTF, XML, and PostScript. In addition, when scheduling to run a bursting report, you can make it generate not only the bursting output by applying bursting schemas but also the non-bursting output based on the whole data without data split.

## 
Scheduling a Bursting Report to Generate Bursting Output

A bursting report may have one or more bursting schemas, and you need to apply one or more of them in order to get a bursting output, that is when you schedule a bursting report, you need to select the schemas in the General tab of the Schedule dialog box.

Then, Server displays a tab named Bursting Result on the Publish tab, and only the corresponding sub tabs that you have defined in the selected bursting schemas' recipients in Designer are available. 

For example, a bursting report has three bursting schemas: Schema 1 defines recipient E-mail and Disk, Schema 2 defines recipient FTP, and Schema 3 defines recipient Report Server Version. If you select Schema 1 and Schema 3, Server will only display To E-mail, To Disk, and To Version sub tabs on the Publish > Bursting Result tab for the bursting output.

The following table shows which tab will be available in the Publish > Bursting Result tab of the Schedule dialog box for which recipient address defined in the bursting schema.

| Recipient | Sub tab in the Publish tab |
| --- | --- |
| E-mail | To E-mail |
| FTP | To FTP |
| Disk | To Disk |
| Report Server Version | To Version |
| Report Server User/Group/Role > User E-mail | To E-mail |
| Report Server User/Group/Role > User Private Folder | To Version |

When scheduling a bursting report, you do not need to specify the destination in the Publish tab since the bursting schema has included the recipient addresses. However, you can provide a file name to the subset of report instead of using the default name. To define a dynamic file name, you can use the string recipMapping_<colName> to return the value of a column in the recipient queries that you defined in the bursting schemas for the schedule. Here, <ColName> is the mapping name of the column in the catalog. For example, if you define the output file name as Bursting_[recipMapping_Country].pdf, Server will generate the output files as Bursting_USA.pdf, Bursting_France.pdf, and so on.

### 
Default Name for Bursting Output

Sometimes you may not want to specify a file name for each bursting output when defining recipients. The bursting system will give it a default name. The default name format for scheduling to disk is: ReportTabName + "_" + BurstingKey + suffix (format type). When there are multiple bursting key columns, Server connects them by the character "_".

Converting to String

When a bursting key is of one of the following data types, Server converts it into String to make a valid output file name:

- Integer, Float, and Character: Same as Java, Server transfers these data types to String directly.

- Date and Time: Server transfers all date and time formats to the date format: yyyy-MM-dd hh:mm:ss.

- Currency: Server transfers Currency to the number without the currency mark ($ or others).

Name length

In the Server resource system, the resource name only supports up to 64-character length. If a bursting output file name is longer than that, Server will trim it down automatically.

To avoid the same name in the same path, Server appends an index to the output name, for example: report1_USA_Maryland1.pdf, report1_USA_Maryland2.pdf.

- All bursting outputs use the security information of the bursting task submitter.

- When a busting report has used security policies or filters, Server may not be able to obtain the bursting key from the specified bursting schema. In this case, Server will not send the busting output. 

## 
Scheduling a Bursting Report to Generate Non-bursting Output

Besides generating bursting output for a bursting report, you can also generate non-bursting output for the report without applying any bursting definition, which is based on full data without data split.

To generate non-bursting output, select Non-bursting Result in the General tab of the Schedule dialog box. Then, Server displays a tab named Non-bursting Result on the Publish tab, and all the publish types - To Version, To Disk, To E-mail, To Printer, To Fax, and To FTP - are available on this tab for the non-bursting output.
