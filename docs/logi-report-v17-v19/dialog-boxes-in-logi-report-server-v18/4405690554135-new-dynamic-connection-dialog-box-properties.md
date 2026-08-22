---
title: "New Dynamic Connection Dialog Box Properties"
id: 4405690554135
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690554135-New-Dynamic-Connection-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:03Z
---

# New Dynamic Connection Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690553239-New-Dashboard-Listener-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690555031-New-Dynamic-Display-Name-Dialog-Box-Properties)

# New Dynamic Connection Dialog Box Properties

This topic describes how you can use the New Dynamic Connection dialog box to [create a dynamic connection](https://devnet.logianalytics.com/hc/en-us/articles/4405690485527-Creating-and-Using-Dynamic-Connections).

Server displays the dialog box when an administrator selects **New Dynamic Connection** in the Administration > Connection > Dynamic Connections page on the Server Console.

![New Dynamic Connection dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420453597079/nwdyncnct.gif)

**Catalog**

Specify the catalog in which you would like to create a dynamic connection. Select **Browse** to select a catalog in the [Select Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683769367-Select-Catalog-Dialog-Box-Properties), or type the catalog path in the text box, for example, `/SampleReports/SampleReports.cat`.

**Data Source Name**

Select the data source in which you would like to create a dynamic connection in the catalog.

**Connection Name**

Select a connection to connect to the data source.

**Properties**

Properties of the database connection. You can select it to expand or collapse the [property table](https://devnet.logianalytics.com/hc/en-us/articles/4405690485527-Creating-and-Using-Dynamic-Connections#Properties).

**Add Database User Mapping**

Select to add a new database user mapping.

**Delete**

Select to delete the selected database user mappings.

**Database user mapping table**

After you select the database user mappings, you can then delete them if you do not want them. You can select the checkbox on the column header to select all database user mappings.

* **SID**  
   Select the security identifier (SID). A SID can be a group, role, or user in the Logi Report Server security system. You can define at most one database user mapping for an SID within a dynamic connection.
* **Organization Name**  
   Double-click the text box, and then select an organization. You can first specify the organization and then the SID. The column is available to system admin when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations) feature is enabled.
* **Database User**  
   Double-click the text box, and then type the database username. Null means using the default database username.
* **Database Password**  
   Double-click the text box, and then type the database password. Server masks the password.
* **Control**  
  Select **Test Connection** to test whether the connection configuration works using the database username and password.

**OK**

Select to create the dynamic connection and exit the dialog box.

**Cancel**

Select to close the dialog box without creating a dynamic connection.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690553239-New-Dashboard-Listener-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690555031-New-Dynamic-Display-Name-Dialog-Box-Properties)
