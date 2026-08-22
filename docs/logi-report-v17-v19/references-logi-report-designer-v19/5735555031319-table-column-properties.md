---
title: "Table Column Properties"
id: 5735555031319
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735555031319-Table-Column-Properties
updated_at: 2022-11-02T08:17:31Z
---

# Table Column Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735517614999-Table-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557805335-Table-Detail-Properties)

# Table Column Properties

A table can contain four types of columns: Common Column, Detail Column, Group Column, and Summary Column, and Designer displays the same set of properties for all the columns. This topic describes the properties of a Table Column object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Others | | |
| Auto Fit | Page Report, Web Report, Library Component | Specifies whether to adjust the width of the object according to its content. Data type: Boolean  Note icon When you set this property to "true", Designer adjusts the width of the object only when the Position property of the field/label in this object is "static" or "relative"; if Position of the field/label is "absolute", its Auto Fit property should be "true". |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV output. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format or use the library component at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text output. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML output. Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Reduce Width When Auto Fit | Page Report, Web Report, Library Component | Specifies whether to reduce the width of the object according to its content when you specify to automatically adjust its width (set the object's [Auto Fit](#AutoFit) property to "true") and the actual width of the content is smaller than that of the object. Data type: Boolean |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* If a table contains a merged cell that is across columns and there are absolutely positioned objects in the cell, when you exclude a column which is not the last column for this merged cell from the report output, Logi Report Engine recalculates the X coordinates of those objects that are in the excluded column and tries to display them in the output if space allows. However, this may result in that some objects overlap in their new position in the output.
* Because one cell in Excel can only contain one value, if you exclude a table column from the Excel output, Logi Report Engine is not able to display the value of a data field which is originally in the excluded column in the Excel output if the new position of the field is in a cell that already contains a value, even when the field satisfies the conditions as described in the preceding note.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735517614999-Table-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557805335-Table-Detail-Properties)
