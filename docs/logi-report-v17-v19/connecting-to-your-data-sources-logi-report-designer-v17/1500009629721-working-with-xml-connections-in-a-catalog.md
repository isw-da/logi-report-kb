---
title: "Working with XML Connections in a Catalog"
id: 1500009629721
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629721-Working-with-XML-Connections-in-a-Catalog
updated_at: 2021-07-24T16:05:04Z
---

# Working with XML Connections in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607062-How-Logi-Report-Gets-Data-from-XML-Data-Sources) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629701-SOAP-Web-Service-Connections)

# Working with XML Connections in a Catalog

This topic introduces how to set up XML connections in a Logi Report catalog to get data from XML data sources, and manage the tables that are transformed from the XML data sources in the Logi Report catalog.

This topic includes the following sections:

* [Setting Up XML Connections in a Catalog](#Set)
* [Adding More Tables to an XML Connection](#Add)
* [Managing the Tables in an XML Connection](#Manage)

## Setting Up XML Connections in a Catalog

To set up an XML connection to connect a Logi Report catalog to an XML data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **Add XML Connection** from the shortcut menu.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **XML** connection type and select **OK**.

   The [XML Connection Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009634021-XML-Connection-Wizard-Dialog) appears.

   ![XML Connection Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404904228887/xmlcnnctn_import.gif)
3. In the Import XML Schema screen, specify [the way to import the XML schemas](https://devnet.logianalytics.com/hc/en-us/articles/1500009607062-How-Logi-Report-Gets-Data-from-XML-Data-Sources#Import) from the Schema Type drop-down list: Import from XSD or Parse from XML Instance.
4. Provide the required information for importing the XML schemas.
   * If Import from XSD is selected in the Schema Type drop-down list:
     1. In the Schema Name text box, type the URI string of the schema file or select **Browse** to select the file.

        In the URI string, you can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#CLF) in the current catalog data source and the special field User Name in the format "*@fieldname*". For example, if a URI string is `http://localhost:8080/rest/getData?startDate=2016-01-01`, and you want to use the parameters pHost, pPort and pStartDate to dynamically generate the URI at runtime, then the URI string will be `http://@pHost:@pPort/rest/getData?startDate=@pStartDate`. Moreover, if a URI string contains characters, such as @, '.' or double quotation marks, or other strings that do not need to be parsed, quote them with double quotation marks. You can select **New Parameter** to create a parameter in the current catalog data source and reference it in the URI string. If the special field User Name is used, when selecting Next in the connection wizard, the Security Identifier dialog will pop up for you to specify the user name with which to generate the stream in Logi Report Designer. When running reports created on the XML data in Logi Report Server, the real user's ID will be used.
     2. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the RESTful options for the schema file in the [RESTful Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009610062-RESTful-Data-Source-Options-Dialog) dialog.

        ![RESTful Data Source Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911686039/rstdtsrc.gif)
     3. To receive the remote data via REST Web Service, select **Via REST Web Service**, then from the MIME Type drop-down list, select the MIME type for the REST Web Service data source. You can also specify the type in the text box directly. The remote data will then be provided by the REST Web Services on the application server, and the REST Web Service Client API (such as JAX-RS client API of Java EE) will be used to get the remote data.
        ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")When a proxy is used for connecting to the REST Web Service, you need to [configure the proxy parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009606902-JSON-Connections#Proxy) in Logi Report so that the proxy can work successfully.

        When Via REST Web Service is unselected, the remote data will be received via the protocol in the URL you specify in the Schema Name text box in the connection wizard.
     4. Specify the user name and password for remote data authentication.
     5. Select **HTTP Advanced Options** to specify the advanced HTTP options.
     6. Select an HTTP method from the Method drop-down list to send the request, which can be GET or POST.
     7. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the Headers box to add a header line, then specify the name and value of the user defined HTTP header. Repeat this to edit more headers.
     8. In the Body box, specify the user defined HTTP body.
     9. When editing the HTTP headers and body, you can reference the parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname". You can select ![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/4404904245655/btn_nwparam.gif) to create a parameter in the current catalog data source and reference it in the header or body. When parameters and formulas are referenced, you can select the **Edit Format** button to edit the format of their values.
     10. select **OK** to apply the specified RESTful data source options and return to the XML Connection Wizard.
     11. From the Starting Node drop-down list, specify the starting node accordingly.
     12. Specify the XML instance file.

         To use an instance file from URI, select the **URI** radio button, then type the URI string in the Instance text box or select **Browse** to select the instance file. You can also reference parameters, constant level formulas and the special field User Name in the URI string. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the [RESTful options](#RESTful) for the instance data.

         To use an instance file from a user defined interface, select **User Defined**, then provide the class name with package name in the Class Name field. You can also select **Browse** to find the class file. The class you specify must exist and can be found by Logi Report Designer and Logi Report Server at runtime, which means the class should be in the class path of the system environment. After filling in this field, the class name of the interface that the class implements will be displayed automatically behind "The class implements:". Then specify the parameter string for the user defined interface in the Parameter box. The parameter string must match the format defined in the class. You can also reference parameters, constant level formulas, and the special field User Name in the parameter string.
     13. Select **Validate with schema before fetching** to validate whether or not values in the XML instance are valid according to the W3C standard and the selected XSD schema.

         **Notes:**

         + If a value of DateTime data type is accurate to millisecond, although the value is valid according to the W3C standard, a message - Invalid Value still pops up. You can ignore the error message and continue the transformation steps.
         + If you use a parameter to dynamically specify an XML instance at runtime, the XML instance will be validated at runtime rather than in the importing process.
   * If Parse from XML Instance is selected in the Schema Type drop-down list, type the URI string of the XML instance in the Schema Name text box or select **Browse** to select it. In the URI string, you can reference parameters, constant level formulas and the special field User Name. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the [RESTful options](#RESTful) for the instance data.
5. Select the **Time Zone and Locale** button to specify the time zone and the locale for the XML instance in the [Time Zone and Locale Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009633921-Time-Zone-and-Locale-Options-Dialog) dialog.
6. When parameters and formulas are referenced in the URI/parameter string, you can select the **Edit Format** button to edit the format of their values.
7. Select **Next** to go to the next screen.
8. In the Modify Schema Properties screen, [supplement and modify the element properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009607062-How-Logi-Report-Gets-Data-from-XML-Data-Sources#SupplementInfo) as required and then select **Next**.

   ![XML Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404911672727/xmlcnnctn_modify.gif)
9. In the Transform XML Schema screen, select an XPath to be the transforming start point. Select **Next**.

   ![XML Connection Wizard - Transform XML Schema](https://devnet.logianalytics.com/hc/article_attachments/4404904230039/xmlcnnctn_trnsfrm.gif)
10. In the Transformed Relational Schema screen, check the transformed result, and then select **Next**.

    ![XML Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404911673239/xmlcnnctn_trnsfrmd.gif)
11. In the Add Table screen, add the required tables to the connection, and select **Generate the default pre-join path** for generating default pre-join paths for the tables. A table contains fields mapped to attributes, simple elements, contents of complex elements, and other nodes in the XML data source.

    ![XML Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404911673495/xmlcnnctn_add.gif)

    [Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009635921-Business-Views) can be created based on these tables and a report is developed from a query (or something else which is functionally similar) or from a business view.
12. Select **Finish** to confirm the transformed result and complete the transformation process.

## Adding More Tables to an XML Connection

When an XML connection is set up, you can add more tables transformed from the XML data source into the Logi Report catalog via the XML connection.

1. Do one of the following:
   * Right-click the XML connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the XML connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the XML connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the XML connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the XML connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   The [Add Tables](https://devnet.logianalytics.com/hc/en-us/articles/1500009607162-Add-Tables-Dialog) dialog appears.

   ![Add Tables dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916819991/addtbl_xml.gif)
2. Select the **Refresh** button. The tables contained in the schema that is transformed from the XML file will then be displayed in the Tables box.
3. Choose the required tables in the Tables box, and then select **Add**.

   To choose consecutive tables, select the first table, press and hold down the **SHIFT** key, and then select the last table. To choose tables that are not consecutive, press and hold down **CTRL**, and then select each table.
4. After adding the required tables, select **Done** to close the dialog.

## Managing the Tables in an XML Connection

For the tables that have been transformed from an XML data source and added into a Logi Report catalog via the specified XML connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms#Remove) the same as you do on tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607062-How-Logi-Report-Gets-Data-from-XML-Data-Sources) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629701-SOAP-Web-Service-Connections)
