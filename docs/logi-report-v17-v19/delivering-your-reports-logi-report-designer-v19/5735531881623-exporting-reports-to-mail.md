---
title: "Exporting Reports to Mail"
id: 5735531881623
section: "Delivering Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735531881623-Exporting-Reports-to-Mail
updated_at: 2022-11-02T07:57:53Z
---

# Exporting Reports to Mail

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525374615-Exporting-Reports-to-Logi-Report-Result)

# Exporting Reports to Mail

If you want to send a report to other people, you can attach it to an email. This topic describes how you can configure the report email system and export reports via email.

This topic contains the following sections:

* [Configuring the Report Email System](#Config)
* [Exporting Reports via Email](#Export)

## Configuring the Report Email System

1. Navigate to **File** > **Options**. Designer displays the Options dialog box.
2. In the **Category** box, select **Export to**. Designer selects the E-mail tab by default.

   ![Options dialog box - Export to category - E-mail tab](https://devnet.logianalytics.com/hc/article_attachments/9898476923159/optn_expt_mal.gif)
3. In the **SMTP Server**
   text box, specify the numeric or named host of the machine where the email server is located.
4. In the **Port**
   text box, type the port where the email server runs.
5. In the **Mail Sender** text box, specify the address of the email sender. You must specify an address and make sure that the format of the specified address is valid.
6. From the **Default Mail Format** drop-down list, select the default format with which to send the report.
7. Select **Server requires authentication** if the email server requires authentication. However, if the email server does not need authentication but you select the option, the email may not be sent successfully due to the email server.
8. Select **Compress Attachment as Java Archive**  to compress the email before sending out.
9. Select **OK** to apply the settings.

## Exporting Reports via Email

After you have configured the report email system in the Options dialog box, you can now export your page or web reports to others via email.

1. Open the report that you want to export.
2. Navigate to **File** > **Export** > **To Mail**. Designer displays the [Export to Mail dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735500667927-Export-to-Mail-Dialog-Box).

   ![Export to Mail dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898476929303/expt2mal.gif)
3. Specify addresses for **TO**, **CC**, and **Bcc** respectively.
4. Specify the email subject in the **Subject** text box.
5. If your SMTP server requires authentication, specify the options in the **SMTP Logon Information** box.
6. Type some comments for the email in the **Comments** box. What you write here displays in the text part of your email.
7. When you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can select a report tab and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to change the order of the report tabs.
8. From the **Formats** drop-down list, select the format to send the email.
   * **E-mail Result in HTML E-mail Format**  
     Select this option if you want to send the report via email to the specified address in HTML. The report displays in HTML in the email body. If you select this format, the comments that you specify is overwritten by the report.
   * **E-mail Result in Plain Text E-mail Format**  
     Select this option if you want to send the report via email to the specified address in plain Text format. The report displays in plain text format in the email body with no other information such as color and images.
   * **Attachment in XXX Format**  
     Select this option if you want to send the report via email to the specified address with a XXX file as attachment.
9. Specify the parameters for the selected format. When you select to send the report as an attachment, you can specify whether to compress the attachment as Java archive. For more information about the parameters of each format, see the corresponding topic in [Exporting Reports](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports).
10. Select **OK** to send the report to the specified email address. The recipient can open the email normally, using Outlook Express or any other email processing product.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525374615-Exporting-Reports-to-Logi-Report-Result)
