---
title: "Working with JSON Connections in a Catalog"
id: 1500010057762
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057762-Working-with-JSON-Connections-in-a-Catalog
updated_at: 2021-07-23T19:14:56Z
---

# Working with JSON Connections in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057742-How-Designer-Gets-Data-from-JSON-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057722-Example-Connecting-to-Google-Cloud-BigQuery-via-a-JSON-Connection)

# Working with JSON Connections in a Catalog

This topic describes how you can set up JSON connections in a catalog, and add and manage tables transformed from JSON data sources in the catalog via the connections.

This topic contains the following sections:

* [Setting Up JSON Connections in a Catalog](#Set)
  + [Configuring Proxy for Connecting to a REST Web Service](#Proxy)
* [Adding More Tables to a JSON Connection](#Add)
* [Managing the Tables in a JSON Connection](#Manage)

## Setting Up JSON Connections in a Catalog

To set up a JSON connection to connect a catalog to a JSON data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **New JSON Connection** from the shortcut menu.  

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **JSON** connection type and select **OK**.

   Designer displays the [JSON Connection Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097801-JSON-Connection-Wizard-Dialog-Box).

   ![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/4404848514839/jsoncnctn_extrt.gif)
3. In the **Extract JSON Schema** screen, select the schema source from the **Schema Source** drop-down list: [Extract Schema from Sample Data](#Sample) or [Extract Schema from Instance Data](#Instance).
4. Provide the required information for extracting the JSON schema.
   * When you select the schema source as **Extract Schema from Sample Data**,
     1. In the **Sample Data** text box, type the URI string of the sample data file or select **Browse** to select the file.

        In the URI string, you can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010099721-Working-with-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010061022-Formula-Levels#CLF) in the current catalog data source in the format *@FieldName*, and the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields#UserName)" as *@username*. For example, if a URI string is `http://localhost:8080/rest/getData?startDate=2016-01-01`, and you want to use the parameters pHost, pPort, and pStartDate to dynamically generate the URI at runtime, then the URI string is `http://@pHost:@pPort/rest/getData?startDate=@pStartDate`. Moreover, if a URI string contains characters, such as @, '.', or double quotation marks, or other strings that do not need to be parsed, quote them with double quotation marks. You can select **New Parameter** to create a parameter in the current catalog data source and reference it in the URI string. If you use the special field "User Name", when selecting Next in the connection wizard, Designer displays the Security Identifier dialog box for you to specify the user name with which to generate the stream. When end users run the report on Server, Server applies the login user's ID.
     2. When the specified URI string begins with the "http://" or "https://" protocol, Designer enables the **RESTful** button. Select the button to specify the RESTful options for the sample data in the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098501-RESTful-Data-Source-Options-Dialog-Box).

        ![RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856898199/rstdtsrc.gif)
     3. To receive the remote data via REST Web Service on the application server, select **Via REST Web Service**, then from the **MIME Type** drop-down list, select the MIME type for the REST Web Service data source. You can also specify the type in the text box manually. The REST Web Service Client API (such as the JAX-RS Client API of Java EE) will then be used to get the remote data. When you use a proxy to connect to the REST Web Service, you need to [configure the proxy parameters](#Proxy) in Designer so that the proxy can work successfully.

        If you do no select Via REST Web Service, Designer receives the remote data via the protocol in the URL you specify in the **Sample Data** text box in the connection wizard.
     4. Specify the user name and password for remote data authentication.
     5. Select **HTTP Advanced Options** to specify the advanced HTTP options.
     6. Select an HTTP method from the **Method** drop-down list to send the request, which can be GET or POST.
     7. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) above the **Headers** box to add a header line, then specify the name and value of the user-defined HTTP header. Repeat this to edit more headers. To delete an unwanted header, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).
     8. In the **Body** box, specify the user-defined HTTP body.
     9. When editing the HTTP headers and body, you can reference parameters and constant level formulas predefined in the current catalog data source, as well as the special field "User Name". Select ![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/4404856898455/btn_nwparam.gif) to create a parameter and reference it in the header or body, if the predefined parameters cannot meet your requirements.
     10. If you reference parameters and formulas in the HTTP headers and body, you can select the **Edit Format** button to edit the format of their values.
     11. Select **OK** to apply the specified RESTful data source options and return to the JSON Connection Wizard.
     12. Specify how to get the instance data.

         To use instance data from a URI, select the **URI** radio button, then type the URI string in the **Instance** text box or select **Browse** to select the instance file. You can also reference parameters, constant level formulas, and the special field "User Name" in the URI string. When the specified URI string begins with the "http://" or "https://" protocol, Designer enables the **RESTful** button. Select the button to specify the [RESTful options](#RESTful) for the instance data.

         To use instance data from a user-defined interface, select **User Defined**, then provide the class name with package name in the **Class Name** text box. You can also select **Browse** to find the class file. The class you specify should exist and can be found by Designer, which means the class should be in the class path of the system environment or in the ADDCLASSPATH in **setenv.bat**/**setenv.sh**. After you fill in this text box, Designer automatically displays the class name of the interface that the class implements behind "The class implements:". Specify the parameter string for the user-defined interface in the **Parameter** box. The parameter string must match the format defined in the class. You can also reference parameters, constant level formulas, and the special field "User Name" in the parameter string.
   * When you select the schema source as **Extract Schema from Instance Data**, type the URI string of the instance file in the **Instance** text box or select **Browse** to select the file. In the URI string, you can reference parameters, constant level formulas, and the special field "User Name". When the specified URI string begins with `http://` or `https://` protocol, Designer enables the **RESTful** button. Select the button to specify the [RESTful options](#RESTful) for the instance data.

     ![Extract Schema from Instance Data](https://devnet.logianalytics.com/hc/article_attachments/4404848651671/cnctn_json_work.gif)
5. When you reference parameters and formulas in the URI/parameter string, you can select the **Edit Format** button to edit the format of their values.
6. Select **Next** to go to the next screen.
7. In the **Modify Schema Properties** screen, Designer lists the elements in the JSON schema in the **Schema** box. Select an element and modify its properties in the **Properties** box, then select **Next**.

   ![JSON Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404848515223/jsoncnctn_mdfy.gif)
8. In the **Transformed Relational Schema** screen, Designer lists the relational tables built based on the transformed relational schema structure. Check the transformed result in the **Transformed Tables** box, and then select **Next**.

   ![JSON Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404848515479/jsoncnctn_trnsfrmd.gif)
9. In the **Add Table** screen, add the required tables to the connection.

   ![JSON Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404856915863/jsoncnctn_adtbl.gif)

   You can create [queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010062562-Working-with-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views) using these tables and a report is developed from a query (or something else which is functionally similar) or from a business view.
10. Select **Finish** to confirm the transformed result and complete the transformation process.

### Configuring Proxy for Connecting to a REST Web Service

In a restricted network when a proxy is used for connecting to a REST Web Service as the data source, you can set the proxy parameters in a configuration file in Designer so as for the proxy to work successfully. You need manually create the configuration file in XML named "restdsproxy.xml" in the directory `<install_root>\bin`.

The following is an example of the configuration file and the detailed description of each tag in the file:

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
  The root tag that contains one or more <proxymapping> sub-tags.
* **proxymapping**  
  Represents the whole set of parameters of a proxy. It contains the following sub-tags each defining a specific proxy parameter.
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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) The <user> and <password> information is encrypted, and replaced by the <encrypt-sign> tag after Designer starts up as follows:

`<encrypt-sign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-sign>`

If you want to change the user or password, delete the <encrypt-sign> tag and then add the <user> and <password> tags inrestdsproxy.xml.

## Adding More Tables to a JSON Connection

After you have set up a JSON connection in a catalog, you can add more tables transformed from the JSON data source into the catalog via the JSON connection.

1. Do one of the following:
   * Right-click the JSON connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the JSON connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the JSON connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the JSON connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the JSON connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   Designer displays the [Add Tables dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095521-Add-Tables-Dialog-Box).

   ![Add Tables dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857014039/addtbl_xml.gif)
2. Select the **Refresh** button.
3. Designer displays the tables contained in the schema that it transforms from the JSON file in the **Tables** box. Choose the required tables and select **Add**.

   To choose consecutive tables, select the first table, press and hold down the **SHIFT** key, and then select the last table. To choose tables that are not consecutive, press and hold down **CTRL**, and then select each table.
4. After adding the required tables, select **Done** to close the dialog box.

## Managing the Tables in a JSON Connection

For the tables that have been transformed from a JSON data source and added into a catalog via a JSON connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Remove) the same as you do with tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057742-How-Designer-Gets-Data-from-JSON-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057722-Example-Connecting-to-Google-Cloud-BigQuery-via-a-JSON-Connection)
