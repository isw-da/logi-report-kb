---
title: "Browsing Versions"
id: 5741462114583
section: "Managing Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741462114583-Browsing-Versions
updated_at: 2022-10-31T17:18:10Z
---

# Browsing Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741462158487-Creating-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741482415639-Checking-Version-Properties)

# Browsing Versions

This topic describes how you can view the version information of a resource via its version table in the Resources page of the Server Console.

* To view the version information of a single resource, browse to the folder where the resource is, then:
  + Put the mouse pointer over the resource row and select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/9905658584855/btn_srv_vrsn.gif) on the floating toolbar.
  + Right-click in the resource row and select **Version** from the shortcut menu.
  + Select the resource row and select **Tools** > **Version** on the task bar.

  Server displays the version table of the resource.
* To view the version information of multiple resources at a time, browse to the folder where the resources are, select the required resources (to view the version information of all the resources, select the top checkbox), then select **Tools** > **Version** on the task bar, or right-click in any selected resource row and select **Version** from the shortcut menu. Server displays the version table for multiple resources.

## Version Tables

Server collects relevant information about the versions that a resource hosts, such as the version date and version number, in a table called the version table. You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/5741485252503-Working-with-Server-via-URL#Version) to directly access the version table of a specific resource.

![Version Table](https://devnet.logianalytics.com/hc/article_attachments/9905713924247/mng_vrsn_browse.gif)

The following shows the columns contained in the version tables of different resource types.

**Catalog Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time when Server generated the version. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741482629911-NLS-at-Report-Level#Local) for a specified catalog version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |

**Report Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time when Server generated the version. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741482629911-NLS-at-Report-Level#Local) for a specified report version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |
| Creator | The ID of the user who created the version. Available to web reports that you used create [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports) only. |
| Status | Indicate whether the version is finished or unfinished. Available to web reports that you used to create shared reports only. |

**Report Result Version table**

| Column | Description |
| --- | --- |
| Results | The output file formats. You can select the format links to view the output files (see [Viewing Results Scheduled to Version](https://devnet.logianalytics.com/hc/en-us/articles/5741469840663-Viewing-Scheduled-Reports#Version) for more information). You can also download the output files to your local directory.  * To download the output of a report result version, do any of the following:   + Put the mouse pointer over the version row and select the **Download** button Download button on the floating toolbar.   + Select the version row and select **Edit** > **Download** on the task bar.   + Select the version row, right-click in the row, and select **Download** on the shortcut menu. Then, if the report result version contains only one output file, Server sends the file to the web browser for downloading; if the version contains multiple output files, Server adds all the files into a zip file and sends the zip file to the web browser for downloading. * To download the output of multiple report result versions at a time, select the version rows, then select **Edit** > **Download** on the task bar or right-click in any version row and select **Download** from the shortcut menu. Server puts all the output files of the selected versions into one zip file, stores the output files of each version in a separate sub folder, and sends the zip file to the web browser for downloading. |
| Version Date | The date and time when Server generated the version. You can sort the versions by version date. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameters. |
| Creator | The ID of the user who created the version. |
| Version Number | The serial ID that identifies a version in the version table. |

You can customize the maximum number of versions that Server can keep in the Report Result Version table. To do this, select the **Maximum Number of Versions** option on the right top of the table, type the required number in the text box and select **OK**. You can also specify this number when [creating the result version](https://devnet.logianalytics.com/hc/en-us/articles/5741462158487-Creating-Versions#Result).

**Result Version table**

| Column | Description |
| --- | --- |
| Results | The output file formats. You can select the format links to view the output files or download the output files to your local directory in the same way as shown in the Report Result Version table. |
| Version Date | The date and time when Server generated the version. You can sort the versions by version date. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameters. |
| Creator | The ID of the user who created the version. |
| Version Number | The serial ID that identifies a version in the version table. |

**Dashboard Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time when Server generated the version. You can sort the versions by version date. |
| Version Number | The serial ID that identifies a version in the version table. |

**Library Component Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time when Server generated the version. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741482629911-NLS-at-Report-Level#Local) for a specific library component version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |

**Analysis Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time when Server generated the version. You can sort the versions by version date. |
| Version Number | The serial ID that identifies a version in the version table. |

**Version table for multiple resources**

| Column | Description |
| --- | --- |
| Version Date | The date and time when Server generated the version. You can sort the versions by version date. |
| Version Number | The serial ID that identifies a version for a specific resource in its version table. |
| Path | The path of the resource in the server resource tree. |

**Tips:**

* When accessing the version tables on the Server Console, you can customize the columns in the tables: locate the table, select **Preferences** on the task bar of the Resources page, select the corresponding items in the Preferences dialog box, then select **OK** to apply the settings.
* In the result version tables, Server highlights the results that you have not viewed in bold. You can cancel the highlighting by setting the property **web.version.mark\_unviewed** to **false** in the **server.properties** file in `<install_root>\bin`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741462158487-Creating-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741482415639-Checking-Version-Properties)
