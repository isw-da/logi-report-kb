---
title: "Options for Embedding Reports and Dashboards into your Software Application"
id: 360050173013
section: "Best Practices"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050173013-Options-for-Embedding-Reports-and-Dashboards-into-your-Software-Application
updated_at: 2023-08-01T07:11:59Z
---

# Options for Embedding Reports and Dashboards into your Software Application

Logi Report allows you to embed reports and dashboards in multiple ways. One of the first things you need to decide is whether you want your analytics within your existing application or in a separate application/window.

![Application Window](https://devnet.logianalytics.com/hc/article_attachments/9896648040855)

When integrating Logi Report reports or dashboards within an existing application window, there are two primary options:

* Option 1: Logi Report URL on iFrame: display report via URL on the iFrame’s src attribute
* Option 2: Logi Report API via JavaScript: display report via JavaScript file

Although JavaScript is the more preferred method in most use cases, iFrames are still fine for many applications. On the surface, the end result may look very similar, but the chosen invocation method carries many ripple effects from a security, portability, and maintenance perspective.

The screenshot below shows a Logi Report chart report embedded within a Microsoft .NET application (MixERP). The chart report is invoked via JavaScript API from the calling .NET application.

![Chart Report Embedded Within a Microsoft
  .NET Application (MixERP)](https://devnet.logianalytics.com/hc/article_attachments/9896631919255)

To achieve different styles of embedding reports and dashboards into your application, Logi Report offers different options for security and user authentication.
