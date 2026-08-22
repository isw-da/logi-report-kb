---
title: "Insert Image Dialog Box Properties"
id: 45203905022349
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203905022349-Insert-Image-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:49Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Insert Image Dialog Box Properties 

Use the Insert Image dialog box to insert an image into the dashboard header or into the HTML component. This topic describes how to specify an image.

Server displays the dialog box when you drag Image from Toolbox in the Resources panel to the dashboard header, or select the Insert Image button  in the Insert HTML dialog box or Edit HTML dialog box. 

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
type the URL of the image file in the File URL text box.    If your Report Server is in an intranet which requires a proxy, to access an image via URL, you need to add the parameters -Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX to the server's startup file JRServer.bat in <install_root>\bin.	  

- 
Library
 Select to use an existing image.  
    - 
My Pictures
      The My Pictures folder is a virtual location where Report Server stores the images that you have once inserted into dashboards. Select the one you want to use.

Preview

Server shows a preview of the selected image.

OK

Select to insert the selected image in the dashboard header.

Cancel

Select to close the dialog box without the insertion.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without the insertion.
