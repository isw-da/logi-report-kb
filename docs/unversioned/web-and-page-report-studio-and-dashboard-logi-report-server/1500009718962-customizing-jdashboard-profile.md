---
title: "Customizing JDashboard Profile"
id: 1500009718962
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718962-Customizing-JDashboard-Profile
updated_at: 2021-07-25T07:20:13Z
---

# Customizing JDashboard Profile

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745141-Opening-Visual-Analysis-in-JDashboard)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719022-Customizing-the-JDashboard-UI)

# Customizing JDashboard Profile

Preferences and features of JDashboard can be configured by profile in the Logi Report Server console. The Administration > Server Profile > Customize Profile page is available to administrators and provides default settings for running JDashboard, and controls whether the settings in the My Profile > Customize Profile page can be configured. Administrators may change the settings in the Server Profile > Customize Profile page so as to enable or disable some features. Then end users can configure JDashboard preferences in the My Profile > Customize Profile page for their own, that is, they can decide whether or not to enable the features which have been enabled by administrators.

**To configure JDashboard preferences and features:**

1. Make a choice according to your user account:
   * Anyone can configure for himself: go to the **My Profile** > **Customize Profile** > **JDashboard** tab.
   * Administrators can configure for all users: go to the **Administration** > **Server Profile** > **Customize Profile** > **JDashboard** tab.
2. In the Features sub tab, select the feature profile from the Default Profile drop-down list which will determine the features that are available in JDashboard.

   ![Features tab](https://devnet.logianalytics.com/hc/article_attachments/4404936714135/profile_featr.gif)

   Logi Report provides a Default profile in which all the JDashboard features are enabled. Administrators can create, edit or remove the customized feature profiles. End users can only select a profile and view its settings.

   * To create a profile, click the **New Profile** link. In the [JDashboard Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009720582-JDashboard-Profile) dialog box, create the profile.
   * To edit a profile, select its **Edit** link in the profile table.
   * To remove a profile, select its check box in the profile table, then select the **Delete** link.
3. In the Properties sub tab, specify the [properties](#Property) for configuring the JDashboard preferences and screen elements.

   Whether an option is available in the JDashboard window is determined by two factors: whether the corresponding feature is enabled in the selected profile and whether the property is enabled in the Properties tab. Only when both places are enabled can the option be available for use. If a feature is disabled in the profile, the corresponding option will be hidden from the JDashboard window even though it is enabled in the Properties tab.
4. Select **OK** to accept the profile settings.

The following table lists the properties for configuring the JDashboard settings and their usages. The properties for customizing the screen elements are classified for the two working modes of JDashboard: [Edit Mode](#Edit) and [View Mode](#View).

| Option | Description |
| --- | --- |
| Show Enter Parameter Values Dialog | Specifies whether to pop up the Enter Parameter Values dialog box when running dashboards with parameters. |
| Use User Defined Default Parameter Values | Specifies whether to use the user saved default parameter values in the Enter Parameter Values dialog box to run dashboards by default when the dialog box is not prompted. |
| Right-click Menu | Specifies to show a shortcut menu when selecting the right mouse button on a component, which can help with most of the component operations in JDashboard. |
| Customize Component Title Bar > Component Title Bar | Specifies the way of showing the component title bar: Always Show, Show When Mouse Over or Never Show. When Never Show is selected, options for icons on the component title bar are disabled. |
| Customize Component Title Bar > Icon on Component Title Bar | Specifies the way of showing the icons on the component title bar: Always Show, Show When Mouse Over or Never Show. |
| Edit Mode properties | |
| Show Toolbar | Specifies whether or not to show the toolbar which contains the menu options for working with dashboards. For details about the usage of each toolbar icon and menu option, see [JDashboard Window Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009745161-JDashboard-Window-Elements). |
| Toolbar Icons | Specifies whether or not to display the following icons on the toolbar: Show Resources, New, Open, Save, Refresh, Enter Parameter Values, Export, Print, Clear Filters, Arrange, Options. |
| Options Menu | Specifies whether or not to display the following items on the Options menu: New, Open, Save, Save As, Export, Print, Clear Filters, Arrange, Auto Arrange, Set as Server Home, Component Title Bar, Share Parameter, Themes, Hide JDashboard Header, Help, Exit. Enabled when Options in the Toolbar Icons section is selected. |
| Themes > Default Theme | Specifies the default theme applied to dashboards. Enabled when Themes in the Options Menu section is selected. |
| Component Options Menu | Specifies whether or not to display the following items on the component's Options menu: Analyze, Edit Setting, Export, Delete, Refresh, About. In JDashboard the menu items available for different component types vary. |
| Show Dashboard Title Bar | Specifies whether or not to show the dashboard title bar that contains tabs labeling the names of the open dashboards. |
| View Mode properties | |
| Show Toolbar | Specifies whether or not to show the toolbar which contains the menu options for working with dashboards. |
| Toolbar Icons | Specifies whether or not to display the following icons on the toolbar: Refresh, Enter Parameter Values, Export, Print, Clear Filters, Responsive View, Options. |
| Options Menu | Specifies whether or not to display the following items on the Options menu: Export, Print, Clear Filters, Responsive View, Set as Server Home, Component Title Bar, Themes, Hide JDashboard Header, Help, Exit. Enabled when Options in the Toolbar Icons section is selected. |
| Themes > Default Theme | Specifies the default theme applied to dashboards. Enabled when Themes in the Options Menu section is selected. |
| Component Options Menu | Specifies whether or not to display the following items on the component's Options menu: Edit Setting, Export, About. |
| Show Dashboard Title Bar | Specifies whether or not to show the dashboard title bar that contains tabs labeling the names of the open dashboards. |
| View Dashboards in Responsive Mode | Specifies whether [responsive view](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#Responsive) is enabled by default when running dashboards in view mode of JDashboard on computers.  * **Fold Components When Width <=**   Specifies a compression ratio between 50% and 100% to determine when components will be folded. Each time when the available width for a library component is reduced within the ratio of the component original width, the rightmost components in the same row will be placed in a new row. This goes on until there is only one component in a row. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745141-Opening-Visual-Analysis-in-JDashboard)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719022-Customizing-the-JDashboard-UI)
