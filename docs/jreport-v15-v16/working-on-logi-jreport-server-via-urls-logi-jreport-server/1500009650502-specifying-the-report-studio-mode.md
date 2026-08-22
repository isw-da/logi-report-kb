---
title: "Specifying the Report Studio Mode"
id: 1500009650502
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650502-Specifying-the-Report-Studio-Mode
updated_at: 2021-07-24T20:53:31Z
---

# Specifying the Report Studio Mode

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675501-Opening-Web-Reports-in-Web-Report-Studio-via-JSON)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650482-Specifying-a-Time-Duration-for-a-Task-and-Notifying-Someone-by-E-mail)

# Specifying the Report Studio Mode

This topic introduces how to specify the Web Report Studio mode.

Below is a list of the sections covered in this topic:

* [Specifying the Web Report Studio Mode](#Web)
* [Specifying the Page Report Studio View](#Page)

## Specifying the Web Report Studio Mode

Web Report Studio has two modes: View Mode and Edit Mode. When opening web reports in Web Report Studio by URL, you can use the property jrd\_studio\_mode to specify the mode. If this property is not provided in the URL, the [default mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#WebMode)  set in the server profile will be applied.

Below are the values of the property:

* view - Displays Web Report Studio in View Mode by default and allows for switching to Edit Mode.
* view\_only - Displays Web Report Studio in View Mode only.
* edit - Displays Web Report Studio in Edit Mode by default and allows for switching to View Mode.

However for web reports saved in the Public Reports folder in the server resource tree, Web Report Studio adopts a [permission control](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) to restrict user access, so whether the specified mode can be opened depends on if you have the Execute and/or Edit permissions on the web reports: Execute for View Mode and Edit for Edit Mode. If you do not have the required permission on the public web report you are going to run:

* When both Execute and Edit are disabled, you will be denied to access Web Report Studio.
* When Execute is enabled but Edit is not:
  + view - Displays Web Report Studio in View Mode, same as view\_only.
  + edit - Access to Web Report Studio is denied.
* When Edit is enabled but Execute is not:
  + view and view\_only - Access to Web Report Studio is denied.
  + edit - Displays Web Report Studio in Edit Mode.

**Example：**

`http://localhost:8888/webreport/studio/entry/run.jsp?jrd_report={"name":"/SampleReports/Products.wls"}&jrd_catalog={"name":"/SampleReports/SampleReports.cat"}&jrd_studio_mode=view`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying the Page Report Studio View

Page Report Studio has two views: Basic View and Interactive View. When opening page reports or page report results in Page Report Studio by URL, you can use the property jrd\_studio\_mode to specify the view. If this property is not provided in the URL, the [default view](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#PageMode)  set in the server profile will be applied.

Below are the values of the property:

* basic - Displays Page Report Studio in Basic View by default and allows for switching to Interactive View.
* basic\_only - Displays Page Report Studio in Basic View only.
* interactive - Displays Page Report Studio in Interactive View by default and allows for switching to Basic View.

However for page reports and page report results saved in the Public Reports folder in the server resource tree, Page Report Studio adopts a [permission control](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) to restrict user access, so whether the specified view can be opened depends on if you have the Execute and/or Edit permissions on the page reports or page report results: Execute for Basic View and Edit for Interactive View. If you do not have the required permission on the public page report or page report result you are going to run:

* When both Execute and Edit are disabled, you will be denied to access Page Report Studio.
* When Execute is enabled but Edit is not:
  + basic - Displays Page Report Studio in Basic View, same as basic\_only.
  + interactive - Access to Page Report Studio is denied.
* When Edit is enabled but Execute is not:
  + basic and basic\_only - Access to Page Report Studio is denied.
  + interactive - Displays Page Report Studio in Interactive View.

**Examples：**

* `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrd_studio_mode=interactive`
* `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.resource_path=%2fUSERFOLDERPATH%2fadmin%2ftest&jrs.file=1980996366.rsd&jrd_studio_mode=basic_only`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675501-Opening-Web-Reports-in-Web-Report-Studio-via-JSON)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650482-Specifying-a-Time-Duration-for-a-Task-and-Notifying-Someone-by-E-mail)
