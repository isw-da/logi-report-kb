---
title: "Logi JReport Designer Guide v16 Overview"
id: 4403502450711
section: "Introduction to Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4403502450711-Logi-JReport-Designer-Guide-v16-Overview
updated_at: 2021-07-24T10:37:41Z
---

# Logi JReport Designer Guide v16 Overview

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068801-Logi-JReport-v16-Enhancements)

# Logi JReport Designer Guide v16 Overview

Logi JReport is a complete Java reporting solution that provides sophisticated enterprise reporting, ad hoc reporting, and data analysis. A 100% Java EE architecture and a rich set of APIs allow Logi JReport to be seamlessly embedded into any application, providing end users with a transparent interface to easily generate reports, share information, and analyze data. With Logi JReport, any report can be made interactive, extending the "life" of a report by allowing users to easily sort, group, navigate, and filter via the Web. This wide range of functionality, including the ability to drill down on data, enables users to quickly derive value from their business intelligence.

The Logi JReport Designer Guide v16 Help System provides you with everything you need to know to fully utilize all of the features of Logi JReport Designer v16. You can access the information by looking at the Table of Contents, or by using Search.

In addition to the regular documentation you can read here, a set of Java and API documentation and samples are also provided for your reference. To view the Javadoc, select this link: [Logi JReport v16 API Doc](https://www.jinfonet.com/kbase/jreport16.1/api/index.html "Click to view the Javadoc."); to download the samples, select this link: [Logi JReport v16 Samples](https://www.jinfonet.com/kbase/jreport16.1/samples.zip "ZIP file containing samples. ").

This topic provides a brief introduction to Logi JReport v16 as follows:

* [Logi JReport Product Overview](#Product)
* [Who Uses Logi JReport?](#Who)
* [What Is a Report?](#What)
* [Lifecycle of a Report](#Lifecycle)

## Logi JReport Product Overview

Logi JReport's architecture takes advantage of the portability, scalability, and ease of integration associated with Java EE technology to provide a powerful, flexible reporting solution that fits perfectly within any application architecture.

![](https://devnet.logianalytics.com/hc/article_attachments/4404901037847/jreport-architecture.gif)

**Logi JReport Server** is a high performance reporting engine designed to support embedded analytics for any application. It can scale from a single CPU to a cluster of servers for any deployment requirement on any system architecture. With a full set of Java and JavaScript APIs, Logi JReport Server has been integrated into hundreds of applications and caters to hundreds of thousands of users every day. As a 100% Java report generation and management tool, Logi JReport Server enables efficient management, sharing, scheduling and delivery of reports. With Logi JReport Server, any application can empower end users to create, navigate and interact with their data visualizations.

**Logi JReport Designer** is a Swing-based Integrated Development Environment (IDE) that enables sophisticated report design and presentation of critical business data. It provides an intuitive interface, reusable report components, flexible layout, and a toolset for designing and testing reports. With Logi JReport designer, you can build reports using simple drag and drop techniques or by using the report wizard. Data can be accessed from any data source to design and preview reports in order to deliver information to end users in the most relevant and intuitive manner. Rapid creation and modification of reports is accomplished by toggling between design mode and view mode where the report will be displayed with the actual dataset. Once report design is complete, the report is published to Logi JReport Server for generation, delivery, and management.

## Who Uses Logi JReport?

Logi JReport delivers an enterprise-wide solution. Therefore different types of users throughout your organization will use Logi JReport. Each type of user will be able to understand the features and find value in Logi JReport as it relates to their job function or reporting requirements.

There are five general types of Logi JReport users:

* **Business Analyst**If you are a business analyst, you should understand how Logi JReport Page Report Studio and Web Report Studio allow you to create a special category of reports called ad hoc reports. Unlike the predefined reports in Logi JReport designer, you build these reports in the runtime environment based on a data model built and published by a report developer.

  You can also create a dashboard rather than a web report or page report, using predefined data components with JDashboard, or use the in-context analysis tool Visual Analysis to visualize the result of every step of your work.
* **Developer and Report Developer**

  If you are a report developer, you will use Logi JReport designer, Logi JReport's visual design environment. This intuitive desktop design tool enables the building of data source connections to your database for retrieving data to reports and uses familiar conventions such as property panels, toolbars, style sheets, and drag and drop placement to support every aspect of the report design process. You will quickly become proficient in using the design environment and be able to create professional reports.
* **Systems Analyst or Application Server Administrator**

  If you are a systems analyst or application server administrator, you should know that the Logi JReport solution is managed from a single access point, a web-based console. The Logi JReport solution offers many different deployment options, enabling existing architecture to be leveraged. It can be embedded in a web application via a self-contained WAR/EAR file to provide a reporting service or it can operate as a standalone server.
* **End User**

  If you are an end user of reports, you should understand the many different presentation strategies that are available. You can decide which format best delivers the information that you need to make timely and critical business decisions. With Logi JReport, reports can be viewed and exported to a variety of formats including HTML, PDF, Excel, XML, RTF, CSV, PostScript, Page Report Result and Web Report Result. Logi JReport's Page Report Result and Web Report Result outputs enable you to interact with and customize report views to obtain exactly the information needed.

## What Is a Report?

A report is comprised of a report template and a dataset.

A report template contains static text and graphics as well as placeholders for data.

When a report is in the runtime environment, it connects to the data source associated with the report, executes the query, and applies the fetched data to the template thereby creating a report result file:

![Report Template](https://devnet.logianalytics.com/hc/article_attachments/4404901038103/what-is-a-report.gif)

Therefore, each report result represents a unique dataset, the one that exists at the time the query is run.

## Lifecycle of a Report

Just like an application, a report has a distinct life cycle. The life cycle contains the following phases:

![Report Lifecycle](https://devnet.logianalytics.com/hc/article_attachments/4404901038359/report-lifecycle.gif)

**Phase 1: Determine requirements (report developer)**

The first fundamental requirement comes from the intended end users of the report. First, determine who will be the end user of the report and then identify the general purpose of the report. Ask what decisions those users need to make and how often they need to make them (daily, monthly, or other).

Second, you should determine the specific pieces of data that need to be presented in the report and how the pieces map to the data source. Look for common data elements that span multiple reports.

Third, you need to determine the security implications associated with the report. Are there pieces of data that need restricted access? Are there regulatory drivers of the report?

Fourth, determine the expected demand of the report result. Will on-demand report results be necessary or can the report be scheduled? Will report results need to be saved, and for how long?

Fifth, determine the desired report output format. For most Java applications delivery via the Web is the preferred method to present information. However, there may be other end users who don't need or want Web-based information. Perhaps they require the report be delivered in a standard business format (such as Excel or PDF) or printed.

**Phase 2: Develop report template (report developer)**

A template can be thought of as a report blueprint that contains static text and graphical objects as well as placeholders to display the data pieces needed on the report. The template definition includes the query that needs to execute to provide the data, as well as the database connection on which to execute it.

Share a report prototype that includes sample data with the end users to see if it meets their requirements and also to obtain feedback on the scope and layout of the report.

**Phase 3: Publish report results (system administrator)**

Publishing a report template executes the query and merges the resulting data set with the template. The result is a report instance that is available in the context of Logi JReport Server. Report results can be saved to other locations, and in various formats such as HTML, PDF, RTF, and others.

Communicate with the end users regarding how they can access the report and then provide training, as needed. Include a way for the end users to provide feedback; acknowledge feedback and build release schedule.

As report production scales up, the system administrator should monitor performance and apply the appropriate load balancing and security measures.

**Phase 4: Access report results (end user and business analyst) and administer (system administrator)**

After a report is generated, end users can access it in a variety of ways. A report can be viewed through the Logi JReport Server console, through a Java application, or routed to a delivery target such as an e-mail address or printer. The business analyst can also build ad hoc reports as needed.

The system administer monitors the report access environment through the Logi JReport Server Monitor.

**Phase 5: Update report template (report developer)**

Collect feedback from the end users to determine any needed improvements to the layout or behavior of the report. Also, modify security as needed (add/drop users) and update data source connections.

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068801-Logi-JReport-v16-Enhancements)
