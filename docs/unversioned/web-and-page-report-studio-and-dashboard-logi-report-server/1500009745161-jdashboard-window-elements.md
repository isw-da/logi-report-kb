---
title: "JDashboard Window Elements"
id: 1500009745161
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745161-JDashboard-Window-Elements
updated_at: 2021-07-25T07:20:12Z
---

# JDashboard Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745001-JDashboard-Basic-Concepts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745101-Running-Dashboards)

# JDashboard Window Elements

The window elements of JDashboard vary with its two working modes: edit mode and view mode. The following introduces the full UI elements based on the edit mode.

The full-featured JDashboard window is composed of three sections: the [dashboard title bar](#Title) at the top, the [toolbar](#Toolbar) on the left providing options for working with dashboards, and the [dashboard editing area](#Edit) where you navigate and modify dashboards. Since JDashboard can also be used to [access Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009745141-Opening-Visual-Analysis-in-JDashboard), if your Logi Report Server is enabled with Visual Analysis, the elements in the JDashboard window have slight differences.

The options available in JDashboard are determined by the [feature profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009718962-Customizing-JDashboard-Profile) that is selected as the default profile in the Configure Profile > JDashboard > Features tab of the profile page and the property setting in the Configure Profile > JDashboard > Properties tab (profile has the higher priority). The default JDashboard profile provides full options.

## Dashboard Title Bar

The dashboard title bar at the top contains tabs labeling the names of the open dashboards.

**Dashboard name tabs**

Each tab represents an open dashboard and the dashboard name is shown on the tab.

The following are operations on the tabs:

* Select a tab to activate the corresponding dashboard.
* Rename a tab. Double-click a tab name and the name becomes editable. Type a new name, then press Enter or select outside of the input field to save the name.
* Move a tab. Drag a tab and drop it beside a different tab so as to change the tab order.
* Select **x** beside a dashboard name to close the dashboard.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif)

Adds a new blank dashboard in the current web browser.

If Visual Analysis is enabled, you can put the mouse pointer on the button for one second and a drop-down menu will be displayed containing the following options:

* **Dashboard**  
   Creates a new blank dashboard as a new tab.
* **Analysis**  
   Opens Visual Analysis as a new tab.

![Language button](https://devnet.logianalytics.com/hc/article_attachments/4404936953623/btn_dshbrd_nls.gif)

Specifies the language in which the dashboard will be displayed if it is an [NLS dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level). Available when [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#NLS) is selected in the server profile.

**View Mode/Edit Mode**

Switches to View Mode or Edit Mode of JDashboard.

## Toolbar

The toolbar on the left contains these buttons:

![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404942565655/btn_dshbrd_show.gif)**Show/Hide Resources**

Shows or hides the Resources panel which includes these branches:

* **Component Library** lists the library components created in and published from Logi Report Designer. You can select a library component and drag it into the dashboard body.
* **Reports** lists page reports and web reports. You can open any report from JDashboard or add report data components into your dashboards.
* **Toolbox** lists the objects that can be inserted in your dashboards such as labels, images, special fields, filtering tools, third-party objects, and HTML components.

You can use the search bar to search for any desired resources in a fast and convenient way (to display the search bar, select the **Search** button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif) on the panel title bar).

The following shows the options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404936734231/btn_srchtlbr.gif)

* **Text box**  
  Type in the text you want to search in the text box and the values containing the matched text will be listed.
* **X**  
  Closes the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404942460951/btn_srchtlbr_adv.gif)  
  Lists more search options.
  + **Highlight All**   
    Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Specifies whether to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404936734487/btn_srchtlbr_prv.gif)  
  When Highlight All is selected, you can use this button to go to the previous matched text.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404936734743/btn_srchtlbr_nxt.gif)  
   When Highlight All is selected, you can use this button to go to the next matched text.

![New button](https://devnet.logianalytics.com/hc/article_attachments/4404936714519/btn_newobj.gif)**New**

Creates a new blank dashboard with a new tab added.

If Visual Analysis is enabled, selecting the button will bring out a drop-down menu that contains the following options:

* **New Dashboard**  
   Creates a new blank dashboard as a new tab.
* **New Analysis**  
   Opens Visual Analysis as a new tab.

![Open button](https://devnet.logianalytics.com/hc/article_attachments/4404942445591/btn_open.gif)**Open**

Displays the [Open Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009720202-Open-Dashboard) dialog box for you to specify a dashboard to run, or the [Open Document](https://devnet.logianalytics.com/hc/en-us/articles/1500009746961-Open-Document) dialog box where you can select a dashboard or a analysis template to open. Which dialog box JDashboard will display depends on whether Visual Analysis is enabled.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404942445847/btn_save.gif)**Save**

Saves the changes made to the current dashboard.

![Refresh button](https://devnet.logianalytics.com/hc/article_attachments/4404936716311/btn_refresh.gif)**Refresh**

Refreshes the current dashboard.

![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404936748567/btn_dshbrd_prm.gif)**Enter Parameter Values**

Opens the Enter Parameter Values dialog box which lists all the parameters used in the dashboard for [specifying their values](https://devnet.logianalytics.com/hc/en-us/articles/1500009720082-Enter-Parameter-Values).

![Clear Filters button](https://devnet.logianalytics.com/hc/article_attachments/4404942605079/btn_dshbrd_clrfltr.gif)**Clear Filters**

Removes all the filters from the current dashboard including those generated via filter controls, messages, drilling and going actions and those designed using web browsers such as Page Report Studio and Web Report Studio, except query filters and others designed and taking effect in Logi Report Designer.

![Arrange button](https://devnet.logianalytics.com/hc/article_attachments/4404936953879/btn_dshbrd_autoarng.gif) **Arrange**

[Automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly one time. It is an instant action.

![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404936715287/btn_expt.gif)**Export**

Displays the Export dialog box for [exporting the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009745041-Exporting-and-Printing-Library-Components#Export) in the current dashboard.

![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404936715543/btn_print.gif)**Print**

Displays the Print dialog box for [printing the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009745041-Exporting-and-Printing-Library-Components#Print) in the current dashboard.

![Open Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4404936717079/btn_rspnsvopn.gif)/![Close Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4404942446615/btn_rspnsvcls.gif)**Open/Close Responsive Mode**

Enables or disables the capability of automatically scaling and folding the dashboard in the view mode according to the current browser window on computers. See [Automatically scaling dashboard components according to browser window](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#Responsive) for more information.

![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936890647/btn_dshbrd_optn.gif)**Options**

Displays the following options:

* **New**  
   Creates a new blank dashboard.

  If Visual Analysis is enabled, the New option contains a submenu:

  + **Dashboard**  
     Creates a new blank dashboard as a new tab.
  + **Analysis**  
     Opens Visual Analysis as a new tab.
* **Open**  
   Displays the [Open Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009720202-Open-Dashboard) dialog box for you to specify a dashboard to open, or the [Open Document](https://devnet.logianalytics.com/hc/en-us/articles/1500009746961-Open-Document) dialog box where you can select a dashboard or a analysis template to open. Which dialog box JDashboard will display depends on whether Visual Analysis is enabled.
* **Save**  
   Saves the changes made to the current dashboard.
* **Save As**  
   Saves the dashboard with a different name or to a new location.
* **Export**  
   Displays the Export dialog box for exporting library components in the current dashboard.
* **Print**  
   Displays the Print dialog box for printing library components in the current dashboard.
* **Clear Filters**  
   Removes all the filters from the current dashboard including those generated via filter controls, messages, drilling and going actions and those designed using web browsers such as Page Report Studio and Web Report Studio, except query filters and others designed and taking effect in Logi Report Designer.
* **[On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009745061-Filtering-the-Data-Components-in-a-Dashboard#Default)**  
   The option is unavailable when [Enable Setting Default On-screen Filter Values For Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#OnScreenFilter) is not selected in the server profile.
  + **Save as Default**  
     Saves the current on-screen filter values as the user defined default values for the dashboard and for the user. This menu item is disabled when the current on-screen filter values are the same as the default values.
  + **Restore to Default**  
     Restores to the default on-screen filter values. This menu item is disabled when current on-screen filter values are the same as the default values.
  + **Clear Default**  
     Clears user defined default on-screen filter values. This menu item is disabled when there are no user defined default values.
* **Share Parameter**  
   Opens the Share Parameters Setting dialog box for [sharing parameters between library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009718942-Specifying-Parameter-Values-for-a-Dashboard#Share).
* **Arrange**  
  [Automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly one time. It is an instant action.
* **Auto Arrange**  
  [Automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly once the layout requires arrangement. It is a status setting. After selecting it, this option will be kept selected and the Arrange option will be disabled until you unselect Auto Arrange. The status will be saved with the dashboard.
* **Responsive View**Enables or disables the capability of automatically scaling and folding the dashboard in the view mode according to the current browser window on computers. See [Automatically scaling dashboard components according to browser window](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#Responsive) for more information.
* **Set as Server Home**  
  [Sets the current dashboard as the home page](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#HomePage) after logging onto the Logi Report Server console.
* **Language**  
   Allows you to specify the language in which the dashboard will be displayed. Available when [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#NLS) is selected in the server profile.
* **Component Title Bar**  
  [Customizes the way of showing component title bar and the icons on it](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#TitleBar).
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

Library components inserted to dashboards are references of the library components in the component library. The changes to a library component in the library will be reflected in all of the dashboards referencing the library component, such as removal of library components, version update, and permission change.

Likewise, data components referenced directly from reports are also affected by any changes to the reports.

**Component Options menu**

Each component in the dashboard body has its own Options menu, which is available when you select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4404942444951/btn_dshbrd_more.gif) on the [title bar of the component](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#TitleBar).

This Options menu varies with the component type. It may contain the following items:

* **Analyze**  
   Loads the analysis template in [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009745141-Opening-Visual-Analysis-in-JDashboard) in a new dashboard tab or browser window.
* **Edit Setting**  
   Edits the component setting in the corresponding edit dialog box.
* **Export**  
  [Exports the library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009745041-Exporting-and-Printing-Library-Components).
* **Delete**  
   Deletes the library component from the current dashboard.
* **Refresh**  
  [Customizes the auto refresh action](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#Refresh) for the library component.
* **About**  
   Displays the component information such as its ID, the author and his/her e-mail address, and the description about the component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745001-JDashboard-Basic-Concepts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745101-Running-Dashboards)
