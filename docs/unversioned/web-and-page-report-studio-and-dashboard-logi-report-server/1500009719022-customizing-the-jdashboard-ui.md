---
title: "Customizing the JDashboard UI"
id: 1500009719022
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719022-Customizing-the-JDashboard-UI
updated_at: 2021-07-25T07:20:12Z
---

# Customizing the JDashboard UI

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718962-Customizing-JDashboard-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718222-Using-Visual-Analysis-to-Analyze-Data-Intuitively-and-Instantly-Logi-Report-Server-v17)

# Customizing the JDashboard UI

Logi Report controls the appearance of the JDashboard UI by CSS files. After determining which theme you would like to apply to JDashboard, you can customize the appearance of your JDashboard UI by modifying the file dashboard.css stored in the `<install_root>\public_html\webos\style\theme-name` directory among these CSS files to change the width, height, color, font, borders, padding, and so on of the JDashboard window elements. This topics describes how to use dashboard.css to design your own JDashboard visual effect.

How are JDashboard UI elements and CSS declarations mapped in dashboard.css

The file dashboard.css contains a lot of selectors, which are mainly class selectors consisting of a dot "." followed by a class name. These selectors are the links between the JDashboard window elements and the style. They specify what elements are affected by the CSS declarations. You can modify or add CSS declarations for a selector or a group of selectors, or add CSS rules to customize the style of the elements.

In addition, when you hover the mouse pointer over an item in the Resources panel, you can find the background color of the item changes to yellow. A disabled button has lighter color than a working button. These are achieved by the combination of state mechanism and CSS. JDashboard marks element states using an 8-bit binary number which will be converted to a decimal number. You can append the decimal number to the end of the class name in a CSS selector to indicate the state of the element, for example, taskbar\_16 means that the dashboard title bar is invisible. The following table lists the most commonly used decimal numbers in dashboard.css and the corresponding element state:

| Decimal Number | Element State |
| --- | --- |
| 0 | Normal state. Usually not added in class names. |
| 1 | Disabled |
| 2 | Hovered |
| 3 | Usually having the same style effect as 1. For example: `.dlg_button_1, .dlg_button_3 { }` |
| 4 | Triggered |
| 6 | Triggered + hovered |
| 16 | Invisible |

How to edit dashboard.css to customize the JDashboard UI

1. In JDashboard [specify the theme](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#Theme) you want to use, for example, Green.
2. Go to the `<install_root>\public_html\webos\style\theme-name` directory, for example `<install_root>\public_html\webos\style\green`.
3. Open dashboard.css with your preferred editor.
4. Find the selectors for the elements you want to customize.
5. Edit the CSS declarations for the selectors.
6. Save dashboard.css.
7. Run make.bat/make.sh in the `<install_root>\public_html\bin` directory with the argument "jsvm" to make the changes take effect. For example, on the Windows platform, run the command `make.bat jsvm`.
8. Refresh the current JDashboard window. You can find the UI elements appear in the style you define.

**Tip:** You can access Developer Tools on Internet Explorer, Google Chrome, or Mozilla Firefox to get the code about how CSS is applied to the JDashboard window elements. To do this, open JDashboard by running a dashboard or creating a new dashboard, then press **F12**.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718962-Customizing-JDashboard-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718222-Using-Visual-Analysis-to-Analyze-Data-Intuitively-and-Instantly-Logi-Report-Server-v17)
