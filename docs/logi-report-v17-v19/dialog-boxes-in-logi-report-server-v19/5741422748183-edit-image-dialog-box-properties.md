---
title: "Edit Image Dialog Box Properties"
id: 5741422748183
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741422748183-Edit-Image-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:20Z
---

# Edit Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741444498967-Edit-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741434764823-Edit-Link-Dialog-Box-Properties)

# Edit Image Dialog Box Properties

This topic describes how you can use the Edit Image dialog box to edit an image. Server displays the dialog box when you right-click an image and select **Edit** from the shortcut menu.

![Edit Image dialog](https://devnet.logianalytics.com/hc/article_attachments/9905631310999/edtimg.gif)

**Image From**

Specify the source of the image file.

* **Local File**  
   Select to use an image from the local file system.
  Then, select **Browse** to locate the image file.
* **Web URL**  
   Select to use an image via URL.
  Then, specify the URL of the image file in the **Image URL** text box.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If your Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
* **Library**  
   Select to use an existing image.
  + **My Pictures**  
     The My Pictures folder is a virtual location where Server stores the images that you have once inserted into reports. Select the image you want to use.

**Preview**

Server displays a preview of the selected image.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741444498967-Edit-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741434764823-Edit-Link-Dialog-Box-Properties)
