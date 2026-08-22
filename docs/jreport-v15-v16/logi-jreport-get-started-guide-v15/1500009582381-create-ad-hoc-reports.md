---
title: "Create Ad Hoc Reports"
id: 1500009582381
section: "Logi JReport Get Started Guide v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582381-Create-Ad-Hoc-Reports
updated_at: 2023-06-30T11:57:14Z
---

# Create Ad Hoc Reports

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582521-View-Sample-Reports)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582501-Start-a-Visual-Analysis-Session)

# Create Ad Hoc Reports

There are two types of ad hoc reports in Logi JReport, Web Report and Page Report. Both are created from a business view in a catalog. Business views have the capability of providing multiple hierarchies allowing for automatic drill down and drill up for detailed analysis and slicing and dicing data which is especially powerful using a crosstab component.

To create ad hoc reports, you should have [logged onto the Logi JReport Server user console](https://devnet.logianalytics.com/hc/en-us/articles/1500009562162-Test-Server-Installation), and disabled the Pop-up Blocker on your web browser. Then:

**To create a web report:**

1. On the Logi JReport Server Start Page, select **Web Reports** in the Create category.
2. In the Select Data Source dialog, select data fields from a business view to display in the report.

   ![Select Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404894018199/adhocrpt_slctdtsc.gif)
3. Select **OK**. A table report is generated.

   ![Web Report Table](https://devnet.logianalytics.com/hc/article_attachments/4404889436439/adhocrpt_tbl.gif)

**To create a page report:**

1. On the Logi JReport Server Start Page, select **Page Report** in the Create category.
2. Select the folder that contains the catalog you want to use to create the page report and then the catalog. Select **OK**.
3. The New Page Report dialog appears for you to create a page report with the first report tab in it.

   ![New Page Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889436695/adhocrpt_page.gif)
4. Specify the title of the report tab in the Report Title text box.
5. In the Choose Report Layout box, select the required layout with which you want to create the report tab.
6. Select **OK** to create the report.
   * If Blank Report is selected as the layout, a report which is blank will be created. You can then use the Toolbox and the Resource View panels to add objects and view elements to the report.
   * If you select the layout as Banded, Table, Chart, or Crosstab, the corresponding report wizard will then be displayed. Specify the settings according to your requirements.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582521-View-Sample-Reports)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582501-Start-a-Visual-Analysis-Session)
