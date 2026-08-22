---
title: "Working with Parameter Fields"
id: 5735512482071
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields
updated_at: 2022-11-02T04:13:16Z
---

# Working with Parameter Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields)

# Working with Parameter Fields

A [parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735532413719-Working-with-Parameters) in Logi Report is a variable whose value is determined at runtime. The runtime parameters help you dynamically control your report. This topic introduces how you can insert parameter fields in a report and apply conditional formatting to the parameter fields.

For the parameter fields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/5735555544087-Changing-the-Display-Type-of-Objects-in-a-Report) if you want.

This topic contains the following sections:

* [Inserting Parameter Fields in a Report](#Insert)
* [Adding Conditional Formatting to Parameter Fields](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the parameter field examples, open the following reports: `<install_root>\Demo\Reports\SampleComponents\Parameter.cls`, and `<install_root>\Demo\Reports\SampleComponents\ParameterField.cls`.

## Inserting Parameter Fields in a Report

You can insert parameter fields in the report areas listed in [Component Placement in Different Report Type](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type).

To insert a parameter field into a report, in the **Data** panel, select a dataset from the dataset drop-down list, then select the parameter from the **Parameters** node and drag it to the destination. When the predefined parameters are not what your want, you can select **<New Parameter...>** to [create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735516481047-Creating-Parameters-in-a-Catalog). For a business view-based report, you can also create [local parameters](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Param) to use in the report specifically.

For a query-based page report, you can also use dialog box to insert a parameter field into it.

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the parameter.
2. Navigate to **Insert** > **Parameter** or **Home** >
   **Insert** > **Parameter**. Designer displays the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530158487-Insert-Fields-Dialog-Box).

   ![Insert Field dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898462184727/instfld.gif)
3. Select a dataset from the dataset drop-down list. Designer then lists all resources in the specified dataset. However, if you are inserting parameter fields into a data component, you should not change the dataset. You can only apply one dataset in a data component.
4. Select the parameter you need from the **Parameters** node. You can select multiple parameters to insert them all at a time.
5. When you select multiple parameters, in the **Insert Layout** box, specify the layout of the parameter fields in the report. By default, Designer arranges them in the default layout. You can arrange the parameter fields horizontally or vertically by selecting **Horizontal** or **Vertical**, and customize the space between them.
6. Select **Insert** to insert the parameter fields into the destination.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) If you insert a parameter into the detail panel of a banded object or table, Designer automatically inserts its name as a label into the corresponding header panel; otherwise, Designer places the parameter and its name label in the same panel. If you do not want Designer to insert the name label automatically, clear "Insert field name label with field" in the Component category of the Options dialog box.

## Adding Conditional Formatting to Parameter Fields

You can add conditional formatting to parameter fields in a report, so the field values that meet a specified condition can automatically apply the formatting you define for the condition. This is very useful to highlight values that users may need to act on at runtime.

To apply conditional formatting to a parameter field, right-click it and select **Conditional Formatting** from the shortcut menu, then take the same procedure as described in [Adding Conditional Formatting to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields)
