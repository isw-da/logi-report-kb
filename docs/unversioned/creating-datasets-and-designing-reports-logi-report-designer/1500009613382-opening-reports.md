---
title: "Opening Reports"
id: 1500009613382
section: "Creating Datasets and Designing Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009613382-Opening-Reports
updated_at: 2021-07-24T16:03:21Z
---

# Opening Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636221-Saving-Reports)

# Opening Reports

This topic demonstrates how to open a report.

1. Select **Home**/**File** > **Open** to display the [Open Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009632821-Open-Report-Dialog) dialog.

   ![Open Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904180503/opnrpt.gif)
2. Select **Browse** to select the catalog in which the reports you want to open are saved.
3. In the Reports tab, select the type of the reports from the Report of Type drop-down list.
4. All the reports of the specified type in the specified catalog are then displayed in the report box. Select the desired reports.
5. If you want to open reports that you have opened recently, switch to the **Recent** tab, and then select the reports to open.
6. Select **Open** to open the specified reports. The last selected report in the report box will be the active report.

If you just want to access some recently open reports, you can also select **File** > **Open Recent** and select the reports one by one from the submenu.

## Opening Self-contained Page Reports

When a page report you have selected in the Open Report dialog is a self-contained page report, after you select OK in the Open Report dialog, the Open As dialog will appear, prompting you to specify the way in which you want the page report to be opened.

![Open As dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911611031/rpt_open.gif)

* **Open a self-contained page report in current catalog**  
   Specifies to open the selected self-contained page report in the current catalog and make it work under the current catalog.

  Logi Report Designer will compare the resources in the catalog of the self-contained page report with the current catalog according to the checking level (whether the Check all data match is selected). If conflicts exist between the two catalogs, the page report cannot be opened.
* **Open a self-contained page report directly**  
   Specifies to open the selected self-contained page report directly to make it work under a new catalog.
* **Open a self-contained page report in another catalog**  
   Specifies to open the selected self-contained page report in another catalog and make it work under that catalog.

  If this option is selected, you will be prompted to open another existing catalog for the self-contained page report. Logi Report Designer will then compare the resources in the catalog of the self-contained page report with the newly selected catalog according to the checking level (whether the Check all data match is selected). If conflicts exist between the two catalogs, the page report cannot be opened.
* **Check all data match**This checkbox is enabled when Open a self-contained page report in current catalog or Open a self-contained page report in another catalog is selected. It is used to specify the checking level between two catalogs.
  + If the option is selected, all the differences between the two catalogs will be selected by Logi Report Designer.
  + If unselected, only the differences that can cause the report engine to fail when running the page report will be checked by Logi Report Designer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636221-Saving-Reports)
