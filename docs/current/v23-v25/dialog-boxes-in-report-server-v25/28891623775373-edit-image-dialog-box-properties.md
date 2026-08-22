---
title: "Edit Image Dialog Box Properties"
id: 28891623775373
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891623775373-Edit-Image-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:58Z
source_host: docs-report.zendesk.com
---
# 
Edit Image Dialog Box Properties 

You can use the Edit Image dialog box to select another image to replace the current one. This topic describes the properties in the dialog box.

Server displays the dialog box when you hover over an image in the dashboard header and then select the Edit button  that displays around the image. 

Image From 

Select the source of the image file.

- 
Local File
  Select to use an image from the local file system. Then, 
select Browse to locate the image file. 
 

- 
Web URL
 Select to use an image via URL.
Then, 
type the URL of the image file in the File URL text box.      If your Report Server is in an intranet which requires a proxy, to access an image via URL, you need to add the parameters -Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX to the server's startup file JRServer.bat in <install_root>\bin.	  

- 
Library
  Select to use an existing image.  
    - 
My Pictures
      The My Pictures folder is a virtual location where Report Server stores the images that you have once inserted into dashboards. Select the one you want to use.

Preview

  Server shows a preview of the selected image.

OK

Select to use the selected image to replace the current image.

Cancel

Select to close the dialog box without doing anything.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without doing anything.
