---
title: "Accessing Logi Report Server via a Web Browser"
id: 4405690636055
section: "Starting, Accessing, and Shutting Down Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690636055-Accessing-Logi-Report-Server-via-a-Web-Browser
updated_at: 2022-01-27T07:59:35Z
---

# Accessing Logi Report Server via a Web Browser

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690637847-Sending-Commands-to-Logi-Report-Server-from-Java)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690639639-Shutting-Down-Logi-Report-Server)

# Accessing Logi Report Server via a Web Browser

You can access Logi Report Server through a web browser such as Internet Explorer, Firefox, and Google Chrome. This topic describes how you can sign in to the Server Console locally or via URL, search for resources and properties on the Server Console, and sign out.

The Logi Report Server Console provides a unified UI for normal users and administrators (users who have the "administrators" role, also referred to as administrators) to access and manage server resources depending on authorization. Normal users can perform report related tasks such as running and creating reports and dashboards, starting visual analysis, and customizing their own server preferences. Administrators can also perform administrative tasks such as managing security and databases, configuring the server, and setting up a Cluster.

This topic contains the following sections:

* [Signing in to the Server Console Locally](#Local)
* [Signing in to the Server Console by URL](#URL)
* [Additional Channel for Administrators to Sign In](#Admin)
* [Searching for Resources on the Server Console](#Search)
* [Signing out of Logi Report Server](#Shut)

## Signing in to the Server Console Locally

To access the Server Console from the same machine on which you installed Logi Report Server, take the following steps:

1. Start Logi Report Server.
2. Server displays a welcome page automatically in your default web browser. Provide your username and password as assigned by your administrator.

   When Server enables [Organization](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations) and your user account belongs to an organization, you need to also specify the correct organization name. The default organization name **System** means that you do not belong to any organizations. Select **Remember Me** if you want Server to remember your information.

   ![Login dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461600151/launch_acs_login.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)Username for signing in to the Server Console should be case sensitive by default. You can change this by clearing the **Case-Sensitive Login User Name** option in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#UserName), if you are an administrator.
3. Select **LOGIN**. Server displays the home page of the Server Console which can be the Start Page, the Console page, or a dashboard depending on the Home Page setting in the server profile.

   The Start Page is the default home page of the Server Console. It provides quick entries to some key functions. Choose a topic to start your work on the server.

   ![Start Page](https://devnet.logianalytics.com/hc/article_attachments/4420453530135/launch_acs_strtpg.gif)

   | Option | Description |
   | --- | --- |
   | How To | |
   | Feature Guide | Select if you want to read Logi Report Feature Guide about Logi Report's main features. |
   | Demo | Select if you want to view dashboards and reports demos. |
   | Tutorial | Select if you want to read Logi Report Tutorial. |
   | Create | |
   | Dashboard | Select if you want to [create a dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4405683594647-Creating-and-Saving-Dashboards). |
   | Web Report | Select if you want to [create a web report](https://devnet.logianalytics.com/hc/en-us/articles/4405690690711-Quick-Start-with-a-Table-Report). |
   | Page Report | Select if you want to [create a page report](https://devnet.logianalytics.com/hc/en-us/articles/4405683950743-Creating-Page-Reports). |
   | Open | |
   | My Folder | Select if you want to open the My Reports folder on the Server Console. |
   | Public Folder | Select if you want to open the Public Reports folder on the Server Console. |
   | Manage | |
   | My Profile | Select if you want to open the Server Console > My Profile > Customize Server Preferences page for [configuring the server profile settings](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile) of your own. |
   | Schedule | Select if you want to [schedule a task to run a report](https://devnet.logianalytics.com/hc/en-us/articles/4405684005015-Scheduling-Tasks-to-Run-Reports). |
   | Administration | Select if you want to open the Server Console > Administration > Configuration > Advanced page for managing the server advanced resources. Available to administrators only. |
   | Others | |
   | Username | The name of the current user who signed in. |
   | Logout button | Select if you want to sign out of the server. |
   | User's Guide | Select if you want to read Logi Report Server Guide. |
   | Logi Report Home Page | Select if you want to go to the Logi Analytics home page. |
   | Contact Support | Select if you want to go to the Logi Analytics support portal. |
   | Do not show this page at start up | Select if you want to access the Server Console instead of Start Page as the home page after Server starts next time. You can display Start Page by selecting the **Start Page** icon Start Page button on the system toolbar of the Server Console. |

## Signing in to the Server Console by URL

Sometimes you may have closed the Start Page or the Server Console page while the local server remains started, or you are accessing the Server Console from a remote computer, you can access it by URL:

1. Open a web browser and set the URL to `http://IP_or_HostName_or_DomainName:port` (by default the port for accessing the Server Console is 8888).

   If you do not know the IP address of the machine on which the server runs, and it is the same machine where you are going to sign in, you can use **localhost** instead of the IP address. You can also open a console window such as telnet on the server computer and type **hostname** to get the name of the host.
2. Server displays the welcome page. Type your username and password as assigned by your administrator.
3. Select **LOGIN**. Server displays the Server home page.

## Additional Channel for Administrators to Sign In

Logi Report Server provides a special channel that automatically creates an extra user session for management purposes if the license limit of the maximum number of concurrent users has been reached. You cannot use the extra user session to run reports or submit schedule tasks. You can only perform management operations as an administrator. If your Logi Report Server license has a bounded limit to the maximum number of concurrent users, this feature will take effect.

Server creates only one extra valid user session within this special channel at any time. If an extra user session already exists and is still valid, Server displays a confirmation page asking you whether to close the existing extra user session. Only when you close the existing user session can Logi Report Server start a new user session for you to perform management operations. Otherwise, you cannot sign in to Logi Report Server.

## Searching for Resources on the Server Console

On the Server Console, you can make use of the Global Search feature to search for the resources and options you need. You can perform global search anywhere on the Server Console to search among the following:

* [Report resources](https://devnet.logianalytics.com/hc/en-us/articles/4405683925143-Managing-Resources) such as reports, catalogs, dashboards, library components, and folders in the server resource tree.
* [Scheduled and background tasks](https://devnet.logianalytics.com/hc/en-us/articles/4405683937303-Managing-Report-Running-Tasks).
* Options in the [My Profile](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile) > Customize Server Preferences and Customize Profile pages (excluding the Features sub tab in the Page Report Studio/Web Report Studio/JDashboard tab).
* [Users](https://devnet.logianalytics.com/hc/en-us/articles/4405684026007-Managing-User-Accounts), [groups](https://devnet.logianalytics.com/hc/en-us/articles/4405684021783-Managing-Groups), [roles](https://devnet.logianalytics.com/hc/en-us/articles/4405684024983-Managing-Roles), and [organizations](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations) in the Administration > Security page that is available to administrators only.

To use global search, select the **Global Search** button ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4420447195799/btn_srchglbl.gif) on the system toolbar. Server displays the following search page.

![Global Search](https://devnet.logianalytics.com/hc/article_attachments/4420461603991/launch_acs_srch.gif)

In the search box, type the text you want to search for and Server lists the resources that contain the matched text (for the My Profile page the options whose key values contain the matched text are listed). In the search result list, select an option and Server displays the page where the option is and highlights the matched text. When there are more than 10 results, you can select **More** at the end to show all the other results. To cancel the search operation, clear the text in the search box or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420461456151/btn_dltobj.gif).

## Signing out of Logi Report Server

To sign out from the Start Page, select the ![Logout button](https://devnet.logianalytics.com/hc/article_attachments/4420447195415/btn_logout.gif) icon at the upper right corner.

To sign out from the Server Console, select the User icon ![User icon](https://devnet.logianalytics.com/hc/article_attachments/4420453530903/btn_user.gif) at the upper right corner and then select **Logout** from the drop-down menu.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690637847-Sending-Commands-to-Logi-Report-Server-from-Java)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690639639-Shutting-Down-Logi-Report-Server)
