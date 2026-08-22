---
title: "Configuring Server Profile"
id: 5741409420567
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile
updated_at: 2022-10-31T17:16:02Z
---

# Configuring Server Profile

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415874327-Configuring-Cache)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741409443095-Configuring-Proxy-for-Connecting-to-a-REST-Web-Service)

# Configuring Server Profile

This topic describes how you can customize the three parts of the server profile: Change Password, Customize Server Preferences, and Customize Profile, and how you can search for properties conveniently.

Administrators can define the initial settings of Logi Report Server and customize features for all users by creating server profiles via Administration > Server Profile on the Server Console. Any users can use one of the server profiles or configure their own profiles via **My Profile**.

There are three subjects in the server profile: [Change Password](#Password), [Customize Server Preferences](#Server), and [Customize Profile](#Profile).

* **Change Password** is available to My Profile only. You can change the password for signing into Server.
* **Customize Server Preferences** contains properties for customizing Server web pages and features, and has three further categories: [General](#General), [Export Formats](#Export), and [Advanced](#Advanced).
* **Customize Profile** is for applying a default profile for Page Report Studio, Web Report Studio, or JDashboard or customizing all the common and specific properties of Page Report Studio, Web Report Studio, and JDashboard together conveniently.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif)JDashboard is in maintenance mode, and we will not be adding new features to it. If you need more information, contact [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.).

You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/5741485252503-Working-with-Server-via-URL#Preference) to change the user password or load the Server Preferences page directly.

In addition, administrators can customize the allowed image types when report users insert images from the local file system into reports or dashboards in Page Report Studio, Web Report Studio, and JDashboard. To do this, on the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Upload**. Server displays the Upload page. Select the image types you want and then select **Save**. The setting takes effect after Server restarts.

This topic contains the following sections:

* [Customizing Your Server Profile](#CustomizeProfile)
* [Searching for Properties](#Search)
* [Profile Properties](#Properties)

## Customizing Your Server Profile

In the My Profile > Customize Profile page on the Server Console, you can set a default profile for Page Report Studio, Web Report Studio, or JDashboard. To do this, select a profile from the **Default Profile** drop-down list on the corresponding tab. Server displays the **Default** profile and all other profiles that server administrators have created in the drop-down list for your selection.

You can set the name of a profile for Page Report Studio, Web Report Studio, or JDashboard using the **jrs.profile** property when running page reports, web reports, or dashboards via URL or JavaScript API. Suppose that there is a Page Report Studio profile with the name **notoolbar**. You can set it in the URL for running a page report as follows:

`http://localhost:8888/jinfonet/tryView.jsp?jrs.report=%2fSampleReports%2fEmployee%20Information%20List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8&jrs.profile=notoolbar`

To specify a profile in JavaScript API, use the format `"jrs.profile":"PROFILE_NAME"`.

If you don't want to use the existing profiles, you can customize all the common and specific properties of Page Report Studio, Web Report Studio, and JDashboard together conveniently. Take the following steps:

1. Select **Customize Profile**. Server displays the [Customize Profile dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties).
2. By default, Server clears **Enable Customize Properties** for users on a new Server and new users. Select **Enable Customize Properties**.
3. Change the settings as you want. The properties on the Common tab are applicable to Page Report Studio, Web Report Studio, and JDashboard.
4. Select **OK**. Server applies your customized profile settings instead of the default profile you selected.

## Searching for Properties

On the My Profile > Customize Server Preferences and Customize Profile pages (excluding the **Features** sub tab in the Page Report Studio/Web Report Studio/JDashboard tab), you can search for the properties you want using the Search box. Type the text you want to search for, and Server lists the properties whose key values contain the matched text (you can define the key values of the properties using the <Value></Value> tags in the file **keywords.xml** in the `<install_root>\resources\server\languages\en\properties` and `<install_root>\resources\server\languages\en-us\properties` directories. You can customize the key values in any languages). In the search result list, select a property, and Server displays the page containing the property and highlights the matched text. When there are more than 10 results, you can select **More** at the end to show all the other results. After typing text in the Search box, you can also select the arrow ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/9905618988823/btn_mvdown1.gif) in the box to specify the following search properties. To cancel the search, clear the text or select the Delete button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905616261527/btn_dltobj.gif).

* **Highlight All**  
  Select if you want to highlight all matched text.
* **Match Case**  
  Select if you want to search for text that meets the case of the typed text.
* **Match Whole Word**  
  Select if you want to search for text that matches the whole property name as defined in the <UIName></UIName> tags in **keywords.xml**. You can customize the <UIName></UIName> tags if you want. When you select this property, Server ignores the key values of the properties.

## Profile Properties

The following table lists the profile properties in the Server Profile and My Profile.

| Option | Description |
| --- | --- |
| Change Password (Available to My Profile) | |
| Logged in User's Password | The password of the currently signed-in user. |
| User ID | The ID of the current user. |
| New Password | The new password. |
| Confirm New Password | Type the new password again. |
| Customize Server Preferences | |
| Allow users to modify preferences from user console | Select if you want to allow users to modify the server preferences on the My Profile page of the Server Console. Available only on the Administration > Server Profile > Customize Server Preferences page of the Server Console. |
| General | |
| Home Page | Select the default home page for the Server Console: the Start Page, a dashboard (available when you have the JDashboard license), or the Server Console page. |
| Default Format for Viewing Report | The default format for viewing reports. By default, **Web/Page Studio** is selected, which means that page reports open in Page Report Studio and web reports in Web Report Studio. If the property **Default Format for Viewing Report** of a page report tab or web report has been set to a specific format when the report was designed in Logi Report Designer, the value in Designer has higher priority than the one here. |
| Default View for Page Report Studio | The default view of Page Report Studio when running page reports in Page Report Studio by selecting report names or via URL:  * **Basic View**  Page Report Studio runs in Basic View by default. You can switch to Interactive View if it is available. * **Basic View Only**  Select if you want Page Report Studio to run in Basic View only. You cannot switch to Interactive View. * **Interactive View** Select if you want Page Report Studio to run in Interactive View by default. You can switch to Basic View if it is available. |
| Default Mode for Web Report Studio | The default mode of Web Report Studio when running web reports in Web Report Studio by selecting report names or via URL:  * **View Mode** Web Report Studio runs in View Mode by default. You can switch to Edit Mode if it is available. * **View Mode Only** Select if you want Web Report Studio to run in View Mode only. You cannot switch to Edit Mode. * **Edit Mode** Select if you want Web Report Studio to run in Edit Mode by default. You can switch to View Mode if it is available. |
| Default Mode for JDashboard | The default mode for viewing dashboards in JDashboard. You can choose between View Mode and Edit Mode. The property is available when you have the JDashboard license. |
| Use Major Sort as Default | Server uses major sort as the default sort rule when sorting summary tables in Web Report Studio or JDashboard, which is to sort data by the last sort condition only. Clear this property if you want to apply minor sort, which is to sort lower groups based on the sort result of all its higher-level groups. |
| Open All Reports and Dashboards in New Window | By default, Server displays Web Report Studio, Page Report Studio, and JDashboard in a new window. Clear this property if you want to embed them in the current window. Note icon When you do not have the JDashboard license, the property name is **Open All Reports in New Window**. |
| Use Wizard for Web Report Studio | You can create web reports using two methods: the quick start method to create a table report, which is the default method when you clear **Yes**, and the traditional method using a wizard when you select **Yes**. For more information, see [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741464180119-Web-Report-Studio-Server-v19). |
| Only Display CSS Styles in Style List | By default, Server displays only the CSS styles in the style list. |
| Display the Last Login Time | By default, Server displays the time you last signed in, on the top banner of the Server Console, and records the time in the login.properties file in `<install_root>\bin` after it shuts down. |
| Display the Last Logout Time | Select if you want to display the time you last signed out, on the top banner of the Server Console. Server records the time in the logout.properties file in `<install_root>\bin` after it shuts down. |
| Keep Completed Tasks for | The number of days Server keeps the completed tasks in the Completed list. The default value 0 means Server keeps the completed tasks until you delete them from the Completed page. |
| Parameter Display Size | The display length in characters of the parameters that you want to apply to both the completed and active schedules. |
| Folder Selector Type | Select the type of the tool used for selecting folder paths from the file system. This property is available on the Internet Explorer browser and applies to local published reports only. There are three types of folder selectors:   * **JavaScript format**  Folder selector is a dialog box generated by JavaScript. * **VBScript format**  Folder selector is a dialog box generated by VBScript. * **JSP format** Folder selector is an HTML page generated by JSP. This format is available to administrators only. |
| Skin Format | Select the skin format you want to apply to the Server Console and Page Report Studio UI: Standard, Classical, and Windows XP. |
| Columns Shown in \_ List | Select the columns you want to display as default in the following list when you sign in to Logi Report Server: Resources, Scheduled, Running, Completed, Background Tasks, Report Result Versions, Report Versions, Catalog Versions, and Result Versions. |
| Show Loading Icon When Refreshing | By default, Server shows the loading icon when refreshing reports or dashboards. |
| Enable IE Navigate2 | Select if you want to load resources with the IE Navigate2 method and its flags setting when viewing reports or loading URL links in Internet Explorer. |
| This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Create and Export Reports in New Window | Specify whether to display reports in a new window when creating reports on the Server Console, or in Web/Page Report Studio creating/opening reports or exporting reports with View Report Result. Clear this property if you want to display reports in the current window. |
| Export Formats | |
| Logi Report Result | The default properties for exporting a page report to a Logi Report result file (RST file). You can export RST files to HTML, PDF, Text, Excel, XML, RTF, and Postscript formats via Server.  * **Use Custom File Extension** Select if you want the output file to have no file extension or want to use a different file extension from the default one (.rst). * **Zip Result**  Select if you want to compress the result and make its size smaller. |
| Page Report Result | The default properties for exporting a report in the Page Report Result format.  * **Use Custom File Extension** Select if you want the output file to have no file extension or want to use a different file extension from the default one (.rsd). * **Resolution**  The resolution of the report to zoom in/out, in DPI. Server obtains the default value from the operation system, which is the resolution of your monitor, for example, 72 DPI on UNIX or 96 on Windows. You can set a higher/lower value to zoom in/out. |
| HTML | The default properties for exporting a report in HTML. For more information, see [HTML](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#HTML). |
| PDF | The default properties for exporting a report in PDF.  * **Keep Scrollable Chart Status** Select to keep the current data status of scrollable charts. * **Clipping Area**  Select to hide the contents that extends beyond a specific area due to limited space.   For more information, see [PDF](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#PDF). |
| Excel | The default properties for exporting a report in Excel. For more information, see [Excel](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#Excel). |
| Text | The default properties for exporting a report in Text. For more information, see [Text](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#Text). |
| RTF | The default properties for exporting a report in RTF. For more information, see [RTF](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#RTF). |
| XML | The default properties for exporting a report in XML. For more information, see [XML](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#XML). |
| PostScript | The default properties for exporting a report in PostScript. For more information, see [PostScript](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#PS). |
| Advanced | |
| Enable Waiting Page | By default, Server shows the waiting page. You can select **Customize** to customize the waiting page in the [Customize Waiting Page](https://devnet.logianalytics.com/hc/en-us/articles/5741426929303-Customize-Waiting-Page-Dialog-Box-Properties) dialog box. The property is available on the Administration > Server Profile > Customize Server Preferences page of the Server Console. |
| Specify Default Language | Select **Yes** and then select a language if want to use the language as the Server environment language. Server displays all UI text and messages in the specified language. The available languages come from the qualified language packages you defined in `<install_root>\resources\server\languages`. By default, there are two built-in English language packages: **en** and **en-us**. You can add more language packages following [NLS at Application Level](https://devnet.logianalytics.com/hc/en-us/articles/5741474708887-NLS-at-Application-Level).  * **Language** Select the environment language of Logi Report Server. * **Reset All Users' Preference**  Select if you want to reset all users' default language to the one you selected from the **Language** drop-down list. The property is only available on the Administration > Server Profile page of the Server Console. |
| Enable NLS | Select **Yes** and then select the default language and encoding if you want to enable the NLS feature for when directly running reports and dashboards. The property is only available on the My Profile page of the Server Console.  * **Default Language** Select the default language in which you want to display reports and dashboards. * **Default Encoding** Select the default encoding for reports and dashboards. |
| Time Zone Setting | You can change the time zone for displaying date and time on Logi Report Server UI and in reports and parameters. Choose from the following:   * **VM Time Zone** Server uses the time zone of your machine where you installed Logi Report Server. * **User Specified Time Zone** Select if you want to use another time zone. Then select one from the **Time Zone** drop-down list. * **Use Setting in Server Profile** You see this property when you are accessing **My Profile**. Select **Use Setting in Server Profile** if you want to use the time zone that the server administrator defined in the Server Profile.   Server uses the submitter's real-time time zone setting to run a scheduled task. |
| Specify Date Time Format | Select the default date and time formats in which you want to display date and time on the Server Console, for example, the last modified time of a report, and the time when a schedule task finished. |
| Override Style Group | Select the default style group that you want to apply when running reports on Server, including direct running, advanced running, and scheduled running. Page Report Studio also exports reports with this default style group if you do not specify another one. |
| Identify Server Preference | You can manually select a clustered server to perform a task when scheduling a report. The property is available only in the Cluster environment. |
| Use Accessible Version | Select if you want to set the accessible version of Logi Report Server as the default portal instead of the Server Console. In the accessible version, Server displays reports in HTML with accessibility attributes, and outputs tables and crosstabs as HTML data tables. With the help of a reader agent, you can navigate through the server resource to view the target report. For more information, select [Making HTML and PDF Report Outputs and Server Console Accessible](https://devnet.logianalytics.com/hc/en-us/articles/5741473969431-Making-HTML-and-PDF-Report-Outputs-and-Server-Console-Accessible). |
| Enable Saving Parameter Values | Select **Yes** if you want to save parameter values for reuse when specifying parameter values to run reports or dashboards. You need to further choose a way of saving the parameter values: **Manually** or **Automatically**. When you switch from one to the other and then select **OK**, Server clears all parameter values you saved. For a report/dashboard that has multiple parameters, Server saves the values of all the parameters you specified at a time together as a group for the report/dashboard. The group is also called a list. Selecting a group as the value will apply the values in the group to all the corresponding parameters in the report/dashboard.   * **Manually**  Select if you want to manually save the parameter values you are going to reuse frequently and manage the saved values. Then in cases when you are asked to specify parameter values, Server also provides the properties for using saved parameter values, saving the specified values, and deleting the saved values. * **Automatically**  Select if you want Server to save submitted parameter values on a user-report or user-dashboard basis. The automatically saved parameter value groups will be available in the value drop-down list of each of those parameters next time when the same user is asked to specify parameter values for the same report or dashboard. Selecting a group from any of the parameters' value lists will apply the saved group of values to all the parameters. A parameter value group in the value lists is a one-row values' set. It lists the values of the parameters in one row with blank to separate between parameters, and the values are in an order same as the display order of the parameters. * **Maximum Number of Auto Complete Parameters List**  For both manually and automatically saved parameter value groups or lists for a report/dashboard, there is a number restriction. By default, it is 3, which means the manually saved parameter value lists or auto saved lists for a report or dashboard can be no more than three. When the saved lists exceed the maximum number or if you change the current number to a smaller one, Server removes the oldest lists. |
| Enable Setting Default Parameter Values For | By default, Server displays **Save as default** on the parameter page, which enables you to customize the default parameter values for reports or dashboards on a user-report or user-dashboard basis.  * **Page Report**  You can set default parameter values for page reports. * **Web Report** You can set default parameter values for web reports. * **Dashboard**  You can set default parameter values for dashboards in JDashboard. The property is available when you have the JDashboard license. |
| Enable Hiding Initial Parameter Dialog For | By default, Server displays **Do not show this screen again** in the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/5741442503831-Enter-Parameter-Values-Dialog-Box-Properties) dialog box or **Re-enable Parameter Screen** in the [Parameter Settings](https://devnet.logianalytics.com/hc/en-us/articles/5741433447063-Parameter-Settings-Dialog-Box-Properties) dialog box or the [Parameter panel](https://devnet.logianalytics.com/hc/en-us/articles/5741490884759-Applying-Parameters-to-Web-Report), which enables you to hide the initial parameter dialog box brought by actions on the Server Console to run a report on a user-report basis.  * **Page Report**  You can hide the initial parameter dialog box for running page reports. * **Web Report** You can hide the initial parameter dialog box for running web reports. |
| Enable Setting Default On-screen Filter Values For | You can customize the default on-screen filter values of a report/dashboard on a user-report/user-dashboard basis. The property is available only on the Administration > Server Profile page of the Server Console.  * **Page Report** Page Report Studio displays the [On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/5741483215255-Page-Report-Studio-Window-Elements#OnScreen) item on the **Report** menu. * **Web Report** Web Report Studio displays the [On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/5741484883735-Web-Report-Studio-Window-Elements#OnScreen) item on the **Edit** menu. * **Dashboard** JDashboard displays the [On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/5741423794583-JDashboard-Window-Elements#OnScreen) item on the **Options** list. The property is available when you have the JDashboard license. |
| Case-Sensitive Login User Name | Username for signing into the Server Console is case sensitive by default. Clear the property if you do not want the usernames to be case sensitive. The property is available only on the Administration > Server Profile > Customize Server Preferences page of the Server Console. |
| Customize Profile | |
| Customize Profile | This property is available to My Profile. Select it if you want to customize your Server profile. Server then displays the [Customize Profile dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties). |
| Page Report Studio | |
| You can customize preferences and features of Page Report Studio. For more information, see [Customizing Page Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/5741439209879-Customizing-Page-Report-Studio-Profile). | |
| Web Report Studio | |
| You can customize preferences and features of Web Report Studio. For more information, see [Customizing Web Report Studio Profile](https://devnet.logianalytics.com/hc/en-us/articles/5741456214039-Customizing-Web-Report-Studio-Profile). | |
| JDashboard | |
| You can customize preferences and features of JDashboard. The tab is available when you have the JDashboard license. For more information, see [Customizing JDashboard Profile](https://devnet.logianalytics.com/hc/en-us/articles/5741401784855-Customizing-JDashboard-Profile). | |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415874327-Configuring-Cache)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741409443095-Configuring-Proxy-for-Connecting-to-a-REST-Web-Service)
