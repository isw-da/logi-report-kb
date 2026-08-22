---
title: "Save As Dialog Box Properties"
id: 1500009776361
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776361-Save-As-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:11Z
---

# Save As Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776201-Report-Body-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776281-Select-a-Report-Dialog-Box-Properties)

# Save As Dialog Box Properties

This topic describes how you can use the Save As dialog box to save the current [web report](#Report) or the [web report page template](#Template), or save a data component in the current web report [as a library component](#LC). The dialog box varies for different purposes.

---

To use the Save As dialog box to [save the current web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750182-Saving-a-Web-Report), select Menu > File > Save As or the Save As button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404880136727/btn_saveas.gif) on the toolbar, or select **Save** in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776601-Web-Report-Wizard-Properties). In this case Server displays the dialog box as follows:

![Save As dialog - Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404885318167/svas_rpt.gif)

**Save In**

Specifies the directory in the server resource tree where you want to save the report. Use the button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4404880146199/btn_wbrpt_up.gif) to go to the parent folder. The root folder cannot be used to store resources.

The resource table shows the resources in the current directory. You can select the column names to change the order of the resources in the table list.

* **Name**  
   Displays the resource names.
* **Size**  
   Displays the size of the resources.
* **Type**  
   Displays the resource types.
* **Last Modified**  
   Displays the last modified time of the resources.

**File Name**

Specifies the name for the report.

**Type**

It is Web Report by default.

**Advanced**/**Simple**

Displays or hides the advanced settings.

* **Status**Specifies the status of the report.
  + **Active**  
     The report can be executed. To execute a report means to run, advanced run and schedule to run it.
  + **Inactive**  
     The report cannot be executed. If selected, the corresponding Run, Advanced Run and Schedule commands for the report are not available.
  + **Incomplete**  
     The report is not completely designed and cannot be executed. If selected, the corresponding Run, Advanced Run and Schedule commands for the report are not available.

* **Catalog**  
   Specifies the catalog that the report uses.
  + **Set Original Catalog as Linked Catalog into Saved Report**  
     If the option is selected, the saved report will be linked with the catalog and will run with the catalog no matter whether the two are in the same directory. If later the catalog is updated, the report will run with the latest version of the catalog.
  + **Set Catalog Copy to Target Folder**  
     If the option is selected, the catalog will be copied to the directory where the report is saved, and the saved report will run with the copied catalog.
* **Save Sort Criteria**  
   Specifies whether to save the changes made by sorting.
* **Save Filter Criteria**  
   Specifies whether to save the changes made by filtering.
* **Description**Specifies the description for the report.

**OK**

Saves the report with the specified settings and closes this dialog box.

**Cancel**

Does not save the report and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

---

If you are an admin user with the privilege of publishing resources, you are able to see the option **Web Report Template** from the **Type** drop-down list of the Save As dialog box. By selecting the option you can [save the page template](https://devnet.logianalytics.com/hc/en-us/articles/1500009750022-Creating-Web-Reports-Using-the-Wizard#Template) the web report uses.

When you use the Save As dialog box to save a web report page template, it appears as follows:

![Save As dialog - Web Report Template](https://devnet.logianalytics.com/hc/article_attachments/4404885440663/svas_rpttmplt.gif)

**Template box**

Lists the existing web report page templates.

**File Name**

Specifies the name of the web report page template. You can type the name to save it as a new template (.wsld) or select one from the template box above to overwrite an existing template according to the Publish privilege, which is the system level authorization.

**Type**

Select **Web Report Template** from the drop-down list. The option Web Report Template is available to administrators with the privilege of publishing resources.

**OK**

Saves the web report page template with the specified settings and closes this dialog box.

**Cancel**

Does not save the web report page template and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

---

To use the dialog box to [save a data component in a web report as a library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report#SaveAsLC), right-click a table, crosstab, chart, KPI, or geographic map and select **Save as Library Component**. In this case Server displays the dialog box as follows:

![Save As dialog - Library Component](https://devnet.logianalytics.com/hc/article_attachments/4404880158999/svas_lc.gif)

**Save In**

Specifies the directory in the server resource tree where you want to save the library component. Use the button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4404880146199/btn_wbrpt_up.gif) to go to the parent folder. The root folder cannot be used to store resources.

The resource table shows the resources in the current directory. You can select the column names to change the order of the resources in the table list.

* **Name**  
   Displays the resource names.
* **Size**  
   Displays the size of the resources.
* **Type**  
   Displays the resource types.
* **Last Modified**  
   Displays the last modified time of the resources.

**File Name**

Specifies the name for the library component.

**Type**

It is Library Component by default which cannot be changed.

**Advanced**/**Simple**

Displays or hides the advanced settings.

* **Catalog**  
   Specifies the catalog that the library component uses.
  + **Set Original Catalog as Linked Catalog into Saved Component**  
     If the option is selected, the saved library component will be linked with the catalog and will run with the catalog no matter whether the two are in the same directory. If later the catalog is updated, the library component will run with the latest version of the catalog.
  + **Set Catalog Copy to Target Folder**  
     If the option is selected, the catalog will be copied to the directory where the library component is saved, and the library component will run with the copied catalog.
* **Save Sort Criteria**  
   Specifies whether to save the changes made by sorting.
* **Save Filter Criteria**  
   Specifies whether to save the changes made by filtering.
* **Description**Specifies the description for the library component.

**OK**

Saves the library component with the specified settings and closes this dialog box.

**Cancel**

Does not save the library component and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776201-Report-Body-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776281-Select-a-Report-Dialog-Box-Properties)
