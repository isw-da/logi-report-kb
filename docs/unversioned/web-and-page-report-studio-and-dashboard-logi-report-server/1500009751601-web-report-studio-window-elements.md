---
title: "Web Report Studio Window Elements"
id: 1500009751601
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751601-Web-Report-Studio-Window-Elements
updated_at: 2021-07-25T07:18:33Z
---

# Web Report Studio Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724682-Creating-Web-Reports-Using-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724702-Editing-Web-Reports-in-Web-Report-Studio)

# Web Report Studio Window Elements

The options available in Web Report Studio are determined by the feature profile that is selected as the default profile in the Customize Profile > Web Report Studio > Features tab of the profile page and the property settings in the Customize Profile > Web Report Studio > Properties tab (profile has the higher priority). For additional information, see [Customizing Web Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009724902-Customizing-Web-Report-Studio-Profile).

The window elements of Web Report Studio vary with its two modes: View Mode and Edit Mode. The following table introduces the full UI elements based on Edit Mode. The shortcut menu contents vary with the objects you right-click and the table only lists some typical items.

| Menu/Toolbar | Option/Button | Description |
| --- | --- | --- |
| File | New Report | [Creates a new web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009724682-Creating-Web-Reports-Using-Wizard) based on an existing business view. |
|  | Open | Opens a web report. |
|  | Save | Saves the changes of the current web report. If the current web report is a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports), the option is enabled only when the report owner sets it as editable. |
|  | Save As | [Saves a copy of the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009751541-Saving-the-Report) or the report template in the current web report to server resources. Disabled if the current web report is a shared report. |
|  | Export | [Exports the report result](https://devnet.logianalytics.com/hc/en-us/articles/1500009724762-Exporting-Printing-the-Report-Result) to disk or version in various formats. |
|  | Page Setup | Configures the [report page settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009724782-General-Operations-in-a-Report#Page). |
|  | Print | Displays the Print dialog box for [printing the web report result](https://devnet.logianalytics.com/hc/en-us/articles/1500009724762-Exporting-Printing-the-Report-Result). |
|  | Share | [Share the current report.](https://devnet.logianalytics.com/hc/en-us/articles/1500009724782-General-Operations-in-a-Report#Share)Enabled when the report is owned by the current user and already saved before and is not a shared report. |
|  | Exit | Closes the current web report and exits Web Report Studio. |
| Edit | Undo | Undoes the last operation. |
|  | Redo | Reverses the operation of Undo. |
|  | Delete | Deletes the selected object. |
|  | Wizard | Opens the report wizard for you to edit the selected table, crosstab or chart. |
|  | Query Filter | [Applies a filter to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters)used by the specified data component. |
|  | Filter | [Filters the report records](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters) according to the filter criteria you specify. |
|  | [On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters#OnScreen) | The option is unavailable when [Enable Setting Default On-screen Filter Values For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#OnScreenFilter) is not selected in the server profile.  * **Save as Default**  Saves the current on-screen filter values as the user defined default values for the report and for the user. This menu item is disabled when the current on-screen filter values are the same as the default values. * **Restore to Default**  Restores to the default on-screen filter values. This menu item is disabled when current on-screen filter values are the same as the default values. * **Clear Default**  Clears user defined default on-screen filter values. This menu item is disabled when there are no user defined default values. |
|  | To Chart | [Converts a crosstab into a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components#ToChart). |
|  | To Crosstab | [Converts a chart into a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components#ToCrosstab). |
|  | Rotate Crosstab | Rotates a crosstab to exchange the axes on the crosstab in order to create a different view of the crosstab. |
|  | Report Body Properties | Defines [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749281-Report-Body-Properties) of the report body. |
|  | Bind Data | Specifies to [bind a data source](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components#Formula) to the web report. |
|  | Use Wizard | Specifies whether to work with web reports in the [standard wizard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009724642-Web-Report-Studio#Way). |
|  | Unhide Components | Shows the hidden components you specify. |
|  | Style | [Applies a style](https://devnet.logianalytics.com/hc/en-us/articles/1500009724882-Applying-CSS-Styles) to the selected components or the whole report. |
| View menu | Inspector | Shows or hides the Inspector panel, which lists all the objects in the report in a tree structure with their properties. You can select any object in the tree to [edit its properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009750621-Web-Report-Object-Property-Reference). |
|  | Editing Marks | Shows or hides editing marks (dashed outlines for objects and report body). If the option is unselected, the editing mark will not be shown when a report object receives focus, and report objects cannot be moved or resized. |
|  | Refresh | Runs the web report using previously provided parameters. The Refresh operation fetches the data again. |
| Format | Font | Specifies the font format of the selected text. Available only when a label or field is selected. |
|  | Merge | Merges the selected tabular cells into one. |
|  | Split | Splits the selected tabular cell into the specified number of rows and columns. |
| Language |  | Allows you to specify the language in which to display the report. Available only when [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#NLS) is selected in the server profile. |
| Help | User's Guide | Opens the Web Report Studio user documentation. |
|  | Logi Report Home Page | Connects to Logi Report Home Page. |
|  | Technical Support | Accesses Logi Analytics Technical Support. |
|  | About Web Report Studio | Shows product information about Web Report Studio. |
| Standard Toolbar | New Report button New Report | Creates a new web report based on an existing business view. |
|  | Open button Open | Opens a web report. |
|  | Save button Save | Saves the changes of the current web report. If the current web report is a shared report, the button is enabled only when the report owner sets it as editable. |
|  | Save As button Save As | Saves a copy of the web report or the report template in the current web report to server resources. Disabled if the current web report is a shared report. |
|  | Export button Export | Exports the report result to disk or version in various formats. |
|  | Print button Print | Displays the Print dialog box for printing the web report result. |
|  | Page Setup button Page Setup | Configures the report page settings. |
|  | Share button Share | Share the current report. Enabled when the report is owned by the current user and already saved before and is not a shared report. |
|  | Refresh button Refresh | Runs the web report using previously provided parameters. The Refresh operation fetches the data again. |
|  | Undo button Undo | Undoes the last operation. |
|  | Redo button Redo | Reverses the operation of Undo. |
|  | Help buttonQuery Filter | Applies a filter to the business view used by the specified data component. |
|  | Filter button Filter | Filters the report records according to the filter criteria you specify. |
|  | Open Responsive Mode button/Close Responsive Mode button Open/Close Responsive Mode | Specifies whether report components are [responsive to the browser window](https://devnet.logianalytics.com/hc/en-us/articles/1500009724782-General-Operations-in-a-Report#Responsive). Available in View Mode only. |
|  | Delete button Delete | Deletes the selected object. |
|  | Show Objects button Show Objects | Specifies [which objects to show](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components#Formula) in the report. |
|  | Language button Language | Specifies the language in which to display the report if it is an [NLS report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level). Available only when [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#NLS) is selected in the server profile. |
|  | Exit button Exit | Closes the current web report and exits Web Report Studio. |
| Quick Format Toolbar | Font button Font | Specifies the font format of the selected text. Available only when a label or field is selected. |
|  | Background Color button Background Color | Changes the background color of the selected text. Available only when a label or field is selected. |
|  | Align button Align | Makes the selected text left, center or right aligned. Available only when a label or field is selected. |
|  | Merge button Merge | Merges the selected tabular cells into one. |
|  | Split button Split | Splits the selected tabular cell vertically or horizontally. |
| Context Toolbar for Table | Show/Hide Detail button Show/Hide Detail | Hides or shows the detail columns you specify. |
|  | Add/Remove Group button Add/Remove Group | Specifies whether to add or remove the selected field as a group. |
|  | Show/Hide Summary button Show/Hide Summary | Specifies whether to show or hide the selected summary field. |
|  | Hide button Hide | Hides the selected column. |
|  | Aggregate On button Aggregate On | Creates a new summary directly based on the field bound with the table detail column. |
| Context Toolbar for Crosstab | Rotate Crosstab button Rotate Crosstab | Rotates a crosstab to exchange the axes on the crosstab in order to create a different view of the crosstab. |
| Context Toolbar for Chart | Swap Chart Groups button Swap Chart Groups | Specifies whether to switch data between the category and series axes, or between the category and value axes if there is no field on the series axes. |
|  | Chart Type button Chart Type | Lists all available chart types for you to change the type of the chart. |
|  | Chart Options button Chart Options | Lists more options for you to specify the layout of the chart. |
| More Commands | Full Data button/Partial Data button | Specifies the [data mode of the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009724782-General-Operations-in-a-Report#DataMode). |
|  | Edit Mode button/View Mode button | Lists the two modes of Web Report Studio to allow you to switch from one mode to another. Unavailable if [Show Link of View/Edit Mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009724902-Customizing-Web-Report-Studio-Profile#Mode) is unselected in the Web Report Studio profile. |
| Panel | Parameters | Lists all the parameters used by the current report. It is available when the current report uses parameters. |
|  | Resources | Lists all the available resources. When a data component is selected, the Sort Sort button and Search Search button buttons on the title bar of the panel will be enabled. For the usage about the two buttons, see the description of Sort under [Details Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009722522-Web-Report-Wizard#Display). |
|  | Components | Lists all the available components that can be inserted into reports. |
|  | Filter | [Specifies the criteria to filter the data field](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters#Panel). You can also remove or change existing filters. |
|  | "Go To" Filter | After you perform the go-to-by-value or go-down actions, Report Server displays the panel showing the filter created by the actions. You can also select in a table, crosstab, or chart to show this panel for the component. |
|  | Inspector | Lists all the objects in the report in a tree structure with their properties. |
| Visualization Toolbar | Wizard button Wizard | Re-enters the wizard of the current data component. |
|  | Edit Template button Edit Template | Enters the template editor to edit the current banded object. |
|  | Convert or drag to add table button Convert or drag to add table | Converts the current data component to a table, or drag a table into the report. |
|  | Convert or drag to add crosstab button Convert or drag to add crosstab | Converts the current data component to a crosstab, or drag a crosstab into the report. |
|  | Convert or drag to add banded object button Convert or drag to add banded object | Converts the current table to a banded object, or drag a banded object into the report. |
|  | [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500009724662-Components-Supported-in-Web-Reports#Chart) | Converts the current data component to a specific chart type, or drag the chart type into the report. |
|  | More button More | Shows more icons that the visualization toolbar cannot present. |
| Shortcut Menu | Query Filter | Filters the business view used by the selected data component according to the filter criteria you specify. |
|  | Show | Shows the selected fields. |
|  | Apply Style | Applies a style to the selected component. |
|  | Delete | Deletes the selected object. |
|  | Autofit | Adjusts the width of table and crosstab fields according to the contents. |
|  | Hide | Hides the selected object. |
|  | Filter | Provides submenu items for filtering the data in the selected component or remove existing filters. |
|  | Sort | Provides submenu items for sorting records on the selected field in ascending/descending order, or remove the sort. |
|  | Edit Detail Table | [Edits the detail table](https://devnet.logianalytics.com/hc/en-us/articles/1500009748241-Edit-Detail-Table) to define the detail fields of the summary. |
|  | Go to Detail | [Goes to the detailed information](https://devnet.logianalytics.com/hc/en-us/articles/1500009724802-Going-Through-the-Report-Data#Go-to-detail) of the selected summary. |
|  | Link/Edit Link | [Links the selected object to a report, URL, e-mail or Blob data type field](https://devnet.logianalytics.com/hc/en-us/articles/1500009724822-Adding-Links-in-a-Report). |
|  | Conditional Formatting | [Adds some conditional formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009724722-Adding-Conditional-Formats-to-Data-Fields) to the currently selected field. |
|  | Go Down | Goes from a group which is non-bottom level in a predefined hierarchy to the one-level-lower group while applying the current selected value as a filter condition. See [Go-down](https://devnet.logianalytics.com/hc/en-us/articles/1500009724802-Going-Through-the-Report-Data#Go-down) for details. |
|  | Go Up | Goes from a group which is non-top level in a predefined hierarchy to the one-level-higher group. See [Go-up](https://devnet.logianalytics.com/hc/en-us/articles/1500009724802-Going-Through-the-Report-Data#Go-up) for details. |
|  | Go To | [Goes to any group](https://devnet.logianalytics.com/hc/en-us/articles/1500009724802-Going-Through-the-Report-Data#Go-to) to show its record information. |
|  | Go to By Value | [Goes to any group with the current group value as a filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009724802-Going-Through-the-Report-Data#Go-to-by-value) to show its record information. |
|  | Select | Make the corresponding object selected. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724682-Creating-Web-Reports-Using-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724702-Editing-Web-Reports-in-Web-Report-Studio)
