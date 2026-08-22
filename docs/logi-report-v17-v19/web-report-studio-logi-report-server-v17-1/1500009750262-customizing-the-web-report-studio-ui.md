---
title: "Customizing the Web Report Studio UI"
id: 1500009750262
section: "Web Report Studio Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750262-Customizing-the-Web-Report-Studio-UI
updated_at: 2021-07-24T00:47:29Z
---

# Customizing the Web Report Studio UI

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750242-Customizing-Web-Report-Studio-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777501-Page-Report-Studio)

# Customizing the Web Report Studio UI

Logi Report controls the appearance of the Web Report Studio UI by CSS files in the `<install_root>\public_html\webos\style\default` directory. This topic describes how you can edit the file **wrptstudio.css** among these CSS files to customize the Web Report Studio UI.

Via modifying the file **wrptstudio.css**, you can customize the width, height, color, font, borders, padding, and so on of the Web Report Studio window elements to design your own Web Report Studio visual effect.

* [How Wrptstudio.css Maps Web Report Studio UI Elements and CSS Declarations](#Map)
* [Editing wrptstudio.css to Customize the Web Report Studio UI](#Edit)

## How Wrptstudio.css Maps Web Report Studio UI Elements and CSS Declarations

The file wrptstudio.css contains a lot of selectors, which are mainly class selectors consisting of a dot "." followed by a class name. These selectors are the links between the Web Report Studio window elements and the style. They specify what elements are affected by the CSS declarations. You can modify or add CSS declarations for a selector or a group of selectors, or add CSS rules to customize the style of the elements.

In addition, when you hover the mouse pointer over an item on a toolbar, you can find the background color of the item changes to yellow. This is achieved by the combination of state mechanism and CSS. Web Report Studio marks element states using an 8-bit binary number which will be converted to a decimal number. You can append the decimal number to the end of the class name in a CSS selector to indicate the state of the element, for example, studioPanel\_16 means that the panels in Web Report Studio are invisible. The following table lists the most commonly used decimal numbers in wrptstudio.css and the corresponding element state:

| Decimal Number | Element State |
| --- | --- |
| 0 | Normal state. Usually not added in class names. |
| 1 | Disabled |
| 2 | Hovered |
| 3 | Usually having the same style effect as 1. For example: `.dlg_button_1, .dlg_button_3 { }` |
| 4 | Triggered |
| 6 | Triggered + Hovered |
| 16 | Invisible |

## Editing wrptstudio.css to Customize the Web Report Studio UI

1. Go to the `<install_root>\public_html\webos\style\default` directory.
2. Open wrptstudio.css with your preferred editor.
3. Find the selectors for the elements you want to customize.
4. Edit the CSS declarations for the selectors.
5. Save wrptstudio.css.
6. Run make.bat/make.sh in the `<install_root>\public_html\bin` directory with the argument "jsvm" to make the changes take effect. For example, on the Windows platform, run the command `make.bat jsvm`.
7. Open Web Report Studio by running a web report or creating a new one. You can find the UI elements appear in the style you define.

**Tip:** You can access the Developer Tools on Internet Explorer, Google Chrome, or Mozilla Firefox to get the code about how CSS is applied to the Web Report Studio window elements. To do this, open Web Report Studio, then press **F12**.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750242-Customizing-Web-Report-Studio-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777501-Page-Report-Studio)
