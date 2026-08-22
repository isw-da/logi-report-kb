---
title: "Customizing the Web Report Studio UI"
id: 28891742396301
section: "Creating and Editing Web Reports Using Web Report Studio Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891742396301-Customizing-the-Web-Report-Studio-UI
updated_at: 2026-02-26T02:14:04Z
source_host: docs-report.zendesk.com
---
# 
Customizing the Web Report Studio UI 

Report controls the appearance of the Web Report Studio UI by CSS files in the <install_root>\public_html\webos\style\default directory. This topic describes how you can edit the file wrptstudio.css among these CSS files to customize the Web Report Studio UI.

Via modifying the file wrptstudio.css, you can customize the width, height, color, font, borders, and padding of the Web Report Studio window elements to design your own Web Report Studio visual effect. 

- How wrptstudio.css Maps Web Report Studio UI Elements and CSS Declarations

- Editing wrptstudio.css to Customize the Web Report Studio UI

## 
How wrptstudio.css Maps Web Report Studio UI Elements and CSS Declarations

The wrptstudio.css file contains a lot of selectors, which are mainly class selectors consisting of a dot "." followed by a class name. These selectors are the links between the Web Report Studio window elements and the style. They specify what elements are affected by the CSS declarations. You can modify or add CSS declarations for a selector or a group of selectors, or add CSS rules to customize the style of the elements.

In addition, when you hover the mouse pointer over an item on a toolbar, you can find the background color of the item changes to yellow. This is achieved by the combination of the state mechanism and CSS. Web Report Studio marks element states using an 8-bit binary number which will be converted to a decimal number. You can append the decimal number to the end of the class name in a CSS selector to indicate the state of the element, for example, studioPanel_16 means that the panels in Web Report Studio are invisible. The following table lists the most commonly used decimal numbers in wrptstudio.css and the corresponding element states:

| Decimal Number | Element State |
| --- | --- |
| 0 | Normal state. Usually, you need not add it in class names. |
| 1 | Disabled |
| 2 | Hovered |
| 3 | Usually having the same style effect as 1. For example: .dlg_button_1, .dlg_button_3 { } |
| 4 | Triggered |
| 6 | Triggered and Hovered |
| 16 | Invisible |

## 
Editing wrptstudio.css to Customize the Web Report Studio UI

- Go to the <install_root>\public_html\webos\style\default directory.

- Open wrptstudio.css in an editor.

- Find the selectors for the elements you want to customize.

- Edit the CSS declarations for the selectors.

- Save wrptstudio.css.

- Run make.bat/make.sh in the <install_root>\public_html\bin directory with the argument "jsvm" to make the changes take effect. For example, on the Windows platform, run the command make.bat jsvm. 

- Open Web Report Studio by running a web report or creating a new one. You can see the UI elements using the style you defined in wrptstudio.css.

Tip: You can access the Developer Tools on Google Chrome or Mozilla Firefox to get the code about how to apply CSS to the Web Report Studio window elements. To do this, open Web Report Studio, and then press F12.
