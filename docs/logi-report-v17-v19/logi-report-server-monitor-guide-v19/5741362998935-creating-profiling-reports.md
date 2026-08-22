---
title: "Creating Profiling Reports"
id: 5741362998935
section: "Logi Report Server Monitor Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741362998935-Creating-Profiling-Reports
updated_at: 2022-10-31T17:15:39Z
---

# Creating Profiling Reports

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741399674519-Maintaining-Server)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394264727-Managing-and-Monitoring-Resources-Using-the-JMX-Monitoring-Features)

# Creating Profiling Reports

Server Monitor can generate a performance statistic report to inspect the performance of Server during a certain period of time. This topic introduces what information the report may contain and how you can create report on Server Monitor.

There can be two types of profiling reports: one collects report running information and the other obtains a specified number of frequently accessed reports. The profiling report that collects report running information categories the reports into three groups: All, Page Report, and Non Page Report. Server records all page reports running in Page Report Studio and other formats and all web reports on-demand running in the PDF, Excel, and HTML formats. However, the profiling report does not record web reports running in Web Report Studio.

Server Monitor generates the performance statistic report using the information that Server collects and saves to its own database. Whether or not Server collects profiling information is controlled by the property server.profiling.enable=true/false in the **server.properties** file in `<server_install_root>\bin`. Before Server Monitor can inspect the performance of Server, you must first make sure that Server has collected its report-running information. To make certain of this, make sure that the property **server.profiling.enable** is set to **true**.

**To create a profiling report:**

1. Select a Server node in the left tree, and then select the **Profiling** tab.
2. Specify the time period for Server Monitor to get related data.

   If you want to create a profiling report for the topN most frequently viewed reports, in the Top box, specify how many most frequently accessed reports are to be recorded. Make sure that the number specified here must be valid. If not, the latest used number will be applied.
3. Select **Submit** to create the report.

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741399674519-Maintaining-Server)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394264727-Managing-and-Monitoring-Resources-Using-the-JMX-Monitoring-Features)
