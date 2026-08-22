---
title: "Insert Image Dialog Box Properties"
id: 1500009747622
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747622-Insert-Image-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:17Z
---

# Insert Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775981-Insert-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747642-Insert-Link-Dialog-Box-Properties)

# Insert Image Dialog Box Properties

This topic describes how you can use the Insert Image dialog box to select the image you want to use in a report.

Server displays the dialog box in the following cases:

* Drag **Image** from the **Components** panel to a report.
* Select ![Insert Image](https://devnet.logianalytics.com/hc/article_attachments/4404880145687/btn_chsr2.gif) on the **Page** screen of the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776601-Web-Report-Wizard-Properties#Page).
* Select **Customized** in the **Value Pointer** or **Target Pointer** drop-down list in the [Format Bar Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009747162-Format-Bar-Gauge-Dialog-Box-Properties), [Format Dial Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009775481-Format-Dial-Gauge-Dialog-Box-Properties), or [Format Solid Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009747382-Format-Solid-Gauge-Dialog-Box-Properties) dialog box.
* Select **Customized** in the **Value Pointe**r drop-down list in the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500009748122-Style-List-Dialog-Box-Properties) dialog box.

![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885337367/insrtimg.gif)

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
     The My Pictures folder is a virtual location where Logi Report Server stores the images that have once been inserted into reports. Select the one you want to use.

**Preview**

Displays a preview of the selected image.

**OK**

Inserts the image into the report and closes the dialog box.

**Cancel**

Cancels the insertion and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775981-Insert-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747642-Insert-Link-Dialog-Box-Properties)
