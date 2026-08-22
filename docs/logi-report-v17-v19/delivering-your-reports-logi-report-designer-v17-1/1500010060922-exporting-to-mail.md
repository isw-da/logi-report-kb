---
title: "Exporting to Mail"
id: 1500010060922
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010060922-Exporting-to-Mail
updated_at: 2021-07-23T19:16:11Z
---

# Exporting to Mail

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060902-Exporting-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060942-Exporting-to-Logi-Report-Result)

# Exporting to Mail

If you want to send the result of a report to other people, you can attach it to an e-mail. However, before you can export report results via e-mails, you must first have the report mail system configured. This topic describes how you can configure the report mail system and export report results via e-mails.

This topic contains the following sections:

* [Configuring the Report Mail System](#Config)
* [Exporting Reports via E-mail](#Export)

## Configuring the Report Mail System

1. Select **File** > **Options**. Designer displays the Options dialog box.
2. In the **Category** box, select **Export to**. The E-mail tab is selected by default.

   ![Options dialog box - Export to category - E-mail tab](https://devnet.logianalytics.com/hc/article_attachments/4404856876695/optn_expt_mal.gif)
3. In the **SMTP Server**
   text box, specify the numeric or named host of the machine where the e-mail server is located.
4. In the **Port**
   text box, type the port where the e-mail server runs.
5. In the **Mail Sender** text box, specify the address of the e-mail sender. You must specify an address and make sure that the format of the specified address is valid.
6. From the **Default Mail Format** drop-down list, select the default format with which to send the report result.
7. Select **Server requires authentication** if the mail server requires authentication. However, if the mail server does not need authentication but you select the option, the mail may not be sent successfully due to the mail server.
8. Select **Compress Attachment as Java Archive**  to compress the mail before sending out.
9. Select **OK** to apply the settings.

## Exporting Reports via E-mail

After you have configured the report mail system in the Options dialog box, you can now export your page or web reports to others via e-mail as follows:

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To Mail**. Designer displays the [Export to Mail dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096701-Export-to-Mail-Dialog-Box).

   ![Export to Mail dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856877079/expt2mal.gif)
3. Specify addresses for **TO**, **CC**, and **Bcc** respectively.
4. Specify the mail subject in the **Subject** text box.
5. If your SMTP server requires authentication, specify the required information in the **SMTP Logon Information** box.
6. Type some comments for the mail in the **Comments** box. What you write here displays in the text part of your mail.
7. If you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can make use of the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons to change the order of the report tabs.
8. From the **Formats** drop-down list, select in which format to send the mail.
   * **E-mail Result in HTML E-mail Format**  
     Select it if you want to send the report result via e-mail to the specified address in HTML. The report result displays in HTML in the mail body. If you select this format, the comments that you specify is overwritten by the report.
   * **E-mail Result in Plain Text E-mail Format**  
     Select it if you want to send the report result via e-mail to the specified address in plain Text format. The report result displays in plain text format in the mail body with no other information such as color and images.
   * **Attachment in XXX Format**  
     Select it if you want to send the report result via e-mail to the specified address with a XXX result file as attachment.
9. Specify the parameters for the selected format. When you select to send the report result as an attachment, you can specify whether to compress the attachment as Java archive. For more information about the parameters of each format, see the corresponding topic in [Exporting Report Result](https://devnet.logianalytics.com/hc/en-us/articles/1500010060902-Exporting-Report-Result).
10. Select **OK** to send the report result to the specified mail address. The recipient can open the mail normally, using Outlook Express or any other mail processing product.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060902-Exporting-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060942-Exporting-to-Logi-Report-Result)
