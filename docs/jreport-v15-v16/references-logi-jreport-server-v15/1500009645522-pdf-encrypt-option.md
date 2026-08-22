---
title: "PDF Encrypt Option"
id: 1500009645522
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009645522-PDF-Encrypt-Option
updated_at: 2021-07-24T20:55:05Z
---

# PDF Encrypt Option

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645602-Parameter-Form-Control-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645542-PDF-Sign-Option)

# PDF Encrypt Option

The PDF Encrypt Option dialog helps you to set encryption options for the PDF file to be saved. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920620055/pdfencrpt.gif)

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

Saves the settings and exits the dialog.

**Cancel**

Cancels the settings and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645602-Parameter-Form-Control-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645542-PDF-Sign-Option)
