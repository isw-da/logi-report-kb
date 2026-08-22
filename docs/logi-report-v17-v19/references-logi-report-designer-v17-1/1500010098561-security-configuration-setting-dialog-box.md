---
title: "Security Configuration Setting Dialog Box"
id: 1500010098561
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010098561-Security-Configuration-Setting-Dialog-Box
updated_at: 2021-07-23T19:15:55Z
---

# Security Configuration Setting Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060282-Security-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098581-Select-a-Report-Dialog-Box)

# Security Configuration Setting Dialog Box

The Security Configuration Setting dialog box helps you to configure security for a [web service data source](https://devnet.logianalytics.com/hc/en-us/articles/1500010057862-Connecting-via-SOAP-Web-Service-Connections#Set). It appears when you select the Security Configuration button in the [Web Service Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099201-SOAP-Web-Service-Data-Source-Dialog-Box).

![Security Configuration Setting dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848499991/scrtyconfigset.gif)

The followings are details about options of the dialog box:

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
  Specifies the URI to get the key store file. You can select the Browse button to find the file or type the file path in the text box.
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

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties).

**OK**

Accepts the configuration settings and closes the dialog box.

**Cancel**

Cancels the configuration settings and exists the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060282-Security-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098581-Select-a-Report-Dialog-Box)
