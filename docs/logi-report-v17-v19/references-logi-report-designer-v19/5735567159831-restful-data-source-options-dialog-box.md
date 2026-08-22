---
title: "RESTful Data Source Options Dialog Box"
id: 5735567159831
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735567159831-RESTful-Data-Source-Options-Dialog-Box
updated_at: 2022-11-02T04:40:14Z
---

# RESTful Data Source Options Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735544182423-Reset-All-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515297943-RTF-Option-Dialog-Box)

# RESTful Data Source Options Dialog Box

You can use the RESTful Data Source Options dialog box to edit the RESTful options for a [JSON data source](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog#RESTful) or [XML data source](https://devnet.logianalytics.com/hc/en-us/articles/5735499628183-Working-with-XML-Connections-in-a-Catalog#RESTful). This topic describes the options in the dialog box.

Designer displays the RESTful Data Source Options dialog box when you select RESTful in the [Extract JSON Schema](https://devnet.logianalytics.com/hc/en-us/articles/5735566628631-JSON-Connection-Wizard-Dialog-Box#Extract) screen of the JSON Connection Wizard dialog box, or in the [Import XML Schema](https://devnet.logianalytics.com/hc/en-us/articles/5735544859287-XML-Connection-Wizard-Dialog-Box#Import) screen of the XML Connection Wizard dialog box.

![RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898478146839/rstdtsrc.gif)

Designer displays these options:

**Via REST Web Service**

Select to receive the remote data via REST Web Service on the application server; otherwise, Designer receives the remote data via the protocol in the URL specified in the connection wizard.

**MIME Type**

Designer enables this option when you select Via REST Web Service. You can use it to select the MIME type for the REST Web Service data source from the drop-down list or specify the type in the text box manually.

**User Name**

Specify the user name for remote data authentication.

**Password**

Specify the password for remote data authentication.

**HTTP Advanced Options**

Select to show/hide the advanced HTTP protocol options.

* **Method**  
  Select the HTTP method using which to send the request, GET or POST.
* **Headers**  
  You can specify the user-defined HTTP headers in this box.
  + ![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/9898478152855/btn_nwparam.gif)**New parameter button**  
    Select to open the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box) to create a parameter in the current catalog data source and reference it in the HTTP header or body to dynamically compose the HTTP information.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**  
    Select to add a new HTTP header.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
    Select to remove the specified HTTP headers.
  + **Name**  
    This column shows the names that you specify for the HTTP headers. Double-click in the cell to edit the name.
  + **Value**  
    This column shows the values that you specify for the HTTP header. Double-click in the cell to edit the value. You can reference parameters, constant level formulas, and the special field "User Name".
* **Body**  
  You can specify the user-defined HTTP body in this box. You can also reference parameters, constant level formulas, and the special field "User Name" in the body.
* **Edit Format**  
  Select to open the Edit Format dialog box to specify the value formats for the parameters and formulas that you reference in the HTTP headers and body.
  + **Name**  
    This column shows the names of the parameters and formulas.
  + **Format**  
    This column shows the value formats that you specify for the parameters and formulas.
  + **OK**  
    Select to apply your settings and close the dialog box.
  + **Cancel**  
    Select to close the dialog box without saving any changes.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735544182423-Reset-All-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515297943-RTF-Option-Dialog-Box)
