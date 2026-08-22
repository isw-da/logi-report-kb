---
title: "Working with Images"
id: 4405661381143
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661381143-Working-with-Images
updated_at: 2022-01-27T20:34:31Z
---

# Working with Images

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661390743-Working-with-Multimedia-Objects)

# Working with Images

An image is a digital representation of a picture. Logi Report supports the following image formats: .bmp, .gif, .jpg, and .png. This topic describes how you can insert images into a report.

For the images in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports).

**To insert an image in a report**

1. Position the mouse pointer at the destination where you want to insert the image. You can insert an image in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship).
2. Do any of the following.
   * From the **Components** panel, drag the **Image** icon ![Image icon](https://devnet.logianalytics.com/hc/article_attachments/4420550977943/icon_image.gif) in the **Basic** category.
   * Navigate to **Insert** > **Image**.
   * Navigate to **Home** > **Insert** > **Image**.
3. In the Select an Image dialog box, select the image you want to use.
   * If you want to use an image from your local file system, use the **Look in** drop-down list to browse for the image, then select **Open**. If the image file is not in the current catalog directory, Designer prompts you to copy it to the directory.
   * If you want to use an image via URL, type the URL in the **URL** text box and select **OK**. When you save the report, Designer saves the URL information into the report template.

     ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420542088087/criticalicon.gif) If you are in an intranet, to successfully access an image via URL, you need to add the parameters `-DproxyHost=XXX -DproxyPort=XX` to the batch file JReport.bat in `<install_root>\bin`.
4. Select **Open** to insert the image into the destination.

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the image component example, open `<install_root>\Demo\Reports\SampleComponents\ForImage.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661390743-Working-with-Multimedia-Objects)
