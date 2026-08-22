---
title: "Insert Image Dialog Box Properties"
id: 5741459251991
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741459251991-Insert-Image-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:36Z
---

# Insert Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741435929751-Insert-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741459269271-Insert-Link-Dialog-Box-Properties)

# Insert Image Dialog Box Properties

This topic describes how you can use the Insert Image dialog box to select the image you want to use in a web report.

Server displays the dialog box in the following cases:

* Drag **Image** from the **Components** panel to a report.
* Select the ellipsis button ![Insert Image](https://devnet.logianalytics.com/hc/article_attachments/9905577763991/btn_chsr2.gif) on the **Page** screen of the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties#Page).
* Select **Customized** from the **Value Pointer** or **Target Pointer** drop-down list in the [Format Bar Gauge](https://devnet.logianalytics.com/hc/en-us/articles/5741450135575-Format-Bar-Gauge-Dialog-Box-Properties), [Format Dial Gauge](https://devnet.logianalytics.com/hc/en-us/articles/5741444981015-Format-Dial-Gauge-Dialog-Box-Properties), or [Format Solid Gauge](https://devnet.logianalytics.com/hc/en-us/articles/5741429743767-Format-Solid-Gauge-Dialog-Box-Properties) dialog box.
* Select **Customized** in the **Value Pointer** drop-down list in the [Style List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741466876439-Style-List-Dialog-Box-Properties).

![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/9905654285335/insrtimg.gif)

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

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If your Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
* **Library**  
   Select to use an existing image.
  + **My Pictures**  
     The My Pictures folder is a virtual location where Server stores the images that you have once inserted into reports. Select the one you want to use.

**Preview**

Server displays a preview of the selected image.

**OK**

Select to insert the image into the report and close the dialog box.

**Cancel**

Select to close the dialog box without inserting an image.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without inserting an image.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741435929751-Insert-Filter-Control-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741459269271-Insert-Link-Dialog-Box-Properties)
