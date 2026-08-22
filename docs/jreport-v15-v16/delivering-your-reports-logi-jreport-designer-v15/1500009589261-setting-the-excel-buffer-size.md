---
title: "Setting the Excel Buffer Size"
id: 1500009589261
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589261-Setting-the-Excel-Buffer-Size
updated_at: 2021-07-24T05:54:41Z
---

# Setting the Excel Buffer Size

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568022-Exporting-to-Excel)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589301-Setting-the-Maximum-Number-of-Rows-for-Every-Worksheet)

# Setting the Excel Buffer Size

You can store the report result in Excel buffer sheets when exporting to Excel format. To do this:

1. Select the node that represents the report in the Report Inspector.
2. In the Properties sheet, set the Excel Buffer Size property as required.

   The default size is 1, which indicates that 1 sheet of the report result will be allocated to the result buffer, while the other sheets will be stored onto disk. If you have enough memory, to improve performance, you can increase the Excel buffer size to store more sheets of the excel format report result.
3. Select **File** > **Export**  > **To Excel**.
4. In the Export to Excel dialog, make sure Data Format is not checked and set the other options as required.
5. Select **OK** to start exporting.

**Note:** The Excel Buffer Size property takes effect only when the Data Format option in the Export to Excel dialog is not selected.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568022-Exporting-to-Excel)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589301-Setting-the-Maximum-Number-of-Rows-for-Every-Worksheet)
