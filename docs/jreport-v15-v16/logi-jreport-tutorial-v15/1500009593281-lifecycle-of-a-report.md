---
title: "Lifecycle of a Report"
id: 1500009593281
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593281-Lifecycle-of-a-Report
updated_at: 2021-07-24T05:53:41Z
---

# Lifecycle of a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593361-What-Is-a-Report-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593341-Logi-JReport-Product-Overview)

# Lifecycle of a Report

Just like an application, a report has a distinct life cycle. The life cycle contains the following phases:

![Report Lifecycle](https://devnet.logianalytics.com/hc/article_attachments/4404893788439/ov_life.gif)

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

After a report is generated, end users can access it in a variety of ways. A report can be viewed through the Logi JReport Server user console, through a Java application, or routed to a delivery target such as an e-mail address or printer. The business analyst can also build ad hoc reports as needed.

The system administer monitors the report access environment through the Logi JReport Server administration console.

**Phase 5: Update report template (report developer)**

Collect feedback from the end users to determine any needed improvements to the layout or behavior of the report. Also, modify security as needed (add/drop users) and update data source connections.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593361-What-Is-a-Report-) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593341-Logi-JReport-Product-Overview)
