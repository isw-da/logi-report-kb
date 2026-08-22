---
title: "Customizing UI by Modifying CSS"
id: 12491116654733
section: "Report Feature Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491116654733-Customizing-UI-by-Modifying-CSS
updated_at: 2026-02-25T23:50:59Z
source_host: docs-report.zendesk.com
---
# 
Customizing UI by Modifying CSS 

You can customize the Web Report Studio and JDashboard UI by modifying CSS files, like changing the width, height, color, font, borders, and padding of the window elements in different states. 

JDashboard is in maintenance mode, and we will not be adding new features to it. If you need more information, contact Customer Service.

In the following example, we change the background color of the title bar for the panels in Web Report Studio to light green by adding the following CSS rule in the file wrptstudio.css and then running make.bat stored in <install_root>\public_html\bin with the jsvm option in the command console to make the change take effect. 

.studioPanel_title {
    background-color: lightgreen;
    background-image: none;
}
