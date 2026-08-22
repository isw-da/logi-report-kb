---
title: "Customizing UI by Modifying CSS"
id: 5735563288215
section: "Logi Report Feature Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735563288215-Customizing-UI-by-Modifying-CSS
updated_at: 2022-11-02T04:11:53Z
---

# Customizing UI by Modifying CSS

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735519780631-Custom-Aggregations)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735526375703-Data-Mash-Up)

# Customizing UI by Modifying CSS

You can customize the Web Report Studio and JDashboard UI by modifying CSS files, like changing the width, height, color, font, borders, and padding of the window elements in different states.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9898419824023/criticalicon.gif)JDashboard is in maintenance mode, and we will not be adding new features to it. If you need more information, contact [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.).

In the following example, we change the background color of the title bar for the panels in Web Report Studio to light green by adding the following CSS rule in the file wrptstudio.css and then running make.bat stored in `<install_root>\public_html\bin` with the *jsvm* option in the command console to make the change take effect.

`.studioPanel_title {  
    background-color: lightgreen;  
    background-image: none;  
}`

![Customize UI](https://devnet.logianalytics.com/hc/article_attachments/9898521685399/customizeui.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735519780631-Custom-Aggregations)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735526375703-Data-Mash-Up)
