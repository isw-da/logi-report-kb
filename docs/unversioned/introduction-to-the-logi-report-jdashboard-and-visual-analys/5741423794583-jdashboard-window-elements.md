---
title: "JDashboard Window Elements"
id: 5741423794583
section: "Introduction to the Logi Report JDashboard and Visual Analysis Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741423794583-JDashboard-Window-Elements
updated_at: 2022-10-31T17:16:06Z
---

# JDashboard Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741396274071-JDashboard-Basic-Concepts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741416524055-Running-Dashboards)

# JDashboard Window Elements

JDashboard window elements vary with its two working modes: edit mode and view mode. This topic describes the full UI elements based on the edit mode.

The full-featured JDashboard window contains three sections: the [dashboard title bar](#Title) at the top, the [toolbar](#Toolbar) on the left providing options for working with dashboards, and the [dashboard editing area](#Edit) where you navigate and modify dashboards. Since you can also use JDashboard to [access Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/5741409837079-Opening-Visual-Analysis-in-JDashboard), if your Server enables Visual Analysis, the elements in the JDashboard window have slight differences.

The default JDashboard profile provides full options. You can change the options in JDashboard by [Customizing JDashboard Profile](https://devnet.logianalytics.com/hc/en-us/articles/5741401784855-Customizing-JDashboard-Profile).

## Dashboard Title Bar

The dashboard title bar at the top contains tabs labeling the names of the dashboards that you open.

**Dashboard name tabs**

Each tab represents an open dashboard, and the tab name is the dashboard name.

You can perform the following operations on the tabs:

* Select a tab to activate the corresponding dashboard.
* Rename a tab. Double-click a tab name and the name becomes editable. Type a new name, then press Enter or select outside of the input field to save the name.
* Move a tab. Drag a tab and drop it beside a different tab to change the tab order.
* Select **x** beside a dashboard name to close the dashboard.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif)**Add button**

Select to add a new blank dashboard in the current web browser.

If Server enables Visual Analysis, you can hover over this button for one second and Server will display a drop-down menu that contains the following options:

* **Dashboard**  
   Select to create a new blank dashboard as a new tab.
* **Analysis**  
   Select to open Visual Analysis as a new tab.

![Language button](https://devnet.logianalytics.com/hc/article_attachments/9905779037591/btn_dshbrd_nls.gif)

Specify the language in which you want to display the dashboard if it is an [NLS dashboard](https://devnet.logianalytics.com/hc/en-us/articles/5741482629911-NLS-at-Report-Level). This setting is available when you have selected [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#NLS) in the server profile.

## Toolbar

The toolbar on the left contains these buttons:

![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/9905736385175/btn_dshbrd_show.gif)**Show/Hide Resources button**

Select to show or hide the Resources panel which includes these parts:

* **Component Library** lists the library components that you created in and published from Logi Report Designer. You can select a library component and drag it into the dashboard body.
* **Reports** lists page reports and web reports on the server resource tree. You can open any report in JDashboard or add report data components into your dashboards.
* **Toolbox** lists the objects that you can insert in your dashboards such as labels, images, special fields, filtering tools, third-party objects, and HTML components.

You can use the search bar to search for resources in a fast and convenient way. To display the search bar, select the **Search** button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif) on the Resources panel title bar.

See the following properties in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/9905619099031/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)****Close button**  
  Select to close the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/9905631409303/btn_srchtlbr_adv.gif)**More Options button**  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/9905631449623/btn_srchtlbr_prv.gif) **Previous button**  
  Select to go to the previous matched text when you have selected **Highlight All**.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/9905619191959/btn_srchtlbr_nxt.gif)**Next button**  
   Select to go to the next matched text when you have selected **Highlight All**.

![New button](https://devnet.logianalytics.com/hc/article_attachments/9905577927831/btn_newobj.gif) **New button**

Select to create a new blank dashboard with a new tab.

If Server enables Visual Analysis, selecting this button will bring out a drop-down menu that contains the following options:

* **Dashboard**  
   Select to create a new blank dashboard as a new tab.
* **Analysis**  
   Select to open Visual Analysis as a new tab.

![Open button](https://devnet.logianalytics.com/hc/article_attachments/9905577968791/btn_open.gif) **Open button**

Select to open the [Open Dashboard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741419729431-Open-Dashboard-Dialog-Box-Properties) to specify a dashboard you want to run, or the [Open Document dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741441646871-Open-Document-Dialog-Box-Properties) where you can select a dashboard or an analysis template to open. Which dialog box will display depends on whether Server enables Visual Analysis.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/9905577991703/btn_save.gif) **Save button**

Select to save the changes you made to the current dashboard.

![Refresh button](https://devnet.logianalytics.com/hc/article_attachments/9905616092439/btn_refresh.gif)**Refresh button**

Select to refresh the current dashboard.

![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/9905575308823/btn_dshbrd_prm.gif)**Enter Parameter Values button**

Select to open the Enter Parameter Values dialog box which lists all the parameters that the dashboard uses for [specifying their values](https://devnet.logianalytics.com/hc/en-us/articles/5741441420695-Enter-Parameter-Values-Dialog-Box-Properties).

![Clear Filters button](https://devnet.logianalytics.com/hc/article_attachments/9905779069079/btn_dshbrd_clrfltr.gif)**Clear Filters button**

Select to remove all the filters from the current dashboard, including those generated via filter controls, messages, drilling and going actions, and those designed using web browsers such as Page Report Studio and Web Report Studio, except dataset filters and others designed and taking effect in Designer.

![Arrange button](https://devnet.logianalytics.com/hc/article_attachments/9905817727767/btn_dshbrd_autoarng.gif) **Arrange button**

Select to [automatically arrange the library components](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly. It is an instant action.

![Export button](https://devnet.logianalytics.com/hc/article_attachments/9905578054551/btn_expt.gif)**Export button**

Select to open the Export dialog box for [exporting the library components](https://devnet.logianalytics.com/hc/en-us/articles/5741401668759-Exporting-and-Printing-the-Library-Components-in-a-Dashboard) in the current dashboard.

![Print button](https://devnet.logianalytics.com/hc/article_attachments/9905616008343/btn_print.gif)**Print button**

Select to open the Print dialog box for [printing the library components](https://devnet.logianalytics.com/hc/en-us/articles/5741401668759-Exporting-and-Printing-the-Library-Components-in-a-Dashboard) in the current dashboard.

![Open Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/9905616210327/btn_rspnsvopn.gif)/![Close Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/9905616238231/btn_rspnsvcls.gif)**Open/Close Responsive Mode button**

Select to enable or disable the capability of automatically scaling and folding the dashboard in the view mode according to the current browser window on computers. For more information, see [Responsive View](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#Responsive).

![Options button](https://devnet.logianalytics.com/hc/article_attachments/9905759210647/btn_dshbrd_optn.gif)**Options button**

Select this button and Server displays the following options:

* **New**  
   Select to create a new blank dashboard.

  If Server enables Visual Analysis, the New option contains a sub menu:

  + **Dashboard**  
     Select to create a new blank dashboard as a new tab.
  + **Analysis**  
     Select to open Visual Analysis as a new tab.
* **Open**  
   Select to open the [Open Dashboard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741419729431-Open-Dashboard-Dialog-Box-Properties) to specify a dashboard you want to open, or the [Open Document dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741441646871-Open-Document-Dialog-Box-Properties) where you can select a dashboard or an analysis template to open. Which dialog box will open depends on whether Server enables Visual Analysis.
* **Save**  
   Select to save the changes you made to the current dashboard.
* **Save As**  
   Select to save the dashboard with a different name or to a new location.
* **Export**  
   Select to open the Export dialog box for exporting library components in the current dashboard.
* **Print**  
   Select to open the Print dialog box for printing library components in the current dashboard.
* **Clear Filters**  
   Select to remove all the filters from the current dashboard, including those generated via filter controls, messages, drilling and going actions, and those designed using web browsers such as Page Report Studio and Web Report Studio, except dataset filters and others designed and taking effect in Designer.
* **[On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/5741416414103-Filtering-the-Data-Components-in-a-Dashboard#Default)**  
   The option is available when administrators did not clear [Enable Setting Default On-screen Filter Values For Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#OnScreenFilter) in the server profile.
  + **Save as Default**  
     Select to save the current on-screen filter values as the user defined default values for the dashboard and for you. Server disables this menu item when the current on-screen filter values are the same as the default values.
  + **Restore to Default**  
     Select to restore to the default on-screen filter values. Server disables this menu item when current on-screen filter values are the same as the default values.
  + **Clear Default**  
     Select to clear user defined default on-screen filter values. Server disables this menu item when there are no user defined default values.
  + **Push Down**  
    Select if you want to generate the dashboard data by applying all filters to the database.
* **Share Parameter**  
   Select to open the Share Parameters Setting dialog box for [sharing parameters between library components](https://devnet.logianalytics.com/hc/en-us/articles/5741423625879-Specifying-Parameter-Values-for-a-Dashboard#Share).
* **Arrange**  
  Select to [automatically arrange the library components](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly. It is an instant action.
* **Auto Arrange**  
  Select to [automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly once the layout requires arrangement. It is a status setting. After you select it, Server keeps this option being selected and disable the **Arrange** option until you clear **Auto Arrange**. Server will save the status with the dashboard.
* **Responsive View**  
  Select to enable or disable the capability of automatically scaling and folding the dashboard in the view mode according to the current browser window on computers. For more information, see [Responsive View](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#Responsive).
* **Set as Server Home**  
  Select to [set the current dashboard as the home page](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#HomePage) after you sign on to the Server Console.
* **Language**  
   You can specify the language in which you want to display the dashboard. Available when you have selected [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#NLS) in the server profile.
* **Component Title Bar**  
  Select to [customize the way of showing component title bar and the icons on it](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#TitleBar).
* **Themes**  
   Select to open the Themes dialog box for selecting a theme to apply to the current dashboard.
* **Show/Hide Dashboard Header**  
   Select to change the current status of the dashboard header from being shown to hidden or from being hidden to shown.
* **Help**  
   Select to view the JDashboard help documentation.
* **Exit**  
   Select to exit JDashboard.

## Dashboard Editing Area

Dashboard view has header and body sections.

The dashboard header can contain labels, images, and special fields.

The dashboard body can contain library components, report components, filtering tools, third-party objects, and HTML components. You can insert the same library component repeatedly to the same dashboard body.

Library components that you inserted in dashboards are references of the library components in the component library. The changes to a library component in the library will be reflected in all the dashboards referencing the library component, such as removal of library components, version update, and permission change.

Likewise, data components you referenced directly from reports can also obtain changes from the reports.

**Component Options menu**

Each component in the dashboard body has its own **Options** menu, which is available when you select the **Options** button ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/9905772219671/btn_dshbrd_more.gif) on the [title bar of the component](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#TitleBar).

This Options menu varies with the component type. It may contain the following items:

* **Analyze**  
   Select to load the visual analysis template into a new dashboard tab or browser window.
* **Edit Setting**  
   Select to edit the component setting in the corresponding edit dialog box.
* **Export**  
  Select to [export the library component](https://devnet.logianalytics.com/hc/en-us/articles/5741401668759-Exporting-and-Printing-the-Library-Components-in-a-Dashboard).
* **Delete**  
   Select to remove the library component from the current dashboard.
* **Refresh**  
  Select to [customize the auto refresh action](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#Refresh) for the library component.
* **About**  
   Select to view the component information such as its ID, the author and the email address, and the description about the component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741396274071-JDashboard-Basic-Concepts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741416524055-Running-Dashboards)
