---
title: "Working with Parameter Fields"
id: 1500010057382
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057382-Working-with-Parameter-Fields
updated_at: 2021-07-23T19:14:48Z
---

# Working with Parameter Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields)

# Working with Parameter Fields

A [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099721-Working-with-Parameters) in Logi Report is a variable whose value is determined at runtime. The runtime parameters help you dynamically control your report result. This topic introduces how you can insert parameter fields in a report and apply conditional formats to the parameter fields.

For the parameter fields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports) if you want.

This topic contains the following sections:

* [Inserting Parameter Fields in a Report](#Insert)
* [Adding Conditional Formats to Parameter Fields](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the parameter field examples, open the following reports: `<install_root>\Demo\Reports\SampleComponents\Parameter.cls`, and `<install_root>\Demo\Reports\SampleComponents\ParameterField.cls`.

## Inserting Parameter Fields in a Report

You can insert parameter fields in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship).

To insert a parameter field into a report, select the required parameter from the **Data** panel, then drag it to the destination. If the given parameters are not what your want, select the **<New Parameter...>** item to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog) as required. For a business view-based report, you can create [local parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param) to use in the report specifically.

For a page report using a query resource, you can also use dialog box to insert a parameter field into it as follows:

1. Position the mouse pointer at the destination where you want to insert the parameter.
2. Select **Insert** > **Parameter** or **Home** >
   **Insert** > **Parameter**. Designer displays the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097601-Insert-Fields-Dialog-Box).

   ![Insert Field dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848523671/instfld.gif)
3. Select the required parameter from the **Parameters** node. You can select multiple parameters to insert them all a time.
4. If you select multiple parameters, in the **Insert Layout** box, specify the layout of the parameter fields in the report. By default, Designer arranges them in the default layout. You can arrange the parameter fields horizontally or vertically by selecting **Horizontal** or **Vertical**, and customize the space between them.
5. Select the **Insert** button to insert the parameter fields into the destination.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If you insert a parameter into the detail panel of a banded object or table, Designer automatically inserts its name as a label into the corresponding header panel; otherwise, Designer places the parameter and its name label in the same panel. If you do not want Designer to insert the name label automatically, you can clear **Insert field name label with field** in the Options dialog box (File > Options > Component > Insert field name label with field).

## Adding Conditional Formats to Parameter Fields

You can add conditional formats to parameter fields in a report, then when a specified condition is fulfilled, Logi Report automatically applies the format defined on the condition to the field values. This is very useful to highlight values that the report users may need to act on at runtime.

To add conditional format to a parameter field, right-click it and select **Conditional Formatting** from the shortcut menu, then take the same procedure as described in [Adding Conditional Formats to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields)
