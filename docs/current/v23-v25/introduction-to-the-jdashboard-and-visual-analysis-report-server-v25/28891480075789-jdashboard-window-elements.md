---
title: "JDashboard Window Elements"
id: 28891480075789
section: "Introduction to the JDashboard and Visual Analysis Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891480075789-JDashboard-Window-Elements
updated_at: 2026-02-26T02:11:24Z
source_host: docs-report.zendesk.com
---
# 
JDashboard Window Elements 

JDashboard window elements vary with its two working modes: edit mode and view mode. This topic describes the full UI elements based on the edit mode.

The full-featured JDashboard window contains three sections: the dashboard title bar at the top, the toolbar on the left providing options for working with dashboards, and the dashboard editing area where you navigate and modify dashboards. Since you can also use JDashboard to access Visual Analysis, if your Server enables Visual Analysis, the elements in the JDashboard window have slight differences.

The default JDashboard profile provides full options. You can change the options in JDashboard by Customizing JDashboard Profile.

## 
Dashboard Title Bar

The dashboard title bar at the top contains tabs labeling the names of the dashboards that you open.

Dashboard name tabs

Each tab represents an open dashboard, and the tab name is the dashboard name.

You can perform the following operations on the tabs:

- Select a tab to activate the corresponding dashboard. 

- Rename a tab. Double-click a tab name and the name becomes editable. Type a new name, then press Enter or select outside of the input field to save the name. 

- Move a tab. Drag a tab and drop it beside a different tab to change the tab order. 

- Select x beside a dashboard name to close the dashboard. 

Add button

Select to add a new blank dashboard in the current web browser.

If Server enables Visual Analysis, you can hover over this button for one second and Server will display a drop-down menu that contains the following options:

- 
 Dashboard
  Select to create a new blank dashboard as a new tab. 

- 
 Analysis
  Select to open Visual Analysis as a new tab.

Specify the language in which you want to display the dashboard if it is an NLS dashboard. This setting is available when you have selected Enable NLS in the server profile.

## 
Toolbar

The toolbar on the left contains these buttons: 

Show/Hide Resources button

Select to show or hide the Resources panel which includes these parts:

- 
Component Library lists the library components that you created in and published from Report Designer. You can select a library component and drag it into the dashboard body.

- 
Reports lists page reports and web reports on the server resource tree. You can open any report in JDashboard or add report data components into your dashboards.

- 
Toolbox lists the objects that you can insert in your dashboards such as labels, images, special fields, filtering tools, third-party objects, and HTML components.

You can use the search bar to search for resources in a fast and convenient way. To display the search bar, select the Search button  on the Resources panel title bar.

See the following properties in the search bar:

- 
Text box

Type the text you want to search in the text box. Server lists the values that contain the matched text. 

- 
Close button

Select to close the search bar.

- 
More Options button

Select the button and Server displays more search options.
          

- 
Highlight All

Select if you want to highlight all matched text. 

- 
Match Case

Select if you want  to search for text that meets the case of the typed text. 

- Match Whole Word
Select if you want  to search for text that looks the same as the typed text.

- 
 Previous button

Select to go to the previous matched text when you have selected Highlight All.

- 
Next button

  Select to go to the next matched text when you have selected Highlight All.

 New button

Select to create a new blank dashboard with a new tab.

If Server enables Visual Analysis, selecting this button will bring out a drop-down menu that contains the following options:

- 
Dashboard
    Select to create a new blank dashboard as a new tab. 

- 
Analysis
    Select to open Visual Analysis as a new tab.

 Open button

Select to open the Open Dashboard dialog box to specify a dashboard you want to run, or the Open Document dialog box where you can select a dashboard or an analysis template to open. Which dialog box will display depends on whether Server enables Visual Analysis.

 Save button

Select to save the changes you made to the current dashboard.

Refresh button

Select to refresh the current dashboard. 

Enter Parameter Values button

Select to open the Enter Parameter Values dialog box which lists all the parameters that the dashboard uses for specifying their values. 

Clear Filters button

Select to remove all the filters from the current dashboard, including those generated via filter controls, messages, drilling and going actions, and those designed using web browsers such as Page Report Studio and Web Report Studio, except dataset filters and others designed and taking effect in Designer.

 Arrange button

Select to automatically arrange the library components in the current dashboard neatly. It is an instant action. 

Export button

Select to open the Export dialog box for exporting the library components in the current dashboard.

Print button

Select to open the Print dialog box for printing the library components in the current dashboard.

/Open/Close Responsive Mode button

Select to enable or disable the capability of automatically scaling and folding the dashboard in the view mode according to the current browser window on computers. For more information, see Responsive View.

Options button

Select this button and Server displays the following options: 

- 
New
    Select to create a new blank dashboard.
    If Server enables Visual Analysis, the New option contains a sub menu:

- 
Dashboard
          Select to create a new blank dashboard as a new tab. 

- 
Analysis
        Select to open Visual Analysis as a new tab.

- 
Open
    Select to open the Open Dashboard dialog box to specify a dashboard you want to open, or the Open Document dialog box where you can select a dashboard or an analysis template to open. Which dialog box will open depends on whether Server enables Visual Analysis.

- 
Save
    Select to save the changes you made to the current dashboard. 

- 
Save As
    Select to save the dashboard with a different name or to a new location. 

- 
Export
    Select to open the Export dialog box for exporting library components in the current dashboard.

- 
Print
    Select to open the Print dialog box for printing library components in the current dashboard.

- 
Clear Filters
    Select to remove all the filters from the current dashboard, including those generated via filter controls, messages, drilling and going actions, and those designed using web browsers such as Page Report Studio and Web Report Studio, except dataset filters and others designed and taking effect in Designer.

- 
On-screen Filter Values
    The option is available when administrators did not clear Enable Setting Default On-screen Filter Values For Dashboard in the server profile.
    
- 
Save as Default
                       Select to save the current on-screen filter values as the user defined default values for the dashboard and for you. Server disables this menu item when the current on-screen filter values are the same as the default values. 

- 
Restore to Default
                       Select to restore to the default on-screen filter values. Server disables this menu item when current on-screen filter values are the same as the default values. 

- 
Clear Default
                       Select to clear user defined default on-screen filter values. Server disables this menu item when there are no user defined default values. 

- 
Push Down
Select if you want to generate the dashboard data by applying all filters to the database.

- 
Share Parameter
    Select to open the Share Parameters Setting dialog box for sharing parameters between library components.

- 
Arrange
Select to automatically arrange the library components in the current dashboard neatly. It is an instant action.

- 
Auto Arrange
Select to automatically arranges the library components in the current dashboard neatly once the layout requires arrangement. It is a status setting. After you select it, Server keeps this option being selected and disable the Arrange option until you clear Auto Arrange. Server will save the status with the dashboard.

- 
Responsive View
Select to enable or disable the capability of automatically scaling and folding the dashboard in the view mode according to the current browser window on computers. For more information, see Responsive View.

- 
Set as Server Home
Select to set the current dashboard as the home page after you sign on to the Server Console.

- 
Language
 You can specify the language in which you want to display the dashboard. Available when you have selected Enable NLS in the server profile.

- 
Component Title Bar
Select to customize the way of showing component title bar and the icons on it. 

- 
Themes
    Select to open the Themes dialog box for selecting a theme to apply to the current dashboard.

- 
Show/Hide Dashboard Header
    Select to change the current status of the dashboard header from being shown to hidden or from being hidden to shown.

- 
Help
    Select to view the JDashboard help documentation. 

- 
Exit
    Select to exit JDashboard.

## 
Dashboard Editing Area

Dashboard view has header and body sections.

The dashboard header can contain labels, images, and special fields. 

 The dashboard body can contain library components, report components, filtering tools, third-party objects, and HTML components. You can insert the same library component repeatedly to the same dashboard body. 

Library components that you inserted in dashboards are references of the library components in the component library. The changes to a library component in the library will be reflected in all the dashboards referencing the library component, such as removal of library components, version update, and permission change. 

Likewise, data components you referenced directly from reports can also obtain changes from the reports.

Component Options menu

Each component in the dashboard body has its own Options menu, which is available when you select the Options button  on the title bar of the component.

This Options menu varies with the component type. It may contain the following items: 

- 
Analyze
      Select to load the visual analysis template into a new dashboard tab or browser window.

- 
Edit Setting
    Select to edit the component setting in the corresponding edit dialog box. 

- 
Export
Select to export the library component. 

- 
Delete
    Select to remove the library component from the current dashboard. 

- 
Refresh
Select to customize the auto refresh action for the library component. 

- 
About
    Select to view the component information such as its ID, the author and the email address, and the description about the component.
