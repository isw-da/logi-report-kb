---
title: "Edit Operation Calling Property Dialog Box"
id: 5735508770583
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735508770583-Edit-Operation-Calling-Property-Dialog-Box
updated_at: 2022-11-02T04:15:03Z
---

# Edit Operation Calling Property Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513788311-Edit-Node-Style-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735565715351-Edit-Parameter-Dialog-Box)

# Edit Operation Calling Property Dialog Box

You can use the Edit Operation Calling Property dialog box to [edit the information of the specified operation](https://devnet.logianalytics.com/hc/en-us/articles/5735528205847-Accessing-Data-via-SOAP-Web-Service-Connections#Operation). This topic describes the options in the dialog box.

Designer displays the Edit Operation Calling Property dialog box when you right-click an operation node under the Tables node in a SOAP Web Service connection and select Edit from the shortcut menu in the Catalog Manager.

![Edit Operating Calling Property dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898481678103/edtoprtn.gif)

Designer displays these options:

**Service Name**

This option shows the service name you have selected to create the table.

**Port Type**

Designer displays this option only when the SOAP Web Service is defined by WSDL 1.1.
It shows the port type for the selected service.

**Operation Name**

This option shows the selected operation name.

**Time Out**

Specify how long to wait for the operation to complete.

**Use Schema from Response**

Designer displays this option only when the SOAP Web Service is defined by WSDL 1.1.

When the XML schema in the output message does not match the specific XML instance in the SOAP responded from the web service, Logi Report Engine is not able to read data properly from that XML instance. In this case, you can use this option to control whether to ignore the XML schema in the output message and parse the XML schema directly from the specific XML instance in the SOAP for the web service.

**Input Message**

This column shows the input message information for the selected operation.

**Value**

This column shows the values that you specify for the input messages. You can either type the value, or define a constant level formula or parameter to be the value of an input message.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513788311-Edit-Node-Style-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735565715351-Edit-Parameter-Dialog-Box)
