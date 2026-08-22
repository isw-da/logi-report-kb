---
title: "Page Reports vs. Web Reports vs. Library Components"
id: 1500011463341
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463341-Page-Reports-vs-Web-Reports-vs-Library-Components
updated_at: 2021-07-24T10:39:38Z
---

# Page Reports vs. Web Reports vs. Library Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431322-Business-Views) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463601-Part-II-Advanced-Reporting)

# Page Reports vs. Web Reports vs. Library Components

Logi JReport supports three types of reports, Page Report, Web Report, and Library Component. All serve different reporting requirements.

* Web reports provide easier and faster report creation and design, faster report execution, streamlined customization, and interactive presentation style using the latest Web technology. Web reports also support agile development techniques such as continuous integration by allowing report templates to be updated by both Web Report Studio and Logi JReport Designer.
* Page reports are composed of one or more report tabs that are designed for the same or related purposes. Report developers can design, maintain, run and schedule these report tabs together or separately. Page reports are designed for paginated result sets as well as more complex reporting techniques such as pixel-perfect reporting. Page report templates can also be edited in both Page Report Studio and Logi JReport Designer.
* Library components or widgets, are charts, tables, crosstabs, control components and others, that are created and edited in Logi JReport Designer for use in dashboards.

As a report developer your first task with Logi JReport Designer is to decide what report type you need. The following compares the report types briefly.

**Web Reports**

Web reports are designed to be more efficient at runtime than page reports. They allow for most user actions to be performed in the browser rather than going back to the server for every request. For example, sorting on a column can be done in the browser. Web reports can therefore handle a much larger number of user requests than page reports on the same hardware. Moreover, when running a web report in a browser you have a user interface to view each component with local page navigation and scrollbars that are not available in a page report, and when exporting a web report to PDF or printing you can still do page numbers and page breaks the same as with a page report. See [Creating Web Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500011463421-Track-3-Creating-Web-Reports) for an example of creating a web report in Logi JReport Designer, and [Creating a Web Report the Quick Start Way](https://devnet.logianalytics.com/hc/en-us/articles/1500011463261-Lesson-1-Creating-a-Web-Report-the-Quick-Start-Way) and [Creating a Web Report Using Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500011463241-Lesson-2-Creating-a-Web-Report-Using-Wizard) for examples about creating and running web reports in Web Report Studio.

**Page Reports**

Page reports are designed to maximize product performance, avoid wasting data sources by sharing them in one page report, and manage and maintain reports more easily for the report developers. There are features that are only available in page reports such as subreports, bursting report and complex calculations that require the use of formulas that use global variables. You can refer to [Creating Page Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500011463501-Track-1-Creating-Page-Reports) for examples of creating page reports in Logi JReport Designer and [Creating and Performing Data Analysis on Page Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500011463221-Lesson-3-Creating-and-Performing-Data-Analysis-on-Page-Reports) about creating and running page reports in Page Report Studio.

**Library Components**

Library components are built specifically for use in dashboards. They are able to communicate with each other via a messaging mechanism, which makes the runtime data synchronization possible. Any data component built in a web report can also be saved as a library component, therefore a good way to create library components is to first build them in a web report and test the web report. Once a web report is working well you can save the data components in it as a library component to reuse them easily. [Creating Library Components](https://devnet.logianalytics.com/hc/en-us/articles/1500011431482-Track-4-Creating-Library-Components) contains some library component examples. For how to use library components in dashboards, refer to [Self-service Dashboard with Logi JReport](https://devnet.logianalytics.com/hc/en-us/articles/1500011463201-Track-1-Self-service-Dashboard-with-Logi-JReport).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431322-Business-Views) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463601-Part-II-Advanced-Reporting)
