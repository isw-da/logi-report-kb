---
title: "Button Properties"
id: 1500009669461
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669461-Button-Properties
updated_at: 2021-07-24T20:55:14Z
---

# Button Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669441-Bottom-N)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669481-Chart-Definition)

# Button Properties

The Button Properties dialog helps you to modify the properties of a button in a navigation control.

**Button Type**

* [Button](#Button)  
   The button is displayed as a normal button.
* [Image Button](#Image)  
   The button is displayed as an image.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Button

When Button is selected as the button type, the following options are available. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920644631/btnprpty_btn.gif)

**Button Label**

Specifies the properties of the button label.

* **Text**Specifies the text of the label.
* **Font**Specifies the font face of the text.
* **Font Style**  
   Specifies the font style of the text.
* **Font Size**Specifies the font size of the text.
* **Align**  
   Specifies the alignment way of the label in the button.
* **Font Color**  
   Specifies the font color of the text.

**Border**

Specifies the properties of the button border.

* **Color**  
   Specifies the border color.
* **Thickness**  
   Specifies the border width in inches.
* **Top Line**  
   Specifies the style of the top border line.
* **Bottom Line**  
   Specifies the style of the bottom border line.
* **Left Line**  
   Specifies the style of the left border line.
* **Right Line**  
   Specifies the style of the right border line.

**Button Body**

Specifies the properties of the button body.

* **Background**Specifies the background color of the button body.

  To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009645662-Select-Color) dialog and then specify a new color, or input a color string in the format #RRGGBB. If you want to make the background transparent, input Transparent in the text box.
* **Width**  
   Specifies the width of the button in inches.
* **Height**  
   Specifies the height of the button in inches.
* **Position**  
   Displays the position mode of the button. If the button is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.
  + **Absolute**: The button's position will be decided by its X and Y property values.
  + **Static**: The button will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.
* **X**  
   Specifies the X coordinate of the button, in inches.
* **Y**  
   Specifies the Y coordinate of the button, in inches.

**Preview**

Displays a preview of the button according to the button properties.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Image Button

When Button Image is selected as the button type, the following options are available. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920644887/btnprpty_img.gif)

**Image From**

Specifies the source of the image file.

* **Local File**  
   Specifies to use an image from the local file system. The types and size of the images that can be used are defined by the administrator on the Logi JReport Administration > Configuration > Upload page.
  + **File Name**  
     Specifies the path and name of the image file. You can select the Browse button to locate the image file.
* **Web URL**  
   Specifies to use an image via URL.
  + **Image URL**  
     Specifies the URL of the image file. Logi JReport will record the latest 10 entered URLs in the drop-down list.

  **Note:** If your Logi JReport Server is in an intranet, to successfully access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file JRServer.bat, which locates in `<install_root>\bin`.
* **Library**  
   Specifies to use an existing image.
  + **My Images**  
     The My Images folder is a virtual location where Logi JReport Server stores the images that have once been inserted into reports. Select the one you want to use.
  + **Preview**  
     Displays a preview of the selected image.

**OK**

Applies the button properties and closes this dialog.

**Cancel**

Cancels the changes and closes this dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669441-Bottom-N)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669481-Chart-Definition)
