---
title: "Print Dialog Box Properties"
id: 1500009745562
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745562-Print-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:54Z
---

# Print Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773581-Page-Setup-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745582-Printer-Properties)

# Print Dialog Box Properties

Use the Print dialog box to [print one or more library components in a dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009771781-Exporting-and-Printing-the-Library-Components-in-a-Dashboard) in the same format. This topic describes how to customize component layout and page properties for printing.

JDashboard displays the dialog box after you select the Print button ![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404880137367/btn_print.gif) on the toolbar or select the Options button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880435735/btn_dshbrd_optn.gif) on the toolbar and then select Print from the option list.

![Print dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880439191/prnt.gif)

**Layout**

* **System Layout**  
  Logi Report calculates the layout based on the position of the printable library components in the current dashboard. JDashboard displays the preview result of the system layout on the right. You can decide the components to print and their printing order in the Resources box.
* **Customize Layout**  
  Select **Customize Layout** if you want to rearrange the layout of the library components you would like to print using a tabular. You can customize the layout in the **Design** tab and preview it in the **Preview** tab.
* **Other customized layouts saved**  
  JDashboard also lists the layouts that you have saved for selection. You can do further modifications to them. For each of the customized layouts, you can edit its name or delete it using the two buttons - Rename and Delete - that JDashboard displays on the right when the mouse hovers over the layout item on the drop-down list.

  ![Layout Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4404880439703/dshbrd_expt_layout.gif)

**Resources**

* **For System Layout**  
   Select the library components you are going to print and customize their printing order.

  By default, JDashboard prints all printable library components. You can clear the library components that you do not want to print.

  The display order of the library components determines the order in which Logi Report prints them. You can select the buttons ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) to adjust the printing order.
* **For Customize Layout**JDashboard displays all the printable library components in the dashboard. You can drag the components from the Resources box to the Design tab to customize the layout.

**Show Component Title**

Select **Show Component Title** to display the library component titles in the printed result.

**Printer**

Select the printer with which to print the library components. In the Printer drop-down list, JDashboard displays the printers that the web browser can access, that is to say, the virtual printers in this drop-down list vary according to the operating system and the web browser you are using. If you want to download the result to a PDF or HTML file and then use your local printer to print the file, select **Save as PDF** or **Save as HTML**.

**Properties**

Select **Properties** to open the [Printer Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009745582-Printer-Properties) dialog box to specify the printing properties. JDashboard disables this option when you select Save as PDF or Save as HTML.

**Page Range**

The range of the pages that are to print.

* **All**  
   Logi Report prints all the pages.

**Copies**

Select the number of copies you want to print. The number of copies will take effect on the specified pages. JDashboard disables this option when you select Save as PDF or Save as HTML.

**Orientation**

Select the orientation for the printed result.

* **Portrait**  
  Select **Portrait** to print the result in a standard letter orientation.
* **Landscape**  
   Select **Landscape** to print the result in a landscape orientation.

**Paper**

Select the type of paper for printing the result.

**More Setting**

Select **More Setting** to open the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009773581-Page-Setup-Dialog-Box-Properties#Print) dialog box to specify page size and margin for the printed result.

**![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404880137367/btn_print.gif) Print**

Select to start printing. If you have selected Save as PDF or Save as HTML in the Printer drop-down list, Logi Report opens the result file of the library components in an associated program with which you can print the result to a printer.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404885307671/btn_save.gif)**Save**

Select to save the changes to an existing layout or open the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009745682-Save-As-Dialog-Box-Properties#Layout) dialog box if you are creating a new layout. JDashboard displays the layouts that you saved in the Layout drop-down list for applying. Other users will also be able to see and use the layouts that you saved when they open the same dashboard.

**![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404880136727/btn_saveas.gif) Save As**

Select to open the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009745682-Save-As-Dialog-Box-Properties#Layout) dialog box for saving a new layout with a name or saving an existing layout with another name.

**Options for managing tabular cell**

You can see the following icons when it is not System Layout and use them for customizing the layout in the Design tab.

* **![Horizontal Split](https://devnet.logianalytics.com/hc/article_attachments/4404880440087/btn_dshbrd_splth.gif) Horizontal Split**  
  Select to split a cell into two horizontal cells. When there is a library component in the cell, Logi Report places it in the left cell after the splitting.
* **![Merge](https://devnet.logianalytics.com/hc/article_attachments/4404885522967/btn_dshbrd_merge.gif) Merge**  
   Select to merge the adjacent cells that form a rectangle into one cell. When there is more than one library component in the cells, you cannot merge the cells.
* **![Vertical Split](https://devnet.logianalytics.com/hc/article_attachments/4404885523735/btn_dshbrd_spltv.gif) Vertical Split**  
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

By default, for tables and crosstabs, Logi Report only prints their current view of data as displayed in the dashboard. For example, if a table contains 10 pages of data and you browse to page 3 when you open the Print dialog box, then the table will only contain the data of page 3 in the printed result. If you want to print their full data, you can use the Filter option on the context menu to switch from Current View to All.

You see these options on the context menu after right-clicking in a tabular cell:

* **Filter**  
   Select **Filter** to open the [Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009773381-Filter-Dialog-Box-Properties) dialog box to choose the data scope of the table or crosstab in the tabular cell.
* **Remove**  
   Select **Remove** to remove the library component from the tabular cell.

**View tab**

You see the View tab when it is not System Layout. It provides a preview of the customized layout. You can select the page navigation and zooming buttons to preview the result.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Print dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without printing.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773581-Page-Setup-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745582-Printer-Properties)
