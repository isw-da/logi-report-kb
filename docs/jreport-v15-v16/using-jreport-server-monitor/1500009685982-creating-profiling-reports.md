---
title: "Creating Profiling Reports"
id: 1500009685982
section: "Using JReport Server Monitor"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009685982-Creating-Profiling-Reports
updated_at: 2021-11-03T06:58:39Z
---

# Creating Profiling Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686002-Maintaining-Logi-JReport-Server)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139637399/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009685882-Managing-and-Monitoring-Resources-Using-the-JMX-Monitoring-Features)

# Creating Profiling Reports

Logi JReport Server Monitor can generate a Logi JReport Server performance statistic report for you to inspect the server performance during a certain period of time. There can be two types of profiling reports: one collects report running information and the other obtains a specified number of frequently accessed reports. The profiling report that collects report running information categories the reports into three groups: All, Page Report and Non Page Report. All page reports running in Page Report Studio and other formats, all web reports on-demand running in the PDF, Excel, HTML formats, etc will be recorded. However, the profiling report does not record web reports running in Web Report Studio.

Logi JReport Server Monitor generates the Logi JReport Server performance statistic report using the information that Logi JReport Server collects and saves to its own database. Whether or not Logi JReport Server collects profiling information is controlled by the property server.profiling.enable=true/false in the server.properties file in `<server_install_root>\bin`.

Before Logi JReport Server Monitor can inspect server performance, you must first make sure that Logi JReport Server has collected its report-running information. To make certain of this, make sure that the property server.profiling.enable is set to true.

**To create a profiling report:**

1. Select a server node in the left tree, and then select the **Profiling** tab.
2. Specify the time period for Logi JReport Server Monitor to get related data.

   If you want to create a profiling report for the topN most frequently viewed reports, in the Top box, specify how many most frequently accessed reports are to be recorded. Make sure that the number specified here must be valid. If not, the latest used number will be applied.
3. Select **Submit** to create the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686002-Maintaining-Logi-JReport-Server)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139637399/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009685882-Managing-and-Monitoring-Resources-Using-the-JMX-Monitoring-Features)
