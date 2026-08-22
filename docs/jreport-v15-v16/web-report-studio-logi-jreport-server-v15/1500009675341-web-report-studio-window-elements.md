---
title: "Web Report Studio Window Elements"
id: 1500009675341
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675341-Web-Report-Studio-Window-Elements
updated_at: 2021-07-24T20:53:34Z
---

# Web Report Studio Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675141-Standard-Way-of-Report-Creation-Using-Wizard)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675161-Editing-Web-Reports-in-Web-Report-Studio)

# Web Report Studio Window Elements

The options available on the Web Report Studio window are determined by the feature profile that is selected as the default profile in the Profile > Customize Profile > Web Report Studio > Features tab and the property settings in the Profile > Customize Profile > Web Report Studio > Properties tab (profile has the higher priority). For additional information, see [Customizing Web Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009675361-Customizing-Web-Report-Studio-Profile).

The window elements of Web Report Studio vary with its two modes: View Mode and Edit Mode. The following table introduces the full UI elements based on Edit Mode. The shortcut menu contents vary with the objects you right-click and the table only lists some typical items.

| Menu/Toolbar | Button | Tool Name | Description |
| --- | --- | --- | --- |
| File |  | New Report | [Creates a new web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009675141-Standard-Way-of-Report-Creation-Using-Wizard) based on an existing business view. |
|  |  | Open | Opens a web report. |
|  |  | Save | Saves the changes of the current web report. |
|  |  | Save As | [Saves a copy of the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009650362-Saving-the-Report) or the report template in the current web report to server resources. |
|  |  | Export | [Exports the report result](https://devnet.logianalytics.com/hc/en-us/articles/1500009650262-Exporting-Printing-the-Report-Result) to disk or version in various formats. |
|  |  | Page Setup | Configures the [report page settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009675201-General-Operations-in-Reports#Page). |
|  |  | Print | Displays the Print dialog for [printing the web report result](https://devnet.logianalytics.com/hc/en-us/articles/1500009650262-Exporting-Printing-the-Report-Result). |
|  |  | Exit | Closes the current web report and exits Web Report Studio. |
| Edit |  | Undo | Undoes the last operation. |
|  |  | Redo | Reverses the operation of Undo. |
|  |  | Delete | Deletes the selected object. |
|  |  | Wizard | Opens the report wizard for you to edit the selected table, crosstab or chart. |
|  |  | Filter | [Filters the report records](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters) according to the filter criteria you specify. |
|  |  | [On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters#OnScreen) | The option is available when [Enable Setting Default On-screen Filter Values For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#OnScreenFilter) is selected in the Profile > Customize Server Preferences > Advanced tab.  * **Save as Default**  Saves the current on-screen filter values as the user-defined default values for the report and for the user. This menu item is disabled when the current on-screen filter values are the same as the default values. * **Restore to Default**  Restores to the default on-screen filter values. This menu item is disabled when current on-screen filter values are the same as the default values. * **Clear Default**  Clears user-defined default on-screen filter values. This menu item is disabled when there are no user-defined default values. |
|  |  | To Chart | [Converts a crosstab into a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components#ToChart). |
|  |  | To Crosstab | [Converts a chart into a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components#ToCrosstab). |
|  |  | Rotate Crosstab | Rotates a crosstab to exchange the axes on the crosstab in order to create a different view of the crosstab. |
|  |  | Report Body Properties | Defines [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009672461-Report-Body-Properties) of the report body. |
|  |  | Bind Data | Specifies to [bind a data source](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components#Formula) to the web report. |
|  |  | Use Wizard | Specifies whether to work with web reports in the [standard wizard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio#Way). |
|  |  | Unhide Components | Shows the hidden components you specify. |
|  |  | Style | [Applies a style](https://devnet.logianalytics.com/hc/en-us/articles/1500009675301-Applying-CSS-Styles) to the selected components or the whole report. |
| View menu |  | Inspector | Shows or hides the Inspector panel, which lists all the objects in the report in a tree structure with their properties. You can select any object in the tree to [edit its properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009649522-Web-Report-Object-Property-Reference). |
|  |  | Editing Marks | Shows or hides editing marks (dashed outlines for objects and report body). If the option is unselected, the editing mark will not be shown when a report object receives focus, and report objects cannot be moved or resized. |
|  |  | Refresh | Runs the web report using previously provided parameters. The Refresh operation fetches the data again. |
| Format |  | Font | Specifies the font format of the selected text. Available only when a label or field is selected. |
|  |  | Merge | Merges the selected tabular cells into one. |
|  |  | Split | Splits the selected tabular cell into the specified number of rows and columns. |
| Language |  |  | Allows you to specify the language in which to display the report. Available only when [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#NLS) is checked in the Profile > Customize Server Preferences > Advanced tab. |
| Help |  | User's Guide | Opens the Web Report Studio User's Guide. |
|  |  | Logi JReport Home Page | Connects to Logi JReport Home Page. |
|  |  | Technical Support | Accesses Jinfonet Technical Support. |
|  |  | About Web Report Studio | Shows product information about Web Report Studio. |
| Standard Toolbar |  | New Report | Creates a new web report based on an existing business view. |
|  |  | Open | Opens a web report. |
|  |  | Save | Saves the changes of the current web report. |
|  |  | Save As | Saves a copy of the web report or the report template in the current web report to server resources. |
|  |  | Export | Exports the report result to disk or version in various formats. |
|  |  | Print | Displays the Print dialog for printing the web report result. |
|  |  | Page Setup | Configures the report page settings. |
|  |  | Refresh | Runs the web report using previously provided parameters. The Refresh operation fetches the data again. |
|  |  | Undo | Undoes the last operation. |
|  |  | Redo | Reverses the operation of Undo. |
|  |  | Filter | Filters the report records according to the filter criteria you specify. |
|  | / | Open/Close Responsive Mode | Specifies whether report components are [responsive to the browser window](https://devnet.logianalytics.com/hc/en-us/articles/1500009675201-General-Operations-in-Reports#Responsive). Available in View Mode only. |
|  |  | Delete | Deletes the selected object. |
|  |  | Show Objects | Specifies [which objects to show](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components#Formula) in the report. |
|  |  | Language | Specifies the language in which to display the report if it is an [NLS report](https://devnet.logianalytics.com/hc/en-us/articles/1500009649142-NLS-at-Report-Level). Available only when Enable NLS is checked in the Profile > Customize Server Preferences > Advanced tab. |
|  |  | Exit | Closes the current web report and exits Web Report Studio. |
| Quick Format Toolbar |  | Font | Specifies the font format of the selected text. Available only when a label or field is selected. |
|  |  | Background Color | Changes the background color of the selected text. Available only when a label or field is selected. |
|  |  | Align | Makes the selected text left, center or right aligned. Available only when a label or field is selected. |
|  |  | Merge | Merges the selected tabular cells into one. |
|  |  | Split | Splits the selected tabular cell vertically or horizontally. |
| Context Toolbar for Table |  | Show/Hide Detail | Hides or shows the detail columns you specify. |
|  |  | Add/Remove Group | Specifies whether to add or remove the selected field as a group. |
|  |  | Show/Hide Summary | Specifies whether to show or hide the selected summary field. |
|  |  | Hide | Hides the selected column. |
|  |  | Aggregate On | Creates a new summary directly based on the field bound with the table detail column. |
| Context Toolbar for Crosstab |  | Rotate Crosstab | Rotates a crosstab to exchange the axes on the crosstab in order to create a different view of the crosstab. |
| Context Toolbar for Chart |  | Swap Chart Groups | Specifies whether to switch data between the category and series axes, or between the category and value axes if there is no field on the series axes. |
|  |  | Chart Type | Lists all available chart types for you to change the type of the chart. |
|  |  | Chart Options | Lists more options for you to specify the layout of the chart. |
| More Commands | / | Data Mode | Specifies the [data mode of the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009675201-General-Operations-in-Reports#DataMode). |
|  | / |  | Lists the two modes of Web Report Studio to allow you to switch from one mode to another. Unavailable if [Show Link of View/Edit Mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009675361-Customizing-Web-Report-Studio-Profile#Mode) is unchecked in the Web Report Studio profile. |
| Panel |  | Parameters | Lists all the parameters used by the current report. It is available when the current report uses parameters. |
|  |  | Resources | Lists all the available resources. When a data component is selected, the Sort  and Search  buttons on the title bar of the panel will be enabled. For the usage about the two buttons, see [*Web Report Wizard*](https://devnet.logianalytics.com/hc/en-us/articles/1500009648042-Web-Report-Wizard#Display). |
|  |  | Components | Lists all the available components that can be inserted into reports. |
|  |  | Filter | [Specifies the criteria to filter the data field](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters#Panel). You can also remove or change existing filters. |
|  |  | "Go To" Filter | After you perform the go-to-by-value or go-down actions, the panel is displayed showing the filter created by the actions. You can also select in a table, crosstab, or chart to show this panel for the component. |
|  |  | Inspector | Lists all the objects in the report in a tree structure with their properties. |
| Visualization Toolbar |  | Wizard | Re-enters the wizard of the current data component. |
|  |  | Convert or drag to add table | Converts the current data component to a table, or drag a table into the report. |
|  |  | Convert or drag to add crosstab | Converts the current data component to a crosstab, or drag a crosstab into the report. |
|  |  | [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500009650202-Components-Supported-in-Web-Reports#Chart) | Converts the current data component to a specific chart type, or drag the chart type into the report. |
|  |  | More | Shows more icons that the visualization toolbar cannot present. |
| Shortcut Menu |  | Show | Shows the selected fields. |
|  |  | Apply Style | Applies a style to the selected component. |
|  |  | Delete | Deletes the selected object. |
|  |  | Autofit | Adjusts the width of table and crosstab fields according to the contents. |
|  |  | Hide | Hides the selected object. |
|  |  | Filter | Provides submenu items for filtering the data in the selected component or remove existing filters. |
|  |  | Sort | Provides submenu items for sorting records on the selected field in ascending/descending order, or remove the sort. |
|  |  | Edit Detail Table | [Edits the detail table](https://devnet.logianalytics.com/hc/en-us/articles/1500009671661-Edit-Detail-Table) to define the detail fields of the summary. |
|  |  | Go to Detail | [Goes to the detailed information](https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data#Go-to-detail) of the selected summary. |
|  |  | Link/Edit Link | [Links the selected object to a report, URL, e-mail or Blob data type field](https://devnet.logianalytics.com/hc/en-us/articles/1500009650322-Binding-Links-to-Objects). |
|  |  | Conditional Formatting | [Adds some conditional formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009675181-Adding-Conditional-Formats-to-Fields) to the currently selected field. |
|  |  | Go Down | Goes from a group which is non-bottom level in a predefined hierarchy to the one-level-lower group while applying the current selected value as a filter condition. See [Go-down](https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data#Go-down) for details. |
|  |  | Go Up | Goes from a group which is non-top level in a predefined hierarchy to the one-level-higher group. See [Go-up](https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data#Go-up) for details. |
|  |  | Go To | [Goes to any group](https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data#Go-to) to show its record information. |
|  |  | Go to By Value | [Goes to any group with the current group value as a filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data#Go-to-by-value) to show its record information. |
|  |  | Select | Make the corresponding object selected. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675141-Standard-Way-of-Report-Creation-Using-Wizard)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675161-Editing-Web-Reports-in-Web-Report-Studio)
