---
title: "Insert Image Dialog Box Properties"
id: 4405683662743
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683662743-Insert-Image-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:44Z
---

# Insert Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683661719-Insert-Group-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683663767-Insert-Parameter-Control-Dialog-Box-Properties)

# Insert Image Dialog Box Properties

You can use the Insert Image dialog box to select a image file to use in a report. It varies according to how you will use the image: as [an image component in a report](#Report) or [as the pointer in a gauge chart.](#Gauge) This topic describes the properties in the dialog box.

---

When you open the Insert Image dialog box by selecting Menu > Insert > Image or dragging Image from the Toolbox panel into the current report, You can use it to [insert an image](https://devnet.logianalytics.com/hc/en-us/articles/4405690648471-Adding-Objects-in-Page-Report#Image) into the report.

![Insert Image dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420447163031/insrtimg.gif)

**Image From**

Specify the source of the image file.

* **Local File**  
   Select to use an image from the local file system. Admin can define the types of the images on the Administration > Configuration > Upload page on the Server Console.
  + **File Name**  
     Specify the path and name of the image file. You can select **Browse** to locate the image file.
* **Web URL**  
   Select to use an image via URL.
  + **Image URL**  
     Specify the URL of the image file. Server records the latest 10 entered URLs in the list.
* **Library**  
   Select to use an existing image.
  + **My Images**  
     The My Images folder is a virtual location where Server stores the images that you have once inserted into reports. Select the one you want to use.
  + **Preview**  
     Server displays a preview of the selected image.

**OK**

Select to insert the image in the report.

**Cancel**

Select to close the dialog box without the insertion.

**Help**

Select to view information about the dialog box.

---

When you open the Insert Image dialog box by selecting **Customized** in the Value Pointer or Target Pointer list in the [Format Bar Gauge](https://devnet.logianalytics.com/hc/en-us/articles/4405683636119-Format-Bar-Gauge-Dialog-Box-Properties), [Format Dial Gauge](https://devnet.logianalytics.com/hc/en-us/articles/4405683638423-Format-Dial-Gauge-Dialog-Box-Properties), or [Format Solid Gauge](https://devnet.logianalytics.com/hc/en-us/articles/4405683651351-Format-Solid-Gauge-Dialog-Box-Properties) dialog box, or in the Value Pointer list in the [Style List](https://devnet.logianalytics.com/hc/en-us/articles/4405690525463-Style-List-Dialog-Box-Properties) dialog box, You can use it to specify an image as the pointer in a gauge chart.

![Insert Image dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420447083415/insrtimg.gif)

**Image From**

Specify the source of the image file.

* **Local File**  
   Select to use an image from the local file system.
  Admin can define the types of the images on the Administration > Configuration > Upload page on the Server Console.
  + **File Name**  
     Specify the path and name of the image file. You can select **Browse** to locate the image file.
* **Web URL**  
   Select to use an image via URL.
  + **File URL**  
     Specify the URL of the image file.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) If your Logi Report Server is in an intranet which requires a proxy, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
* **Library**  
   Select to use an existing image.
  + **My Pictures**  
     The My Pictures folder is a virtual location where Server stores the images that you have once inserted into reports. Select the image you want to use.

**Preview**

Server displays a preview of the selected image.

**OK**

Select to use the image as the pointer in the gauge chart.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683661719-Insert-Group-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683663767-Insert-Parameter-Control-Dialog-Box-Properties)
