---
title: "Multimedia Objects"
id: 1500009606362
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606362-Multimedia-Objects
updated_at: 2021-07-24T16:05:14Z
---

# Multimedia Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606262-Images) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606542-Text-Boxes)

# Multimedia Objects

Logi Report Designer supports the following multimedia objects: Applet, Flash, RealMedia, and Windows Media. They can be used in page report and web report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports#Relationship).

This topic includes the following sections:

* [Inserting Applet Objects in a Report](#Applet)
* [Inserting Flash Objects in a Report](#Flash)
* [Inserting Real Media Objects in a Report](#RealMedia)
* [Inserting Windows Media Objects in a Report](#WMA)

**See an example:** The SampleComponents catalog, included with Logi Report Designer, contains reports that have examples of how each component type could be used in a report. For the label component example, open `<install_root>\Demo\Reports\SampleComponents\MultimediaObject.cls`.

## Inserting Applet Objects in a Report

Applet is not supported in page reports created using business views.

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * Drag ![Applet button](https://devnet.logianalytics.com/hc/article_attachments/4404904432535/btn_applet.gif) from the Components panel to the report.
   * Select **Insert** > **Multimedia Objects** > **Applet**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **Applet**.

   The [Applet Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607282-Applet-Parameter-Dialog) dialog appears.

   ![Applet Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904395671/apltprm.gif)
3. Type the code for this applet in the Code field.
4. In the Plug-in Page field, set the URL of the plug-in page. By default, it is `http://java.sun.com/products/plugin/index.html#download`.
5. Select the **Browse** button next to the Archive field to specify the archive file (.zip or .jar).
6. Select **OK** in the dialog to insert the object in the required location.

When you use a Java technology-enabled web browser to view a report that contains an applet, the applet's code will be transferred to your system and executed by the web browser's Java Virtual Machine (JVM).

To further edit the Applet object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings In the Applet Parameter dialog as required.

## Inserting Flash Objects in a Report

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * Drag ![Flash button](https://devnet.logianalytics.com/hc/article_attachments/4404916804887/btn_flash.gif) from the Components panel to the report.
   * Select **Insert** > **Multimedia Objects** > **Flash**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **Flash**.

   The [Flash Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009631181-Flash-Parameter-dialog-Dialog) dialog appears.

   ![Flash Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916805143/flshprm.gif)
3. Select the **Browse** button to select a flash file, or type the URL of a flash file in the File Name/URL field.
4. In the Plug-in Page field, set the URL of the plug-in page. By default, it is `http://www.macromedia.com/go/getflashplayer`.
5. Specify the properties so as to control the options when playing the flash file in Page Report Studio or Web Report Studio.
6. Select **OK** in the dialog to insert the object in the required location.

When you view the report result with a web browser in which the Flash Player plug-in has been installed, the flash file will be played according to your settings.

To further edit the Flash object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings In the Flash Parameter dialog as required.

## Inserting RealMedia Objects in a Report

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * Drag ![RealMedia button](https://devnet.logianalytics.com/hc/article_attachments/4404911686295/btn_realmedia.gif) from the Components panel to the report.
   * Select **Insert** > **Multimedia Objects** > **RealMedia File**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **RealMedia File**.

   The [RealPlayer Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009633261-RealPlayer-Parameter-Dialog) dialog appears.

   ![RealPlayer Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904246423/rlplyrpm.gif)
3. Select the **Browse** button to select a RealMedia file, or type the URL of a RealMedia file in the File Name/URL field.
4. In the Plug-in Page field, set the URL of the plug-in page. By default, it is `http://www.real.com/`.
5. Specify the properties so as to control the options when playing the media file in Page Report Studio or Web Report Studio.
6. Select **OK** in the dialog to insert the object in the required location.

When you view the report result with a web browser in which the RealPlayer plug-in has been installed, the media file will be played according to your settings.

To further edit the RealMedia object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings In the RealPlayer Parameter dialog as required.

## Inserting Windows Media Files in a Report

1. Position the mouse pointer at the destination where you want to insert the object.
2. Do any of the following:
   * Drag ![Windows Media File button](https://devnet.logianalytics.com/hc/article_attachments/4404911673879/btn_instwinmedia.gif) from the Components panel to the report.
   * Select **Insert** > **Multimedia Objects** >  **Windows Media File**.
   * Select **Home** > **Insert** > **Multimedia Objects** > **Windows Media File**.

   The [Windows Media Player Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009610862-Windows-Media-Player-Parameter-Dialog) dialog appears.

   ![Windows Media Player Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904231191/wma.gif)
3. Select the **Browse** button to select a Windows Media file, or type the URL of a Windows Media file in the File Name/URL field.
4. In the Plug-in Page field, set the URL of the plug-in page. By default, it is `http://www.microsoft.com/Windows/MediaPlayer/`.
5. Specify the properties so as to control the options when playing the media file in Page Report Studio or Web Report Studio.
6. Select **OK** in the dialog to insert the object in the required location.

When you view the report result with a web browser in which the Windows Media Player plug-in has been installed, the media file will be played according to your settings.

To further edit the Windows Media object, right-click it and select **Edit WebOLEObject** from the shortcut menu, then edit the settings In the Windows Media Player Parameter dialog as required.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606262-Images) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606542-Text-Boxes)
