---
title: "Page Setup Dialog Box"
id: 1500010060082
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box
updated_at: 2021-07-23T19:15:49Z
---

# Page Setup Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060062-Page-Report-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060162-Parameter-Dialog-Box)

# Page Setup Dialog Box

You can use the Page Setup dialog box to specify the [general](https://devnet.logianalytics.com/hc/en-us/articles/1500010101321-Designing-the-Report-Pages#Setting) and [export](https://devnet.logianalytics.com/hc/en-us/articles/1500010060902-Exporting-Report-Result#Page) page properties for the current report tab in a page report, or for the current web report or library component. This topic describes the options in the dialog box.

Designer displays the Page Setup dialog box when you select File > Page Setup, or the Page Setup button in the Style screen of the page report wizard.

The dialog box contains the following tabs:

* [General Tab](#General)
* [Export Tab](#Export)

You see these buttons in both tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab

Use this tab to specify the general properties of the page, which you can also define via the [Page Panel object](https://devnet.logianalytics.com/hc/en-us/articles/1500010062242-Page-Panel-Properties) in the Report Inspector.

![Page Setup - General](https://devnet.logianalytics.com/hc/article_attachments/4404848402327/pgstup_gnrl.gif)

**Paper**

You can specify the page size in this box.

* **Type**  
  Select the paper type. Select the desired size from the drop-down list, or select Custom Size to define the paper width and height by yourself.
* **Width**  
  Specify the width of the page.
  + **Auto Fit**  
    Select to dynamically calculate the page width according to the width of the contents within the page. The default behavior for exporting a new report (the option is unselected) is to enable content pagination which greatly improves the performance of the exporting process, especially for a huge report.
* **Height**  
   Specify the height of the page.
  + **Auto Fit**  
    Select to dynamically calculate the page height according to the height of the contents within the page. The default behavior for exporting a new report (the option is unselected) is to enable content pagination which greatly improves the performance of the exporting process, especially for a huge report.

**Orientation**

You can specify the page orientation in this box.

* **Portrait**  
  Select to display the page as portrait.
* **Landscape**  
  Select to display the page as landscape.

**Margin**

You can specify the distance of the report data to the top, bottom, left, and right boundaries of the page in this box.

* **Top**  
  Specify the top margin of the page.
* **Bottom**  
  Specify the bottom margin of the page.
* **Left**  
  Specify the left margin of the page.
* **Right**  
  Specify the right margin of the page.

## Export Tab

Use this tab to specify the page properties for the outputs of the report tab/web report/library component. The page properties that you specify for any export format will also be applied when end users advanced run and schedule to run the report in this format on Server.

![Page Setup - Export](https://devnet.logianalytics.com/hc/article_attachments/4404848476439/pgstup_export.gif)

**Export To**

Select the export format to customize the page properties of its output.

**Auto**

If you select the option, Designer applies the page properties that you define in the [General](#General) tab of this dialog box to the output of the selected export format. Clear the option to customize the page properties for the selected format.

When you clear the Auto option for an export format and select OK in the dialog box, Designer adds a corresponding [Export Page Setting object](https://devnet.logianalytics.com/hc/en-us/articles/1500010100681-Export-Page-Setting-Object-Properties) to the report structure tree in the Report Inspector. You can edit the export page properties there too. When you select the Auto option for this export format and select OK in the dialog box again, Designer automatically removes its Export Page Setting object from the report structure tree.

**Paper**

You can specify the [paper size](#Paper) for the output of the selected format in this box.

**Orientation**

Select the page orientation for the output of the selected format: Portrait (vertically) or Landscape (horizontally).

**Margin**

You can specify the distance of the report data to the top, bottom, left, and right boundaries of the page in the output of the selected format in this box.

* **Top**  
  Specify the top margin of the page.
* **Bottom**  
  Specify the bottom margin of the page.
* **Left**  
  Specify the left margin of the page.
* **Right**  
  Specify the right margin of the page.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060062-Page-Report-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060162-Parameter-Dialog-Box)
