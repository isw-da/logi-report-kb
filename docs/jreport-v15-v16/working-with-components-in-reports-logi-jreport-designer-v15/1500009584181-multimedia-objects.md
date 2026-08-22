---
title: "Multimedia Objects"
id: 1500009584181
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584181-Multimedia-Objects
updated_at: 2021-07-24T05:55:58Z
---

# Multimedia Objects

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583961-Images)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563762-Text-Boxes)

# Multimedia Objects

Multimedia objects, including Applet, Flash, RealMedia, and Windows Media objects can be inserted in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports#Relationship).

Multimedia objects are not supported in library components, and Applet is not supported in page reports that are created using business views.

Below is a list of the sections covered in this topic:

> * [Inserting an Applet Object](#Applet)
> * [Inserting a Flash Object](#Flash)
> * [Inserting a RealMedia Object](#RealMedia)
> * [Inserting a Windows Media Object](#WMA)

## Inserting an Applet Object

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * Drag the **Applet** button ![Applet button](https://devnet.logianalytics.com/hc/article_attachments/4404893982487/btn_applet.gif) from the Components panel to the report.
   * Select **Insert** > **Multimedia Objects** > **Applet**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **Applet**.

   The [Applet Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009564582-Applet-Parameter-Dialog) dialog appears.

   ![Applet Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893955863/apltprm.gif)
3. Type the code for this applet in the Code field.
4. In the Plug-in Page field, set the URL of the plug-in page. By default, it is `http://java.sun.com/products/plugin/index.html#download`.
5. Select the **Browse** button next to the Archive field to specify the archive file (.zip or .jar).
6. Select **OK** in the dialog to insert the object in the required location.

When you use a Java technology-enabled web browser to view a report that contains an applet, the applet's code will be transferred to your system and executed by the web browser's Java Virtual Machine (JVM).

## Inserting a Flash Object

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * Drag the **Flash** button ![Flash button](https://devnet.logianalytics.com/hc/article_attachments/4404889406871/btn_flash_26x28.gif) from the Components panel to the report.
   * Select **Insert** > **Multimedia Objects** > **Flash**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **Flash**.

   The [Flash Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009586861-Flash-Parameter-dialog-Dialog) dialog appears.

   ![Flash Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889362455/flshprm.gif)
3. Select the **Browse** button to select a flash file, or type the URL of a flash file in the File Name/URL field.
4. In the Plug-in Page field, set the URL of the plug-in page. By default, it is `http://www.macromedia.com/go/getflashplayer`.
5. Specify the properties so as to control the options when playing the flash file in Page Report Studio or Web Report Studio.
6. Select **OK** in the dialog to insert the object in the required location.

When you view the report result with a web browser in which the Flash Player plug-in has been installed, the media file will be played according to your settings.

## Inserting a RealMedia Object

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * Drag the **RealMedia File** button ![RealMedia button](https://devnet.logianalytics.com/hc/article_attachments/4404893859095/btn_realmedia.gif) from the Components panel to the report.
   * Select **Insert** > **Multimedia Objects** > **RealMedia File**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **RealMedia File**.

   The [RealPlayer Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009588441-RealPlayer-Parameter-Dialog) dialog appears.

   ![RealPlayer Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889323159/rlplyrpm.gif)
3. Select the **Browse** button to select a RealMedia file, or type the URL of a RealMedia file in the File Name/URL field.
4. In the Plug-in Page field, set the URL of the plug-in page. By default, it is `http://www.real.com/`.
5. Specify the properties so as to control the options when playing the media file in Page Report Studio or Web Report Studio.
6. Select **OK** in the dialog to insert the object in the required location.

When you view the report result with a web browser in which the RealPlayer plug-in has been installed, the media file will be played according to your settings.

## Inserting a Windows Media Object

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * Drag the **Windows Media File** button ![Windows Media File button](https://devnet.logianalytics.com/hc/article_attachments/4404889312407/btn_instwinmedia.gif) from the Components panel to the report.
   * Select **Insert** > **Multimedia Objects** >  **Windows Media File**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **Windows Media File**.

   The [Windows Media Player Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009567942-Windows-Media-Player-Parameter-Dialog) dialog appears.

   ![Windows Media Player Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889312663/wma.gif)
3. Select the **Browse** button to select a Windows Media file, or type the URL of a Windows Media file in the File Name/URL field.
4. In the Plug-in Page field, set the URL of the plug-in page. By default, it is `http://www.microsoft.com/Windows/MediaPlayer/`.
5. Specify the properties so as to control the options when playing the media file in Page Report Studio or Web Report Studio.
6. Select **OK** in the dialog to insert the object in the required location.

When you view the report result with a web browser in which the Windows Media Player plug-in has been installed, the media file will be played according to your settings.

When a multimedia object has been inserted into a report, you can further edit it if required (to do this, right-click the object and select **Edit WebOLEObject** from the shortcut menu).

**See an example:** The SampleComponents catalog, included with Logi JReport Designer, contains reports that have examples of how each component type could be used in a report. For the label component example, open `<install_root>\Demo\Reports\SampleComponents\MultimediaObject.cls`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583961-Images)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563762-Text-Boxes)
