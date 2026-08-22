---
title: "Edit Image Dialog Box Properties"
id: 45203922535565
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203922535565-Edit-Image-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:45Z
source_host: logi-report-v26.insightsoftware.com
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
