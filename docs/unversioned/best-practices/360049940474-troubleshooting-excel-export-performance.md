---
title: "Troubleshooting Excel Export Performance"
id: 360049940474
section: "Best Practices"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049940474-Troubleshooting-Excel-Export-Performance
updated_at: 2020-07-27T22:41:00Z
---

# Troubleshooting Excel Export Performance

### Handling Large Excel Exports

In Logi Report, if you have a page report created before v17 GA release, you may have noticed or run into some performance issues when you export the report into Excel format, especially when there are a lot of data returned into the report. In certain extreme cases, it may also cause the Logi Report Server to run into OutOfMemory exceptions, forcing you to stop the Logi Report Server service.

### Root Cause

The root cause of this performance issue is that before v17 GA release, the default option of generating the Excel output is to generate all the pages from the page report all at once.  If your report has a lot of data, then it also has a lot of pages, and exporting all of them at once will consume a lot of memory. From v15, Logi Report has provided options inside Logi Report Designer to allow you change this default behavior, which means you can set the Excel output to be page-by-page instead of exporting all the pages at once. Starting from v17 GA release, the page-by-page setting has been turned on for Excel output by default.

### Changing Settings

1. Start Logi Report Designer and open the Page Report.  Please ensure you are using a version of Report Designer that is v15 or higher.

2. Open the Report Inspector and under the "Page Panel" you will see a node named "Excel Export Page Setting".  Select the node.

3. Set both the property "Height Auto Fit" and "Width Auto Fit" to false.

4. Save the report.

![image003__1_.png](https://devnet.logianalytics.com/hc/article_attachments/360076915153/image003__1_.png)
