---
title: "Accessing Logi JReport Server via a Web Browser"
id: 1500009717601
section: "Introduction to Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717601-Accessing-Logi-JReport-Server-via-a-Web-Browser
updated_at: 2021-11-03T06:56:57Z
---

# Accessing Logi JReport Server via a Web Browser

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717621-Sending-Commands-to-Logi-Report-Server-from-Java)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717661-Shutting-Down-Logi-Report-Server)

# Accessing Logi JReport Server via a Web Browser

Logi JReport Server is accessible through a web browser such as Internet Explorer, Firefox or Google Chrome. The Logi JReport Server console provides a unified UI for end users and administrators to access and manage server resources depending on authorization. End users can perform report related tasks such as running and creating reports and dashboards, starting visual analysis, customizing their own server preferences and so on. Administrators can perform administrative tasks such as managing security and databases, configuring the server, setting up cluster and so on.

Below is a list of the sections covered in this topic:

* [Logging onto the Server Console Locally](#Local)
* [Logging onto the Server Console by URL](#URL)
* [Additional Login Channel for Admin Users](#Admin)
* [Searching for Resources in the Server Console](#Search)
* [Logging off Logi JReport Server](#Shut)

## Logging onto the Server Console Locally

To access the Logi JReport Server console from the same machine on which Logi JReport Server is installed, take the following steps:

1. After Logi JReport Server is started, a welcome page is automatically displayed in your default web browser, prompting you to provide your user name and password as assigned by your administrator. When the server is [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations) enabled and your user account belongs to an organization, you need to also specify the correct organization name. The default organization name *System* means that the login user does not belong to any organizations. To have your login information remembered, check **Remember Me**.

   ![Login dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112565655/launch_acs_login.gif)
2. Select **LOGIN**, the Logi JReport Server console home page is displayed which can be the Start Page, the Console page, or a dashboard depending on the Home Page setting in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile).

   The Start Page is the default home page of the Logi JReport Server console. It provides quick entries to some key functions. Choose a topic to start your work on the server.

   ![Start Page](https://devnet.logianalytics.com/hc/article_attachments/4412139534999/launch_acs_strtpg.gif)

   | Option | Description |
   | --- | --- |
   | How To | |
   | Feature Guide | Displays the guide about Logi JReport's main features. |
   | Demo | Displays dashboards and reports demos. |
   | Webinar | Goes to Logi JReport webinar web page. |
   | Tutorial | Displays the Logi JReport Tutorial guide. |
   | Create | |
   | Dashboard | [Creates a dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009712541-Creating-and-Saving-Dashboards). |
   | Web Report | [Creates a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009692882-Quick-Start-with-a-Table-Report). |
   | Page Report | [Creates a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009718121-Creating-Page-Reports). |
   | Open | |
   | My Folder | Opens the My Reports folder in the Logi JReport Server console. |
   | Public Folder | Opens the Public Reports folder in the Logi JReport Server console. |
   | Manage | |
   | My Profile | Opens the server console > My Profile > Customize Server Preferences page for [configuring the server profile settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile) of your own. |
   | Schedule | [Schedules a task to run a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009692502-Scheduling-Tasks-to-Publish-Reports). |
   | Administration | Opens the server console > Administration > Configuration > Advanced page for managing the server advanced resources. Available to administrators only. |
   | Others | |
   | User name | Shows the name of the current login user. |
   | Logout button | Logs out the server. |
   | User's Guide | Displays the Logi JReport Server User's Guide. |
   | Knowledge Base | Goes to the Logi JReport Knowledge Base to seek help. |
   | Jinfonet Home Page | Goes to the Logi JReport Home Page. |
   | Contact Support | Goes to Logi JReport support center. |
   | Do not show this page at start up | If checked, the Logi JReport Server console home page will be changed from the Start Page to the server console when the server starts next time. You can display the Start Page by selecting the Start Page button Start Page button on the system toolbar of the server console. |

## Logging onto the Server Console by URL

Sometimes you may have closed the Start Page or server console while the local server remains started, or you are accessing the server console from a remote computer, you can access it by URL as follows:

1. Open a web browser and set the URL to `http://IP_or_HostName_or_DomainName:port` (by default the port for accessing the server console is 8888).

   If you don't know the IP address of the machine on which the server runs, and it is the same machine where you are going to log in, you can use localhost instead of the IP address. You can also open a console window such as telnet on the server machine and type **hostname** to get the name of the host.
2. In the welcome page, type your user name and password as assigned by your administrator.
3. Select **LOGIN** and the Logi JReport Server console home page is displayed.

## Additional Login Channel for Admin Users

Logi JReport Server provides a special channel that automatically creates an extra user session for management purposes if the license limit of the maximum number of concurrent users has been reached. The extra user session cannot be used to run reports or submit schedules. It can only be used by admin users for performing management operations. If your Logi JReport Server license has a bounded limit to the maximum number of concurrent users, this feature will take effect.

Only one extra valid user session can be created and used within this special channel at any time. If an extra user session has already been created and is still valid, your request for login will be prompted with a confirmation page asking you whether or not to close the existing extra user session. Only when the existing user session is closed can Logi JReport Server start a new user session for you to perform management operations. Otherwise, you will not be allowed to log onto Logi JReport Server.

## Searching for Resources in the Server Console

In the Logi JReport Server user console, you can make use of the Global Search feature to search for the resources and options you need. Global search can be performed anywhere in the server console to search among all of the following:

* [Report resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009717721-Managing-Resources) such as reports, catalogs, dashboards, library components and folders in the server resource tree
* [Scheduled and background tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009691382-Managing-Tasks)
* Options in the [My Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile) > Customize Server Preferences and Customize Profile pages (excluding the Features sub tab in the Page Report Studio/Web Report Studio/JDashboard tab)
* [Users](https://devnet.logianalytics.com/hc/en-us/articles/1500009718921-Managing-User-Accounts), [groups](https://devnet.logianalytics.com/hc/en-us/articles/1500009718841-Managing-Groups), [roles](https://devnet.logianalytics.com/hc/en-us/articles/1500009692682-Managing-Roles) and [organizations](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations) in the Administration > Security page that is available to administrators only

To use global search, select the **Global Search** button ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4412139535639/btn_srchglbl.gif) on the system toolbar and the following search page is displayed.

![Global Search](https://devnet.logianalytics.com/hc/article_attachments/4412131440663/launch_acs_srch.gif)

In the search box, type in the text you want to search for and the resources containing the matched text will be listed (for the My Profile page the options whose key values contain the matched text are listed). In the search result list, select an option and the page where the option is will be displayed with the matched text highlighted. When there are more than 10 results, you can select the **More** link at the end to show all the other results. To cancel the search operation, clear the text in the search box or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112483991/btn_dltobj.gif).

## Logging off Logi JReport Server

To log out from the Logi JReport Server Start Page, select the ![Logout button](https://devnet.logianalytics.com/hc/article_attachments/4412131440407/btn_logout.gif) button at the upper right corner.

To log out from the Logi JReport Server console, point at the user name at the upper right corner and select **Logout** from the drop-down menu.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717621-Sending-Commands-to-Logi-Report-Server-from-Java)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717661-Shutting-Down-Logi-Report-Server)
