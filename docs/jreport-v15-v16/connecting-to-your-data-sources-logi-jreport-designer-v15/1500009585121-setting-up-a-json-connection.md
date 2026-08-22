---
title: "Setting Up a JSON Connection"
id: 1500009585121
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585121-Setting-Up-a-JSON-Connection
updated_at: 2021-07-24T05:55:46Z
---

# Setting Up a JSON Connection

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585141-Transforming-a-JSON-Schema-to-a-Relational-Schema)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564342-Web-Service-Data-Sources)

# Setting Up a JSON Connection

To set up a JSON connection to connect a Logi JReport catalog to a JSON data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog).
2. In the Catalog Manager, right-click the node of a data source and choose **New JSON Connection** from the shortcut menu.  

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **JSON** connection type and select **OK**.

   The [JSON Connection Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009587721-JSON-Connection-Wizard-Dialog) appears.

   ![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/4404889332119/jsoncnctn_extrt.gif)
3. In the Extract JSON Schema screen, select the schema source: [Extract Schema from Sample Data](#Sample) or [Extract Schema from Instance Data](#Instance).
4. Provide the required information for extracting the JSON schema.
   * When Extract Schema from Sample Data is selected from the Schema Source drop-down list,
     1. In the Sample Data text field, input the URI string of the sample data file or select **Browse** to select the file.

        In the URI string, you can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590021-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels#CLF) in the current catalog data source and the special field User Name in the format "@fieldname". For example, if a URI string is `http://localhost:8080/rest/getData?startDate=2016-01-01`, and you want to use the parameters pHost, pPort and pStartDate to dynamically generate the URI at runtime, then the URI string will be `http://@pHost:@pPort/rest/getData?startDate=@pStartDate`. Moreover, if a URI string contains characters, such as @, '.' or double quotation marks, or other strings that do not need to be parsed, quote them with double quotation marks. If needed, you can select **New Parameter** to create a parameter in the current catalog data source and reference it in the URI string. If the special field User Name is used, when selecting Next in the connection wizard, the Security Identifier dialog will pop up for you to specify the user name with which to generate the stream. When you run the report on Logi JReport Server the real user's ID will be used.
     2. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the RESTful options for the sample data in the [RESTful Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009588461-RESTful-Data-Source-Options-Dialog) dialog.

        ![RESTful Data Source Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893858199/rstdtsrc.gif)
     3. To receive the remote data via REST web service, check **Via REST Web Service**, then from the MIME Type drop-down list, select the MIME type for the REST web service data source. You can also input the type in the text field directly. The remote data will then be provided by the REST web services on the application server, and the REST web service client API (such as JAX-RS client API of Java EE) will be used to get the remote data.

        When Via REST Web Service is unchecked, the remote data will be received via the protocol in the URL you specify in the Sample Data text field in the connection wizard.
     4. Input the user name and password for remote data authentication.
     5. Select **HTTP Advanced Options** to specify the advanced HTTP options.
     6. Select an HTTP method from the Method drop-down list to send the request, which can be GET or POST.
     7. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) above the Headers box to add a header line, then specify the name and value of the user defined HTTP header. Repeat this to edit more headers.
     8. In the Body box, specify the user defined HTTP body.
     9. When editing the HTTP headers and body, you can reference parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname". If needed, you can select ![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/4404893858455/btn_nwparam.gif) to create a parameter in the current catalog data source and reference it in the header or body. When parameters and formulas are referenced, you can select the **Edit Format** button to edit the format of their values.
     10. Select **OK** to apply the specified RESTful data source options and return to the JSON Connection Wizard.
     11. Specify how to get the instance data.

         To use instance data from a URI, check the **URI** radio button, then input the URI string directly in the Instance text field or select **Browse** to select the instance file. You can also reference parameters, constant level formulas and the special field User Name in the URI string. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the [RESTful options](#RESTful) for the instance data.

         To use instance data from a user defined interface, check **User Defined**, then provide the class name with package name in the Class Name field. You can also select **Browse** to find the class file. The class you enter should exist and can be found by Logi JReport Designer, which means the class should be in the class path of the system environment or in the ADDCLASSPATH in setenv.bat/setenv.sh. After filling in this field, the class name of the interface that the class implements will be displayed automatically behind The class implements:. Then specify the parameter string for the user defined interface in the Parameter box. The parameter string must match the format defined in the class. You can also reference parameters, constant level formulas, and the special field User Name in the parameter string.
   * When Extract Schema from Instance Data is selected from the Schema Source drop-down list, input the URI string of the instance file directly in the Schema Name text field or select **Browse** to select it. In the URI string, you can reference parameters, constant level formulas and the special field User Name. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the [RESTful options](#RESTful) for the instance data.
5. When parameters and formulas are referenced in the URI/parameter string, select the **Edit Format** button to edit the format of their values if needed.
6. Select **Next** to go to the next screen.
7. In the Modify Schema Properties screen, the elements in the JSON schema are listed in the Schema box. Select an element and modify its properties in the Properties box as required and then select **Next**.

   ![JSON Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404893869975/jsoncnctn_mdfy.gif)
8. In the Transformed Relational Schema screen, check the transformed result listed in the Transformed Tables box, and then select **Next**.

   ![JSON Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404889332375/jsoncnctn_trnsfrmd.gif)
9. In the Add Table screen, add the required tables to the connection.

   ![JSON Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404893870231/jsoncnctn_adtbl.gif)
10. Select **Finish** to confirm the transformed result and complete the transformation process.

When a JSON connection is set up, you can manage the tables transformed from the JSON data source the same as you do with tables from an XML data source. For example, you can add more tables via the JSON connection into the Logi JReport catalog, remove undesired table columns, organizing the tables into folder and refreshing the tables. For details, see [Managing Tables in an XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009585461-Managing-Tables-in-an-XML-Connection).

## Example of connecting a Logi JReport catalog data source to Google Cloud BigQuery

In the following example, we will set up a JSON connection to connect a Logi JReport catalog data source to Google Cloud BigQuery. In this example, we will create two parameters in the Logi JReport catalog and use them to provide values for the two tokens access\_token and maxResults in the URL of the JSON instance file used to access Google Cloud BigQuery. The token access\_token is for authorizing a Google API request, and maxResults represents the maximum record number to return. You can change the parameter values to provide dynamic values for the two tokens at runtime.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. Right-click the **Parameters** node in Data Source 1 of the catalog and select **New Parameter** from the shortcut menu.
3. In the New Parameter dialog, input **pAccessToken** in the Name field.
4. Select **String** from the Value Type drop-down list.
5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a value line, double-click in it and then type in the valid token value to access Google Cloud BigQuery, for example, ya29.Ci9dA2sA8J\_wM8e5FnY9rJg551153GQWGbleO-y9aeZOky9V36Tz497HY1chApjLFg.
6. Select **OK** to create the parameter.

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893966103/cnctn_json_stup1.gif)
7. Repeat the above steps to create another parameter pMaxResults of Integer type with the prompt value 2 in the Value List.

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893966359/cnctn_json_stup2.gif)

   For more information about creating parameters, see [Creating a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter).
8. Right-click the **Data Source 1** node and select **New JSON Connection** from the shortcut menu. The JSON Connection Wizard appears.
9. In the Extract JSON Schema screen, select **Extract Schema from Instance Data** from the Schema Source drop-down list.
10. Input the following URL in the Instance text box:

    `https://www.googleapis.com/bigquery/v2/projects/bigquery-public-data/datasets/samples/tables/gsod/data?maxResults=@pMaxResults&access_token=@pAccessToken`

    ![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/4404893966615/cnctn_json_stup3.gif)
11. Select **Next** three times to go to the Add Table screen. Select **f** in the Tables box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Added Tables box.
12. Select **Finish** to set up the connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585141-Transforming-a-JSON-Schema-to-a-Relational-Schema)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564342-Web-Service-Data-Sources)
