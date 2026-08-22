---
title: "Logi Report v17 Enhancements"
id: 1500009634381
section: "Release Notes for Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634381-Logi-Report-v17-Enhancements
updated_at: 2021-07-24T16:03:53Z
---

# Logi Report v17 Enhancements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634361-Logi-Report-v17-Release-Notes) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009627521-Logi-Report-Designer-Guide-v17-Update-1-Overview)

# Logi Report v17 Enhancements

This topic introduces the significant features of Logi Report for the v17 release. This includes a More Robust Resource Deployment feature, User Interface enhancements, Performance enhancements, and other new functionality for Logi Report.

## More Robust Resource Deployment

You can now publish resources from one Logi Report Server to another Logi Report Server, meaning you can easily replicate the same resource tree between servers.

![More Robust Resource Deployment](https://devnet.logianalytics.com/hc/article_attachments/4404911663511/publish-from-server-to-server.png)

## Logi Report UI Enhancements

Scheduling Multiple Reports by Just One Click (per Folder)

You can now schedule to run multiple page reports and web reports that are stored in the same folder and created on the same catalog, using a single schedule task. The scheduled report results can be published to the Logi Report versioning system and sent via e-mails.

![Schedule to Run Multiple Reports](https://devnet.logianalytics.com/hc/article_attachments/4404911663767/schedule-multiple-report.gif)

Easy to Use Parameter User Interface with Quick Search, Sort, and Type-in Workflows

We have improved the performance and user experience when specifying parameter values in Logi Report Designer, Logi Report Server, and Web Report Studio. Now, the initial value list displays no more than 500 records, resulting in faster loading when there are a large number of records; and you can load more records piece by piece. Quick search and sort functions make it convenient to find values you want in a long value list. Typing-in workflow is more efficient now; you can simply select the Value text box to automatically select all the values, and then type in new values.

![More Intuitive Parameter User Interfaces with Improved Performance](https://devnet.logianalytics.com/hc/article_attachments/4404911664023/parameter-user-experience.gif)

For more information about the feature, select the following links:

* [Specifying Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009634541-Specifying-Parameter-Values)
* [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009608062-Enter-Values-Dialog)

Well-Designed Editor for Creating and Importing SQL Statements

You can now use the Imported SQL Editor to write your SQL statements directly in Logi Report Designer as the data source for creating reports with, as well as importing the SQL statement from an SQL file.

![Imported SQL Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904220183/imported-sql-editor.gif)

For more information about the feature, select the following links:

* [Creating and Importing SQL Statements](https://devnet.logianalytics.com/hc/en-us/articles/1500009606822-Creating-and-Importing-SQL-Statements)
* [Imported SQL Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009631981-Imported-SQL-Editor-Dialog)

## Logi Report Performance Enhancements

Performance Enhancement-Running XML Format Catalogs and Reports

When you publish catalogs and page reports that are saved in XML format to Logi Report Server, Logi Report Server parses the XML files, converts them to binary files, and stores the converted binary files into its resource system instead of the XML files. This means that your Server performance can be greatly improved, because it does not have to go through parsing of the XML files each time the catalogs and page reports are executed. You can also download catalogs and page reports saved in the server resource system to Logi Report Designer in the XML format, if you prefer this format for checking into source code control systems.

![Convert XML Resources to Binary Format](https://devnet.logianalytics.com/hc/article_attachments/4404904220567/convert-xml-to-binary.png)

For more information about the feature, select the link: [Publishing and Downloading Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources).

Dynamic Links in Hierarchical Drilling Layers

When creating links on report objects in both Logi Report Designer and Web Report Studio, you can use Current Field and Corresponding Field in the link conditions to set up dynamic links with filters automatically generated from the drilling path.

![Dynamic Links with Hierarchical Drilling Layer](https://devnet.logianalytics.com/hc/article_attachments/4404911664407/dynamic-links-with-hierarchical-drilling-layer.gif)

For more information about the feature, select the link: [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009613322-Adding-Links-in-Reports).

Support for SSH in Publishing to FTP

You can now use SSH key files to authenticate to the FTP servers, besides using passwords, when publishing reports to FTP servers via SFTP on Logi Report Server. The use of SSH key files greatly reduces the security risks in communications between Logi Report Server and the clients.

![Support for SSH in Publishing to FTP](https://devnet.logianalytics.com/hc/article_attachments/4404911664663/support-ssh-in-publishing-to-ftp.gif)

Permission Control for Scheduling Recipients

Logi Report Server administrators can customize the recipients that a user can send scheduled report results to via e-mails. This ensures that a user can only access the recipients' mail addresses he or she is permitted.

![Permission Control for Scheduling Recipients](https://devnet.logianalytics.com/hc/article_attachments/4404911664919/permission-control-for-scheduling-recipients1.gif)

![Permission Control for Scheduling Recipients](https://devnet.logianalytics.com/hc/article_attachments/4404904220823/permission-control-for-scheduling-recipients2.gif)

Horizontal Table Word Wrap Enhancement

Fields in a horizontal table can now word wrap successfully to expand the cell height when you enable the Auto Fit feature for the columns in the table. You can also display the exact number of records or groups on one page with a fixed table cell width. You can also set the table property Split Overflow Columns to "true", to display a big table on multiple pages without cutting overflow columns, when there are many columns and one page cannot hold all the columns.

![Horizontal Table Word Wrap Enhancement](https://devnet.logianalytics.com/hc/article_attachments/4404904221079/horizontal-table-enhancement.gif)

Auto Fit Enhancement in Banded Object and Tabular Components

Large components can now well fit in tabular cells, and you can move components around in a tabular without changing any cell size. Banded objects can now also freely auto fit with the content in it at run time, so you won’t see unexpected empty space after you export banded objects to PDF, or see unnecessary scroll bars when viewing banded objects on the web.

![Auto Fit Enhancement in Banded Object and Tabular](https://devnet.logianalytics.com/hc/article_attachments/4404911665431/autofit-for-banded-object-and-tabular.gif)

For more information about the feature, select the following links:

* [Tabulars](https://devnet.logianalytics.com/hc/en-us/articles/1500009629321-Tabulars)
* [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634361-Logi-Report-v17-Release-Notes) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009627521-Logi-Report-Designer-Guide-v17-Update-1-Overview)
