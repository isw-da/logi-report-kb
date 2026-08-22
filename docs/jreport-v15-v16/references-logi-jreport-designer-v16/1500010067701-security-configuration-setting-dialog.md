---
title: "Security Configuration Setting Dialog"
id: 1500010067701
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067701-Security-Configuration-Setting-Dialog
updated_at: 2021-07-24T10:38:25Z
---

# Security Configuration Setting Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067681-Security-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032362-Select-a-Report-Dialog)

# Security Configuration Setting Dialog

The Security Configuration Setting dialog helps you to configure security for a [web service data source](https://devnet.logianalytics.com/hc/en-us/articles/1500010064561-SOAP-Web-Service-Connections#Set). It appears when you select the Security Configuration button in the [Web Service Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010068361-SOAP-Web-Service-Data-Source-Dialog) dialog.

![Security Configuration Setting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909157911/scrtyconfigset.gif)

The followings are details about options of the dialog:

**User Name Token**

Specifies the properties for the user name token.

* **User Name**  
   Specifies the user name for the user name token to be used in the security policy.
* **Password**  
   Specifies the password for the user name token to be used in the security policy.

**Key Store**

Specifies the properties of the key store.

* **Key Store Type**  
   Specifies the type for the key store. It could be JKS or PKCS12.
* **Key Store File**  
   Specifies the URI to get the key store file. You can select the Browse button to find the file or input the file path directly in the text box.
* **Key Store Password**  
   Specifies the password to open the key store file.

**Client Key**

Specifies the properties for the client key.

* **Alias Name**  
   Specifies the alias name which is used as client signature in the key store.
* **Alias Password**  
   Specifies the password for the alias name.

**Server Key**

Specifies the properties for the server key.

* **Alias Name**  
   Specifies the alias name which is used to get the server-side certification or public key in the key store.
* **Alias Password**  
   Specifies the password for the alias name.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties).

**OK**

Accepts the configuration settings and closes the dialog.

**Cancel**

Cancels the configuration settings and exists the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067681-Security-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032362-Select-a-Report-Dialog)
