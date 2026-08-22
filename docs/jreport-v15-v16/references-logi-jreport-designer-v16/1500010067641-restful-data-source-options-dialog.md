---
title: "RESTful Data Source Options Dialog"
id: 1500010067641
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067641-RESTful-Data-Source-Options-Dialog
updated_at: 2021-07-24T10:38:27Z
---

# RESTful Data Source Options Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032282-Reset-All-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032342-RTF-Option-Dialog)

# RESTful Data Source Options Dialog

The RESTful Data Source Options dialog helps you to edit the RESTful options for a [JSON data source](https://devnet.logianalytics.com/hc/en-us/articles/1500010029482-JSON-Connections#RESTful) or [XML data source](https://devnet.logianalytics.com/hc/en-us/articles/1500010064601-Working-with-XML-Connections-in-a-Catalog#RESTful). It appears when you select the RESTful button in the [Extract JSON Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500010031582-JSON-Connection-Wizard-Dialog#Extract) screen of the JSON Connection Wizard, or the [Import XML Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500010033042-XML-Connection-Wizard-Dialog#Import) screen of the XML Connection Wizard.

![RESTful Data Source Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909158679/rstdtsrc.gif)

The following are details about options in the dialog:

**Via REST Web Service**

Specifies whether or not to receive remote data via REST Web Service.

If not, remote data is received via the protocol in the URL specified in the connection wizard.

If true, the remote data is provided by REST Web Services on the application server. Logi JReport Engine will use the REST Web Service Client API (such as the JAX-RS client API of Java EE) to get remote data from REST Web Services on the application server and the URL, the HTTP method (GET, POST etc.), MIME type and so on need to be specified to setup the connection. Generally only the HTTP.GET method can be used to get remote data.

**MIME Type**

Specifies the MIME type for the REST Web Service data source. Select the type from the drop-down list or input the type in the text box. Available only when Via REST Web Service is checked.

**User Name**

Specifies the user name for remote data authentication.

**Password**

Specifies the password for remote data authentication.

**HTTP Advanced Options**

Select to show/hide the advanced options for the HTTP protocol.

* **Method**  
   Specifies the HTTP method used to send the request, which can be GET or POST.
* **Headers**  
   Specifies the user defined HTTP headers.
  + ![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/4404909158935/btn_nwparam.gif)  
     Opens the [New Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010067241-New-Parameter-Dialog) dialog to create a parameter in the current catalog data source and reference it in the HTTP header or body to dynamically compose the HTTP information.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
     Adds a new HTTP header.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
     Removes the selected HTTP headers.
  + **Name**  
     Specifies the name of the HTTP header. double-click in the line to edit the name.
  + **Value**  
     Specifies the value of the HTTP header. double-click in the line to edit the value. You can reference parameters and constant level formulas in the current catalog data source or the special field User Name in the format "@fieldname".
* **Body**  
   Specifies the user defined HTTP body. You can also reference parameters, constant level formulas and the special field User Name in the body.
* **Edit Format**  
   Opens the Edit Format dialog to specify the value formats of the parameters and formulas referenced in the HTTP headers and body.
  + **Name**  
     Displays names of the parameters and formulas.
  + **Format**  
     Specifies the value formats of the parameters and formulas.
  + **OK**  
     Accepts changes and closes the dialog.
  + **Cancel**  
     Does not retain changes and closes the dialog.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032282-Reset-All-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032342-RTF-Option-Dialog)
