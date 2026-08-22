---
title: "Encrypt Dialog Box Properties"
id: 45203925807245
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203925807245-Encrypt-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:08Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Encrypt Dialog Box Properties

This topic describes how you can use the Encrypt dialog box to specify the PDF encryption properties while configuring settings for advanced running/publishing a report in PDF.

Compatibility

Select the encryption type for encrypting the PDF output. Acrobat 3.0 and later uses a low encryption level (40-bit RC4), while Acrobat 5.0 and later uses a high encryption level (128-bit RC4).

Encryption Level

Server shows the level of the encryption compatibility that you specified in the Compatibility box.

Require a password to open the document

Select if you want to use a password to open the PDF document, to prevent others from opening it without authorization.

- 
Document Open Password
  Specify the password for opening the PDF document.

- 
Confirm Password
  Type the password again to confirm it.

Use a password to restrict printing and editing of the document and its security settings

Select if you want to use the Permissions Password to prevent others from printing and editing the document. The password you specify here cannot be the same as the one you use to open the document.

- 
Permissions Password
    Specify the password for printing and editing the PDF document.

- 
Confirm Password
    Type the password again to confirm it.

- 
Printing Allowed
    Select the printing quality for the PDF document.

- 
Changes Allowed
    Specify the editing actions you want to allow in the PDF document.

Enable copying of text, images and other content

Select if you want others to select and copy the contents of the PDF document.

Enable text access for screen reader devices for the visually impaired

Select if you want  visually impaired users to read the PDF document using window readers. This property is available only when you have selected the Compatibility property of Acrobat 5.0 and later.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
