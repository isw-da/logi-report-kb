---
title: "Login Server Dialog Box Properties"
id: 4405690549655
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690549655-Login-Server-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:02Z
---

# Login Server Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683748759-JDashboard-Profile-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683758103-Multiple-Type-Properties)

# Login Server Dialog Box Properties

This topic describes how you can use the Login Server dialog box to specify the information required for signing into a Logi Report Server in order to [publish resources to the server](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources#ToServer).

Server displays the dialog box when you select **Publish** > **To Server** on the task bar of the Resources page on the Server Console but you have not signed into the target server, or select **Change Login Settings** in the [Publish to Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690562327-Publish-to-Server-Dialog-Box-Properties).

![Login Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461591447/loginsrv.gif)

**Host**

Type the host of the target Logi Report Server to which you want to publish resources.

**Port**

Type the port that the target server listens to.

**Servlet Path**

It is **/jrserver** when the target server is a standalone server, which you can use in the URL to access the servlet. If the target Server is an embedded server, for example jreport.jar, the servlet path would be **/jreport/jrserver**.

**SSL**

Abbreviation of Security Socket Layer. Select **SSL** you want to create an SSL connection when the target server is integrated with another web server that supports SSL.

**User Name**

Specify the username to access the target server.

**Password**

Specify the password of the username.

**Remember Me**

Select if you want Server to remember your information.

**Connect**

Select to connect to the target server and sign in.

**Cancel**

Select to close the dialog box without connecting to a server.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683748759-JDashboard-Profile-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683758103-Multiple-Type-Properties)
