---
title: "Edit Operation Calling Property Dialog Box"
id: 45190478107661
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190478107661-Edit-Operation-Calling-Property-Dialog-Box
updated_at: 2026-04-30T15:13:15Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Edit Operation Calling Property Dialog Box

You can use the Edit Operation Calling Property dialog box  to edit the information of the specified operation. This topic describes the options in the dialog box.
    

Designer displays the Edit Operation Calling Property dialog box when you right-click an operation node under the Tables node in a SOAP Web Service connection and select Edit from the shortcut menu in the Catalog Manager.

Designer displays these options:

Service Name

This option shows the service name you have selected to create the table.

Port Type

Designer displays this option only when the SOAP Web Service is defined by WSDL 1.1.
It shows the port type for the selected service. 

Operation Name

This option shows the selected operation name. 

Time Out

Specify how long to wait for the operation to complete.

Use Schema from Response 

Designer displays this option only when the SOAP Web Service is defined by WSDL 1.1.

When the XML schema in the output message does not match the specific XML instance in the SOAP responded from the web service, Report Engine is not able to read data properly from that XML instance. In this case, you can use this option to control whether to ignore the XML schema in the output message and parse the XML schema directly from the specific XML instance in the SOAP for the web service.

Input Message

This column shows the input message information for the selected operation.

Value

This column shows the values that you specify for the input messages. You can either type the value, or define a constant level formula or parameter to be the value of an input message.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
