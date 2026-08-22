---
title: "Quick Schedule Dialog Box Properties"
id: 4405690600215
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690600215-Quick-Schedule-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:26Z
---

# Quick Schedule Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683872023-Query-Filter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683873047-RealMedia-Properties)

# Quick Schedule Dialog Box Properties

This topic describes how you can use the Quick Schedule dialog box to [schedule a report task](https://devnet.logianalytics.com/hc/en-us/articles/4405690686231-General-Operations-in-Web-Report#Schedule) based on the current web report in Web Report Studio. Server displays the dialog box when you select the Quick Schedule button ![Quick Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4420447088151/btn_schdl.gif) on the toolbar in the **View Mode** of Web Report Studio.

![Quick Schedule dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447088407/qckschdl.gif)

**Schedule Name**

Specifies the name for the schedule task.

**Time Type**

Specifies when the task will be performed.

* **Immediately**  
   Specifies to run the task as soon as you select **OK** in the dialog box.
* **Periodically**  
   Specifies the time for when the task is to be performed on a repeated basis.
  + **Date**  
    - **Daily**  
       Performs the task every day.
    - **Weekly**  
       Performs the task every week on a specific weekday.
      * **On**  
         Specifies a week day.
    - **Monthly**  
       Performs the task every month on a specific day.
      * **On**  
         Specifies a day of a month.
  + **Time** **At**  
     Specifies the exact time at which the task is to be performed.

**Publish To**

Specifies to publish the report to one of the following locations:

* **E-mail**  
   Specifies to publish the report to email.
  + **To**  
     Specifies the address you want to send the email to.
  + **CC**  
     Specifies the address you want to copy to.
  + **BCC**  
     Specifies the address you want to secretly copy to.
  + **Subject**  
     Specifies the subject of the email.
  + **Comments**  
     Specifies the contents of the email or comments to the contents.
  + **E-mail Result in**  
    Specifies whether to send the report in the mail body.
    - **HTML**  
       The report will be shown in HTML format in the mail body. The comments that you input for the email will be overwritten by the report.
    - **Text**  
       The report will be shown in plain text format in the mail body with no other information such as color and images. The comments that you input for the email will be positioned in front of the report.
  + **Attachment in**  
    Specifies whether to send the report as an attachment.
    - **Web Report Result**  
      Sends the report in a static web report result file (WST file) as attachment in the email.
    - **PDF**  
       Sends the report in a PDF file as attachment in the email.
    - **HTML**  
       Sends the report in an HTML file as attachment in the email.
    - **Excel**  
       Sends the report in an Excel file as attachment in the email.
    - **Text**  
       Sends the report in a Text file as attachment in the email.
    - **RTF**  
       Sends the report in an RTF file as attachment in the email.
    - **XML**  
       Sends the report in an XML file as attachment in the email.
    - **PostScript**  
       Sends the report in a PostScript file as attachment in the email.
* **Version System**  
   Specifies to publish the report to the Logi Report Server versioning system.
  + **Format**  
     Specifies in which format to publish the report.
    - **Web Report Result**  
      Publishes the report to a static web report result file (WST file). WST files can be exported to HTML, PDF, Text, Excel, XML, RTF, and Postscript formats via Logi Report Server.
    - **PDF**  
      Publishes the report to the versioning system in PDF format.
    - **HTML**  
       Publishes the report to the versioning system in HTML format.
    - **Excel**  
       Publishes the report to the versioning system in Excel format.
    - **Text**  
       Publishes the report to the versioning system in Text format.
    - **RTF**  
       Publishes the report to the versioning system in RTF format.
    - **XML**  
       Publishes the report to the versioning system in XML format.
    - **PostScript**  
       Publishes the report to the versioning system in PostScript format.
* **FTP**  
   Specifies to send the report to an FTP site.
  + **Host Address**  
     The domain name or IP address of the FTP site. It cannot be null.
  + **Port**  
     The port of the FTP server. It is optional, and by default 21 is used for Standard FTP and Explicit FTPS, 22 for SCP and SFTP, and 990 for Implicit FTPS.
  + **User Name**  
     The username is valid to the authentication of the FTP server that can access the FTP site. If not specified, "anonymous" will be used as the username by default.
  + **Password**  
     The password is valid to the authentication of the FTP server that enables the username to access the FTP site.
  + **Account**  
     The account of the FTP user if there exists.
  + **Folder Location**  
     The location where to put the report file on the FTP server. If not specified, the root path "/" of the FTP server will be used by default.
  + **[Protocol Type](https://devnet.logianalytics.com/hc/en-us/articles/4405683761815-Schedule-Dialog-Box-Properties#ProtocolType)**  
     Specifies the protocol type used for publishing the report to FTP.
  + **Format**  
     Specifies in which format to send the report to the FTP site.
    - **Web Report Result**  
      Sends the report in a static web report result file (WST file) to the specified FTP site.
    - **PDF**  
      Sends the report in a PDF file to the specified FTP site.
    - **HTML**  
       Sends the report in an HTML file to the specified FTP site.
    - **Excel**  
       Sends the report in an Excel file to the specified FTP site.
    - **Text**  
       Sends the report in a Text file to the specified FTP site.
    - **RTF**  
       Sends the report in an RTF file to the specified FTP site.
    - **XML**  
       Sends the report in an XML file to the specified FTP site.
    - **PostScript**  
       Sends the report in a PostScript file to the specified FTP site.

**OK**

Closes this dialog box and applies the settings.

**Cancel**

Cancels the scheduling task and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Cancels the scheduling task and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683872023-Query-Filter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683873047-RealMedia-Properties)
