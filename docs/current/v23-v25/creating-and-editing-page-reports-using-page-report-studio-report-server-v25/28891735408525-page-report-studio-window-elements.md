---
title: "Page Report Studio Window Elements"
id: 28891735408525
section: "Creating and Editing Page Reports Using Page Report Studio Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891735408525-Page-Report-Studio-Window-Elements
updated_at: 2026-02-26T02:13:41Z
source_host: docs-report.zendesk.com
---
# 
Page Report Studio Window Elements 

You can determine the options that you see in Page Report Studio by configuring the server profile. This topic describes how to use the options in the Page Report Studio Window.

To customize the options in Page Report Studio, see Customizing Page Report Studio Profile.

The window elements of Page Report Studio vary with its two view modes: Basic View and Interactive View. The following table introduces the full UI elements involving both modes. The shortcut menu contents vary with the objects you right-click, and the table only list some typical items.

| Menu/Toolbar | Option/Button | Description |
| --- | --- | --- |
| Menu > File | New Page Report Tab | Select to create a new report tab to the current page report. |
| New Page Report | Select to create a new page report containing a report tab. |  |
| Open | Select to display the Open Report Tabs dialog box, and then select or clear the report tabs that you want to open or close in the current report. |  |
| Rename Report Tab | Select to open the Rename Report Tab dialog box, and then give the current report tab a new name. |  |
| Close Report Tab | Select to close the current report tab if there is more than one report tab in the report, or to decide whether you want to close the report if it has only one report tab. |  |
| Delete Report Tab | Select to delete the current report tab if there is more than one report tab in the report. Server disables this item when haven't access the last page of the current report tab, and if Format Page on Demand is selected in the Page Report Studio profile. |  |
| Save | Select to save the report as a report version. |  |
| Save As | Select to save a copy of the report. |  |
| Export | Select to export the report to disk or version in various formats. |  |
| Page Setup | Select to open the Page Properties dialog box to specify the page layout settings for the report. |  |
| Printable Version | Select to open the Printable Version dialog box to print the current report to PDF/HTML. |  |
| Exit | Select to close the current report and exit the Page Report Studio. |  |
| Menu > Edit | Undo | Select to undo the last operation. |
| Redo | Select to reverse the operation of Undo. |  |
| Search | Select to open the Search dialog box to find specific text. |  |
| Menu > View | Toolbar | Clear to hide the Standard, View, or Analysis toolbar. |
| User Information Bar | Select to display the User Information Bar, which shows your username, the catalog name, and the report name. |  |
| Toolbox | Select to display the Toolbox panel from which you can insert components into the report. |  |
| Resource View | Select to display the Resource View panel, with which you can add view elements to your report and create dynamic resources to use them in your report. |  |
| TOC Browser | Select to display the TOC Browser, with which you can navigate the report data. |  |
| Editing Marks | Select to display editing marks, that is dashed outlines for objects and report body. By default, the option is cleared. In this case, the editing marks do not show when a report object receives focus, and you cannot move or resize report objects. |  |
| Turn To | Select a report page. |  |
| Refresh | Select to run the report using previously provided parameters and fetch the report data again. |  |
| Zoom | Select to open the Zoom dialog box and then set a zoom ratio for the report page. |  |
| Options | Select to open the Options dialog box, then set the skin and unit for Page Report Studio, and customize toolbar options. |  |
| Show Grids | Select to show grids in the report area. |  |
| Snap to Grids | By default, Server enables this option, and aligning objects is easier. It snaps an object to grids when you move it by dragging and dropping in the report area. To temporarily replace the setting, press ALT as you move an object. |  |
| Menu > Insert | Label | Select to insert a label into the report. |
| Image | Select to insert an image into the report. |  |
| Banded Object | Select to insert a banded object into the report. |  |
| Table | Select to insert a table into the report. |  |
| Crosstab | Select to insert a crosstab into the report. |  |
| Chart | Select to insert a chart into the report. |  |
| Parameter Control | Select to insert a parameter control into the report. |  |
| Parameter Form Control | Select to insert a parameter form control into the report. |  |
| Filter Control | Select to insert a filter control into the report. |  |
| Navigation Control | Select to insert a navigation control into the report. |  |
| Special Fields | Select to insert a special field into the report. |  |
| Page Break | Select to insert a page break into the report. |  |
| Menu > Report | Edit Dataset Filter | Select to apply a filter to the business view used by a data component in the report. |
| Filter | Select to filter the report records. |  |
| On-screen Filter Values | The option is available when administrators did not clear Enable Setting Default On-screen Filter Values For Page Report in the server profile. Save as Default Select to save the current on-screen filter values as the user defined default values for the report and for you. Server disables this menu item when the current on-screen filter values are the same as the default values. Restore to Default Select to restore to the default on-screen filter values. Server disables this menu item when the current on-screen filter values are the same as the default values. Clear Default Select to clear user defined default on-screen filter values. Server disables this menu item when there are no user defined default values. Push Down Select if you want to generate the report data by applying all filters to the database. |  |
| Sort | Select to sort the report records or groups in ascending or descending order on the fields you select. |  |
| To Chart | Select to convert the crosstab into a chart. |  |
| To Crosstab | Select to convert the chart into a crosstab. |  |
| Rotate Table | Select to switch the table between the horizontal and vertical layout modes. |  |
| Rotate Crosstab | Select to exchange the columns and rows in the crosstab. |  |
| Merge | Select to merge selected tabular cells into one. |  |
| Split | Select to split the tabular cell into the specified number of rows and columns. |  |
| Language | Select the language in which you want to display the report if it is an NLS report. Available only when you selected Enable NLS in the server profile. |  |
| Use Dynamic Formula in Property | You can use dynamic formulas to control object properties. You see this option when you enabled the Advanced User feature in the Page Report Studio profile. |  |
| Style | Select to apply a style to the report. |  |
| Change Parameters | Select to change the parameter values in the report. |  |
| Manage Datasets | Select to manage datasets in a page report. |  |
| Parameter Order | You can use the Parameter Order dialog to adjust the display sequence of the parameters in the UI for specifying parameter values at report level. |  |
| Menu > Help | User's Guide | Select to open the Page Report Studio user documentation. |
| Report Home Page | Select to connect to Report Home Page at https://www.logianalytics.com/. |  |
| Technical Support | Select to contact Logi Analytics technical support. |  |
| About Page Report Studio | Select to view product information about Page Report Studio. |  |
| Standard Toolbar | New Report Tab | Select to create a new report tab. |
| Open | Select to display the Open Report Tabs dialog box, and then open/close report tabs in the current report. |  |
| Save | Select to save the report as a report version. |  |
| Save As | Select to save a copy of the report. |  |
| Export | Select to export the report to disk or version in various formats. |  |
| Printable Version | Select to display the Printable Version dialog box to print the current report to a PDF/HTML file. |  |
| Undo | Select to undo the last operation. |  |
| Redo | Select to reverse the operation of Undo. |  |
| Delete | Select to delete the selected object. |  |
| View Toolbar | Toolbox | Select to display the Toolbox panel from which you can insert components into the report. Select the button again to hide the Toolbox panel. |
| Resource View | Select to display the Resource View panel, with which you can add view elements to your report and create dynamic resources in your report. Select the button again to hide the Resource View panel. |  |
| Filter | Select to display the Filter dialog box, with which you can filter the report records according to the filter criteria you specify. |  |
| Dataset Filter | Select to display the Edit Dataset Filter dialog box, with which you can apply a filter to the dataset used by the selected data component in the report. |  |
| Sort | Select to display the Sort dialog box, with which you can sort the report records or groups in ascending or descending order on the fields you select. |  |
| Search | Select to display the Search dialog box to find specific text. |  |
| Zoom | Select to enlarge or reduce the size of the report. |  |
| Analysis Toolbar | Rotate | Select to rotate the selected crosstab or table. |
| Chart Type | Select to change the type of the selected chart. |  |
| Select One Style | Select a style you want to apply to the report. |  |
| Font Format | Select Font | Select to update the font face of the selected text. You see this item only when you selected a label or field. |
| Select Font Size | Select to update the size of the selected text. You see this item only when you selected a label or field. |  |
| Bold | Select to make the selected text in bold. You see this item only when you selected a label or field. |  |
| Italic | Select to make the selected text in italic type. You see this item only when you selected a label or field. |  |
| Underline | Select to make the selected text in underlined style. You see this item only when you selected a label or field. |  |
| Left | Select to make the selected text left aligned. You see this item only when you selected a label or field. |  |
| Center | Select to make the selected text center aligned. You see this item only when you selected a label or field. |  |
| Right | Select to make the selected text right aligned. You see this item only when you selected a label or field. |  |
| Page Controls | Turn to Page | Type a page number in the number box and press Enter to go to that page. |
| First Page | Select to go to the first page of the current report tab. |  |
| Previous Page | Select to go to the previous page. |  |
| Next Page | Select to go to the next page. |  |
| Last Page | Select to go to the last page. |  |
| Go To |  | If a report contains several report tabs, you can use this list to switch among the report tabs. Also, when opening a detail report in the same window as the master report, Server lists the items for tracing the master/detail report navigation here, with which you can return to any report easily. |
| More Commands | Keep as Background Task | Select to keep the open page report as a background task. |
| Quick Schedule | Select to schedule a task to publish the report to email, FTP site, or the Report Server versioning system. |  |
| TOC Browser | Select to display the TOC Browser, with which you can navigate the report data. You can then clear the button to hide the TOC Browser. To display the TOC Browser button on the toolbar in the Basic View, select the Customize Toolbar Items button on the toolbar, then select the closed eye icon beside TOC Browser. |  |
| / | Select the data mode of the report. |  |
| Interactive View/Basic View | Switch between the two views of Page Report Studio. Available if you do not clear Show Link of Basic/Interactive View in the Page Report Studio profile. |  |
| Back | Select to go back to the previous level in the report chain, which Server creates when you perform the going-to-detail or linking-to-report action. |  |
| Next | Select to go forward to the next level in the report chain, which Server creates when you perform the going-to-detail or linking-to-report action. |  |
| Visited Reports | When you perform the going or linking-to-report action, Server creates a report chain. This drop-down button lists the original report and the reports you have just visited within the report chain. The selected report in the drop-down list is the report you currently open. Select another report and you will jump to that report. |  |
| Customize Toolbar Items | Select to show or hide the toolbar items and adjust their order in the Basic View of Page Report Studio. |  |
| More Items | Select to access more toolbar items that cannot display directly on the toolbar due to limited space. |  |
|  | Select the language in which you want to display the report if it is an NLS report. Available only when you selected Enable NLS in the server profile. |  |
| Shortcut Menu | Filter | Select an item for filtering the data in a banded object/table or removing the filter. |
| Sort | Select an item for sorting records on the selected field in ascending/descending order, or removing the sort order. |  |
| Drill Down | Select to drill data to a lower group according to predefined hierarchy. |  |
| Drill To | Select to obtain a different view of data by switching among groups. |  |
| Drill to By Value | Select to filter data based on groups while also obtaining a more detailed view of the data. |  |
| Drill Up | Select to drill data to a higher group according to predefined hierarchy. |  |
| Go To | Select to go to any group to show its record information. |  |
| Go Up | Select to go up one group level to show the records of a higher-level group. |  |
| Go Down | Select to go down one group level to show the records of a child group. |  |
| Go to Detail | Select to go to the details of a group. |  |
| Conditional Formatting | Select to add conditional format to the selected field. |  |
| Search | Select to display the Search dialog box, and then search the report for specific text. |  |
| Edit Dataset Filter | Select to apply a filter to the business view used by the selected data component. |  |
| Refresh | Select to re-fetch data of the specified data component. |  |
| Properties | Select to display a dialog box, and then define the object's properties. |  |
