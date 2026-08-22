---
title: "Mapping Table Dialog Box"
id: 4405661647639
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661647639-Mapping-Table-Dialog-Box
updated_at: 2022-01-27T20:38:02Z
---

# Mapping Table Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661641879-Manage-Datasets-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664530199-Merge-Dialog-Box)

# Mapping Table Dialog Box

You can use the Mapping Table dialog box to define the [mapping relationship](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports#Map), based on which to set up the filter relationship between the primary report and the linked report. This topic describes the options in the dialog box.

Designer displays the Mapping Table dialog box when you select Mapping Table in the [Insert Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664522263-Insert-Link-Dialog-Box) or [Edit Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661518487-Edit-Link-Dialog-Box).

![Mapping Table dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550879639/mptbl.gif)

You see the following options in the dialog box:

**Fields (Primary)**

This column shows the fields in the primary report that you select to set up the mapping relationship.

This drop-down list in the column contains all the fields in the data resource used by the data component that contains the trigger object in the primary report. Select a field that is bound with an on-screen filter to define the mapping relationship.

**Fields (Linked)**

This column shows the fields in the linked report that you select to set up the mapping relationship.

This drop-down list in the column contains all the fields in the data resource used by the selected component in the linked report, which are of the same data type as the specified primary report field. Select a field whose values are the same as those of the specified primary report field, then when the link is triggered at runtime, Server applies the corresponding on-screen filter in the primary report to the selected linked report field.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif)**Add button**

Select to add a mapping line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**

Select to delete the specified mapping line.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661641879-Manage-Datasets-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664530199-Merge-Dialog-Box)
