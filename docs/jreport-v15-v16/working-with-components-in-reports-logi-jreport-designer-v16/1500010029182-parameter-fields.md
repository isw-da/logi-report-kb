---
title: "Parameter Fields"
id: 1500010029182
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029182-Parameter-Fields
updated_at: 2021-07-24T10:39:20Z
---

# Parameter Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063761-DBFields) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029262-Summary-Fields-)

# Parameter Fields

A [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010068961-Parameters) in Logi JReport is a variable whose value is determined at runtime. The runtime parameters help you dynamically control your report result.

Parameter fields in a report can be used as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports), and you can change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/1500010034802-Changing-the-Display-Type-of-Objects-in-Reports) if you want.

Below is a list of the sections covered in this topic:

* [Inserting Parameter Fields in a Report](#Insert)
* [Adding Conditional Formats to Parameter Fields](#Format)

**See an example:** The SampleComponents catalog, included with Logi JReport Designer, contains reports that have examples of how each component type could be used in a report. For the parameter field examples, open the following reports: `<install_root>\Demo\Reports\SampleComponents\Parameter.cls`, and `<install_root>\Demo\Reports\SampleComponents\ParameterField.cls`.

## Inserting Parameter Fields in a Report

Parameter fields can be inserted in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010063261-Working-with-Components-in-Reports-#Relationship).

To insert a parameter field into a report, select the required parameter from the Data panel, then drag it to the destination. If the given parameters are not what your want, select the **<New Parameter...>** item to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog) as required. For a business view based report, you can create [local parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param) to use in the report specifically.

For a page report created using a query resource, you can also use dialog to insert a parameter field into it as follows:

1. Position the mouse pointer at the destination where you want to insert the parameter and select **Insert** > **Parameter** or **Home** >
   **Insert** > **Parameter.**

   The [Insert Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010031442-Insert-Fields-Dialog) dialog appears.

   ![Insert Field dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901205911/instfld.gif)
2. Select the required parameter from the Parameters node, then specify its layout in the Insert Layout box.
3. Select the **Insert** button to insert the parameter into the destination.

**Note:** If you insert a parameter into the detail panel of a banded object or table, the name of the parameter will automatically be inserted as a label into the corresponding header panel. Otherwise the parameter and its name label will be placed in the same panel. If you do not want to insert the name label automatically, you can uncheck Insert field name label with field in the Options dialog (**File** > **Options** > **Component** > **Insert field name label with field**).

## Adding Conditional Formats to Parameter Fields

You can add conditional formats to parameter fields in a report, then when a specified condition is fulfilled, the format defined on the condition will be applied to the field values automatically. This is very useful to highlight values that might need to be acted on by end users.

To add conditional format to a parameter field, right-click it and select **Conditional Formatting**  from the shortcut menu, then take the same procedure as described in [Adding Conditional Formats to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500010063761-DBFields#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063761-DBFields) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029262-Summary-Fields-)
