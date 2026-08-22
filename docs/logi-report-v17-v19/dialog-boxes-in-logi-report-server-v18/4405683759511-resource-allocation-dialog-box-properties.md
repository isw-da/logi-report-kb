---
title: "Resource Allocation Dialog Box Properties"
id: 4405683759511
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683759511-Resource-Allocation-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:06Z
---

# Resource Allocation Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690562327-Publish-to-Server-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683760535-Resource-Properties)

# Resource Allocation Dialog Box Properties

This topic describes how you can use the Resource Allocation dialog box to allocate the server resources to a specific [organization](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations).

Server displays the dialog box when an administrator selects Resource Allocation in the Control column of the organization table in Administration > Security > Organization page on the Server Console.

![Resource Allocation dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447105431/rscalct.gif)

**Concurrent Users**

The number of concurrent users available.

* **Maximum Concurrent Users**  
   Specify the maximum number of concurrent users you want to allow in the organization. The concurrent organization users at runtime is under the control of the maximum number of concurrent users that the server license permits.

**Concurrent Reports**

The number of concurrent reports available.

* **Maximum Concurrent Reports**  
   Specify the maximum number of concurrent reports you want to allow in the organization. The concurrent organization reports at runtime is under the control of the maximum number of concurrent reports that the server license permits.

**Disk**

The disk size available.

* **Maximum Size**  
   Specify the maximum disk size that the organization can use, including disk space for resources and report files (the server history folder), log files (the server logs folder; in a cluster, log size is the sum of the log size in all the nodes), cached data and cube files (the server cache folder), even some temporary runtime files that Server created when the organization users run reports/dashboards/Visual Analysis (the server temp folder).

**Memory**

The memory size available.

* **Maximum Size**  
   Specify the maximum memory size that the organization can use.
* **Cache Catalogs**  
   Select to cache catalogs that the organization uses.
  + **Maximum Size**  
     Specify the maximum memory size that Server can use for caching catalogs. The value should be no more than 80% of the maximum memory size.
* **Cache Reports**  
   Select to cache reports that the organization uses.
  + **Maximum Size**  
     Specify the maximum memory size that Server can use for caching reports. The value should be no more than 80% of the maximum memory size.
* **Cache Images**  
   Select to cache images that the organization uses.
  + **Maximum Size**  
     Specify the maximum memory size that Server can use for caching images. The value should be no more than 80% of the maximum memory size.
* **Maximum Report Data Size**  
   Specify the maximum memory size that Server can use for caching report data within the organization. The value should be no more than 80% of the maximum memory size.
* **Maximum Cube Size**  
   Specify the maximum memory size for the cube that the organization uses. The value should be no more than 80% of the maximum memory size.
* **Compress Swap Files**  
   Select to compress the temporary data that Server generates during runtime before swapping data to disk. Compressing the swap files may remarkably reduce the I/O efforts in certain circumstance, which can improve the overall performance.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) Compressing swap files will increase CPU pressure because it uses compress algorithm to shrink data. If your system already has high CPU usage, enabling this property will bring extra performance impact, depending on different circumstances, and such impact may overcome the performance gain that comes from reducing I/O time.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Reset**

Select to discard your changes and restore the dialog box to its default status.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690562327-Publish-to-Server-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683760535-Resource-Properties)
