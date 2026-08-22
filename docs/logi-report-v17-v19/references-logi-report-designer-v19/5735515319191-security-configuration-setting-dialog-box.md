---
title: "Security Configuration Setting Dialog Box"
id: 5735515319191
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735515319191-Security-Configuration-Setting-Dialog-Box
updated_at: 2022-11-02T04:40:16Z
---

# Security Configuration Setting Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735524608407-Security-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735552759063-Select-a-Report-Dialog-Box)

# Security Configuration Setting Dialog Box

You can use the Security Configuration Setting dialog box to configure security for a [SOAP Web Service data source](https://devnet.logianalytics.com/hc/en-us/articles/5735528205847-Accessing-Data-via-SOAP-Web-Service-Connections#Set). This topic describes the options in the dialog box.

Designer displays the Security Configuration Setting dialog box when you select Security Configuration in the [SOAP Web Service Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735553273623-SOAP-Web-Service-Data-Source-Dialog-Box).

![Security Configuration Setting dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898460973463/scrtyconfigset.gif)

Designer displays these options:

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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Designer display the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) for some options. It indicates that you can [use a formula to control the value](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties) of an option.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735524608407-Security-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735552759063-Select-a-Report-Dialog-Box)
