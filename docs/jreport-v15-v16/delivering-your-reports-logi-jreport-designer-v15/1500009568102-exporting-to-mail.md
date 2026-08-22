---
title: "Exporting to Mail"
id: 1500009568102
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568102-Exporting-to-Mail
updated_at: 2021-07-24T05:54:40Z
---

# Exporting to Mail

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589221-Exporting-Report-Results)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568122-Exporting-to-Logi-JReport-Result)

# Exporting to Mail

If you want to send the results of a report to other people, you can attach it to a mail. Be aware that before you can export the report results via e-mail, you must first have your report mail system configured. Otherwise, a warning message will be displayed when you try to export to mail. When exporting a page report to mail, only the current specified report tab of the report in Logi JReport Designer will be exported.

Below is a list of the sections covered in this topic:

> * [Configuring the Report Mail System](#Configure)
> * [Exporting the Report Results to Mail](#Export)

## Configuring the Report Mail System

To configure the report mail system, follow the steps below:

1. Select **File** > **Options**.
2. In the Options dialog, select the **Export to** category.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893841303/optn_expt_mal.gif)
3. In the E-mail tab, set up the SMTP Server, Port, Mail Box and Default Mail Format respectively.
4. Check the **Server requires authentication** if the mail server requires authentication.

   **Note:** If the mail server does not need authentication but you check the Server requires authentication, the mail may not be sent successfully due to the mail server.
5. Check **Compress Attachment as Java Archive**  to compress the mail before sending out.
6. Select **OK** to apply the settings.

## Exporting the Report Results to Mail

Now you can export your report results to mail as follows:

1. Open the report that you would like to export.
2. Select **File** > **Export**  > **To****Mail** to access the Export to Mail dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893841559/expt2mal.gif)
3. Specify addresses for TO, CC, and BCC respectively.
4. Input the mail subject in the Subject field.
5. If your SMTP server requires authentication, specify the required information in the SMTP Logon Information box.
6. Enter some comments for the mail in the Comments text box, and what you write here will be shown in the text part of your mail.
7. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839511/btn_mvup3.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839767/btn_mvdwn3.gif) to change the order or the report tabs.
8. Select the required mail format and set the parameters for the format as required (for details about the parameter settings, refer to [Export to Mail](https://devnet.logianalytics.com/hc/en-us/articles/1500009565562-Export-to-Mail-Dialog) dialog).
9. Select **OK**, and the report results will then be sent to the specified mail address. The recipient can open the mail normally, using Outlook Express, or any other mail processing product.

**Note:** If you select E-mail Result in HTML E-mail Format as the mail format, the comments that you input will be overwritten by the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589221-Exporting-Report-Results)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568122-Exporting-to-Logi-JReport-Result)
