---
title: "Scheduling Bursting Reports"
id: 5741463244055
section: "Running and Scheduling Reports Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741463244055-Scheduling-Bursting-Reports
updated_at: 2022-10-31T17:18:21Z
---

# Scheduling Bursting Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483494551-Examples-of-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741483587607-Applying-Dynamic-Names-for-Published-Report-Files)

# Scheduling Bursting Reports

This topic describes bursting reports and how you can schedule bursting reports to generate bursting output and non-bursting output.

This topic contains the following sections:

* [An Introduction to Bursting Reports](#Intro)
* [Scheduling a Bursting Report to Generate Bursting Output](#Burst)
  + [Default Name for Bursting Output](#Name)
* [Scheduling a Bursting Report to Generate Non-bursting Output](#NonBurst)

## An Introduction to Bursting Reports

In a large enterprise reporting deployment, it is important to handle both large amounts of data as well as a large number of users. Report bursting enables running a report once and distributing it to multiple recipients who each will receive a subset of the report, subject to security rules.

You can distribute bursting reports to email or FTP addresses, to disk, to the Logi Report versioning system, or to the security system members such as users, groups, and roles.

You can submit a schedule task to contain only one bursting report on Server. When Serve r activates a bursting task, it will create a main bursting task and some sub bursting tasks. Logi Report guarantees that bursting tasks compete with normal tasks for system resources. You can give bursting tasks lower priority by setting queue.policy to 1.

* **Main bursting task**: It is responsible for getting/splitting data and distributing work to the sub tasks. There can be only one main bursting task for a sub bursting task.
* **Sub bursting task**: It is responsible for generating the report output according to split data and sending the output to the addresses of the bursting recipients.

For more information, see Creating Bursting Reports in the *Logi Report Designer Guide*.

On Server, Server supports the Run and Advanced Run actions for normal reports but not for bursting reports. You cannot run a page report containing only bursting report tabs directly or in the Advanced mode but can schedule it.

Server supports scheduling for both types of reports excluding the combination of the two types: for normal reports, you can schedule multiple reports at a time; however, for bursting reports, you can schedule only one report. For a scheduled bursting task, you can use seven kinds of file formats: HTML, PDF, Excel, Text, RTF, XML, and PostScript. In addition, when scheduling to run a bursting report, you can make it generate not only the bursting output by applying bursting schemas but also the non-bursting output based on the whole data without data split.

## Scheduling a Bursting Report to Generate Bursting Output

A bursting report may have one or more bursting schemas, and you need to apply one or more of them in order to get a bursting output, that is when you schedule a bursting report, you need to select the schemas in the General tab of the Schedule dialog box.

![Select Bursting Schema](https://devnet.logianalytics.com/hc/article_attachments/9905659212183/wkrpt_sch_burst1.gif)

Then, Server displays a tab named Bursting Result on the Publish tab, and only the corresponding sub tabs that you have defined in the selected bursting schemas' recipients in Designer are available.

![Bursting Result Tab](https://devnet.logianalytics.com/hc/article_attachments/9905671400599/wkrpt_sch_burst2.gif)

For example, a bursting report has three bursting schemas: Schema 1 defines recipient E-mail and Disk, Schema 2 defines recipient FTP, and Schema 3 defines recipient Logi Report Server Version. If you select Schema 1 and Schema 3, Server will only display To E-mail, To Disk, and To Version sub tabs on the Publish > Bursting Result tab for the bursting output.

The following table shows which tab will be available in the Publish > Bursting Result tab of the Schedule dialog box for which recipient address defined in the bursting schema.

| Recipient | Sub tab in the Publish tab |
| --- | --- |
| E-mail | To E-mail |
| FTP | To FTP |
| Disk | To Disk |
| Logi Report Server Version | To Version |
| Logi Report Server User/Group/Role > User E-mail | To E-mail |
| Logi Report Server User/Group/Role > User Private Folder | To Version |

When scheduling a bursting report, you do not need to specify the destination in the Publish tab since the bursting schema has included the recipient addresses. However, you can provide a file name to the subset of report instead of using the default name. To define a dynamic file name, you can use the string [recipMapping\_<colName>](https://devnet.logianalytics.com/hc/en-us/articles/5741483587607-Applying-Dynamic-Names-for-Published-Report-Files#Field) to return the value of a column in the recipient queries that you defined in the bursting schemas for the schedule. Here, **<ColName>** is the mapping name of the column in the catalog. For example, if you define the output file name as **Bursting\_[recipMapping\_Country].pdf**, Server will generate the output files as Bursting\_USA.pdf, Bursting\_France.pdf, and so on.

### Default Name for Bursting Output

Sometimes you may not want to specify a file name for each bursting output when defining recipients. The bursting system will give it a default name. The default name format for scheduling to disk is: ReportTabName + "\_" + BurstingKey + suffix (format type). When there are multiple bursting key columns, Server connects them by the character "\_".

**Converting to String**

When a bursting key is of one of the following data types, Server converts it into String to make a valid output file name:

* Integer, Float, and Character: Same as Java, Server transfers these data types to String directly.
* Date and Time: Server transfers all date and time formats to the date format: yyyy-MM-dd hh:mm:ss.
* Currency: Server transfers Currency to the number without the currency mark ($ or others).

**Name length**

In the Server resource system, the resource name only supports up to 64-character length. If a bursting output file name is longer than that, Server will trim it down automatically.

To avoid the same name in the same path, Server appends an index to the output name, for example: report1\_USA\_Maryland1.pdf, report1\_USA\_Maryland2.pdf.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* All bursting outputs use the security information of the bursting task submitter.
* When a busting report has used security policies or filters, Server may not be able to obtain the bursting key from the specified bursting schema. In this case, Server will not send the busting output.

## Scheduling a Bursting Report to Generate Non-bursting Output

Besides generating bursting output for a bursting report, you can also generate non-bursting output for the report without applying any bursting definition, which is based on full data without data split.

To generate non-bursting output, select **Non-bursting Result** in the General tab of the Schedule dialog box. Then, Server displays a tab named Non-bursting Result on the Publish tab, and all the publish types - To Version, To Disk, To E-mail, To Printer, To Fax, and To FTP - are available on this tab for the non-bursting output.

![Non-bursting Result Tab](https://devnet.logianalytics.com/hc/article_attachments/9905659267479/wkrpt_sch_burst3.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483494551-Examples-of-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741483587607-Applying-Dynamic-Names-for-Published-Report-Files)
