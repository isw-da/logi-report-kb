---
title: "Edit Image Dialog Box Properties"
id: 1500009773301
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773301-Edit-Image-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:58Z
---

# Edit Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745382-Edit-HTML-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745422-Edit-Label-Dialog-Box-Properties)

# Edit Image Dialog Box Properties

You can use the Edit Image dialog box to [select another image to replace the current one](https://devnet.logianalytics.com/hc/en-us/articles/1500009771761-Creating-and-Saving-Dashboards#Image). This topic describes the options in the dialog box.

JDashboard displays the dialog box when you hover the mouse pointer on an image in the dashboard header and then select the Edit button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404885533975/btn_dshbrd_edt.gif) that JDashboard displays around the image.

![Edit Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880457367/edtimg.gif)

**Image From**

Specifies the source of the image file.

* **Local File**  
   Specifies to use an image from the local file system.
  + **File Name**  
     Specifies the path and name of the image file. You can select the Browse button to locate the image file.
* **Web URL**  
   Specifies to use an image via URL.
  + **File URL**  
     Specifies the URL of the image file.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If your Logi Report Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
* **Library**  
   Specifies to use an existing image.
  + **My Pictures**  
     The My Pictures folder is a virtual location where Logi Report Server stores the images that have once been inserted into JDashboard. Select the one you want to use.

**Preview**

Displays a preview of the selected image.

**OK**

Select **OK** to use the selected image to replace the current image.

**Cancel**

Cancels the change of the image and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745382-Edit-HTML-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745422-Edit-Label-Dialog-Box-Properties)
