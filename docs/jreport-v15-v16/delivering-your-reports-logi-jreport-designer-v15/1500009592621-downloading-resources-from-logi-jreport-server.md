---
title: "Downloading Resources from Logi JReport Server"
id: 1500009592621
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592621-Downloading-Resources-from-Logi-JReport-Server
updated_at: 2021-07-24T05:53:51Z
---

# Downloading Resources from Logi JReport Server

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582541-Working-with-APIs)

# Downloading Resources from Logi JReport Server

This topic introduces how to download resources from Logi JReport Server.

Below is a list of the sections covered in this topic:

> * [Downloading Reports and Library Components](#Report)
> * [Downloading Customized Controls](#CC)

## Downloading Reports and Library Components

Reports created on Logi JReport Server can be downloaded to your local computer and further modified using Logi JReport Designer. The same as with publishing, all resources used by the reports will also be downloaded such as other linked reports and images.

1. In Logi JReport Designer:
   * Select **File** >  **Download** > **Download Report from Server** if you want to download reports.
   * Select **File** > **Download** > **Download Component from Server** if you want to download library components.

   The [Connect to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009585921-Connect-to-JReport-Server-Dialog) dialog appears.

   ![Connect to Logi JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893818519/connect.gif)
2. Type in the host and port of the remote Logi JReport Server in the Host and Port text fields.
3. When using a standalone server, enter **/jrserver** in the Servlet Path text field or the context root of your web application if deployed as a war or ear fie such as /Logi JReport/jrserver.
4. If the server has been integrated with another web server that supports SSL, select the **SSL** (Security Socket Layer) checkbox to create an SSL connection.
5. Check **Remember connection information**  to enable Logi JReport Designer to remember the connection information.
6. Provide the user name and password of the server. When the Organization feature is enabled and when the user is an organization user, User Name should include the organization name. Use \ to separate the organization name and the user name, for example, org1\user1.
7. Select **Connect**. The [Download from Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009586321-Download-from-JReport-Server-Dialog) dialog appears.

   ![Download from Logi JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893819927/dwldjrsrv.gif)
8. In the Download Resource From text field, select the **Browse** button to specify the folder on the server where to download resources. The resources in the specified folder will then be loaded automatically in the resource tree box.
9. In the resource tree box, check the checkboxes in front of the resources that you want to download.
10. Select the **Browse** button next to the Download Resource To text field to specify the path to which resources will be downloaded, or type in the directory in the text field directly.
11. Select **OK**. The selected resources and all additional resources referenced by them such as linked reports and images will then be downloaded from Logi JReport Server.

When the resources are successfully downloaded from Logi JReport Server, you can open them in Logi JReport Designer, and further edit them if required.

**Notes:**

* Resources in the Public Reports folder of Logi JReport Server are protected by permissions. If you specify to download resources from that folder, which resources you can see in the resource tree box and which resources you can download are determined by the user name with which you use to connect to the server. You can only view the resources on which you have the Visible permission in this box and download resources on which you are assigned the Read permission. For more information, refer to Managing Permissions in the *Logi JReport Server User's Guide*.
* Downloading reports which use business views as data source from Logi JReport Server requires that Logi JReport Designer and Logi JReport Server each has its own [Live license](https://devnet.logianalytics.com/hc/en-us/articles/1500009568442-Logi-JReport-Licenses#Live).

## Downloading Customized Controls

[Customized controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009584281-Using-Customized-Controls-in-a-Table) on Logi JReport Server can be downloaded to your local computer and further modified using Logi JReport Designer.

1. Select **File** > **Download** > **Download Customized Control from Server**.
2. In the Connect to Logi JReport Server dialog, specify the information to [connect to a started Logi JReport Server](#Connect). The [Download Customized Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009565162-Download-Customized-Control-Dialog) dialog is displayed.

   ![Download Customized Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893820183/dwldcstmzdctrl.gif)
3. Select the customized control files you need, select the right-headed single arrow button to add them to the right box, and then select **OK**.

Note that the downloaded files will overwrite the local ones with the same name directly without warning.

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582541-Working-with-APIs)
