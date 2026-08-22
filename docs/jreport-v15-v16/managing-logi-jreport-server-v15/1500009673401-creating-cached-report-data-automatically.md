---
title: "Creating Cached Report Data Automatically"
id: 1500009673401
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673401-Creating-Cached-Report-Data-Automatically
updated_at: 2021-07-24T20:54:07Z
---

# Creating Cached Report Data Automatically

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673381-Managing-Cached-Report-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673421-Scheduling-Cached-Report-Data-Results)

# Creating Cached Report Data Automatically

Cached report data (CRD) cannot be generated automatically by default. Administrators can enable the generation of auto CRD and configure the maximum hard disk space for auto CRD and how long an auto CRD can be kept.

**To enable creating cached report data automatically:**

1. On the Logi JReport Administration page, select **Cache** on the system toolbar and select **Data Cache** from the drop-down menu. The Cache - Data Cache page is displayed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920495383/mng_crd_pg.gif)
2. Select **Cache Configuration** on the task bar. This option is not available to [organization admins](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations).
3. Check **Automatic Cache** to enable creating cached report data automatically.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920496663/mng_crd_auto.gif)
4. In the Maximum Disk Usage text box, specify the maximum hard disk space for the automatically created CRD, which determines how many auto CRD can be held within one server session. The value should be between 4 MB and 1024\*1024 MB.
5. Specify how long an automatically cached data result can be kept
   within one server session.
   * **Never**  
      The auto CRD will not expire.
   * **Custom**  
      Specifies the period an auto CRD exists.
6. In the Maximum Memory Usage text field, specify the maximum memory usage when running reports using CRD. The value should be at least 4 MB and not more than 80% of the JVM current maximum heap size (-Xmx value in JRServer.bat). The number of MBs must be configured in whole numbers.

   All CRD (both auto CRD and [scheduled CRD](https://devnet.logianalytics.com/hc/en-us/articles/1500009673421-Scheduling-Cached-Report-Data-Results)) share the same memory space. If possible, set the maximum memory usage to a number that the memory can tolerate, for example, 1024 MB or bigger. The cache is used to improve performance when multiple users are running reports using the same CRD. Any size CRD can be accessed with even the smallest cache size. The larger the cache size the faster performance will be for concurrent users, but a large cache size may lower performance for users who do not use the CRD.
7. Select **OK** to apply the settings.

When automatic cache is enabled, while running a report, if there is no scheduled CRD created for the data resource that the report is using directly or indirectly (for example, the report is created based on a business view and the business view is built from a data resource), data will be fetched from the data resource, and at the same time the fetched data is cached and becomes an auto CRD.

When there are auto CRD generated for a data resource, the report running request based on the data resource will first search for the auto CRD that contains all the data required by the report. If an auto CRD is located, Logi JReport will retrieve data from the CRD to run the report; if no applicable auto CRD can be found, data is fetched from the DBMS and cached to be another auto CRD.

Auto CRD are only available within one server running life cycle, which means that once the server shuts down or restarts, they will be removed and a new cycle of auto CRD generation begins.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673381-Managing-Cached-Report-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673421-Scheduling-Cached-Report-Data-Results)
