---
title: "Encrypt Dialog Box"
id: 1500010096561
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096561-Encrypt-Dialog-Box
updated_at: 2021-07-23T19:15:21Z
---

# Encrypt Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096541-E-mail-Settings-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096581-Enter-Parameter-Values-Dialog-Box)

# Encrypt Dialog Box

You can use the Encrypt dialog box to configure the [encryption settings](https://devnet.logianalytics.com/hc/en-us/articles/1500010099321-Exporting-to-PDF#Encrypt) for a PDF document. This topic describes the options in the dialog box.

Designer displays the Encrypt dialog box when you select the Setting button after selecting the Encrypt checkbox in the [Export to PDF dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096721-Export-to-PDF-Dialog-Box).

![Encrypt dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848474263/encrypt.gif)

You see the following options in the dialog box:

**Compatibility**

Select the encryption type to encrypt the PDF document. "Acrobat 3.0 and later" uses a low encryption level (40-bit RC4), while "Acrobat 5.0 and later" uses a high encryption level (128-bit RC4).

**Encryption Level**

The option shows the level of the encryption compatibility that you select in the Compatibility drop-down list.

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
      Designer displays the option when you select a high encryption level - Acrobat 5.0. If you select the option, users can print the document at no higher than 150-dpi resolution.
    - **High Resolution**  
      Select to allow users print at any resolution, directing high-quality vector output to PostScript and other printers that support advanced high-quality printing features.
  + **Changes Allowed**  
    Select what editing actions you allow in the PDF document.
    - **None**  
      Select to prevent users from making any changes to the document, including filling in signature and form fields.
    - **Inserting, deleting, and rotating pages**  
      Designer displays the option when you select a high encryption level - Acrobat 5.0. If you select the option, users can insert, delete, and rotate pages, as well as create bookmarks and thumbnail pages.
    - **Filling in form fields and signing**  
      Select to allow users fill in forms and add digital signatures. This option doesn't allow users to add comments or create form fields.
    - **Commenting, filling in form fields** **and signing**  
      Select to allow users fill in forms and add digital signatures and comments.
    - **Any except extracting pages**  
      Select to allow users change the document using any method listed in the Changes Allowed menu, except removing pages.
  + **Enable copying of text, images and other content**  
    Select to enable users to select and copy the contents of the PDF document.
  + **Enable text access for screen reader devices for the visually impaired**  
    Designer enables this option only when you set Compatibility to Acrobat 5.0 or later. Select it if you want to enable the use of screen readers for visually impaired users on the PDF document.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096541-E-mail-Settings-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096581-Enter-Parameter-Values-Dialog-Box)
