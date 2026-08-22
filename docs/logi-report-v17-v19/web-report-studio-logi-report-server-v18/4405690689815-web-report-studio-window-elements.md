---
title: "Web Report Studio Window Elements"
id: 4405690689815
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690689815-Web-Report-Studio-Window-Elements
updated_at: 2022-01-27T07:59:53Z
---

# Web Report Studio Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684047895-Creating-and-Using-Web-Report-Page-Templates)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684035223-Editing-Web-Reports-in-Web-Report-Studio)

# Web Report Studio Window Elements

This topic describes the full window elements in Web Report Studio and how you can use them.

You can determine the options available in Web Report Studio by the feature profile that you selected as the default profile in the Customize Profile > Web Report Studio > Features tab of the profile page and the property settings in the Customize Profile > Web Report Studio > Properties tab. Profile has the higher priority. For more information, see [Customizing Web Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/4405684049047-Customizing-Web-Report-Studio-Profile).

The window elements of Web Report Studio vary with its two modes: View Mode and Edit Mode. The following table introduces the full UI elements based on the **Edit Mode**. The shortcut menu options vary with the objects you right-click, and the table only list some typical items.

| Menu/Toolbar | Option/Button | Description |
| --- | --- | --- |
| Menu > File | New Report | Select to [create a new web report](https://devnet.logianalytics.com/hc/en-us/articles/4405690684439-Creating-Web-Reports-Using-the-Wizard) based on an existing business view. |
| Open | Select to open a web report. |
| Save | Select to save the changes that you made to the current web report. If the current web report is a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/4405683936279-Sharing-Web-Reports), Server enables the option only when the report owner sets it as editable. |
| Save As | Select to [save a copy of the web report](https://devnet.logianalytics.com/hc/en-us/articles/4405684044439-Saving-a-Web-Report) or the web report template to server resources. Server disables the option if the current web report is a shared report. |
| Export | Select to [export the report](https://devnet.logianalytics.com/hc/en-us/articles/4405690685335-Exporting-Printing-the-Web-Report-Result) to disk or version in various formats. |
| Page Setup | Select to configure the [report page settings](https://devnet.logianalytics.com/hc/en-us/articles/4405690686231-General-Operations-in-Web-Report#Page). |
| Print | Select to [print the web report](https://devnet.logianalytics.com/hc/en-us/articles/4405690685335-Exporting-Printing-the-Web-Report-Result) in the Print dialog box. |
| Share | Select to [share the current report.](https://devnet.logianalytics.com/hc/en-us/articles/4405690686231-General-Operations-in-Web-Report#Share)Server enables the option when you own the report and already saved it before and it is not a shared report. |
| Exit | Select to close the current web report and exit Web Report Studio. |
| Menu > Edit | Undo | Select to undo the last operation. |
| Redo | Select to reverse the operation of **Undo**. |
| Delete | Select to delete the selected object. |
| Wizard | Select to open the wizard to edit the selected table, crosstab, or chart. |
| Query Filter | Select to [apply a filter to the business view](https://devnet.logianalytics.com/hc/en-us/articles/4405684038423-Applying-Filters-in-Web-Report) used by a data component. |
| Filter | Select to [filter the report records](https://devnet.logianalytics.com/hc/en-us/articles/4405684038423-Applying-Filters-in-Web-Report) according to the filter criteria you specify. |
| [On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/4405684038423-Applying-Filters-in-Web-Report#OnScreen) | Select one of the following:  * **Save as Default**  Select to save the current on-screen filter values as the user defined default values for the report and for the user. Server disables this menu item when the current on-screen filter values are the same as the default values. * **Restore to Default**  Select to restore to the default on-screen filter values. Server disables this menu item when current on-screen filter values are the same as the default values. * **Clear Default**  Select to clear user defined default on-screen filter values. Server disables this menu item when there are no user defined default values.   The option is available when the administrator did not clear [Enable Setting Default On-screen Filter Values For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#OnScreenFilter) in the server profile. |
| To Chart | Select to [convert a crosstab into a chart](https://devnet.logianalytics.com/hc/en-us/articles/4405684043031-Manipulating-Data-Components-in-Web-Report#CrosstabConvertToChart). |
| To Crosstab | Select to [convert a chart into a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/4405684043031-Manipulating-Data-Components-in-Web-Report#ChartToCrosstab). |
| Rotate Crosstab | Select to rotate a crosstab to exchange its axes to create a different view of the crosstab. |
| Report Body Properties | Select to define the [properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683874071-Report-Body-Properties) of the report body. |
| Bind Data | Select to [bind a data source](https://devnet.logianalytics.com/hc/en-us/articles/4405690687511-Making-Simple-Modifications-to-Web-Report-Components#Formula) to the web report. |
| Use Wizard | Select to create web reports using the [standard wizard way](https://devnet.logianalytics.com/hc/en-us/articles/4405684031639-Web-Report-Studio-Server-v18#Way). |
| Unhide Components | Select to show the components you hid. |
| Style | [Select a style to apply to](https://devnet.logianalytics.com/hc/en-us/articles/4405684045591-Applying-CSS-Styles-in-Web-Report) the selected components or the whole report. |
| Menu > View | Inspector | Select to show or hide the **Inspector** panel, which lists all the objects in the report in a tree structure with their properties. You can select any object in the tree to [edit its properties](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel). |
| Editing Marks | Select to show or hide editing marks (dashed outlines for objects and report body). If you clear the option, Server does not show the editing mark when a report object receives focus, and you cannot move or resize report objects. |
| Refresh | Select to run the web report using previously provided parameters and fetch the data again. |
| Menu > Format | Font | Select to update the font format of the text in a label or field. |
| Merge | Select to merge the selected tabular cells that forms a rectangle into one cell. |
| Split | Select to split the selected tabular cell into the specified number of rows and columns. |
| Menu > Language |  | Select the language in which to display the report. Available only when you selected [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#NLS) in the server profile. |
| Menu > Help | User's Guide | Select to open the Web Report Studio user documentation. |
| Logi Report Home Page | Select to access the Logi Analytics Home Page. |
| Technical Support | Select to reach Logi Analytics Technical Support. |
| About Web Report Studio | Select to view the product information about Web Report Studio. |
| Standard Toolbar | New Report button New Report | Select to create a new web report based on an existing business view. |
| Open button Open | Select to open a web report. |
| Save button Save | Select to save the changes that you made to the current web report. If the current web report is a shared report, Server enables the button only when the report owner sets it as editable. |
| Save As button Save As | Select to save a copy of the web report or the web report template to server resources. Server disables the option if the current web report is a shared report. |
| Export button Export | Select to export the report to disk or version in various formats. |
| Print button Print | Select to print the web report in the Print dialog box. |
| Page Setup button Page Setup | Select to configure the report page settings. |
| Share button Share | Select to share the current report. Server enables the option when you own the report and already saved it before and it is not a shared report. |
| Refresh button Refresh | Select to run the web report using previously provided parameters and fetch the data again. |
| Undo button Undo | Select to undo the last operation. |
| Redo button Redo | Select to reverse the operation of **Undo**. |
| Help buttonQuery Filter | Select to apply a filter to the business view used by a data component. |
| Filter button Filter | Select to filter the report records according to the filter criteria you specify. |
| Open Responsive Mode button/Close Responsive Mode button Open/Close Responsive Mode | Select to open or close [Responsive View](https://devnet.logianalytics.com/hc/en-us/articles/4405690686231-General-Operations-in-Web-Report#Responsive) in which report components are responsive to the browser window. Available in View Mode only. |
| Delete button Delete | Select to delete the selected object. |
| Show Hidden Objects button Show Hidden Objects | Select to [show the hidden banded panels](https://devnet.logianalytics.com/hc/en-us/articles/4405684043031-Manipulating-Data-Components-in-Web-Report#ShowHiddenObjects). Server displays the button when you are editing the template of a banded object. |
| Language button Language | Select the language in which to display the report if it is an [NLS report](https://devnet.logianalytics.com/hc/en-us/articles/4405683948567-NLS-at-Report-Level). Server displays the option only when you selected [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#NLS) in the server profile. |
| Exit button Exit | Select to close the current web report and exit Web Report Studio. |
| Quick Format Toolbar | Font button Font | Select the font format of the text in a label or field. |
| Background Color button Background Color | Select to change the background color of the text in a label or field. |
| Align button Align | Select to make the text in a label or field left, center, or right aligned. |
| Merge button Merge | Select to merge the selected tabular cells that form a rectangle into one cell. |
| Split button Split | Select to split the selected tabular cell vertically or horizontally. |
| Context Toolbar for Table | Show/Hide Detail button Show/Hide Detail | Select to hide or show detail columns. |
| Add/Remove Group button Add/Remove Group | Select to add or remove the selected field as a group. |
| Show/Hide Summary button Show/Hide Summary | Select to show or hide the selected summary field. |
| Aggregate On button Aggregate On | Select to create a new summary directly based on the field bound with the selected table detail column. |
| Hide button Hide | Select to hide the selected column. |  |
| Context Toolbar for Crosstab | Rotate Crosstab button Rotate Crosstab | Select to rotates a crosstab to exchange its axes to create a different view of the crosstab. |
| Context Toolbar for Chart | Swap Chart Groups button Swap Chart Groups | Select to switch data between the category and series axes, or between the category and value axes if there is no field on the series axis. |
| Chart Type button Chart Type | Select a new chart type for the chart. |
| Chart Options button Chart Options | Select the layout of the chart. |
| More Commands | Full Data button/Partial Data button | Select the [data mode of the report](https://devnet.logianalytics.com/hc/en-us/articles/4405690686231-General-Operations-in-Web-Report#DataMode). |
| Edit Mode button/View Mode button | Select to switch from one mode of Web Report Studio to another. Server displays the option when you did not clear [Show Link of View/Edit Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405684049047-Customizing-Web-Report-Studio-Profile#Mode) in the Web Report Studio profile. |
| Panels | Resources panel | The Resources panel lists all the available resources for the object you selected. When you selected a data component, Server enables the **Sort**Sort button and **Search**Search button buttons on the title bar of the panel. For more information about the two buttons, see the description about Sort under [Details Tab](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties#Display). |
| Components panel | The Components panel lists all the available components that you can insert into reports. |
| Parameters panel | The Parameters panel lists all the parameters used by the current report. Server displays the panel when the current report uses parameters. |
| Filter panel | [Specify the criteria to filter the data field](https://devnet.logianalytics.com/hc/en-us/articles/4405684038423-Applying-Filters-in-Web-Report#Panel). You can also remove or change existing filters. |
| "Go To" Filter panel | After you perform the go-to-by-value or go-down actions, Server displays the panel showing the filter created by the actions. You can then select in a table, crosstab, or chart to show this panel for the component. |
| Inspector panel | The Inspector panel lists all the objects in the report in a tree structure with their properties. |
| Visualization Toolbar | Wizard button Wizard | Select to re-enter the wizard of the current data component. |
| Edit Template button Edit Template | Select to enter the template editor to edit the current banded object. |
| Convert or drag to add table button Convert or drag to add Table | Select to convert the current data component to a table, or drag to add a table into the report. |
| Convert or drag to add crosstab button Convert or drag to add Crosstab | Select to convert the current data component to a crosstab, or drag to add a crosstab into the report. |
| Convert or drag to add banded object button Convert or drag to add Banded Object | Select to convert the current table to a banded object, or drag to add a banded object into the report. |
| [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/4405684033815-Components-Supported-in-Web-Reports#Chart) | Select to convert the current data component to a specific chart type, or drag to add the type of chart into the report. |
| KPI button Drag to add KPI | Drag to add a KPI into the report. |
| More button More | Select to show more icons that the visualization toolbar cannot present. |
| Shortcut Menu | Query Filter | Select to filter the business view used by the selected data component according to the filter criteria you specify. |
| Show | Select to show the selected fields. |
| Apply Style | Select a style to apply to the selected component. |
| Delete | Select to delete the selected object. |
| Autofit | Select to adjust the width of table and crosstab fields according to the contents. |
| Hide | Select to hide the selected object. |
| Filter | The Filter menu provides items for filtering the data in the selected component or removing existing filters. |
| Sort | The Sort menu provides items for sorting records on the selected field in ascending/descending order, or removing the sort. |
| Edit Detail Table | Select to [edit the detail table](https://devnet.logianalytics.com/hc/en-us/articles/4405683810071-Edit-Detail-Table-Dialog-Box-Properties) to define the detail fields of the summary. |
| Go to Detail | Select to [go to the detailed information](https://devnet.logianalytics.com/hc/en-us/articles/4405684039575-Going-Through-Web-Report-Data#Go-to-detail) of the selected summary. |
| Link/Edit Link | Select to [link the selected object to a report, URL, email, or Blob data type field](https://devnet.logianalytics.com/hc/en-us/articles/4405684041879-Adding-Links-in-Web-Report). |
| Conditional Formatting | Select to [add conditional formatting](https://devnet.logianalytics.com/hc/en-us/articles/4405684036247-Adding-Conditional-Formats-to-Data-Fields-in-Web-Report) to the selected field. |
| Go Down | Select to go from a group which is a non-bottom level in a predefined hierarchy to the one-level-lower group while applying the current selected value as a filter condition. For more information, see [Go-down](https://devnet.logianalytics.com/hc/en-us/articles/4405684039575-Going-Through-Web-Report-Data#Go-down). |
| Go Up | Select to go from a group which is a non-top level in a predefined hierarchy to the one-level-higher group. For more information, see [Go-up](https://devnet.logianalytics.com/hc/en-us/articles/4405684039575-Going-Through-Web-Report-Data#Go-up). |
| Go To | Select to [jump to any group](https://devnet.logianalytics.com/hc/en-us/articles/4405684039575-Going-Through-Web-Report-Data#Go-to) to show its record information. |
| Go to By Value | Select to [go to any group with the current group value as a filter](https://devnet.logianalytics.com/hc/en-us/articles/4405684039575-Going-Through-Web-Report-Data#Go-to-by-value) to show its record information. |
| Select | Select the corresponding object. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684047895-Creating-and-Using-Web-Report-Page-Templates)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684035223-Editing-Web-Reports-in-Web-Report-Studio)
