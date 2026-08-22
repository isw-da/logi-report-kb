---
title: "Working with Summary Fields"
id: 4405661398551
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661398551-Working-with-Summary-Fields
updated_at: 2022-01-27T20:34:33Z
---

# Working with Summary Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664399255-Working-with-Parameter-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661380119-Working-with-Formula-Fields)

# Working with Summary Fields

A [summary](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries) generates a count, average, sum, standard deviation, or other transformation of a set of data values. A summary applies to a defined group of data or to the entire dataset. This topic introduces how you can insert summary fields in a report and add conditional formatting to the summary fields.

For the summary fields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/4405661930647-Changing-the-Display-Type-of-Objects-in-Reports) if you want.

This topic contains the following sections:

* [Inserting Summary Fields in a Report](#Insert)
* [Adding Conditional Formatting to Summary Fields](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the summary field example, open `<install_root>\Demo\Reports\SampleComponents\UsingSummaries.cls`.

## Inserting Summary Fields in a Report

You can insert summary fields in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship).

**For a business view-based report**

In the **Data** panel, select the aggregation and drag it to the destination. Create [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/4405661937559-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg) if the predefined aggregations in the specified business view cannot meet your requirement.

**For a query-based report**

In the **Data** panel, select the summary from the **Summaries** node, then drag it to the destination. If the predefined summaries are not what you want, select the **<Add Summary...>** item to [create one](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries) as required. You can also create a summary by [applying aggregation on a DBField](https://devnet.logianalytics.com/hc/en-us/articles/4405664395799-Working-with-DBFields#Add).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* When you insert a dynamic summary field into a report and there is no corresponding group level to match settings of the dynamic summary, Designer prompts an error message.
* You can insert dynamic summary fields into the header/footer/detail panel and all group panels in both banded objects and tables. However, if you are using a static summary, you can only insert it at the group level specified.
* If you want to insert a summary field defined with a special function into a table or banded object, there must be [a group with the same special function](https://devnet.logianalytics.com/hc/en-us/articles/4405664404503-Grouping-the-Data-in-Tables#Function) in the table or banded object.
* When you insert summary fields to a table or banded object, if the table or banded object is in another banded object and it inherits its parent's dataset, the summaries should take Up group level if they are dynamic summaries.
* If you insert a summary into the detail panel of a table or banded object, Designer automatically inserts its name as a label into the corresponding header panel; otherwise, Designer places the summary and its name label in the same panel. If you do not want Designer to insert the name label automatically, clear "Insert field name label with field" in the Component category of the Options dialog box.

## Adding Conditional Formatting to Summary Fields

You can add conditional formatting to summary fields in a report, so the field values that meet a specified condition can automatically apply the formatting you define for the condition. This is very useful to highlight values that users may need to act on at runtime.

To apply conditional formatting to a summary field, right-click it and select **Conditional Formatting** from the shortcut menu, then take the same procedure as described in [Adding Conditional Formatting to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/4405664395799-Working-with-DBFields#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664399255-Working-with-Parameter-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661380119-Working-with-Formula-Fields)
