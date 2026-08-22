---
title: "Working with Summary Fields"
id: 12479958219917
section: "Working with Components in Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479958219917-Working-with-Summary-Fields
updated_at: 2026-02-25T23:50:24Z
source_host: docs-report.zendesk.com
---
# Working with Summary Fields

A summary generates a count, average, sum, standard deviation, or other transformation of a set of data values. A summary applies to a defined group of data or to the entire dataset. This topic introduces how you can insert summary fields in a report and add conditional formatting to the summary fields.

For the summary fields in a report, you can use them as the trigger object of links, and change their display types if you want.

This topic contains the following sections:

- Inserting Summary Fields in a Report

- Adding Conditional Formatting to Summary Fields

See an example: The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the summary field example, open <install_root>\Demo\Reports\SampleComponents\UsingSummaries.cls.

## 
Inserting Summary Fields in a Report

You can insert summary fields in the report areas listed in Component Placement in Different Report Type.

For a business view-based report

In the Data panel, select the aggregation and drag it to the destination. When the predefined aggregations in the specified business view cannot meet your requirement, you can create dynamic aggregations to use in the report specifically.

For a query-based report

In the Data panel, select a dataset from the dataset drop-down list, then select a summary from the Summaries node and drag it to the destination. When the predefined summaries are not what you want, you can select <Add Summary...> to create a summary. You can also create a summary by applying aggregation on a DBField.

- When you insert a dynamic summary into a report and there is no corresponding group level to match settings of the dynamic summary, Designer prompts an error message.

- You can insert dynamic summaries  into the header/footer/detail panel and all group panels in both banded objects and tables. However, if you are using a static summary, you can only insert it  at the group level specified.

- If you want to insert a summary containing a special function into a table or banded object, there must be a group with the same special function in the table or banded object.

- When you insert summaries to a table or banded object, if the table or banded object is in another banded object and it inherits its parent's dataset, the summaries should apply the Up group level if they are dynamic summaries. 

- If you insert a summary into the detail panel of a table or banded object, Designer automatically inserts its name as a label into the corresponding header panel; otherwise, Designer places the summary and its name label in the same panel. If you do not want Designer to insert the name label automatically,  clear "Insert field name label with field" in the Component category of the Options dialog box.

## 
Adding Conditional Formatting to Summary Fields

You can add conditional formatting to summary fields in a report, so the field values that meet a specified condition can automatically apply the formatting you define for the condition. This is very useful to highlight values that users may need to act on at runtime.

To apply conditional formatting to a summary field, right-click it and select Conditional Formatting from the shortcut menu, then take the same procedure as described in Adding Conditional Formatting to DBFields.
