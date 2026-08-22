---
title: "Web Service Connection Properties"
id: 5735532819095
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735532819095-Web-Service-Connection-Properties
updated_at: 2022-11-02T08:09:56Z
---

# Web Service Connection Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532797207-User-Defined-Function-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735532825111-XML-Connection-Properties)

# Web Service Connection Properties

This topic describes the properties of a [Web Service Connection object](https://devnet.logianalytics.com/hc/en-us/articles/5735528205847-Accessing-Data-via-SOAP-Web-Service-Connections) in a catalog.

| Property Name | Description |
| --- | --- |
| General | |
| Date Format | Specifies the default format for Date type data. Data type: String |
| Default | Specifies whether the connection is the default connection in the current catalog data source. By default, the first connection you create in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the connection. Data type: String |
| Name | Specifies the mapped name of the connection in the catalog. By default, the name is the same as the connection URL. Data type: String |
| Name Pattern | Specifies whether to use catalog or schema in data manipulation. Choose an option from the drop-down list.  * **unqualified name** Select to include neither catalog nor schema in data manipulation. Example: SELECT t.c FROM t * **2-part names** Select to use schema in data manipulation. Example: SELECT schema.t.c FROM schema.t * **3-part names** Select to use both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t   Data type: Enumeration |
| Password | Specifies the password for accessing the WSDL file through the WSDL URI. Data type: String |
| Time Format | Specifies the default format for Time type data. Data type: String |
| Time Out | Specifies how long to wait to get the WSDL file, in seconds. Data type: Integer |
| Timestamp Format | Specifies the default format for Timestamp type data. Data type: String |
| URI | Shows the URI to get the WSDL file. Read only. |
| User | Specifies the user name for accessing the WSDL file through the WSDL URI. Data type: String |
| Security Configuration | |
| Client Key Alias Name | Shows the alias name which is used as client signature in the key store. Read only. |
| Client Key Alias Password | Shows the password for the alias name which is used as client signature in the key store. Read only. |
| Key Store File | Shows the URI to get the key store file. Read only. |
| Key Store Password | Shows the password to open the key store file. Read only. |
| Key Store Type | Shows the type for the key store. Read only. |
| Security Password | Shows the password for the user name token to be used. Read only. |
| Security User Name | Shows the user name for the user name token to be used. Read only. |
| Server Key Alias Name | Shows the alias name used to get the server-side certification or public key in the key store. Read only. |
| Server Key Alias Password | Shows the password for the alias name used to get the server-side certification or public key in the key store. Read only. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532797207-User-Defined-Function-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735532825111-XML-Connection-Properties)
