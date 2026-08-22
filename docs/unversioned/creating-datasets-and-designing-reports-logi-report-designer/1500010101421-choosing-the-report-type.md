---
title: "Choosing the Report Type"
id: 1500010101421
section: "Creating Datasets and Designing Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101421-Choosing-the-Report-Type
updated_at: 2021-11-16T03:29:30Z
---

# Choosing the Report Type

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062742-Designing-Your-Reports)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports)

# Choosing the Report Type

Logi Report supports three types of reports, Page Report, Web Report, and Library Component. As a report developer, you need to decide what report type you should choose to best serve your reporting requirements before creating reports in Designer. This topic compares the report types briefly to help you know about the characteristics of each report type.

**Page Report**

Page reports are composed of one or more report tabs that are designed for the same or related purposes. Report developers can design, maintain, run, and schedule these report tabs together or separately. Page reports are designed for paginated result sets as well as more complex reporting techniques such as pixel-perfect reporting. Page reports maximize product performance by sharing data sources in one page report. There are features that are only available in page reports such as subreports, bursting report, and complex calculations that require the use of formulas which use global variables. You can edit page report templates in both Designer and Page Report Studio.

**Web Report**

Compared with page reports, web reports provide easier and faster report creation and design, faster report execution, streamlined customization, and interactive presentation style using the latest Web technology. Web reports are designed to be more efficient at runtime than page reports. They allow for most user actions to be taken in the browser rather than going back to Server for every request. For example, sorting on a column can be done in the browser. Web reports can therefore handle a much larger number of user requests than page reports on the same hardware. Moreover, when running a web report in a browser, you have a user interface to view each component with local page navigation and scrollbars that are not available in a page report, and when exporting a web report to PDF or printing, you can still do page numbers and page breaks the same as with a page report. Web reports also support agile development techniques such as continuous integration by enabling you to update report templates in both Designer and Web Report Studio.

**Library Component**

Library components or widgets, are charts, tables, crosstabs, control components, and others, which are created and edited in Designer for use in dashboards specifically. Library components are able to communicate with each other via a messaging mechanism, which makes the runtime data synchronization possible. Designer also supports saving any data component in a web report as a library component, therefore, a good way to create library components is to first build them in a web report and test the web report. Once the web report is working well, you can save the data components in it as library components to reuse them easily.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062742-Designing-Your-Reports)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports)
