---
title: "Maintaining Server"
id: 28891516056589
section: "Report Server Monitor Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891516056589-Maintaining-Server
updated_at: 2026-02-26T02:10:56Z
source_host: docs-report.zendesk.com
---
# 
Maintaining Server

You can perform maintenance tasks on  Server Monitor, such as stopping problematic reports and connections, and shutting down Servers in a cluster. This topic introduces how you can maintain Server from Server Monitor.

## Stopping Problematic Reports and Connections

To stop a problematic report from running:

- Expand a Server node in the left panel of the Server Monitor home page, and then select Reports. You can then see the status of the reports on the Server.

- Select to select different reports from the drop-down list. There are five types of reports - all reports, running reports, waiting reports, finished reports, and failed reports.

- Choose to view running reports or waiting reports. Select on the Action column, you will find a command link Kill in front of each report status row. Select Kill to terminate the report running process.

To disconnect a connection:

- Expand a Server node in the left panel of the Server Monitor home page, and select Databases. You can see the status of the database connections on the Server.

- Select the connection that you want to disconnect, and then select the Disconnect link on the top.

## Shutting Down Servers in a Cluster

To shut down one or more Servers in a cluster, in the left panel of the Server Monitor home page, select the root node, then in the Status tab, select the Servers you want to shut down and select the Shut Down link.
