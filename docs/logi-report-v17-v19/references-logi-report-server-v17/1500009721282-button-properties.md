---
title: "Button Properties"
id: 1500009721282
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009721282-Button-Properties
updated_at: 2021-07-25T07:19:30Z
---

# Button Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009721222-Bind-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721462-Category-Options)

# Button Properties

The Button Properties dialog box is used to modify the properties of the button. It appears when you right-click a button in a navigation control and select Properties from the shortcut menu.

The dialog box varies according to the button type:

* [Button](#Button)  
  Displays the button as a normal button.
* [Image Button](#Image)  
  Displays the button as an image.

## Button

When Button is selected as the button type, the following options are available.

![Button Properties dialog - Button](https://devnet.logianalytics.com/hc/article_attachments/4404942556567/btnprpty_btn.gif)

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

  To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.
* **Width**  
   Specifies the width of the button.
* **Height**  
   Specifies the height of the button.

**Preview**

Displays a preview of the button according to the button properties.

## Image Button

When Button Image is selected as the button type, the following options are available.

![Button Properties dialog - Image Button](https://devnet.logianalytics.com/hc/article_attachments/4404942556823/btnprpty_img.gif)

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

  **Note:** If your Logi Report Server is in an intranet, to successfully access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file JRServer.bat, which locates in `<install_root>\bin`.
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

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009721222-Bind-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721462-Category-Options)
