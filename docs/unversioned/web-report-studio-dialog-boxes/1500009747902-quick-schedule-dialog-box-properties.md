---
title: "Quick Schedule Dialog Box Properties"
id: 1500009747902
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747902-Quick-Schedule-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:14Z
---

# Quick Schedule Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747922-Query-Filter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747942-RealMedia-Properties)

# Quick Schedule Dialog Box Properties

This topic describes how you can use the Quick Schedule dialog box to [schedule a report task](https://devnet.logianalytics.com/hc/en-us/articles/1500009778761-General-Operations-in-Web-Report#Schedule) based on the current web report in Web Report Studio. Server displays the dialog box when you select the Quick Schedule button ![Quick Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880187927/btn_schdl.gif) on the toolbar in the **View Mode** of Web Report Studio.

![Quick Schedule dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880188311/qckschdl.gif)

**Schedule Name**

Specifies the name for the schedule task.

**Time Type**

Specifies when the task will be performed.

* **Immediately**  
   Specifies to run the task as soon as you select OK in the dialog box.
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

Specifies to publish the report result to one of the following locations:

* **E-mail**  
   Specifies to publishing the report result to e-mail.
  + **To**  
     Specifies the address you want to send the e-mail to.
  + **CC**  
     Specifies the address you want to copy to.
  + **BCC**  
     Specifies the address you want to secretly copy to.
  + **Subject**  
     Specifies the subject of the e-mail.
  + **Comments**  
     Specifies the contents of the e-mail or comments to the contents.
  + **E-mail Result in**  
    Specifies whether to send the report result in the mail body.
    - **HTML**  
       The report result will be shown in HTML format in the mail body. The comments that you input for the e-mail will be overwritten by the report result.
    - **Text**  
       The report result will be shown in plain text format in the mail body with no other information such as color and images. The comments that you input for the e-mail will be positioned in front of the report result.
  + **Attachment in**  
    Specifies whether to send the report result as an attachment.
    - **Web Report Result**  
      Sends the report result in a static web report result file (WST file) as attachment in the e-mail.
    - **PDF**  
       Sends the report result in a PDF file as attachment in the e-mail.
    - **HTML**  
       Sends the report result in an HTML file as attachment in the e-mail.
    - **Excel**  
       Sends the report result in an Excel file as attachment in the e-mail.
    - **Text**  
       Sends the report result in a Text file as attachment in the e-mail.
    - **RTF**  
       Sends the report result in an RTF file as attachment in the e-mail.
    - **XML**  
       Sends the report result in an XML file as attachment in the e-mail.
    - **PostScript**  
       Sends the report result in a PostScript file as attachment in the e-mail.
* **Version System**  
   Specifies to publish the report result to the Logi Report Server versioning system.
  + **Format**  
     Specifies in which format to publish the report result.
    - **Web Report Result**  
      Publishes the report result to a static web report result file (WST file). WST files can be exported to HTML, PDF, Text, Excel, XML, RTF, and Postscript formats via Logi Report Server.
    - **PDF**  
      Publishes the report result to the versioning system in PDF format.
    - **HTML**  
       Publishes the report result to the versioning system in HTML format.
    - **Excel**  
       Publishes the report result to the versioning system in Excel format.
    - **Text**  
       Publishes the report result to the versioning system in Text format.
    - **RTF**  
       Publishes the report result to the versioning system in RTF format.
    - **XML**  
       Publishes the report result to the versioning system in XML format.
    - **PostScript**  
       Publishes the report result to the versioning system in PostScript format.
* **FTP**  
   Specifies to send the report result to an FTP site.
  + **Host Address**  
     The domain name or IP address of the FTP site. It cannot be null.
  + **Port**  
     The port of the FTP server. It is optional, and by default 21 is used for Standard FTP and Explicit FTPS, 22 for SCP and SFTP, and 990 for Implicit FTPS.
  + **User Name**  
     The user name is valid to the authentication of the FTP server that can access the FTP site. If not specified, "anonymous" will be used as the user name by default.
  + **Password**  
     The password is valid to the authentication of the FTP server that enables the user name to access the FTP site.
  + **Account**  
     The account of the FTP user if there exists.
  + **Folder Location**  
     The location where to put the report result file on the FTP server. If not specified, the root path "/" of the FTP server will be used by default.
  + **[Protocol Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009774581-Schedule-Dialog-Box-Properties#ProtocolType)**  
     Specifies the protocol type used for publishing the report result to FTP.
  + **Format**  
     Specifies in which format to send the report result to the FTP site.
    - **Web Report Result**  
      Sends the report result in a static web report result file (WST file) to the specified FTP site.
    - **PDF**  
      Sends the report result in a PDF file to the specified FTP site.
    - **HTML**  
       Sends the report result in an HTML file to the specified FTP site.
    - **Excel**  
       Sends the report result in an Excel file to the specified FTP site.
    - **Text**  
       Sends the report result in a Text file to the specified FTP site.
    - **RTF**  
       Sends the report result in an RTF file to the specified FTP site.
    - **XML**  
       Sends the report result in an XML file to the specified FTP site.
    - **PostScript**  
       Sends the report result in a PostScript file to the specified FTP site.

**OK**

Closes this dialog box and applies the settings.

**Cancel**

Cancels the scheduling task and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Cancels the scheduling task and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747922-Query-Filter-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747942-RealMedia-Properties)
