---
title: "Connect to MySQL Dialog Box"
id: 12480048933005
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480048933005-Connect-to-MySQL-Dialog-Box
updated_at: 2026-02-25T23:49:59Z
source_host: docs-report.zendesk.com
---
# 
Connect to MySQL Dialog Box

You can use the Connect to MySQL dialog box to specify the information for connecting to a MySQL database via the connection plug-in. This topic describes the options in the dialog box.
    

Designer displays the Connect to MySQL dialog box when you select the OK button in the Add Driver dialog box, or when you do one of the following in the case that you have already added the MySQL driver in Designer using the Add Driver dialog box:

- Select OK in the Create Connection to MySQL dialog box.

- Select MySQL and select OK in the New Data Source dialog box.

- In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu, then select MySQL in the Select Connection Type dialog box and select OK.

Designer displays these options:

Driver

This option shows the MySQL JDBC driver name that this connection uses.

Server

Specify the host name or IP address of the database server.

Port

Specify the port of the database server. 

Database

Specify the name of the database or schema that you want Designer to connect with by default.

User

Specify the user ID used for accessing the database.

Password

Specify the password used for accessing the database.

Show URL

Select to show the URL used for connecting to the database server. 

- 
URL
This option shows the URL which is formulated by the information you provide. You can also type the valid JDBC URL   in the text box to establish the connection to the database server. The URL format is regulated by the driver itself.

Test Connection

Select to test whether the specified connection information can connect to the database successfully.

More Options/Less Options

Select to show or hide the options for experienced users to configure the connection to meet the special requirements of the database.

OK

Select to create the connection to the MySQL database and close the dialog box.

Cancel

Select to quit creating the connection and close the dialog box.

Help

Select to view information about the dialog box.
