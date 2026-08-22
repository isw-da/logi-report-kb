---
title: "Configuring Cache"
id: 1500009771501
section: "Configuring Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771501-Configuring-Cache
updated_at: 2021-07-24T00:49:28Z
---

# Configuring Cache

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771481-Configuring-Advanced-Server-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile)

# Configuring Cache

Administrators can configure the cache settings of Logi Report Server. This topic describes how you can cache reports, catalogs, images, security objects, report datasets, and in-memory cubes.

* [Configuring Cube](#Cube)
* [Configuring Data Cache](#Data)
* [Configuring Report Cache](#Report)
* [Configuring Image Cache](#Image)
* [Configuring Security Cache](#Security)

## Configuring Cube

You can cache the aggregation objects of a business view as an in-memory cube, to improve the running performance of the reports that use the business view. For more information, select [Managing In-Memory Cubes](https://devnet.logianalytics.com/hc/en-us/articles/1500009777121-Managing-In-Memory-Cubes).

## Configuring Data Cache

Logi Report Server can cache the dataset of a report automatically when the report runs, or you can schedule to cache the data result without actually running a report. When a report has a cached result set, it will run with the data from the cache and not from the DBMS. See [Managing Cached Report Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009777101-Managing-Cached-Report-Data) for more information.

## Configuring Report Cache

To improve performance, you can cache reports and catalogs into memory in advance so that Logi Report Server does not need to load them from disk when you run reports. Logi Report Server will clear the cached catalogs and reports from memory when it restarts.

**To configure the report cache of Logi Report Server:**

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Configuration** > **Cache** > **Report Cache** from the drop-down menu. Server displays the Report Cache page.

   ![Configure Report Cache](https://devnet.logianalytics.com/hc/article_attachments/4404885608599/config_cache_rpt.gif)
2. Select **Cache Loaded Catalogs** if you want to keep catalogs in memory after the reports using them are generated. However, when a report runs in Page Report Studio, Report Server will not cache its catalog even when this option is selected.
3. In the **Maximum Number of Catalogs to Be Cached** text box, specify the maximum number of catalogs to cache in the memory. No more catalogs can be cached if this amount is reached.
4. The **Cached Catalogs** box lists the currently cached catalogs with their file path in the server resource tree and catalog version number.

   To add a new catalog to the list of catalogs to be cached, select the **Add** button. Server displays a dialog box. Select the catalog you want to cache and its catalog version.

   To remove a cached catalog, select it in the Cached Catalogs box, then select **Remove**.
5. Select **Cache Loaded Reports** to keep reports in memory after they are generated.
6. In the **Maximum Number of Reports to Be Cached** text box, specify the maximum number of reports to cache in the memory. No more reports can be cached if this amount is reached.

   Each cached report will use some heap memory. If the heap is used up, Report Server will throw an OutOfMemoryException. In JRServer.bat/sh the -Xms setting specifies the initial heap and *-*Xmx specifies the maximum heap. For example, -Xms256m -Xmx1024m means that the initial heap is 256MB and the maximum heap is 1024MB. You can refer to the Java VM documents for more information.

   See the following example. The accuracy depends on your OS and VM.

   | Cache Size | Heap Size Required |
   | --- | --- |
   | 10 reports | 16M |
   | 30 reports | 25M |

   The default cache size is 10 reports and the default maximum heap space is 1024MB. When you adjust the number, you should adjust the heap accordingly. The larger the heap space, the better the performance provided enough physical memory is available.
7. The **Cached Reports** box lists the currently cached reports with their file path in the server resource tree and report version number.

   To add a new report to the list of reports to be cached, select the **Add** button. Server displays a dialog box. Select the report you want to cache and its report version.

   To remove a cached report, select it in the Cached Reports box, then select **Remove**.
8. Specify the buffer size for the sort action on page reports as required. Any change to the buffer size takes effect immediately. This setting is not available to [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations).
   * **System Managed Size**  
      Specifies whether to enable the system to automatically control the buffer size used in the RAM for each report when performing the sort action on page reports. If selected, all data for sorting will be stored in the RAM automatically.
   * **Custom Size**  
      Specifies to customize the buffer size used in the RAM for each report when performing the sort action on page reports. The default value is 16 MB, and the minimum size required by Logi Report is 4 MB. Any value smaller than 4 MB will be ignored and use 4 MB instead, because if the amount of data for sorting is large (such as 5,000,000 records), but the buffer size that you configure is small, it will require a lot of IO and produce poor performance.
9. Select **Save** to apply the cache configuration.

## Configuring Image Cache

You can cache images used in reports and dashboards so that Logi Report Server does not need to load them from disk when you run them. Logi Report Server will clear the cached images from memory when it restarts.

**To configure the image cache of Logi Report Server:**

1. In the Server Console, point to **Administration** on the system toolbar, select **Configuration** > **Cache** >  **Image Cache** from the drop-down menu. Server displays the Image Cache page.

   ![Configure Image Cache](https://devnet.logianalytics.com/hc/article_attachments/4404885608855/config_cache_img.gif)
2. Select the **Cache Images** check box to enable image cache.
3. Specify how to cache the images.
   * **All Used Images**  
      If you select this option, Report Server will cache all the images that are used in reports and dashboards.
   * **Maximum Image Cache Size**  
      If you select this option, you can specify the maximum size for caching images in the memory. No more images can be cached if this size is reached.
4. To view the detailed information of the cached images, select **Show Details.** Server displays a table with the following columns:

   | Column | Description |
   | --- | --- |
   | Name | Displays the name of the image. |
   | Size | Displays the size of the image file. |
   | Catalog | Displays the catalog file in which the image file is. |
   | Path | Displays the path of the cached image in the server resource tree. |
   | Locked | Displays the lock status of the image file. |

   You can edit the cached images in the table as follows.

   * To add an image to be cached, select the **Add** button. Server displays a dialog box. Select the image you want to cache.
   * To lock an image, select it from the table, then select the **Lock** button. When an image is locked, Logi Report Server will always keep it in the image cache until you remove it manually or restart the server. You can select multiple images and lock them at a time. To release the lock, select the images and select **Unlock**.
   * To remove an image from the image cache, select it from the table, then select **Remove**. You can select **Remove All** to remove all the cached images.
5. Select **Save** to apply the cache configuration.

## Configuring Security Cache

The security cache system temporarily stores security objects such as users, roles, groups, and ACLs. For more information, see [Security Cache System](https://devnet.logianalytics.com/hc/en-us/articles/1500009778561-Security-Cache-System).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771481-Configuring-Advanced-Server-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile)
