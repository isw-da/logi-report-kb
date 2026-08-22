---
title: "Save As Dialog Box Properties"
id: 4405690607895
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690607895-Save-As-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:29Z
---

# Save As Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683874071-Report-Body-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683880855-Select-a-Report-Dialog-Box-Properties)

# Save As Dialog Box Properties

This topic describes how you can use the Save As dialog box to save the current [web report](#Report) or the [web report page template](#Template), or save a data component in the current web report [as a library component](#LC). The dialog box varies for different purposes.

---

To use the Save As dialog box to [save the current web report](https://devnet.logianalytics.com/hc/en-us/articles/4405684044439-Saving-a-Web-Report), select Menu > File > Save As, select the Save As button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4420447052311/btn_saveas.gif) on the toolbar, or select **Save** in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties). Server displays the dialog box:

![Save As dialog box - Web Report](https://devnet.logianalytics.com/hc/article_attachments/4420453403671/svas_rpt.gif)

**Save In**

Specify the folder in the server resource tree where you want to save the report. Use the arrow button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4420453403927/btn_wbrpt_up.gif) to go to the parent folder. The root folder cannot store resources.

The resource table shows the resources in the selected folder. You can select the column names to change the order of the resources in the table.

* **Name**  
   The resource names.
* **Size**  
   The size of the resources.
* **Type**  
   The resource types.
* **Last Modified**  
   The last modified time of the resources.

**File Name**

Specify the name for the report.

**Type**

Select a file type for the saved report.

* **Web Report (\*.wls)**  
  Select to save the web report as a binary formatting file, which you can edit using Web Report Studio and Logi Report Designer.
* **Web Report XML Format (\*.wls.xml)**  
  Select to save the web report as an XML formatting file, which you can edit using external XML editors besides Web Report Studio and Logi Report Designer. Using XML is better for checking into source code control systems than using the binary formats.

**Advanced**/**Simple**

Select to display or hide the advanced settings.

* **Status**Specify the status of the report.
  + **Active**  
     Select if you want to execute the report. To execute a report means to run, advanced run, and schedule to run it.
  + **Inactive**  
     Select if you don't want to execute the report. The corresponding Run, Advanced Run, and Schedule commands for the report are not available.
  + **Incomplete**  
     Select if you have not finished the report design and you don't want to execute the report. The corresponding Run, Advanced Run, and Schedule commands for the report are not available.

* **Catalog**  
   Specify the catalog that you want the report to use.
  + **Set Original Catalog as Linked Catalog into Saved Report**  
     Select if you want to link the saved report with the catalog. The saved report will run with the catalog even if the two are in different folders. If later you update the catalog, the saved report will run with the latest version of the catalog.
  + **Set Catalog Copy to Target Folder**  
    Select if you want to copy the catalog to the folder where you save the report. The saved report will run with the copied catalog.
* **Save Sort Criteria**  
   Select to save the changes you made by sorting.
* **Save Filter Criteria**  
   Select to save the changes you made by filtering.
* **Description**Provide a description for the saved report.

**OK**

Select to save the report with the specified settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving the report.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif) **Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif) **Close button**

Select to close the dialog box without saving the report.

---

If you are an administrator with the privilege of publishing resources, you are able to see **Web Report Template** in the **Type** list of the Save As dialog box. By selecting **Web Report Template**, you can [save the page template](https://devnet.logianalytics.com/hc/en-us/articles/4405684047895-Creating-and-Using-Web-Report-Page-Templates) the web report uses.

When you use the Save As dialog box to save a web report page template, it looks like this:

![Save As dialog box - Web Report Template](https://devnet.logianalytics.com/hc/article_attachments/4420453545879/svas_rpttmplt.gif)

**Template box**

Server lists the existing web report page templates.

**File Name**

Specify the name of the web report page template. You can type the name to save it as a new template (.wsld) or select one from the template box to replace an existing template according to the Publish privilege, which is the system level authorization.

**Type**

Select **Web Report Template** from the list. You can see it when you are an administrator with the privilege of publishing resources.

**OK**

Select to save the web report page template with the specified settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving the web report page template.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif) **Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif) **Close button**

Select to close the dialog box without saving the web report page template.

---

To use the dialog box to [save a data component in a web report as a library component](https://devnet.logianalytics.com/hc/en-us/articles/4405684043031-Manipulating-Data-Components-in-Web-Report#SaveAsLC), right-click a table, crosstab, chart, KPI, or geographic map and select **Save as Library Component**. Server displays the dialog box:

![Save As dialog box - Library Component](https://devnet.logianalytics.com/hc/article_attachments/4420453418903/svas_lc.gif)

**Save In**

Select the folder in the server resource tree where you want to save the library component. Use the arrow button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4420453403927/btn_wbrpt_up.gif) to go to the parent folder. The root folder cannot store resources.

The resource table shows the resources in the selected folder. You can select the column names to change the order of the resources in the table.

* **Name**  
   The resource names.
* **Size**  
   The size of the resources.
* **Type**  
   The resource types.
* **Last Modified**  
   The last modified time of the resources.

**File Name**

Specify the name for the library component.

**Type**

It is Library Component by default which you cannot change.

**Advanced**/**Simple**

Select to display or hide the advanced settings.

* **Catalog**  
   Specify the catalog that the library component uses.
  + **Set Original Catalog as Linked Catalog into Saved Component**  
     Select if you want to link the library component with the catalog. The library component will run with the catalog even if the two are in different folders. If later you update the catalog, the library component will run with the latest version of the catalog.
  + **Set Catalog Copy to Target Folder**  
     Select if you want to copy the catalog to the folder where you save the library component. The library component will run with the copied catalog.
* **Save Sort Criteria**  
   Select to save the changes you made by sorting.
* **Save Filter Criteria**  
   Select to save the changes you made by filtering.
* **Description**Provide a description for the library component.

**OK**

Select to save the library component with the specified settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving the library component.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif) **Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif) **Close button**

Select to close the dialog box without saving the library component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683874071-Report-Body-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683880855-Select-a-Report-Dialog-Box-Properties)
