---
title: "Logi Report v19 Enhancements"
id: 5741431563031
section: "Release Notes for Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741431563031-Logi-Report-v19-Enhancements
updated_at: 2022-10-31T17:18:51Z
---

# Logi Report v19 Enhancements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741437478167-Logi-Report-v19-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741393125527-Logi-Report-Server-Guide-v19-Overview)

# Logi Report v19 Enhancements

This topic describes the significant enhancements in Logi Report v19.

* [Enhanced UX](#UX)
* [Enhanced Table of Contents](#TOC)
* [Enhanced Export Capabilities](#Export)
* [Enhanced Performance and Scalability](#Performance)

## Enhanced UX

* You can now share datasets that are based on business views between data components in a web or page report, to improve the report performance at runtime.

  ![Share Dataset](https://devnet.logianalytics.com/hc/article_attachments/9905715936535/share-dataset.jpg)
* You can now use data container links in web reports to set up data relations between two data containers in a parent-child relationship.

  ![Data Container Link](https://devnet.logianalytics.com/hc/article_attachments/9905677494167/data-container-link.jpg)

## Enhanced Table of Contents

You can now display additional information such as a cover or preface for a report before the Table of Contents, and insert the Export Page Number and Export Total Page Number special fields in the report to display number for the cover, TOC, and report content pages differently or continuously (by setting the report's Continuous Page Number with TOC property). Using the Ignore TOC Anchor of Parent property, you can customize whether to generate TOC entries for objects that are contained in other objects when you exclude their parent objects from the TOC.

![Enhanced TOC](https://devnet.logianalytics.com/hc/article_attachments/9905677528727/enhanced-toc.jpg)

## Enhanced Export Capabilities

* You can now select Use Custom File Extension on the export UI if you want to use your preferred extension (or to have no extension) for the file name of your report output.

  ![Use Custom File Extension](https://devnet.logianalytics.com/hc/article_attachments/9905716049175/custom-file-extension.png)
* You can now define the Title and Subject properties for the PDF output of your reports.

  ![PDF Title and Subject](https://devnet.logianalytics.com/hc/article_attachments/9905716085655/pdf-title-subject.jpg)

## Enhanced Performance and Scalability

* You can now call the method *\_client.send(Request)* or *\_client.send(Request[], integer)* in a formula to fetch paginated JSON data from a REST Web Service either sequentially or concurrently.

  ![Paginated JSON Data Fetch](https://devnet.logianalytics.com/hc/article_attachments/9905716127639/paginated-data-fetch.jpg)
* Logi Report now attempts to apply all filters to the database when generating report data, when you enable On-Screen Filter Push-Down.

  ![Push Down On-screen Filters to Database](https://devnet.logianalytics.com/hc/article_attachments/9905716168215/push-down.png)
* Administrators can now cache JSON/XML connection data on Server in advance so that reports created from these connections can reuse the cached data, improving the report rendering performance.

  ![Cached Connection Data](https://devnet.logianalytics.com/hc/article_attachments/9905677700247/cached-connection-data.png)
* You can now use REST APIs to schedule report bursting tasks to Version/Disk/E-mail/FTP, and schedule non-bursting results to Version/Disk/E-mail/Printer/Fax/FTP. For E-mail and FTP, you can also update properties of different formats.

  ![Report Bursting Schedule via REST APIs](https://devnet.logianalytics.com/hc/article_attachments/9905716215447/burst-schedule.png)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741437478167-Logi-Report-v19-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741393125527-Logi-Report-Server-Guide-v19-Overview)
