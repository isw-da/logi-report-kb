---
title: "Customizing Web Report Studio Profile"
id: 1500009724902
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724902-Customizing-Web-Report-Studio-Profile
updated_at: 2021-07-25T07:18:32Z
---

# Customizing Web Report Studio Profile

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724762-Exporting-Printing-the-Report-Result)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751641-Customizing-the-Web-Report-Studio-UI)

# Customizing Web Report Studio Profile

Preferences and features of Web Report Studio can be configured by profile in the Logi Report Server console. The Administration > Server Profile > Customize Profile page is available to administrators and provides default settings for running Web Report Studio, and controls whether the settings in the My Profile > Customize Profile page can be configured. Administrators may change the settings in the Server Profile > Customize Profile page so as to enable or disable some features. Then end users can configure Web Report Studio preferences in the My Profile > Customize Profile page for their own, that is, they can decide whether or not to enable the features which have been enabled by administrators.

**To configure Web Report Studio preferences and features:**

1. Make a choice according to your user account:
   * Anyone can configure for himself: go to the **My Profile** > **Customize Profile** > **Web Report Studio** tab.
   * Administrators can configure for all users: go to the **Administration** > **Server Profile** > **Customize Profile** > **Web Report Studio** tab.
2. In the Features sub tab, select the feature profile from the Default Profile drop-down list which will determine the features that are available in Web Report Studio.

   ![Features subtab](https://devnet.logianalytics.com/hc/article_attachments/4404936714135/profile_featr.gif)

   Logi Report provides a default profile in which all the Web Report Studio features are enabled. Administrators can create, edit or remove the customized feature profiles. End users can only select a profile and view its settings.

   * To create a profile, select the **New Profile** link. In the [Web Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009748021-Web-Report-Studio-Profile) dialog box, create the profile.
   * To edit a profile, select its **Edit** link in the profile table.
   * To remove a profile, select its check box in the profile table, then select the **Delete** link.
3. In the Properties sub tab, specify the [properties](#Property) for configuring the Web Report Studio preferences and screen elements.

   Whether an option is available in Web Report Studio is determined by two factors: the corresponding feature is enabled in the selected profile and the property is enabled in the Properties tab. Only when both places are enabled can the option be available for use. If a feature is disabled in the profile, the corresponding option will be hidden from the Web Report Studio window even though it is enabled in the Properties tab.
4. Select **OK** to accept the profile settings.

The following table lists the properties for configuring the Web Report Studio settings and their usages. The properties for customizing the screen elements are classified for the two working modes of Web Report Studio: [Edit Mode](#Edit) and [View Mode](#View).

| Option | Description |
| --- | --- |
| Show Link of View/Edit Mode | Specifies whether to allow switching between View Mode and Edit Mode when running web reports in Web Report Studio. View Mode provides just simple functions for mainly viewing reports, while Edit Mode provides editing and analytic functions. |
| Target of Detail Table Report and Links | Specifies where to load the linked target in Web Report Studio, which can be a link report, a URL, a chart hyperlink, or the detail table created from the go-to-detail function. Applied when Server Setting is specified as the target frame when defining such links either in Logi Report Designer or in Web Report Studio. New Window means to load the linked target into a new window, while Same Frame means to load the linked target into the same frame or window where the main report is. |
| When web report template cannot work properly Logi Report should | Specifies how you want Logi Report to deal with the situation when a web report cannot be created with the selected web report template, which uses a formula that references bound data to control the company logo.  * **Stop**  If selected, Logi Report will stop creating the report. * **Ignore**  If selected, Logi Report will remove all the data context like the bound data and formula from the template and continue creating the report. * **Show warning**  If selected, Logi Report will pop up a warning message. |
| Edit Mode properties | |
| Show Toolbar | Specifies whether or not to show the toolbar which contains the menu options and toolbar icons for working with Web Report Studio. For details about the usage of each toolbar icon and menu option, see [Web Report Studio Window Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009751601-Web-Report-Studio-Window-Elements). |
| Toolbar Icons | Specifies whether or not to display the following icons on the Web Report Studio toolbar: Menu, New Report, Open, Save, Save As, Export, Page Setup, Print, Refresh, Undo, Redo, Query Filter, Filter, Delete, Font, Background Color, Align, Merge, Split, Language, Exit. When Menu is selected, you can further customize the items in the Menu list and the options for each submenu. |
| Menu | Specifies whether or not to display the following items in the Menu list: File, Edit, View, Format, Language, Help. Enabled when Menu in the Toolbar Icons section is selected. You can further customize the options on each submenu. |
| File Menu | Specifies whether or not to display the following options on the File submenu: New Report, Open, Save, Save As, Export, Page Setup, Print, Exit. Enabled when File in the Menu section is selected. |
| Edit Menu | Specifies whether or not to display the following options on the Edit submenu: Undo, Redo, Delete, Wizard, Query Filter, Filter, To Chart, To Crosstab, Rotate Crosstab, Report Body Properties, Bind Data, Use Wizard, Unhide Components, Style. Enabled when Edit in the Menu section is selected. |
| View Menu | Specifies whether or not to display the following options on the View submenu: Inspector, Editing Marks, Refresh. Enabled when View in the Menu section is selected. |
| Format Menu | Specifies whether or not to display the following options on the Format submenu: Font, Merge, Split. Enabled when Format in the Menu section is selected. |
| Show Panels | Specifies whether to show all the panels: Resources panel, Components panel, Parameters panel and Filter panel. When this option is selected, the following four options are selected too. |
| Show Resources Panel | Specifies whether or not to show the Resources panel that lists all the available resources for a report. |
| Show Components Panel | Specifies whether or not to show the Components panel that lists all the available components that can be inserted into reports. |
| Show Parameters Panel | Specifies whether or not to show the Parameters panel that lists all the parameters used by the current report. |
| Show Filter Panel | Specifies whether or not to show the Filter panel that specifies the criteria to filter the data field. |
| Right-click Menu | Specifies whether or not to show a shortcut menu when you select the right mouse button, which can help you with most of the component operations in Web Report Studio. |
| View Mode properties | |
| Show Toolbar | Specifies whether or not to show the toolbar which contains icons for working with Web Report Studio. |
| Toolbar Icons | Specifies whether or not to display the following icons on the Web Report Studio toolbar: Save, Save As, Export, Page Setup, Print, Refresh, Undo, Redo, Query Filter, Filter, Language, Exit. For details about the usage of the icons, see Web Report Studio window elements > [Toolbar](https://devnet.logianalytics.com/hc/en-us/articles/1500009751601-Web-Report-Studio-Window-Elements#Toolbar). |
| Show Panels | Specifies whether to show the Parameters panel and Filter panel. When this option is selected, the following two options are selected too. |
| Show Parameters Panel | Specifies whether or not to show the Parameters panel that lists all the parameters used by the current report. |
| Show Filter Panel | Specifies whether or not to show the Filter panel that specifies the criteria to filter the data field. |
| Right-click Menu | Specifies whether or not to show a shortcut menu when you select the right mouse button, which can help you with most of the component operations in Web Report Studio. |
| View Web Reports in Responsive Mode | Specifies whether [responsive view](https://devnet.logianalytics.com/hc/en-us/articles/1500009724782-General-Operations-in-a-Report#Responsive) is enabled by default when running web reports in View Mode of Web Report Studio on computers. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724762-Exporting-Printing-the-Report-Result)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751641-Customizing-the-Web-Report-Studio-UI)
