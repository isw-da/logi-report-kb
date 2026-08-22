---
title: "Designing Your Reports"
id: 1500009613242
section: "Creating Datasets and Designing Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009613242-Designing-Your-Reports
updated_at: 2021-07-24T16:03:23Z
---

# Designing Your Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports)

# Designing Your Reports

Logi Report supports three types of reports, Page Report, Web Report and Library Component. All serve different reporting requirements. As a report developer your need to decide what report type you need. The following compares the report types briefly.

**Page Report**

Page reports are composed of one or more report tabs that are designed for the same or related purposes. Report developers can design, maintain, run and schedule these report tabs together or separately. Page reports are designed for paginated result sets as well as more complex reporting techniques such as pixel-perfect reporting. Page reports maximize product performance by sharing data sources in one page report. There are features that are only available in page reports such as subreports, bursting report and complex calculations that require the use of formulas that use global variables. Page report templates can be edited in both Page Report Studio and Logi Report Designer.

**Web Report**

Compared with page reports, web reports provide easier and faster report creation and design, faster report execution, streamlined customization, and interactive presentation style using the latest Web technology. Web reports are designed to be more efficient at runtime than page reports. They allow for most user actions to be taken in the browser rather than going back to the server for every request. For example, sorting on a column can be done in the browser. Web reports can therefore handle a much larger number of user requests than page reports on the same hardware. Moreover, when running a web report in a browser you have a user interface to view each component with local page navigation and scrollbars that are not available in a page report, and when exporting a web report to PDF or printing you can still do page numbers and page breaks the same as with a page report. Web reports also support agile development techniques such as continuous integration by allowing report templates to be updated by both Web Report Studio and Logi Report Designer.

**Library Component**

Library components or widgets, are charts, tables, crosstabs, control components and others, that are created and edited in Logi Report Designer for use in dashboards specifically. Library components are able to communicate with each other via a messaging mechanism, which makes the runtime data synchronization possible. Logi Report Designer also supports saving any data component in a web report as a library component, therefore a good way to create library components is to first build them in a web report and test the web report, once the web report is working well you can save the data components in it as library components to reuse them easily.

Select the following links to view the topics:

* [Creating Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports)
* [Opening Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009613382-Opening-Reports)
* [Saving Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009636221-Saving-Reports)
* [Previewing Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009613422-Previewing-Reports)
* [Editing Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009613302-Editing-Reports)
* [Filtering Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009636161-Filtering-Reports)
* [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009613322-Adding-Links-in-Reports)
* [Changing the Display Type of Objects in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009613282-Changing-the-Display-Type-of-Objects-in-Reports)
* [Using Dynamic Resources and Local Parameters in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports)
* [Delivering Messages Between Library Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009613362-Delivering-Messages-Between-Library-Components-)
* [Creating Bursting Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009636121-Creating-Bursting-Reports)
* [Designing the Report Pages](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages)
* [Making High-Efficiency Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009636141-Making-High-Efficiency-Reports)
* [Managing Page Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009613342-Managing-Page-Reports)

**Notes:**

* A [Logi Report Live license for Logi Report Designer](https://devnet.logianalytics.com/hc/en-us/articles/1500009611222-Logi-Report-Licenses#Live) is required in order to create reports using business views and use all the related features. If you do not have the license, contact your Logi Analytics account manager to obtain it.
* The resources, components, properties and options that are not supported for a report type are disabled on the user interface.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports)
