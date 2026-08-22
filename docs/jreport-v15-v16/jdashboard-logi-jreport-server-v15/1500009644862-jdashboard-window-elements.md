---
title: "JDashboard Window Elements"
id: 1500009644862
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644862-JDashboard-Window-Elements
updated_at: 2021-07-24T20:55:15Z
---

# JDashboard Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644622-JDashboard-Basic-Concepts)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644782-Running-Dashboards)

# JDashboard Window Elements

The window elements of JDashboard vary with its two working modes: edit mode and view mode. The following introduces the full UI elements based on the edit mode.

The full-featured JDashboard window is composed of three sections: the [dashboard title bar](#Title) at the top, the [toolbar](#Sidebar) on the left providing options for working with dashboards, and the [dashboard editing area](#Edit) where you navigate and modify dashboards. Since JDashboard can also be used to [access Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009644842-Opening-Visual-Analysis-in-JDashboard), if your Logi JReport Server is enabled with Visual Analysis, the elements on the JDashboard window have slight differences.

The options available on the JDashboard window UI are determined by the [feature profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009669321-Customizing-JDashboard-Profile) that is selected as the default profile in the Profile > Configure Profile > JDashboard > Features tab and the property setting on the Profile > Configure Profile > JDashboard > Properties tab (profile has the higher priority). The default JDashboard profile provides full options.

Below is a list of the JDashboard window elements:

* [Dashboard Title Bar](#Title)
* [Toolbar](#Sidebar)
* [Dashboard Editing Area](#Edit)

## Dashboard Title Bar

The dashboard title bar at the top contains tabs labeling the names of the open dashboards.

**Dashboard name tabs**

Each tab represents an open dashboard and the dashboard name is shown on the tab.

The following are operations on the tabs:

* Select a tab to activate the corresponding dashboard.
* Rename a tab. Double-select a tab name and the name becomes editable. Enter a new name, then press Enter or select outside of the input field to save the name.
* Move a tab. Drag a tab and drop it beside a different tab so as to change the tab order.
* Select **x** beside a dashboard name to close the dashboard.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif)

Adds a new blank dashboard in the current web browser.

If Visual Analysis is enabled, you can put the mouse pointer on the button for one second and a drop-down menu will be displayed containing the following options:

* **Dashboard**  
   Creates a new blank dashboard as a new tab.
* **Analysis**  
   Opens Visual Analysis as a new tab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920647063/btn_dshbrd_nls.gif)

Specifies the language in which the dashboard will be displayed if it is an [NLS dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009649142-NLS-at-Report-Level). Available when Enable NLS is checked in the Profile > Customize Server Preferences > Advanced tab.

**View Mode/Edit Mode**

Switches to View Mode or Edit Mode of JDashboard.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Toolbar

The toolbar on the left contains these buttons:

![](https://devnet.logianalytics.com/hc/article_attachments/4404920571287/btn_dshbrd_show.gif)**Show/Hide Resources**

Shows or hides the Resources panel which includes these branches:

* **Component Library** lists the library components created in and published from Logi JReport Designer. You can select a library component and drag it into the dashboard body.
* **Reports** lists page reports and web reports. You can open any report from JDashboard or add report data components into your dashboards.
* **Toolbox** lists the objects that can be inserted in your dashboards such as labels, images, special fields, filtering tools, third-party objects, and HTML components.

You can use the quick search toolbar to search for any desired resources in a fast and convenient way (to display the toolbar, select the **Search** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif) at the upper right corner of the panel).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920384023/btn_srchtlbr.gif)

* **Text box**  
   The quick search toolbar treats resource names as strings and searches by consecutive text. Type in the text you want to search for in the text box and the resources containing the matched text will be listed.
* **X**  
   Closes the quick search toolbar.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920384279/btn_srchtlbr_adv.gif)  
   Lists more search options.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920384535/btn_srchtlbr_prv.gif)  
   When Highlight All is selected, you can use this button to go to the previous matched text.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920384791/btn_srchtlbr_nxt.gif)  
   When Highlight All is selected, you can use this button to go to the next matched text.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920357527/btn_newobj.gif)**New**

Creates a new blank dashboard with a new tab added.

If Visual Analysis is enabled, selecting the button will bring out a drop-down menu that contains the following options:

* **New Dashboard**  
   Creates a new blank dashboard as a new tab.
* **New Analysis**  
   Opens Visual Analysis as a new tab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920357783/btn_open.gif)**Open**

Displays the [Open Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009646182-Open-Dashboard) dialog for you to specify a dashboard to run, or the [Open Document](https://devnet.logianalytics.com/hc/en-us/articles/1500009670361-Open-Document) dialog where you can select a dashboard or a analysis template to open. Which dialog will be displayed depends on whether Visual Analysis is enabled.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926628119/btn_save.gif)**Save**

Saves the changes made to the current dashboard.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920358935/btn_refresh.gif)**Refresh**

Refreshes the current dashboard.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920398103/btn_dshbrd_prm.gif)**Enter Parameter Values**

Opens the Enter Parameter Values dialog which lists all the parameters used in the dashboard for [specifying their values](https://devnet.logianalytics.com/hc/en-us/articles/1500009670301-Enter-Parameter-Values).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920647319/btn_dshbrd_clrfltr.gif)**Clear Filters**

Removes all the filters from the current dashboard including those generated via filter controls, messages, drilling and going actions and those designed using web browsers such as Page Report Studio and Web Report Studio, except query filters and others designed and taking effect in Logi JReport Designer.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926780183/btn_dshbrd_autoarng.gif) **Arrange**

[Automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly one time. It is an instant action.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920358295/btn_expt.gif)**Export**

Displays the Export dialog for [exporting the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009669241-Exporting-Library-Components) in the current dashboard.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926628503/btn_print.gif)**Print**

Displays the Print dialog for [printing the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009644762-Printing-Library-Components) in the current dashboard.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920360215/btn_rspnsvopn.gif)/![](https://devnet.logianalytics.com/hc/article_attachments/4404920360599/btn_rspnsvcls.gif)**Open Responsive Mode**/**Close Responsive Mode**

Enables or disables the capability of automatically scaling and folding the dashboard according to the current browser window on computers. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#Responsive) for more information.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif)**Options**

Displays the following options:

* **New**  
   Creates a new blank dashboard.

  If Visual Analysis is enabled, the New option contains a submenu:

  + **Dashboard**  
     Creates a new blank dashboard as a new tab.
  + **Analysis**  
     Opens Visual Analysis as a new tab.
* **Open**  
   Displays the [Open Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009646182-Open-Dashboard) dialog for you to specify a dashboard to open, or the [Open Document](https://devnet.logianalytics.com/hc/en-us/articles/1500009670361-Open-Document) dialog where you can select a dashboard or a analysis template to open. Which dialog will be displayed depends on whether Visual Analysis is enabled.
* **Save**  
   Saves the changes made to the current dashboard.
* **Save As**  
   Saves the dashboard with a different name or to a new location.
* **Export**  
   Displays the Export dialog for exporting library components in the current dashboard.
* **Print**  
   Displays the Print dialog for printing library components in the current dashboard.
* **Clear Filters**  
   Removes all the filters from the current dashboard including those generated via filter controls, messages, drilling and going actions and those designed using web browsers such as Page Report Studio and Web Report Studio, except query filters and others designed and taking effect in Logi JReport Designer.
* **[On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data#Default)**  
   The option is available when [Enable Setting Default On-screen Filter Values For Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#OnScreenFilter) is selected in the Profile > Customize Server Preferences > Advanced tab.
  + **Save as Default**  
     Saves the current on-screen filter values as the user-defined default values for the dashboard and for the user. This menu item is disabled when the current on-screen filter values are the same as the default values.
  + **Restore to Default**  
     Restores to the default on-screen filter values. This menu item is disabled when current on-screen filter values are the same as the default values.
  + **Clear Default**  
     Clears user-defined default on-screen filter values. This menu item is disabled when there are no user-defined default values.
* **Share Parameter**  
   Opens the Share Parameters Setting dialog for [sharing parameters between library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009644722-Specifying-Parameter-Values#Share).
* **Arrange**  
  [Automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly one time. It is an instant action.
* **Auto Arrange**  
  [Automatically arranges the library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#Arrange) in the current dashboard neatly once the layout requires arrangement. It is a status setting. After selecting it, this option will be kept checked and the Arrange option will be disabled until you unselect Auto Arrange. The status will be saved with the dashboard.
* **Responsive View**Enables or disables the capability of automatically scaling and folding the dashboard according to the current browser window on computers. See [*General Operations in JDashboard*](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#Responsive) for more information.
* **Set as Server Home**  
   Sets the current dashboard as the home page after logging onto the Logi JReport Server user console. For details, see [Setting a dashboard as the server home page](https://devnet.logianalytics.com/hc/en-us/articles/1500009644682-Setting-a-Dashboard-as-the-Server-Home-Page).
* **Language**  
   Allows you to specify the language in which the dashboard will be displayed. Available when [Enable NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#NLS) is checked in the Profile > Customize Server Preferences > Advanced tab.
* **Component Title Bar**  
  [Customizes the way of showing component title bar and the icons on it](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#TitleBar).
* **Themes**  
   Opens the Themes dialog for selecting a theme to apply to the current dashboard.
* **Show/Hide Dashboard Header**  
   Changes the current status of the dashboard header from being shown to hidden or from being hidden to shown.
* **Help**  
   Displays the JDashboard help documents.
* **Exit**  
   Exits JDashboard.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Dashboard Editing Area

Dashboard view has header and body sections.

The dashboard header can contain labels, images, and special fields.

The dashboard body can contain report components, library components, filtering tools, third-party objects, and HTML components. You can insert the same library component repeatedly to the same dashboard body.

Library components inserted to dashboards are references of the library component in the component library. The changes to a library component in the library will be reflected in all of the dashboards referencing the library component, such as removal of library components, version update, and permission change.

Likewise, data components referenced directly from reports are also affected by any changes to the web report.

**Component options menu**

Each component in the dashboard body has its own component options menu, which is available when you select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the [title bar of the component](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#TitleBar).

The component options menu varies for different component types. It may contain the following items:

* **Analyze**  
   Loads the analysis template in [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009644842-Opening-Visual-Analysis-in-JDashboard) in a new dashboard tab or browser window.
* **Edit Setting**  
   Edits the component setting in the corresponding edit dialog.
* **Export**  
  [Exports the library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009669241-Exporting-Library-Components).
* **Delete**  
   Deletes the library component from the current dashboard.
* **Refresh**  
  [Customizes the auto refresh action](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#Refresh) for the library component.
* **About**  
   Displays the component information such as its ID, the author and his/her e-mail address, and the description about the component.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644622-JDashboard-Basic-Concepts)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644782-Running-Dashboards)
