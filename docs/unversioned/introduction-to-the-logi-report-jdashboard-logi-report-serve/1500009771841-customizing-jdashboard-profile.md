---
title: "Customizing JDashboard Profile"
id: 1500009771841
section: "Introduction to the Logi Report JDashboard Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771841-Customizing-JDashboard-Profile
updated_at: 2021-07-24T00:49:23Z
---

# Customizing JDashboard Profile

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743962-Opening-Visual-Analysis-in-JDashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743942-Customizing-the-JDashboard-UI)

# Customizing JDashboard Profile

You can configure the preferences and features of JDashboard by profile in the Server Console. This topic describes how to configure server profile for all users and configure user profile for self, and describes the properties of JDashboard profile.

Administrators can provide default settings for running JDashboard for all users, in the Server Profile. All users can configure JDashboard preferences in the My Profile for their own, that is, they can decide whether to disable the features that administrators have enabled.

**To configure JDashboard preferences and features:**

1. Make a choice according to your user account:
   * Anyone can configure for self: go to the **My Profile** > **Customize Profile** > **JDashboard** tab.
   * Administrators can configure for all users: go to the **Administration** > **Server Profile** > **Customize Profile** > **JDashboard** tab.
2. In the **Features** tab, select the feature profile from the **Default Profile** drop-down list which will determine the features that are available in JDashboard.

   ![Features tab](https://devnet.logianalytics.com/hc/article_attachments/4404885306647/profile_featr.gif)

   Logi Report provides a **Default** profile in which Server enables all the JDashboard features. Administrators can create, edit, or remove the customized feature profiles. End users can only select a profile and view its settings.

   * To create a profile, select **New Profile**. In the [JDashboard Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009746042-JDashboard-Profile-Properties) dialog box, create the profile.
   * To edit a profile, select **Edit** in the profile table.
   * To remove a profile, select its check box in the profile table, then select **Delete**.
3. In the **Properties** tab, specify the [properties](#Property) for configuring the JDashboard preferences and screen elements.

   Whether an option is available in the JDashboard window depends on two factors: whether you have enabled the corresponding feature in the selected profile and whether you have enabled the property in the **Properties** tab. Only when you have enabled them in both places can the option be available for use. If you disable a feature in the profile, JDashboard will hide the corresponding option from the window even though you have enabled it in the **Properties** tab.
4. Select **OK** to accept the profile settings.

The following table describes the properties for configuring the JDashboard settings. The properties for customizing the screen elements are classified for the two working modes of JDashboard: [Edit Mode](#Edit) and [View Mode](#View).

| Option | Description |
| --- | --- |
| Show Enter Parameter Values Dialog | Specifies whether to pop up the Enter Parameter Values dialog box when running dashboards with parameters. |
| Use User Defined Default Parameter Values | Specifies whether to use the user saved default parameter values in the Enter Parameter Values dialog box to run dashboards by default when the dialog box is not prompted. |
| Right-click Menu | Specifies to show a shortcut menu when selecting the right mouse button on a component, which can help with most of the component operations in JDashboard. |
| Customize Component Title Bar > Component Title Bar | Specifies the way of showing the component title bar: Always Show, Show When Mouse Over or Never Show. When Never Show is selected, options for icons on the component title bar are disabled. |
| Customize Component Title Bar > Icon on Component Title Bar | Specifies the way of showing the icons on the component title bar: Always Show, Show When Mouse Over or Never Show. |
| Edit Mode properties | |
| Show Toolbar | Specifies whether to show the toolbar which contains the menu options for working with dashboards. For more information, see [JDashboard Window Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009743982-JDashboard-Window-Elements). |
| Toolbar Icons | Specifies whether to display the following icons on the toolbar: Show Resources, New, Open, Save, Refresh, Enter Parameter Values, Export, Print, Clear Filters, Arrange, Options. |
| Options Menu | Specifies whether to display the following items on the Options menu: New, Open, Save, Save As, Export, Print, Clear Filters, Arrange, Auto Arrange, Set as Server Home, Component Title Bar, Share Parameter, Themes, Hide JDashboard Header, Help, Exit. Enabled when Options in the Toolbar Icons section is selected. |
| Themes > Default Theme | Specifies the default theme applied to dashboards. Enabled when Themes in the Options Menu section is selected. |
| Component Options Menu | Specifies whether to display the following items on the component's Options menu: Analyze, Edit Setting, Export, Delete, Refresh, About. In JDashboard the menu items available for different component types vary. |
| Show Dashboard Title Bar | Specifies whether to show the dashboard title bar that contains tabs labeling the names of the open dashboards. |
| View Mode properties | |
| Show Toolbar | Specifies whether to show the toolbar which contains the menu options for working with dashboards. |
| Toolbar Icons | Specifies whether to display the following icons on the toolbar: Refresh, Enter Parameter Values, Export, Print, Clear Filters, Responsive View, Options. |
| Options Menu | Specifies whether to display the following items on the Options menu: Export, Print, Clear Filters, Responsive View, Set as Server Home, Component Title Bar, Themes, Hide JDashboard Header, Help, Exit. Enabled when Options in the Toolbar Icons section is selected. |
| Themes > Default Theme | Specifies the default theme applied to dashboards. Enabled when Themes in the Options Menu section is selected. |
| Component Options Menu | Specifies whether to display the following items on the component's Options menu: Edit Setting, Export, About. |
| Show Dashboard Title Bar | Specifies whether to show the dashboard title bar that contains tabs labeling the names of the open dashboards. |
| View Dashboards in Responsive Mode | Specifies whether to enable [Responsive View](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#Responsive) by default when running dashboards in view mode of JDashboard on computers.  * **Fold Components When Width <=**   Specifies a compression ratio between 50% and 100% to determine when components will be folded. Each time when the available width for a library component is reduced within the ratio of the component original width, the rightmost components in the same row will be placed in a new row. This goes on until there is only one component in a row. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743962-Opening-Visual-Analysis-in-JDashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743942-Customizing-the-JDashboard-UI)
