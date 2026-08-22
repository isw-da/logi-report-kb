---
title: "Working with Multimedia Objects"
id: 5735564368791
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects
updated_at: 2022-11-02T04:13:15Z
---

# Working with Multimedia Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes)

# Working with Multimedia Objects

Logi Report supports the following multimedia objects: Applet, RealMedia, and Windows Media. You can use them in page report and web report areas listed in [Component Placement in Different Report Type](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type).. This topic describes how you can each of the multimedia objects in a report.

This topic contains the following sections:

* [Inserting Applet Objects in a Report](#Applet)
* [Inserting Real Media Objects in a Report](#RealMedia)
* [Inserting Windows Media Objects in a Report](#WMA)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the label component example, open `<install_root>\Demo\Reports\SampleComponents\MultimediaObject.cls`.

## Inserting Applet Objects in a Report

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You cannot use Applet in business view-based page reports.

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the object.
2. Do one of the following:
   * From the **Components** panel, drag the **Applet** icon ![Applet icon](https://devnet.logianalytics.com/hc/article_attachments/9898516838167/icon_applet.gif) in the **Others** category to the report.
   * Navigate to **Insert** > **Multimedia Objects** > **Applet**.
   * Navigate to **Home** > **Insert** > **Multimedia Objects** > **Applet**.

   Designer displays the [Applet Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513162391-Applet-Parameter-Dialog-Box).

   ![Applet Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898533287447/apltprm.gif)
3. In the **Code** text box, type the name for the class file contained in the archive file.
4. In the **Plug-in Page** text box, specify the URL from which to download JDK to run this applet. By default, it is `http://java.sun.com/products/plugin/index.html#download`.
5. Select **Browse** next to the **Archive** text box to specify the archive file (.zip or .jar), which contains the resources that can make the applet run properly.
6. Select **OK** to insert the object in the required location.

When you use a Java technology-enabled web browser to view a report that contains an applet, the applet's code will be transferred to your system and executed by the web browser's Java Virtual Machine (JVM).

To further edit the applet object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings in the Applet Parameter dialog box as required.

## Inserting RealMedia Objects in a Report

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the object.
2. Do one of the following:
   * From the **Components** panel, drag the **RealMedia File** icon ![RealMedia icon](https://devnet.logianalytics.com/hc/article_attachments/9898478171543/icon_realmedia.gif) in the **Others** category to the report.
   * Navigate to **Insert** > **Multimedia Objects** > **RealMedia File**.
   * Navigate to **Home** > **Insert** > **Multimedia Objects** > **RealMedia File**.

   Designer displays the [RealPlayer Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552527511-RealPlayer-Parameter-Dialog-Box).

   ![RealPlayer Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898478191255/rlplyrpm.gif)
3. Select **Browse** to select a RealMedia file, or type the URL of a RealMedia file in the **File Name/URL** text box.
4. In the **Plug-in Page** text box, specify the URL of the plug-in page from which to download the player used to play the media file, if the player is not available on the local disk. By default, it is `http://www.real.com/`.
5. Specify the properties for controlling the options when playing the media file in Page Report Studio or Web Report Studio.
6. Select **OK** to insert the object in the required location.

When you view the report with a web browser in which the RealPlayer plug-in has been installed, the media file plays according to your settings.

To further edit the RealMedia object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings in the RealPlayer Parameter dialog box as required.

## Inserting Windows Media Files in a Report

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the object.
2. Do one of the following:
   * From the **Components** panel, drag the **Windows Media File** icon ![Windows Media File icon](https://devnet.logianalytics.com/hc/article_attachments/9898477124631/icon_winmedia.gif) in the **Others** category to the report.
   * Navigate to **Insert** > **Multimedia Objects** >  **Windows Media File**.
   * Navigate to **Home** > **Insert** > **Multimedia Objects** > **Windows Media File**.

   Designer displays the [Windows Media Player Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567858839-Windows-Media-Player-Parameter-Dialog-Box).

   ![Windows Media Player Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898460095767/wma.gif)
3. Select **Browse** to select a Windows Media file, or type the URL of a Windows Media file in the **File Name/URL** text box.
4. In the **Plug-in Page** text box, specify the URL of the plug-in page from which to download the player used to play the media file, if the player is not available on the local disk. By default, it is `http://www.microsoft.com/Windows/MediaPlayer/`.
5. Specify the properties for controlling the options when playing the media file in Page Report Studio or Web Report Studio.
6. Select **OK** to insert the object in the required location.

When you view the report with a web browser in which the Windows Media Player plug-in has been installed, the media file plays according to your settings.

To further edit the Windows Media object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings in the Windows Media Player Parameter dialog box as required.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes)
