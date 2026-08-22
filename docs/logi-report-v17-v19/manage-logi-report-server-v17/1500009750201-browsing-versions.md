---
title: "Browsing Versions"
id: 1500009750201
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750201-Browsing-Versions
updated_at: 2021-07-25T07:18:57Z
---

# Browsing Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750221-Creating-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723242-Checking-Version-Properties)

# Browsing Versions

You can view the version information of a resource via its version table in the Resources page of the server console.

* To view the version information of a single resource, browse to the folder where the resource is located, then:
  + Put the mouse pointer over the resource row and select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4404942480279/btn_srv_vrsn.gif) on the floating toolbar.
  + Right-click in the resource row and select **Version** from the shortcut menu.
  + Select the resource row and select **Tools** > **Version** on the task bar.

  Report Server displays the version table of the resource.
* To view the version information of multiple resources at a time, browse to the folder where the resources are saved, select the check boxes ahead of the required resources (to view the version information of all the resources, select the top check box), then select **Tools** > **Version** on the task bar, or right-click in any selected resource row and select **Version** from the shortcut menu. Report Server displays the version table for multiple resources.

## Version Tables

Relevant information about the versions that a resource hosts, such as the version date and version number, is collected in a table called the version table. You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009725002-Working-with-Logi-Report-Server#Version) to directly access the version table of a specific resource.

![Version Table](https://devnet.logianalytics.com/hc/article_attachments/4404936796439/mng_vrsn_browse.gif)

The following shows the columns contained in the version tables of different resource types.

**Catalog Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level#Local) for a specified catalog version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |

**Report Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level#Local) for a specified report version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |
| Creator | The ID of the user who creates the version. Available to web reports that are used to created [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports) only. |
| Status | Indicates whether the version is finished or unfinished. Available to web reports that are used to create shared reports only. |

**Report Result Version table**

| Column | Description |
| --- | --- |
| Results | The output file formats. You can select the format links to view the output files (see [Viewing Results Scheduled to Version](https://devnet.logianalytics.com/hc/en-us/articles/1500009751161-Viewing-Scheduled-Report-Results#Version) for more information). You can also download the output files to your local directory.  * To download the output of a report result version, do any of the following:   + Put the mouse pointer over the version row and select the **Download** button Download button on the floating toolbar.   + Select the version row and select **Edit** > **Download** on the task bar.   + Select the version row, right-click in the row and select **Download** on the shortcut menu. Then, if the report result version contains only one output file, the file will be sent to the web browser for downloading; if the version contains multiple output files, Logi Report Server will add all the files into a zip file and send the zip file to the web browser for downloading. * To download the output of multiple report result versions at a time, select the version rows, then select **Edit** > **Download** on the task bar or right-click in any version row and select **Download** from the shortcut menu. Logi Report Server will then put all the output files of the selected versions into one zip file, with the output files of each version stored in a separate subfolder, and send the zip file to the web browser for downloading. |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameters. |
| Creator | The ID of the user who created the version. |
| Version Number | The serial ID that identifies a version in the version table. |

You can customize the maximum number of versions that can be kept in the Report Result Version table. To do this, select the **Maximum Number of Versions** option on the right top of the table, type the required number in the text box and select the **OK** button. This number can also be specified when [creating the result version](https://devnet.logianalytics.com/hc/en-us/articles/1500009750221-Creating-Versions#Result).

**Result Version table**

| Column | Description |
| --- | --- |
| Results | The output file formats. You can select the format links to view the output files or download the output files to your local directory in the same way as shown in the Report Result Version table. |
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
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level#Local) for a specific library component version by selecting the corresponding link. |
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

**Tips:**

* When accessing the version tables from the server console, end users can customize the columns shown in the tables as follows: locate the table, select **Preferences** on the task bar of the Resources page, select the corresponding items in the Preferences dialog box, then select **OK** to apply the settings.
* In the result version tables, the unviewed results are highlighted in bold. You can cancel the highlighting by setting the property web.version.mark\_unviewed to false in the server.properties file in `<install_root>\bin`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750221-Creating-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723242-Checking-Version-Properties)
