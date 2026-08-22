---
title: "PDF Encrypt Option"
id: 1500009716721
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009716721-PDF-Encrypt-Option
updated_at: 2021-11-03T06:57:13Z
---

# PDF Encrypt Option

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009716801-Parameter-Form-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009690502-PDF-Sign-Option)

# PDF Encrypt Option

The PDF Encrypt Option dialog helps you to set encryption options for the PDF file to be saved. This dialog appears when you check the Encrypt checkbox in the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009689842-Export) dialog.

![PDF Encrypt Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112583959/pdfencrypt.gif)

**Compatibility**

Specifies the encryption type to encrypt the PDF document. The option Acrobat 3.0 and later uses a low encryption level (40-bit RC4), while the other option Acrobat 5.0 and later uses a high encryption level (128-bit RC4).

**Encryption Level**

Shows the level of the encryption compatibility that you specified in the Compatibility drop-down list.

**Require a password to open the document**

Specifies the Document Open Password to prevent others from opening the document without authorization.

* **Document Open Password**  
   Specifies the password to prevent others from opening the document without authorization.
* **Confirm Password**  
   Confirms the password you have specified in the Document Open Password text box.

**Use a password to restrict printing and editing of the document and its security settings**

Specifies the Permission Password to prevent others from printing and editing the document. The password you specify here cannot be the same as the one that you use to open the document.

* **Permissions Password**  
   Specifies the password to prevent others from printing and editing.
* **Confirm Password**  
   Confirms the password you have specified in the Permissions Password text box.
* **Printing Allowed**  
   Specifies the printing quality for the PDF document.
* **Changes Allowed**  
   Specifies the editing actions that are permitted in the PDF document.

**Enable copying of text, images and other content**

Allows others to select and copy the contents of the PDF document.

**Enable text access for screen reader devices for the visually impaired**

Allows visually impaired users to read the PDF document with window readers. This option is available only if the Compatibility option is set to Acrobat 5.0 or later Acrobat version.

**OK**

Applies the encryption option settings and closes this dialog.

**Cancel**

Cancels the settings and closes this dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009716801-Parameter-Form-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009690502-PDF-Sign-Option)
