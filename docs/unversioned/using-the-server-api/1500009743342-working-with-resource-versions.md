---
title: "Working with Resource Versions"
id: 1500009743342
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009743342-Working-with-Resource-Versions
updated_at: 2021-07-24T00:49:33Z
---

# Working with Resource Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743242-Publishing-Resources-from-One-Server-to-Another)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743262-Changing-the-Runtime-Database-Connection)

# Working with Resource Versions

You can [manage versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009777341-Managing-Resource-Versions) using the Server API, other than on the Logi Report Server UI. This topic describes how you can specify the archive policy, schedule to save report results to versions, and obtain version information.

You can find program examples showing how to publish a report to the versioning system, how to run a report, and how to publish a catalog/report, in the  `<install_root>\help\samples\APIServer` folder.

This topic contains the following sections:

* [Applying an Archive Policy](#Archive)
* [Scheduling Report Result to the Versioning System](#Schedule)
* [Obtaining Version Information](#Info)

## Applying an Archive Policy

You may find that whenever you create catalog/report template versions, or report result versions, an archive policy is applied. The archive policy is a series of settings for controlling whether to use multiple versions for a specific resource, for specifying the maximum version amount and archive location, and for controlling whether to auto-delete versions after a certain period of time.

Here are some parameters that you will need when specifying your archive policy:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parameter | Value | Description | Parameter | Value | Description |
| APIConst.TAG\_ENABLE\_ARCHIVE\_POLICY | true/false | Whether or not to apply a new archive policy. |  |  |  |
| APIConst.TAG\_AUTO\_ARCHIVE | true/false | Whether or not to auto-archive the viewed result. |  |  |  |
| APIConst.TAG\_ARCHIVE\_LOCATION | 0 | Built-in version folder is used as the result archiving location. |  |  |  |
|  | 1 | The My Reports folder is used as the result archiving location. |  |  |  |
|  |  |  | APICONST. TAG\_ARCHIVE\_MY\_DESTINATION |  | Subfolder name in the My Reports folder for this user. For example, /rtp100, which means to output the file to /USERFOLDERPATH/<userid>/rtp100. |
|  | 2 | The Public Reports folder is used as the result archiving location. |  |  |  |
|  |  |  | APICONST. TAG\_ARCHIVE\_PUBLIC\_DESTINATION |  | Subfolder name in the Public Reports folder for all the users. For example, /ActimizeTest/rtp100 |
| APIConst.TAG\_REPLACE\_OLD\_VERSION | true/false | Whether or not to replace the previous version. |  |  |  |
| APIConst.TAG\_ARCHIVE\_NEW\_VERSION | true/false | Whether or not to archive the next version as a new version. |  |  |  |
|  |  |  |  |  |  |
| APICONST. TAG\_NEED\_MAXVERSION | 0 or N | The number of versions to keep for this resource result. |  |  |  |
| APICONST.TAG\_NEED\_EXPIRE | true/false | Whether or not to auto delete this version. |  |  |  |
| APIConst.TAG\_EXPIRE\_METHOD | 0 | Version expires after a number of days. |  |  |  |
|  |  |  | APIConst.DAY\_EXPIRE | Number | The number of days until a version expires. |
|  | 1 | Version expires after a certain date. |  |  |  |
|  |  |  | APIConst.TAG\_EXPIRE\_YEAR | Number | The year of expiration. |
|  |  |  | APIConst.TAG\_EXPIRE\_MONTH | Number | The month of expiration. |
|  |  |  | APIConst.TAG\_EXPIRE\_DATE | Number | The date of expiration. |

## Scheduling Report Result to the Versioning System

You can use the Java class **HttpRptServer** with the following methods to schedule report result to the versioning system: *runTask()* and *submitScheduledTask()*.

There is a Hashtable argument for these two methods, which includes the parameters used for running tasks. Here are some parameters that you will need when specifying your Hashtable for scheduling to version:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parameter | Value | Description | Parameter | Value | Description |
| APICONST.TAG\_TO\_VERSION | true/false | Whether or not to schedule to the versioning system. |  |  |  |
|  |  |  | APICONST.TAG\_TO\_VERSION\_EXCEL | true/false | Whether or not to schedule to an Excel version. |
|  |  |  | APICONST.TAG\_TO\_VERSION\_HTML | true/false | Whether or not to schedule to an HTML version. |
|  |  |  | APICONST.TAG\_TO\_VERSION\_PDF | true/false | Whether or not to schedule to a PDF version. |
|  |  |  | APICONST.TAG\_TO\_VERSION\_PS | true/false | Whether or not to schedule to a PostScript version. |
|  |  |  | APICONST.TAG\_TO\_VERSION\_RSD | true/false | Whether or not to schedule to a Page Report Result version. |
|  |  |  | APICONST.TAG\_TO\_VERSION\_RST | true/false | Whether or not to schedule to an rst version |
|  |  |  | APICONST.TAG\_TO\_VERSION\_RTF | true/false | Whether or not to schedule to an rtf version. |
|  |  |  | APICONST.TAG\_TO\_VERSION\_TXT | true/false | Whether or not to schedule to a TEXT version. |
|  |  |  | APICONST.TAG\_TO\_VERSION\_XML | rue/false | Whether or not to schedule to an XML version. |

## Obtaining Version Information

You will be able to fetch version records with the following function calls:

1. Get the resource manager from the HttpRptServer:

   `public ResourceManager getResourceManager()`
2. Then use the following methods to obtain a version:
   * **Report version**  
      getReportVersions(String userID, String rptName)
   * **Report Result version**  
      getResultVersion(String userID, String rptName, int versionNumber)
   * **Catalog version**  
      getCatalogVersions(String userID, String catName)
   * **Result version**  
      getResultDocVersions(String userID, String resultDocName)
   * **Dashboard version**  
      getReportVersions(String userID, String dashboardName)
   * **Library component version**  
      getLCVersions(String userID, String lcName)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)**userID** is only used for checking privilege in this method, and not for filtering the submitter.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743242-Publishing-Resources-from-One-Server-to-Another)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743262-Changing-the-Runtime-Database-Connection)
