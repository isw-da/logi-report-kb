---
title: "SOAP Web Service Data Source Dialog Box"
id: 5735553273623
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735553273623-SOAP-Web-Service-Data-Source-Dialog-Box
updated_at: 2022-11-02T08:23:42Z
---

# SOAP Web Service Data Source Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567246359-Size-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515567127-Sort-Dialog-Box)

# SOAP Web Service Data Source Dialog Box

You can use the SOAP Web Service Data Source dialog box to [create or edit a SOAP Web Service data source](https://devnet.logianalytics.com/hc/en-us/articles/5735528205847-Connecting-via-SOAP-Web-Service-Connections#Set) in a catalog. This topic describes the options in the dialog box.

Designer displays the SOAP Web Service Data Source dialog box when you select SOAP Web Service and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530467735-New-Data-Source-Dialog-Box); or in the Catalog Manager, right-click a data source and select New SOAP Web Service Connection from the shortcut menu, or right-click an existing SOAP Web Service connection and select Edit Connection from the shortcut menu.

![SOAP Web Service Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/7933665579159/wbsvc.gif)

Designer displays these options:

**Get WSDL File**

Specify where to get the WSDL file of the SOAP Web Service data source.

* **Local File**  
  Select to get the WSDL file from your local disk. Select **Browse** to specify the file.
* **URI**  
  Select to get the WSDL file through a URI. Type the URI string in the text box.
  + **User Name**  
    Specify the user name for accessing the WSDL file through the URI.
  + **Password**  
    Specify the password for accessing the WSDL file through the URI.

**Time Zone and Locale**

You can specify the default time zone and locale for the SOAP Web Service data source in this box.

* **Default Time Zone**  
  Specify the default time zone for the data source.
* **Locale**  
  Select the locale for the data source.

**Qualified Name Pattern**

You can specify whether to use catalog or schema in data manipulation in this box.

* **Unqualified Name**  
  Select to include neither catalog nor schema in data manipulation.
* **2-Part Names**  
  Select to use schema in data manipulation.
* **3-Part Names**  
  Select to use both catalog and schema in data manipulation.

**Time Out**

Specify how long to wait to get the WSDL file.

**Security Configuration**

Select to open the [Security Configuration Setting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515319191-Security-Configuration-Setting-Dialog-Box) to configure security for the SOAP Web Service data source.

**Options**

Select to show or hide the additional SOAP Web Service data source settings.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567246359-Size-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515567127-Sort-Dialog-Box)
