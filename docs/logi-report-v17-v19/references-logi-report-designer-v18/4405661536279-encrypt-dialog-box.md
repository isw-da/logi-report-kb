---
title: "Encrypt Dialog Box"
id: 4405661536279
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661536279-Encrypt-Dialog-Box
updated_at: 2022-01-27T20:36:09Z
---

# Encrypt Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661535255-E-mail-Settings-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664471063-Enter-Parameter-Values-Dialog-Box)

# Encrypt Dialog Box

You can use the Encrypt dialog box to configure the [encryption settings](https://devnet.logianalytics.com/hc/en-us/articles/4405661756567-Exporting-to-PDF#Encrypt) for a PDF document. This topic describes the options in the dialog box.

Designer displays the Encrypt dialog box when you select the Setting button after selecting the Encrypt checkbox in the [Export to PDF dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664477335-Export-to-PDF-Dialog-Box).

![Encrypt dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556120599/encrypt.gif)

You see the following options in the dialog box:

**Compatibility**

Select the encryption type to encrypt the PDF document. "Acrobat 3.0 and later" uses a low encryption level (40-bit RC4), while "Acrobat 5.0 and later" uses a high encryption level (128-bit RC4).

**Encryption Level**

This option shows the level of the encryption compatibility that you select in the Compatibility drop-down list.

**Options**

* **Require a password to open the document**  
  Select to protect the document using a password.
  + **Document Open Password**  
    Specify the password to prevent users from opening the document without authorization.
  + **Confirm Password**  
    Confirm the password you specified in the Document Open Password text box.

**Permissions**

* **Use a password to restrict printing and editing of the document and its security settings**  
  Select to use a permission password to restrict users from printing and editing the PDF document.
  + **Permission Password**  
    Specify the password to restrict users from printing and editing the PDF document.
  + **Confirm Password**  
    Confirm the password you have specified in the Permission Password text box.
  + **Printing Allowed**  
    Select whether to allow users to print the PDF document.
    - **None**  
      Select to prevent users from printing the document.
    - **Low Resolution**  
      Designer displays this option when you select a high encryption level: Acrobat 5.0 and later. If you select it, users can print the document at no higher than 150-dpi resolution.
    - **High Resolution**  
      Select to allow users print at any resolution, directing high-quality vector output to PostScript and other printers that support advanced high-quality printing features.
  + **Changes Allowed**  
    Select what editing actions you allow in the PDF document.
    - **None**  
      Select to prevent users from making any changes to the document, including filling in signature and form fields.
    - **Inserting, deleting, and rotating pages**  
      Designer displays this option when you select a high encryption level: Acrobat 5.0 and later. If you select it, users can insert, delete, and rotate pages, and create bookmarks and thumbnail pages.
    - **Filling in form fields and signing**  
      Select to allow users fill in forms and add digital signatures. This option doesn't allow users to add comments or create form fields.
    - **Commenting, filling in form fields** **and signing**  
      Select to allow users fill in forms and add digital signatures and comments.
    - **Any except extracting pages**  
      Select to allow users change the document using any method listed in the Changes Allowed menu, except removing pages.
  + **Enable copying of text, images and other content**  
    Select to enable users to select and copy the contents of the PDF document.
  + **Enable text access for screen reader devices for the visually impaired**  
    Designer enables this option only when you select Compatibility of "Acrobat 5.0 or later". Select it if you want to enable the use of screen readers for visually impaired users on the PDF document.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661535255-E-mail-Settings-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664471063-Enter-Parameter-Values-Dialog-Box)
