---
title: "Page Setup Dialog Box Properties"
id: 4405683867543
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683867543-Page-Setup-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:24Z
---

# Page Setup Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683864471-Navigation-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683868567-Parameter-Control-Properties)

# Page Setup Dialog Box Properties

This topic describes how you can use the Page Setup dialog box to set the page properties of a web report and for the exported output of a web report. The dialog box varies according to different sources that you opened it from.

---

When you select the **Page Setup** link in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties#Page) to open the Page Setup dialog box, it helps you to set the page properties of a web report and consists of two categories: [Web Report](#WizardWeb) and [Print Report](#WizardPrint).

**OK**

Applies all changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Ignores the setting and closes this dialog box.

## Web Report

If selected, the unit of page size is pixel, and Server displays the dialog box as follows.

![Page Setup dialog - Web Report](https://devnet.logianalytics.com/hc/article_attachments/4420447210647/pgstup_studio.gif)

**Resolution**

Specifies the resolution of the report page.

* **Type**  
   Specifies the page type. Select the desired size from the drop-down list, if the given ones cannot meet your requirement, select Custom Size, and then define the page width and height by yourself.
* **Width**  
   Specifies the page width.
* **Height**  
   Specifies the page height.

**Margin**

Specifies the margin properties of the report page.

* **Top**  
   Specifies the distance of report data to the top edge of the page.
* **Left**  
   Specifies the distance of report data to the left edge of the page.
* **Bottom**  
   Specifies the distance of report data to the bottom edge of the page.
* **Right**  
   Specifies the distance of report data to the right edge of the page.

## Print Report

If selected, the unit of the page size is inch, and Server displays the dialog box as follows.

![Page Setup dialog - Print Report](https://devnet.logianalytics.com/hc/article_attachments/4420453556631/pgstup_prnt.gif)

**Page**

Specifies the size of the report page.

* **Type**  
   Specifies the page type. Select the desired size from the drop-down list, if the given ones cannot meet your requirement, select Custom Size, and then define the page width and height by yourself.
* **Width**  
   Specifies the page width.
* **Height**  
   Specifies the page height.

**Orientation**

Specifies the orientation of the report page.

* **Portrait**  
   The page is positioned vertically.
* **Landscape**  
   The page is positioned horizontally.

**Margin**

Specifies the distance of the report data to the top, bottom, left, or right edge of the report page.

---

When you select Menu > File > Page Setup in Web Report Studio to open the Page Setup dialog box, it helps you to set the page properties of a web report and for the exported output of a web report, and consists of the following two tabs: [General](#General) and [Export.](#Export)

**OK**

Applies all changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Ignores the setting and closes this dialog box.

## General

This tab helps you to set the page properties of a web report and consists of two categories: [Web Report](#StudioWeb) and [Print Report](#StudioPrint).

### Web Report

If selected, the unit of page size is pixel, and the tab appears as follows.

![Page Setup dialog - General - Web Report](https://devnet.logianalytics.com/hc/article_attachments/4420447210903/pgstup_gnrl_web.gif)

**Resolution**

Specifies the resolution of the report page.

* **Type**  
   Specifies the page type. Select the desired size from the drop-down list, if the given ones cannot meet your requirement, select Custom Size, and then define the page width and height by yourself.
* **Width**  
   Specifies the page width.
  + **Auto Fit**  
     Specifies to dynamically calculate the page width according to the width of the contents within the page. The default behavior for exporting a new report (the option is unselected) is to enable content pagination which greatly improves the performance of the exporting process especially for a huge report.
* **Height**  
   Specifies the page height.
  + **Auto Fit**  
     Specifies to dynamically calculate the page height according to the height of the contents within the page. The default behavior for exporting a new report (the option is unselected) is to enable content pagination which greatly improves the performance of the exporting process especially for a huge report.

**Margin**

Specifies the distance of the report data to the top, bottom, left, or right edge of the page.

### Print Report

If selected, the unit of the page size is inch, and the tab appears as follows.

![Page Setup dialog - General - Print Report](https://devnet.logianalytics.com/hc/article_attachments/4420447086871/pgstup_gnrl_prnt.gif)

**Page**

Specifies the [page properties](#Page) of the report page.

**Orientation**

Specifies the orientation of the report page: Portrait (vertically) or Landscape (horizontally).

**Margin**

Specifies the distance of the report data to the top, bottom, left, or right edge of the report page.

## Export

Specifies the page properties for the exported output of the report. The page properties specified for any export format will also be applied when advanced running and scheduling to run the report in this format on Logi Report Server.

![Page Setup dialog - Export](https://devnet.logianalytics.com/hc/article_attachments/4420453434519/pgstup_export.gif)

**Export to**

Specifies the export format to customize the page properties of its exported output.

**Auto**

If the option is selected, the page properties defined for the report in the [General tab](#General) of the dialog box will be applied to the exported output of the report. Clear the option to customize the page properties for each export format.

When you clear **Auto** for an export format and select **OK** in the dialog box, Server adds an export page setting object to the report structure tree in the Inspector panel, for this specific export format. You can edit the export page properties there too. The page properties that you specify for any export format also apply when you advanced run and schedule to run the report in this format on Logi Report Server.

When you select **Auto** for this export format and select **OK** in the dialog box again, Server removes its export page setting object automatically from the report structure tree.

**Page**

Specifies the [page properties](#Page) for the exported output.

**Orientation**

Specifies the page orientation for the exported output: Portrait (vertically) or Landscape (horizontally).

**Margin**

Specifies the distance of report data to the top, bottom, left and right edge of the exported output page, in inches.

---

When you select the More Settings link in the [Print](https://devnet.logianalytics.com/hc/en-us/articles/4405683870743-Print-Dialog-Box-Properties) dialog box to open the dialog box, it helps you to specify the page properties for the printed output file and contains the following options.

![Page Setup dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453556887/pgstup.gif)

**Page**

Specifies the page size.

* **Type**  
   Specifies the page type. Select the desired size from the drop-down list, if the given ones cannot meet your requirement, select Custom Size, and then define the page width and height by yourself.
* **Width**  
   Specifies the width of the page, in inches.
* **Height**  
   Specifies the height of the page, in inches.

**Margin**

Specifies the margin properties.

* **Top**  
   Specifies the distance of the layout area to the top edge of the page, in inches.
* **Left**  
   Specifies the distance of the layout area to the left edge of the page, in inches.
* **Bottom**  
   Specifies the distance of the layout area to the bottom edge of the page, in inches.
* **Right**  
   Specifies the distance of the layout area to the right edge of the page, in inches.

**OK**

Applies all changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683864471-Navigation-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683868567-Parameter-Control-Properties)
