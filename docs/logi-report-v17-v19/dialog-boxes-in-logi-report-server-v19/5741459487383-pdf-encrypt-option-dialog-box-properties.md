---
title: "PDF Encrypt Option Dialog Box Properties"
id: 5741459487383
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741459487383-PDF-Encrypt-Option-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:39Z
---

# PDF Encrypt Option Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741446257943-Parameter-Form-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741446173335-PDF-Sign-Option-Dialog-Box-Properties)

# PDF Encrypt Option Dialog Box Properties

This topic describes how you can use the PDF Encrypt Option dialog box to set encryption properties for the PDF output. Server displays the dialog box when you select **Encrypt** in the [Export dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741458025111-Export-Dialog-Box-Properties).

![PDF Encrypt Option dialog](https://devnet.logianalytics.com/hc/article_attachments/9905718470423/pdfencrypt.gif)

**Compatibility**

Specify the encryption type to encrypt the PDF document. Acrobat 3.0 and later uses a low encryption level (40-bit RC4), while Acrobat 5.0 and later uses a high encryption level (128-bit RC4).

**Encryption Level**

Server shows the level of the encryption compatibility that you specified in the Compatibility drop-down list.

**Require a password to open the document**

Specify a password to prevent others from opening the document without authorization.

* **Document Open Password**  
   Specify the password to prevent others from opening the document without authorization.
* **Confirm Password**  
   Type the password again to confirm it.

**Use a password to restrict printing and editing of the document and its security settings**

Specify a password to prevent others from printing and editing the document. The password you specify here cannot be the same as the one that you use to open the document.

* **Permissions Password**  
   Specify the password to prevent others from printing and editing.
* **Confirm Password**  
   Type the password again to confirm it.
* **Printing Allowed**  
   Specify the printing quality for the PDF document.
* **Changes Allowed**  
   Specify the editing actions you want to do in the PDF document.

**Enable copying of text, images and other content**

Select if you want to select and copy the contents of the PDF document.

**Enable text access for screen reader devices for the visually impaired**

Select if you want visually impaired users to read the PDF document with window readers. This property is available only if you have set Compatibility as "Acrobat 5.0 or later".

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741446257943-Parameter-Form-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741446173335-PDF-Sign-Option-Dialog-Box-Properties)
