---
title: "Security Configuration Setting Dialog Box"
id: 4405661698071
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661698071-Security-Configuration-Setting-Dialog-Box
updated_at: 2022-01-27T20:36:12Z
---

# Security Configuration Setting Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661696919-Security-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664574743-Select-a-Report-Dialog-Box)

# Security Configuration Setting Dialog Box

You can use the Security Configuration Setting dialog box to configure security for a [web service data source](https://devnet.logianalytics.com/hc/en-us/articles/4405661439639-Connecting-via-SOAP-Web-Service-Connections#Set). This topic describes the options in the dialog box.

Designer displays the Security Configuration Setting dialog box when you select Security Configuration in the [Web Service Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661748759-SOAP-Web-Service-Data-Source-Dialog-Box).

![Security Configuration Setting dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550865175/scrtyconfigset.gif)

You see the following options in the dialog box:

**User Name Token**

You can specify options for the user name token in this box.

* **User Name**  
  Specify the user name for the user name token to use in the security policy.
* **Password**  
  Specify the password for the user name token to use in the security policy.

**Key Store**

You can specify options for the key store in this box.

* **Key Store Type**  
  Select the type for the key store: JKS or PKCS12.
* **Key Store File**  
  Specify the URI to get the key store file. You can select **Browse** to find the file or type the file path in the text box.
* **Key Store Password**  
  Specify the password to open the key store file.

**Client Key**

You can specify options for the client key in this box.

* **Alias Name**  
  Specify the alias name to use as client signature in the key store.
* **Alias Password**  
  Specify the password for the alias name.

**Server Key**

You can specify options for the server key in this box.

* **Alias Name**  
  Specify the alias name to get the server-side certification or public key in the key store.
* **Alias Password**  
  Specify the password for the alias name.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Designer display the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) for some options. It indicates that you can [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties) of an option.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661696919-Security-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664574743-Select-a-Report-Dialog-Box)
