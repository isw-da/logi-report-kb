---
title: "Working with Multimedia Objects"
id: 1500010094821
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094821-Working-with-Multimedia-Objects
updated_at: 2021-07-23T19:14:48Z
---

# Working with Multimedia Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094761-Working-with-Images)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094981-Working-with-Text-Boxes)

# Working with Multimedia Objects

Logi Report supports the following multimedia objects: Applet, Flash, RealMedia, and Windows Media. You can use them in page report and web report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship). This topic describes how you can each of the multimedia objects in a report.

This topic contains the following sections:

* [Inserting Applet Objects in a Report](#Applet)
* [Inserting Flash Objects in a Report](#Flash)
* [Inserting Real Media Objects in a Report](#RealMedia)
* [Inserting Windows Media Objects in a Report](#WMA)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the label component example, open `<install_root>\Demo\Reports\SampleComponents\MultimediaObject.cls`.

## Inserting Applet Objects in a Report

Applet is not supported in page reports created using business views.

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * From the **Components** panel, drag the **Applet** icon ![Applet button](https://devnet.logianalytics.com/hc/article_attachments/4404857040791/btn_applet.gif) in the Others category to the report.
   * Select **Insert** > **Multimedia Objects** > **Applet**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **Applet**.

   Designer displays the [Applet Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095601-Applet-Parameter-Dialog-Box).

   ![Applet Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857011991/apltprm.gif)
3. Type the code for this applet in the **Code** text box.
4. In the **Plug-in Page** text box, set the URL of the plug-in page. By default, it is `http://java.sun.com/products/plugin/index.html#download`.
5. Select the **Browse** button next to the **Archive** text box to specify the archive file (.zip or .jar).
6. Select **OK** to insert the object in the required location.

When you use a Java technology-enabled web browser to view a report that contains an applet, the applet's code will be transferred to your system and executed by the web browser's Java Virtual Machine (JVM).

To further edit the applet object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings in the Applet Parameter dialog box as required.

## Inserting Flash Objects in a Report

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * From the Components panel, drag the **Flash** icon ![Flash button](https://devnet.logianalytics.com/hc/article_attachments/4404848576663/btn_flash.gif) in the Others category to the report.
   * Select **Insert** > **Multimedia Objects** > **Flash**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **Flash**.

   Designer displays the [Flash Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096821-Flash-Parameter-Dialog-Box).

   ![Flash Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848577303/flshprm.gif)
3. Select the **Browse** button to select a flash file, or type the URL of a flash file in the **File Name/URL** text box.
4. In the **Plug-in Page** text box, set the URL of the plug-in page. By default, it is `http://www.macromedia.com/go/getflashplayer`.
5. Specify the properties so as to control the options when playing the flash file in Page Report Studio or Web Report Studio.
6. Select **OK** to insert the object in the required location.

When you view the report result with a web browser in which the Flash Player plug-in has been installed, the flash file plays according to your settings.

To further edit the flash object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings in the Flash Parameter dialog box as required.

## Inserting RealMedia Objects in a Report

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * From the **Components** panel, drag the **RealMedia File** icon ![RealMedia button](https://devnet.logianalytics.com/hc/article_attachments/4404856899479/btn_realmedia.gif) in the Others category to the report.
   * Select **Insert** > **Multimedia Objects** > **RealMedia File**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **RealMedia File**.

   Designer displays the [RealPlayer Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098441-RealPlayer-Parameter-Dialog-Box).

   ![RealPlayer Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856899735/rlplyrpm.gif)
3. Select the **Browse** button to select a RealMedia file, or type the URL of a RealMedia file in the **File Name/URL** text box.
4. In the **Plug-in Page** text box, set the URL of the plug-in page. By default, it is `http://www.real.com/`.
5. Specify the properties so as to control the options when playing the media file in Page Report Studio or Web Report Studio.
6. Select **OK** to insert the object in the required location.

When you view the report result with a web browser in which the RealPlayer plug-in has been installed, the media file plays according to your settings.

To further edit the RealMedia object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings in the RealPlayer Parameter dialog box as required.

## Inserting Windows Media Files in a Report

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * From the **Components** panel, drag the **Windows Media File** icon ![Windows Media File icon](https://devnet.logianalytics.com/hc/article_attachments/4404856881559/icon_winmedia.gif) in the Others category to the report.
   * Select **Insert** > **Multimedia Objects** >  **Windows Media File**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **Windows Media File**.

   Designer displays the [Windows Media Player Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060842-Windows-Media-Player-Parameter-Dialog-Box).

   ![Windows Media Player Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856881815/wma.gif)
3. Select the **Browse** button to select a Windows Media file, or type the URL of a Windows Media file in the **File Name/URL** text box.
4. In the **Plug-in Page** text box, set the URL of the plug-in page. By default, it is `http://www.microsoft.com/Windows/MediaPlayer/`.
5. Specify the properties so as to control the options when playing the media file in Page Report Studio or Web Report Studio.
6. Select **OK** to insert the object in the required location.

When you view the report result with a web browser in which the Windows Media Player plug-in has been installed, the media file plays according to your settings.

To further edit the Windows Media object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings in the Windows Media Player Parameter dialog box as required.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094761-Working-with-Images)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094981-Working-with-Text-Boxes)
