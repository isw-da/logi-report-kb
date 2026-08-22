---
title: "Insert Image Dialog Box Properties"
id: 1500009744722
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744722-Insert-Image-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:10Z
---

# Insert Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744682-Insert-Group-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772661-Insert-Parameter-Control-Dialog-Box-Properties)

# Insert Image Dialog Box Properties

You can use the Insert Image dialog box to select the image file to use in a report. It varies according to how you will use the image: as [an image component in a report](#Report) or [as the pointer in a gauge chart.](#Gauge) This topic describes the options in the dialog box.

---

When you open the Insert Image dialog box by selecting Menu > Insert > Image or dragging Image from the Toolbox panel into the current report, You can use it to [insert an image](https://devnet.logianalytics.com/hc/en-us/articles/1500009748902-Adding-Objects-in-Page-Report#Image) into the report and contains the following options.

![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885402135/insrtimg.gif)

**Image From**

Specifies the source of the image file.

* **Local File**  
   Specifies to use an image from the local file system. The types of the images that can be used are defined by the administrator in the Administration > Configuration > Upload page in the Server Console.
  + **File Name**  
     Specifies the path and name of the image file. You can select the Browse button to locate the image file.
* **Web URL**  
   Specifies to use an image via URL.
  + **Image URL**  
     Specifies the URL of the image file. Logi Report will record the latest 10 entered URLs in the drop-down list.
* **Library**  
   Specifies to use an existing image.
  + **My Images**  
     The My Images folder is a virtual location where Logi Report Server stores the images that have once been inserted into reports. Select the one you want to use.
  + **Preview**  
     Displays a preview of the selected image.

**OK**

Inserts the image in the report and closes the dialog box.

**Cancel**

Cancels the insertion and closes the dialog box.

**Help**

Displays the help document about this feature.

---

When you open the Insert Image dialog box by selecting Customized in the Value Pointer or Target Pointer drop-down list in the [Format Bar Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009744382-Format-Bar-Gauge-Dialog-Box-Properties), [Format Dial Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009744422-Format-Dial-Gauge-Dialog-Box-Properties), or [Format Solid Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009744562-Format-Solid-Gauge-Dialog-Box-Properties) dialog box, or in the Value Pointer drop-down list in the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/1500009773101-Style-List-Dialog-Box-Properties) dialog box, You can use it to specify an image as the pointer in a gauge chart.

![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885337367/insrtimg.gif)

**Image From**

Specifies the source of the image file.

* **Local File**  
   Specifies to use an image from the local file system.
  The types of the images that can be used are defined by the administrator in the Administration > Configuration > Upload page in the Server Console.
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
     The My Pictures folder is a virtual location where Logi Report Server stores the images that you have once inserted into reports. Select the one you want to use.

**Preview**

Displays a preview of the selected image.

**OK**

Uses the image as the pointer in the gauge chart and closes the dialog box.

**Cancel**

Cancels the operation and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744682-Insert-Group-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772661-Insert-Parameter-Control-Dialog-Box-Properties)
