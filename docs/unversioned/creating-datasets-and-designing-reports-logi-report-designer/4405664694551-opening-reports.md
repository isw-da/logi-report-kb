---
title: "Opening Reports"
id: 4405664694551
section: "Creating Datasets and Designing Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664694551-Opening-Reports
updated_at: 2022-01-27T20:34:55Z
---

# Opening Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661938967-Saving-Reports)

# Opening Reports

This topic describes how you can open a report in Designer.

1. Navigate to **Home**/**File** > **Open**. Designer displays the [Open Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661666327-Open-Report-Dialog-Box).

   ![Open Report dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556098327/opnrpt.gif)
2. Select **Browse** to select the catalog in which you have saved the reports you want to open.
3. In the **Reports** tab, select the type of the reports from the **Report of Type** drop-down list.
4. Designer displays all reports of the type in the specified catalog in the report box. Select the reports you want to open.
5. If you want to open reports that you have opened recently, switch to the **Recent** tab, and then select the reports to open.
6. Select **Open** to open the reports. Designer displays the last selected report in the report box as the active report.

If you just want to access some recently open reports, you can also navigate to **File** > **Open Recent** and select the reports one by one from the submenu.

## Opening Self-contained Page Reports

When a page report you select in the Open Report dialog box is a self-contained page report, after you select OK in the Open Report dialog box, Designer displays the Open As dialog box, prompting you to specify the way in which you want to open the page report.

![Open As dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556098583/rpt_open.gif)

* **Open a self-contained page report in current catalog**  
  Select to open the specified self-contained page report in the current catalog and make it work under the current catalog.

  Designer compares the resources in the catalog of the self-contained page report with the current catalog according to the checking level (whether you select "Check all data match"). If conflicts exist between the two catalogs, you cannot open the page report.
* **Open a self-contained page report directly**  
  Select to open the specified self-contained page report directly to make it work under a new catalog.
* **Open a self-contained page report in another catalog**  
  Select to open the specified self-contained page report in another catalog and make it work under that catalog.

  If you select this option, Designer prompts you to open another existing catalog for the self-contained page report. Designer then compares the resources in the catalog of the self-contained page report with the newly selected catalog according to the checking level (whether you select "Check all data match"). If conflicts exist between the two catalogs, you cannot open the page report.
* **Check all data match**  
  Designer enables this checkbox when you select "Open a self-contained page report in current catalog" or "Open a self-contained page report in another catalog". You can use it to specify the checking level between two catalogs.
  + If you select the checkbox, Designer checks all the differences between the two catalogs.
  + If you clear the checkbox, Designer only checks the differences that can cause the report engine to fail when running the page report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661938967-Saving-Reports)
