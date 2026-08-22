---
title: "Customizing the JDashboard UI"
id: 28891490564109
section: "Introduction to the JDashboard and Visual Analysis Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891490564109-Customizing-the-JDashboard-UI
updated_at: 2026-02-26T02:11:24Z
source_host: docs-report.zendesk.com
---
# 
Customizing the JDashboard UI 

Report controls the appearance of the JDashboard UI by CSS files. This topic describes how you can use dashboard.css to design your own JDashboard visual effect.

After determining which theme you would like to apply to JDashboard, you can customize the appearance of your JDashboard UI by modifying the file dashboard.css in the <install_root>\public_html\webos\style\theme-name directory, to change the JDashboard window elements in ways like the width, height, color, font, borders, and padding. 

This topic contains the following sections:

- Mapping JDashboard UI Elements and CSS Declarations in Dashboard.css

- Editing Dashboard.css to Customize the JDashboard UI

## 
Mapping JDashboard UI Elements and CSS Declarations in Dashboard.css

The file dashboard.css contains a lot of selectors, which are mainly class selectors consisting of a dot "." followed by a class name. These selectors are the links between the JDashboard window elements and the style. They specify what elements are affected by the CSS declarations. You can modify or add CSS declarations for a selector or a group of selectors, or add CSS rules to customize the style of the elements. 

In addition, when you hover the mouse pointer over an item in the Resources panel, you can find the background color of the item changes to yellow. A disabled button has lighter color than a working button. JDashboard achieves this by the combination of state mechanism and CSS. JDashboard marks element states using an 8-bit binary number and will convert it to a decimal number. You can append the decimal number to the end of the class name in a CSS selector to indicate the state of the element, for example, taskbar_16 means that the dashboard title bar is invisible. The following table lists the most commonly used decimal numbers in dashboard.css and the corresponding element states:

| Decimal Number | Element State |
| --- | --- |
| 0 | Normal state. Usually, you need not add 0 in class names. |
| 1 | Disabled |
| 2 | Hovered |
| 3 | Usually having the same style effect as 1. For example: .dlg_button_1, .dlg_button_3 { } |
| 4 | Triggered |
| 6 | Triggered and hovered |
| 16 | Invisible |

## 
Editing Dashboard.css to Customize the JDashboard UI

- In JDashboard specify the theme you want to use, for example, Green.

- Go to the <install_root>\public_html\webos\style\theme-name directory, for example <install_root>\public_html\webos\style\green.

- Open dashboard.css with an editor.

- Find the selectors for the elements you want to customize.

- Edit the CSS declarations for the selectors.

- Save dashboard.css.

- Run make.bat/make.sh in the <install_root>\public_html\bin directory with the argument jsvm to make the changes take effect. For example, on the Windows platform, run the command make.bat jsvm. 

- Refresh the current JDashboard window. You can find the UI elements appear in the style you define.

Tip: You can access Developer Tools on Google Chrome or Mozilla Firefox to get the code about how JDashboard applies CSS to the window elements. To do this, open JDashboard by running a dashboard or creating a new dashboard, then press F12.
