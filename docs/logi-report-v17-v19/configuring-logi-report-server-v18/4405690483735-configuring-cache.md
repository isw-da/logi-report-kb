---
title: "Configuring Cache"
id: 4405690483735
section: "Configuring Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690483735-Configuring-Cache
updated_at: 2022-01-27T07:58:30Z
---

# Configuring Cache

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683579799-Configuring-Advanced-Server-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile)

# Configuring Cache

Administrators can configure the cache settings of Logi Report Server. This topic describes how you can cache reports, catalogs, images, security objects, report datasets, and in-memory cubes.

* [Configuring Cube](#Cube)
* [Configuring Data Cache](#Data)
* [Configuring Report Cache](#Report)
* [Configuring Image Cache](#Image)
* [Configuring Security Cache](#Security)

## Configuring Cube

You can cache the aggregation objects of a business view as an in-memory cube, to improve the running performance of the reports that use the business view. For more information, select [Managing In-Memory Cubes](https://devnet.logianalytics.com/hc/en-us/articles/4405690641431-Managing-In-Memory-Cubes).

## Configuring Data Cache

Logi Report Server can cache the dataset of a report automatically when it runs the report, or you can schedule to cache the data without actually running a report. When a report has a cached data set, it will run with the data from the cache and not from the DBMS. See [Managing Cached Report Data](https://devnet.logianalytics.com/hc/en-us/articles/4405683922583-Managing-Cached-Report-Data) for more information.

## Configuring Report Cache

To improve performance, you can cache reports and catalogs into memory in advance so that Logi Report Server does not need to load them from disk when you run reports. Server clears the cached catalogs and reports from memory when it restarts.

**To configure the report cache of Logi Report Server:**

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Cache** > **Report Cache**. Server displays the Report Cache page.

   ![Configure Report Cache](https://devnet.logianalytics.com/hc/article_attachments/4420461728535/config_cache_rpt.gif)
2. Select **Cache Loaded Catalogs** if you want to keep catalogs in memory after you create reports using them. However, when running a report in Page Report Studio, Server does not cache its catalog even if you selected this option.
3. In the **Maximum Number of Catalogs to Be Cached** text box, type the maximum number of catalogs you want to cache in the memory.
4. The **Cached Catalogs** box lists the currently cached catalogs with their file paths in the server resource tree and catalog version numbers.

   To add a new catalog to the cache, select **Add**. Server displays a dialog box. Select the catalog you want to cache and its catalog version.

   To remove a cached catalog, select it in the Cached Catalogs box, then select **Remove**.
5. Select **Cache Loaded Reports** to keep reports in memory after they are generated.
6. In the **Maximum Number of Reports to Be Cached** text box, type the maximum number of reports you want to cache in the memory.

   Each cached report uses part of heap memory. If the heap is used up, Server throws an OutOfMemoryException. In JRServer.bat/sh, you can use the -Xms setting to specify the initial heap and -Xmx the maximum heap. For example, -Xms256m -Xmx1024m means that the initial heap is 256 MB and the maximum heap is 1024 MB. You can refer to the Java VM documents for more information.

   See the following example. The accuracy depends on your OS and VM.

   | Cache Size | Heap Size Required |
   | --- | --- |
   | 10 reports | 16 MB |
   | 30 reports | 25 MB |

   The default cache size is 10 reports and the default maximum heap space is 1024 MB. When you adjust the number, you should adjust the heap accordingly. The larger the heap space, the better the performance provided enough physical memory is available.
7. The **Cached Reports** box lists the currently cached reports with their file paths in the server resource tree and report version numbers.

   To add a new report to the cache, select **Add**. Server displays a dialog box. Select the report you want to cache and its report version.

   To remove a cached report, select it in the Cached Reports box, then select **Remove**.
8. Specify the buffer size for the sort action on page reports. Any change to the buffer size takes effect immediately. This setting is not available to [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations).
   * **System Managed Size**  
      Select to enable the system to automatically control the buffer size used in the RAM for each report when performing the sort action on page reports. Server stores all data for sorting in the RAM automatically.
   * **Custom Size**  
      Select to customize the buffer size used in the RAM for each report when performing the sort action on page reports. The default value is 16 MB, and the minimum size required by Logi Report is 4 MB. Server ignores any value smaller than 4 MB and uses 4 MB instead. If the amount of data for sorting is large, for instance, 5,000,000 records, but the buffer size is small, it will require a lot of IO and produce poor performance.
9. Select **Save** to apply the cache configuration.

## Configuring Image Cache

You can cache images used in reports and dashboards so that Logi Report Server does not need to load images from disk when you run reports and dashboards. Server clears the cached images from memory when it restarts.

**To configure the image cache of Logi Report Server:**

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Cache** >  **Image Cache**. Server displays the Image Cache page.

   ![Configure Image Cache](https://devnet.logianalytics.com/hc/article_attachments/4420453673495/config_cache_img.gif)
2. Select **Cache Images** to enable image cache.
3. Specify how you want to cache images.
   * **All Used Images**  
      Server caches all the images that are used in reports and dashboards.
   * **Maximum Image Cache Size**  
      Select this option if you want to configure the maximum size for caching images in the memory.
4. To view the information of the cached images, select **Show Details.** Server displays a table with the following columns:

   | Column | Description |
   | --- | --- |
   | Name | The name of the image. |
   | Size | The size of the image file. |
   | Catalog | The catalog file in which the image file is. |
   | Path | The path of the cached image in the server resource tree. |
   | Locked | The lock status of the image file. |

   You can edit the cached images in the table:

   * To add an image to the cache, select **Add**. Server displays a dialog box. Select an image you want to cache.
   * To lock an image, select it, and then select **Lock**. When you lock an image, Server always keeps it in the image cache until you remove it manually or restart Server. You can select multiple images and lock them at a time. To release the lock, select the images and select **Unlock**.
   * To remove an image from the cache, select it, and then select **Remove**. You can select **Remove All** to remove all the cached images.
5. Select **Save** to apply the cache configuration.

## Configuring Security Cache

The security cache system temporarily stores security objects such as users, roles, groups, and ACLs. For more information, see [Security Cache System](https://devnet.logianalytics.com/hc/en-us/articles/4405684018711-Security-Cache-System).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683579799-Configuring-Advanced-Server-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile)
