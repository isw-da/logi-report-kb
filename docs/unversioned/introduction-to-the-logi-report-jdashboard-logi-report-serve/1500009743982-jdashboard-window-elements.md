---
title: "JDashboard Window Elements"
id: 1500009743982
section: "Introduction to the Logi Report JDashboard Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009743982-JDashboard-Window-Elements
updated_at: 2021-07-24T00:49:23Z
---

# JDashboard Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743842-JDashboard-Basic-Concepts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771861-Running-Dashboards)

# JDashboard Window Elements

JDashboard window elements vary with its two working modes: edit mode and view mode. This topic describes the full UI elements based on the edit mode.

The full-featured JDashboard window contains three sections: the [dashboard title bar](#Title) at the top, the [toolbar](#Toolbar) on the left providing options for working with dashboards, and the [dashboard editing area](#Edit) where you navigate and modify dashboards. Since you can also use JDashboard to [access Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009743962-Opening-Visual-Analysis-in-JDashboard), if your Logi Report Server enables Visual Analysis, the elements in the JDashboard window have slight differences.

The default JDashboard profile provides full options. You can change the options in JDashboard by [Customizing JDashboard Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009771841-Customizing-JDashboard-Profile).

## Dashboard Title Bar

The dashboard title bar at the top contains tabs labeling the names of the open dashboards.

**Dashboard name tabs**

Each tab represents an open dashboard and the tab name is the dashboard name.

You can perform the following operations on the tabs:

* Select a tab to activate the corresponding dashboard.
* Rename a tab. Double-click a tab name and the name becomes editable. Type a new name, then press Enter or select outside of the input field to save the name.
* Move a tab. Drag a tab and drop it beside a different tab to change the tab order.
* Select **x** beside a dashboard name to close the dashboard.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)**Add**

Adds a new blank dashboard in the current web browser.

If Server enables Visual Analysis, you can put the mouse pointer on the button for one second and JDashboard will display a drop-down menu that contains the following options:

* **Dashboard**  
   Creates a new blank dashboard as a new tab.
* **Analysis**  
   Opens Visual Analysis as a new tab.

![Language button](https://devnet.logianalytics.com/hc/article_attachments/4404880558871/btn_dshbrd_nls.gif)

Specifies the language in which the dashboard will be displayed if it is an [NLS dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009777481-NLS-at-Report-Level). Available when you have selected [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#NLS) in the server profile.

## Toolbar

The toolbar on the left contains these buttons:

![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404880425623/btn_dshbrd_show.gif)**Show/Hide Resources**

Shows or hides the Resources panel which includes these branches:

* **Component Library** lists the library components that you created in and published from Logi Report Designer. You can select a library component and drag it into the dashboard body.
* **Reports** lists page reports and web reports. You can open any report in JDashboard or add report data components into your dashboards.
* **Toolbox** lists the objects that you can insert in your dashboards such as labels, images, special fields, filtering tools, third-party objects, and HTML components.

You can use the search bar to search for resources in a fast and convenient way. To display the search bar, select the **Search** button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif) on the Resources panel title bar.

See the following options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **X**  
  Select to close the search bar or clear the typed text.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
  When you selected **Highlight All**, you can use this button to go to the previous matched text.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
   When you selected **Highlight All**, you can use this button to go to the next matched text.

![New button](https://devnet.logianalytics.com/hc/article_attachments/4404885307031/btn_newobj.gif) **New**

Creates a new blank dashboard with a new tab.

If Server enables Visual Analysis, selecting the button will bring out a drop-down menu that contains the following options:

* **Dashboard**  
   Creates a new blank dashboard as a new tab.
* **Analysis**  
   Opens Visual Analysis as a new tab.

![Open button](https://devnet.logianalytics.com/hc/article_attachments/4404880136471/btn_open.gif) **Open**

Displays the [Open Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009773541-Open-Dashboard-Dialog-Box-Properties) dialog box for you to specify a dashboard to run, or the [Open Document](https://devnet.logianalytics.com/hc/en-us/articles/1500009745542-Open-Document-Dialog-Box-Properties) dialog box where you can select a dashboard or a analysis template to open. Which dialog box JDashboard will display depends on whether Server enables Visual Analysis.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404885307671/btn_save.gif) **Save**

Saves the changes you made to the current dashboard.

![Refresh button](https://devnet.logianalytics.com/hc/article_attachments/4404880138135/btn_refresh.gif)**Refresh**

Refreshes the current dashboard.

![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404880189463/btn_dshbrd_prm.gif)**Enter Parameter Values**

Opens the Enter Parameter Values dialog box which lists all the parameters that the dashboard uses for [specifying their values](https://devnet.logianalytics.com/hc/en-us/articles/1500009745482-Enter-Parameter-Values-Dialog-Box-Properties).

![Clear Filters button](https://devnet.logianalytics.com/hc/article_attachments/4404885601815/btn_dshbrd_clrfltr.gif)**Clear Filters**

Removes all the filters from the current dashboard including those generated via filter controls, messages, drilling and going actions and those designed using web browsers such as Page Report Studio and Web Report Studio, except query filters and others designed and taking effect in Logi Report Designer.

![Arrange button](https://devnet.logianalytics.com/hc/article_attachments/4404885602327/btn_dshbrd_autoarng.gif) **Arrange**

[Automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly one time. It is an instant action.

![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404880137111/btn_expt.gif)**Export**

Displays the Export dialog box for [exporting the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009771781-Exporting-and-Printing-the-Library-Components-in-a-Dashboard) in the current dashboard.

![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404880137367/btn_print.gif)**Print**

Displays the Print dialog box for [printing the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009771781-Exporting-and-Printing-the-Library-Components-in-a-Dashboard) in the current dashboard.

![Open Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4404880139159/btn_rspnsvopn.gif)/![Close Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4404880139415/btn_rspnsvcls.gif)**Open/Close Responsive Mode**

Enables or disables the capability of automatically scaling and folding the dashboard in the view mode according to the current browser window on computers. For more information, see [Automatically scaling dashboard components according to browser window](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#Responsive).

![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880435735/btn_dshbrd_optn.gif)**Options**

Displays the following options:

* **New**  
   Creates a new blank dashboard.

  If Server enables Visual Analysis, the New option contains a sub menu:

  + **Dashboard**  
     Creates a new blank dashboard as a new tab.
  + **Analysis**  
     Opens Visual Analysis as a new tab.
* **Open**  
   Displays the [Open Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009773541-Open-Dashboard-Dialog-Box-Properties) dialog box for you to specify a dashboard to open, or the [Open Document](https://devnet.logianalytics.com/hc/en-us/articles/1500009745542-Open-Document-Dialog-Box-Properties) dialog box where you can select a dashboard or a analysis template to open. Which dialog box JDashboard will display depends on whether Server enables Visual Analysis.
* **Save**  
   Saves the changes you made to the current dashboard.
* **Save As**  
   Saves the dashboard with a different name or to a new location.
* **Export**  
   Displays the Export dialog box for exporting library components in the current dashboard.
* **Print**  
   Displays the Print dialog box for printing library components in the current dashboard.
* **Clear Filters**  
   Removes all the filters from the current dashboard including those generated via filter controls, messages, drilling and going actions and those designed using web browsers such as Page Report Studio and Web Report Studio, except query filters and others designed and taking effect in Logi Report Designer.
* **[On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009743862-Filtering-the-Data-Components-in-a-Dashboard#Default)**  
   The option is unavailable when [Enable Setting Default On-screen Filter Values For Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#OnScreenFilter) is not selected in the server profile.
  + **Save as Default**  
     Saves the current on-screen filter values as the user defined default values for the dashboard and for the user. JDashboard disables this menu item when the current on-screen filter values are the same as the default values.
  + **Restore to Default**  
     Restores to the default on-screen filter values. JDashboard disables this menu item when current on-screen filter values are the same as the default values.
  + **Clear Default**  
     Clears user defined default on-screen filter values. JDashboard disables this menu item when there are no user defined default values.
* **Share Parameter**  
   Opens the Share Parameters Setting dialog box for [sharing parameters between library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009743882-Specifying-Parameter-Values-for-a-Dashboard#Share).
* **Arrange**  
  [Automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly one time. It is an instant action.
* **Auto Arrange**  
  [Automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly once the layout requires arrangement. It is a status setting. After you select it, JDashboard will keep this option selected and will disable the **Arrange** option until you deselect **Auto Arrange**. JDashboard will save the status with the dashboard.
* **Responsive View**Enables or disables the capability of automatically scaling and folding the dashboard in the view mode according to the current browser window on computers. For more information, see [Automatically scaling dashboard components according to browser window](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#Responsive).
* **Set as Server Home**  
  [Sets the current dashboard as the home page](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#HomePage) after logging onto the Server Console.
* **Language**  
   You can specify the language in which to display the dashboard. Available when you have selected [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#NLS) in the server profile.
* **Component Title Bar**  
  [Customizes the way of showing component title bar and the icons on it](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#TitleBar).
* **Themes**  
   Opens the Themes dialog box for selecting a theme to apply to the current dashboard.
* **Show/Hide Dashboard Header**  
   Changes the current status of the dashboard header from being shown to hidden or from being hidden to shown.
* **Help**  
   Displays the JDashboard help documents.
* **Exit**  
   Exits JDashboard.

## Dashboard Editing Area

Dashboard view has header and body sections.

The dashboard header can contain labels, images, and special fields.

The dashboard body can contain library components, report components, filtering tools, third-party objects, and HTML components. You can insert the same library component repeatedly to the same dashboard body.

Library components that you inserted in dashboards are references of the library components in the component library. The changes to a library component in the library will be reflected in all the dashboards referencing the library component, such as removal of library components, version update, and permission change.

Likewise, data components you referenced directly from reports can also obtain changes from the reports.

**Component Options menu**

Each component in the dashboard body has its own **Options** menu, which is available when you select the **Options** button ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4404880135063/btn_dshbrd_more.gif) on the [title bar of the component](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#TitleBar).

This Options menu varies with the component type. It may contain the following items:

* **Analyze**  
   Loads the analysis template in [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009743962-Opening-Visual-Analysis-in-JDashboard) in a new dashboard tab or browser window.
* **Edit Setting**  
   Edits the component setting in the corresponding edit dialog box.
* **Export**  
  [Exports the library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009771781-Exporting-and-Printing-the-Library-Components-in-a-Dashboard).
* **Delete**  
   Deletes the library component from the current dashboard.
* **Refresh**  
  [Customizes the auto refresh action](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#Refresh) for the library component.
* **About**  
   Displays the component information such as its ID, the author and his/her e-mail address, and the description about the component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743842-JDashboard-Basic-Concepts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771861-Running-Dashboards)
