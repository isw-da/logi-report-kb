---
title: "Page Report Studio Window Elements"
id: 1500009691762
section: "Page Report Studio Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691762-Page-Report-Studio-Window-Elements
updated_at: 2021-11-03T06:56:48Z
---

# Page Report Studio Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718101-Page-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718121-Creating-Page-Reports)

# Page Report Studio Window Elements

The options available in Page Report Studio are determined by the feature profile that is selected as the default profile in the Customize Profile > Page Report Studio > Features tab of the profile page and the property settings in the Customize Profile > Page Report Studio > Properties tab (profile has the higher priority). For additional information, see [Customizing Page Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009691802-Customizing-Page-Report-Studio-Profile).

The window elements of Page Report Studio vary with its two view modes: Basic View and Interactive View. The following table introduces the full UI elements based on the Interactive View mode. The shortcut menu contents vary with the objects you right-click and the table only lists some typical items.

| Menu/Toolbar | Option/Button | Description |
| --- | --- | --- |
| File | New Page Report Tab | [Creates a new report tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009718121-Creating-Page-Reports) to the current page report based on an existing business view. |
|  | New Page Report | Creates a new page report containing a report tab based on an existing business view. |
|  | Open | Opens the Open Report Tabs dialog for you to open/close report tabs in current report. |
|  | Rename Report Tab | Opens the Rename Report Tab dialog to give the open report tab a new name. |
|  | Close Report Tab | Closes the current report tab if there is more than one report tab open in the report; or prompts you to close the report if there is only one report tab. |
|  | Delete Report Tab | Deletes the current report tab if there is more than one report tab open in the report. This command is disabled when the last page of the current report tab does not display if [Format Page on Demand](https://devnet.logianalytics.com/hc/en-us/articles/1500009691802-Customizing-Page-Report-Studio-Profile#RenderMode) is selected in the Page Report Studio profile. |
|  | Save | [Saves the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009691682-Saving-the-Report) as a report version. |
|  | Save As | Saves a copy of the report. |
|  | Export | [Exports the report result](https://devnet.logianalytics.com/hc/en-us/articles/1500009718161-Exporting-Printing-the-Report-Result) to disk or version in various formats. |
|  | Page Setup | Shows the Page Properties dialog for you to specify the page layout settings for the report result. |
|  | Printable Version | Shows the Printable Version dialog for you to [print the current report result](https://devnet.logianalytics.com/hc/en-us/articles/1500009718161-Exporting-Printing-the-Report-Result#Print) to a PDF/HTML file. |
|  | Exit | Closes the current report. |
| Edit | Undo | Undoes the last operation. |
|  | Redo | Reverses the operation of Undo. |
|  | Search | Shows the Search dialog for you to [find specific text](https://devnet.logianalytics.com/hc/en-us/articles/1500009691722-Searching-for-Text-in-a-Report). |
| View | Toolbar | Shows or hides toolbars. |
|  | User Information Bar | Shows or hides the User Information Bar, which displays the user name, catalog name and report name. |
|  | Toolbox | Shows or hides the Toolbox panel which allows you to insert a component into the report. |
|  | Resource View | Shows or hides the Resource View panel, with which you can add view elements to your report and [create dynamic resources to use them](https://devnet.logianalytics.com/hc/en-us/articles/1500009691582-Using-Dynamic-Resources) in your report. |
|  | TOC Browser | Shows or hides the TOC Browser, with which you can navigate the report data. |
|  | Editing Marks | Shows or hides editing marks (dashed outlines for objects and report body). If the option is unselected, the editing mark will not be shown when a report object receives focus, and report objects cannot be moved or resized. |
|  | Turn To | Provides a submenu for you to turn the report pages. |
|  | Refresh | Runs the report using previously provided parameters. The Refresh operation fetches the data again. |
|  | Zoom | Shows the Zoom dialog for you to set a zoom ratio for the report page. |
|  | Options | Shows the Options dialog for you to set the skin and unit for Page Report Studio, and to customize toolbars. |
|  | Show Grids | Shows grids in the report area. |
|  | Snap to Grids | Snaps an object to grids when you move it by dragging and dropping in the report area. If this option is enabled, aligning objects will be made easier. To temporarily override the setting, press the ALT key as you move an object. |
| Insert | Label | Inserts a label into the report. |
|  | Image | Inserts an image into the report. |
|  | Banded Object | Inserts a banded object into the report. |
|  | Table | Inserts a table into the report. |
|  | Crosstab | Inserts a crosstab into the report. |
|  | Chart | Inserts a chart into the report. |
|  | Parameter Control | [Inserts a parameter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls#Parameter) into the report. |
|  | Parameter Form Control | [Inserts a parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls#ParamForm) into the report. |
|  | Filter Control | [Inserts a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls#Filter) into the report. |
|  | Navigation Control | [Inserts a navigation control](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls#Navigation) into the report. |
|  | Special Fields | Inserts special fields into the report. |
|  | Page Break | [Inserts a page break](https://devnet.logianalytics.com/hc/en-us/articles/1500009718181-General-Operations-in-a-Report#PageBreak) into the report. |
| Report | Query Filter | [Applies a filter to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009691602-Applying-Filters) used by certain component. |
|  | Filter | [Filters the report records](https://devnet.logianalytics.com/hc/en-us/articles/1500009691602-Applying-Filters#Dialog) according to the filter criteria you specify. |
|  | [On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls#Default) | The option is unavailable when [Enable Setting Default On-screen Filter Values For Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#OnScreenFilter) is not selected in the server profile.  * **Save as Default**  Saves the current on-screen filter values as the user-defined default values for the report and for the user. This menu item is disabled when the current on-screen filter values are the same as the default values. * **Restore to Default**  Restores to the default on-screen filter values. This menu item is disabled when current on-screen filter values are the same as the default values. * **Clear Default**  Clears user-defined default on-screen filter values. This menu item is disabled when there are no user-defined default values. |
|  | Sort | [Sorts the report records or groups](https://devnet.logianalytics.com/hc/en-us/articles/1500009691702-Sorting-Report-Data) in ascending or descending order on the fields you select. |
|  | To Chart | [Converts a crosstab into a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009691642-Manipulating-Data-Components#ToChart). |
|  | To Crosstab | [Converts a chart into a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009691642-Manipulating-Data-Components#ToCrosstab). |
|  | Rotate Table | Rotates a table to switch its appearance between the horizontal and vertical layout modes. |
|  | Rotate Crosstab | Rotates a crosstab to exchange the columns and rows in the crosstab in order to create a different view of the crosstab. |
|  | Merge | Merges selected tabular cells into one. |
|  | Split | Splits a tabular cell into the specified number of rows and columns. |
|  | Language | Allows you to specify the language in which to display the report. Available only when [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#NLS) is checked in the server profile. |
|  | Use Dynamic Formula in Property | Allows you to apply dynamic formulas to control object properties. |
|  | Style | Allows you to [apply a style](https://devnet.logianalytics.com/hc/en-us/articles/1500009718181-General-Operations-in-a-Report#Style) to the report. |
|  | Change Parameters | Allows you to [change the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009718181-General-Operations-in-a-Report#Param) in the report. |
| Help | User's Guide | Opens Page Report Studio User's Guide. |
|  | Logi JReport Home Page | Connects to Logi JReport Home Page. |
|  | Technical Support | Accesses Logi Analytics Technical Support. |
|  | About Page Report Studio | Shows product information about Page Report Studio. |
| Standard Toolbar | New Report Tab button New Report Tab | Creates a new report tab based on an existing business view. |
|  | Open button Open | Brings out the Open Report Tabs dialog for you to open/close report tabs in current report. |
|  | Save button Save | Saves the report as a report version. |
|  | Save As button Save As | Saves a copy of the report. |
|  | Export button Export | Exports the report result to disk or version in various formats. |
|  | Printable Version button Printable Version | Shows the Printable Version dialog for you to print the current report result to a PDF/HTML file. |
|  | Undo button Undo | Undoes the last operation. |
|  | Redo button Redo | Reverses the operation of Undo. |
|  | Delete button Delete | Deletes the selected object. |
| View Toolbar | Toolbox button Toolbox | Shows the Toolbox panel for you to insert a component into the report. Select it again to hide the Toolbox. |
|  | Resource View button Resource View | Shows the Resource View panel, with which you can add view elements to your report and create dynamic resources to use them in your report. Select it again to hide the Resource View panel. |
|  | Filter button Filter | Shows the Filter dialog, with which you can filter the report records according to the filter criteria you specify. |
|  | Sort button Sort | Shows the Sort dialog, with which you can sort the report records or groups in ascending or descending order on the fields you select. |
|  | Search button Search | Shows the Search dialog for you to find specific text. |
|  | Zoom button Zoom | Enables you to enlarge or reduce the size of the report. |
| Analysis Toolbar | Rotate button Rotate | Rotates a crosstab or rotates a table. |
|  | Chart Type button Chart Type | Lists all available chart types for you to change the type of a selected chart. |
|  | Style button | Allows you to apply a style to the report. |
| Font format buttons | Font Face button | Changes the face of the selected font. Available only when a label or field is selected. |
|  | Font Size button | Changes the size of the selected font. Available only when a label or field is selected. |
|  | Bold button | Makes the selected font in bold style. Available only when a label or field is selected. |
|  | Italic button | Makes the selected font in italic style. Available only when a label or field is selected. |
|  | Underline button | Makes the selected font in underlined style. Available only when a label or field is selected. |
|  | Align Left button | Makes the selected font left aligned. Available only when a label or field is selected. |
|  | Align Center button | Makes the selected font center aligned. Available only when a label or field is selected. |
|  | Align Right button | Makes the selected font right aligned. Available only when a label or field is selected. |
| Page navigation buttons | Page Number button | Displays the current page number. You can also input a page number in the page box and press Enter on the keyboard to go to that page. |
|  | First button | Goes to the first page of the current report tab. |
|  | Previous button | Goes to the previous page. |
|  | Next button | Goes to the next page. |
|  | End button | Goes to the last page. |
| Go To drop-down list | Go To Drop-down List | If a report contains several report tabs, you can use this list to switch among the report tabs. Also, when opening a detail report which is displayed in the same window as the master report, the items for tracing the master/detail report navigation will be listed in the list, with which you can return to any report easily. |
| More Commands | Keep as Background Task Keep as Background Task | Specifies to [keep the opened page report in the Background Tasks table](https://devnet.logianalytics.com/hc/en-us/articles/1500009718181-General-Operations-in-a-Report#Background). |
|  | Quick Schedule button Quick Schedule | [Schedules task](https://devnet.logianalytics.com/hc/en-us/articles/1500009718181-General-Operations-in-a-Report#Schedule)  to publish the report to e-mail, FTP site, or the Logi JReport Server versioning system. |
|  | Full Data/Partial Data | Specifies the [data mode of the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009718181-General-Operations-in-a-Report#DataMode). |
|  | Interactive View/Basic View | Switches between the two views of Page Report Studio. Unavailable when [Show Link of Basic/Interactive View](https://devnet.logianalytics.com/hc/en-us/articles/1500009691802-Customizing-Page-Report-Studio-Profile#View) is unchecked in the Page Report Studio profile. |
|  | Back button | Goes back to the previous level in the report chain, which is created when performing the going or linking-to-report action on a report tab. |
|  | Next button | Goes forward to the next level in the report chain, which is created when performing the going or linking-to-report action on a report tab. |
|  | Go To Drop-down List | When you perform the going or linking-to-report actions on a report tab, a report chain is created. This drop-down list lists the original report and the reports you have just visited within the report chain. The item checked in the drop-down list is the currently opened report. Select an unchecked item and you will be directed to that report. |
|  | More Commands | When the Page Report Studio window is not maximized in Interactive View mode, the button will be displayed on the toolbar, by selecting which you can get all the other toolbar commands the small window hasn't enough space for. |
|  | Language button | Specifies the language in which to display the report if it is an [NLS report](https://devnet.logianalytics.com/hc/en-us/articles/1500009718081-NLS-at-Report-Level). Available only when [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#NLS) is checked in the server profile. |
| Shortcut Menu | Filter | Provides submenu items for filtering the data in a banded object/table or removing the filtering. |
|  | Sort | Provides submenu items for sorting records on the selected field in ascending/descending order, or removing the sorting. |
|  | Drill Down | Drills data to a lower group according to predefined hierarchies. |
|  | Drill To | Enables you to obtain a different view of data by switching among groups. |
|  | Drill to By Value | Allows you to filter data based on groups while also obtaining a more detailed view of the data. |
|  | Drill Up | Drills data to a higher group according to predefined hierarchies. |
|  | Go To | Goes to any group to show its record information. |
|  | Go Up | Goes up one group level to show the records of a higher-level group. |
|  | Go Down | Goes down one group level to show the records of a child group. |
|  | Go to Detail | Goes to the details of a group. |
|  | Conditional Formatting | Enables you to [add conditional format](https://devnet.logianalytics.com/hc/en-us/articles/1500009691622-Adding-Conditional-Formats-to-Fields) to the currently selected field. |
|  | Search | Shows the Search dialog for you to search the report result for some text. |
|  | Query Filter | Applies a filter to the business view used by the specified data component. |
|  | Refresh | Re-fetches data of the specified data component. |
|  | Properties | Shows a dialog for you to define the object's properties. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718101-Page-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718121-Creating-Page-Reports)
