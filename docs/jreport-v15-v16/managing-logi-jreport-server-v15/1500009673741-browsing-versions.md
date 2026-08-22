---
title: "Browsing Versions"
id: 1500009673741
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673741-Browsing-Versions
updated_at: 2021-07-24T20:54:00Z
---

# Browsing Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673781-Checking-Version-Properties)

# Browsing Versions

You can view the version information of a resource via its version table.

* For administrators, on the Logi JReport Administration > Resources page, browse to the folder that contains the resource, then select the **Version** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926662807/btn_srv_vrsn.gif) in the Control column. The version table of the resource is displayed.
* As an end user, you can view the version information of one or more resources at a time on the Logi JReport Console > Resources page.
  + To view the version information of a single resource, browse to the folder where the resource is located, then:
    - Put the mouse pointer over the resource row and select the **Version** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926662807/btn_srv_vrsn.gif) on the floating toolbar.
    - Right-select in the resource row and select **Version** from the shortcut menu.
    - Select the resource row and select **Tools** > **Version** on the task bar

    The version table of the resource is displayed.
  + To view the version information of multiple resources, browse to the folder where the resources are saved, check the checkboxes ahead of the required resources (to view the version information of all the resources, check the top checkbox), then select **Tools** > **Version** on the task bar, or right-click in any selected resource row and select **Version** from the shortcut menu. The version table for multiple resources is displayed.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Version Tables

Relevant information about the versions that a resource hosts, such as the version date, version number, is collected and represented in a table, called the version table. You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009650542-Working-with-Logi-JReport-Server-Guide-v15-Server#Version) to directly access the version table of a specific resource.

Some columns in the version table are not shown by default. To have them displayed, locate the table, select **Preferences** on the task bar if available, check the corresponding items in the Preferences dialog, then select **OK** to save the settings. The preference settings specified via the version table for multiple resources apply to the individual version tables of the selected resources.

**Catalog Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009649162-Editing-Local-NLS) for a specified catalog version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |

**Report Version table**

| Column | Description |
| --- | --- |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009649162-Editing-Local-NLS) for a specified report version by selecting the corresponding link. |
| Version Number | The serial ID that identifies a version in the version table. |

**Report Result** **Version table**

| Column | Description |
| --- | --- |
| Result | The output file formats. You can select the links to view the output files. To view a page report result file, necessary permissions are required. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009674841-Viewing-Scheduled-Report-Results#Version) for more information. |
| Version Date | The date and time of when the version is generated. You can sort the versions by version date. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameters. |
| Creator | The ID of the user who created the version. |
| Version Number | The serial ID that identifies a version in the version table. |

You can customize the maximum number of versions that can be kept in the table. To do this, check the **Maximum Number of Versions** option on the right top of the table, enter the required number in the text box and select the **OK** button. This number can also be specified when [creating the result version](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions#Result).

**Result** **Version**  **table**

| Column | Description |
| --- | --- |
| Result | The output file formats. You can select the links to view the output files. To view a page report result file, necessary permissions are required. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009674841-Viewing-Scheduled-Report-Results#Version) for more information. |
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
| NLS Editor | Administrators can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009649162-Editing-Local-NLS) for a specific library component version by selecting the corresponding link. |
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673781-Checking-Version-Properties)
