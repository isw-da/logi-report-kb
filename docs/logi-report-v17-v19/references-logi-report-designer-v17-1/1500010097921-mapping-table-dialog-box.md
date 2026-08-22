---
title: "Mapping Table Dialog Box"
id: 1500010097921
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097921-Mapping-Table-Dialog-Box
updated_at: 2021-07-23T19:15:44Z
---

# Mapping Table Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059762-Manage-Datasets-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059742-Merge-Dialog-Box)

# Mapping Table Dialog Box

You can use the Mapping Table dialog box to define the [mapping relationship](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports#Map), based on which to set up the filter relationship between the primary report and the linked report. This topic describes the options in the dialog box.

Designer displays the Mapping Table dialog box when you select the Mapping Table button in the [Insert Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097661-Insert-Link-Dialog-Box) or [Edit Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096301-Edit-Link-Dialog-Box).

![Mapping Table dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856830743/mptbl.gif)

You see the following options in the dialog box:

**Fields (Primary)**

The column shows the fields in the primary report that you select to set up the mapping relationship.

The drop-down list in the column contains all the fields in the data resource used by the data component that contains the trigger object in the primary report. Select a field that is bound with an on-screen filter to define the mapping relationship.

**Fields (Linked)**

The column shows the fields in the linked report that you select to set up the mapping relationship.

The drop-down list in the column contains all the fields in the data resource used by the selected component in the linked report, which are of the same data type as the specified primary report field. Select a field whose values are the same as those of the specified primary report field, then when the link is triggered at runtime, Logi Report Engine applies the corresponding on-screen filter in the primary report to the selected linked report field.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a mapping line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified mapping line.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059762-Manage-Datasets-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059742-Merge-Dialog-Box)
