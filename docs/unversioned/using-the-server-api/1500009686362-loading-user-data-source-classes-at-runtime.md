---
title: "Loading User Data Source Classes at Runtime"
id: 1500009686362
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686362-Loading-User-Data-Source-Classes-at-Runtime
updated_at: 2021-11-03T06:58:34Z
---

# Loading User Data Source Classes at Runtime

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712021-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686282-Applying-a-User-Defined-CSS-to-an-HTML-Result-File)

# Loading User Data Source Classes at Runtime

Logi JReport allows you to create your reports using user data source (UDS), user-defined objects (UDO), and user-defined formulas (UDF). When you publish the reports using UDS, UDO or UDF to your production environment, Logi JReport requires the UDS, UDO or UDF jars to be in the class path or part of the EAR bundle. This might be difficult for you. You need to shut down your application and wrap the new UDS, UDO or UDF classes into the WAR or EAR or put them in the class path of the application server.

The feature Loading User Classes at Runtime can solve this issue. That is, for standalone Logi JReport Server, or in your embedded application server calling the Server API, you can control loading the classes at runtime without shutting down your application.

There are two important methods in the Server API that you need to call to dynamically load your UDS classes:

* **String jet.server.api.ServerEnv.getDynamicClassDir()**  
   Retrieves the path of the dynamic classes of the report server.
* **static void jet.server.api.engine.ReportEngineFactory.loadClasses(String path)**  
   Loads the dynamic classes from the location specified by the path parameter.

To load UDS classes, follow the steps below:

1. Specify a folder location on the machine where Logi JReport Server runs to hold all the UDS/UDO/UDF jar files, so that you can specify to load the classes from that folder. When Logi JReport Server initializes, you can specify the location in one of the following ways:
   * **Using the Server API static void jet.server.api.http.HttpUtil.initEnv(java.util.Properties props)**

     Use the key server.dynamic.class.dir to set the location, for example:

     `System.getProperties().put("server.dynamic.class.dir", "C:\\JReport\\Server\\dynamic");
     HttpUtil.initEnv(System.getProperties());`
   * **Using the option -Dserver.dynamic.class.dir in the server/application startup file**

     It will be loaded to system properties. Here is an example:

     -Dserver.dynamic.class.dir=*YOUR\_FOLDER*
   * **Using the property server.dynamic.class.dir in the server.properties file located in `<install_root>\bin`**

     The default value of this property is <install\_root>\dynamicclasses. Here is an example:

     server.dynamic.class.dir=*YOUR\_FOLDER*

   **Note:** In general, among the above three approaches, the first has the highest priority, and the third has the lowest.
2. Check the dynamic UDS/UDO/UDF folder any time by calling the method *static String jet.server.api.ServerEnv.getDynamicClassDir()*.

   Usage of the method:

   HttpUtil.getHttpRptServer().getServerEnv().getDynamicClassDir()

   Example:

   `System.out.println("Dynamic path"+httpRptServer.getServerEnv().getDynamicClassDir());`

   You can get the path's value in your own properties file. You can even copy your UDS/UDO/UDF jar files to the above folders programmatically.
3. Specify to load classes at runtime by calling the method *static void jet.server.api.engine.ReportEngineFactory.loadClasses(java.lang.String path)*. The parameter path is the dynamic class folder.

   For example:

   `ReportEngineFactory.loadClasses(httpRptServer.getServerEnv().getDynamicClassDir());`

**Notes (technical issues):**

* Only \*.jar or \*.zip packages in the specified folder including resource files (recommended \*.jar) will be loaded, which excludes the sub directories and unpackaged classes.
* If there are duplicated classes (having the same package and class name) in different \*.jar files, the default loading sequence is in time order. The latest modified file will be loaded first, and the older ones will be neglected.
* If you split one dynamic UDS classes into different \*.jar or \*.zip packages and also want to take advantage of dynamic loader, then you should follow the below rules:
  + The jar with the main class implementing JRUserDataSource class of the dynamic UDS must be in the dynamic class folder.
  + The classes in the \*.jar or \*.zip packages in the dynamic class folder can call or refer the classes under the JVM's class path, it cannot work in reverse.
* If your UDS classes also go to load the recourse files,
  + You should bundle the resource files into a jar no matter whether it is in the same class jar file or not.
  + In addition, the classes (in the \*.jar or \*.zip ) in the dynamic class folder can get the recourse files both in the dynamic class folder and under the JVM class path. However, the classes under the JVM class path cannot get the resource files in the dynamic class folder.
* When you call the API for loading the classes, Logi JReport Server will not kill the running catalogs and reports but run them using the old UDS classes, and freeze new reports until the loading action has finished.
* Logi JReport Server will try loading dynamic classes in the above way. If failed, it will try loading them in the traditional way (using the class path in the Logi JReport Server startup file, or EAR/EAR in embedded integration environment). Once it fails to find the classes, ClassNotFoundException will be thrown.
* For the UDO classes, only the creator class and render class can be loaded.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712021-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686282-Applying-a-User-Defined-CSS-to-an-HTML-Result-File)
