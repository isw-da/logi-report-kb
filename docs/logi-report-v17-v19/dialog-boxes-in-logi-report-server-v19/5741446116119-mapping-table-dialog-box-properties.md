---
title: "Mapping Table Dialog Box Properties"
id: 5741446116119
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741446116119-Mapping-Table-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:39Z
---

# Mapping Table Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985360502423-Manage-Datasets-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741436173335-Navigation-Control-Properties)

# Mapping Table Dialog Box Properties

This topic describes how you can use the Mapping Table dialog box to define the mapping relationship between fields in the primary report and linked report.

---

When you select **Mapping Table** in the [Insert Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459269271-Insert-Link-Dialog-Box-Properties) or [Edit Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741434764823-Edit-Link-Dialog-Box-Properties), the Mapping Table dialog box looks like this. You can define the [mapping relationship](https://devnet.logianalytics.com/hc/en-us/articles/5741456004887-Adding-Links-in-Web-Report#Map) based on which Server passes the on-screen filters in the primary report to the linked report.

![Mapping Table dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905631644823/mptbl.gif)

**Fields (Primary)**

Specify the fields in the primary report to set up the mapping relationship.

The drop-down list contains all fields in the business view used by the trigger component in the primary report. However, if the trigger object is in a crosstab, Server only lists the field that is related to the trigger object. Select a field that binds with an on-screen filter to define the mapping relationship.

**Fields (Linked)**

Specify the fields in the linked report to set up the mapping relationship.

The drop-down list contains all the fields in the business view used by the selected component in the linked report, which are of the same data type as the specified primary report field. Select a field whose values are the same as those of the specified primary report field. Then, when you trigger the link, the corresponding on-screen filter in the primary report will apply to the selected linked report field.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif)**Add button**

Select to add a mapping line.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**

Select to remove the selected mapping line.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

---

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")When you select a linked data component in the **Components** box and then select the **Mapping Table** button ![Mapping Table button](https://devnet.logianalytics.com/hc/article_attachments/9905619314327/btn_mptbl.gif) in the **Field Conditions** section in the [Insert Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459269271-Insert-Link-Dialog-Box-Properties) or [Edit Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741434764823-Edit-Link-Dialog-Box-Properties), the Mapping Table dialog box looks like this. You can define the mapping relationship between Current Field in the primary report and Corresponding Field in the linked report.

![Mapping Table dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905619328151/mptbl-1.gif)

**Current Field**

Specify the fields in the primary report to set up the mapping relationship.

The drop-down list contains all the fields in the business view used by the data component that contains the trigger object in the primary report. However, if the trigger object is in a crosstab, Server only lists the field that is related to the trigger object. Select a field to define the mapping relationship.

**Corresponding Field**

Specify the fields in the linked report to map to the current field you specified.

The drop-down list contains all the fields in the business view used by the linked data component in the linked report, which are of the same data type as the current field. Select a field whose values are the same as those of the current field.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif)**Add button**

Select to add a mapping line.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**

Select to remove the selected mapping line.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985360502423-Manage-Datasets-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741436173335-Navigation-Control-Properties)
