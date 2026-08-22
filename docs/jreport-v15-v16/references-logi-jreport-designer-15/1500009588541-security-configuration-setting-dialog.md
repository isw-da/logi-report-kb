---
title: "Security Configuration Setting Dialog"
id: 1500009588541
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009588541-Security-Configuration-Setting-Dialog
updated_at: 2021-07-24T05:54:53Z
---

# Security Configuration Setting Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009588941-Search-Reports-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588521-Security-Dialog)

# Security Configuration Setting Dialog

The Security Configuration Setting dialog appears when you select the Security Configuration button in the [Web Service Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009567922-SOAP-Web-Service-Data-Source-Dialog) dialog. It helps you to configure security for the [web service data source](https://devnet.logianalytics.com/hc/en-us/articles/1500009585401-Setting-Up-a-Web-Service-Connection). [See the dialog](javascript:%20void(null)).

![Security Configuration Setting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893857303/scrtyconfigset.gif)

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
   Specifies the URI to get the key store file. You can select the Browse button to find the file or input the file path directly in the text field.
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

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**OK**

Accepts the configuration settings and closes the dialog.

**Cancel**

Cancels the configuration settings and exists the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009588941-Search-Reports-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588521-Security-Dialog)
