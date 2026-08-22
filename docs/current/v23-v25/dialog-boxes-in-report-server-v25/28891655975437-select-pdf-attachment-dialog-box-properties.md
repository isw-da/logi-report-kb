---
title: "Select PDF Attachment Dialog Box Properties"
id: 28891655975437
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891655975437-Select-PDF-Attachment-Dialog-Box-Properties
updated_at: 2026-02-26T02:13:08Z
source_host: docs-report.zendesk.com
---
# 
Select PDF Attachment Dialog Box Properties

This topic describes how you can use the Select PDF Attachment dialog box to select the file you want to attach to a data field in a web report. 

Server displays the dialog box when you right-click a data field except for chart and Map fields and then select PDF Attachment.

Attachment From

Specify the source of the attachment.

- 
Local File
  Select to use a file from the local file system. 
  - 
File Name
      Specify the path and name of the file. You can select Browse to locate the file.

- 
Web URL
  Select to use a file via URL.
    - 
File URL
      Specify the URL of the file.

 If your Server is in an intranet which requires a proxy, to access the file via URL, you need to add the parameters -Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX to the server's startup file JRServer.bat in <install_root>\bin.	  

- 
Library
  Select to use an existing file.  
    - 
PDF Attachment
      The PDF Attachment folder is a virtual location where Server stores the PDF attachments that you have once used in reports. Select the one you want.

Preview

Display a preview of the selected file if it is an image.

PDF Attachment Name

Specify the name of the PDF Attachment.

Ignore When No Attachment

Select this option if you don't want to block the export when the attachment does not exist or fails to load when exporting to PDF/A. Otherwise, Server will block the PDF/A export and throw an error message "Failed to export to PDF/A because the embedded attachment {filename} does not exist".

OK

Select to attach the file to the report and close the dialog box.

Cancel

Select to close the dialog box without attaching a file.

Help button

Select to view information about the  dialog box.

Close button

Select to close the dialog box without attaching a PDF file.
