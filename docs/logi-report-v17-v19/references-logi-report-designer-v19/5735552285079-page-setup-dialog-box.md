---
title: "Page Setup Dialog Box"
id: 5735552285079
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box
updated_at: 2022-11-02T07:53:18Z
---

# Page Setup Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735515048599-Page-Report-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735524288151-Parameter-Dialog-Box)

# Page Setup Dialog Box

You can use the Page Setup dialog box to specify the [general](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Setting) and [export](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports#Page) page settings for the current report tab in a page report, or for the current web report or library component. This topic describes the options in the dialog box.

Designer displays the Page Setup dialog box when you navigate to File > Page Setup, or select Page Setup in the Style screen of the component wizard.

This dialog box contains the following tabs:

* [General Tab](#General)
* [Export Tab](#Export)

Designer displays these buttons in all the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab

Use this tab to specify general settings of the page. You can [use constant level formulas to control](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties) some page options for a page report tab, if you have [bound a data resource to its report body](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports).

![Page Setup dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9898422989079/pgstup_gnrl19.2.gif)

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898423002391/___newv19.2.png "New for version 19.2.")**Page Layout**

* For a page report tab or web report, Designer selects this option by default so the report applies pagination mode in Designer view, and in Page Report Studio as well, for a page report tab. Clear it if you want to apply continuous page mode to the report, meaning, display the report in a single page.
* For a library component, you cannot specify its page layout.

**Paper**

You can specify the page size in this box.

* **Type**  
  Select the paper type. Select the size you want from the drop-down list, or select **Custom Size** to define the paper width and height by yourself.
* **Width**  
  Specify the width of the page, in inches.
  + **Auto Fit**  
    Select to dynamically calculate the page width according to the width of the content within the page.
* **Height**  
   Specify the height of the page, in inches.
  + **Auto Fit**  
    Select to dynamically calculate the page height according to the height of the content within the page.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) After you select a paper type and then edit either Width or Height, Designer automatically changes the paper type to Custom Size in the Type drop-down list.

**Orientation**

You can specify the page orientation in this box. Designer disables the Orientation option if you select a formula to control either Width or Height.

* **Portrait**  
  Select to display the page vertically.
* **Landscape**  
  Select to display the page horizontally.

**Margin**

You can specify the distance of the report data to the top, bottom, left, and right edge of the page in this box.

* **Top**  
  Specify the top margin of the page.
* **Bottom**  
  Specify the bottom margin of the page.
* **Left**  
  Specify the left margin of the page.
* **Right**  
  Specify the right margin of the page.

## Export Tab

Use this tab to specify page settings for the output of the report tab, web report, or library component.

![Page Setup dialog box - Export tab](https://devnet.logianalytics.com/hc/article_attachments/9898460005783/pgstup_expt19.2.gif)

**Export To**

Select the export format to customize page settings of its output.

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898423002391/___newv19.2.png "New for version 19.2.")**Page Layout**

* For a page report tab or web report, Designer selects this option by default so the output of the selected format applies pagination mode. Clear it if you want to apply continuous page mode to the output, meaning, display the output in a single page.
* For a library component, you cannot specify the page layout of its output.

**Auto**

By default, Designer automatically applies the page settings that you define in the [General](#General) tab to the output of the selected format. Clear this option if you want to apply different page settings to the output.

When you clear the Auto option for an export format and select OK in the dialog box, Designer adds a corresponding [Export Page Setting object](https://devnet.logianalytics.com/hc/en-us/articles/5735533514391-Export-Page-Setting-Object-Properties) to the report structure tree in the Report Inspector. You can edit the export page properties there too. When you select the Auto option for this export format and select OK in the dialog box again, Designer automatically removes its Export Page Setting object from the report structure tree.

**Paper**

You can specify the paper size for the output of the selected format in this box.

* **Type**  
  Select the paper type. Select the size you want from the drop-down list, or select Custom Size to define the paper width and height.
* **Width**  
  Specify the width of the page, in inches.
  + **Auto Fit**  
    Select to dynamically calculate the page width according to the width of the content within the page. The default behavior for exporting a report is to enable content pagination (the option is cleared), which greatly improves the performance of the exporting process, especially for a huge report.
* **Height**  
  Specify the height of the page, in inches.
  + **Auto Fit**  
    Select to dynamically calculate the page height according to the height of the content within the page. The default behavior for exporting a report is to enable content pagination (the option is cleared), which greatly improves the performance of the exporting process, especially for a huge report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) After you select a paper type and then edit either Width or Height, Designer changes the paper type to Custom Size in the Type drop-down list automatically.

**Orientation**

Select the page orientation for the output of the specified format: Portrait (vertically) or Landscape (horizontally).

**Margin**

You can specify the distance of the report data to the top, bottom, left, and right edge of the page for the output of the selected format in this box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735515048599-Page-Report-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735524288151-Parameter-Dialog-Box)
