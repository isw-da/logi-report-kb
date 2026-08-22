---
title: "Configuring Cache"
id: 1500009718762
section: "Configure Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718762-Configuring-Cache
updated_at: 2021-07-25T07:20:17Z
---

# Configuring Cache

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744721-Configuring-Advanced-Server-Settings)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile)

# Configuring Cache

Administrators can configure the following cache settings of Logi Report Server:

* [Configuring Cube](#Cube)
* [Configuring Data Cache](#Data)
* [Configuring Report Cache](#Report)
* [Configuring Image Cache](#Image)
* [Configuring Security Cache](#Security)

## Configuring Cube

The aggregation objects of a business view can be cached as in-memory cube so as to improve report running performance. For detailed information, see [Managing In-Memory Cubes](https://devnet.logianalytics.com/hc/en-us/articles/1500009750021-Managing-In-memory-Cubes).

## Configuring Data Cache

The Logi Report data cache system allows for caching the dataset of a report automatically when the report runs, as well as scheduling and caching the data result without actually running a report. When an end user selects a report that is linked to a cached result set, the data is retrieved from the cache and not from the DBMS. See [Managing Cached Report Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009750001-Managing-Cached-Report-Data) for detailed information.

## Configuring Report Cache

To improve performance, Logi Report Server enables you to cache reports and catalogs into memory so that they do not have to be loaded from disk when they are required. The cached catalogs and reports will be cleared from memory when Logi Report Server restarts.

**To configure the report cache of Logi Report Server:**

1. In the Logi Report Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Cache** > **Report Cache** from the drop-down menu to open the Report Cache page.

   ![Configure Report Cache](https://devnet.logianalytics.com/hc/article_attachments/4404936958871/config_cache_rpt.gif)
2. Select **Cache Loaded Catalogs** if you want to keep catalogs in memory after the reports using them are generated. If this option is unselected, after a report is generated, the catalog used to generate it will be removed from memory. However, when a report runs in Page Report Studio, its catalog will not be cached even when this option is selected.
3. In the Maximum Number of Catalogs to Be Cached text box, specify the maximum number of catalogs that can be cached by the server in its memory. No more catalogs can be cached if this amount is reached.
4. The Cached Catalogs box lists the currently cached catalogs with their file path in the server resource tree and catalog version number.

   To add a new catalog to the list of catalogs to be cached, select the **Add** button. In the displayed dialog box, select the catalog you want to cache and its catalog version.

   To remove a cached catalog, select it in the Cached Catalogs box, then select **Remove**.
5. Select **Cache Loaded Reports** to keep reports in memory after they are generated. If this options is unselected, after a report is generated Logi Report will remove it from memory.
6. In the Maximum Number of Reports to Be Cached text box, specify the maximum number of reports that can be cached by the server in its memory. No more reports can be cached if this amount is reached.

   Each cached report will use some heap memory. If the heap is used up, an OutOfMemoryException will be thrown. In JRServer.bat/sh the -Xms setting specifies the initial heap and *-*Xmx specifies the maximum heap. For example, -Xms256m -Xmx1024m means that the initial heap is 256MB and the maximum heap is 1024MB. You can refer to the documents of the Java VM for more information.

   Here is an example, the accuracy depends on your OS and VM:

   | Cache Size | Heap Size Required |
   | --- | --- |
   | 10 reports | 16M |
   | 30 reports | 25M |

   The default cache size is 10 reports and the default maximum heap space is 1024MB. When you adjust the number, you should adjust the heap accordingly. The larger the heap space, the better the performance provided enough physical memory is available.
7. The Cached Reports box lists the currently cached reports with their file path in the server resource tree and report version number.

   To add a new report to the list of reports to be cached, select the **Add** button. In the displayed dialog box, select the report you want to cache and its report version.

   To remove a cached report, select it in the Cached Reports box, then select **Remove**.
8. Specify the buffer size for the sort action on page reports as required. Any change to the buffer size takes effect immediately. This setting is not available to [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations).
   * **System Managed Size**  
      Specifies whether to allow the system to automatically control the buffer size used in the RAM for each report when performing the sort action on page reports. If selected, all data for sorting will be stored in the RAM automatically.
   * **Custom Size**  
      Specifies to customize the buffer size used in the RAM for each report when performing the sort action on page reports. The default value is 16 MB, and the minimum size required by Logi Report is 4 MB. Any value smaller than 4 MB will be ignored and use 4 MB instead, because if the amount of data for sorting is large (such as 5,000,000 records), but the buffer size that you configure is small, it will require a lot of IO and produce poor performance.
9. Select **Save** to apply the cache configuration.

## Configuring Image Cache

Image cache allows you to cache images used in reports and dashboards so that they do not have to be loaded from disk when they are required. The cached images will be cleared from memory when Logi Report Server restarts.

**To configure the image cache of Logi Report Server:**

1. In the Logi Report Server console, point to **Administration** on the system toolbar, select **Configuration** > **Cache** >  **Image Cache** from the drop-down menu to open the Image Cache page.

   ![Configure Image Cache](https://devnet.logianalytics.com/hc/article_attachments/4404936959127/config_cache_img.gif)
2. Select the **Cache Images** check box to enable image cache.
3. Specify how to cache the images.
   * **All Used Images**  
      If selected, all the images that are used in reports and dashboards will be cached.
   * **Maximum Image Cache Size**  
      If selected, you can specify a maximum size that can be used to cache images by the server in its memory. No more images can be cached if this size is reached.
4. To view the detailed information of the cached images, select **Show Details.** The cached image table displays with the following columns:

   | Column | Description |
   | --- | --- |
   | Name | Displays the name of the image. |
   | Size | Displays the size of the image file. |
   | Catalog | Displays the catalog file in which the image file is. |
   | Path | Displays the path of the cached image in the server resource tree. |
   | Locked | Displays the lock status of the image file. |

   You can edit the cached images in the table as follows.

   * To add an image to be cached, select the **Add** button. In the displayed dialog box, select the image you want to cache.
   * To lock an image, select it from the table, then select the **Lock** button. When an image is locked, it will be always kept in the image cache until you remove it manually or restart Logi Report Server. You can select multiple images and lock them at a time. To release the lock, select the images and select **Unlock**.
   * To remove an image from the image cache, select it from the table, then select **Remove**. Select **Remove All** to remove all the cached images.
5. Select **Save** to apply the cache configuration.

## Configuring Security Cache

The security cache system temporarily stores security objects such as users, roles, groups and ACLs. For detailed information, see [Security Cache System](https://devnet.logianalytics.com/hc/en-us/articles/1500009751221-Security-Cache-System).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744721-Configuring-Advanced-Server-Settings)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile)
