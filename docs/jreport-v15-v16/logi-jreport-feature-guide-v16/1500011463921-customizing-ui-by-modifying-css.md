---
title: "Customizing UI by Modifying CSS"
id: 1500011463921
section: "Logi JReport Feature Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463921-Customizing-UI-by-Modifying-CSS
updated_at: 2021-07-24T10:39:48Z
---

# Customizing UI by Modifying CSS

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011463941-Custom-Aggregations) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431942-Data-Mashup)

# Customizing UI by Modifying CSS

Logi JReport combines state mechanism and CSS to present a window element with different styles before and after the state of the element is changed by event triggering or API calls, for example, when you hover the mouse pointer over a toolbar item, the background color of the item changes to yellow. The change of state is recorded using an 8-bit binary number which will be converted to a decimal number. The decimal number is appended to the end of the class name in a CSS selector to indicate the state of the element, for example, studioPanel\_16 means that the panels in Web Report Studio are invisible. In this way different states of a window element can be controlled with different CSS rules. See the following sample:

```
.studioPanel {  
    display: block;  
    }  
    .studioPanel_16 {  
    display: none;  
    }
```

You can customize the Web Report Studio and JDashboard UI by modifying CSS files directly, like changing the width, height, color, font, borders, padding and so on of the window elements in different states. For details, refer to Customizing the Web Report Studio UI and Customizing the JDashboard UI in the *Logi JReport Server User's Guide*.

In the following example, we change the background color of the title bar for the panels on the left of Web Report Studio to light green by adding the following CSS rule in the file wrptstudio.css and then running `make.bat jsvm` in the command console to make the change take effect.

```
.studioPanel_title {  
    background-color: lightgreen;  
    background-image: none;  
    }
```

![Customize UI](https://devnet.logianalytics.com/hc/article_attachments/4404901360151/customizeui.gif)

>![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011463941-Custom-Aggregations) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431942-Data-Mashup)
