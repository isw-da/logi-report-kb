---
title: "Edit Image Dialog Box Properties"
id: 28891497237901
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891497237901-Edit-Image-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:45Z
source_host: docs-report.zendesk.com
---
# 
Edit Image Dialog Box Properties

This topic describes how you can use the Edit Image dialog box to edit an image. Server displays the dialog box when you right-click an image and select Edit from the shortcut menu.

Image From 

Specify the source of the image file.

- 
Local File
  Select to use an image from the local file system.
Then, select Browse to locate the image file.   

- 
Web URL
  Select to use an image via URL.
Then, specify the URL of the image file in the Image URL text box.   If your Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters -Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX to the server's startup file JRServer.bat in <install_root>\bin.
	  

- 
Library
 Select to use an existing image.
    - 
My Pictures
      The My Pictures folder is a virtual location where Server stores the images that you have once inserted into reports. Select the image you want to use.

Preview

  Server displays a preview of the selected image.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
