---
title: "Insert Image Dialog Box Properties"
id: 1500009773481
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773481-Insert-Image-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:55Z
---

# Insert Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745502-Insert-HTML-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773501-Insert-Special-Field-Dialog-Box-Properties)

# Insert Image Dialog Box Properties

Use the Insert Image dialog box to [insert an image](https://devnet.logianalytics.com/hc/en-us/articles/1500009771761-Creating-and-Saving-Dashboards#Image) into the dashboard header or into the HTML component. This topic describes how to specify an image.

JDashboard displays the dialog box when you drag Image from Toolbox in the Resources panel to the dashboard header, or select the Insert Image button ![Insert Image button](https://devnet.logianalytics.com/hc/article_attachments/4404880443543/btn_dshbrd_img.gif) in the [Insert HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009745502-Insert-HTML-Dialog-Box-Properties) dialog box or [Edit HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009745382-Edit-HTML-Dialog-Box-Properties) dialog box.

![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880444311/insrtimg.gif)

**Image From**

Select the source of the image file.

* **Local File**  
   Select to use an image from the local file system.
  + **File Name**  
     Path and name of the image file. You can select the Browse button to locate the image file.
* **Web URL**  
   Select to use an image via URL.
  + **File URL**  
     Type the URL of the image file.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If your Logi Report Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
* **Library**  
   Select to use an existing image.
  + **My Pictures**  
     The My Pictures folder is a virtual location where Logi Report Server stores the images that have once been inserted into dashboards. Select the one you want to use.

**Preview**

Preview of the selected image.

**OK**

Select **OK** to insert the selected image in the dashboard header.

**Cancel**

Select **Cancel** to close the dialog box without the insertion.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Insert Image dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without the insertion.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745502-Insert-HTML-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773501-Insert-Special-Field-Dialog-Box-Properties)
