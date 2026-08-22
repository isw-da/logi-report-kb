---
title: "Tuning Server Performance"
id: 5741409384343
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741409384343-Tuning-Server-Performance
updated_at: 2022-10-31T17:16:01Z
---

# Tuning Server Performance

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741401150871-Changing-the-Server-Context-Path)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties)

# Tuning Server Performance

Many variables affect the performance of Logi Report Server, including the hardware and software environments. If you have the proper permissions, you can carry out performance tuning to make Logi Report Server faster, more efficient, and more reliable. This topic describes what you can do to tune your server performance.

This topic contains the following sections:

* [Factors That Help with the Server Performance](#Factor)
* [Preloading Catalogs and Reports](#Preload)
* [Customizing the Heartbeat Interval](#Heartbeat)
* [Configuring Table Pipeline](#TablePipeline)
* [Using the Action Task Manager](#ATM)
* [Limiting the Size of the Fetch Data Buffer](#Limit)
* [Canceling the Running Query](#Cancel)

## Factors That Help with the Server Performance

* Use Connection Pooling using either JNDI and the connection pool of the application server or Logi Report connection pool by configuring the [ConnectionPoolConfig.properties](https://devnet.logianalytics.com/hc/en-us/articles/5741401425047-Configuring-Connection-Pool) file.
* For each of your business views set **Prefetch=false** in Logi Report Designer if you only want to fetch the fields used in reports from the DBMS. The default value is **true**, so if you have a large business view with many fields yet you only use a few in reports, still Server consumes a lot of memory and network band width fetching data that the report does not need.
* For best performance and reliability you should [change the Logi Report Server DBMS](https://devnet.logianalytics.com/hc/en-us/articles/5741415979543-Configuring-Server-Databases-for-Server-Metadata-in-a-Standalone-Environment) from Derby, the internal Java DBMS, to your standard production DBMS or other DBMS you are familiar with. Server includes Derby for out of the box ease of use, but you should not use it for production use.
* Limiting the number of actively running reports can avoid momentary system overload. Setting the property [performance.max.reports](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#performance.max) to a limited number in the server.properties file in the `<install_root>\bin` directory can smooth out performance and provide higher overall throughput. The best number depends entirely on your environment, so you need to test which setting provides the highest throughput in your environment. A good starting point is the number of CPUs plus 2. For example, if you have a quad-core CPU, start out by setting the value to 6.
* When using an application server, you can achieve a similar result to [performance.max.reports](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#performance.max) by limiting the total number of active threads for Logi Report. Assume a report consumes around 5 threads on average, so setting the number of active threads to 50 is similar to setting performance.max.reports=10 but may provide better overall throughput since it is has finer granularity to control CPU utilization.
* [Cache catalogs, reports, and images](https://devnet.logianalytics.com/hc/en-us/articles/5741415874327-Configuring-Cache). This is effective when you use the same catalogs, templates, and images frequently, but may harm performance when you use many different catalogs, templates, and images and the requested resources are not in the cache. In this case, it slows performance checking the cache and wastes memory.
* [Preload catalogs and reports](#Preload). This improves the performance the first time you use the reports and catalogs.
* Set [log level](https://devnet.logianalytics.com/hc/en-us/articles/5741364633239-Configuring-Logi-Report-Logging-System#LogLevel) to record less information. In production servers log level should be **ERROR** unless you are searching for specific issues such as monitoring the SQL statements sent to the DBMS.
* [Convert reports from earlier versions to the current version](https://devnet.logianalytics.com/hc/en-us/articles/5741474096919-Converting-Resources-of-Earlier-Versions-to-the-Current-Version).
* [Set task-level timeout for advanced run and scheduled tasks](https://devnet.logianalytics.com/hc/en-us/articles/5741438263319-Managing-Report-Running-Tasks#Timeout). This ensures that users do not run extremely long jobs accidentally.
* Modify the JVM heap size. Again, this needs testing in your system to determine the best overall throughput. On 32-bit systems the maximum size is 2GB. However, on 64-bit systems the maximum size is extremely large. You can monitor the heap usage by tools such as the JDK JConsole application. Set a starting heap size just under your normal average usage (use -Xms in JRServer.sh/bat) and set the maximum heap (use -Xmx) to the maximum that you want the heap to grow. Logi Report can use additional heap to improve performance of queries, and sort and reduce the number of garbage collections (GC) which use CPU time. However, using too much memory for Java heap can impact performance of other applications. The maximum heap size is 1.4G by default.
* Set [queue.policy](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#queue.policy)=1, 2, or 3 in server.properties in the `<install_root>\bin` directory to turn on using priorities, so on demand reports will be higher than scheduled reports. Using the different policies, you can dynamically adjust priorities so reports increase their priority the longer they wait in the queue. You can also enable a third high priority queue for on demand reports which need to run immediately.
* Set [engine.single\_thread](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#engine.single_thread)=true or false in server.properties. Depending on your environment and JDK, some systems run faster with a single-threaded engine than with a multi-threaded engine. This needs tests in your environment to determine which setting provides the highest throughput. As a general rule, smaller systems are faster with this set to true, and larger systems are faster with it set to false.
* Set the maximum number of user handlers to the optimal size by setting the [httpserver.max.handlers](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#handler) property in the server.properties file. This is the number of threads which are waiting to handle user requests. Setting it larger than needed wastes resources; however, setting it too small means that some users will not be able to access reporting until someone else exits.
* Adjust the engine's utilization of the CPU in accordance with your requirements, by setting the [Engine Priority](https://devnet.logianalytics.com/hc/en-us/articles/5741401055383-Configuring-Advanced-Server-Settings#Engine) property to a higher or lower priority on the Administration > Configuration > Advanced page on the Server Console.
* Select the two properties [View Incomplete Pages and Format Page on Demand](https://devnet.logianalytics.com/hc/en-us/articles/5741427459479-Page-Report-Studio-Profile-Properties#RenderMode) in the Page Report Studio profile, for faster viewing the first page of large reports in Page Report Studio. The disadvantage is that to see the actual number of pages, calculate complete report totals, and create the TOC, you have to manually select the last page of the report.
* Be sure [performance.exe\_gc](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#performance.exe_gc)=false as the default in the server.properties file. This enables the JDK to schedule garbage collections rather than at specific times.
* To take less overhead for the Logi Report Server DBMS updates, you can set [Performance.commit.thread](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#performance.commit.thread)=true and [Performance.commit.interval](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#Performance.commit.interval)=30, so that commits of updates to the DBMS will be every 30 seconds rather than every write.
* If you have a very active server, it is more efficient to set [resource.result.life](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties#ResultLife) to 600, so that Server removes temporary files every 10 minutes rather than once per hour.
* Minimize the use of Word Wrap to columns which really need it. Word Wrap pre-formats the data in memory to determine its size, wrap the field as necessary, and then continue to format it.  If fields are never large enough to wrap, especially labels, it is a lot of overhead.
* True Type Fonts (TTF) provide better throughput by reducing font substitution and scaling time. Changing all the fonts to use TTF fonts improves the quality of the output as well as the performance when you are working on a mixture of operating systems such as report design on Windows and production on UNIX.
* Use binary versions of .cls and .cat, not the xml versions when you publish reports to Logi Report Server. This saves processing time and I/O time when converting the files to Java classes.
* The Quartz scheduler by default checks every 15 seconds (15000ms) to see if there are any scheduled reports that need to start. This requires queries to the DBMS to check the schedule times. By editing quartz.properties in `<install_root>\bin`, you can increase the time by updating org.quartz.scheduler.idleWaitTIme in milliseconds to the frequency you need. You can also adjust org.quartz.threadPool.threadCount to limit the number of threads starting scheduled reports. The default is 5.
* [Customize the heartbeat interval](#Heartbeat) for web browser products such as Web Report Studio, Page Report Studio, JDashboard, and Visual Analysis.
* [Use table pipeline](#TablePipeline) to speed up the rendering performance of tables involving millions of data records in Web Report Studio and JDashboard.
* Some Page Report Studio operations require a large amount of memory and CPU processing power. The [Action Task Manager](#ATM) improves Page Report Studio service performance by preventing a large number of actions from running simultaneously.
* [Limit the size of the fetch data buffer](#Limit) to retrieve a specified number of rows in each read instead of all rows.
* [Cancel the running query](#Cancel) used by a report in the database when you cancel the running task of the report.
* Select the Gear icon ![Shut Down the Server button](https://devnet.logianalytics.com/hc/article_attachments/9905715393943/btn_srv_shtdwn.gif) at the upper right of the Server Console and select **Garbage Collection** from the drop-down menu, to remove the unreferenced objects of Logi Report Server from heap memory.

## Preloading Catalogs and Reports

Administrators can preload catalogs, reports, analysis templates, as well as Java classes and fonts to improve performance.

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Performance**. Server displays the Performance page.

   ![Configure Performance](https://devnet.logianalytics.com/hc/article_attachments/9905779770263/config_perfmc_preld.gif)
2. Select **Add** beside the **Catalogs to Be Preloaded** box. Server displays a dialog box.
3. Select the ellipsis button ![Select Folder button](https://devnet.logianalytics.com/hc/article_attachments/9905758084119/btn_chsr3.gif) to select a folder or type the folder name with full path in the server resource tree directly, for example, `/SampleReports`. Server loads the catalogs in the folder.
4. Select a catalog.
5. Select a version of the catalog.
6. Select **OK**. Server displays the catalog in the **Catalogs to Be Preloaded** box.
7. Repeat the preceding steps to preload more catalogs.
8. To remove an unwanted catalog, select it and select **Remove**.
9. Select **Add** beside the **Reports to Be Preloaded** box. Server displays a dialog box.
10. Select the ellipsis button ![Select Folder button](https://devnet.logianalytics.com/hc/article_attachments/9905758084119/btn_chsr3.gif) to select a folder or type the folder name with full path in the server resource tree directly, for example, `/SampleReports`. Server loads the reports and analysis templates in the folder.
11. Select a report or analysis template.
12. Select a version of it.
13. Select **OK**. Server adds the report or analysis template in the **Reports to Be Preloaded** box.
14. Repeat the preceding steps to preload more reports and analysis templates.
15. To remove an unwanted report or analysis template, select it and select **Remove**.
16. To preload Java classes that the catalogs, reports, and Logi Report Engine use, select the corresponding options. Preloading some useful Java classes will improve performance. Otherwise, it will take some time for Logi Report Server to load any required Java classes each time generating reports. [Organization admin](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations) cannot use this feature.
17. To preload the fonts that reports use, select **Preload Fonts**. The option is not available to organization admin.
18. To compress the temporary data Server generates during runtime before swapping it to disk, select **Compress Swap Files**. By compressing swap files, the I/O efforts in certain circumstances may remarkably reduce, to improve the overall performance. This function is not available to organization admin.

    ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) Compressing swap files increases CPU pressure because it uses compress algorithm to shrink data. If your system already has high CPU usage, enabling this option brings extra performance impact, depending on different circumstances. Such impact may overcome the performance gain that comes from reducing I/O time.
19. Select **Save**.
20. Restart Logi Report Server to make the settings to take effect.

## Customizing the Heartbeat Interval

Logi Report Server introduces the heartbeat mechanism in Web Report Studio, Page Report Studio, JDashboard, and Visual Analysis. It works together with [User Session Timeout](https://devnet.logianalytics.com/hc/en-us/articles/5741401055383-Configuring-Advanced-Server-Settings#SessionTimeout) to release the unused resources of the products in time. Logi Report activates heartbeat by default. It begins to work after you open any of the products, by reporting to Server that the product is alive per a period of time in a way similar to heartbeats. If within 3 times of the heartbeat interval Server has not received a heartbeat, the product expires, and Server releases its resources.

Heartbeat stops in the following situations:

* You close the product or the related web browser.
* The computer powers off.
* No action happens to the product such as mouse move and automatic refresh until the session times out.

If the heartbeat interval is shorter than the user session timeout time that you configured in the Administration > Configuration > Advanced page, the session does not expire as long as there are heartbeats. If the heartbeat interval is longer than the session timeout time, the session expires when it times out.

You can use the following parameters for heartbeat:

* **jrd.heartbeat**  
   The heartbeat interval in milliseconds. The default value is 15000 milliseconds.
* **jrd.hbtimeout**  
   The period of time before heartbeat times out, in milliseconds. The default value is three times of the heartbeat interval.

You can configure heartbeat by adding the JVM parameter **-Djrd.heartbeat** and **-Djrd.hbtimeout** in the Logi Report Server startup file. In an integration environment, you can also specify the parameters in **web.xml**:

```
<context-param>  
    <param-name>jrd.heartbeat</param-name>  
    <param-value>15000</param-value>  
</context-param>  
<context-param>  
    <param-name>jrd.hbtimeout</param-name>  
    <param-value>45000</param-value>  
</context-param>
```

Heartbeat uses Web Worker technology of HTML5. Firefox, Chrome, and Safari can support Web Worker that works in a separate JavaScript thread.

## Configuring Table Pipeline

Table pipeline enables tables to show data as soon as there are data ready for the first page while partial summaries and the rest are still being processed in the background. By default, Server enables table pipeline to speed up the rendering performance of tables in web reports and dashboards that involve millions of data records.

**To configure table pipeline:**

1. Choose according to your user account:
   * Anyone can configure for themselves: navigate to the **My Profile** > **Customize Profile** page, then select **Customize Profile**. Server displays the [Customize Profile dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties). Select **Enable Customize Properties**.
   * Administrators can configure for all users: navigate to the **Administration** > **Server Profile** > **Customize Profile** page. Then, select **New Profile** if you want to create a new profile or select **Edit** to update an existing profile (later you need to make sure you select this profile as the default profile). Server displays a profile dialog box. Select **Common**.
2. Server selects **Table Pipeline** by default.
3. In the **Table Block Refresh Time** text box, specify the time interval in seconds for refreshing data so as to update partial data before the tables are fully ready.
4. Select **OK** to save the changes.

Table pipeline can work in most cases. However, when you apply the component-level sort to a table and the **Prefetch** property of the business view the table uses is **true**, in order to make table pipeline take effect, the table and all the other data components in the same web report or dashboard that use the same business view should have the same component-level sort setting: the same sort on field (sorting group by summary is excluded) and the same sort order.

In addition, if your report database is MySQL which fetches all data before returning the result set and Logi Report has to wait for the result set, the performance would not be much improved even when table pipeline is enabled. To solve the problem, you need to make fetch size work for MySQL in either ways:

* Set fetch size in the catalog database URL, for example, to set the fetch size to 20 records, the URL could be `jdbc:mysql://192.0.0.1:3306/test?useCursorFetch=true&defaultFetchSize=20`.
* Set fetch size in your code after connecting to the database and before sending SQL:

  ```
  con = DriverManager.getConnection(url);   
  ps = (PreparedStatement) con.prepareStatement(sql,ResultSet.TYPE_FORWARD_ONLY,ResultSet.CONCUR_READ_ONLY);   
  ps.setFetchSize(20);   
  ps.setFetchDirection(ResultSet.FETCH_REVERSE);   
  rs = ps.executeQuery();
  ```

## Using the Action Task Manager

The Action Task Manager coordinates Page Report Studio actions through two fixed-size tables:

* **Concurrent Processing Table** - This registers the requests that the Page Report Studio service is currently processing.
* **Waiting Requests Queue** - This registers the requests that are waiting for the Page Report Studio service to process.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) You need only prevent certain operations that consume considerable hardware resources from running at the same time. You can define the kind of requests to queue before processing them.

![Action Task Manager](https://devnet.logianalytics.com/hc/article_attachments/9905818389527/config_perfmc_atm.gif)

When a new Page Report Studio request reaches the server, it will be processed according to the following flow:

1. The Page Report Studio service determines whether the requested operation is a restricted action. If it is, the Action Task Manager will take over the request. Otherwise, it will be processed directly, without being managed by the Action Task Manager.
2. If the Concurrent Processing Table is full, the restricted request will be assigned to the Waiting Requests Queue. If the queue is full, the Page Report Studio service will refuse the request and return a warning message.
3. After the request has been processed, it will be de-registered from the Concurrent Processing table. The Page Report Studio service will then automatically continue to process the requests in the Waiting Requests Queue.

Using the property file **dhtml.properties** for Page Report Studio, you can balance the server load by adjusting table size and specify which kind of requests are managed by the Action Task Manager to queue page report actions to ensure Page Report Studio features do not take too many system resources and impact other functions.

**dhtml.properties**

The dhtml.properties file is in  `<install_root>\bin`. You can use it to control three major options for the Action Task Manager:

* **Specifying the size of the Concurrent Processing Table**

  Use `queue.actions.max.concurrent=[integer]` to set the maximum number of requests that can be processed simultaneously. The value of this property can be equal to or larger than 0. Use 0 (the default value) to disable the request queue feature.
* **Specifying the size of the Waiting Requests Queue table**

  Use `queue.actions.max.pending=[integer]` to set the maximum number of to-be-handled requests that the queue can contain. The value of this property can be equal to or larger than 0. 0 means no requests will be stored in the queue. A request will either be handled by the Page Report Studio service or be rejected when the maximum limit of the Concurrent Processing table has been reached.
* **Specifying the actions that can be applied for the Page Report Studio Request Queue feature**

  `queue.actions.init=false           
  # Action: Page report initialization  
   queue.actions.undo=true            
  # Action: Undo  
   queue.actions.redo=true            
  # Action: Redo  
   queue.actions.drill=true           
  # Action: Drilling  
   queue.actions.drillup=true         
  # Action: Drilling up  
   queue.actions.refresh=false        
  # Action: Refreshing  
   queue.actions.filter=true          
  # Action: Filtering  
   queue.actions.sort=true            
  # Action: Sorting  
   queue.actions.search=true          
  # Action: Searching  
   queue.actions.finishNewReport=true  # Action: Finishing
  creating a new report`

  The preceding properties only work when you enabled the queue feature by setting `queue.max.concurrent.actions>0`. You can set the properties to either true or false:

  **true** - The Action Task Manager will handle the action.  
  **false** - The Action Task Manager will not handle the action. The Page Report Studio service will directly process it without queuing it.

## Limiting the Size of the Fetch Data Buffer

If you are using a database which supports the JDBC method *Statement.setFetchSize()*, you can request the database to retrieve a specified number of rows in each read instead of all rows, by setting the property **setFetchSize** in the **JdbcDriversConfig.properties** file in the `<install_root>\bin` directory. This can minimize memory usage, improve performance, and avoid Java heap out of memory errors when doing large queries.

See the following example of setting the setFetchSize property in the JdbcDriversConfig.properties file and the description of each property:

`DriverName_D1 = MySQL-AB JDBC Driver  
Vendor_D1 = MySql.com  
Version_D1 = 3.0.8-stable ( $Date: 2003/05/19 00:57:19 $, $Revision: 1.27.2.18 $ )  
 setFetchSize_D1 = 5000`

* **DriverName\_[Name]**  
  The Database driver name that you use to establish a connection. You can use `connection.getMetaData().getDriverName()` to obtain the value.
* **Vendor\_[Name]**  
  The vendor of current JDBC driver. It is a string value.
* **Version\_[Name]**  
  The version of current JDBC driver. You can use `connection.getMetaData().getDriverVersion()` to obtain the value. The entire string must match completely.
* **setFetchSize\_[Name]**  
  The number of rows in each buffer that the database retrieves. It is an Integer value that should be larger than 0 and less than or equal to getMaxRows(). The default value is different according to the driver in use. You can refer to your own database driver specification.
* **\_[Name]**  
  It is a user defined name that you use to mark a group of driver settings different from the other groups.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* After you modify the JdbcDriversConfig.properties file, you need to start Server to load the changes.
* The Version information must match 100% with the version that the JDBC Driver returns, if not a full match Server ignores the settings without warning.
* If there is more than one group with the same group marking name, Server adopts the last group.
* Add the sign # before the "DriverName" of a group, or provide a negative value to the **setFetchSize** property, if you want to disable the whole group.

## Canceling the Running Query

If the JDBC driver of your report database supports the Cancel Running Query feature, you can ask Logi Report to cancel the running query used by a report in the database when you cancel the running task of the report, to reduce pressure on the database and to release resources as early as possible. To achieve this, configure the **JdbcDriversConfig.properties** file in the `<install_root>\bin` directory:

1. Add the JDBC driver you use into JdbcDriversConfig.properties if it is not there.
2. In JdbcDriversConfig.properties there is a line:

   `#supportCancelQueryStatement_D5=true`

   Remove the sign # and use your driver number instead of D5 to activate the feature.
3. Restart Logi Report Server to load the change.
4. Cancel the running task of a report, for example, select **Cancel** on the report processing page of Page Report Studio, or [stop a report running in the background mode](https://devnet.logianalytics.com/hc/en-us/articles/5741438263319-Managing-Report-Running-Tasks#ManageBack). Logi Report Server cancels the running query in the database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741401150871-Changing-the-Server-Context-Path)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties)
