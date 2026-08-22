---
title: "Checking Version Properties"
id: 5741482415639
section: "Managing Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741482415639-Checking-Version-Properties
updated_at: 2022-10-31T17:18:11Z
---

# Checking Version Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741462114583-Browsing-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy)

# Checking Version Properties

This topic describes how you can view and edit the properties of a version in the [version table](https://devnet.logianalytics.com/hc/en-us/articles/5741462114583-Browsing-Versions).

The multiple report results that you created by one scheduled task are regarded as one version.

To view the properties of a resource version, take any of the following in the version table of the resource:

* Locate the version and select the **Properties** link on the same row.
* Select the version row and select **Edit** > **Properties** on the task bar.
* Select the version row, right-click in the row, and select **Properties** on the shortcut menu.
* Put the mouse pointer over the version row and select the **Properties** button ![Properties button](https://devnet.logianalytics.com/hc/article_attachments/9905657474071/btn_srv_prpty.gif) on the floating toolbar.

The following lists the properties for versions of different resource types.

**Catalog version properties**

You need to be an administrator to view the properties of catalog versions.

| Option | Description |
| --- | --- |
| General | |
| Version Date | The date and time when Server generated the catalog version. |
| Version Number | The number of the catalog version. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Open the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/5741414587159-Resource-Properties#Permission) tab of the parent catalog for defining permission settings. |
| Connections | |
| JDBC Connection Information | The JDBC Connection Information table contains the following columns:   | Column | Description | | --- | --- | | Resource Name | The name of the JDBC connection. | | Description | The description of the JDBC connection. | | URL | The JDBC URL which establishes the connection to the database. | | JDBC Driver | The class name of the JDBC driver. | | User | The username for connecting to the database, which is determined by the database DBA. | | Password | The password for connecting with the database, which is determined by the database DBA. | | JDBC Plugin | The name of the JDBC connection plugin using which the connection is created. | |
| XML Connection Information | The XML Connection Information table contains the following columns:   | Column | Description | | --- | --- | | Resource Name | The name of the XML Connection. | | URI | The full path of the XML Connection .xml file. | | XSD Name | The name of the XML schema. | | Start Point | The starting node according to the root name in the XML source. | |
| Web Service Connection Information | The Web Service Connection Information table contains the following columns:   | Column | Description | | --- | --- | | WSDL URI | The URI to get the WSDL file. | | User | The username for accessing the WSDL file through the URI. | | Password | The password for accessing the WSDL file through the URI. | | Zone | The default time zone for the web service data source. | | Locale | The locale for the web service data source. | |
| JSON Connection Information | The JSON Connection Information table contains the following columns:  | Column | Description | | --- | --- | | Resource Name | The name of the JSON Connection. | | URI | The full path of the JSON Connection .xml file. | |
| Mongo Connection Information | The Mongo Connection Information table contains the following columns:   | Column | Description | | --- | --- | | Resource Name | The name of the Mongo Connection. | | Description | The description of the Mongo connection. | | URL | The Mongo URL which establishes the connection to the database. | | Mongo Driver | The class name of the Mongo driver. | | User | The username for connecting to the database, which is determined by the database DBA. | | Password | The password for connecting with the database, which is determined by the database DBA. | | Server Address | The IP/host name and port of the Mongo server. | |

**Report version properties**

| Option | Description |
| --- | --- |
| General | |
| Version Date | The date and time when Server generated the report version. |
| Version Number | The number of the report versions. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Open the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/5741414587159-Resource-Properties#Permission) tab of the parent report for defining permission settings. Available only when you have the **Grant** permission on the parent report. |
| Resources | |
| Referred Resource Type | The type of the resources in the report version, including images, fonts, and sub reports. |
| Referred Resource Names | Null. |

**Report result version properties**

| Option | Description |
| --- | --- |
| Version Date | The date and time when Server generated the report result version. |
| Version Number | The number of the report result versions. |
| Report Tab Name | The name of the page report tab for which Server generated the report result version. Available to page report result versions only. |
| Real Path | The full path of the version file on the disk. |

**Result version properties**

| Option | Description |
| --- | --- |
| Version Date | The date and time when Server generated the result version. |
| Version Number | The number of the result versions. |
| Report Tab Name | The name of the page report tab for which Server generated the result version. Available to result versions that you created based on page reports only. |
| Real Path | The full path of the version file on the disk. |
| [Result Auto-delete](https://devnet.logianalytics.com/hc/en-us/articles/5741468720791-Deleting-Versions#Autodelete) | Specify whether to remove the result versions automatically. Select if you want to further specify whether to make the result version expire after a designated number of days or right after a certain date. |
| Set Permissions | Open the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/5741414587159-Resource-Properties#Permission) tab of the parent result for defining permission settings. Available only when you have the **Grant** permission on the parent result. |

**Dashboard version properties**

| Option | Description |
| --- | --- |
| General | |
| Version Date | The date and time when Server generated the dashboard version. |
| Version Number | The number of the dashboard versions. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Open the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/5741414587159-Resource-Properties#Permission) tab of the parent dashboard for defining permission settings. Available only when you have the **Grant** permission on the parent dashboard. |
| Resources | |
| Referred Resource Type | The type of the resources in the dashboard version, such as images and fonts. |
| Referred Resource Names | Null. |

**Library component version properties**

| Option | Description |
| --- | --- |
| Version Date | The date and time when Server generated the library component version. |
| Version Number | The number of the library component versions. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Open the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/5741414587159-Resource-Properties#Permission) tab of the parent library component for defining permission settings. Available only when you have the **Grant** permission on the parent library component. |

**Analysis version properties**

| Option | Description |
| --- | --- |
| General | |
| Version Date | The date and time when Server generated the analysis template version. |
| Version Number | The number of the analysis template version. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Open the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/5741414587159-Resource-Properties#Permission) tab of the parent analysis template for defining permission settings. Available only when you have the **Grant** permission on the parent analysis template. |
| Resources | |
| Referred Resource Type | The type of the resources in the analysis template version, such as images and fonts. |
| Referred Resource Names | Null. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741462114583-Browsing-Versions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy)
