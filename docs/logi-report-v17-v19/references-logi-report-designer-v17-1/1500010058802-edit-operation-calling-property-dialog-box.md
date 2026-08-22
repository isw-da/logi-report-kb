---
title: "Edit Operation Calling Property Dialog Box"
id: 1500010058802
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058802-Edit-Operation-Calling-Property-Dialog-Box
updated_at: 2021-07-23T19:15:17Z
---

# Edit Operation Calling Property Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058782-Edit-Node-Style-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096341-Edit-Parameter-Dialog-Box)

# Edit Operation Calling Property Dialog Box

You can use the Edit Operation Calling Property dialog box to [edit the information of the specified operation](https://devnet.logianalytics.com/hc/en-us/articles/1500010057862-Connecting-via-SOAP-Web-Service-Connections#Operation). This topic describes the options in the dialog box.

Designer displays the Edit Operation Calling Property dialog box when you right-click an operation node under the Tables node in a web service connection and select Edit from the shortcut menu in the Catalog Manager.

![Edit Operating Calling Property dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848583447/edtoprtn.gif)

You see the following options in the dialog box:

**Service Name**

The option shows the service name you have selected to create the table.

**Port Type**

The option shows the port type for the selected service. Designer displays the option only when the web service is defined by WSDL 1.1.

**Operation Name**

The option shows the selected operation name.

**Time Out**

Specify how long to wait for the operation to complete.

**Use Schema from Response**

Designer displays the option only when the web service is defined by WSDL 1.1.

When the XML schema in the output message does not match the specific XML instance in the SOAP responded from the web service, Logi Report Engine is not able to read data properly from that XML instance. In this case, you can use this option to control whether to ignore the XML schema in the output message and parse the XML schema directly from the specific XML instance in the SOAP for the web service.

**Input Message**

The column shows the input message information for the selected operation.

**Value**

The column shows the values that you specify for the input messages. You can either type the value, or define a constant level formula or parameter to be the value of an input message.

**OK**

Select to accept the editing result and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058782-Edit-Node-Style-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096341-Edit-Parameter-Dialog-Box)
