---
title: "Edit Image Dialog Box Properties"
id: 1500009775161
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775161-Edit-Image-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:30Z
---

# Edit Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775141-Edit-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775181-Edit-Link-Dialog-Box-Properties)

# Edit Image Dialog Box Properties

This topic describes how you can use the Edit Image dialog box to edit an image. Server displays the dialog box when you right-click an image and select **Edit** from the shortcut menu.

![Edit Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885329431/edtimg.gif)

**Image From**

Specifies the source of the image file.

* **Local File**  
   Specifies to use an image from the local file system.
  + **File Name**  
     Specifies the path and name of the image file. You can select Browse button to locate the image file.
* **Web URL**  
   Specifies to use an image via URL.
  + **Image URL**  
     Specifies the URL of the image file.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If your Logi Report Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
* **Library**  
   Specifies to use an existing image.
  + **My Images**  
     The My Images folder is a virtual location where Logi Report Server stores the images that have once been inserted into reports. Select the one you want to use.

**Preview**

Displays a preview of the selected image.

**OK**

Applies the settings and closes the dialog box.

**Cancel**

Cancels the changes and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775141-Edit-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775181-Edit-Link-Dialog-Box-Properties)
