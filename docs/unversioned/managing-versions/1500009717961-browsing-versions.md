---
title: "Browsing Versions"
id: 1500009717961
section: "Managing Versions"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717961-Browsing-Versions
updated_at: 2021-11-03T06:56:52Z
---

# Browsing Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717981-Creating-Versions)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718001-Checking-Version-Properties)

# Browsing Versions

You can view the version information of a resource via its version table in the Resources page of the server console.

* To view the version information of a single resource, browse to the folder where the resource is located, then:
  + Put the mouse pointer over the resource row and select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4412131412631/btn_srv_vrsn.gif) on the floating toolbar.
  + Right-click in the resource row and select **Version** from the shortcut menu.
  + Select the resource row and select **Tools** > **Version** on the task bar.

  The version table of the resource is displayed.
* To view the version information of multiple resources at a time, browse to the folder where the resources are saved, check the checkboxes ahead of the required resources (to view the version information of all the resources, check the top checkbox), then select **Tools** > **Version** on the task bar, or right-click in any selected resource row and select **Version** from the shortcut menu. The version table for multiple resources is displayed.

## Version Tables

Relevant information about the versions that a resource hosts, such as the version date and version number, is collected in a table called the version table. You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009719381-Working-with-Logi-Report-Server#Version) to directly access the version table of a specific resource.

![Version Table](https://devnet.logianalytics.com/hc/article_attachments/4412131435031/mng_vrsn_browse.gif)

The following shows the columns contained in the version tables of different resource types.

**Catalog Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009718081-NLS-at-Report-Level#Local) for a specified catalog version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |

**Report Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009718081-NLS-at-Report-Level#Local) for a specified report version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |
| Creator | The ID of the user who creates the version. Available to web reports that are used to created [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009717901-Sharing-Reports) only. |
| Status | Indicates whether the version is finished or unfinished. Available to web reports that are used to create shared reports only. |

**Report Result** **Version table**

| Column | Description |
| --- | --- |
| Result | The output file formats. You can select the links to view the output files. To view a page report result file, necessary permissions are required. See [Viewing Results Scheduled to Version](https://devnet.logianalytics.com/hc/en-us/articles/1500009718741-Viewing-Scheduled-Report-Results#Version) for more information. |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameters. |
| Creator | The ID of the user who created the version. |
| Version Number | The serial ID that identifies a version in the version table. |

You can customize the maximum number of versions that can be kept in the Report Result Version table. To do this, check the **Maximum Number of Versions** option on the right top of the table, enter the required number in the text box and select the **OK** button. This number can also be specified when [creating the result version](https://devnet.logianalytics.com/hc/en-us/articles/1500009717981-Creating-Versions#Result).

**Result** **Version**  **table**

| Column | Description |
| --- | --- |
| Result | The output file formats. You can select the links to view the output files. To view a page report result file, necessary permissions are required. See [Viewing Results Scheduled to Version](https://devnet.logianalytics.com/hc/en-us/articles/1500009718741-Viewing-Scheduled-Report-Results#Version) for more information. |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameters. |
| Creator | The ID of the user who created the version. |
| Version Number | The serial ID that identifies a version in the version table. |

**Dashboard Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| Version Number | The serial ID that identifies a version in the version table. |

**Library Component Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009718081-NLS-at-Report-Level#Local) for a specific library component version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |

**Analysis Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| Version Number | The serial ID that identifies a version in the version table. |

**Version table for multiple resources**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| Version Number | The serial ID that identifies a version for a specific resource in its version table. |
| Path | The path of the resource in the server resource tree. |

**Tip:** When accessing the version tables from the server console, end users can customize the columns shown in the tables as follows: locate the table, select **Preferences** on the task bar of the Resources page, check the corresponding items in the Preferences dialog, then select **OK** to apply the settings.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717981-Creating-Versions)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718001-Checking-Version-Properties)
