---
title: "Button Properties"
id: 1500009771981
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771981-Button-Properties
updated_at: 2021-07-24T00:49:21Z
---

# Button Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744082-Bottom-N-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744102-Chart-Definition-Dialog-Box-Properties)

# Button Properties

You can use the Button Properties dialog box to modify the properties of a button in a navigation control. This topic describes the options in the dialog box.

The dialog box varies according to the button type:

* [Button](#Button)  
  Displays the button as a normal button.
* [Image Button](#Image)  
  Displays the button as an image.

## Button

When you select **Button** as the button type, Studio displays the following options.

![Button Properties dialog - Button](https://devnet.logianalytics.com/hc/article_attachments/4404880555287/btnprpty_btn.gif)

**Button Label**

Specifies the properties of the button label.

* **Text**  
   Specifies the text of the label.
* **Font**  
   Specifies the font face of the text.
* **Font Style**  
   Specifies the font style of the text.
* **Font Size**  
   Specifies the font size of the text.
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

* **Background**  
   Specifies the background color of the button body.

  To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type **Transparent** in the text box.
* **Width**  
   Specifies the width of the button in inches.
* **Height**  
   Specifies the height of the button in inches.
* **Position**
Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

+ **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
+ **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

* **X**  
   Specifies the X coordinate of the button, in inches.
* **Y**  
   Specifies the Y coordinate of the button, in inches.

**Preview**

Displays a preview of the button according to the button properties.

## Image Button

When you select **Image Button** as the button type, Studio displays the following options.

![Button Properties dialog - Image Button](https://devnet.logianalytics.com/hc/article_attachments/4404880555543/btnprpty_img.gif)

**Image From**

Specifies the source of the image file.

* **Local File**  
   Specifies to use an image from the local file system. Administrators can define the types and size of the images that can be used, in the Administration > Configuration > Upload page in the Logi Report Server console.
  + **File Name**  
     Specifies the path and name of the image file. You can select the **Browse** button to locate the image file.
* **Web URL**  
   Specifies to use an image via URL.
  + **Image URL**  
     Specifies the URL of the image file. Logi Report will record the latest 10 entered URLs in the drop-down list.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If your Logi Report Server is in an intranet, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file JRServer.bat, which is in `<install_root>\bin`.
* **Library**  
   Specifies to use an existing image.
  + **My Images**  
     The **My Images** folder is a virtual location where Logi Report Server stores the images that have once been inserted into reports. Select the one you want to use.
  + **Preview**  
     Displays a preview of the selected image.

**OK**

Applies the button properties and closes this dialog box.

**Cancel**

Cancels the changes and closes this dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744082-Bottom-N-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744102-Chart-Definition-Dialog-Box-Properties)
