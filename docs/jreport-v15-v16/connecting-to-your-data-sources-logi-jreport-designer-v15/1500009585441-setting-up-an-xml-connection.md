---
title: "Setting Up an XML Connection"
id: 1500009585441
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585441-Setting-Up-an-XML-Connection
updated_at: 2021-07-24T05:55:41Z
---

# Setting Up an XML Connection

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564402-Transforming-an-XML-Schema-to-a-Relational-Schema)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585461-Managing-Tables-in-an-XML-Connection)

# Setting Up an XML Connection

This topic demonstrates how to set up an XML Connection.

To set up an XML connection to connect a Logi JReport catalog to an XML data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog).
2. In the Catalog Manager, right-click the node of a data source and choose **Add XML Connection** from the shortcut menu.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **XML** connection type and select **OK**.

   The [XML Connection Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009567962-XML-Connection-Wizard-Dialog) appears.

   ![XML Connection Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404893844247/xmlcnnctn_import.gif)
3. In the Import XML Schema screen, specify [the way to import the XML schema](https://devnet.logianalytics.com/hc/en-us/articles/1500009564382-Importing-an-XML-Schema) from the Schema Type drop-down list: Import from XSD or Parse from XML Instance.
4. Provide the required information for importing the XML schema.
   * When Import from XSD is selected from the Schema Type drop-down list,
     1. In the Schema Name text field, input the URI string of the schema file or select **Browse** to select the file.

        In the URI string, you can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590021-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels#CLF) in the current catalog data source and the special field User Name in the format "@fieldname". For example, if a URI string is `http://localhost:8080/rest/getData?startDate=2016-01-01`, and you want to use the parameters pHost, pPort and pStartDate to dynamically generate the URI at runtime, then the URI string will be `http://@pHost:@pPort/rest/getData?startDate=@pStartDate`. Moreover, if a URI string contains characters, such as @, '.' or double quotation marks, or other strings that do not need to be parsed, quote them with double quotation marks. If needed, you can select **New Parameter** to create a parameter in the current catalog data source and reference it in the URI string. If the special field User Name is used, when selecting Next in the connection wizard, the Security Identifier dialog will pop up for you to specify the user name with which to generate the stream in Designer. When run on Logi JReport Server, the real user's ID will be used.
     2. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the RESTful options for the schema file in the [RESTful Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009588461-RESTful-Data-Source-Options-Dialog) dialog.

        ![RESTful Data Source Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893858199/rstdtsrc.gif)
     3. To receive the remote data via REST web service, check **Via REST Web Service**, then from the MIME Type drop-down list, select the MIME type for the REST web service data source. You can also input the type in text field directly. The remote data will then be provided by the REST web services on the application server, and the REST web service client API (such as JAX-RS client API of Java EE) will be used to get the remote data.

        When Via REST Web Service is unchecked, the remote data will be received via the protocol in the URL you specify in the Schema Name text field in the connection wizard.
     4. Input the user name and password for remote data authentication.
     5. Select **HTTP Advanced Options** to specify the advanced HTTP options.
     6. Select an HTTP method from the Method drop-down list to send the request, which can be GET or POST.
     7. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) above the Headers box to add a header line, then specify the name and value of the user defined HTTP header. Repeat this to edit more headers.
     8. In the Body box, specify the user defined HTTP body.
     9. When editing the HTTP headers and body, you can reference the parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname". If needed, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893858455/btn_nwparam.gif) to create a parameter in the current catalog data source and reference it in the header or body. When parameters and formulas are referenced, you can select the **Edit Format** button to edit the format of their values.
     10. Select **OK** to apply the specified RESTful data source options and return to the XML Connection Wizard.
     11. From the Starting Node drop-down list, specify the starting node accordingly.
     12. Specify the XML instance file.

         To use an instance file from URI, check the **URI** radio button, then input the URI string directly in the Instance text field or select **Browse** to select the instance file. You can also reference parameters, constant level formulas and the special field User Name in the URI string. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the [RESTful options](#RESTful) for the instance data.

         To use an instance file from a user defined interface, check **User Defined**, then provide the class name with package name in the Class Name field. You can also select **Browse** to find the class file. The class you enter must exist and can be found by Logi JReport Designer and Logi JReport Server at runtime, which means the class should be in the class path of the system environment. After filling in this field, the class name of the interface that the class implements will be displayed automatically behind The class implements:. Then specify the parameter string for the user defined interface in the Parameter box. The parameter string must match the format defined in the class. You can also reference parameters, constant level formulas, and the special field User Name in the parameter string.
     13. Check the **Validate with schema before fetching** to validate whether or not values in the XML instance are valid according to the W3C standard and the selected XSD schema.


     **Notes:**

     + If a value of DateTime data type is accurate to millisecond, a message - Invalid Value will still pop-up although the value is valid according to the W3C standard. You can ignore the error message and continue the transformation steps.
     + If you use a parameter to dynamically specify an XML instance at runtime, the XML instance will be validated at runtime rather than in the importing process.
   * When Parse from XML Instance is selected from the Schema Type drop-down list, input the URI string of the XML instance directly in the Schema Name text field or select **Browse** to select it. In the URI string, you can reference parameters, constant level formulas and the special field User Name. When the specified URI string begins with `http://` or `https://` protocol, the RESTful button is activated. Select it to specify the [RESTful options](#RESTful) for the instance data.
5. Select the **Time Zone and Locale** button to specify the time zone and the locale for the XML instance in the [Time Zone and Locale Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009567782-Time-Zone-and-Locale-Options-Dialog) dialog.
6. When parameters and formulas are referenced in the URI/parameter string, select the **Edit Format** button to edit the format of their values if needed.
7. Select **Next** to go to the next screen.
8. In the Modify Schema Properties screen, [supplement and modify the element properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009564382-Importing-an-XML-Schema#XMLSchema) as required and then select **Next**.

   ![XML Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404893844503/xmlcnnctn_modify.gif)
9. In the Transform XML Schema screen, select an XPath to be the transforming start point. Select **Next**.

   ![XML Connection Wizard - Transform XML Schema](https://devnet.logianalytics.com/hc/article_attachments/4404889311895/xmlcnnctn_trnsfrm.gif)
10. In the Transformed Relational Schema screen, check the transformed result, and then select **Next**.

    ![XML Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404889312151/xmlcnnctn_trnsfrmd.gif)
11. In the Add Table screen, add the required tables to the connection, and check the **Generate the default pre-join path** checkbox for generating default pre-join paths for tables of the XML data source.

    ![XML Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404893845015/xmlcnnctn_add.gif)
12. Select **Finish** to confirm the transformed result and complete the transformation process.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564402-Transforming-an-XML-Schema-to-a-Relational-Schema)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585461-Managing-Tables-in-an-XML-Connection)
