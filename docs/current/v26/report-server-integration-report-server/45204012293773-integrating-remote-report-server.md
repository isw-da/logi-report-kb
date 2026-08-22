---
title: "Integrating Remote Report Server"
id: 45204012293773
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204012293773-Integrating-Remote-Report-Server
updated_at: 2026-04-30T14:10:21Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Integrating Remote Report Server 

You can implement Report Remote Server API in your JSPs and integrate the JSPs with the application server to call Report Server that is running on a different machine. This topic describes how you can integrate remote Report Server with IBM WebSphere and WebLogic.

Select the following links to view the topics:

- 
                    Integrating Remote Report Server With IBM WebSphere 9.0.0.7 by a WAR File
                

- 
                    Integrating Remote Report Server With WebLogic 14.1.1 by a WAR File
                

Related topic:

- 
                    Using JSP With a Dedicated Machine
                

- In a remote integration environment, Report Server hides the options for publishing resources since Report JSPs do not support them. If you want to publish reports or catalogs to Report Server, use one of the following ways:
      
- Access the Report Server Console (not the remote server) as an administrator to perform publish work.

- Copy the report or catalog files to the computer where Report Server (not the remote server) is, and then call the RMI API to publish them.

- Publish the report or catalog files from Report Designer to Report Server. 

- In a remote integration environment, Report Server hides the two links Administration > Other > Monitor and Administration > Configuration > Server DB in the Report Server Console since they are not supported.

- You can change the location of the two folders, skin and dhtmljsp, in the \public_html directory in the application server side. What you need to do is create a file jrserver.properties in the \WEB-INF directory and then add the following two properties and provide the correct paths (excluding the context root): 
      web.skin.dir
  web.dhtml_jsp_path
