---
title: "Working with XML Connections in a Catalog"
id: 5735499628183
section: "Connecting to Your Data Sources - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735499628183-Working-with-XML-Connections-in-a-Catalog
updated_at: 2022-11-02T04:14:08Z
---

# Working with XML Connections in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735528222487-How-Designer-Gets-Data-from-XML-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735528205847-Accessing-Data-via-SOAP-Web-Service-Connections)

# Working with XML Connections in a Catalog

This topic describes how you can set up XML connections in a catalog, and add and manage tables transformed from XML data sources in the catalog via the connections.

This topic contains the following sections:

* [Setting Up XML Connections in a Catalog](#Set)
* [Adding More Tables to an XML Connection](#Add)
* [Managing Tables in an XML Connection](#Manage)

## Setting Up XML Connections in a Catalog

To set up an XML connection to connect a catalog to an XML data source, take the following steps:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, do either of the following:
   * To set up the connection in an existing data source in the catalog, right-click the data source node and select **Add XML Connection** from the shortcut menu.
   * To set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **XML** connection type and select **OK**.

   Designer displays the [XML Connection Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544859287-XML-Connection-Wizard-Dialog-Box).

   ![XML Connection Wizard](https://devnet.logianalytics.com/hc/article_attachments/9898533503767/xmlcnnctn_import.gif)
3. In the **Import XML Schema** screen, specify [the way to import the XML schema](https://devnet.logianalytics.com/hc/en-us/articles/5735528222487-How-Designer-Gets-Data-from-XML-Data-Sources#Import) from the **Schema Type** drop-down list: [Import from XSD](#XSD) or [Parse from XML Instance](#XMLInstance).
4. Provide the information for importing the XML schema.
   * When you select the schema type as **Import from XSD**
     1. In the **Schema Name** text box, type the URI string of the schema file or select **Browse** to select the file.
        + In the URI string, you can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/5735532413719-Working-with-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#CLF) in the current catalog data source in the format *@FieldName*, and the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields#UserName)" as *@username*. For example, if a URI string is `http://localhost:8080/rest/getData?startDate=2016-01-01`, and you want to use the parameters pHost, pPort, and pStartDate to dynamically generate the URI at runtime, then the URI string is `http://@pHost:@pPort/rest/getData?startDate=@pStartDate`.
        + You can select **New Parameter** to create a parameter in the current catalog data source and reference it in the URI string, when the predefined parameters cannot meet your requirement.
        + When the URI string contains characters, such as "@", ":", and double quotation marks, or other strings that do not need to be parsed, you should quote them with double quotation marks.
        + If you use the special field "User Name", when you select Next in the connection wizard, Designer displays the Security Identifier dialog box for you to specify the user name that you want to use to generate the stream. When a user runs a report that uses data from the XML data source at runtime, Server applies the user's ID.
     2. When the URI string you specify begins with the "http://" or "https://" protocol, Designer enables the **RESTful** button. Select the button to specify RESTful options for the schema file in the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567159831-RESTful-Data-Source-Options-Dialog-Box).

        ![RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898478146839/rstdtsrc.gif)
     3. To receive the remote data via REST Web Service on the application server, select **Via REST Web Service**, then from the **MIME Type** drop-down list, select the MIME type for the REST Web Service data source. You can also specify the type in the text box manually. The REST Web Service Client API (such as the JAX-RS Client API of Java EE) will then be called to get the remote data. When you use a proxy to connect to the REST Web Service, you need to [configure the proxy parameters](https://devnet.logianalytics.com/hc/en-us/articles/6417117277591-Configuring-Proxy-for-Connecting-to-REST-Web-Service) to enable the proxy to work successfully.

        ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) If you do not select Via REST Web Service, Designer receives the remote data via the protocol in the URL you specify in the Schema Name text box in the connection wizard.
     4. Specify the user name and password for remote data authentication.
     5. Select **HTTP Advanced Options** to specify the advanced HTTP options.
     6. Select an HTTP method from the **Method** drop-down list to send the request, which can be GET or POST.
     7. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) above the **Headers** box to add a header line, then specify the name and value of the user-defined HTTP header. Repeat this to edit more headers. To delete a header, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
     8. In the **Body** box, specify the user-defined HTTP body.
     9. When editing the HTTP headers and body, you can reference parameters, constant level formulas, and the special field "User Name" [as described earlier](#RefParam). When the predefined parameters cannot meet your requirements, you can select ![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/9898478152855/btn_nwparam.gif) to create the parameter.
     10. If you reference parameters and formulas in the HTTP headers and body, you can select **Edit Format** to edit the format of their values.
     11. Select **OK** to apply the RESTful data source options and return to the XML Connection Wizard dialog box.
     12. From the **Starting Node** drop-down list, specify the starting node accordingly.
     13. Specify the XML instance file.
         + To use an instance file from URI, select **URI**, then type the URI string in the **Instance** text box or select **Browse** to select the instance file. You can also reference parameters, constant level formulas, and the special field "User Name" in the URI string [as described earlier](#RefParam). When the specified URI string begins with the "http://" or "https://" protocol., Designer enables the **RESTful** button. Select the button to specify [RESTful options](#RESTful) for the instance data.
         + To use an instance file from a user-defined interface, select **User Defined**, then provide the class name with package name in the Class Name field. You can also select **Browse** to find the class file. The class you specify must exist and can be found by Designer, also by Server at runtime, which means the class should be in the class path of the system environment. After filling in this text box, Designer automatically displays the class name of the interface that the class implements behind "The class implements:". Specify the parameter string for the user-defined interface in the **Parameter** box. The parameter string must match the format defined in the class. You can also reference parameters, constant level formulas, and the special field "User Name" in the parameter string.
     14. Select **Validate with schema before fetching** to validate whether values in the XML instance are valid according to the W3C standard and the selected XSD schema.

         ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

         + If a value of DateTime data type is accurate to millisecond, although the value is valid according to the W3C standard, Designer still displays the "Invalid Value" message. You can ignore the error message and continue the transformation process.
         + If you use a parameter to dynamically specify an XML instance at runtime, the XML instance will be validated at runtime rather than in the importing process.
   * When you select the schema type as **Parse from XML Instance**, type the URI string of the XML instance in the **Schema Name** text box or select **Browse** to select it. In the URI string, you can reference parameters, constant level formulas, and the special field "User Name" [as described earlier](#RefParam). When the URI string you specify begins with the "http://" or "https://" protocol, Designer enables the **RESTful** button. Select the button to specify [RESTful options](#RESTful) for the instance data.
5. Select **Time Zone and Locale** to specify the time zone and locale for the XML instance in the [Time Zone and Locale Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735525134999-Time-Zone-and-Locale-Options-Dialog-Box).
6. When you reference parameters and formulas in the URI/parameter string, you can select **Edit Format** to edit the format of their values.
7. Select **Next**. Designer displays the **Modify Schema Properties** screen. You can [supplement and modify the properties](https://devnet.logianalytics.com/hc/en-us/articles/5735528222487-How-Designer-Gets-Data-from-XML-Data-Sources#SupplementInfo).

   ![XML Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/9898533511831/xmlcnnctn_modify.gif)
8. Select **Next**. Designer displays the **Transform XML Schema** screen. Select an XPath to be the transforming start point.

   ![XML Connection Wizard - Transform XML Schema](https://devnet.logianalytics.com/hc/article_attachments/9898517019415/xmlcnnctn_trnsfrm.gif)
9. Select **Next**. Designer displays
   the **Transformed Relational Schema** screen, showing the relational schema structure it transforms from the XML schema.

   ![XML Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/9898517039255/xmlcnnctn_rltnal.gif)
10. Select **Next**. Designer displays the **Add Table** screen.

    ![XML Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/9898533541143/xmlcnnctn_add.gif)
11. The **Tables** box lists the tables Designer transforms from the schema. A table contains fields mapped to attributes, simple elements, content of complex elements, and other nodes in the XML data source. Select the tables you want to use in the connection and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add them to the **Added Tables** box. Clear **Generate the default pre-join path** if you do not want to generate default pre-join paths for the tables.
    You can create [queries](https://devnet.logianalytics.com/hc/en-us/articles/5735547120407-Working-with-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/5735547021975-Working-with-Business-Views) using these tables and then develop reports based on the queries and business views.
12. Select **Finish** to complete the transformation process.

## Adding More Tables to an XML Connection

After you have set up an XML connection in a catalog, you can add more tables transformed from the XML data source into the catalog via the connection.

1. Do one of the following:
   * Right-click the XML connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the XML connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the XML connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the XML connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the XML connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   Designer displays the [Add Tables dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735521826967-Add-Tables-Dialog-Box).

   ![Add Tables dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898533418263/addtbl_xml.gif)
2. Select **Refresh**.
3. Designer lists the tables contained in the schema that it transforms from the XML file in the **Tables** box. Choose the required tables and select **Add**.
4. Select **Done** to finish adding the tables and close the dialog box.

## Managing Tables in an XML Connection

For the tables you have transformed from an XML data source and added into a catalog via an XML connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/5735521508887-Using-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/5735521508887-Using-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/5735521508887-Using-Tables-Views-Synonyms#Remove) the same as you do with tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735528222487-How-Designer-Gets-Data-from-XML-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735528205847-Accessing-Data-via-SOAP-Web-Service-Connections)
