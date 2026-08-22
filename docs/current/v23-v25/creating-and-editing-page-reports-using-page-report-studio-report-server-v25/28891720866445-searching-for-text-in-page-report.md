---
title: "Searching for Text in Page Report"
id: 28891720866445
section: "Creating and Editing Page Reports Using Page Report Studio Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891720866445-Searching-for-Text-in-Page-Report
updated_at: 2026-02-26T02:13:40Z
source_host: docs-report.zendesk.com
---
# 
Searching for Text in Page Report 

You can use the Search dialog box to find text in the values of a certain field or in the whole report content. This topic describes how you can search for text in Page Report.

To show the Search dialog box, select Menu > Edit > Search, select the Search button  on the toolbar, or right-click a field value or label (or object such as text box) and select Search on the shortcut menu.

To find text in the values of a particular field:

- DO NOT select the Search in Whole Report option in the Search dialog box.

- Select a field from the Select Field drop-down list.

- Set the range with which to search for the value from the Value Range drop-down list. 

- Select the field value you want to search for from the Value drop-down list.

- Specify whether to match case, match whole word, and highlight all the matching values, and select the searching direction.

- Select the Search button.

To find text in the report content:

- In the Search dialog box, select Search in Whole Report.

- Type the string you want to search for in the Value box.

- Set the other options such as the searching direction.

- Select the Search button.

- Finding text in the values of a particular field is not supported on crosstabs and charts.

- If you select Highlight All in the Search dialog box, to clear the highlighting in the search result, clear the option and submit the search again, or refresh the report.

- If you have not selected the Search in Whole Report option, you cannot search special fields for strings.

- When you select All in the Value Range drop-down list, the only item in the Value drop-down list is All and you cannot change it. In this case when you submit the search, Page Report Studio searches for all the values of the selected field.
