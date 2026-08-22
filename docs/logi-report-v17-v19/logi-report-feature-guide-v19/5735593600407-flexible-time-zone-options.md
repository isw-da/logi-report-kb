---
title: "Flexible Time Zone Options"
id: 5735593600407
section: "Logi Report Feature Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735593600407-Flexible-Time-Zone-Options
updated_at: 2022-11-02T08:18:19Z
---

# Flexible Time Zone Options

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735563367191-Dynamic-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520011031-Geo-Analysis)

# Flexible Time Zone Options

You can set time zone in both Logi Report Designer and Server in a variety of ways. This topic describes the different time zone options.

On Server, you can change time zone at the server level for displaying date and time on the Server UI and in reports and parameters.

![Server-Level Time Zone Setting](https://devnet.logianalytics.com/hc/article_attachments/9898403263895/timezone-server.gif)

You can also set time zone at the session level to work in one report or user session, such as in the session and the URL for running reports or dashboards, using the property **rpt\_timezone**.

Furthermore, in the XML data source, you can set different time zones for different date and time values. To make the time zones work on the values, you can run reports using URLs and add the parameter **CustomOffset=true** in the URLs, on Logi Report Server.

Besides, in Logi Report Designer, you can view and export reports with value-level time zone that you set in the XML data source, by enabling the **Use value time zone** option.

![Enable Value-Level Time Zone in Designer](https://devnet.logianalytics.com/hc/article_attachments/9898403292695/timezone-designer.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735563367191-Dynamic-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520011031-Geo-Analysis)
