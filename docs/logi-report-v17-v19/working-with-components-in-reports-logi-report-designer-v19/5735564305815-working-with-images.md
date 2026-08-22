---
title: "Working with Images"
id: 5735564305815
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images
updated_at: 2022-11-02T04:13:08Z
---

# Working with Images

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects)

# Working with Images

An image is a digital representation of a picture. Logi Report supports the following image formats: .bmp, .gif, .jpg, and .png. This topic describes how you can insert images into a report.

For the images in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report).

**To insert an image in a report**

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the image.
2. Do one of the following:
   * From the **Components** panel, drag the **Image** icon ![Image icon](https://devnet.logianalytics.com/hc/article_attachments/9898518419351/icon_image.gif) in the **Basic** category.
   * Navigate to **Insert** > **Image**.
   * Navigate to **Home** > **Insert** > **Image**.
3. In the Select an Image dialog box, select the image you want to use.
   * If you want to use an image from your local file system, use the **Look in** drop-down list to browse for the image, then select **Open**. If the image file is not in the current catalog directory, Designer prompts you to copy it to the directory.
   * If you want to use an image via URL, type the URL in the **URL** text box and select **OK**. When you save the report, Designer saves the URL information into the report template.

     ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9898419824023/criticalicon.gif) If you are in an intranet, to successfully access an image via URL, you need to add the `-DproxyHost` and `-DproxyPort` JVM options to the CLASSPATH environment variable of Designer's startup file JReport.bat in `<install_root>\bin` to specify the intranet information.
4. Select **Open** to insert the image into the destination.

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the image component example, open `<install_root>\Demo\Reports\SampleComponents\ForImage.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects)
