---
title: "Quick Schedule Dialog Box Properties"
id: 5741436360471
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741436360471-Quick-Schedule-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:42Z
---

# Quick Schedule Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741446321303-Printer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741466515607-RealMedia-Properties)

# Quick Schedule Dialog Box Properties

This topic describes how you can use the Quick Schedule dialog box to [schedule a report task](https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report#Schedule) based on the current web report in Web Report Studio. Server displays the dialog box when you select the Quick Schedule button ![Quick Schedule button](https://devnet.logianalytics.com/hc/article_attachments/9905654855063/btn_schdl.gif) on the toolbar in the **View Mode** of Web Report Studio.

![Quick Schedule dialog](https://devnet.logianalytics.com/hc/article_attachments/9905654880151/qckschdl.gif)

**Schedule Name**

Specify the name for the schedule task.

**Time Type**

Specify when you want to perform the task.

* **Immediately**  
   Select if you want to perform the task as soon as you submit it.
* **Periodically**  
  Select if you want to perform the task on a repeated basis.
  + **Date**  
    Specify the dates when you want to perform the task.   
    - **Daily**  
      Select if you want to perform the task every day.
    - **Weekly**  
       Select if you want to perform the task on a specific day every week.
      * **On**  
         Specify a day of the week.
    - **Monthly**  
       Select if you want to perform the task every month on a specific day.
      * **On**  
         Specify a day of the month.
  + **Time At**  
     Specify the time of the day when you want to perform the task.

**Publish To**

Specify to publish the report to one of the following locations:

* **E-mail**  
   Select to publish the report to email.
  + **To**  
     Specify the address you want to send the email to.
  + **CC**  
     Specify the address you want to copy the email to.
  + **BCC**  
     Specify the address you want to secretly copy the email to.
  + **Subject**  
     Specify the subject of the email.
  + **Comments**  
     Specify the contents of the email or comments to the contents.
  + **E-mail Result in**  
    Select to send the report in the mail body.
    - **HTML**  
       Select to send the report in HTML in the mail body. The report will overwrite the comments that you input for the email.
    - **Text**  
       Select to send the report in plain text format in the mail body with no other information such as color and images. Server positions the comments that you input for the email in front of the report.
  + **Attachment in**  
    Select to send the report as an attachment.
    - **Web Report Result**  
      Select to send the report in a static web report result file (WST file) as attachment in the email.
    - **PDF**  
       Select to send the report in a PDF file as attachment in the email.
    - **HTML**  
       Select to send the report in an HTML file as attachment in the email.
    - **Excel**  
       Select to send the report in an Excel file as attachment in the email.
    - **Text**  
       Select to send the report in a Text file as attachment in the email.
    - **RTF**  
       Sends the report in an RTF file as attachment in the email.
    - **XML**  
       Select to send the report in an XML file as attachment in the email.
    - **PostScript**  
       Select to send the report in a PostScript file as attachment in the email.
* **Version System**  
   Select to publish the report to the Server versioning system.
  + **Format**  
     Specify in which format you want to publish the report.
    - **Web Report Result**  
      Select to publish the report to a static web report result file (WST file). You can export WST files to HTML, PDF, Text, Excel, XML, RTF, and Postscript formats via Server.
    - **PDF**  
      Select to publish the report to the versioning system in PDF.
    - **HTML**  
       Select to publish the report to the versioning system in HTML.
    - **Excel**  
       Select to publish the report to the versioning system in Excel.
    - **Text**  
       Select to publish the report to the versioning system in Text.
    - **RTF**  
       Select to publish the report to the versioning system in RTF.
    - **XML**  
       Select to publish the report to the versioning system in XML.
    - **PostScript**  
       Select to publish the report to the versioning system in PostScript.
* **FTP**  
   Select to send the report to an FTP site.
  + **Host Address**  
     Specify the domain name or IP address of the FTP site. It cannot be null.
  + **Port**  
     Specify the port of the FTP server. It is optional. By default, 21 is used for Standard FTP and Explicit FTPS, 22 for SCP and SFTP, and 990 for Implicit FTPS.
  + **User Name**  
     Specify the username that is valid to the authentication of the FTP server and that can access the FTP site. If you don't provide username here, Server will use "anonymous" as the username by default.
  + **Password**  
     Specify the password that is valid to the authentication of the FTP server and that enables the username to access the FTP site.
  + **Account**  
     The account of the FTP user if there exists.
  + **Folder Location**  
     Specify the location where you want to put the report file on the FTP server. If you don't provide a location here, Server will use the root path "/" of the FTP server by default.
  + **[Protocol Type](https://devnet.logianalytics.com/hc/en-us/articles/5741433620631-Schedule-Dialog-Box-Properties#ProtocolType)**  
     Specify the protocol type for publishing the report to FTP.
  + **Format**  
     Specify in which format you want to send the report to the FTP site.
    - **Web Report Result**  
      Select to send the report in a static web report result file (WST file) to the specified FTP site.
    - **PDF**  
      Select to send the report in a PDF file to the specified FTP site.
    - **HTML**  
       Select to send the report in an HTML file to the specified FTP site.
    - **Excel**  
       Select to send the report in an Excel file to the specified FTP site.
    - **Text**  
       Select to send the report in a Text file to the specified FTP site.
    - **RTF**  
       Select to send the report in an RTF file to the specified FTP site.
    - **XML**  
       Select to send the report in an XML file to the specified FTP site.
    - **PostScript**  
       Select to send the report in a PostScript file to the specified FTP site.

**OK**

Select to submit the task with the settings you specified here.

**Cancel**

Select to close the dialog box without scheduling a report task.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without scheduling a report task.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741446321303-Printer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741466515607-RealMedia-Properties)
