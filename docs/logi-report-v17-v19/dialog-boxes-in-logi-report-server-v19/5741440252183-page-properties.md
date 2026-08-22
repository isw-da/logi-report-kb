---
title: "Page Properties"
id: 5741440252183
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741440252183-Page-Properties
updated_at: 2022-10-31T17:16:28Z
---

# Page Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741411534871-Order-Select-N-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741425258519-Parameter-Control-Properties)

# Page Properties

You can use the Page Properties dialog box to specify the page properties of a report and its output. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Export Tab Properties](#Export)

You see these elements on both tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Use this tab to specify the general properties of the page.

![Page Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905661644055/pgprpty_gnrl.gif)

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")**Page Layout**

Server selects this option by default, so the report applies [pagination mode](https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report#PageMode) in Page Report Studio. Clear it if you want to apply continuous page mode to the report, meaning, display the report in a single page.

**Page**

Specify the page size properties.

* **Type**  
  Select the page type, or select **Custom Size** and then define the paper width and height by yourself.
* **Width**  
  Specify the width of the page, in inches.
  + **Auto Fit**  
    Select to dynamically calculate the page width according to the content width.
* **Height**  
  Specify the height of the page, in inches.
  + **Auto Fit**  
    Select to dynamically calculate the page height according to the content height.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) After you select a page type and then select **Auto Fit**, Server changes the page type to **Custom Size** automatically.

**Orientation**

Specify the page orientation.

* **Portrait**  
  Select to display the page vertically.
* **Landscape**  
  Select to display the page horizontally.

**Margin**

Specify the distance of the report data to the top, bottom, left, and right edge of the page.

* **Top**  
  Specify the top margin of the page.
* **Bottom**  
  Specify the bottom margin of the page.
* **Left**  
  Specify the left margin of the page.
* **Right**  
  Specify the right margin of the page.

## Export Tab Properties

Use this tab to specify the page properties for the report output. Server also applies the page properties that you set for any export format when you advanced run and schedule to run the report in this format.

![Page Properties dialog box - Export tab](https://devnet.logianalytics.com/hc/article_attachments/9905673597079/pgprpty_export.gif)

**Export To**

Select the export format to customize the page properties of its output.

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")**Page Layout**

Server selects this option by default, so the output of the selected format applies [pagination mode](https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report#PageMode). Clear it if you want to apply continuous page mode to the output, meaning, display the output in a single page.

You can customize the following properties for the selected format when you do not clear **Page Layout**.

**Auto**

Select if you want to apply the page properties that you define on the [General tab](#General) of this dialog box to the output of the selected format. Clear if you want to customize the page properties for the selected format.

**Page**

Specify the page size for the output of the selected format.

* **Type**  
  Select the page type, or select **Custom Size** and then define the paper width and height by yourself.
* **Width**  
  Specify the width of the page, in inches.
  + **Auto Fit**  
     Select to dynamically calculate the page width according to the content width. The default behavior for exporting a report is to enable content pagination (the property is cleared), which greatly improves the performance of the exporting process, especially for a huge report.
* **Height**  
  Specify the height of the page, in inches.
  + **Auto Fit**  
     Select to dynamically calculate the page height according to the content height. The default behavior for exporting a report is to enable content pagination (the property is cleared), which greatly improves the performance of the exporting process, especially for a huge report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) After you select a page type and then select **Auto Fit**, Server changes the page type to **Custom Size** automatically.

**Orientation**

Select the page orientation for the output of the selected format: Portrait (vertically) or Landscape (horizontally).

**Margin**

Specify the distance of the report data to the top, bottom, left, and right edge of the page for the output of the selected format, in inches.

* **Top**  
  Specify the top margin of the page.
* **Bottom**  
  Specify the bottom margin of the page.
* **Left**  
  Specify the left margin of the page.
* **Right**  
  Specify the right margin of the page.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741411534871-Order-Select-N-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741425258519-Parameter-Control-Properties)
