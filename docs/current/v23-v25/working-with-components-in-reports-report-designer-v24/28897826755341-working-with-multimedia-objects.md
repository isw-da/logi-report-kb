---
title: "Working with Multimedia Objects"
id: 28897826755341
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897826755341-Working-with-Multimedia-Objects
updated_at: 2024-09-30T09:13:26Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Working with Multimedia Objects

Report supports the following multimedia objects: Applet, RealMedia, and Windows Media. You can use them in page report and web report areas listed in Component Placement in Different Report Type.. This topic describes how you can each of the multimedia objects in a report.

This topic contains the following sections:

- Inserting Applet Objects in a Report

- Inserting Real Media Objects in a Report

- Inserting Windows Media Objects in a Report

See an example: The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the label component example, open <install_root>\Demo\Reports\SampleComponents\MultimediaObject.cls.

## 
Inserting Applet Objects in a Report 

 You cannot use Applet  in business view-based page reports.

- Position the mouse pointer at the allowed report location where you want to insert the object.				 

- Do one of the following:
    
- From the Components panel, drag the Applet icon   in the Others category to the report.

- Navigate to Insert > Multimedia Objects > Applet.

- Navigate to Home > Insert > Multimedia Objects > Applet.

Designer displays the Applet Parameter dialog box.

- In the Code text box, type the name for the class file contained in the archive file.

- In the Plug-in Page text box, specify the URL from which to download JDK to run this applet. By default, it is http://java.sun.com/products/plugin/index.html#download.

- Select Browse next to the Archive text box to specify the archive file (.zip or .jar), which contains the resources that can make the applet run properly. 

- Select OK to insert the object in the required location.

When you use a Java technology-enabled web browser to view a report that contains an applet, the applet's code will be transferred to your system and executed by the web browser's Java Virtual Machine (JVM).

To further edit the applet object, right-click it and select Edit WebOLEObject from the shortcut menu, then edit the settings in the Applet Parameter dialog box as required.

## 
Inserting RealMedia Objects in a Report 

- Position the mouse pointer at the allowed report location where you want to insert the object.				 

- Do one of the following:
    
- From the Components panel, drag the RealMedia File icon    in the Others category to the report.

- Navigate to Insert > Multimedia Objects > RealMedia File.

- Navigate to Home > Insert > Multimedia Objects > RealMedia File.

Designer displays the RealPlayer Parameter dialog box.    

- Select Browse to select a RealMedia file, or type the URL of a RealMedia file in the File Name/URL text box.

- In the Plug-in Page text box, specify the URL of the plug-in page from which to download the player used to play the media file, if the player is not available on the local disk. By default, it is http://www.real.com/.

- Specify the properties for controlling the options when playing the media file in Page Report Studio or Web Report Studio.

- Select OK to insert the object in the required location.

When you view the report with a web browser in which the RealPlayer plug-in has been installed, the media file  plays according to your settings.

To further edit the RealMedia object, right-click it and select Edit WebOLEObject from the shortcut menu, then edit the settings in the RealPlayer Parameter dialog box as required.

## 
Inserting Windows Media Files in a Report 

- Position the mouse pointer at the allowed report location where you want to insert the object.				 

- Do one of the following:
    
- From the Components panel, drag the Windows Media File icon  in the Others category to the report.

- Navigate to Insert > Multimedia Objects >  Windows Media File.

- Navigate to Home > Insert > Multimedia Objects > Windows Media File.

Designer displays the Windows Media Player Parameter dialog box.

- Select Browse to select a Windows Media file, or type the URL of a Windows Media file in the File Name/URL text box.

- In the Plug-in Page text box, specify the URL of the plug-in page from which to download the player used to play the media file, if the player is not available on the local disk. By default, it is http://www.microsoft.com/Windows/MediaPlayer/.

- Specify the properties for controlling the options when playing the media file in Page Report Studio or Web Report Studio.

- Select OK to insert the object in the required location.

When you view the report with a web browser in which the Windows Media Player plug-in has been installed, the media file plays according to your settings.

To further edit the Windows Media object, right-click it and select Edit WebOLEObject from the shortcut menu, then edit the settings in the Windows Media Player Parameter dialog box as required.

Previous Topic  Next Topic
