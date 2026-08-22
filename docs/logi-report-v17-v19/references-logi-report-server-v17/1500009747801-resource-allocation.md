---
title: "Resource Allocation"
id: 1500009747801
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747801-Resource-Allocation
updated_at: 2021-07-25T07:19:36Z
---

# Resource Allocation

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747781-Report-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009720842-Result-Properties)

# Resource Allocation

The Resource Allocation dialog box is used to allocate the server resources to a specific [organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations). It appears when an admin user selects the Resource Allocation link in the Control column of the organization table in Administration > Security > Organization page in the server console.

![Resource Allocation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936758423/rscalct.gif)

**Concurrent Users**

Shows the number of concurrent users available.

* **Maximum Concurrent Users**  
   Specifies the maximum number of concurrent users allowed in the organization. The concurrent organization users at runtime is under the control of the maximum number of concurrent users permitted by the server license.

**Concurrent Reports**

Shows the number of concurrent reports available.

* **Maximum Concurrent Reports**  
   Specifies the maximum number of concurrent reports allowed in the organization. The concurrent organization reports at runtime is under the control of the maximum number of concurrent reports permitted by the server license.

**Disk**

Shows the disk size available.

* **Maximum Size**  
   Specifies the maximum disk size that the organization can use, including disk space for resources and result files (the server history folder), log files (the server logs folder; in a cluster, log size is the sum of the log size in all the nodes), cached data and cube files (the server cache folder), even some temporary runtime files that are created when the organization users run reports/dashboards/Visual Analysis (the server temp folder).

**Memory**

Shows the memory size available.

* **Maximum Size**  
   Specifies the maximum memory size that the organization can use.
* **Cache Catalogs**  
   Specifies whether to cache catalogs used by the organization.
  + **Maximum Size**  
     Specifies the maximum memory size that can be used for caching catalogs. The value should be no more than 80% of the maximum memory size.
* **Cache Reports**  
   Specifies whether to cache reports used by the organization.
  + **Maximum Size**  
     Specifies the maximum memory size that can be used for caching reports. The value should be no more than 80% of the maximum memory size.
* **Cache Images**  
   Specifies whether to cache images used by the organization.
  + **Maximum Size**  
     Specifies the maximum memory size that can be used for caching images. The value should be no more than 80% of the maximum memory size.
* **Maximum Report Data Size**  
   Specifies the maximum memory size that can be used for caching report data within the organization. The value should be no more than 80% of the maximum memory size.
* **Maximum Cube Size**  
   Specifies the maximum memory size for the cube used by the organization. The value should be no more than 80% of the maximum memory size.
* **Compress Swap Files**  
   Specifies whether or not to compress the temporary data generated during runtime before it is swapped to disk. By compressing the swap files, the I/O efforts in certain circumstance may be remarkably reduced so that the overall performance can be improved.

  **Note:** Compressing swap files will increase CPU pressure because it uses compress algorithm to shrink data, so if your system already has high CPU usage, enabling this option will bring extra performance impact, depending on different circumstance, and such impact may overcome the performance gain that comes from reducing I/O time.

**OK**

Applies the selected values to the parameter and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Reset**

Resets to the default settings.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747781-Report-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009720842-Result-Properties)
