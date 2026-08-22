---
title: "Customizing Web Report Studio Profile"
id: 4405684049047
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405684049047-Customizing-Web-Report-Studio-Profile
updated_at: 2022-01-27T07:59:53Z
---

# Customizing Web Report Studio Profile

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690685335-Exporting-Printing-the-Web-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690691607-Customizing-the-Web-Report-Studio-UI)

# Customizing Web Report Studio Profile

This topic describes how you can configure the preferences and features of Web Report Studio using the Server Console.

The Administration > Server Profile > Customize Profile page is available to administrators, provides default settings for running Web Report Studio, and controls whether end users can configure the settings in the My Profile > Customize Profile page. Administrators may change the settings in the Server Profile > Customize Profile page to enable or disable some features. Then, end users can configure Web Report Studio preferences in the My Profile > Customize Profile page for themselves, that is, they can decide whether to disable the features which administrators have enabled.

**To configure Web Report Studio preferences and features:**

1. Choose according to your user account:
   * Anyone can configure for themselves: go to the **My Profile** > **Customize Profile** > **Web Report Studio** tab.
   * Administrators can configure for all users: go to the **Administration** > **Server Profile** > **Customize Profile** > **Web Report Studio** tab.
2. In the **Features** tab, select the feature profile from the **Default Profile** list. The feature profile determines the features that are available in Web Report Studio.

   ![Features subtab](https://devnet.logianalytics.com/hc/article_attachments/4420453392919/profile_featr.gif)

   Logi Report provides a default profile in which Server enables all the Web Report Studio features. Administrators can create, edit, or remove the customized feature profiles. End users can only select a profile and view its settings.

   * To create a profile, select **New Profile**. Server displays the [Web Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/4405683776023-Web-Report-Studio-Profile-Properties) dialog box. Then create the profile.
   * To edit a profile, select **Edit** in the profile table.
   * To remove a profile, select it in the profile table, then select **Delete**.
3. In the **Properties** tab, specify the [properties](#Property) for configuring the Web Report Studio preferences and screen elements.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)Two factors determine whether an option is available in Web Report Studio: whether you enabled the corresponding feature in the selected profile and whether you enabled the property in the **Properties** tab. Only when you enabled both can the option be available for use. If you disabled a feature in the profile, Server hides the corresponding option from the Web Report Studio window even though you enabled it in the **Properties** tab.
4. Select **OK** to accept the profile settings.

The following table describes the properties for configuring the Web Report Studio settings. The properties for customizing the screen elements are classified for the two working modes of Web Report Studio: [Edit Mode](#Edit) and [View Mode](#View).

| Option | Description |
| --- | --- |
| Show Link of View/Edit Mode | You can switch between View Mode and Edit Mode when running web reports in Web Report Studio. View Mode provides simple functions for mainly viewing reports, while Edit Mode provides editing and analytic functions. |
| Target of Detail Table Report and Links | Select where to load the linked target in Web Report Studio, which can be a link report, a URL, a chart hyperlink, or the detail table created from the go-to-detail function. The setting takes effect when you set **Server Setting** as the target frame when defining such links either in Logi Report Designer or in Web Report Studio. **New Window** means to load the linked target into a new window, while **Same Frame** means to load the linked target into the same frame or window where the main report is. |
| Show Description When Hovering Over Table Header Labels | Select if you want to display the description of the related data field when you hover over a label in the table header in Web Report Studio. |
| Web Report Page Template for Quick Start | Select the default page template you want to use in the reports that you create [using the quick start method](https://devnet.logianalytics.com/hc/en-us/articles/4405690690711-Quick-Start-with-a-Table-Report). |
| When web report template cannot work properly Logi Report should | Select how you want Logi Report to deal with the situation when Server cannot create a web report with the selected web report page template, which uses a formula that references bound data to control the company logo.  * **Stop**  Select to stop creating the report. * **Ignore**  Select to remove all the data context like the bound data and formula from the template and continue creating the report. * **Show warning**  Select to display a warning message. |
| Edit Mode Properties | |
| Show Toolbar | Server shows the toolbar which contains the menu options and toolbar icons for working with Web Report Studio. For more information, see [Web Report Studio Window Elements](https://devnet.logianalytics.com/hc/en-us/articles/4405690689815-Web-Report-Studio-Window-Elements). |
| Toolbar Icons | Server displays the following icons on the Web Report Studio toolbar: Menu, New Report, Open, Save, Save As, Export, Page Setup, Print, Share, Refresh, Undo, Redo, Query Filter, Filter, Delete, Font, Background Color, Align, Merge, Split, Language, and Exit. When **Menu** is selected, you can further customize the items in the Menu list and the options for each submenu. |
| Menu | Server displays the following items in the **Menu** list: File, Edit, View, Format, Language, and Help. Enabled when **Menu** in the **Toolbar Icons** section is selected. You can further customize the options on each submenu. |
| File Menu | Server displays the following options on the **File** menu: New Report, Open, Save, Save As, Export, Page Setup, Print, Share, and Exit. Enabled when **File** in the **Menu** section is selected. |
| Edit Menu | Server displays the following options on the **Edit** menu: Undo, Redo, Delete, Wizard, Query Filter, Filter, To Chart, To Crosstab, Rotate Crosstab, Report Body Properties, Bind Data, Use Wizard, Unhide Components, and Style. Enabled when **Edit** in the **Menu** section is selected. |
| View Menu | Server displays the following options on the **View** menu: Inspector, Editing Marks, Refresh. Enabled when View in the Menu section is selected. |
| Format Menu | Server displays the following options on the **Format** menu: Font, Merge, Split. Enabled when **Format** in the **Menu** section is selected. |
| Show Panels | Server shows the following panels: Resources panel, Components panel, Parameters panel, and Filter panel. When this option is selected, Server also selects the following four options. |
| Show Resources Panel | Server shows the Resources panel that lists all the available resources for an object that you select in the current report. |
| Show Components Panel | Server shows the Components panel that lists all the available components that you can insert into a web report. |
| Show Parameters Panel | Server shows the Parameters panel that lists all the parameters used by the current report. |
| Show Filter Panel | Server shows the Filter panel in which you can set the criteria to filter data fields. |
| Right-click Menu | Server shows a shortcut menu when you select the right mouse button, which can help you with most of the component operations in Web Report Studio. |
| View Mode Properties | |
| Show Toolbar | Server shows the toolbar which contains icons for working with Web Report Studio. |
| Toolbar Icons | Server displays the following icons on the Web Report Studio toolbar: Save, Save As, Export, Page Setup, Print, Refresh, Undo, Redo, Query Filter, Filter, Language, and Exit. For more information, see Web Report Studio window elements > [Toolbar](https://devnet.logianalytics.com/hc/en-us/articles/4405690689815-Web-Report-Studio-Window-Elements#Toolbar). |
| Show Panels | Server shows the Parameters panel and Filter panel. When this option is selected, Server selects the following two options too. |
| Show Parameters Panel | Server shows the Parameters panel that lists all the parameters used by the current report. |
| Show Filter Panel | Server shows the Filter panel in which you can set the criteria to filter data fields. |
| Right-click Menu | Server shows a shortcut menu when you select the right mouse button, which can help you with most of the component operations in Web Report Studio. |
| View Web Reports in Responsive Mode | Clear this option to disable [Responsive View](https://devnet.logianalytics.com/hc/en-us/articles/4405690686231-General-Operations-in-Web-Report#Responsive) in the View Mode of Web Report Studio, which you access from a computer. |
| Align Center Report Content | Select this option and clear the **View Web Reports in Responsive Mode** option if you want to display the report contents centrally in the View Mode of Web Report Studio. By default, reports appear the upper-left corner in the View Mode of Web Report Studio, which may leave space on the right for a small report. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690685335-Exporting-Printing-the-Web-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690691607-Customizing-the-Web-Report-Studio-UI)
