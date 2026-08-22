---
title: "Designing Your Reports"
id: 1500010070781
section: "Creating Datasets and Designing Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070781-Designing-Your-Reports
updated_at: 2021-07-24T10:37:45Z
---

# Designing Your Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports)

# Designing Your Reports

Logi JReport supports three types of reports, Page Report, Web Report and Library Component. All serve different reporting requirements. As a report developer your need to decide what report type you need. The following compares the report types briefly.

**Page Report**

Page reports are composed of one or more report tabs that are designed for the same or related purposes. Report developers can design, maintain, run and schedule these report tabs together or separately. Page reports are designed for paginated result sets as well as more complex reporting techniques such as pixel-perfect reporting. Page reports maximize product performance by sharing data sources in one page report. There are features that are only available in page reports such as subreports, bursting report and complex calculations that require the use of formulas that use global variables. Page report templates can be edited in both Page Report Studio and Logi JReport Designer.

**Web Report**

Compared with page reports, web reports provide easier and faster report creation and design, faster report execution, streamlined customization, and interactive presentation style using the latest Web technology. Web reports are designed to be more efficient at runtime than page reports. They allow for most user actions to be taken in the browser rather than going back to the server for every request. For example, sorting on a column can be done in the browser. Web reports can therefore handle a much larger number of user requests than page reports on the same hardware. Moreover, when running a web report in a browser you have a user interface to view each component with local page navigation and scrollbars that are not available in a page report, and when exporting a web report to PDF or printing you can still do page numbers and page breaks the same as with a page report. Web reports also support agile development techniques such as continuous integration by allowing report templates to be updated by both Web Report Studio and Logi JReport Designer.

**Library Component**

Library components or widgets, are charts, tables, crosstabs, control components and others, that are created and edited in Logi JReport Designer for use in dashboards specifically. Library components are able to communicate with each other via a messaging mechanism, which makes the runtime data synchronization possible. Logi JReport Designer also supports saving any data component in a web report as a library component, therefore a good way to create library components is to first build them in a web report and test the web report, once the web report is working well you can save the data components in it as library components to reuse them easily.

The following topics provide more information on reports:

* [Creating Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports)
* [Opening Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010070901-Opening-Reports)
* [Saving Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010034882-Saving-Reports)
* [Previewing Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010070941-Previewing-Reports)
* [Editing Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010070821-Editing-Reports)
* [Filtering Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010070861-Filtering-Reports)
* [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports)
* [Changing the Display Type of Objects in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010034802-Changing-the-Display-Type-of-Objects-in-Reports)
* [Using Dynamic Resources and Local Parameters in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports)
* [Delivering Messages Between Library Components](https://devnet.logianalytics.com/hc/en-us/articles/1500010034842-Delivering-Messages-Between-Library-Components-)
* [Creating Bursting Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010070801-Creating-Bursting-Reports)
* [Designing the Report Pages](https://devnet.logianalytics.com/hc/en-us/articles/1500010070921-Designing-the-Report-Pages)
* [Making High-Efficiency Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010070841-Making-High-Efficiency-Reports)
* [Managing Page Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010070881-Managing-Page-Reports)

**Notes:**

* A [Logi JReport Live license for Logi JReport Designer](https://devnet.logianalytics.com/hc/en-us/articles/1500010068641-Logi-JReport-Licenses#Live) is required in order to create reports using business views and use all the related features. If you do not have the license, contact your Logi Analytics account manager to obtain it.
* The resources, components, properties and options that are not supported for a report type are disabled on the user interface.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports)
