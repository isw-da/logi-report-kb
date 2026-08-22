---
title: "Customizing UI by Modifying CSS"
id: 4405683512727
section: "Logi Report Feature Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683512727-Customizing-UI-by-Modifying-CSS
updated_at: 2022-01-27T07:58:23Z
---

# Customizing UI by Modifying CSS

![](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683511703-Custom-Aggregations)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683514775-Data-Mash-up)

# Customizing UI by Modifying CSS

You can customize the Web Report Studio and JDashboard UI by modifying CSS files, like changing the width, height, color, font, borders, and padding of the window elements in different states.

In the following example, we change the background color of the title bar for the panels in Web Report Studio to light green by adding the following CSS rule in the file wrptstudio.css and then running make.bat stored in `<install_root>\public_html\bin` with the *jsvm* option in the command console to make the change take effect.

`.studioPanel_title {  
    background-color: lightgreen;  
    background-image: none;  
}`

![Customize UI](https://devnet.logianalytics.com/hc/article_attachments/4420461785623/customizeui.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683511703-Custom-Aggregations)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683514775-Data-Mash-up)
