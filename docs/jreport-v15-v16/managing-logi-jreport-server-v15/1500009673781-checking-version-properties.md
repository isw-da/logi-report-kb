---
title: "Checking Version Properties"
id: 1500009673781
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673781-Checking-Version-Properties
updated_at: 2021-07-24T20:53:59Z
---

# Checking Version Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673741-Browsing-Versions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy)

# Checking Version Properties

From the [version table](https://devnet.logianalytics.com/hc/en-us/articles/1500009673741-Browsing-Versions), you can view the detailed properties of each version and edit some properties of the version. The multiple report results created by one scheduled task are regarded as one version.

To view the properties of a resource version, in the version table of the resource:

* For administrators, locate the version and then select the **Properties** link on the same row.
* For end users, locate the version and then:
  + Select the version row and select **Edit** > **Properties** on the task bar.
  + Select the version row, right-click in the row and select **Properties** on the shortcut menu.
  + Put the mouse pointer over the version row and select the **Properties** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926692119/btn_srv_prpty.gif).

The following lists the properties of versions of different resource types.

**Catalog version properties**

| Option | Description |
| --- | --- |
| General | | | |
| Version Date | The date and time of when the catalog version is generated. |
| Version Number | The number of the catalog version. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Opens the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009670961-Catalog-Properties#Permission) tab of the parent catalog for defining permission settings. |
| Connections | | | |
| JDBC Connection Information | The JDBC Connection Information table contains the following columns:  * **Resource Name**  The name of the JDBC connection. * **Description**  The description of the JDBC connection. * **URL**  The JDBC URL which establishes the connection to the database. * **JDBC Driver**  The class name of the JDBC driver. * **User**  The user name for connecting to the database, which is determined by the database DBA. * **Password**  The password for connecting with the database, which is determined by the database DBA. * **JDBC Plugin**  The name of the JDBC connection plugin. For details, see "Connection Plugins" in the *Logi JReport Designer User's Guide*. |
| XML Connection Information | The XML Connection Information table contains the following columns:  * **Resource Name**  The name of the XML Connection. * **URI**  The full path of the XML Connection .xml file. * **XSD Name**  The name of the XML schema. * **Start Point**  The starting node according to the root name in the XML source. |
| Web Service Connection Information | The Web Service Connection Information table contains the following columns:  * **WSDL URI**  The URI to get the WSDL file. * **User**  The user name used for accessing the WSDL file through the URI. * **Password**  The password used for accessing the WSDL file through the URI. * **Zone**  The default time zone for the web service data source. * **Locale**  The locale for the web service data source. |
| JSON Connection Information | The JSON Connection Information table contains the following columns:  * **Resource Name**  The name of the JSON Connection. * **URI**  The full path of the JSON Connection .xml file. |
| Mongo Connection Information | The Mongo Connection Information table contains the following columns:  * **Resource Name**  The name of the Mongo Connection. * **Description**  The description of the Mongo connection. * **URL**  The Mongo URL which establishes the connection to the database. * **Mongo Driver**  The class name of the Mongo driver. * **User**  The user name for connecting to the database, which is determined by the database DBA. * **Password**  The password for connecting with the database, which is determined by the database DBA. * **Server Address**  The IP/host name and port of the Mongo server. |

**Report version properties**

| Option | Description |
| --- | --- |
| General | | | |
| Version Date | The date and time of when the report version is generated. |
| Version Number | The number of the report version. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Opens the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009671061-Report-Properties#Permission) tab of the parent report for defining permission settings. |
| Resources | | | |
| Referred Resource Type | Lists the type of the resources used in the report version, including images, fonts, and sub reports. |
| Referred Resource Names | Null. |

**Report result version properties**

| Option | Description |
| --- | --- |
| Version Date | The date and time of when the report result versions are generated. |
| Version Number | The number of the report result versions. |
| Report Tab Name | The name of the page report tab in the report result versions. Available to page report results. |
| Real Path | The full path of the version files on the disk. |

**Result version properties**

| Option | Description |
| --- | --- |
| Version Date | The date and time of when the result version is generated. |
| Version Number | The number of the result version. |
| Report Tab Name | The name of the page report tab in the result versions. Available to result versions created based on page reports. |
| Real Path | The full path of the version files on the disk. |
| [Result Auto-delete](https://devnet.logianalytics.com/hc/en-us/articles/1500009673761-Deleting-Versions#Autodelete) | Specifies whether to make the result versions be removed automatically. If it is checked, you can continue to specify whether to make the results expire after a specified number of days or right after a certain date. |
| Set Permissions | Opens the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009671081-Result-Properties#Permission) tab of the parent result for defining permission settings. |

**Dashboard version properties**

| Option | Description |
| --- | --- |
| General | | | |
| Version Date | The date and time of when the dashboard version is generated. |
| Version Number | The number of the dashboard version. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Opens the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009670981-Dashboard-Properties#Permission) tab of the parent dashboard for defining permission settings. |
| Resources | | | |
| Referred Resource Type | Lists the type of the resources used in the dashboard version, such as images and fonts. |
| Referred Resource Names | Null. |

**Library component version properties**

| Option | Description |
| --- | --- |
| Version Date | The date and time of when the library component version is generated. |
| Version Number | The number of the library component version. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Opens the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009671021-Library-Component-Properties#Permission) tab of the parent library component for defining permission settings. |

**Analysis version properties**

| Option | Description |
| --- | --- |
| General | | | |
| Version Date | The date and time of when the analysis template version is generated. |
| Version Number | The number of the analysis template version. |
| Real Path | The full path of the version file on the disk. |
| Set Permissions | Opens the [Permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009646722-Analysis-Template-Properties#Permission) tab of the parent analysis template for defining permission settings. |
| Resources | | | |
| Referred Resource Type | Lists the type of the resources used in the analysis template version, such as images and fonts. |
| Referred Resource Names | Null. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673741-Browsing-Versions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy)
