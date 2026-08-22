---
title: "Customizing JDashboard Profile"
id: 4405683597719
section: "Introduction to the Logi Report JDashboard Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683597719-Customizing-JDashboard-Profile
updated_at: 2022-01-27T07:58:34Z
---

# Customizing JDashboard Profile

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690497559-Opening-Visual-Analysis-in-JDashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683602199-Customizing-the-JDashboard-UI)

# Customizing JDashboard Profile

You can configure the preferences and features of JDashboard using the Server Console. This topic describes how to configure server profile for all users and configure user profile for yourself, and describes the properties of JDashboard profile.

Administrators can provide default settings for running JDashboard for all users, in the Server Profile. Any user can configure JDashboard preferences in the My Profile for themselves, that is, they can decide whether to disable the features that administrators have enabled.

**To configure JDashboard preferences and features:**

1. Choose according to your user account:
   * Anyone can configure for themselves: go to the **My Profile** > **Customize Profile** > **JDashboard** tab.
   * Administrators can configure for all users: go to the **Administration** > **Server Profile** > **Customize Profile** > **JDashboard** tab.
2. In the **Features** tab, select the feature profile from the **Default Profile** list which will determine the features that are available in JDashboard.

   ![Features tab](https://devnet.logianalytics.com/hc/article_attachments/4420453392919/profile_featr.gif)

   Logi Report provides a **Default** profile in which Server enables all the JDashboard features. Administrators can create, edit, or remove the customized feature profiles. End users can only select a profile and view its settings.

   * To create a profile, select **New Profile**. In the [JDashboard Profile dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683748759-JDashboard-Profile-Properties), create the profile.
   * To edit a profile, select **Edit** in the profile table.
   * To remove a profile, select it in the profile table, then select **Delete**.
3. In the **Properties** tab, specify the [properties](#Property) for configuring the JDashboard preferences and screen elements.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) Whether a command is available in the JDashboard window depends on two factors: whether you have enabled the corresponding feature in the selected profile and whether you have enabled the property in the **Properties** tab. If you disable a feature in the profile, JDashboard will hide the corresponding command from the window even though you have enabled it in the **Properties** tab.
4. Select **OK** to accept the profile settings.

The following table describes the properties for configuring the JDashboard settings. The properties for customizing the screen elements are classified for the two working modes of JDashboard: [Edit Mode](#Edit) and [View Mode](#View).

| Option | Description |
| --- | --- |
| Show Enter Parameter Values Dialog | Select to display the Enter Parameter Values dialog box when running dashboards with parameters. |
| Use User Defined Default Parameter Values | Select to use your saved default parameter values in the Enter Parameter Values dialog box to run dashboards by default, when the dialog box does not display. |
| Right-click Menu | Select to show a shortcut menu when right-clicking a component, which can help with most of the component operations in JDashboard. |
| Show Description When Hovering Over Table Header Labels | Select if you want to display the description of the related data field when you hover over a label in the table header in JDashboard. |
| Edit Menu > Component Title Bar | Select the way of showing the component title bar: Always Show, Show When Mouse Over, or Never Show. When you select **Never Show**, Server disables the **Icon on Component Title Bar** property. |
| Edit Menu > Icon on Component Title Bar | Select the way of showing the icons on the component title bar: Always Show, Show When Mouse Over, or Never Show. |
| Edit Mode properties | |
| Show Toolbar | Select to show the toolbar which contains the menu commands for working with dashboards. For more information, see [JDashboard Window Elements](https://devnet.logianalytics.com/hc/en-us/articles/4405683603479-JDashboard-Window-Elements). |
| Toolbar Icons | Select the items you want to display on the toolbar. |
| Options Menu | Server enables the items in this box when you selected **Options** in the **Toolbar Icons** box. Select the items you want to display on the **Options** menu. |
| Themes > Default Theme | Select the default theme to apply to dashboards. |
| Component Options Menu | Select the items you want to display on the **Options** menu on the component title bar. In JDashboard the menu items available for different component types vary. |
| Show Dashboard Title Bar | Select to display the dashboard title bar that contains tabs labeling the names of the open dashboards. |
| View Mode properties | |
| Show Toolbar | Select to show the toolbar which contains the menu commands for working with dashboards. |
| Toolbar Icons | Select the items you want to display on the toolbar. |
| Options Menu | Server enables the items in this box when you selected **Options** in the **Toolbar Icons** box. Select the items you want to display on the **Options** menu. |
| Themes > Default Theme | Select the default theme to apply to dashboards. |
| Component Options Menu | Select the items you want to display on the **Options** menu on the component title bar. In JDashboard the menu items available for different component types vary. |
| Show Dashboard Title Bar | Select to display the dashboard title bar that contains tabs labeling the names of the open dashboards. |
| View Dashboards in Responsive Mode | Select to enable [Responsive View](https://devnet.logianalytics.com/hc/en-us/articles/4405690495383-General-Operations-in-JDashboard#Responsive) by default when running dashboards in the view mode of JDashboard, which you access from a computer.  * **Fold Components When Width <=**   Specify a percentage between 50% and 100%. When the available width for a library component is within the specified percentage of the original component width, the rightmost components in the same row move to a new row, until there is only one component in a row. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690497559-Opening-Visual-Analysis-in-JDashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683602199-Customizing-the-JDashboard-UI)
