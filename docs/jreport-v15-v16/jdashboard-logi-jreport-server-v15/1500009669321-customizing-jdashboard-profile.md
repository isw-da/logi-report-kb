---
title: "Customizing JDashboard Profile"
id: 1500009669321
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669321-Customizing-JDashboard-Profile
updated_at: 2021-07-24T20:55:16Z
---

# Customizing JDashboard Profile

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644842-Opening-Visual-Analysis-in-JDashboard)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009667781-Visual-Analysis)

# Customizing JDashboard Profile

Preferences and features of JDashboard can be configured by profile on both the Logi JReport Administration > Profile page and Logi JReport Console > Profile page. The Logi JReport Administration > Profile page provides default settings for running JDashboard, and controls whether the settings on the Logi JReport Console > Profile page can be configured. Administrators may change the settings from the Logi JReport Administration page so as to enable or disable some features. Then end users can configure JDashboard preferences on the Logi JReport Console page for their own, that is, they can decide whether or not to enable the features which have been enabled on the Logi JReport Administration page.

**To configure JDashboard preferences and features:**

1. Go to the Profile > Customize Profile > JDashboard tab.
2. In the Features sub tab, select the feature profile from the Default Profile drop-down list which will determine the features that are available in JDashboard.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627607/profile_featr.gif)

   Logi JReport provides a Default profile in which all the JDashboard features are enabled. Administrators can create, edit or remove the customized feature profiles. End users can only select a profile and view its settings.

   * To create a profile, select the **New Profile** link. In the [JDashboard Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009670821-JDashboard-Profile) dialog, create the profile.
   * To edit a profile, select its **Edit** link in the profile table.
   * To remove a profile, select its checkbox in the profile table, then select the **Delete** link.
3. In the Properties sub tab, specify the [properties](#Property) for configuring the JDashboard preferences and screen elements.

   Whether an option is available on the JDashboard window is determined by two factors: whether the corresponding feature is enabled in the selected profile and whether the property is enabled in the Properties tab. Only when both places are enabled can the option be available for use. If a feature is disabled in the profile, the corresponding option will be hidden from the JDashboard window even though it is enabled in the Properties tab.
4. Select **OK** to accept the profile settings.

The following table lists the properties for configuring the JDashboard settings and their usages. The properties for customizing the screen elements are classified for the two working modes of JDashboard: [Edit Mode](#Edit) and [View Mode](#View).

|  |  |
| --- | --- |
| **Option** | **Description** |
| Show Enter Parameter Values Dialog | Specifies whether to pop up the Enter Parameter Values dialog when you run a dashboard with parameters. |
| Right-select Menu | Specifies to show a shortcut menu when you select the right mouse button on a component, which can help you with most of the component operations in JDashboard. |
| Customize Component Title Bar > Component Title Bar | Specifies the way of showing the component title bar: Always Show, Show When Mouse Over or Never Show. When Never Show is selected, options for icons on the component title bar are disabled. |
| Customize Component Title Bar > Icon on Component Title Bar | Specifies the way of showing the icons on the component title bar: Always Show, Show When Mouse Over or Never Show. |
| Edit Mode properties | | | |
| Show Toolbar | Specifies whether or not to show the toolbar which contains the menu options for working with dashboards. For details about the usage of each toolbar icon and menu option, see [JDashboard Window Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009644862-JDashboard-Window-Elements). |
| Toolbar Icons | Specifies whether or not to display the following icons on the toolbar: Show Resources, New, Open, Save, Refresh, Enter Parameter Values, Export, Print, Clear Filters, Arrange, Responsive View, Options. |
| Options Menu | Specifies whether or not to display the following items on the Options menu: New, Open, Save, Save As, Export, Print, Clear Filters, Arrange, Auto Arrange, Responsive View, Set as Server Home, Component Title Bar, Share Parameter, Themes, Hide JDashboard Header, Help, Exit. Enabled when Options in the Toolbar Icons section is selected. |
| Themes > Default Theme | Specifies the default theme applied to dashboards. Enabled when Themes in the Options Menu section is selected. |
| Component Options Menu | Specifies whether or not to display the following items on the component options menu: Analyze, Edit Setting, Export, Delete, Refresh, About. In JDashboard the menu items available for different component types vary. |
| Show Dashboard Title Bar | Specifies whether or not to show the dashboard title bar that contains tabs labeling the names of the open dashboards. |
| View Mode properties | | | |
| Show Toolbar | Specifies whether or not to show the toolbar which contains the menu options for working with dashboards. |
| Toolbar Icons | Specifies whether or not to display the following icons on the toolbar: Refresh, Enter Parameter Values, Export, Print, Clear Filters, Responsive View, Options. |
| Options Menu | Specifies whether or not to display the following items on the Options menu: Export, Print, Clear Filters, Responsive View, Set as Server Home, Component Title Bar, Themes, Hide JDashboard Header, Help, Exit. Enabled when Options in the Toolbar Icons section is selected. |
| Themes > Default Theme | Specifies the default theme applied to dashboards. Enabled when Themes in the Options Menu section is selected. |
| Component Options Menu | Specifies whether or not to display the following items on the component options menu: Edit Setting, Export, About. |
| Show Dashboard Title Bar | Specifies whether or not to show the dashboard title bar that contains tabs labeling the names of the open dashboards. |
| View Dashboards in Responsive Mode | Specifies whether [responsive view](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#Responsive) is enabled by default when running dashboards in View Mode of JDashboard on computers. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644842-Opening-Visual-Analysis-in-JDashboard)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009667781-Visual-Analysis)
