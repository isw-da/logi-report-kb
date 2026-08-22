---
title: "Login Server Dialog Box Properties"
id: 5741420798871
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741420798871-Login-Server-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:56Z
---

# Login Server Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741405863703-JDashboard-Profile-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741427584151-Multiple-Type-Properties)

# Login Server Dialog Box Properties

This topic describes how you can use the Login Server dialog box to specify the information required for signing into a Logi Report Server in order to [publish resources to the server](https://devnet.logianalytics.com/hc/en-us/articles/5741453495191-Publishing-Resources#ToServer).

Server displays the dialog box when you select **Publish** > **To Server** on the task bar of the Resources page on the Server Console but you have not signed into the target server, or select **Change Login Settings** in the [Publish to Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741421317271-Publish-to-Server-Dialog-Box-Properties).

![Login Server dialog](https://devnet.logianalytics.com/hc/article_attachments/9905714478743/loginsrv.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741405863703-JDashboard-Profile-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741427584151-Multiple-Type-Properties)
