---
title: "Export Dialog Box Properties"
id: 1500009773361
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773361-Export-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:58Z
---

# Export Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773341-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773401-Fetch-Data-Dialog-Box-Properties)

# Export Dialog Box Properties

Use the component-level Export dialog box to export a specific library component, and the dashboard-level Export dialog box to [export one or more library components in a dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009771781-Exporting-and-Printing-the-Library-Components-in-a-Dashboard) in one format at a time. This topic describes how to customize export settings.

This topic contains the following sections:

* [Component-Level Export Dialog Box Properties](#Component)
* [Dashboard-Level Export Dialog Box Properties](#Dashboard)

## Component-Level Export Dialog Box Properties

JDashboard displays the component level Export dialog box after you select ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880135063/btn_dshbrd_more.gif) and select Export on the title bar of a library component. You can export an individual library component using the dialog box.

![Export dialog - Component Level](https://devnet.logianalytics.com/hc/article_attachments/4404885532951/expt_lc.gif)

**Export File Format**

Select the format in which to export the library component.

**OK**

Select **OK** to start exporting the library component.

**Cancel**

Select **Cancel** to close the dialog box without the export.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Export dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without exporting.

## Dashboard-Level Export Dialog Box Properties

JDashboard displays the dashboard level Export dialog box after you select the Export button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404880137111/btn_expt.gif) on the toolbar, or select the Options button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880435735/btn_dshbrd_optn.gif) on the toolbar and select Export from the option list. You can export one or more library components in a dashboard using the same format using the dialog box.

![Export dialog - Dashboard Level](https://devnet.logianalytics.com/hc/article_attachments/4404880452759/expt_dshbd.gif)

**Layout**

* **System Layout**  
  Logi Report calculates the layout based on the position of the exportable library components in the current dashboard. JDashboard displays the preview result of the system layout on the right.
  You can decide the components to export and their exporting order in the Resources box.
* **Customize Layout**  
   Select **Customize Layout** if you want to rearrange the layout of the library components you would like to export using a tabular. You can customize the layout in the **Design** tab and preview it in the **Preview** tab.
* **Other customized layouts saved**  
   JDashboard also lists the layouts that you have saved for selection. You can do further modifications to them. For each of the customized layouts, you can edit its name or delete it using the two buttons - Rename and Delete - that JDashboard displays on the right when the mouse hovers over the layout item on the drop-down list.

  ![Layout Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4404880439703/dshbrd_expt_layout.gif)

**Resources**

* **For System Layout**  
   Select the library components you are going to export and customize their exporting order.

  By default, JDashboard exports all exportable library components. You can clear the library components that you do not want to export.

  The display order of the library components determines the order in which Logi Report exports them. You can select the buttons ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) to adjust the exporting order.
* **For Customize Layout**  
  JDashboard displays all the exportable library components in the dashboard. You can drag the components from the Resources box to the Design tab to customize the layout.

**Show Component Title**

Select **Show Component Title** to display the library component titles in the exported result.

**![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404880137111/btn_expt.gif) Export**

Select to open the Export dialog box for doing the last setting and then exporting.

![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880453271/expt_expt.gif)

* **Export File Format**  
   Select the format in which to export the library components. For a format other than XML, Logi Report exports all selected library components into one single file. For XML, Logi Report exports each library component to a separate XML file. When the exported result contains more than one file, Logi Report zips all the files.
* **File Name**  
   The exported result may be either a single file or a zipped package of multiple files. The name is either a file name or a zipped package name.
* **Run Linked Report**  
  Select **Run Linked Report** if you want to generate the linked reports (not including the detail reports) in the result when the report is linked with other reports. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data.
* **OK**  
   Select **OK** to start exporting.
* **Cancel**  
   Select **Cancel** to close the dialog box without saving any changes.
* ![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)  
   Select to view information about the Export dialog box.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)  
   Select to close the dialog box without saving any changes.

**![Page Setup button](https://devnet.logianalytics.com/hc/article_attachments/4404885524503/btn_dshbrd_pgstup.gif) Page Setup**

Select to open the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009773581-Page-Setup-Dialog-Box-Properties) dialog box to specify the page properties of the exported result file.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404885307671/btn_save.gif)**Save**

Select to save the changes to an existing layout or open the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009745682-Save-As-Dialog-Box-Properties#Layout) dialog box if you are creating a new layout. JDashboard displays the layouts that you saved in the Layout drop-down list for applying. Other users will also be able to see and use the layouts that you saved when they open the same dashboard.

**![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404880136727/btn_saveas.gif) Save As**

Select to open the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009745682-Save-As-Dialog-Box-Properties#Layout) dialog box for saving a new layout with a name or saving an existing layout with another name.

**Options for managing tabular cell**

You can see the following icons when it is not System Layout and use them for customizing the layout in the Design tab.

* **![Horizontal Split button](https://devnet.logianalytics.com/hc/article_attachments/4404880440087/btn_dshbrd_splth.gif) Horizontal Split**  
   Select to split a cell into two horizontal cells. When there is a library component in the cell, Logi Report places it in the left cell after the splitting.
* **![Merge button](https://devnet.logianalytics.com/hc/article_attachments/4404885522967/btn_dshbrd_merge.gif) Merge**  
   Select to merge the adjacent cells that form a rectangle into one cell. When there is more than one library component in the cells, you cannot merge the cells.
* **![Vertical Split button](https://devnet.logianalytics.com/hc/article_attachments/4404885523735/btn_dshbrd_spltv.gif) Vertical Split**  
   Select to split a cell into two vertical cells. When there is a library component in the cell, Logi Report places it in the top cell after the splitting.

**Options for navigating pages**

* ![First Page](https://devnet.logianalytics.com/hc/article_attachments/4404885381143/btn_firstpg.gif)**First**  
   Select to go to the start page.
* ![Previous Page](https://devnet.logianalytics.com/hc/article_attachments/4404880246679/btn_prevpg.gif)**Previous**  
   Select to go to the previous page.
* ![Turn to Page](https://devnet.logianalytics.com/hc/article_attachments/4404880440727/btn_dshbrd_nmbr.gif)**Turn to Page**  
   Type a number in the text box and then press Enter to go to that page directly. If the input number is larger than the total page number, it goes to the last page, and if the number smaller than 1, it goes to the first page.
* ![Next Page](https://devnet.logianalytics.com/hc/article_attachments/4404880246935/btn_nxtpg.gif)**Next**  
   Select to go to the next page.
* ![Last Page](https://devnet.logianalytics.com/hc/article_attachments/4404880247319/btn_lastpg.gif)**Last**  
   Select to go to the last page.

**Options for zooming in/out the pages**

![Zoom In/Out](https://devnet.logianalytics.com/hc/article_attachments/4404880441239/btn_dshbrd_zm.gif)

The usage of the tool:

* Select **-** to zoom out.
* Select + to zoom in.
* Select a percentage from the drop-down list.
* Type a percentage in the text box. The zoom range is from 30% to 400%. If you type a value out of the range, Logi Report restores the ratio to the previously applied percentage.

**Design tab**

You see the Design tab when it is not System Layout. It is where you customize the component layout. Logi Report decides the page size according to the page setup properties and the ratio setting. A tabular fulfills the page printable area for holding a library component in each cell. Split or merge the cells and then drag library components from the Resources box into the cells to customize the layout.

By default, for tables and crosstabs, Logi Report only exports their current view of data as displayed in the dashboard. For example, if a table contains 10 pages of data and you browse to page 3 when you open the Export dialog box, then the table will only contain the data of page 3 in the exported result. If you want to export their full data, you can use the Filter option on the context menu to switch from Current View to All.

You see these options on the context menu after right-clicking in a tabular cell:

* **Filter**  
   Select **Filter** to open the [Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009773381-Filter-Dialog-Box-Properties) dialog box to choose the data scope of the table or crosstab in the tabular cell.
* **Remove**  
   Select **Remove** to remove the library component from the tabular cell.

**View tab**

You see the View tab when it is not System Layout. It provides a preview of the customized layout. You can select the page navigation and zooming buttons to preview the result.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Export dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without exporting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773341-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773401-Fetch-Data-Dialog-Box-Properties)
