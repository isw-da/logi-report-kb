---
title: "Choosing the Report Type"
id: 5735534332951
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735534332951-Choosing-the-Report-Type
updated_at: 2022-11-02T08:23:10Z
---

# Choosing the Report Type

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569753751-Designing-Your-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports)

# Choosing the Report Type

Logi Report supports these types of reports: Page Report, Web Report, and Library Component. As a report developer, you need to decide what report type you should choose to best serve your reporting requirements before creating reports in Designer. This topic compares the report types briefly to help you know about the characteristics of each report type.

**Page Report**

Page reports aim at paginated result sets and run in Page Report Studio in the Server-powered runtime environment. A page report contains one or more report tabs that are of the same or related purposes. You can design, maintain, run, and schedule the report tabs in a page report together or separately, and thus maximize the product performance by sharing data sources in one report. Page reports support complex reporting techniques such as pixel-perfect reporting. They also provide features that are unique to themselves such as subreports, bursting report, and complex calculations that require the use of formulas which apply global variables. You can edit page report templates in both Designer and Page Report Studio.

**Web Report**

Compared with page reports, web reports provide easier and faster report creation and design, faster report execution, streamlined customization, and interactive presentation style using the latest Web technology. They take the tabular layout for well-aligned multicomponents design that aims at Web view. When running a web report in a browser in Web Report Studio, you have a user interface to view each component with local page navigation and scroll bars that are not available in a page report, and when exporting a web report to PDF or printing, you can still do page numbers and page breaks the same as with a page report. Web reports are more efficient at runtime than page reports. They allow for most user actions to be taken in the browser rather than going back to Server for every request. Web reports can therefore handle a much larger number of user requests than page reports on the same hardware. Web reports also support agile development techniques such as continuous integration by enabling you to update report templates in both Designer and Web Report Studio.

**Library Component**

Library components or widgets, are charts, tables, crosstabs, control components, and others. They are created and edited in Designer for use in dashboards specifically in JDashboard at runtime. Library components can communicate with each other via a messaging mechanism, which makes the runtime data synchronization possible. Designer also supports saving any data component in a web report as a library component, therefore, a good way to create library components is to first build them in a web report and test the web report. Once the web report is working well, you can save the data components in it as library components to reuse them easily.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569753751-Designing-Your-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports)
