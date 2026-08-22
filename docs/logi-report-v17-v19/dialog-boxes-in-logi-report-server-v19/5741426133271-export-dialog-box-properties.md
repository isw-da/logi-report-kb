---
title: "Export Dialog Box Properties"
id: 5741426133271
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741426133271-Export-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:42Z
---

# Export Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741412804759-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741412875287-Fetch-Data-Dialog-Box-Properties)

# Export Dialog Box Properties

Use the component-level Export dialog box to export a specific library component, and the dashboard-level Export dialog box to [export one or more library components in a dashboard](https://devnet.logianalytics.com/hc/en-us/articles/5741401668759-Exporting-and-Printing-the-Library-Components-in-a-Dashboard) in one format at a time. This topic describes how to customize export settings.

This topic contains the following sections:

* [Component-Level Export Dialog Box Properties](#Component)
* [Dashboard-Level Export Dialog Box Properties](#Dashboard)

## Component-Level Export Dialog Box Properties

Server displays the component-level Export dialog box after you select the Options button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/9905772219671/btn_dshbrd_more.gif) and select **Export** on the title bar of a library component. You can export an individual library component using the dialog box.

![Export dialog - Component Level](https://devnet.logianalytics.com/hc/article_attachments/9905760554391/expt_lc.gif)

**Select File Format**

Select the format in which you want to export the library component.

**OK**

Select to start exporting the library component.

**Cancel**

Select to close the dialog box without exporting.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the Export dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without exporting.

## Dashboard-Level Export Dialog Box Properties

Server displays the dashboard-level Export dialog box after you select the Export button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/9905578054551/btn_expt.gif) on the toolbar, or select the Options button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/9905759210647/btn_dshbrd_optn.gif) on the toolbar and select **Export**. You can export one or more library components in a dashboard using the same format using this dialog box.

![Export dialog - Dashboard Level](https://devnet.logianalytics.com/hc/article_attachments/9905760582679/expt_dshbd.gif)

**Layout**

* **System Layout**  
  Server calculates the layout based on the position of the exportable library components in the current dashboard. Server displays the preview result of the system layout on the right.
  You can decide the components to export and their exporting order in the Resources box.
* **Customize Layout**  
   Select if you want to rearrange the layout of the library components you would like to export using a tabular. You can customize the layout in the **Design** tab and preview it in the **View** tab.
* **Other customized layouts you saved**  
   Server also lists the layouts that you have saved for selection. You can do further modifications to them. For each of the customized layouts, you can edit its name or delete it using the two buttons - Rename and Delete - that display on the right when you hover over the layout item on the drop-down list.

  ![Layout Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/9905759609367/dshbrd_expt_layout.gif)

**Resources box**

* **For System Layout**  
   Select the library components you are going to export and customize their exporting order.

  By default, Server exports all exportable library components. You can clear the library components that you don't want to export.

  The display order of the library components defines the order in which Server exports them. You can select the two buttons ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) to adjust the exporting order.
* **For Customize Layout**  
  Server displays all the exportable library components in the dashboard. You can drag the components from the Resources box to the Design tab to customize the layout.

**Show Component Title**

Select to display the library component titles in the exported output.

**![Export button](https://devnet.logianalytics.com/hc/article_attachments/9905578054551/btn_expt.gif) Export button**

Select to open the Export dialog box for doing the last setting and then exporting.

![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/9905772307351/expt_expt.gif)

* **Export File Format**  
   Select the format in which you want to export the library components. For a format other than XML, Server exports all selected library components into one single file. For XML, Server exports each library component to a separate XML file. When the exported output contains more than one file, Server zips all the files.
* **File Name**  
   The exported output might be either a single file or a zipped package of multiple files. The name is either a file name or a zipped package name.
* **Run Linked Report**  
  Select if you want to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, leave this property cleared.
* **OK**  
   Select to start exporting.
* **Cancel**  
   Select to close the dialog box without saving any changes.
* ![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**  
   Select to view information about the Export dialog box.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**  
   Select to close the dialog box without saving any changes.

**![Page Setup button](https://devnet.logianalytics.com/hc/article_attachments/9905737759767/btn_dshbrd_pgstup.gif) Page Setup button**

Select to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741419794839-Page-Setup-Dialog-Box-Properties#Export) to specify the page properties of the output file.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/9905577991703/btn_save.gif)**Save button**

Select to save your changes to an existing layout or open the [Save As dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741405177239-Save-As-Dialog-Box-Properties#Layout) if you are creating a new layout. Server displays the layouts that you saved in the **Layout** drop-down list for applying. Other users will also be able to see and use the layouts that you saved when they open the same dashboard.

**![Save As button](https://devnet.logianalytics.com/hc/article_attachments/9905615943319/btn_saveas.gif) Save As button**

Select to open the [Save As dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741405177239-Save-As-Dialog-Box-Properties#Layout) for saving a new layout with a name or saving an existing layout with another name.

**Buttons for managing tabular cells**

You can see the following buttons when it is not System Layout and use them for customizing the layout in the Design tab.

* **![Horizontal Split button](https://devnet.logianalytics.com/hc/article_attachments/9905737778711/btn_dshbrd_splth.gif) Horizontal Split button**  
   Select to split a cell into two horizontal cells. When there is a library component in the cell, Server places it in the upper cell after the splitting.
* **![Merge button](https://devnet.logianalytics.com/hc/article_attachments/9905759670807/btn_dshbrd_merge.gif) Merge button**  
   Select to merge the adjacent cells that form a rectangle into one cell. When there is more than one library component in the cells, you cannot merge the cells.
* **![Vertical Split button](https://devnet.logianalytics.com/hc/article_attachments/9905737813655/btn_dshbrd_spltv.gif) Vertical Split button**  
   Select to split a cell into two vertical cells. When there is a library component in the cell, Server places it in the left cell after the splitting.

**Design tab**

You see the Design tab when it is not System Layout. It is where you customize the component layout. Logi Report decides the page size according to the page setup properties and the ratio setting. A tabular fulfills the exportable page area for holding a library component in each cell. Split or merge the cells, and then drag library components from the Resources box into the cells to customize the layout.

By default, for tables and crosstabs, Server only exports their current data view as displayed in the dashboard. For example, if a table contains 10 pages of data and you browse to page 3 when you open the Export dialog box, then the table will only contain the data of page 3 in the exported output. If you want to export their full data, you can use the **Filter** option on the shortcut menu to switch from Current View to All.

You see these options on the shortcut menu after right-clicking a tabular cell:

* **Filter**  
   Select to open the [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741441502359-Filter-Dialog-Box-Properties) to choose the data scope of the table or crosstab in the tabular cell.
* **Remove**  
   Select to remove the library component from the tabular cell.

**View tab**

You see the View tab when it is not System Layout. It provides a preview of the customized layout. You can select the page navigation and zooming buttons to preview the report.

**Buttons for navigating pages**

* ![First Page](https://devnet.logianalytics.com/hc/article_attachments/9905660274583/btn_firstpg.gif) **First button**  
   Select to go to the start page.
* ![Previous Page](https://devnet.logianalytics.com/hc/article_attachments/9905672321175/btn_prevpg.gif) **Previous button**  
   Select to go to the previous page.
* ![Turn to Page](https://devnet.logianalytics.com/hc/article_attachments/9905737867671/btn_dshbrd_nmbr.gif) **Turn to Page box**  
   Type a number in the text box and then press Enter to go to that page directly. If the input number is bigger than the total page number, Server displays the last page. If the number is smaller than 1, Server displays the first page.
* ![Next Page](https://devnet.logianalytics.com/hc/article_attachments/9905660312471/btn_nxtpg.gif) **Next button**  
   Select to go to the next page.
* ![Last Page](https://devnet.logianalytics.com/hc/article_attachments/9905660342807/btn_lastpg.gif) **Last button**  
   Select to go to the last page.

**Buttons for zooming in/out the pages**

![Zoom In/Out](https://devnet.logianalytics.com/hc/article_attachments/9905737907735/btn_dshbrd_zm.gif)

The usage of the tool:

* Select **-** to zoom out.
* Select **+** to zoom in.
* Select a percentage from the drop-down list.
* Type a percentage in the text box. The zoom range is from 30% to 400%. If you type a value out of the range, Server restores the ratio to the previously applied percentage.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the Export dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without exporting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741412804759-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741412875287-Fetch-Data-Dialog-Box-Properties)
