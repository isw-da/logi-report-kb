---
title: "Web Service Connection Properties"
id: 1500010061642
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061642-Web-Service-Connection-Properties
updated_at: 2021-07-23T19:16:26Z
---

# Web Service Connection Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061602-User-Defined-Function-UDF-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100161-XML-Connection-Properties)

# Web Service Connection Properties

This topic lists the properties of a Web Service Connection object in a catalog.

| Property Name | Description |
| --- | --- |
| General | |
| Date Format | Specifies the default format for data of Date type. Data type: String |
| Default | Specifies whether the connection is the default connection in the current data source. By default, the first added connection in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the WSDL connection. Data type: String |
| Name | Specifies the name of the connection which, by default, is the same as the connection URL, but can also be a user-defined name for the connection. Data type: String |
| Name Pattern | Specifies whether or not catalog or schema is used in data manipulation. Choose an option from the drop-down list.  * **unqualified name** - Neither catalog nor schema is included in data manipulation. Example: SELECT t.c FROM t * **2-part names**  - Uses schema in data manipulation. Example: SELECT schema.t.c FROM schema.t * **3-part names**  - Uses both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t   Data type: Enumeration |
| Password | Specifies the password used for accessing the WSDL file through the WSDL URI. Data type: String |
| Time Format | Specifies the default Time format corresponding to the database. Data type: String |
| Time Out | Specifies how long to wait to get the WSDL file, in seconds. Data type: Integer |
| Timestamp Format | Specifies the default format for data of Timestamp type. Data type: String |
| URI | Displays the URI to get the WSDL file. This property is read only. |
| User | Specifies the user name used for accessing the WSDL file through the WSDL URI. Data type: String |
| Security Configuration | |
| Client Key Alias Name | Displays the alias name which is used as client signature in the key store. This property is read only. |
| Client Key Alias Password | Displays the password for the alias name which is used as client signature in the key store. This property is read only. |
| Key Store File | Displays the URI to get the key store file. This property is read only. |
| Key Store Password | Displays the password to open the key store file. This property is read only. |
| Key Store Type | Displays the type for the key store. This property is read only. |
| Security Password | Displays the password for the user name token to be used. This property is read only. |
| Security User Name | Displays the user name for the user name token to be used. This property is read only. |
| Server Key Alias Name | Displays the alias name which is used to get the server-side certification or public key in the key store. This property is read only. |
| Server Key Alias Password | Displays the password for the alias name which is used to get the server-side certification or public key in the key store. This property is read only. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061602-User-Defined-Function-UDF-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100161-XML-Connection-Properties)
