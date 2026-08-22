---
title: "Edit Image Dialog Box Properties"
id: 5741431983895
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741431983895-Edit-Image-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:40Z
---

# Edit Image Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741441310743-Edit-HTML-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741431999255-Edit-Label-Dialog-Box-Properties)

# Edit Image Dialog Box Properties

You can use the Edit Image dialog box to [select another image to replace the current one](https://devnet.logianalytics.com/hc/en-us/articles/5741409582359-Creating-and-Saving-Dashboards#Image). This topic describes the properties in the dialog box.

Server displays the dialog box when you hover over an image in the dashboard header and then select the Edit button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905772452759/btn_dshbrd_edt.gif) that displays around the image.

![Edit Image dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905772615063/edtimg.gif)

**Image From**

Select the source of the image file.

* **Local File**  
   Select to use an image from the local file system. Then,
  select **Browse** to locate the image file.
* **Web URL**  
   Select to use an image via URL.
  Then,
  type the URL of the image file in the **File URL** text box.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If your Logi Report Server is in an intranet which requires a proxy, to access an image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
* **Library**  
   Select to use an existing image.
  + **My Pictures**  
     The My Pictures folder is a virtual location where Logi Report Server stores the images that you have once inserted into dashboards. Select the one you want to use.

**Preview**

Server shows a preview of the selected image.

**OK**

Select to use the selected image to replace the current image.

**Cancel**

Select to close the dialog box without doing anything.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without doing anything.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741441310743-Edit-HTML-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741431999255-Edit-Label-Dialog-Box-Properties)
