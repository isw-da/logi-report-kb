---
title: "Exporting Reports to Mail"
id: 28898302918285
section: "Delivering Your Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898302918285-Exporting-Reports-to-Mail
updated_at: 2024-09-30T09:12:02Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Exporting Reports to Mail

If you want to send a report to other people, you can attach it to an email. This topic describes how you can configure the report email system and export reports via email.

This topic contains the following sections:

- Configuring the Report Email System

- Exporting Reports via Email

## 
Configuring the Report Email System

- Navigate to File > Options. Designer displays the Options dialog box.

- In the Category box, select Export to. Designer selects the E-mail tab by default.
    

- In the SMTP Server
 text box, specify the numeric or named host of the machine where the email server is located.

- In the Port
 text box, type the port where the email server runs.

- In the Mail Sender text box, specify the address of the email sender. You must specify an address and make sure that the format of the specified address is valid.

- From the Default Mail Format drop-down list, select the default format with which to send the report.

- Select Server requires authentication if the email server requires authentication. However, if the email server does not need authentication but you select the option, the email may not be sent successfully due to the email server.  

- Select Compress Attachment as Java Archive  to compress the email before sending out.

- Select OK to apply the settings.

## 
Exporting Reports via Email

After you have configured the report email system in the Options dialog box, you can now export your page or web reports to others via email.

- Open the report that you want to export. 

- Navigate to File > Export >  To Mail. Designer displays the Export to Mail dialog box.
	

- Specify addresses for TO, CC, and Bcc respectively.

- Specify the email subject in the Subject text box.

- If your SMTP server requires authentication, specify the options in the SMTP Logon Information box.

- Type some comments for the email in the Comments box. What you write here displays in the text part of your email.

- When you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can select a report tab and select Move Up or Move Down to change the order of the report tabs.

- From the Formats drop-down list, select the format to send the email. 
    
- 
E-mail Result in HTML E-mail Format
Select this option if you want to send the report via email to the specified address in HTML. The report displays in HTML in the email body. If you select this format, the comments that you specify is overwritten by the report.

- 
E-mail Result in Plain Text E-mail Format
Select this option if you want to send the report via email to the specified address in plain Text format. The report displays in plain text format in the email body with no other information such as color and images.

- 
Attachment in XXX Format
Select this option if you want to send the report via email to the specified address with a XXX file as attachment.

- Specify the parameters for the selected format. When you select to send the report as an attachment, you can specify whether to compress the attachment as Java archive. For more information about the parameters of each format, see the corresponding topic in Exporting Reports.

- Select OK to send the report to the specified email address. The recipient can open the email normally, using Outlook Express or any other email processing product.

Previous Topic  Next Topic
