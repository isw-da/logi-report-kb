---
title: "RESTful Data Source Options Dialog Box"
id: 12480188883597
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480188883597-RESTful-Data-Source-Options-Dialog-Box
updated_at: 2026-02-25T23:48:51Z
source_host: docs-report.zendesk.com
---
# 
RESTful Data Source Options Dialog Box

You can use the RESTful Data Source Options dialog box to edit the RESTful options for a JSON data source or XML data source. This topic describes the options in the dialog box.
    

Designer displays the RESTful Data Source Options dialog box when you select RESTful in the Extract JSON Schema screen of the JSON Connection Wizard dialog box, or in the Import XML Schema screen of the XML Connection Wizard dialog box.

Designer displays these options:

Via REST Web Service

Select to receive the remote data via REST Web Service on the application server; otherwise, Designer receives the remote data via the protocol in the URL specified in the connection wizard.

MIME Type

Designer enables this option when you select Via REST Web Service. You can use it to select the MIME type for the REST Web Service data source from the drop-down list or specify the type in the text box manually.

User Name

Specify the user name for remote data authentication.

Password

Specify the password for remote data authentication.

HTTP Advanced Options

Select to show/hide the advanced HTTP protocol options.

- 
Method
Select the HTTP method using which to send the request, GET or POST.

- 
Headers
You can specify the user-defined HTTP headers in this box.
    
- 
New parameter button
Select to open the New Parameter dialog box to create a parameter in the current catalog data source and reference it in the HTTP header or body to dynamically compose the HTTP information.

- 
Add button
Select to add a new HTTP header.

- 
Remove button
Select to remove the specified HTTP headers.

- 
Name
This column shows the names that you specify for the HTTP headers. Double-click in the cell to edit the name.

- 
Value
This column shows the values that you specify for the HTTP header. Double-click in the cell to edit the value. You can reference parameters, constant level formulas, and the User Name special field.

- 
Body
You can specify the user-defined HTTP body in this box. You can also reference parameters, constant level formulas, and the User Name  special field in the body.

- 
Edit Format
Select to open the Edit Format dialog box to specify the value formats for the parameters and formulas that you reference in the HTTP headers and body.
    
- 
Name
This column shows the names of the parameters and formulas.

- 
Format
This column shows the value formats that you specify for the parameters and formulas.

- 
OK
Select to apply your settings and close the dialog box.

- 
Cancel
Select to close the dialog box without saving any changes.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
