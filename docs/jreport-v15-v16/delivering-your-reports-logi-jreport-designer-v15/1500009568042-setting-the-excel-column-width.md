---
title: "Setting the Excel Column Width"
id: 1500009568042
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568042-Setting-the-Excel-Column-Width
updated_at: 2021-07-24T05:54:41Z
---

# Setting the Excel Column Width

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589301-Setting-the-Maximum-Number-of-Rows-for-Every-Worksheet)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589341-Realigning-Objects-for-a-Better-Appearance-in-the-Exported-Excel-File)

# Setting the Excel Column Width

You can set the width of each column for the exported Excel file in Logi JReport Designer. To do this:

1. Select the node that represents the report in the Report Inspector.
2. In the Properties sheet, set the Column Width List property as required.

   Type the width for the columns in turn, using a semicolon (;) to separate each value. If you don't want to specify the width for a certain column, omit the value. Logi JReport will then use the default value (8) for the column.

   For example, the value list 12;15;;20 makes the first column width 12, the second 15, the third 8, which is the default value, and the fourth 20.
3. Select **File** > **Export**  > **To****Excel**.
4. In the Export to Excel dialog, select **Column Format**.
5. Set the other options as required.
6. Select **OK** to start exporting.

**Notes:**

* The Column Width List property takes effect only when the report's Columned property is set to true and the Column Format option in the Export to Excel dialog is selected.
* If a report contains a subreport, the Column Width List property for the subreport is disabled when exporting the report to Excel.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589301-Setting-the-Maximum-Number-of-Rows-for-Every-Worksheet)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589341-Realigning-Objects-for-a-Better-Appearance-in-the-Exported-Excel-File)
