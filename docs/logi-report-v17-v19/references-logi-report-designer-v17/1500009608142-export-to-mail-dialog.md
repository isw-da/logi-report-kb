---
title: "Export to Mail Dialog"
id: 1500009608142
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608142-Export-to-Mail-Dialog
updated_at: 2021-07-24T16:04:41Z
---

# Export to Mail Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608162-Export-to-Logi-Report-Result-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631101-Export-to-PDF-Dialog)

# Export to Mail Dialog

The Export to Mail dialog helps you to send the current report as an attachment in a specified format to someone else [via e-mail](https://devnet.logianalytics.com/hc/en-us/articles/1500009634121-Exporting-to-Mail). It appears when you select File > Export > To Mail.

![Export to Mail dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911670935/expt2mal.gif)

The following are details about options in the dialog:

**To**

Specifies the e-mail address of the recipients to whom you want to send the report.

**Cc**

Specifies the e-mail address of the recipients to whom you want to send a copy of the report.

**Bcc**

Specifies the e-mail address of the recipients to whom you want to send a blind carbon copy of the report.

**Subject**

Specifies the subject of the e-mail that is to be sent.

**SMTP Logon Information**

The following options are available only when you have selected Server requires authentication in the Options dialog (**File** > **Options** > **Export to** > **E-mail** > **Server requires authentication**).

* **Account Name**  
   Specifies the account name in the SMTP server.
* **Password**  
   Specifies the password for logging on to the SMTP server.
* **E-mail Address**  
  Specifies the e-mail address in the SMTP server. Some SMTP may not need the mail address as one part of authentication information.

**Comments**

Specifies some comments about the report. The contents in this text box will be shown in the text part of the mail.

**Select Report Tabs**

When exporting a page report, you can specify the report tabs in the page report you want to send via e-mail. The selected report tabs will be sent in the list order. If the report has only one report tab, it is selected by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the specified report tab one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the specified report tab one step down.

**Formats**

Specifies in which mail format the report will be sent.

* **E-mail Result in HTML E-mail Format**  
  Sends the report result via e-mail to the specified address in HTML format. The report result will be shown in HTML format in the mail body. If this format is selected, the comments that you specify will be overwritten by the report. For the parameter settings, refer to [Export to HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009608122-Web-Wizard-Dialog) dialog.
* **E-mail Result in Plain Text E-mail Format**  
  Sends the report result via e-mail to the specified address in plain text format. The report result will be shown in plain text format in the mail body with no other information such as color, images and so on. For the parameter settings, refer to [Export to Text](https://devnet.logianalytics.com/hc/en-us/articles/1500009608182-Export-to-Text-Dialog) dialog.
* **Attachment in Logi Report Result Format**  
  Sends the report result via e-mail to the specified address with a Logi Report result file as attachment. You can specify whether to compress the attachment as Java Archive. For the other parameter settings, refer to [Export to Logi Report Result](https://devnet.logianalytics.com/hc/en-us/articles/1500009608162-Export-to-Logi-Report-Result-Dialog) dialog.
* **Attachment in HTML Format**  
  Sends the report result via e-mail to the specified address with an HTML file as attachment. You can specify whether to compress the attachment as Java Archive. For the other parameter settings, refer to [Export to HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009608122-Web-Wizard-Dialog) dialog.
* **Attachment in PDF Format**  
  Sends the report result via e-mail to the specified address with a PDF file as attachment. You can specify whether to compress the mail attachment as Java Archive. For the other parameter settings, refer to [Export to PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500009631101-Export-to-PDF-Dialog) dialog.
* **Attachment in Excel Format**  
  Sends the report result via e-mail to the specified address with an Excel file as attachment. You can specify whether to compress the attachment as Java Archive. For the other parameter settings, refer to [Export to Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009631081-Export-to-Excel-Dialog) dialog.
* **Attachment in Text Format**  
  Sends the report result via e-mail to the specified address with a Text file as attachment. You can specify whether to compress the attachment as Java Archive. For the other parameter settings, refer to [Export to Text](https://devnet.logianalytics.com/hc/en-us/articles/1500009608182-Export-to-Text-Dialog) dialog.
* **Attachment in RTF Format**  
  Sends the report result via e-mail to the specified address with a RTF file as attachment. You can specify whether to compress the attachment as Java Archive. For the other parameter settings, refer to [Export to RTF](https://devnet.logianalytics.com/hc/en-us/articles/1500009631141-Export-to-RTF-Dialog) dialog.
* **Attachment in XML Format**  
   Sends the report result via e-mail to the specified address with an XML file as attachment. You can specify whether to compress the attachment as Java Archive. For the other parameter settings, refer to [Export to XML](https://devnet.logianalytics.com/hc/en-us/articles/1500009608202-Export-to-XML-Dialog) dialog.
* **Attachment in PostScript Format**  
  Sends the report result via e-mail to the specified address with a PostScript file as attachment. You can specify whether to compress the attachment as Java Archive. For the other parameter settings, refer to [Export to PostScript](https://devnet.logianalytics.com/hc/en-us/articles/1500009631121-Export-to-PostScript-Dialog) dialog.

**OK**

Applies all changes, and sends the report to the specified E-mail address.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608162-Export-to-Logi-Report-Result-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631101-Export-to-PDF-Dialog)
