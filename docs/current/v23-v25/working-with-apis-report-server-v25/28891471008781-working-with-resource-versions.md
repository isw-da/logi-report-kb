---
title: "Working with Resource Versions"
id: 28891471008781
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891471008781-Working-with-Resource-Versions
updated_at: 2026-02-26T02:11:11Z
source_host: docs-report.zendesk.com
---
# 
Working with Resource Versions

You can manage versions using the Server API, other than on the Report Server UI. This topic describes how you can specify the archive policy, schedule to save reports to versions, and obtain version information.

You can find program examples showing how to publish a report to the versioning system, how to run a report, and how to publish a catalog/report, in the  <install_root>\help\samples\APIServer folder. 

This topic contains the following sections:

- Applying an Archive Policy

- Scheduling Reports to the Versioning System

- Obtaining Version Information

## 
Applying an Archive Policy

You may find that whenever you create catalog/report template versions, or report result versions, Server applies an archive policy to them. The archive policy is a series of settings for controlling whether to use multiple versions for a specific resource, for specifying the maximum version amount and archive location, and for controlling whether to auto-delete versions after a certain period of time.

 Here are some parameters that you will need when specifying your archive policy:

| Parameter | Value | Description | Parameter | Value | Description |
| --- | --- | --- | --- | --- | --- |
| APIConst.TAG_ENABLE_ARCHIVE_POLICY | true/false | Whether or not to apply a new archive policy. |  |  |  |
| APIConst.TAG_AUTO_ARCHIVE | true/false | Whether or not to auto-archive the viewed report. |  |  |  |
| APIConst.TAG_ARCHIVE_LOCATION | 0 | Use the built-in version folder as the archiving location. |  |  |  |
|  | 1 | Use the My Reports folder as the archiving location. |  |  |  |
|  |  |  | APICONST. TAG_ARCHIVE_MY_DESTINATION |  | Subfolder name in the My Reports folder for this user. For example, /rtp100, which means to output the file to /USERFOLDERPATH//rtp100. |
|  | 2 | Use the Public Reports folder the archiving location. |  |  |  |
|  |  |  | APICONST. TAG_ARCHIVE_PUBLIC_DESTINATION |  | Subfolder name in the Public Reports folder for all the users. For example, /ActimizeTest/rtp100 |
| APIConst.TAG_REPLACE_OLD_VERSION | true/false | Whether or not to replace the previous version. |  |  |  |
| APIConst.TAG_ARCHIVE_NEW_VERSION | true/false | Whether or not to archive the next version as a new version. |  |  |  |
| APICONST. TAG_NEED_MAXVERSION | 0 or N | The number of versions to keep for this resource. |  |  |  |
| APICONST.TAG_NEED_EXPIRE | true/false | Whether or not to auto delete this version. |  |  |  |
| APIConst.TAG_EXPIRE_METHOD | 0 | Version expires after a number of days. |  |  |  |
|  |  |  | APIConst.DAY_EXPIRE | Number | The number of days until a version expires. |
|  | 1 | Version expires after a certain date. |  |  |  |
|  |  |  | APIConst.TAG_EXPIRE_YEAR | Number | The year of expiration. |
|  |  |  | APIConst.TAG_EXPIRE_MONTH | Number | The month of expiration. |
|  |  |  | APIConst.TAG_EXPIRE_DATE | Number | The date of expiration. |

## 
Scheduling Reports to the Versioning System

You can use the Java class HttpRptServer with the following methods to schedule reports to the versioning system: runTask() and submitScheduledTask().

There is a Hashtable argument for these two methods, which includes the parameters used for running tasks. Here are some parameters that you will need when specifying your Hashtable for scheduling to version:

| Parameter | Value | Description | Parameter | Value | Description |
| --- | --- | --- | --- | --- | --- |
| APICONST.TAG_TO_VERSION | true/false | Whether or not to schedule to the versioning system. |  |  |  |
|  |  |  | APICONST.TAG_TO_VERSION_EXCEL | true/false | Whether or not to schedule to an Excel version. |
|  |  |  | APICONST.TAG_TO_VERSION_HTML | true/false | Whether or not to schedule to an HTML version. |
|  |  |  | APICONST.TAG_TO_VERSION_PDF | true/false | Whether or not to schedule to a PDF version. |
|  |  |  | APICONST.TAG_TO_VERSION_PS | true/false | Whether or not to schedule to a PostScript version. |
|  |  |  | APICONST.TAG_TO_VERSION_RSD | true/false | Whether or not to schedule to a Page Report Result version. |
|  |  |  | APICONST.TAG_TO_VERSION_RST | true/false | Whether or not to schedule to an rst version |
|  |  |  | APICONST.TAG_TO_VERSION_RTF | true/false | Whether or not to schedule to an rtf version. |
|  |  |  | APICONST.TAG_TO_VERSION_TXT | true/false | Whether or not to schedule to a TEXT version. |
|  |  |  | APICONST.TAG_TO_VERSION_XML | rue/false | Whether or not to schedule to an XML version. |

## 
Obtaining Version Information

You will be able to fetch version records with the following function calls: 

- Get the resource manager from the HttpRptServer:
    public ResourceManager getResourceManager()

- Then use the following methods to obtain a version:
    
- 
Report version
          getReportVersions(String userID, String rptName)

- 
Report Result version
        getResultVersion(String userID, String rptName, int versionNumber)

- 
Catalog version
        getCatalogVersions(String userID, String catName)

- 
Result version
        getResultDocVersions(String userID, String resultDocName)

- 
Dashboard version
        getReportVersions(String userID, String dashboardName)

- 
Library component version
        getLCVersions(String userID, String lcName)

userID is only used for checking privilege in this method, and not for filtering the submitter.
