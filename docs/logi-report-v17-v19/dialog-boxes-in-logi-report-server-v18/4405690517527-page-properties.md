---
title: "Page Properties"
id: 4405690517527
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690517527-Page-Properties
updated_at: 2022-01-27T07:58:47Z
---

# Page Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683670423-Order-Select-N-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690519319-Parameter-Control-Properties)

# Page Properties

You can use the Page Properties dialog box to specify the page properties of a report and its output. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Export Tab Properties](#Export)

You see these elements on both tabs:

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Use this tab to specify the general properties of the page.

![Page Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420461562135/pgprpty_gnrl.gif)

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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) After you select a page type and then select **Auto Fit**, Server changes the page type to **Custom Size** automatically.

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

![Page Properties dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4420461562519/pgprpty_export.gif)

**Export To**

Select the export format to customize the page properties of its output.

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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) After you select a page type and then select **Auto Fit**, Server changes the page type to **Custom Size** automatically.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683670423-Order-Select-N-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690519319-Parameter-Control-Properties)
