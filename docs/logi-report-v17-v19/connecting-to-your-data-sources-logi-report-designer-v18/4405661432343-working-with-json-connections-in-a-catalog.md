---
title: "Working with JSON Connections in a Catalog"
id: 4405661432343
section: "Connecting to Your Data Sources - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661432343-Working-with-JSON-Connections-in-a-Catalog
updated_at: 2022-01-27T20:34:39Z
---

# Working with JSON Connections in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661430807-How-Designer-Gets-Data-from-JSON-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661429399-Example-Connecting-to-Google-Cloud-BigQuery-via-a-JSON-Connection)

# Working with JSON Connections in a Catalog

This topic describes how you can set up JSON connections in a catalog, and add and manage tables transformed from JSON data sources in the catalog via the connections.

This topic contains the following sections:

* [Setting Up JSON Connections in a Catalog](#Set)
  + [Configuring Proxy for Connecting to a REST Web Service](#Proxy)
* [Adding More Tables to a JSON Connection](#Add)
* [Managing Tables in a JSON Connection](#Manage)

## Setting Up JSON Connections in a Catalog

To set up a JSON connection to connect a catalog to a JSON data source, take the following steps:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **New JSON Connection** from the shortcut menu.  

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **JSON** connection type and select **OK**.

   Designer displays the [JSON Connection Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664526999-JSON-Connection-Wizard-Dialog-Box).

   ![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/4420542114199/jsoncnctn_extrt.gif)
3. In the **Extract JSON Schema** screen, select the schema source from the **Schema Source** drop-down list: [Extract Schema from Sample Data](#Sample) or [Extract Schema from Instance Data](#Instance).
4. Provide the required information for extracting the JSON schema.
   * When you select the schema source as **Extract Schema from Sample Data**
     1. In the **Sample Data** text box, type the URI string of the sample data file or select **Browse** to select the file.

        In the URI string, you can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/4405661800215-Working-with-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405664602263-Formula-Levels#CLF) in the current catalog data source in the format *@FieldName*, and the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields#UserName)" as *@username*. For example, if a URI string is `http://localhost:8080/rest/getData?startDate=2016-01-01`, and you want to use the parameters pHost, pPort, and pStartDate to dynamically generate the URI, then the URI string is `http://@pHost:@pPort/rest/getData?startDate=@pStartDate`. Moreover, if a URI string contains characters, such as "@", ":", and double quotation marks, or other strings that do not need to be parsed, you should quote them with double quotation marks. You can select **New Parameter** to create the parameter and reference it if the predefined parameters cannot meet your requirements. If you use the special field "User Name", when you select Next in the connection wizard, Designer displays the Security Identifier dialog box for you to specify the user name with which to generate the stream; when a user runs a report that uses data from the JSON data source at runtime, Server applies the user's ID.
     2. If the specified URI string begins with the "http://" or "https://" protocol, Designer enables the **RESTful** button. Select the button to specify RESTful options for the sample data in the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661694743-RESTful-Data-Source-Options-Dialog-Box).

        ![RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556130839/rstdtsrc.gif)
     3. To receive the remote data via REST Web Service on the application server, select **Via REST Web Service**, then from the **MIME Type** drop-down list, select the MIME type for the REST Web Service data source. You can also specify the type in the text box manually. The REST Web Service Client API (such as the JAX-RS Client API of Java EE) will then be used to get the remote data. When you use a proxy to connect to the REST Web Service, you need to [configure the proxy parameters](#Proxy) in Designer so that the proxy can work successfully.

        If you do no select Via REST Web Service, Designer receives the remote data via the protocol in the URL you specify in the **Sample Data** text box in the connection wizard.
     4. Specify the user name and password for remote data authentication.
     5. Select **HTTP Advanced Options** to specify the advanced HTTP options.
     6. Select an HTTP method from the **Method** drop-down list to send the request, which can be GET or POST.
     7. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) above the **Headers** box to add a header line, then specify the name and value of the user-defined HTTP header. Repeat this to edit more headers. To delete a header, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).
     8. In the **Body** box, specify the user-defined HTTP body.
     9. When editing the HTTP headers and body, you can reference parameters and constant level formulas predefined in the current catalog data source, and the special field "User Name". Select **New Parameter**![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/4420550865687/btn_nwparam.gif) to create a parameter and reference it in the header or body, if the predefined parameters cannot meet your requirements.
     10. If you reference parameters and formulas in the HTTP headers and body, you can select **Edit Format** to edit the format of their values.
     11. Select **OK** to apply the specified RESTful data source options and return to the JSON Connection Wizard.
     12. Specify how to get the instance data.

         To use instance data from a URI, select **URI**, then type the URI string in the **Instance** text box or select **Browse** to select the instance file. The instance should match the JSON schema that you have defined in the specified sample data file. You can also reference parameters, constant level formulas, and the special field "User Name" in the URI string. Select **RESTful** to specify [RESTful options](#RESTful) for the instance data, when you use a URI based on the "http://" or "https://" protocol.

         To use instance data from a user-defined interface, select **User Defined**, then provide the class name with package name in the **Class Name** text box. You can also select **Browse** to find the class file. The class you specify should exist and can be found by Designer, which means the class should be in the class path of the system environment or in the ADDCLASSPATH in **setenv.bat**/**setenv.sh**. After you fill in this text box, Designer automatically displays the class name of the interface that the class implements behind "The class implements:". Specify the parameter string for the user-defined interface in the **Parameter** box. The parameter string must match the format defined in the class. You can also reference parameters, constant level formulas, and the special field "User Name" in the parameter string.
   * When you select the schema source as **Extract Schema from Instance Data**, type the URI string of the instance file in the **Instance** text box or select **Browse** to select the file. In the URI string, you can reference parameters, constant level formulas, and the special field "User Name". When the specified URI string begins with the "http://" or "https://" protocol, Designer enables the **RESTful** button. Select the button to specify RESTful options for the instance data.

     ![Extract Schema from Instance Data](https://devnet.logianalytics.com/hc/article_attachments/4420556229399/cnctn_json_work.gif)
5. If you reference parameters and formulas in the URI/parameter string, you can select **Edit Format** to edit the format of their values.
6. Select **Next** to go to the next screen.
7. In the **Modify Schema Properties** screen, Designer lists the elements in the JSON schema in the **Schema** box. Select an element and modify its properties in the **Properties** box, then select **Next**.

   ![JSON Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4420550883735/jsoncnctn_mdfy.gif)
8. In the **Transformed Relational Schema** screen, Designer lists the relational tables built based on the transformed relational schema structure. Check the transformed result in the **Transformed Tables** box, and then select **Next**.

   ![JSON Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4420556151191/jsoncnctn_trnsfrmd.gif)
9. In the **Add Table** screen, add the required tables to the connection.

   ![JSON Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4420550883991/jsoncnctn_adtbl.gif)

   You can create [queries](https://devnet.logianalytics.com/hc/en-us/articles/4405661915543-Working-with-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/4405664680215-Working-with-Business-Views) using these tables and a report is developed from a query (or something else which is functionally similar) or from a business view.
10. Select **Finish** to confirm the transformed result and complete the transformation process.

### Configuring Proxy for Connecting to a REST Web Service

When you use proxy to connect to a REST Web Service as the data source in a restricted network, you can set the proxy parameters in a configuration file in Designer, so as for the proxy to work successfully. You need to manually create the configuration file in XML and name it **restdsproxy.xml** in the `<install_root>\bin` folder.

The following is an example of the configuration file and the detailed description of each tag in the file.

```
<?xml version="1.0" encoding="UTF-8"?>  
<restdsproxy>  
    <proxymapping>  
        <urlpattern>https://.*\.jinfonet\.com/</urlpattern>  
        <proxyhost>192.0.0.14</proxyhost>
        <proxyport>8888</proxyport>
        <user>user1</user>  
        <password>psw1</password>  
    </proxymapping>  
    <proxymapping>  
        <urlpattern>http://.*\.jinfonet\.com\.cn/</urlpattern>  
        <proxyhost>192.0.0.14</proxyhost>
        <proxyport>80</proxyport>
        <user>user2</user>  
        <password>psw2</password>  
    </proxymapping>  
</restdsproxy>
```

* **restdsproxy**  
  The root tag that contains one or more <proxymapping> subtags.
* **proxymapping**  
  The whole set of the parameters of a proxy. It contains the following subtags, with each defining a specific proxy parameter.
* **urlpattern**  
  A regular expression string supported by Java that matches the URL of a REST Web Service. If there are multiple URL patterns that match the same URL, the proxy setting in the <proxymapping> tag that contains the first one matched takes effect.
* **proxyhost**  
  The host name or IP address of the proxy.
* **proxyport**  
  The port number of the proxy.
* **user**  
  The user name used for the proxy authentication. It is optional.
* **password**  
  The password used for the proxy authentication. It is optional.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) The <user> and <password> information is encrypted, and replaced by the <encrypt-sign> tag after Designer starts up.

`<encrypt-sign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-sign>`

If you want to change the user or password, delete the <encrypt-sign> tag and then add the <user> and <password> tags in restdsproxy.xml.

## Adding More Tables to a JSON Connection

After you have set up a JSON connection in a catalog, you can add more tables transformed from the JSON data source into the catalog via the JSON connection.

**To add tables to a JSON connection**

1. Do one of the following:
   * Right-click the JSON connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the JSON connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the JSON connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the JSON connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the JSON connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   Designer displays the [Add Tables dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664425495-Add-Tables-Dialog-Box).

   ![Add Tables dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556223511/addtbl_xml.gif)
2. Select **Refresh**.
3. Designer displays the tables contained in the schema that it transforms from the JSON data source in the **Tables** box. Choose the required tables and select **Add**.
4. Select **Done** to close the dialog box.

## Managing Tables in a JSON Connection

For the tables that have been transformed from a JSON data source and added into a catalog via a JSON connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms#Remove) the same as you do with tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661430807-How-Designer-Gets-Data-from-JSON-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661429399-Example-Connecting-to-Google-Cloud-BigQuery-via-a-JSON-Connection)
