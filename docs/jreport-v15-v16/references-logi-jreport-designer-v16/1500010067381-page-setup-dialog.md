---
title: "Page Setup Dialog"
id: 1500010067381
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067381-Page-Setup-Dialog
updated_at: 2021-07-24T10:38:31Z
---

# Page Setup Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032002-Page-Report-Option-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032082-Parameter-Dialog)

# Page Setup Dialog

The Page Setup dialog helps you to set the [general](https://devnet.logianalytics.com/hc/en-us/articles/1500010070921-Designing-the-Report-Pages#Setting) and [export](https://devnet.logianalytics.com/hc/en-us/articles/1500010068401-Exporting-Report-Result#Page) page properties for the current report tab in a page report, or for the current web report or library component. It appears when you select File > Page Setup, or the Page Setup button in the Style screen of the page report wizard.

The dialog contains two tabs: [General](#General) and [Export.](#Export)

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

## General

Specifies the general properties of the page, which can also be defined by the [page panel object](https://devnet.logianalytics.com/hc/en-us/articles/1500010034282-Page-Panel-Properties) in the Report Inspector.

![Page Setup - General](https://devnet.logianalytics.com/hc/article_attachments/4404909120535/pgstup_gnrl.gif)

**Paper**

Specifies the page size.

* **Type**  
   Specifies the paper type. Select the desired size from the drop-down list, if the given ones cannot meet your requirement, select Custom Size, and then define the paper width and height by yourself.
* **Width**  
   Specifies the width of the page.
  + **Auto Fit**  
     Specifies to dynamically calculate the page width according to the width of the contents within the page.
* **Height**  
   Specifies the height of the page.
  + **Auto Fit**  
     Specifies to dynamically calculate the page height according to the height of the contents within the page.

**Orientation**

Specifies the page orientation.

* **Portrait**  
   If selected, the page will be displayed as portrait.
* **Landscape**  
   If selected, the page will be displayed as landscape.

**Margin**

Specifies the distance of the report data to the top, bottom, left, or right edge of the page.

* **Top**  
   Specifies the top margin of the page.
* **Bottom**  
   Specifies the bottom margin of the page.
* **Left**  
   Specifies the left margin of the page.
* **Right**  
   Specifies the right margin of the page.

## Export

Specifies the page properties for the exported result of the report tab/web report/library component. The page properties specified for any export format will also be applied when advanced running and scheduling to run the report in this format on Logi JReport Server.

![Page Setup - Export](https://devnet.logianalytics.com/hc/article_attachments/4404909149079/pgstup_export.gif)

**Export to**

Specifies the export format to customize the page properties of its exported result.

**Auto**

If checked, the page properties defined in the [General](#General) tab of the dialog will be applied to the exported result of the selected format. Uncheck the option to customize the page properties for the selected format.

When you uncheck the Auto option for an export format and select OK in the dialog, a corresponding [export page setting object](https://devnet.logianalytics.com/hc/en-us/articles/1500010034322-Export-Page-Setting-Object-Properties) will be added to the report structure tree in the Report Inspector. You can edit the export page properties there too. When you check the Auto option for this export format and select OK in the dialog again, its export page setting object will be removed automatically from the report structure tree.

**Paper**

Specifies the [paper size](#Paper)  for the exported result.

**Orientation**

Specifies the page orientation for the exported result: Portrait (vertically) or Landscape (horizontally).

**Margin**

Specifies the distance of report data to the top, bottom, left and right edge of the exported result page.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032002-Page-Report-Option-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032082-Parameter-Dialog)
