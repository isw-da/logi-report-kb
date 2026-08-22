---
title: "Part I: Report Overview"
id: 12491477567757
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491477567757-Part-I-Report-Overview
updated_at: 2026-02-25T23:47:25Z
source_host: docs-report.zendesk.com
---
# Part I: Report Overview

This part provides an overview of Report, including the following sections: 

- Report Product Overview

- Who Uses Report?

- What Is a Report?

- Lifecycle of a Report

## 
ReportProduct Overview

- Report delivers operational business intelligence to enterprise applications through powerful embedded reporting.

- Report is a complete Java reporting solution that provides sophisticated enterprise reporting, ad hoc reporting, and data analysis.

- Report is architected using Java Enterprise Edition. It also includes a rich set of APIs that enable Report to be seamlessly embedded into any application, providing end users with a transparent interface to easily generate reports, share information, and analyze data.

- Report's architecture takes advantage of the portability, scalability, and ease of integration associated with Java Enterprise Edition, providing a powerful, flexible reporting solution that fits perfectly within any application architecture. 

- In Report, you can make any report interactive, which helps extend the "life" of a report by enabling users to easily sort, group, navigate, drill, and filter via the Web. This wide range of functionality enables users to quickly derive value from their business intelligence.

Report Server is a high-performance reporting engine designed to support embedded analytics for any application. It can scale from a single CPU to a cluster of servers for any deployment requirement on any system architecture.

With a full set of Java and JavaScript APIs, ReportServer has been integrated into hundreds of applications and caters to hundreds of thousands of users every day. As a 100% Java report generation and management tool, Report Server enables efficient management, sharing, scheduling, and delivery of reports.

With Report Server, any application can empower end users to create, navigate, and interact with their data visualizations.

Report Designer is a Swing-based Integrated Development Environment (IDE) that enables sophisticated report design and presentation of critical business data. It provides an intuitive interface, reusable report components, flexible layout, and a toolset for designing and testing reports.

With ReportDesigner, you can build reports using simple drag-and-drop techniques or by using a wizard; you can access data  from any source to design and preview reports in order to deliver information to end users in the most relevant and intuitive manner; you can accomplish rapid creation and modification of reports by toggling between design mode and view mode where the report  displays with the actual dataset.

Once report design is complete, you can publish it  to Report Server for generation, delivery, and management.

## 
Who Uses Report?

Report delivers an enterprise-wide solution. Therefore, different types of users throughout your organization can use Report. Each type of user can understand the features and find value in Report as it relates to their job function or reporting requirements.

There are five general types of Report users. Each type of user can focus on specific areas of this tutorial as described in the following:

- 
Business Analyst
If you are a business analyst, you should understand how Report Page Report Studio and Web Report Studio allow you to create a special category of reports called ad hoc reports.

Unlike predefined reports in Report Designer, you build these reports in the runtime environment based on a data model built and published by a report developer.

In addition to standard reports, you can also create a dashboard using predefined data components with JDashboard, or use the in-context analysis tool Visual Analysis to visualize the result of every step of your work.

Focus on tracks in Part IV: End User Experience.

- 
Developer and Report Developer
If you are a report developer, you will use Report Designer, a visual WYSIWYG design environment. This intuitive desktop design tool enables the building of data source connections to your database for retrieving report data.

Report Designer uses familiar conventions such as property panels, toolbars, style sheets, and drag-and-drop placement of report objects. You can quickly become proficient using the design environment to create professional reports.

Focus on Part II: Report Basics for Developers. 

- 
Systems Analyst or Application Server Administrator
If you are a systems analyst or application server administrator, you should know that the  Report solution is managed from a single access point, a web-based console.

The Report solution offers many different deployment options, enabling existing architectures to be leveraged. It can operate as a standalone server, or it can be embedded in a web application via a self-contained WAR/EAR file to provide a reporting service.

See Publishing, Running and Administering Resources in Part III.

- 
End User
If you are an end user of reports, you should understand the many different presentation strategies that are available. You can decide which format best delivers the information that you need to make timely and critical business decisions.

In Report, you can view and export reports to a variety of formats including HTML, PDF, Excel, XML, RTF, CSV, and PostScript. Report's Page Report Result and Web Report Result outputs enable you to interact with and customize report views to obtain exactly the information needed.

Focus on tracks in Part IV: End User Experience.

## 
What Is a Report?

A report is comprised of a report template and a dataset.

A report template contains static text, graphics, and placeholders for data.

When you run a report in the runtime environment, it connects to the associated data source, executes the query, and applies the fetched data to the template thereby generating the report.

Therefore, each running of a report represents a unique dataset, the one that exists at the time the query runs.

## 
Lifecycle of a Report

Just like an application, a report has a distinct lifecycle. The lifecycle contains the following phases:

Phase 1: Determine requirements (report developer)

The first fundamental requirement comes from the intended end users of the report. First, determine who are the end users and identify the general purpose of the report. Ask what decisions those users need to make and how often they need to make them (daily, monthly, or other).

Second, you should determine the specific pieces of data that need to be presented in the report and how the pieces map to the data source. Look for common data elements that span multiple reports.

Third, you need to determine the security implications associated with the report. Are there pieces of data that need restricted access? Are there regulatory drivers of the report?

Fourth, determine the expected demand of the report. Is on-demand report necessary or can the report be scheduled? Does the report need to be saved, and for how long?

Fifth, determine the report output format. For most Java applications delivery, via the Web is the preferred method to present information. However, there may be other end users who do not need or want Web-based information. Perhaps they require the report be delivered in a standard business format such as Excel, PDF, or printed.

Phase 2: Develop report template (report developer)

A template is a report blueprint that contains static text, graphical objects, and placeholders to display the data pieces needed on the report. The template definition includes the query that needs to execute to provide the data, and the database connection on which to execute it.

Share a report prototype that includes sample data with the end users to see if it meets their requirements and to obtain feedback on the scope and layout of the report.

Phase 3: Publish report (system administrator)

Publishing a report template executes the query and merges the resulting dataset with the template. The result is a report instance that is available in the context of Report Server. You can save the results  to other locations, and in various formats such as HTML, PDF, and Excel.

Communicate with the end users regarding how they can access the report and then provide training, as needed. Include a way for the end users to provide feedback; acknowledge feedback and build a release schedule.

As report production scales up, the system administrator should monitor performance and apply the appropriate load balancing and security measures.

Phase 4: Access report  (end user and business analyst) and administer (system administrator)

After a report is generated, end users can access it in a variety of ways. They can view the report through the Report Server Console, through a Java application, or route it to a delivery target such as an email address or printer. The business analyst can also build ad hoc reports as needed.

The system administer monitors the report access environment through Report Server Monitor.

Phase 5: Update report template (report developer)

Collect feedback from the end users to determine any needed improvements to the layout or behavior of the report. Also, modify security as needed (add/drop users) and update data source connections.
