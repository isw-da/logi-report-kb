---
title: "New Dynamic Connection Dialog Box Properties"
id: 1500009746142
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746142-New-Dynamic-Connection-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:46Z
---

# New Dynamic Connection Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774081-New-Dashboard-Listener-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774101-New-Dynamic-Display-Name-Dialog-Box-Properties)

# New Dynamic Connection Dialog Box Properties

This topic describes how you can use the New Dynamic Connection dialog box to [create a dynamic connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009743582-Creating-and-Using-Dynamic-Connections). Server displays the dialog box when an admin user selects the New Dynamic Connection link in the Administration > Connection > Dynamic Connections page in the Server Console.

![New Dynamic Connection dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885511063/nwdyncnct.gif)

**Catalog**

Specifies the catalog in which you would like to create a dynamic connection. Type the catalog with the full resource path in the text box, for example, `/SampleReports/SampleReports.cat`, or select the Browse button to select a catalog in the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009774661-Select-Catalog-Dialog-Box-Properties) dialog box.

**Data Source Name**

Specifies the data source in which you would like to create a dynamic connection in the catalog from the drop-down list.

**Connection Name**

Specifies a connection to connect to the data source from the drop-down list.

**Properties**

Displays the properties of the database connection. You can select it to expand or collapse the [property table](https://devnet.logianalytics.com/hc/en-us/articles/1500009743582-Creating-and-Using-Dynamic-Connections#Properties).

**Add Database User Mapping**

Adds a new database user mapping. Select to create a new line at the end of the table.

**Delete**

Deletes the selected database user mappings.

**Database user mapping table**

**check boxes are used to** specify whether to select the database user mapping. Select the check box on the column header to select all database user mappings. After you select the database user mappings, you can then delete them if you do not want them.

* **SID**  
   Specifies the security identifier (SID). A SID can be a group, role, or user in the Logi Report Server security system. You can select a value from the drop-down list or type the value in the text box. The **x** in the text box is used to clear the input text. You can define at most one database user mapping for an SID within a dynamic connection.
* **Organization Name**  
   Double-click in the text box and then select an organization from the drop-down list. You can first specify the organization and then the SID. The column is available to system admin when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations) feature is enabled.
* **Database User**  
   Specifies the database user name. Null means using the default database user name.
* **Database Password**  
   Specifies the database password. Passwords are masked.
* **Control**
  + **Test Connection**  
     Tests whether the connection configuration works using the database user name and password.

**OK**

Creates the dynamic connection and exits the dialog box.

**Cancel**

Cancels the creation of a dynamic connection and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774081-New-Dashboard-Listener-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774101-New-Dynamic-Display-Name-Dialog-Box-Properties)
