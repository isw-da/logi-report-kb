---
title: "Add Tables Dialog"
id: 1500010029762
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029762-Add-Tables-Dialog
updated_at: 2021-07-24T10:39:10Z
---

# Add Tables Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029702-Add-Stored-Procedures-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064701-Add-Tables-Views-Queries-Dialog)

# Add Tables Dialog

The Add Tables dialog helps you to add tables into a Logi JReport catalog via the connection you set up. It appears when you right-click the Tables node in a connection and select Add Tables on the shortcut menu in the Catalog Manager, and varies according to connection types.

If it is an [XML](https://devnet.logianalytics.com/hc/en-us/articles/1500010064601-Working-with-XML-Connections-in-a-Catalog#Add), [JSON](https://devnet.logianalytics.com/hc/en-us/articles/1500010029482-JSON-Connections#Add) or [Elasticsearch](https://devnet.logianalytics.com/hc/en-us/articles/1500010064601-Working-with-XML-Connections-in-a-Catalog#Add) connection, options in the dialog are as follows.

![Add Tables dialog - XML/JSON](https://devnet.logianalytics.com/hc/article_attachments/4404901297047/addtbl_xml.gif)

**Database Catalogs**

Lists all the catalogs in the database. Not supported here.

**Schemas**

Lists the schema transformed from the corresponding data source.

**Tables**

Lists the tables contained in the schema after you select the Refresh button.

**Connection**

Shows the name of the current connection.

**Refresh**

Loads the tables contained in the specified schema into the Tables box.

**Add**

Adds the selected tables to the Logi JReport catalog.

**Done**

Completes the adding tables process and closes the dialog.

**Help**

Displays the help document about this feature.

---

If it is a [web service](https://devnet.logianalytics.com/hc/en-us/articles/1500010064561-SOAP-Web-Service-Connections#Table) connection, options in the dialog are as follows.

![Add Tables dialog - web service connection](https://devnet.logianalytics.com/hc/article_attachments/4404901297559/addtbl_wbsvc.gif)

**Service Name**

Contains all the service information defined in the WSDL file. Select one you want from the drop-down list.

**Port Type**

Specifies the port type for the selected service. A port type is a set of abstract operations and the abstract messages involved. Available only when the web service is defined by WSDL 1.1. Select one you want from the drop-down list.

**Operation Name**

Contains all the operation information for the selected service. Select one you want from the drop-down list. An operation is an abstract description of an action supported by the service. Each operation refers to an input message and output messages.

**Time Out**

Specifies how long to wait to get the service and operation information defined in the WSDL file.

**Use Schema from Response**

This option is available only when the web service is defined by WSDL 1.1.

When the XML schema in the output message does not match the specific XML instance in the SOAP responded from the web service, Logi JReport will not be able to read data properly from that XML instance. In this condition, you can use this option to control whether to ignore the XML schema in the output message and parse the XML schema directly from the specific XML instance in the SOAP for the web service.

**Input Message**

Lists the input message information for the selected operation.

**Value**

Specifies the value for the input message. Type in the value, or define a constant level formula or a parameter to be the value.

**OK**

Accepts the adding table result and closes the dialog.

**Cancel**

Cancels the adding table process and exists the dialog.

**Help**

Displays the help document about this feature.

---

If it is a [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/1500010029522-Working-with-MongoDB-Connections-in-a-Catalog#AddTable) connection, options in the dialog are as follows.

![Add Tables dialog - MongoDB connection](https://devnet.logianalytics.com/hc/article_attachments/4404901297815/addtbl_mngodb.gif)

**Tables**

Lists the tables transformed from the relational schemas.

**Added Tables**

Lists the tables that you have added.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected tables.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)

Removes the selected tables from the Added Tables box.

**OK**

Accepts the adding table result and closes the dialog.

**Cancel**

Cancels the adding table process and exists the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029702-Add-Stored-Procedures-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064701-Add-Tables-Views-Queries-Dialog)
