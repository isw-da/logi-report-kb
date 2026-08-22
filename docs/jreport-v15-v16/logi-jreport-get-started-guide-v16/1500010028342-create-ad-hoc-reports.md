---
title: "Create Ad Hoc Reports"
id: 1500010028342
section: "Logi JReport Get Started Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028342-Create-Ad-Hoc-Reports
updated_at: 2021-07-24T10:39:37Z
---

# Create Ad Hoc Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062901-Create-Dashboards) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062961-Start-a-Visual-Analysis-Session)

# Create Ad Hoc Reports

There are two types of ad hoc reports in Logi JReport, Web Report and Page Report. Both are created from a business view in a catalog. Business views have the capability of providing multiple hierarchies allowing for automatic drill down and drill up for detailed analysis and slicing and dicing data which is especially powerful using a crosstab component.

To create ad hoc reports, you should have [logged onto the Logi JReport Server console](https://devnet.logianalytics.com/hc/en-us/articles/1500010028382-Test-Server-Installation), and disabled the Pop-up Blocker on your web browser. Then:

**To create a web report:**

1. In the Logi JReport Server Start Page, select **Web Report** in the Create category.

   Web Report Studio is then displayed in a new tab, prompting you to select data for the new report.

   ![Select Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404909298583/adhocrpt_slctcat.gif)
2. In the Select Catalog dialog, select the catalog published to the server resource tree, which contains the data you want to use for the report. select **OK**.
3. In the Select Data Source dialog, select the required data source in the specified catalog from the Data Source drop-down list, the business view in the selected data source in the Resources box, then check the checkboxes ahead of the data fields you want to display in the report.

   ![Select Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909298839/adhocrpt_slctdtsc.gif)
4. Select **OK**. A table report is generated.

   ![Web Report Table](https://devnet.logianalytics.com/hc/article_attachments/4404901354007/adhocrpt_tbl.gif)

**To create a page report:**

1. In the Logi JReport Server Start Page, select **Page Report**  in the Create category.
2. In the displayed page, select the folder that contains the catalog you want to use to create the page report and then the catalog. select **OK**.
3. The New Page Report dialog appears for you to create a page report with the first report tab in it.

   ![New Page Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909299223/adhocrpt_page.gif)
4. Specify the title of the report tab in the Report Title text box.
5. In the Choose Report Layout box, select the required layout with which you want to create the report tab.
6. Select **OK** to create the report.
   * If Blank Report is selected as the layout, a report which is blank will be created. You can then use the Toolbox and the Resource View panels to add objects and view elements to the report.
   * If you select the layout as Banded, Table, Chart, or Crosstab, the corresponding report wizard will then be displayed. Specify the settings according to your requirements.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062901-Create-Dashboards) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062961-Start-a-Visual-Analysis-Session)
