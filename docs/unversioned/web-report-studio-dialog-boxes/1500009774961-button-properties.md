---
title: "Button Properties"
id: 1500009774961
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009774961-Button-Properties
updated_at: 2021-07-24T00:48:34Z
---

# Button Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774901-Bind-Data-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746902-Category-Options-Dialog-Box-Properties)

# Button Properties

This topic describes how you can use the Button Properties dialog box to update the properties of a button. Server displays the dialog box when you right-click a button in a navigation control and select **Properties** from the shortcut menu.

The dialog box properties vary with the button type:

* [Button](#Button)  
  Select if you want to display the button as a normal button.
* [Image Button](#Image)  
  Select if you want to display the button as an image.

## Button Properties

When you selected **Button** as the button type, you see the following options.

![Button Properties dialog - Button](https://devnet.logianalytics.com/hc/article_attachments/4404880403991/btnprpty_btn.gif)

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
   Specifies the border width.
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

  To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.
* **Width**  
   Specifies the width of the button.
* **Height**  
   Specifies the height of the button.

**Preview**

Displays a preview of the button according to the button properties.

## Image Button Properties

When you selected **Button Image** as the button type, you see the following options.

![Button Properties dialog - Image Button](https://devnet.logianalytics.com/hc/article_attachments/4404885494551/btnprpty_img.gif)

**Image From**

Specifies the source of the image file.

* **Local File**  
   Specifies to use an image from the local file system.
  + **File Name**  
     Specifies the path and name of the image file. You can select the Browse button to locate the image file.
* **Web URL**  
   Specifies to use an image via URL.
  + **Image URL**  
     Specifies the URL of the image file. Logi Report will record the latest 10 entered URLs in the drop-down list.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If your Logi Report Server is in an intranet, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
* **Library**  
   Specifies to use an existing image.
  + **My Images**  
     The My Images folder is a virtual location where Logi Report Server stores the images that have once been inserted into reports. Select the one you want to use.

**Preview**

Displays a preview of the selected image.

**OK**

Applies the button properties and closes this dialog box.

**Cancel**

Cancels the changes and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774901-Bind-Data-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746902-Category-Options-Dialog-Box-Properties)
