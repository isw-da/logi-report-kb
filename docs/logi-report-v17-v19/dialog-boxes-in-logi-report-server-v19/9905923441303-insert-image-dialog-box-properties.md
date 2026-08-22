---
title: "Insert Image Dialog Box Properties"
id: 9905923441303
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9905923441303-Insert-Image-Dialog-Box-Properties
updated_at: 2022-10-31T17:15:18Z
---

# Insert Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9905923363479-Insert-Group-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9905935179159-Insert-Summary-Column-Dialog-Box-Properties)

# This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Insert Image Dialog Box Properties

This topic describes how you can use the Insert Image dialog box to [select the image you want to use](https://devnet.logianalytics.com/hc/en-us/articles/9905923717783-Working-with-Logi-Report-Studio#InsertImage).

Server displays the dialog box when you drag **Image** in the Basic category from the Components panel to the template edit area.

![Insert Image dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905931086615/insrtimg.gif)

**Image From**

Specify the source of the image file.

* **Local File**  
   Select to use an image from the local file system.
  + **File Name**  
     Specify the path and name of the image file. You can select **Browse** to locate the image file.
* **Web URL**  
   Select to use an image via URL.
  + **File URL**  
     Specify the URL of the image file.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If your Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server startup file **JRServer.bat** in `<install_root>\bin`.
* **Library**  
   Select to use an existing image.
  + **My Pictures**  
     The My Pictures folder is a virtual location where Server stores the images that you have once inserted into reports. Select the one you want to use.

**Preview**

Server displays a preview of the selected image.

**Cancel**

Select to close the dialog box without inserting an image.

**OK**

Select to insert the image into the report and close the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905902377623/btn_lrstd_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905880426903/btn_lrstd_delete.gif)**Close button**

Select to close the dialog box without inserting an image.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9905923363479-Insert-Group-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9905935179159-Insert-Summary-Column-Dialog-Box-Properties)
