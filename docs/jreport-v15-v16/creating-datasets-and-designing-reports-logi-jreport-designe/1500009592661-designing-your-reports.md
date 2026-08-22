---
title: "Designing Your Reports"
id: 1500009592661
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592661-Designing-Your-Reports
updated_at: 2021-07-28T18:40:00Z
---

# Designing Your Reports

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570902-Page-Reports)

# Designing Your Reports

Logi JReport supports three types of reports, Page Report, Web Report and Library Component, to serve different reporting requirements.

* A [page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009570902-Page-Reports) is composed of one or more report tabs that are designed for the same purpose, or related purposes. A page report uses .cls as the file suffix.
* A [web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports) contains only one report and uses .wls as the file suffix.
* A [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009592681-Library-Components) is used by end users to build dashboard using JDashboard and uses .lc as the file suffix.

As a report developer your first task with Logi JReport Designer is to decide what report type you need. The choice should not be that the report requires user interactivity as all the three reports have extensive support for interactivity in browsers at runtime.

Comparing with the single-report management system before, the Page Report feature is designed to improve the product performance, avoid wasting data sources by sharing them in one page report, and manage and maintain reports more easily for the report developers. There are features that are only available in page reports such as subreport, bursting report, embedded components inside group panels of a banded object and complex calculations that require the use of formulas that use global variables.

The biggest advantage of web reports is that they are much more efficient at runtime than page reports and are based on newer browser technology. They can do most user actions in the browser rather than going back to the server for every request. For example, sorting on a column can be done in the browser rather than sending the request back to the server using AJAX to execute the sort then sending the updated pages back to the user's browser to display. This results in web reports being able to handle a much larger number of users than page reports on the same hardware. Moreover, when running a web report in a browser you have a much nicer user interface to view each component with local page navigation and scrollbars that are not available in a page report, and when exporting a web report to PDF or printing you can still do page numbers and page breaks the same as you can with a page report. Therefore, when choosing between web report and page report, first see if you can build it in a web report, if you can then use a web report.

Library components cannot run outside of dashboards but you can save any data component in a web report as a library component. Often a good way to create library components is to first build them in a web report and test the web report. Once a web report is working well you can save the data components in it as library components. End users can even drag data components right out of a page report or web report and use them in JDashboard. This allows the user to easily run a report using the components as well as use them in JDashboard. Within a dashboard, library components are able to communicate with each other via the message mechanism. This allows actions such as common filters to be applied to all the components of a dashboard even when coming from different data sources.

**Notes:**

* A [Logi JReport Live license for Logi JReport Designer](https://devnet.logianalytics.com/hc/en-us/articles/1500009568442-Logi-JReport-Licenses#Live) is required in order to create reports and library components based on business views and use all the related features. If you do not have the license, contact your Jinfonet Software account manager to obtain it.
* The resources, components, properties and options that are not supported for a report type are disabled on the user interface.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570902-Page-Reports)
