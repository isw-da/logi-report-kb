---
title: "Add Tables Dialog Box"
id: 4405664425495
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664425495-Add-Tables-Dialog-Box
updated_at: 2022-01-27T20:36:03Z
---

# Add Tables Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661451543-Add-Stored-Procedures-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661454359-Add-Tables-Views-Queries-Dialog-Box)

# Add Tables Dialog Box

You can use the Add Tables dialog box to add tables into a catalog via the connection you set up. This topic describes the options in the dialog box.

Designer displays the Add Tables dialog box when you right-click the Tables node in a connection and select Add Tables on the shortcut menu in the Catalog Manager, and provides you with different options in the dialog box according to the different type of the connection: [XML/JSON/Elasticsearch](#XML), [Web Service](#Web), or [MongoDB](#MongoDB).

---

For an [XML](https://devnet.logianalytics.com/hc/en-us/articles/4405661442711-Working-with-XML-Connections-in-a-Catalog#Add), [JSON](https://devnet.logianalytics.com/hc/en-us/articles/4405661432343-Working-with-JSON-Connections-in-a-Catalog#Add), or [Elasticsearch](https://devnet.logianalytics.com/hc/en-us/articles/4405661442711-Working-with-XML-Connections-in-a-Catalog#Add) connection, Designer displays the following options in the dialog box:

![Add Tables dialog box - XML/JSON](https://devnet.logianalytics.com/hc/article_attachments/4420556223511/addtbl_xml.gif)

**Database Catalogs**

This drop-down list is disabled for an XML, JSON, or Elasticsearch connection.

**Schemas**

This box lists the schemas transformed from the corresponding data source.

**Tables**

This box displays the tables contained in the selected schema after you select the Refresh button.

**Connection**

This option shows the name of the current connection.

**Refresh**

Select to load the tables contained in the specified schema into the Tables box.

**Add**

Select to add the specified tables to the catalog.

**Done**

Select to complete the adding tables process and close the dialog box.

**Help**

Select to view information about the dialog box.

---

For a [web service](https://devnet.logianalytics.com/hc/en-us/articles/4405661439639-Connecting-via-SOAP-Web-Service-Connections#Table) connection, Designer displays the following options in the dialog box:

![Add Tables dialog box - web service connection](https://devnet.logianalytics.com/hc/article_attachments/4420556223767/addtbl_wbsvc.gif)

**Service Name**

This drop-down list contains all the service information defined in the WSDL file. Select the service to use.

**Port Type**

Designer enables the drop-down list only when the web service is defined by WSDL 1.1. Select the port type for the selected service. A port type is a set of abstract operations and the abstract messages involved.

**Operation Name**

This drop-down list contains all the operation information for the selected service. Select the operation to use. An operation is an abstract description of an action supported by the service. Each operation refers to an input message and output messages.

**Time Out**

Specify how long to wait to get the service and operation information defined in the WSDL file.

**Use Schema from Response**

Designer enables this option only when the web service is defined by WSDL 1.1.

When the XML schema in the output message does not match the specific XML instance in the SOAP responded from the web service, Logi Report Engine is not able to read data properly from that XML instance. In this condition, you can use this option to control whether to ignore the XML schema in the output message and parse the XML schema directly from the specific XML instance in the SOAP for the web service.

**Input Message**

This column shows the input message information for the selected operation.

**Value**

This column shows the values for the input messages. You can type the value, or define a constant level formula or a parameter to be the value.

**OK**

Select to apply the adding table result and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

For a [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405664420375-Working-with-MongoDB-Connections-in-a-Catalog#AddTable) connection, Designer displays the following options in the dialog box:

![Add Tables dialog box - MongoDB connection](https://devnet.logianalytics.com/hc/article_attachments/4420542181911/addtbl_mngodb.gif)

**Tables**

This box lists the tables transformed from the relational schemas, which you can add to the catalog.

**Added Tables**

This box lists the tables that you select to add to the catalog.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified tables in the Tables box to use in the catalog.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified tables from the Added Tables box.

**OK**

Select to add the specified tables to the catalog.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661451543-Add-Stored-Procedures-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661454359-Add-Tables-Views-Queries-Dialog-Box)
