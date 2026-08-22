---
title: "Add Tables Dialog Box"
id: 45190489806733
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190489806733-Add-Tables-Dialog-Box
updated_at: 2026-04-30T15:12:45Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Add Tables Dialog Box

You can use the Add Tables dialog box to add tables into a catalog via the connection you set up. This topic describes the options in the dialog box.
    

Designer displays the Add Tables dialog box when you right-click the Tables node in a connection and select Add Tables on the shortcut menu in the Catalog Manager, and provides you with different options in the dialog box according to the different type of the connection: XML/JSON/Elasticsearch, Web Service, or MongoDB.

For an XML, JSON, or Elasticsearch connection, Designer displays the following options in the dialog box:

Database Catalogs

This drop-down list is disabled for an XML, JSON, or Elasticsearch connection.

Schemas

This box lists the schemas transformed from the corresponding data source.

Tables

This box displays the tables contained in the selected schema after you select the Refresh button.

Connection

This option shows the name of the current connection.

Refresh

Select to load the tables contained in the specified schema into the Tables box.

Add

Select to add the specified tables to the catalog.

Done

Select to complete the adding tables process and close the dialog box.

Help

Select to view information about the dialog box.

 

For a SOAP Web Service connection, Designer displays the following options in the dialog box:

Service Name

This drop-down list contains all the service information defined in the WSDL file. Select the service to use.

Port Type

Designer enables this drop-down list only when the SOAP Web Service is defined by WSDL 1.1. Select the port type for the selected service. A port type is a set of abstract operations and the abstract messages involved.

Operation Name

This drop-down list contains all the operation information for the selected service. Select the operation to use. An operation is an abstract description of an action supported by the service. Each operation refers to an input message and output messages.

Time Out

Specify how long to wait to get the service and operation information defined in the WSDL file.

Use Schema from Response 

Designer enables this option only when the SOAP Web Service is defined by WSDL 1.1.

When the XML schema in the output message does not match the specific XML instance in the SOAP responded from the web service, Report Engine is not able to read data properly from that XML instance. In this condition, you can use this option to control whether to ignore the XML schema in the output message and parse the XML schema directly from the specific XML instance in the SOAP for the web service.

Input Message

This column shows the input message information for the selected operation.

Value

This column shows the values for the input messages. You can type the value, or define a constant level formula or a parameter to be the value.

OK

Select to apply the adding table result and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

 

For a MongoDB connection, Designer displays the following options in the dialog box:

Tables

This box lists the tables transformed from the relational schemas, which you can add to the catalog.

Added Tables

This box lists the tables that you select to add to the catalog.

Add button

Select to add the specified tables in the Tables box to use in the catalog.

Remove button

Select to remove the specified tables from the Added Tables box.

OK

Select to add the specified tables to the catalog.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
