---
title: "Customizing the Web Report Studio UI"
id: 1500009692902
section: "Web Report Studio Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692902-Customizing-the-Web-Report-Studio-UI
updated_at: 2021-11-03T06:56:25Z
---

# Customizing the Web Report Studio UI

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719321-Customizing-Web-Report-Studio-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718101-Page-Report-Studio)

# Customizing the Web Report Studio UI

The appearance of the Web Report Studio UI is controlled by CSS files stored in the `<install_root>\public_html\webos\style\default` directory. By modifying the file wrptstudio.css among these CSS files, you can customize the width, height, color, font, borders, padding and so on of the Web Report Studio window elements to design your own Web Report Studio visual effect.

The following diagram shows the Web Report Studio window elements that can be customized:

![JDashboard Window Elements](https://devnet.logianalytics.com/hc/article_attachments/4412131374871/wbrpt_ui_wndw.gif)

In wrptstudio.css, the selectors are mainly class selectors which consist of a dot "." followed by a class name. Selectors are the links between the Web Report Studio window elements and the style. They specify what elements are affected by the CSS declarations. You can modify or add CSS declarations for a selector or a group of selectors or add CSS rules. After editing wrptstudio.css, you need to run make.bat/make.sh in the `<install_root>\public_html\bin` directory with the argument "jsvm" to make the changes work (take the Windows platform as an example, run the command `make.bat jsvm`).

The following table shows the mapping relationship between the window elements and the class names in the class selectors in wrptstudio.css.

| Web Report Studio Window Element | Class Name in wrptstudio.css |
| --- | --- |
| Web Report Studio container | wrptstudio\_app |
| Standard toolbar | wrptToolbar |
| Visualization toolbar | wrptVToolbar |
| Resources panel | studioPanel topPanel |
| Components panel | studioPanel |
| Parameters panel | studioPanel |
| Filter panel | studioPanel |
| "Go To" Filter panel | studioPanel |
| Panel title bar | studioPanel\_title |
| Panel body | studioPanel\_client |
| Report editing area | wrptstudio\_workspace |

In addition, when you hover the mouse pointer over an item on a toolbar, you can find the background color of the item changes to yellow. This is achieved by the combination of state mechanism and CSS. Logi JReport marks element states using an 8-bit binary number which will be converted to a decimal number. The decimal number is appended to the end of the class name in a CSS selector to indicate the state of the element, for example, studioPanel\_16 means that the panels in Web Report Studio are invisible. The following table lists the most commonly used decimal numbers in wrptstudio.css and the corresponding element state:

| Decimal Number | Element State |
| --- | --- |
| 0 | Normal state. Usually not added in class names. |
| 1 | Disabled |
| 2 | Hovered |
| 3 | Usually having the same style effect as 1. For example: `.dlg_button_1, .dlg_button_3 { }` |
| 4 | Triggered |
| 6 | Triggered + hovered |
| 16 | Invisible |

**Tip:** You can access Developer Tools on Internet Explorer, Google Chrome or Mozilla Firefox to get the code about how CSS is applied to the Web Report Studio window elements. To do this, access Web Report Studio by running a web report or creating a new one, then press **F12**.

![Developer Tools](https://devnet.logianalytics.com/hc/article_attachments/4412139482391/wbrpt_ui_devtl.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719321-Customizing-Web-Report-Studio-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718101-Page-Report-Studio)
