---
title: "Specifying Subreport Location in the Exported Excel File"
id: 1500009589361
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589361-Specifying-Subreport-Location-in-the-Exported-Excel-File
updated_at: 2022-06-13T11:26:47Z
---

# Specifying Subreport Location in the Exported Excel File

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589341-Realigning-Objects-for-a-Better-Appearance-in-the-Exported-Excel-File)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589321-Controlling-Banded-Object-Panels-in-the-Exported-Excel-File)

# Specifying Subreport Location in the Exported Excel File

If a report contains a subreport, you can specify where the subreport will be put in the exported Excel file in the following way:

1. Open the report you want to export, which contains a subreport.
2. Select the node that represents the subreport in the Report Inspector.
3. In the Properties sheet, set the On New Sheet property as required.
   * If you want to put the subreport in the same worksheet together with the primary report, set the value to false.
   * If you want to put the subreport in a new worksheet in the exported Excel file, set the property value to true, then enter a name for the new worksheet in the Sheet Name property's value cell. Make sure the name you specify here isn't used by any other worksheets.
4. Select **File** > **Export**  > **To** **Excel**.
5. In the Export to Excel dialog, make sure Report Format is selected.
6. Set the other options as required.
7. Select **OK** to start exporting.

   If you set On New Sheet to true, after exporting the report successfully, you will find that the primary report is exported into the first worksheet, and there are some links on it. Select the links to go to the subreport in the second worksheet of the Excel file.

**Note:** If the subreport are cut into several pages, that is to say you have defined some [page settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page) on the subreport, the links in the primary report will be subreport1\_0, subreport1\_1, subreport1\_2 and so on. You can select the link to see the corresponding part you want.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589341-Realigning-Objects-for-a-Better-Appearance-in-the-Exported-Excel-File)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589321-Controlling-Banded-Object-Panels-in-the-Exported-Excel-File)
