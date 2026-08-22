---
title: "RealPlayer Parameter Dialog Box"
id: 4405661691159
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661691159-RealPlayer-Parameter-Dialog-Box
updated_at: 2022-01-27T20:35:48Z
---

# RealPlayer Parameter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664556055-Rank-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664556951-Receive-Message-Dialog-Box)

# RealPlayer Parameter Dialog Box

You can use the RealPlayer Parameter dialog box to [insert a RealMedia file](https://devnet.logianalytics.com/hc/en-us/articles/4405661390743-Working-with-Multimedia-Objects#RealMedia) into a report. This topic describes the options in the dialog box.

Designer displays the RealPlayer Parameter dialog box when you navigate to Insert > Multimedia > RealMedia File, or drag the RealMedia File icon ![RealMedia button](https://devnet.logianalytics.com/hc/article_attachments/4420550866199/icon_realmedia.gif) from the Components panel to a report.

![RealPlayer Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542104471/rlplyrpm.gif)

You see the following options in the dialog box:

**File Name/URL**

Specify the name or URL of the media file. You can select **Browse** to specify a RealMedia file or type the URL of a RealMedia file in the text box.

**Plug-in Page**

Specify the URL of the plug-in page from which to download the player used to play the media file, if the player is not available on the local disk.

**Properties**

You can specify properties of the media file to control the options when playing the media file in this box.

* **Auto Start**  
  Select to start the media file automatically when users run the report on Server.
* **Center**  
  Select to place the presentation in the center of the image window and display it in its original size (the size is determined by the Width and Height properties of the multimedia object in the Report Inspector).
* **Loop**  
  Select to play the media file repeatedly.
* **Loop Number**  
  Specify the number of the times to loop the media file during playback.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you select the Loop option and specify the Loop Number at the same time, Loop Number takes effect at runtime, which means the media file will play back according to the specified number even if the loop number is 0, regardless whether you select Loop or not.
* **Show Controls**  
  You can specify the RealPlayer controls you want to show in this panel, which support specific RealPlayer functionality. Server reproduces the controls in the report at runtime as they appear in RealPlayer.
  + **All Controls**  
    Select to show all controls. Designer selects all the following controls automatically when you select this option.
  + **Pause Button**  
    Select to show the Pause Button.
  + **Play Button**  
    Select to show the Play Button.
  + **Stop Button**  
    Select to show the Stop Button.
  + **Control Panel**  
    Select to show the Control Panel, which contains the following playback controls: Play Button, Pause Button, Stop Button, Fast-forward Button, Rewind Button, Position Slider, and Home Button.
  + **Fast-forward Button**  
    Select to show the Fast-forward Button.
  + **Home Control**  
    Select to show the Home Button, which connects to the [www.real.com](http://www.real.com) website.
  + **Image Window**  
    Select to show the Image Window, which is used for displaying presentations.
  + **Information Panel**  
    Select to show the Information Panel that displays the title, author, and copyright for the currently playing clip.
  + **Volume Information**  
    Select to show the Information/Volume Bar, which consists of the Information Panel and the Mute/Volume Bar.
  + **Mute Button and Volume Slider**  
    Select to show the Mute Button and Volume Slider. Designer selects the Volume Slider and Mute options correspondingly when you select this option; otherwise, you can select Volume Slider or Mute respectively.
  + **Position Field**  
    Select to show the Position Field, which shows the position of the current clip that identifies the clip's current place within the presentation timeline and the total clip length.
  + **Position Slider**  
    Select to show the Position Slider, which shows the currently playing position within the clip.
  + **Rewind Button**  
    Select to show the Rewind Button.
  + **Status Bar**  
    Select to show the Status Bar, which consists of a text message area, the network congestion LED, and the current clip position indicator.
  + **Status Field**  
    Select to show the Status Field, which consists only of a text message area.
  + **Information Field**  
    Select to show the Information Field, which displays the title, author, and copyright for the currently playing clip or portion of multiple clips.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664556055-Rank-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664556951-Receive-Message-Dialog-Box)
