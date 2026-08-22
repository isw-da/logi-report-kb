---
title: "Scheduling Bursting Reports"
id: 1500009724242
section: "Run and Schedule Reports Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724242-Scheduling-Bursting-Reports
updated_at: 2021-07-25T07:18:41Z
---

# Scheduling Bursting Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724282-Examples-of-Scheduling-Reports)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724322-Applying-Dynamic-Names-for-Published-Result-Files)

# Scheduling Bursting Reports

This topic introduces the advantages of bursting reports and how to schedule bursting reports to generate bursting result and non-bursting result.

Select the following links to view the topics:

* [An Introduction to Bursting Reports](#Intro)
* [Scheduling a Bursting Report to Generate Bursting Result](#Burst)
  + [Default Name for Bursting Result Files](#Name)
* [Scheduling a Bursting Report to Generate Non-bursting Result](#NonBurst)

## An Introduction to Bursting Reports

In a large enterprise reporting deployment, it is important to handle both large amounts of data as well as a large number of users. Report bursting enables running a report once and distributing the report result to multiple recipients who each will receive a subset of the report result, subject to security rules.

Bursting reports can be distributed to e-mail or FTP addresses, to disk, to the Logi Report versioning system, or to the security system members such as users, groups, and roles.

End users can submit a schedule task which contains only one bursting report on Logi Report Server. When a bursting task is activated, it will create a main bursting task and some sub bursting tasks. Logi Report guarantees that bursting tasks compete with normal tasks for system resources. The bursting tasks can be given lower priority if desired (set queue.policy to 1).

* **Main bursting task**: It is responsible for getting/splitting data and distributing work to the sub tasks. There can be only one main bursting task for a sub bursting task.
* **Sub bursting task**: It is responsible for generating the report result according to split data and sending the results to the addresses of the bursting recipients.

For details about what is a bursting report and how to design one, refer to Creating Bursting Reports in the *Logi Report Designer Guide*.

On Logi Report Server, the Run and Advanced Run actions are supported for normal reports but not for bursting reports. A page report containing only bursting report tabs cannot be run directly or in Advanced mode, it must be scheduled.

Scheduling is supported for both types of reports excluding the combination of the two types: for normal reports, multiple reports can be scheduled at a time; however for bursting reports, only one can be scheduled. For a scheduled bursting task, seven kinds of result file formats are supported: HTML, PDF, Excel, Text, RTF, XML, and PostScript. In addition, when scheduling to run a bursting report, you can make it generate not only the bursting result by applying bursting schemas but also the non-bursting result based on whole data without data splitting.

## Scheduling a Bursting Report to Generate Bursting Result

A bursting report may have one or more bursting schemas, and you need to apply one or more of them in order to get a bursting result, that is when you schedule a bursting report, you need to select the schemas in the General tab of the Schedule dialog box.

![Select Bursting Schema](https://devnet.logianalytics.com/hc/article_attachments/4404936769431/wkrpt_sch_burst1.gif)

Then a tab named Bursting Result is displayed in the Publish tab and only the corresponding sub tabs that are defined in the selected bursting schemas' recipients in Logi Report Designer are available.

![Bursting Result Tab](https://devnet.logianalytics.com/hc/article_attachments/4404936769687/wkrpt_sch_burst2.gif)

For example, a bursting report has three bursting schemas: Schema 1 defines recipient E-mail and Disk, Schema 2 defines recipient FTP, and Schema 3 defines recipient Logi Report Server Version. If Schema 1 and Schema 3 are selected, only To E-mail, To Disk, and To Version sub tabs will be shown in the Bursting Result tab of the Publish tab for the bursting result.

The following list shows which tab will be displayed in the Publish > Bursting Result tab of the Schedule dialog box for which recipient address specified in bursting schema.

| Recipient | Sub tab in the Publish tab |
| --- | --- |
| E-mail | To E-mail |
| FTP | To FTP |
| Disk | To Disk |
| Logi Report Server Version | To Version |
| Logi Report Server User/Group/Role > User E-mail | To E-mail |
| Logi Report Server User/Group/Role > User Private Folder | To Version |

When scheduling a bursting report, you don't need to specify the destination in the Publish tab since the recipient addresses have been included in the bursting schema. However, you are allowed to give a file name to the subset of report result instead of using the default name.

### Default Name for Bursting Result Files

Sometimes you may not want to specify a file name for each bursting result when defining recipients. The bursting system will give it a default name. The default name format is: ReportName + "\_" + BurstingKey + suffix (result format type). When there are multiple bursting key columns, they are connected by the character "\_".

**Converting to String**

When a bursting key is of one of the following data types, it will be converted into String so as to make a valid result file name:

* Integer, Float, Character: Same as Java, these data types are transferred to string directly.
* Date and Time: All date and time formats will be transferred to a date format: yyyy-MM-dd hh:mm:ss.
* Currency: Currency will be transferred to the number without the currency mark ($ or others).

**Name length**

In the Logi Report Server resource system, the resource name only supports up to 64-character length. If a bursting result file name is longer than that, the system will trim it down automatically.

In order to avoid using the same name in the same path, an index will be appended to the result name, for example: report1\_USA\_Maryland1.pdf, report1\_USA\_Maryland2.pdf.

**Notes:**

* All bursting sub results will apply the security information of the bursting task submitter.
* When a busting report has been applied with security policies or filters, Logi Report may be not able to obtain the bursting key from the specified bursting schema, in this case, it will not send the busting result.

## Scheduling a Bursting Report to Generate Non-bursting Result

Besides generating bursting result for a bursting report, you can also generate non-bursting result for the report without applying any bursting definition, which is based on full data without data splitting.

To generate non-bursting result, make sure the Non-bursting Result option is selected in the General tab of the Schedule dialog box. Then a tab named Non-bursting Result appears in the Publish tab, and all the publish types - To Version, To Disk, To E-mail, To Printer, To Fax, and To FTP - are available in this tab for the non-bursting result.

![Non-bursting Result Tab](https://devnet.logianalytics.com/hc/article_attachments/4404942483735/wkrpt_sch_burst3.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724282-Examples-of-Scheduling-Reports)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724322-Applying-Dynamic-Names-for-Published-Result-Files)
