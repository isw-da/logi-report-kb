---
title: "Improving the Performance of Exporting to Excel"
id: 1500009589281
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589281-Improving-the-Performance-of-Exporting-to-Excel
updated_at: 2021-07-24T05:54:42Z
---

# Improving the Performance of Exporting to Excel

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589321-Controlling-Banded-Object-Panels-in-the-Exported-Excel-File)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568142-Exporting-to-Text)

# Improving the Performance of Exporting to Excel

Normally, when a report is being exported to an Excel file, the coordinates of the report objects are calculated by Logi JReport Engine, and can require a great deal of processing time. However, you can arrange the coordinates of the report objects manually at design time, so that the extra position calculating time can be saved. To do this:

1. Select the node that represents the report in the Report Inspector.
2. In the Properties sheet, set the Columned property for the report to true.
3. Set the values of Column Index and Row Index for each object to define the position of the object in the exported Excel file.
4. Select **File** > **Export**  > **To****Excel**.
5. In the Export to Excel dialog, select **Column Format**.
6. Set the other options as required.
7. Select **OK** to start exporting.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589321-Controlling-Banded-Object-Panels-in-the-Exported-Excel-File)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568142-Exporting-to-Text)
