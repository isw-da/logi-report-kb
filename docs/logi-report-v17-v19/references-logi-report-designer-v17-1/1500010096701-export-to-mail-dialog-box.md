---
title: "Export to Mail Dialog Box"
id: 1500010096701
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096701-Export-to-Mail-Dialog-Box
updated_at: 2021-07-23T19:15:22Z
---

# Export to Mail Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059002-Export-to-Logi-Report-Result-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096721-Export-to-PDF-Dialog-Box)

# Export to Mail Dialog Box

You can use the Export to Mail dialog box to send the current report as an attachment in a specified format to someone else [via e-mail](https://devnet.logianalytics.com/hc/en-us/articles/1500010060922-Exporting-to-Mail). This topic describes the options in the dialog box.

Designer displays the Export to Mail dialog box when you select File > Export > To Mail.

![Export to Mail dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856877079/expt2mal.gif)

You see the following options in the dialog box:

**To**

Specify the e-mail address of the recipients to whom you want to send the report.

**Cc**

Specify the e-mail address of the recipients to whom you want to send a copy of the report.

**Bcc**

Specify the e-mail address of the recipients to whom you want to send a blind carbon copy of the report.

**Subject**

Specify the subject of the e-mail.

**SMTP Logon Information**

Designer displays the following options when you have selected "Server requires authentication" in the Options dialog box.

* **Account Name**  
  Specify the account name in the SMTP server.
* **Password**  
  Specify the password for logging on to the SMTP server.
* **E-mail Address**  
  Specify the e-mail address in the SMTP server. Some SMTP may not need the mail address as one part of authentication information.

**Comments**

Specify some comments about the report. The contents in this text box will be shown in the text part of the mail.

**Select Report Tabs**

Designer displays the option when you use the dialog box for exporting a page report. Select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. If the report has only one report tab, Designer selects the report tab by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified report tab higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified report tab lower in the list.

**Formats**

Select in which mail format to send the report.

* **E-mail Result in HTML E-mail Format**  
  Select to send the report result via e-mail to the specified address in HTML. The report result will be shown in HTML in the mail body. If you select this format, the comments that you specify will be overwritten by the report. For the HTML format options, see [Export to HTML dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096681-Web-Wizard-Dialog-Box).
* **E-mail Result in Plain Text E-mail Format**  
  Select to send the report result via e-mail to the specified address in plain text format. The report result will be shown in plain text format in the mail body with no other information such as color and images. For the Text format options, see [Export to Text dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096741-Export-to-Text-Dialog-Box).
* **Attachment in Logi Report Result Format**  
  Select to send the report result via e-mail to the specified address with a Logi Report result file as attachment. You can specify whether to compress the attachment as Java Archive. For the other options about the Logi Report Result format, see [Export to Logi Report Result dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059002-Export-to-Logi-Report-Result-Dialog-Box).
* **Attachment in HTML Format**  
  Select to send the report result via e-mail to the specified address with an HTML file as attachment. You can specify whether to compress the attachment as Java Archive. For the other options about the HTML format, see [Export to HTML dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096681-Web-Wizard-Dialog-Box).
* **Attachment in PDF Format**  
  Select to send the report result via e-mail to the specified address with a PDF file as attachment. You can specify whether to compress the mail attachment as Java Archive. For the other options about the PDF format, see [Export to PDF dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096721-Export-to-PDF-Dialog-Box).
* **Attachment in Excel Format**  
  Select to send the report result via e-mail to the specified address with an Excel file as attachment. You can specify whether to compress the attachment as Java Archive. For the other options about the Excel format, see [Export to Excel dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058962-Export-to-Excel-Dialog-Box).
* **Attachment in Text Format**  
  Select to send the report result via e-mail to the specified address with a Text file as attachment. You can specify whether to compress the attachment as Java Archive. For the other options about the Text format, see [Export to Text dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096741-Export-to-Text-Dialog-Box).
* **Attachment in RTF Format**  
  Select to send the report result via e-mail to the specified address with a RTF file as attachment. You can specify whether to compress the attachment as Java Archive. For the other options about the RTD format, see [Export to RTF dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059022-Export-to-RTF-Dialog-Box).
* **Attachment in XML Format**  
  Select to send the report result via e-mail to the specified address with an XML file as attachment. You can specify whether to compress the attachment as Java Archive. For the other options about the XML format, see [Export to XML dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096761-Export-to-XML-Dialog-Box).
* **Attachment in PostScript Format**  
  Select to send the report result via e-mail to the specified address with a PostScript file as attachment. You can specify whether to compress the attachment as Java Archive. For the other options about the PostScript format, see [Export to PostScript dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058982-Export-to-PostScript-Dialog-Box).

**OK**

Select to apply all changes and send the report to the specified E-mail address.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059002-Export-to-Logi-Report-Result-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096721-Export-to-PDF-Dialog-Box)
