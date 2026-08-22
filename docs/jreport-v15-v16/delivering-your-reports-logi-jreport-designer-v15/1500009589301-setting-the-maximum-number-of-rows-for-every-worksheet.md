---
title: "Setting the Maximum Number of Rows for Every Worksheet"
id: 1500009589301
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589301-Setting-the-Maximum-Number-of-Rows-for-Every-Worksheet
updated_at: 2021-07-24T05:54:42Z
---

# Setting the Maximum Number of Rows for Every Worksheet

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589261-Setting-the-Excel-Buffer-Size)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568042-Setting-the-Excel-Column-Width)

# Setting the Maximum Number of Rows for Every Worksheet

You can control the maximum number of rows in every worksheet in the exported Excel file. To do this:

1. Select the node that represents the report in the Report Inspector.
2. In the Properties sheet, set the Rows per Sheet property as required.
3. Select **File** > **Export**  > **To****Excel**.
4. In the Export to Excel dialog, set the options as required.
5. Select **OK** to start exporting.

**Notes:**

* For the Excel version Excel 97-2003 Workbook (\*.xls), the value ranges from 0 to 65000. For the Excel version Excel Workbook (\*.xlsx), the value ranges from 0 to 1048000. If you set the value of the Rows per Sheet property beyond 65000 and choose the Excel version Excel 97-2003 Workbook (\*.xls) in the Export to Excel dialog, 65000 will be used as the maximum number of rows in every worksheet.
* When exporting a report to Excel, rows in the same page of the report cannot be separated and exported to different worksheets, thus the number of rows that is exported to a worksheet may be greater than the maximum number of rows that you set for the property Rows per Sheet. For example, if you set the value of Rows per Sheet to 100, all the contents of the first page will be exported to the first worksheet. After that, the rows of the first worksheet will be tested automatically by Logi JReport Designer. If the number of rows is less than 100, the next page will still be exported to the first worksheet, even if the number of rows in the first page and the next page is greater than 100; If the number of rows in the first page is equal to or more than 100, a new worksheet will be generated and the second page will be exported to the new worksheet.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589261-Setting-the-Excel-Buffer-Size)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568042-Setting-the-Excel-Column-Width)
