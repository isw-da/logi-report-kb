---
title: "Mapping Table Dialog"
id: 1500009587841
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587841-Mapping-Table-Dialog
updated_at: 2021-07-24T05:55:02Z
---

# Mapping Table Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587781-Manage-Datasets-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566662-Merge-Dialog)

# Mapping Table Dialog

The Mapping Table dialog appears when you select the button Mapping Table in the Insert Link dialog for [page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009566502-Insert-Link-Dialog-for-Page-Report-) or [web report/library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009566482-Insert-Link-Dialog-for-Web-Report-and-Library-Component-), or in the Edit Link dialog for [page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009586481-Edit-Link-Dialog-for-Page-Report-) or [web report/library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009586461-Edit-Link-Dialog-for-Web-Report-and-Library-Component-). It helps you to define the [mapping relationship](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label#Map) based on the way the filter relationship between the primary report and the linked report is set up. [See the dialog](javascript:%20void(null)).

![Mapping Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893865111/mptbl.gif)

The following are details about options in the dialog:

**Fields (Primary)**

Specifies the fields in the primary report to set up the mapping relationship.

All fields in the dataset used by the trigger component in the primary report are listed. Select a field that is bound with an on-screen filter to define the mapping relationship.

**Fields (Linked)**

Specifies the fields in the linked report to set up the mapping relationship.

The drop-down list contains all the fields in the dataset used by the selected component in the linked report which are of the same data type as the specified primary report field. Select a field whose values are the same as those of the specified primary report field, then when the link is triggered, the corresponding on-screen filter in the primary report will be applied on the selected linked report field.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a mapping line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected mapping lines.

**OK**

Applies the settings and closes the dialog.

**Cancel**

Closes the dialog, leaving any changes unsaved.

**Help**

Displays the help document.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587781-Manage-Datasets-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566662-Merge-Dialog)
