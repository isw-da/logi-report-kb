---
title: "Working with XML Connections in a Catalog"
id: 4405661442711
section: "Connecting to Your Data Sources - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661442711-Working-with-XML-Connections-in-a-Catalog
updated_at: 2022-01-27T20:34:43Z
---

# Working with XML Connections in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661441687-How-Designer-Gets-Data-from-XML-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661439639-Connecting-via-SOAP-Web-Service-Connections)

# Working with XML Connections in a Catalog

This topic describes how you can set up XML connections in a catalog, and add and manage tables transformed from XML data sources in the catalog via the connections.

This topic contains the following sections:

* [Setting Up XML Connections in a Catalog](#Set)
* [Adding More Tables to an XML Connection](#Add)
* [Managing Tables in an XML Connection](#Manage)

## Setting Up XML Connections in a Catalog

To set up an XML connection to connect a catalog to an XML data source, take the following steps:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **Add XML Connection** from the shortcut menu.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **XML** connection type and select **OK**.

   Designer displays the [XML Connection Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661750167-XML-Connection-Wizard-Dialog-Box).

   ![XML Connection Wizard](https://devnet.logianalytics.com/hc/article_attachments/4420394713623/xmlcnnctn_import.gif)
3. In the **Import XML Schema** screen, specify [the way to import the XML schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405661441687-How-Designer-Gets-Data-from-XML-Data-Sources#Import) from the **Schema Type** drop-down list: **Import from XSD** or **Parse from XML Instance**.
4. Provide the required information for importing the XML schemas.
   * If you select **Import from XSD** as the schema type,
     1. In the **Schema Name** text box, type the URI string of the schema file or select **Browse** to select the file.

        In the URI string, you can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/4405661800215-Working-with-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405664602263-Formula-Levels#CLF) in the current catalog data source in the format *@FieldName*, and the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields#UserName)" as *@username*. For example, if a URI string is `http://localhost:8080/rest/getData?startDate=2016-01-01`, and you want to use the parameters pHost, pPort, and pStartDate to dynamically generate the URI at runtime, then the URI string is `http://@pHost:@pPort/rest/getData?startDate=@pStartDate`. Moreover, if a URI string contains characters, such as @, '.', or double quotation marks, or other strings that do not need to be parsed, quote them with double quotation marks. You can select **New Parameter** to create a parameter in the current catalog data source and reference it in the URI string. If you use the special field "User Name", when you select Next in the connection wizard, Designer displays the Security Identifier dialog box for you to specify the user name with which to generate the stream. When you run reports created on the XML data on Server, the real user's ID will be used.
     2. If the specified URI string begins with the "http://" or "https://" protocol, Designer enables the **RESTful** button. Select the button to specify the RESTful options for the schema file in the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661694743-RESTful-Data-Source-Options-Dialog-Box).

        ![RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420394732183/rstdtsrc.gif)
     3. To receive the remote data via REST Web Service on the application server, select **Via REST Web Service**, then from the **MIME Type** drop-down list, select the MIME type for the REST Web Service data source. You can also specify the type in the text box manually. The REST Web Service Client API (such as the JAX-RS Client API of Java EE) will then be used to get the remote data. When you use a proxy to connect to the REST Web Service, you need to [configure the proxy parameters](https://devnet.logianalytics.com/hc/en-us/articles/4405661432343-Working-with-JSON-Connections-in-a-Catalog#Proxy) in Designer so that the proxy can work successfully.

        If you do not select Via REST Web Service, Designer receives the remote data via the protocol in the URL you specify in the **Schema Name** text box in the connection wizard.
     4. Specify the user name and password for remote data authentication.
     5. Select **HTTP Advanced Options** to specify the advanced HTTP options.
     6. Select an HTTP method from the **Method** drop-down list to send the request, which can be GET or POST.
     7. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif) above the **Headers** box to add a header line, then specify the name and value of the user-defined HTTP header. Repeat this to edit more headers. To delete a header, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif).
     8. In the **Body** box, specify the user-defined HTTP body.
     9. When editing the HTTP headers and body, you can reference parameters and constant level formulas predefined in the current catalog data source, and the special field "User Name". Select **New Parameter**![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/4420394732439/btn_nwparam.gif) to create a parameter and reference it in the header or body, if the predefined parameters cannot meet your requirements.
     10. If you reference parameters and formulas in the HTTP headers and body, you can select **Edit Format** to edit the format of their values.
     11. Select **OK** to apply the specified RESTful data source options and return to the XML Connection Wizard dialog box.
     12. From the **Starting Node** drop-down list, specify the starting node accordingly.
     13. Specify the XML instance file.

         To use an instance file from URI, select **URI**, then type the URI string in the **Instance** text box or select **Browse** to select the instance file. You can also reference parameters, constant level formulas, and the special field "User Name" in the URI string. When the specified URI string begins with `http://` or `https://` protocol, Designer enables the **RESTful** button. Select the button to specify the [RESTful options](#RESTful) for the instance data.

         To use an instance file from a user-defined interface, select **User Defined**, then provide the class name with package name in the Class Name field. You can also select **Browse** to find the class file. The class you specify must exist and can be found by Designer, also by Server at runtime, which means the class should be in the class path of the system environment. After filling in this text box, Designer automatically displays the class name of the interface that the class implements behind "The class implements:". Specify the parameter string for the user-defined interface in the Parameter box. The parameter string must match the format defined in the class. You can also reference parameters, constant level formulas, and the special field "User Name" in the parameter string.
     14. Select **Validate with schema before fetching** to validate whether values in the XML instance are valid according to the W3C standard and the selected XSD schema.

         ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg)

         + If a value of DateTime data type is accurate to millisecond, although the value is valid according to the W3C standard, a message "Invalid Value" still pops up. You can ignore the error message and continue the transformation process.
         + If you use a parameter to dynamically specify an XML instance at runtime, the XML instance will be validated at runtime rather than in the importing process.
   * If you select **Parse from XML Instance** as the schema type, type the URI string of the XML instance in the **Schema Name** text box or select **Browse** to select it. In the URI string, you can reference parameters, constant level formulas, and the special field "User Name". When the specified URI string begins with `http://` or `https://` protocol, Designer enables the **RESTful** button. Select the button to specify the [RESTful options](#RESTful) for the instance data.
5. Select **Time Zone and Locale** to specify the time zone and the locale for the XML instance in the [Time Zone and Locale Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664589207-Time-Zone-and-Locale-Options-Dialog-Box).
6. When you reference parameters and formulas in the URI/parameter string, you can select **Edit Format** to edit the format of their values.
7. Select **Next** to go to the next screen.
8. In the **Modify Schema Properties** screen, [supplement and modify the element properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661441687-How-Designer-Gets-Data-from-XML-Data-Sources#SupplementInfo) and then select **Next**.

   ![XML Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4420394713879/xmlcnnctn_modify.gif)
9. In the **Transform XML Schema** screen, select an XPath to be the transforming start point. Select **Next**.

   ![XML Connection Wizard - Transform XML Schema](https://devnet.logianalytics.com/hc/article_attachments/4420394714263/xmlcnnctn_trnsfrm.gif)
10. In the **Transformed Relational Schema** screen, check the transformed result, and then select **Next**.

    ![XML Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4420402387479/xmlcnnctn_trnsfrmd.gif)
11. In the **Add Table** screen, add the required tables to the connection, and select **Generate the default pre-join path** for generating default pre-join paths for the tables. A table contains fields mapped to attributes, simple elements, contents of complex elements, and other nodes in the XML data source.

    ![XML Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4420402387991/xmlcnnctn_add.gif)

    You can create [queries](https://devnet.logianalytics.com/hc/en-us/articles/4405661915543-Working-with-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/4405664680215-Working-with-Business-Views) using these tables and a report is developed from a query (or something else which is functionally similar) or from a business view.
12. Select **Finish** to confirm the transformed result and complete the transformation process.

## Adding More Tables to an XML Connection

After you have set up an XML connection in a catalog, you can add more tables transformed from the XML data source into the catalog via the XML connection.

**To add tables to an XML connection**

1. Do one of the following:
   * Right-click the XML connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the XML connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the XML connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the XML connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the XML connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   Designer displays the [Add Tables dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664425495-Add-Tables-Dialog-Box).

   ![Add Tables dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402540695/addtbl_xml.gif)
2. Select **Refresh**.
3. Designer lists the tables contained in the schema that it transforms from the XML file in the **Tables** box. Choose the required tables and select **Add**.
4. After adding the required tables, select **Done** to close the dialog box.

## Managing Tables in an XML Connection

For the tables that have been transformed from an XML data source and added into a catalog via an XML connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms#Remove) the same as you do with tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661441687-How-Designer-Gets-Data-from-XML-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661439639-Connecting-via-SOAP-Web-Service-Connections)
