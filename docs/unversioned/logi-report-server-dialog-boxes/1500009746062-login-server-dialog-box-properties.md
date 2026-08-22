---
title: "Login Server Dialog Box Properties"
id: 1500009746062
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746062-Login-Server-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:46Z
---

# Login Server Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746282-Library-Component-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774441-Multiple-Type-Properties)

# Login Server Dialog Box Properties

This topic describes how you can use the Login Server dialog box to specify the information required for logging onto a Logi Report Server in order to [publish resources to the server](https://devnet.logianalytics.com/hc/en-us/articles/1500009777241-Publishing-Resources#ToServer).

Server displays the dialog box when you select Publish > To Server on the task bar of the Resources page in the Server Console but you have not logged onto the target server, or select Change Login Settings in the [Publish to Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009774501-Publish-to-Server-Dialog-Box-Properties) dialog box.

![Login Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880291095/loginsrv.gif)

**Host**

Specifies the host of the target Logi Report Server to which you want to publish resources.

**Port**

Specifies the port that the target server listens to.

**Servlet Path**

It is /jrserver when the target server is a standalone server, and is used in the URL to access the servlet. If the target Logi Report Server is an embedded server, for example jreport.jar the servlet path would be /jreport/jrserver.

**SSL**

Abbreviation of Security Socket Layer. Select this option to specify whether to create an SSL connection when the target server is integrated with another web server which supports SSL.

**User Name**

Specifies the user name used to access the target server.

**Password**

Specifies the password of the user name.

**Remember Me**

Specifies whether to remember the login information.

**Connect**

Connects to the target server and logs you in.

**Cancel**

Cancels operations and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746282-Library-Component-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774441-Multiple-Type-Properties)
