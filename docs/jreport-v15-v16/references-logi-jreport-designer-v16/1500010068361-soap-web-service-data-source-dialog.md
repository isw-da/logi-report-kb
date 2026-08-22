---
title: "SOAP Web Service Data Source Dialog"
id: 1500010068361
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068361-SOAP-Web-Service-Data-Source-Dialog
updated_at: 2021-07-24T10:38:17Z
---

# SOAP Web Service Data Source Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032462-Size-List-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032682-Sort-Dialog)

# SOAP Web Service Data Source Dialog

The SOAP Web Service Data Source dialog helps you to [create or edit a web service data source](https://devnet.logianalytics.com/hc/en-us/articles/1500010064561-SOAP-Web-Service-Connections#Set) in a Logi JReport catalog. It appears when you select SOAP Web Service and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010031882-New-Data-Source-Dialog) dialog, or in the Catalog Manager right-click a data source and select New SOAP Web Service Connection from the shortcut menu or right-click an existing web service connection and select Edit Connection from the shortcut menu.

![SOAP Web Service Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901168151/wbsvc.gif)

The following are details about the options of the dialog:

**Get WSDL file**

Specifies to get a WSDL file to create the web service data source.

* **Local File**  
   Specifies to get a WSDL file from local files by selecting the Browse button.
* **URI**  
   Specifies the location of the WSDL file by inputting the URI string.
  + **User Name**  
     Specifies the user name used for accessing the WSDL file through the URI.
  + **Password**  
     Specifies the password used for accessing the WSDL file through the URI.

**Time Zone and Locale**

Specifies a default time zone and locale for the web service data source.

* **Default Time Zone**  
   Specifies the default time zone for the web service data source.
* **Locale**  
   Specifies the locale for the web service data source.

**Qualified Name Pattern**

Specifies whether or not catalog or schema is used in data manipulation.

* **Unqualified Name**  
   Neither catalog nor schema will be included in data manipulation. Example: SELECT t.c FROM t
* **2-Part Names**  
   Uses schema in data manipulation. Example: SELECT schema.t.c FROM schema.t
* **3-Part Names**  
   Uses both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t

**Time Out**

Specifies how long to wait to get the WSDL file.

**Security Configuration**

Opens the [Security Configuration Setting](https://devnet.logianalytics.com/hc/en-us/articles/1500010067701-Security-Configuration-Setting-Dialog) dialog to configure security for the web service data source.

**Options**

Shows the additional settings for creating the web service data source.

**OK**

Creates the web service data source and closes the dialog.

**Cancel**

Cancels the creation of the web service data source and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032462-Size-List-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032682-Sort-Dialog)
