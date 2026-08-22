---
title: "Working with Summary Fields"
id: 1500010094901
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields
updated_at: 2021-07-23T19:14:49Z
---

# Working with Summary Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057382-Working-with-Parameter-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094741-Working-with-Formula-Fields)

# Working with Summary Fields

A [summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries) generates a count, average, sum, standard deviation, or other transformation of a set of data values. A summary applies to a defined group of data or to the entire dataset. This topic introduces how you can insert summary fields in a report and add conditional formats to the summary fields.

For the summary fields in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports) if you want.

This topic contains the following sections:

* [Inserting Summary Fields in a Report](#Insert)
* [Adding Conditional Formats to Summary Fields](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the summary field example, open `<install_root>\Demo\Reports\SampleComponents\UsingSummaries.cls`.

## Inserting Summary Fields in a Report

You can insert summary fields in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship).

* **For a business view-based report**  
  Select the aggregation in the **Data** panel and drag it to the destination. Create [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg) if the predefined aggregations in the specified business view cannot meet your requirement.
* **For a query-based report**   
  Select the summary from the **Summaries** node in the Data panel, then drag it to the destination. If the given summaries are not what you want, select the **<Add Summary...>** item to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries) as required. You can also create a summary by [applying aggregation on a DBField](https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields#Add).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* When you insert a dynamic summary field into a report and there is no corresponding group level to match settings of the dynamic summary, Designer prompts an error message.
* You can insert dynamic summary fields into the header/footer/detail panel and all group panels in both banded objects and tables. However, if you are using a static summary, you can only insert it at the group level specified.
* If you want to insert a summary field defined with a special function into a table or banded object, there must be [a group with the same special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Function) in the table or banded object.
* When you insert summary fields to a table or banded object, if the table or banded object is in another banded object and it inherits its parent's dataset, the summaries should take Up group level if they are dynamic summaries.
* If you insert a summary into the detail panel of a table or banded object, Designer automatically inserts its name as a label into the corresponding header panel; otherwise, Designer places the summary and its name label in the same panel. If you do not want Designer to insert the name label automatically, you can clear **Insert field name label with field** in the Options dialog box (File > Options > Component > Insert field name label with field).

## Adding Conditional Formats to Summary Fields

You can add conditional formats to summary fields in a report, then when a specified condition is fulfilled, the format defined on the condition will be applied to the field values automatically. This is very useful to highlight values that the report users may need to act on at runtime.

To add conditional format to a summary field, right-click it and select **Conditional Formatting** from the shortcut menu, then take the same procedure as described in [Adding Conditional Formats to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields#Format).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057382-Working-with-Parameter-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094741-Working-with-Formula-Fields)
