---
title: "Working with Images"
id: 1500010094761
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094761-Working-with-Images
updated_at: 2021-07-23T19:14:46Z
---

# Working with Images

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094821-Working-with-Multimedia-Objects)

# Working with Images

An image is a digital representation of a picture. Logi Report supports the following image formats: .bmp, .gif, .jpg, and .png. This topic describes how you can insert images into a report.

For the images in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports).

**To insert an image in a report:**

1. Position the mouse pointer at the destination where you want to insert the image. You can insert an image in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship).
2. Do any of the following.
   * From the **Components** panel, drag the **Image** icon ![Image icon](https://devnet.logianalytics.com/hc/article_attachments/4404857044247/icon_image.gif) in the Basic category.
   * Select **Insert** > **Image**.
   * Select **Home** > **Insert** > **Image**.
3. In the Select an Image dialog box, select the image you want to use.
   * If you want to use an image from your local file system, use the **Look in** drop-down list to browse for the image, then select **Open**. If the image file is not in the current catalog directory, Designer prompts you to copy it to the directory.
   * If you want to use an image via URL, type the URL in the **URL** text box and select **OK**. When you save the report, Designer saves the URL information into the report template.

     ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) If you are in an intranet, to successfully access an image via URL, you need to add the parameters `-DproxyHost=XXX -DproxyPort=XX` to the batch file JReport.bat in `<install_root>\bin`.
4. Select **Open** to insert the image into the destination.

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the image component example, open `<install_root>\Demo\Reports\SampleComponents\ForImage.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094821-Working-with-Multimedia-Objects)
