---
title: "Running a Report Tab in a Page Report"
id: 1500009675481
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675481-Running-a-Report-Tab-in-a-Page-Report
updated_at: 2021-07-24T20:53:31Z
---

# Running a Report Tab in a Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650462-Running-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675441-Refreshing-Page-Report-Data-Automatically)

# Running a Report Tab in a Page Report

If you want to run a specific page report tab, use *jrs.report\_sheet$RPT\_TAB\_NAME=true* to specify a report tab in the current page report, where RPT\_TAB\_NAME is the report name of the specific report tab, not the display name. For example, jrs.report\_sheet$Report2=true.

To get the report name and display name of a page report tab you can open the page report in Logi JReport Designer and look at the Instance Name property in the Report Inspector or you can make use of the API methods getName() and getDisplayName() in the interface jet.server.api.ReportSheetInfo. For the detailed usages, see the Logi JReport Javadoc located in `<install_root>\help\api`.

The URL for running a report tab Applet in Page Report Studio within the report MultimediaObjects.cls is as follows:

`http://localhost:8888/jinfonet/tryView.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fMultimediaObjects.cls&jrs.result_type=8&jrs.report_sheet$report2=true`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650462-Running-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675441-Refreshing-Page-Report-Data-Automatically)
