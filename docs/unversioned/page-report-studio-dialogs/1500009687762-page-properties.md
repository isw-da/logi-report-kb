---
title: "Page Properties"
id: 1500009687762
section: "Page Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009687762-Page-Properties
updated_at: 2021-11-03T06:58:04Z
---

# Page Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009713561-Order-Select-N)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009713641-Parameter-Control-Properties)

# Page Properties

The Page Properties dialog helps you to control the page properties of a report and the exported result of each export format. It consists of the following two tabs: [General](#General) and [Export.](#Export)

**OK**

Applies all changes and closes this dialog.

**Cancel**

Does not retain any changes and exits this dialog.

**Help**

Displays this help document.

## General

Specifies the page properties of the report.

![Page Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412131425687/pgprpty_gnrl.gif)

**Page**

Specifies the page properties of the report.

* **Type**  
   Specifies the page type. Select the desired size from the drop-down list, if the given ones cannot meet your requirement, select Custom Size, and then define the paper width and height by yourself.
* **Width**  
   Specifies the width of the page, in inches.
  + **Auto Fit**  
     Specifies to dynamically calculate the page width according to the width of the contents within the page.
* **Height**  
   Specifies the height of the page, in inches.
  + **Auto Fit**  
     Specifies to dynamically calculate the page height according to the height of the contents within the page.

**Orientation**

Specifies the orientation of the report page.

* **Portrait**  
   The page is positioned vertically.
* **Landscape**  
   The page is positioned horizontally.

**Margin**

Specifies the margin properties of the report page.

* **Top**  
   Specifies the distance of report data to the top edge of the page, in inches.
* **Left**  
   Specifies the distance of report data to the left edge of the page, in inches.
* **Bottom**  
   Specifies the distance of report data to the bottom edge of the page, in inches.
* **Right**  
   Specifies the distance of report data to the right edge of the page, in inches.

## Export

Specifies the page properties for the exported result of the report. The page properties specified for any export format will also be applied when advanced running and scheduling to run the report in this format on Logi JReport Server.

![Page Properties dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4412139527319/pgprpty_export.gif)

**Type**

Specifies the export format to customize the page properties of its exported result.

**Auto**

If checked, the page properties defined for the report in the [General tab](#General) of the dialog will be applied to the exported result of the selected format. Uncheck the option to customize the page properties for the selected format.

**Page**

Specifies the [page properties](#Page) for the exported result.

**Orientation**

Specifies the paper orientation for the exported result: Portrait (vertically) or Landscape (horizontally).

**Margin**

Specifies the distance of report data to the top, bottom, left and right edge of the exported result page, in inches.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009713561-Order-Select-N)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009713641-Parameter-Control-Properties)
