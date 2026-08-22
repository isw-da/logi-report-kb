---
title: "SOAP Web Service Data Source Dialog Box"
id: 4405661748759
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661748759-SOAP-Web-Service-Data-Source-Dialog-Box
updated_at: 2022-01-27T20:36:01Z
---

# SOAP Web Service Data Source Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664568343-Size-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661719191-Sort-Dialog-Box)

# SOAP Web Service Data Source Dialog Box

You can use the SOAP Web Service Data Source dialog box to [create or edit a web service data source](https://devnet.logianalytics.com/hc/en-us/articles/4405661439639-Connecting-via-SOAP-Web-Service-Connections#Set) in a catalog. This topic describes the options in the dialog box.

Designer displays the SOAP Web Service Data Source dialog box when you select SOAP Web Service and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661654807-New-Data-Source-Dialog-Box); or in the Catalog Manager, right-click a data source and select New SOAP Web Service Connection from the shortcut menu, or right-click an existing web service connection and select Edit Connection from the shortcut menu.

![SOAP Web Service Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402388503/wbsvc.gif)

You see the following options in the dialog box:

**Get WSDL file**

Specify where to get the WSDL file to create the web service data source.

* **Local File**  
  Select to get the WSDL file from your local disk. Select **Browse** to specify the file.
* **URI**  
  Select to get the WSDL file through a URI. Type the URI string in the text box.
  + **User Name**  
    Specify the user name for accessing the WSDL file through the URI.
  + **Password**  
    Specify the password for accessing the WSDL file through the URI.

**Time Zone and Locale**

You can specify the default time zone and locale for the web service data source in this box.

* **Default Time Zone**  
  Specify the default time zone for the web service data source.
* **Locale**  
  Select the locale for the web service data source.

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

Select to open the [Security Configuration Setting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661698071-Security-Configuration-Setting-Dialog-Box) to configure security for the web service data source.

**Options**

Select to show or hide the additional settings for creating the web service data source.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664568343-Size-List-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661719191-Sort-Dialog-Box)
