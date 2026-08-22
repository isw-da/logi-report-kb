---
title: "Edit Image Dialog Box Properties"
id: 4405683812119
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683812119-Edit-Image-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:15Z
---

# Edit Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683811095-Edit-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683813143-Edit-Link-Dialog-Box-Properties)

# Edit Image Dialog Box Properties

This topic describes how you can use the Edit Image dialog box to edit an image. Server displays the dialog box when you right-click an image and select **Edit** from the shortcut menu.

![Edit Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453419671/edtimg.gif)

**Image From**

Specify the source of the image file.

* **Local File**  
   Select to use an image from the local file system.
  Then, select **Browse** to locate the image file.
* **Web URL**  
   Select to use an image via URL.
  Then, specify the URL of the image file in the **Image URL** text box.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) If your Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
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

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683811095-Edit-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683813143-Edit-Link-Dialog-Box-Properties)
