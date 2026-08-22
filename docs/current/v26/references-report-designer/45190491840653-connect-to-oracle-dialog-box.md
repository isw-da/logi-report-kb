---
title: "Connect to Oracle Dialog Box"
id: 45190491840653
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190491840653-Connect-to-Oracle-Dialog-Box
updated_at: 2026-04-30T15:12:55Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Connect to Oracle Dialog Box

You can use the Connect to Oracle dialog box to specify the information for connecting to an Oracle database via the connection plug-in. This topic describes the options in the dialog box.
    

Designer displays the Connect to Oracle dialog box appears when you do one of the following:

- Select OK in the Create Connection to Oracle dialog box.

- Select Oracle and select OK in the New Data Source dialog box.

- In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu, then select Oracle in the Select Connection Type dialog box and select OK.

Designer displays these options:

Driver

This option shows the Oracle JDBC driver name that this connection uses.

Connection Type

Specify the way using which to connect to the Oracle database: Service Name, SID, or TNS.

Server

Specify the host name or IP address of the database server.

Port

Specify the port of the database server. 

Service Name/SID/TNS

Specify the service name/SID/TNS of the database instance that you want Designer to connect with by default.

User

Specify the user ID used for accessing the database.

Password

Specify the password used for accessing the database.

Show URL

Select to show the URL used for connecting to the database server. 

- 
URL
This option shows the URL which is formulated by the information you provide. You can also type the valid JDBC URL   in the text box to establish the connection to the database server. The URL format is regulated by the driver itself. When Service Name is selected as the connection type, the format is jdbc:oracle:thin:@//<host>:<port>/<service_name>; when SID is selected, the format is jdbc:oracle:thin:@<host>:<port>:<SID>; for TNS, the format is jdbc:oracle:thin:@<TNS>.

Test Connection

Select to test whether the specified connection information can connect to the database successfully.

More Options/Less Options

Select to show or hide the options for experienced users to configure the connection to meet the special requirements of the database.

OK

Select to create the connection to the Oracle database and close the dialog box.

Cancel

Select to quit creating the connection and close the dialog box.

Help

Select to view information about the dialog box.
