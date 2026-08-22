---
title: "Search Dialog Box Properties"
id: 28891539893773
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891539893773-Search-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:50Z
source_host: docs-report.zendesk.com
---
# 
Search Dialog Box Properties 

You can use the Search dialog box to find specific text in a report. This topic describes the properties in the dialog box.

You can find the contents in two places - in the values of a certain field, or in the report contents.

- To find a certain field value, select the field from the Select Field list, select a range in the Value Range list, and then select the value from the Value list.

- To find text in the report contents, select Search in Whole Report, and then type the search content in the Value box.

Select Field

Select the field among whose values you want to find the text. Server disables this property when you select Search in Whole Report.

Value Range

Select the range of the values so that you can select a required value quickly from the Value field. Server disables this property when you select Search in Whole Report.

 If ALL is the Value Range, the only item in the Value list is ALL, and you cannot change the value. In this case, when you submit the search, Report searches all the values of the selected field.

Value

Specify the text you want to find. You can select a value from the list when you do not select Search in Whole Report.

Search in Whole Report

Select if you want to find text in the report contents. Then, Server disables the Select Field and Value Range properties.

Match Case

Select to search for text that meets the case of the typed text. 

Find Whole Word

Select to search for text that looks the same as the typed text.

Highlight All

Select to highlight all matched text. 

Direction

Specify the searching direction.

- 
Up
    Select to search from the last found string to the beginning of the report.

- 
Down
 Select to search from the last found string to the end of the report.

Search

Select to find the next match of the specified text.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
