---
title: "Edit Operation Calling Property Dialog"
id: 1500009607962
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009607962-Edit-Operation-Calling-Property-Dialog
updated_at: 2021-07-24T16:04:46Z
---

# Edit Operation Calling Property Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607942-Edit-Node-Style-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630781-Edit-Parameter-Dialog)

# Edit Operation Calling Property Dialog

The Edit Operation Calling Property dialog helps you to [edit the information of the specified operation](https://devnet.logianalytics.com/hc/en-us/articles/1500009629701-SOAP-Web-Service-Connections#Operation). It appears when you right-click an operation node under the Tables node in a web service connection and select Edit from the shortcut menu in the Catalog Manager.

![Edit Operating Calling Property dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904347031/edtoprtn.gif)

The following are details about options in the dialog:

**Service Name**

Displays the service name you have selected to create the table.

**Port Type**

Displays the port type for the selected service. Available only when the web service is defined by WSDL 1.1.

**Operation Name**

Displays the selected operation name.

**Time Out**

Specifies how long to wait for the operation to complete.

**Use Schema from Response**

This option is available only when the web service is defined by WSDL 1.1.

When the XML schema in the output message does not match the specific XML instance in the SOAP responded from the web service, Logi Report will not be able to read data properly from that XML instance. In this condition, you can use this option to control whether to ignore the XML schema in the output message and parse the XML schema directly from the specific XML instance in the SOAP for the web service.

**Input Message**

Lists the input message information for the selected operation.

**Value**

Specifies the value for the input message. You can either type in the value, or define a constant level formula or parameter to be the value of the input message.

**OK**

Accepts the editing operation result and closes the dialog.

**Cancel**

Cancels the editing operation process and exists the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607942-Edit-Node-Style-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630781-Edit-Parameter-Dialog)
