---
title: "Page Setup Dialog Box Properties"
id: 5741459540631
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741459540631-Page-Setup-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:41Z
---

# Page Setup Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741436173335-Navigation-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741446225687-Parameter-Control-Properties)

# Page Setup Dialog Box Properties

This topic describes how you can use the Page Setup dialog box to set the page properties of a web report and for the exported output of a web report. The dialog box varies according to different sources that you opened it from.

---

When you select **Page Setup** in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties#Page) to open the Page Setup dialog box, you can set the page properties of a web report, and the dialog box consists of two categories: [Web Report](#WizardWeb) and [Print Report](#WizardPrint).

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## Web Report

When you select **Web Report**, the unit of page size is pixel. Server displays the dialog box as follows.

![Page Setup dialog - Web Report](https://devnet.logianalytics.com/hc/article_attachments/9905730035863/pgstup_studio.gif)

**Resolution**

Specify the resolution of the report page.

* **Type**  
   Select the page type. Or select **Custom Size**, and then define the page width and height by yourself in the Width and Height fields.

**Margin**

Specify the margin properties of the report page.

* **Top**  
   Specify the distance of report data to the top edge of the page.
* **Bottom**  
   Specify the distance of report data to the bottom edge of the page.
* **Left**  
   Specify the distance of report data to the left edge of the page.
* **Right**  
   Specify the distance of report data to the right edge of the page.

## Print Report

When you select **Print Report**, the unit of the page size is inch. Server displays the dialog box as follows.

![Page Setup dialog - Print Report](https://devnet.logianalytics.com/hc/article_attachments/9905730075799/pgstup_prnt.gif)

**Page**

Specify the size of the report page.

* **Type**  
   Select the page type. Or select **Custom Size**, and then define the page width and height by yourself in the Width and Height fields.

**Orientation**

Specify the orientation of the report page.

* **Portrait**  
   Select to position the page vertically.
* **Landscape**  
   Select to position the page horizontally.

**Margin**

Specify the distance of the report data to the top, bottom, left, or right edge of the report page.

---

When you select Menu > File > Page Setup in Web Report Studio to open the Page Setup dialog box, you can set the page properties of a web report and for the exported output of a web report, and the dialog box consists of the following two tabs: [General](#General) and [Export.](#Export)

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## General

Specify the page properties of a web report. This tab consists of two categories: [Web Report](#StudioWeb) and [Print Report](#StudioPrint).

### Web Report

When you select **Web Report**, the unit of page size is pixel. The General tab looks like this.

![Page Setup dialog - General - Web Report](https://devnet.logianalytics.com/hc/article_attachments/9905730105495/pgstup_gnrl_web.gif)

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")**Page Layout**

Server selects this option by default, so the report applies [pagination mode](https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report#PageMode) in Web Report Studio. Clear it if you want to apply continuous page mode to the report, meaning, display the report in a single page.

**Resolution**

Specify the resolution of the report page.

* **Type**  
   Select the page type. Or select **Custom Size**, and then define the page width and height by yourself.
* **Width**  
   Specify the page width.
  + **Auto Fit**  
     Specify to dynamically calculate the page width according to the width of the contents within the page. The default behavior for exporting a new report (the option is unselected) is to enable content pagination which greatly improves the performance of the exporting process especially for a huge report.
* **Height**  
   Specify the page height.
  + **Auto Fit**  
     Specify to dynamically calculate the page height according to the height of the contents within the page. The default behavior for exporting a new report (the option is unselected) is to enable content pagination which greatly improves the performance of the exporting process especially for a huge report.

**Margin**

Specify the distance of the report data to the top, bottom, left, or right edge of the page.

### Print Report

When you select **Print Report**, the unit of the page size is inch. The General tab looks like this.

![Page Setup dialog - General - Web Report](https://devnet.logianalytics.com/hc/article_attachments/9905633489303/pgstup_gnrl_prnt.gif)

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")**Page Layout**

Server selects this option by default, so the report applies [pagination mode](https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report#Page%20Mode) in Web Report Studio. Clear it if you want to apply continuous page mode to the report, meaning, display the report in a single page.

**Page**

Specify the [page properties](#Page) of the report page.

**Orientation**

Specify the orientation of the report page: Portrait (vertically) or Landscape (horizontally).

**Margin**

Specify the distance of the report data to the top, bottom, left, or right edge of the report page.

## Export

Specify the page properties for the exported output of the report. The page properties specified for any export format will also apply when you advanced run and schedule to run the report in this format on Server.

![Page Setup dialog - Export](https://devnet.logianalytics.com/hc/article_attachments/9905654801687/pgstup_export.gif)

**Export to**

Specify the export format for which you want to customize the page properties.

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")**Page Layout**

Server selects this option by default, so the output of the selected format applies [pagination mode](https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report#PageMode). Clear it if you want to apply continuous page mode to the output, meaning, display the output in a single page.

You can customize the following properties for the selected format when you do not clear **Page Layout**.

**Auto**

When **Auto** is selected, the page properties you defined for the report in the [General tab](#General) of the dialog box will apply to the report output. Clear **Auto** if you want to customize the page properties for an export format.

When you clear **Auto** for an export format and select **OK** in the dialog box, Server adds an export page setting object for this format to the report structure tree in the Inspector panel. You can edit the export page properties there too. The page properties that you specify for any export format also apply when you advanced run and schedule to run the report in this format on Server.

Then, when you select **Auto** for this export format and select **OK** in the dialog box again, Server removes its export page setting object automatically from the report structure tree.

**Page**

Specify the [page properties](#Page) for the exported output.

**Orientation**

Specify the page orientation for the exported output: Portrait (vertically) or Landscape (horizontally).

**Margin**

Specify the distance of report data to the top, bottom, left and right edge of the exported output page, in inches.

---

When you select **More Settings** in the [Print dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459652119-Print-Dialog-Box-Properties) to open the Page Setup dialog box, you can specify the page properties for the printed output, and the dialog box contains the following options.

![Page Setup dialog](https://devnet.logianalytics.com/hc/article_attachments/9905730142487/pgstup.gif)

**Page**

Specify the page size.

* **Type**  
   Select the page type. Or select **Custom Size**, and then define the page width and height by yourself in the Width and Height fields.

**Margin**

Specify the margin properties.

* **Top**  
   Specify the distance of the layout area to the top edge of the page, in inches.
* **Left**  
   Specify the distance of the layout area to the left edge of the page, in inches.
* **Bottom**  
   Specify the distance of the layout area to the bottom edge of the page, in inches.
* **Right**  
   Specify the distance of the layout area to the right edge of the page, in inches.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741436173335-Navigation-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741446225687-Parameter-Control-Properties)
