---
title: "Exporting to Mail"
id: 1500010033142
section: "Delivering Your Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010033142-Exporting-to-Mail
updated_at: 2021-07-24T10:38:15Z
---

# Exporting to Mail

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068401-Exporting-Report-Result) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068441-Exporting-to-JReport-Result)

# Exporting to Mail

If you want to send the result of a report to other people, you can attach it to a mail. However before you can export your reports via e-mail, you must first have the report mail system configured.

Below is a list of the sections covered in this topic:

* [Configuring the Report Mail System](#Config)
* [Exporting Reports via E-mail](#Export)

## Configuring the Report Mail System

1. Select **File** > **Options**.
2. In the Options dialog, select the **Export to** category. The E-mail tab is selected by default.

   ![Options dialog - Export to category - E-mail tab](https://devnet.logianalytics.com/hc/article_attachments/4404901164695/optn_expt_mal.gif)
3. In the SMTP Server
   text box, specify the numeric or named host of the machine where the e-mail server is located.
4. In the Port
   text box, enter the port where the e-mail server runs.
5. In the Mail Sender text box**,** 
   specify the address of the e-mail sender. You must specify an address and make sure that the format of the specified address is valid.
6. From the Default Mail Format drop-down list, select the default format with which to send the report result.
7. Check the **Server requires authentication** if the mail server requires authentication. However if the mail server does not need authentication but you check the option, the mail may not be sent successfully due to the mail server.
8. Check **Compress Attachment as Java Archive**  to compress the mail before sending out.
9. Select **OK** to apply the settings.

## Exporting Reports via E-mail

After you have configured the report mail system in the Options dialog, you can now export your reports to others via e-mail as follows:

1. Open the report that you would like to export.
2. Select **File** > **Export**  > **To****Mail** to access the [Export to Mail](https://devnet.logianalytics.com/hc/en-us/articles/1500010065961-Export-to-Mail-Dialog) dialog.

   ![Export to Mail dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901165079/expt2mal.gif)
3. Specify addresses for TO, CC, and BCC respectively.
4. Input the mail subject in the Subject text box.
5. If your SMTP server requires authentication, specify the required information in the SMTP Logon Information box.
6. Enter some comments for the mail in the Comments box, and what you write here will be shown in the text part of your mail.
7. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404901163415/btn_mvup3.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404901163671/btn_mvdwn3.gif) to change the order of the report tabs.
8. Select in which format to send the mail.
   * **E-mail Result in HTML E-mail Format**  
      Sends the report result via e-mail to the specified address in HTML format. The report result will be shown in HTML format in the mail body. If this format is selected, the comments that you input will be overwritten by the report.
   * **E-mail Result in Plain Text E-mail Format**  
      Sends the report result via e-mail to the specified address in plain Text format. The report result will be shown in plain text format in the mail body with no other information such as color, images and so on.
   * **Attachment in Logi JReport Result Format**  
      Sends the report result via e-mail to the specified address with a Logi JReport result file as attachment.
   * **Attachment in HTML Format**  
      Sends the report result via e-mail to the specified address with an HTML file as attachment.
   * **Attachment in PDF Format**  
      Sends the report result via e-mail to the specified address with a PDF file as attachment.
   * **Attachment in Excel Format**  
      Sends the report result via e-mail to the specified address with an Excel file as attachment.
   * **Attachment in Text Format**  
      Sends the report result via e-mail to the specified address with a Text file as attachment.
   * **Attachment in RTF Format**  
      Sends the report result via e-mail to the specified address with a RTF file as attachment.
   * **Attachment in XML Format**  
      Sends the report result via e-mail to the specified address with an XML file as attachment.
   * **Attachment in PostScript Format**  
      Sends the report result via e-mail to the specified address with a PostScript file as attachment.
9. Specify the parameters for the selected format as required. When you select to send the report result as an attachment, you can specify whether to compress the attachment as Java Archive. For detailed information about the parameters of each format, refer to the corresponding topic in the [Exporting Report Result](https://devnet.logianalytics.com/hc/en-us/articles/1500010068401-Exporting-Report-Result) section.
10. Select **OK**. The report result will then be sent to the specified mail address. The recipient can open the mail normally, using Outlook Express or any other mail processing product.

**Note:** If you select E-mail Result in HTML E-mail Format as the mail format, the comments that you input will be overwritten by the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068401-Exporting-Report-Result) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068441-Exporting-to-JReport-Result)
