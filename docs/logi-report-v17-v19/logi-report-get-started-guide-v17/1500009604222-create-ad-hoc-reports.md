---
title: "Create Ad Hoc Reports"
id: 1500009604222
section: "Logi Report Get Started Guide v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009604222-Create-Ad-Hoc-Reports
updated_at: 2021-07-24T16:05:32Z
---

# Create Ad Hoc Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404916886423/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009627501-Create-Dashboards) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404904596631/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604462-Start-a-Visual-Analysis-Session)

# Create Ad Hoc Reports

There are two types of ad hoc reports in Logi Report, Web Report and Page Report. Both are created from a business view in a catalog. Business views have the capability of providing multiple hierarchies allowing for automatic drill down and drill up for detailed analysis and slicing and dicing data which is especially powerful using a crosstab component.

To create ad hoc reports, you should have [logged onto the Logi Report Server console](https://devnet.logianalytics.com/hc/en-us/articles/1500009627601-Test-Server-Installation), and disabled the Pop-up Blocker on your web browser. Then:

**To create a web report:**

1. In the Logi Report Server Start Page, select **Web Report** in the Create category.

   Web Report Studio is then displayed in a new tab, prompting you to select data for the new report.

   ![Select Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404916888599/adhocrpt_slctcat.gif)
2. In the Select Catalog dialog, select the catalog published to the server resource tree, which contains the data you want to use for the report. select **OK**.
3. In the Select Data Source dialog, select the required data source in the specified catalog from the Data Source drop-down list, the business view in the selected data source in the Resources box, then in the right box select the data fields you want to display in the report.

   ![Select Data for Report](https://devnet.logianalytics.com/hc/article_attachments/4404904603671/adhocrpt_slctdtsc.gif)
4. Select **OK**. A table report is generated.

   ![Web Report Table](https://devnet.logianalytics.com/hc/article_attachments/4404916888855/adhocrpt_tbl.gif)

**To create a page report:**

1. In the Logi Report Server Start Page, select **Page Report**  in the Create category.
2. In the displayed page, select the folder that contains the catalog you want to use to create the page report and then the catalog. select **OK**.
3. The New Page Report dialog appears for you to create a page report with the first report tab in it.

   ![New Page Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904604055/adhocrpt_page.gif)
4. Specify the title of the report tab in the Report Title text box.
5. In the Choose Report Layout box, select the required layout with which you want to create the report tab.
6. Select **OK** to create the report.
   * If Blank Report is selected as the layout, a report which is blank is created. You can then use the Toolbox and the Resource View panels to add objects and view elements to the report.
   * If you select the layout as Banded, Table, Chart, or Crosstab, the corresponding report wizard is then displayed. Specify the data to display according to your requirements.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404916886423/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009627501-Create-Dashboards) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404904596631/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604462-Start-a-Visual-Analysis-Session)
