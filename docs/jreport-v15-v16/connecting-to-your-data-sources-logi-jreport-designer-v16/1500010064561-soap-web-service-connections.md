---
title: "SOAP Web Service Connections"
id: 1500010064561
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064561-SOAP-Web-Service-Connections
updated_at: 2021-07-24T10:39:13Z
---

# SOAP Web Service Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064601-Working-with-XML-Connections-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029502-MongoDB-Connections)

# SOAP Web Service Connections

Web services provide a standard means of interoperating between different software applications, running on a variety of platforms and/or frameworks. It is a way to connect to a remote application and request data directly from the application without going to a DBMS. Logi JReport Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources. You can add SOAP Web Service data sources to Logi JReport catalogs by importing WSDL files.

Below is a list of the sections covered in this topic:

* [Setting up Web Service Connections in a Catalog](#Set)
* [Adding Tables to a Web Service Connection](#Table)
* [Editing the Operation Used to Create Tables](#Operation)
* [Managing the Tables in a Web Service Connection](#Manage)

## Setting Up Web Service Connections in a Catalog

To set up a web service connection to connect a Logi JReport catalog to a web service data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **New SOAP Web Service Connection** from the shortcut menu.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **SOAP Web Service**  connection type and select **OK**.

   The [SOAP Web Service Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010068361-SOAP-Web-Service-Data-Source-Dialog) dialog appears.

   ![SOAP Web Service Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901168151/wbsvc.gif)
3. Specify a WSDL file to create the web service connection.
   * If you want to use a WSDL file on your local disk, check the **Local File** radio button, then select the **Browse** button to browse for the file.
   * If you want to use a WSDL file through a URI, check the **URI** radio button, then input the URI string in the text box that follows and specify the user name and password for assessing the WSDL file.
4. Select the **Options** button to show the additional settings.
5. Select the **Time Zone and Locale** button to specify the time zone and the locale as required.
6. If you want the catalog or schema, or both of them to be used in data manipulation, make the selection in the Qualified Name Pattern box according to your requirements.
7. Input the number of seconds in the Time Out text box to specify how long to wait to get the WSDL file.
8. Select the **Security Configuration** button to display the [Security Configuration Setting](https://devnet.logianalytics.com/hc/en-us/articles/1500010067701-Security-Configuration-Setting-Dialog) dialog to configure the security policy.

   ![Security Configuration Setting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909157911/scrtyconfigset.gif)
9. Specify the user name and password for the user name token to be used in the security policy.
10. Specify the type for the key store from the Key Store Type drop-down list.
11. Select the **Browse** button next to Key Store File to specify the key store file.
12. Input the password in the Key Store Password text box to get the access to the key store file.
13. In the Client Key box, specify the alias name to be used as client signature in the key store, and set the password for the name.
14. In the Server Key box, specify the alias name and password to be used to get the server-side certification or public key in the key store.
15. Select **OK** to go back to the SOAP Web Service Data Source dialog.
16. Select **OK** to set up the web service connection.

**Note:** When you configure the security policy for a web service connection, except for Key Store Type, all the other options in Security Configuration Setting dialog can be controlled by [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010068561-Formula-Levels#CLF). However, the formula control is only available after the web service connection is already set up, that is when you edit an existing web service connection.

## Adding Tables to a Web Service Connection

After a web service connection is set up, all the information of the web service defined in the WSDL file will be stored in the catalog, including information of service, operation, and the input message and output message in each operation. You can then add tables into the Logi JReport catalog via the connection based on this information. However you can only define tables based on operations which support SOAP binding.

1. Do any of the following:
   * Right-click the web service connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the web service connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the web service connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the web service connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the web service connection, or any existing table or folder in the connection any and select **Add Tables** on the Catalog Manager toolbar.

   The [Add Table](https://devnet.logianalytics.com/hc/en-us/articles/1500010029762-Add-Tables-Dialog) dialog appears.

   ![Add Tables dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901297559/addtbl_wbsvc.gif)
2. Specify a service from the Service Name drop-down list.
3. If you use WSDL 1.1 to define the web service, you also need to specify the port type for the selected service from the Port Type drop-down list.
4. All the operations with SOAP binding that are included in the selected service are listed in the Operation Name drop-down list. Select one as required, then the input message of the operation will be displayed. You can define the value for the input message if necessary by either typing in the value in the text box in the Value column, or selecting ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) in the text box to select or define a [constant level formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010068561-Formula-Levels#CLF) or [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010068961-Parameters) in the current catalog data source to return the value.

   If the Input Message column is empty, that is to say, the input message has its own defined values, so there is no need for you to provide it the value.
5. Type the number of seconds in the Time Out text box to specify how long to wait to get the specified service and operation information defined in the WSDL file.
6. If you use WSDL 1.1, you may sometimes find that the XML schema described by the output message does not match the concrete XML instance in the SOAP responded from the web service, as a result, Logi JReport will be unable to read data properly from that XML instance. In this case, you can check the option **Use Schema from Response**, so as to ignore the XML schema in the output message and directly parse the XML schema from the specific XML instance included in the SOAP responded from the web service.
7. Select **OK** to accept the changes and exit the dialog.

You can then create [queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010070681-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010070641-Business-Views) based on these tables. A report is developed from a query (or something else which is functionally similar) or from a business view.

## Editing the Operation Used to Create Tables

The service and operation you have selected to create the tables in a web service connection is displayed under the Tables node of the connection. If you use WSDL 1.1 to define the web service, the defined port type is also included. You can edit the information of the operation if necessary.

1. Select the web service operation node, right-click it and then select **Edit** from the shortcut menu. The [Edit Operation Calling Property](https://devnet.logianalytics.com/hc/en-us/articles/1500010065701-Edit-Operation-Calling-Property-Dialog) dialog appears.

   ![Edit Operation Calling Property dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909223703/edtoprtn.gif)
2. In the Input Message column, select the input message you want to edit, then modify its value in the text box of the Value column as required. You can either input the value, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) in the text box to select or define a [constant level formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010068561-Formula-Levels#CLF) or [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010068961-Parameters) in the current catalog data source to return the value of the input message.
3. Type the number of seconds in the Time Out text box to specify how long to wait for the operation to complete.
4. If you use WSDL 1.1 to define the web service, the option Use Schema from Response is available. Check it if you want to ignore the XML schema described in the output message and parse the XML schema directly from the specific XML instance in the SOAP responded from the web service.
5. Select **OK** to accept the changes and exit the dialog.

## Managing the Tables in a Web Service Connection

When the tables have been added into the Logi JReport catalog via the web service connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Remove) the same as you do on tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064601-Working-with-XML-Connections-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029502-MongoDB-Connections)
