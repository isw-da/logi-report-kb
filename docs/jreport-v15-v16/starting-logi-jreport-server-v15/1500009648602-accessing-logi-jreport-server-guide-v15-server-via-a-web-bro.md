---
title: "Accessing Logi JReport Server Guide v15 Server via a Web Browser"
id: 1500009648602
section: "Starting Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648602-Accessing-Logi-JReport-Server-Guide-v15-Server-via-a-Web-Browser
updated_at: 2021-07-24T20:54:08Z
---

# Accessing Logi JReport Server Guide v15 Server via a Web Browser

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673301-Sending-Commands-to-Logi-JReport-Server-Guide-v15-Server-from-Java)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673321-Shutting-Down-Logi-JReport-Server-Guide-v15-Server)

# Accessing Logi JReport Server via a Web Browser

You can access Logi JReport Server through a web browser such as Internet Explorer, Firefox, or Google Chrome. Logi JReport Server provides two consoles: user console and administration console. The user console allows server end users to perform report related tasks such as running and creating reports and dashboards, starting visual analysis, customizing their own server preferences and so on; the administration console is for administrators to perform administrative tasks such as managing security and databases, configuring the server, setting up cluster and so on.

Below is a list of the sections covered in this topic:

* [Logging Onto the User Console Locally](#Local)
* [Logging Onto the User Console by URL](#URL)
* [Logging Onto the Administration Console](#Admin)
* [Logging Off Logi JReport Server](#Shut)

## Logging Onto the User Console Locally

To access the Logi JReport Server user console from the same machine on which Logi JReport Server is installed, take the following steps:

1. After Logi JReport Server is started, a welcome page is automatically displayed in your default web browser, prompting you to provide your user name and password as assigned by your administrator. For first time users, the default user name and password are admin.

   When the server is [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations) enabled, you need to also specify the organization name. The organization name *System* means that the login user is a non-organization user. For organization users, the correct organization name must be provided, otherwise they cannot log in.
2. After login, the Logi JReport Server user console home page is displayed which can be the Start Page, the Console page or a dashboard depending on the Home Page setting in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile).

   The Start Page is the default home page of Logi JReport Server user console. It provides quick entries to some key functions. Choose a topic to start your work on the server.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920497175/launch_acs_strtpg.gif)

   | Option | Description |
   | --- | --- |
   | Create | |
   | Web Reports | [Creates a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009675381-Quick-Start-with-a-Table-Report). |
   | Dashboards | [Creates a dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009644642-Creating-Dashboards). |
   | Page Reports | [Creates a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009673901-Creating-Page-Reports). |
   | Analysis | [Starts visual analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009643282-Performing-Visual-Analysis). |
   | Open | |
   | My Reports | Opens the My Reports folder on the Logi JReport Console page. |
   | Public Reports | Opens the Public Reports folder on the Logi JReport Console page. |
   | Product Demo | Access dashboards and reports demos. |
   | Online Demo | Goes to the Logi JReport Demo Site. |
   | Manage | |
   | Schedule | [Schedules a task to run a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports). |
   | Security | Requires to log into the administration console first as an administrator and then redirects to the Security page for [managing the server security](https://devnet.logianalytics.com/hc/en-us/articles/1500009650062-Security-System-Data-Model). |
   | Profile | Opens the Profile page for [configuring the server profile settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile). |
   | Others | |
   | User name | Shows the user name. |
   | Logout | Logs out the server. |
   | User's Guide | Displays the Logi JReport Server User's Guide. |
   | What's New | Shows the new features of the current server version. |
   | Check for Updates | Goes to the Logi JReport product download center. |
   | Online Support | Goes to the Logi JReport Knowledge Base to seek help. |
   | Jinfonet Software Home Page | Goes to the Jinfonet Software Home Page. |
   | Tutorial | Displays the Logi JReport Tutorial guide. |
   | Do not show this page at start up | If checked, the Logi JReport Server user console home page will be changed from the Start Page to the Logi JReport Console page when the server starts. You can display the Start Page by selecting the Start Page button  on the system toolbar of the Logi JReport Console page. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logging Onto the User Console by URL

Sometimes you may have closed the Start Page or Logi JReport Console page while the local server remains started, or you are accessing the user console from a remote computer, you can access it by URL as follows:

1. Open a web browser and set the URL to `http://IP_or_HostName_or_DomainName:port` (by default the port for accessing the user console is 8888).

   If you don't know the IP address of the machine on which the server runs, and it is the same machine where you are going to log in, you can use *localhost* instead of the IP address. You can also open a console window such as telnet on the server machine and type **hostname** to get the name of the host.
2. On the welcome page, type your user name and password, and the organization name if required.
3. Select **Login** and Logi JReport Server user console home page is then displayed.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logging Onto the Administration Console

1. Select **Start** > **Logi JReport 15** > **System Admin**, or open a web browser and set the URL to `http://IP_or_HostName_or_DomainName:port` (by default the port for accessing the administration console is 8889).
2. In the Sign in dialog, type your user name and password, and the organization name if required.
3. Select **Login** and the Logi JReport Administration page is displayed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920497815/launch_acs_admin.gif)

**Additional login channel for admin users**

Logi JReport Server provides a special channel that automatically creates an extra user session for management purposes if the license limit of the maximum number of concurrent users has been reached. The extra user session cannot be used to run reports or submit schedules. It can only be used by admin users for performing management operations. If your Logi JReport Server license has a bounded limit to the maximum number of concurrent users, this feature will take effect.

Only one extra valid user session can be created and used within this special channel at any time. If an extra user session has already been created and is still valid, your request for login will be prompted with a confirmation page asking you whether or not to close the existing extra user session. Only when the existing user session is closed can Logi JReport Server start a new user session for you to perform management operations. Otherwise, you will not be allowed to log onto Logi JReport Server.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logging Off Logi JReport Server

To log out from Logi JReport Server, select the **Logout** link on the upper right corner of the Logi JReport Server Start/Console/Administration page.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673301-Sending-Commands-to-Logi-JReport-Server-Guide-v15-Server-from-Java)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673321-Shutting-Down-Logi-JReport-Server-Guide-v15-Server)
