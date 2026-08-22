---
title: "Login Server Dialog Box Properties"
id: 28891603763597
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891603763597-Login-Server-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:19Z
source_host: docs-report.zendesk.com
---
# 
Login Server Dialog Box Properties

This topic describes how you can use the Login Server dialog box to specify the information required for signing into a Report Server in order to publish resources to the server. 

Server displays the dialog box when you select Publish > To Server on the task bar of the Resources page on the Server Console but you have not signed into the target server, or select Change Login Settings in the Publish to Server dialog box.

Host

Type the host of the target Report Server to which you want to publish resources.

Port

Type the port that the target server listens to.

Servlet Path

It is /jrserver when the target server is a standalone server, which you can use in the URL to access the servlet. If the target Server is an embedded server, for example jreport.jar, the servlet path would be /jreport/jrserver.

SSL

Abbreviation of Security Socket Layer. Select SSL you want to create an SSL connection when the target server is integrated with another web server that supports SSL.

User Name

Specify the username to access the target server.

Password

Specify the password of the username.

Remember Me

Select if you want Server to remember your information.

Connect

Select to connect to the target server and sign in. 

Cancel

Select to close the dialog box without connecting to a server.

Help

Select to view information about the dialog box.
