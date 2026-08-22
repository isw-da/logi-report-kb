---
title: "JSON Connections"
id: 1500010029482
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029482-JSON-Connections
updated_at: 2021-07-24T10:39:14Z
---

# JSON Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064381-Using-Data-Sources-via-OOJDBC) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064581-XML-Connections)

# JSON Connections

You can set up JSON connections in Logi JReport catalogs to get data from JSON data sources. A JSON connection contains relational data which is transformed from a JSON data source.

Below is a list of the sections covered in this topic:

* [Retrieving Data from JSON Data Sources](#How)
  + [Extracting Metadata from JSON Data](#Extract)
  + [Transforming JSON Schemas to Relational Schemas](#Transform)
* [Setting Up JSON Connections in a Catalog](#Set)
* [Adding More Tables to a JSON Connection](#Add)
* [Managing the Tables in a JSON Connection](#Manage)
* [Example: Connecting a Logi JReport Catalog to Google Cloud BigQuery](#Example)

## Retrieving Data from JSON Data Sources

Logi JReport Designer can parse JSON data to extract JSON schemas including JSON metadata (JSON objects and the relation between the objects), transform JSON schemas to relational schemas, and build relational tables during the transformation, namely map JSON object classes to tables and table columns, and build the relation between the primary and foreign keys in the tables. The tables can then be accessed in the same way as [JDBC supplied tables](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms).

### Extracting Metadata from JSON Data

A JSON metadata contains a root element whose element type can be object class or object array. An object class or object array element contains some elements whose element type can be object class, object array, attribute or simple data array with the data type of String, Number or Boolean. JSON objects in an array should have the same structure, the members (name/value pairs) in an object cannot be of the same name, and for a nested array, only the first layer will be kept.

**Extracting rules**

Logi JReport Designer takes the following rules to extract metadata from JSON data:

* Elements should be extracted from the root value of JSON data hierarchically.
* When creating the root element, the element name is null, and the root element type is object class or object array if the root value of JSON data is an object class or an object array, else the root element type is an empty object class.
* If the value of an object member is a simple value, an attribute element will be created under current element. If it is a simple value array, a simple data array element will be created. If it is an object array, an object array element will be created. If it is an object class, an object class element will be created. The element type will be set according to the conversion rules in the Data type conversion table below. The element name is the object member name.
* All elements of the same name in object members of an object array will be merged into an element.

**Data type conversion rules**

Before the data types defined in the JSON file can function with Logi JReport Designer, they should be converted into corresponding SQL data types when Logi JReport Designer extracts metadata from the JSON data, following the rules in the table below.

| JSON Data Type | SQL Data Type |
| --- | --- |
| String (following the format Combined date and time representations in ISO 8601) | TIMESTAMP |
| String (following JDBC Timestamp escape format) | TIMESTAMP |
| String (following the format Calendar dates in ISO 8601) | DATE |
| String (following the format Times with time zone designators in ISO 8601) | TIME |
| String | VARCHAR |
| Number (excluding fraction and exponent) | INTEGER |
| Number (including fraction and exponent) | NUMERIC |
| Boolean | BOOLEAN |

**Notes:**

* If the data type of all values for members of the same name in an object array is Number, including not only integer, but also fraction or exponent, the data type of all values will be converted to NUMERIC.
* If the values for members of the same name in an object array are of different data types and at least one of them is String, the data type of all values will be converted to VARCHAR.
* The values for the members of the same name in a JSON schema cannot be mixed with simple data array and single value, such as string, number,Boolean, or null, otherwise, the extracted schema maybe incorrect.

### Transforming JSON Schemas to Relational Schemas

When Logi JReport Designer transforms JSON schemas to relational schemas, elements in the JSON schemas are transformed to either tables or columns in tables according to the ideographic transformation rules and named according to the naming rules.

**Transformation rules**

Logi JReport Designer takes the following rules when transforming JSON schemas to relational schemas:

* If an object class or object array element has at least one attribute element or simple data array element, or its embedded element can be mapped to tables, the object class or object array element will be mapped to a table, and its attribute or simple data array element will be mapped to columns in the table.
* When mapping an attribute element to a column, the value of its Mapped SQL Type will be set as the value of the SQL Type of the column.
* For an embedded object class or object array element, a built-in column called foreign key will be created for the mapped table. If there is no built-in column called primary key in its parent element table, the column will be created. The SQL type of the columns primary key and foreign key is SQL type 4 (64 bit Integer).

**Naming rules**

The relational tables and columns in tables are named based on the following rules:

* For the root element, the table name is ROOT. If the name is not unique, the character \_ will be added before the name one by one until it is unique.
* For elements other than the root element, the table name is the element name. If the table name is not unique, the names of the ancestor elements will be added before the table name one by one and be separated by \_ until it is unique.

## Setting Up JSON Connections in a Catalog

To set up a JSON connection to connect a Logi JReport catalog to a JSON data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **New JSON Connection** from the shortcut menu.  

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **JSON** connection type and select **OK**.

   The [JSON Connection Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500010031582-JSON-Connection-Wizard-Dialog) appears.

   ![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/4404909175959/jsoncnctn_extrt.gif)
3. In the Extract JSON Schema screen, select the schema source: [Extract Schema from Sample Data](#Sample) or [Extract Schema from Instance Data](#Instance).
4. Provide the required information for extracting the JSON schema.
   * When Extract Schema from Sample Data is selected from the Schema Source drop-down list,
     1. In the Sample Data text box, input the URI string of the sample data file or select **Browse** to select the file.

        In the URI string, you can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010068961-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010068561-Formula-Levels#CLF) in the current catalog data source and the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010029242-Special-Fields#UserName) in the format *@fieldname*. For example, if a URI string is `http://localhost:8080/rest/getData?startDate=2016-01-01`, and you want to use the parameters pHost, pPort and pStartDate to dynamically generate the URI at runtime, then the URI string will be `http://@pHost:@pPort/rest/getData?startDate=@pStartDate`. Moreover, if a URI string contains characters, such as @, '.' or double quotation marks, or other strings that do not need to be parsed, quote them with double quotation marks. If needed, you can select **New Parameter** to create a parameter in the current catalog data source and reference it in the URI string. If the special field User Name is used, when selecting Next in the connection wizard, the Security Identifier dialog will pop up for you to specify the user name with which to generate the stream. When you run the report on Logi JReport Server the logon user's ID will be used.
     2. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the RESTful options for the sample data in the [RESTful Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010067641-RESTful-Data-Source-Options-Dialog) dialog.

        ![RESTful Data Source Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909158679/rstdtsrc.gif)
     3. To receive the remote data via REST Web Service, check **Via REST Web Service**, then from the MIME Type drop-down list, select the MIME type for the REST Web Service data source. You can also input the type in the text box directly. The remote data will then be provided by the REST Web Services on the application server, and the REST Web Service Client API (such as JAX-RS client API of Java EE) will be used to get the remote data.

        When Via REST Web Service is unchecked, the remote data will be received via the protocol in the URL you specify in the Sample Data text box in the connection wizard.
     4. Input the user name and password for remote data authentication.
     5. Select **HTTP Advanced Options** to specify the advanced HTTP options.
     6. Select an HTTP method from the Method drop-down list to send the request, which can be GET or POST.
     7. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) above the Headers box to add a header line, then specify the name and value of the user defined HTTP header. Repeat this to edit more headers.
     8. In the Body box, specify the user defined HTTP body.
     9. When editing the HTTP headers and body, you can reference parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname". If needed, you can select ![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/4404909158935/btn_nwparam.gif) to create a parameter in the current catalog data source and reference it in the header or body. When parameters and formulas are referenced, you can select the **Edit Format** button to edit the format of their values.
     10. select **OK** to apply the specified RESTful data source options and return to the JSON Connection Wizard.
     11. Specify how to get the instance data.

         To use instance data from a URI, check the **URI** radio button, then input the URI string directly in the Instance text box or select **Browse** to select the instance file. You can also reference parameters, constant level formulas and the special field User Name in the URI string. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the [RESTful options](#RESTful) for the instance data.

         To use instance data from a user defined interface, check **User Defined**, then provide the class name with package name in the Class Name field. You can also select **Browse** to find the class file. The class you enter should exist and can be found by Logi JReport Designer, which means the class should be in the class path of the system environment or in the ADDCLASSPATH in setenv.bat/setenv.sh. After filling in this field, the class name of the interface that the class implements will be displayed automatically behind "The class implements:". Then specify the parameter string for the user defined interface in the Parameter box. The parameter string must match the format defined in the class. You can also reference parameters, constant level formulas, and the special field User Name in the parameter string.
   * When Extract Schema from Instance Data is selected from the Schema Source drop-down list, input the URI string of the instance file in the Schema Name text box or select **Browse** to select it. In the URI string, you can reference parameters, constant level formulas and the special field User Name. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the [RESTful options](#RESTful) for the instance data.
5. When parameters and formulas are referenced in the URI/parameter string, select the **Edit Format** button to edit the format of their values if needed.
6. Select **Next** to go to the next screen.
7. In the Modify Schema Properties screen, the elements in the JSON schema are listed in the Schema box. Select an element and modify its properties in the Properties box as required and then select **Next**.

   ![JSON Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404901201303/jsoncnctn_mdfy.gif)
8. In the Transformed Relational Schema screen, the relational tables built based on the transformed relational schema structure are listed. Check the transformed result listed in the Transformed Tables box, and then select **Next**.

   ![JSON Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404909176215/jsoncnctn_trnsfrmd.gif)
9. In the Add Table screen, add the required tables to the connection.

   ![JSON Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404901201559/jsoncnctn_adtbl.gif)

   [Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010070681-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010070641-Business-Views) are created on tables and a report is developed from a query (or something else which is functionally similar) or from a business view.
10. Select **Finish** to confirm the transformed result and complete the transformation process.

## Adding More Tables to a JSON Connection

When a JSON connection is set up, you can add more tables transformed from the JSON data source into the Logi JReport catalog via the JSON connection.

1. Do one of the following:
   * Right-click the JSON connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the JSON connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the JSON connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the JSON connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the JSON connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   The [Add Tables](https://devnet.logianalytics.com/hc/en-us/articles/1500010029762-Add-Tables-Dialog) dialog appears.

   ![Add Tables dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901297047/addtbl_xml.gif)
2. Select the **Refresh** button. The tables contained in the schema that is transformed from the JSON file will then be displayed in the Tables box.
3. Choose the required tables in the Tables box, and then select **Add**.

   To choose consecutive tables, select the first table, press and hold down the **SHIFT** key, and then select the last table. To choose tables that are not consecutive, press and hold down **CTRL**, and then select each table.
4. After adding the required tables, select **Done** to close the dialog.

## Managing the Tables in a JSON Connection

For the tables that have been transformed from a JSON data source and added into a Logi JReport catalog via the specified JSON connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms#Remove) the same as you do on tables from a JDBC database.

## Example: Connecting a Logi JReport Catalog to Google Cloud BigQuery

In the following example, we will set up a JSON connection to connect a Logi JReport catalog data source to Google Cloud BigQuery. In this example, we will create two parameters in the Logi JReport catalog and use them to provide values for the two tokens access\_token and maxResults in the URL of the JSON instance file used to access Google Cloud BigQuery. The token access\_token is for authorizing a Google API request, and maxResults represents the maximum record number to return. You can change the parameter values to provide dynamic values for the two tokens at runtime.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Right-click the **Parameters** node in Data Source 1 of the catalog and select **New Parameter** from the shortcut menu.
3. In the New Parameter dialog, input **pAccessToken** in the Name field.
4. Select **String** from the Value Type drop-down list.
5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) to add a value line, double-click in it and then type in the valid token value to access Google Cloud BigQuery, for example, ya29.Ci9dA2sA8J\_wM8e5FnY9rJg551153GQWGbleO-y9aeZOky9V36Tz497HY1chApjLFg.
6. Select **OK** to create the parameter.

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909261975/cnctn_json_stup1.gif)
7. Repeat the above steps to create another parameter pMaxResults of Integer type with the prompt value 2 in the Value List.

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909262231/cnctn_json_stup2.gif)

   For more information about creating parameters, see [Creating a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog).
8. Right-click the **Data Source 1** node and select **New JSON Connection** from the shortcut menu. The JSON Connection Wizard appears.
9. In the Extract JSON Schema screen, select **Extract Schema from Instance Data** from the Schema Source drop-down list.
10. Input the following URL in the Instance text box:

    `https://www.googleapis.com/bigquery/v2/projects/bigquery-public-data/datasets/samples/tables/gsod/data?maxResults=@pMaxResults&access_token=@pAccessToken`

    ![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/4404901306135/cnctn_json_stup3.gif)
11. Select **Next** three times to go to the Add Table screen. Select **f** in the Tables box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) to add it to the Added Tables box.
12. Select **Finish** to set up the connection.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064381-Using-Data-Sources-via-OOJDBC) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064581-XML-Connections)
