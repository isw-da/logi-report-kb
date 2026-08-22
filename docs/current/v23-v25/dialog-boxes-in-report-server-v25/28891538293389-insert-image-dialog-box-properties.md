---
title: "Insert Image Dialog Box Properties"
id: 28891538293389
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891538293389-Insert-Image-Dialog-Box-Properties
updated_at: 2026-02-26T02:13:00Z
source_host: docs-report.zendesk.com
---
# 
Insert Image Dialog Box Properties

This topic describes how you can use the Insert Image dialog box to select the image you want to use in a web report. 

Server displays the dialog box in the following cases:

- Drag Image from the Components panel to a report.

- Select the ellipsis button  on the Page screen of the Web Report Wizard.

- Select Customized from the Value Pointer or Target Pointer drop-down list in the Format Bar Gauge, Format Dial Gauge, or Format Solid Gauge dialog box.

- Select Customized in the Value Pointer drop-down list in the Style List dialog box.

Image From

Specify the source of the image file.

- 
Local File
  Select to use an image from the local file system. 
  - 
File Name
      Specify the path and name of the image file. You can select Browse to locate the image file.

- 
Web URL
  Select to use an image via URL.
    - 
File URL
      Specify the URL of the image file.

 If your Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters -Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX to the server's startup file JRServer.bat in <install_root>\bin.	  

- 
Library
  Select to use an existing image.  
    - 
My Pictures
      The My Pictures folder is a virtual location where Server stores the images that you have once inserted into reports. Select the one you want to use.

Preview

  Server displays a preview of the selected image.

OK

Select to insert the image into the report and close the dialog box.

Cancel

Select to close the dialog box without inserting an image.

Help button

Select to view information about the  dialog box.

Close button

Select to close the dialog box without inserting an image.
