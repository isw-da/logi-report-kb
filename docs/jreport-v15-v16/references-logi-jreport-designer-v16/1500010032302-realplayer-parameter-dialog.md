---
title: "RealPlayer Parameter Dialog"
id: 1500010032302
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010032302-RealPlayer-Parameter-Dialog
updated_at: 2021-07-24T10:38:27Z
---

# RealPlayer Parameter Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067541-Rank-Expert-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032262-Receive-Message-Dialog)

# RealPlayer Parameter Dialog

The RealPlayer Parameter dialog helps you to [insert a RealMedia file](https://devnet.logianalytics.com/hc/en-us/articles/1500010029162-Multimedia-Objects#RealMedia) into a report. It appears when you select Insert > Multimedia > RealMedia File, or drag the RealMedia File button ![RealMedia button](https://devnet.logianalytics.com/hc/article_attachments/4404901184535/btn_realmedia.gif)from the Components panel to a report.

![RealPlayer Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909159191/rlplyrpm.gif)

The following are details about options in the dialog:

**File Name/URL**

Specifies the name or the URL of the media file.

**Plug-in Page**

Specifies the URL of the plug-in page from which you can download the player with which to play the media file, if it isn't already installed on your local disk.

**Properties**

Specifies properties for the media file to control the options when playing the media file.

* **Auto Start**  
   Specifies whether to start the media file automatically when the report is opened in Page Report Studio or Web Report Studio.
* **Center**  
   Specifies whether to place the presentation in the center of the image window and display it in its original size (the size is determined by the Width and Height properties of the multimedia object in the Report Inspector).
* **Loop**  
   Specifies whether to play the media file repeatedly.
* **Loop Number**  
   Specifies the number of the times the media file will loop during playback.

  **Note:** If you have checked the Loop option and specified the Loop Number at the same time, the media file will be played back according to the specified number, which means the Loop option will be ignored even though the loop number is set to zero.
* **Show Controls**  
   Specifies the RealPlayer controls you want to show, which support specific RealPlayer functionality. The controls will be reproduced in the report as they appear in RealPlayer.
  + **All Controls**  
     Specifies whether to show all controls. When it is checked, all the following controls will be selected automatically.
  + **Pause Button**  
     Specifies whether to show the Pause Button.
  + **Play Button**  
     Specifies whether to show the Play Button.
  + **Stop Button**  
     Specifies whether to show the Stop Button.
  + **Control Panel**  
     Specifies whether to show the Control Panel, which contains the following playback controls: Play Button, Pause Button, Stop Button, Fast-forward Button, Rewind Button, Position Slider and Home Button.
  + **Fast-forward Button**  
     Specifies whether to show the Fast-forward Button.
  + **Home Control**  
     Specifies whether to show the Home Button, which is connected to the [www.real.com](http://www.real.com) website.
  + **Image Window**  
    Specifies whether to show the Image Window, which is used for displaying presentations.
  + **Information Panel**  
     Specifies whether to show the Information Panel that displays the title, author, and copyright for the currently playing clip.
  + **Volume Information**  
     Specifies whether to show the Information/Volume Bar, which consists of the Information Panel and the Mute/Volume Bar.
  + **Mute Button and Volume Slider**  
     Specifies whether to show the Mute Button and Volume Slider. If checked, the Volume Slider and Mute checkboxes will be checked correspondingly. Otherwise, you can check Volume Slider or Mute respectively.
  + **Position Field**  
     Specifies whether to show the Position Field, which shows the position of the current clip that identifies the clip's current place within the presentation timeline and the total clip length.
  + **Position Slider**  
     Specifies whether to show the Position Slider, which shows the currently playing position within the clip.
  + **Rewind Button**  
     Specifies whether to show the Rewind Button.
  + **Status Bar**  
     Specifies whether to show the Status Bar, which consists of a text message area, the network congestion LED, and the current clip position indicator.
  + **Status Field**  
     Specifies whether to show the Status Field, which consists only of a text message area.
  + **Information Field**  
     Specifies whether to show the Information Field, which displays the title, author, and copyright for the currently playing clip or portion of a multi-clip.

**OK**

Accepts all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067541-Rank-Expert-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032262-Receive-Message-Dialog)
