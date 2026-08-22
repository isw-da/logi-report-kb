---
title: "New Dynamic Connection"
id: 1500009720622
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009720622-New-Dynamic-Connection
updated_at: 2021-07-25T07:19:40Z
---

# New Dynamic Connection

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747541-New-Dashboard-Listener)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747581-New-Dynamic-Display-Name)

# New Dynamic Connection

The New Dynamic Connection dialog box is used to [create a dynamic connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009718782-Creating-and-Using-Dynamic-Connections). It appears when an admin user selects the New Dynamic Connection link in the Administration > Connection > Dynamic Connections page in the server console.

![New Dynamic Connection dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936885271/nwdyncnct.gif)

**Catalog**

Specifies the catalog in which you would like to create a dynamic connection. Type the catalog with the full resource path in the text box, for example, `/SampleReports/SampleReports.cat`, or select the Browse button to select a catalog in the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009720922-Select-Catalog) dialog box.

**Data Source Name**

Specifies the data source in which you would like to create a dynamic connection in the catalog from the drop-down list.

**Connection Name**

Specifies a connection to connect to the data source from the drop-down list.

**Properties**

Displays the properties of the database connection. You can select it to expand or collapse the [property table](https://devnet.logianalytics.com/hc/en-us/articles/1500009718782-Creating-and-Using-Dynamic-Connections#Properties).

**Add Database User Mapping**

Adds a new database user mapping. Select to create a new line at the end of the table.

**Delete**

Deletes the selected database user mappings.

**Database user mapping table**

**check boxes are used to** specify whether or not to select the database user mapping. Select the check box on the column header to select all database user mappings. After you select the database user mappings, you can then delete them if you do not want them.

* **SID**  
   Specifies the security identifier (SID). A SID can be a group, role or user in the Logi Report Server security system. You can select a value from the drop-down list or type the value in the text box. The **x** in the text box is used to clear the input text. You can define at most one database user mapping for an SID within a dynamic connection.
* **Organization Name**  
   Double-click in the text box and then select an organization from the drop-down list. You can first specify the organization and then the SID. The column is available to system admin when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations) feature is enabled.
* **Database User**  
   Specifies the database user name. Null means using the default database user name.
* **Database Password**  
   Specifies the database password. Passwords are masked.
* **Control**
  + **Test Connection**  
     Tests whether the connection configuration works using the database use rname and password.

**OK**

Creates the dynamic connection and exits the dialog box.

**Cancel**

Cancels the creation of a dynamic connection and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747541-New-Dashboard-Listener)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747581-New-Dynamic-Display-Name)
