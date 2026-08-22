---
title: "Configuring Logi Report Logging System"
id: 5741364633239
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741364633239-Configuring-Logi-Report-Logging-System
updated_at: 2022-10-31T17:16:00Z
---

# Configuring Logi Report Logging System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741401425047-Configuring-Connection-Pool)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741416077591-Configuring-Export-Settings)

# Configuring Logi Report Logging System

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")Logi Report provides a robust and flexible logging system that implements the SLF4J (Simple Logging Facade for Java) solution, enabling you to plug in the logging framework you want to use easily. This topic introduces the default Logi Report logging system that is based on Apache Log4j 2 and how you can configure it to serve your requirements. It also describes how you can use SLF4J with different logging frameworks in Server.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif)In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, see [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751-Statement-on-Log4j-and-Log4net-Vulnerabilities "Read this article to mitigate or remove a Log4j vulnerability from your version of Logi Report.").

When your Server enables the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations) feature, each organization has its own log files. By default, there are some .log files in the `<install_root>\logs` folder, for non-organization logs. For each organization there is a specific folder using the organization name and containing a set of log files for the organization. When system admin customizes settings about server log (for example, log level), Server applies the settings to all the organizations. Organization admin cannot configure logs.

This topic contains the following sections:

* [Using the Default Log4j 2-Based Logging System](#Default)
  + [Configuring Logs](#DConfig)
  + [Configuring Output Log Appenders](#DAppender)
  + [Setting the Log Level](#LogLevel)
* [Applying Another Logging Framework](#Another)
  + [Using SimpleLogger](#SimpleLogger)
  + [Using JUL (java.util.logging)](#JUL)
  + [Using Logevents](#Logevents)
  + [Using Log4j](#Log4j)
  + [Using reload4j](#reload4j)
  + [Using logback](#logback)
* [Configuring the Logging System on the Server Console](#ServerConsole)

## Using the Default Log4j 2-Based Logging System

Logi Report uses SLF4J with Apache Log4j 2 by default. This logging system has the following significant benefits:

* Easy to configure and manage.
* Compatible with your application that also uses the Log4j 2 libraries.
* Can be configured to output the log information of different modules separately or to output them all together.

### Configuring Logs

To configure the Logi Report's default logging system, choose one of the following:

* [Configure the Logging System on the Server Console](#ServerConsole)
* Use the **LogConfig.properties** file in `<install_root>\bin`.
* Use command options at [command-line startup](https://devnet.logianalytics.com/hc/en-us/articles/5741437885591-Running-Logi-Report-Server-as-a-Standalone-Server#OtherProperties).  
  + **-vDebug**  
    Set engine log file's log level to DEBUG.
  + **-vError**  
    Set engine log file's log level to ERROR.
  + **-logall]**  
    Set all loggers' log level to DEBUG.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* Any settings that you made using the command options override the log level setting in LogConfig.properties and on UI. To log on console when using the `-vDebug` or `-vError` option, you need to configure the appender in LogConfig.properties first.
* The use of the following conversion characters results in slow generation of caller class or location information: %C, %F, %L, and %M. You should avoid using them unless execution speed is not an issue. For more information about conversion pattern, see the comments in LogConfig.properties.

### Configuring Output Log Appenders

The default logging system of Logi Report provides certain appenders to which you can output the log content. By default, the output file is in
`<install_root>\logs`. For example:

* RollingFile
* DailyRollingFile
* Console

All the log categories use one appender by default, which is RollingFile. You can also define different output appenders or files for different log
categories in LogConfig.properties. For example, to add another log
appender, Console, you can edit LogConfig.properties
as follows:

`appenders=, RollingFile, Console  
...  
appender.console.type=Console  
appender.console.name=STDOUT  
appender.console.layout.type=PatternLayout  
appender.console.layout.pattern=%m[%p][%C]%n  
...`

### Setting the Log Level

The Logi Report logging system can trace both normal and abnormal situations using a log level, for example, something expected or regular such as tracing a program workflow, logging runtime information and associated elements, and something unexpected or irregular like when a URL is unreachable, a file does not exist, or a table cannot be found in a data source. Server divides log level into the following six levels, and order them according to the amount of information logged, from the least to the most. If you want to log the least amount of information, you can set the log level to **ERROR**. If you want to log the most amount of information, set log level to **TRACE**. Setting the highest level could affect system performance as well as disk usage.

* **OFF**  
  Server logs no information.
* **ERROR**  
  Server logs error events that may allow the application to continue running, such as failing to load a report, failing to find a catalog file, failing to parse a parameter, and failing to create a database buffer. Server also logs
  severe error events that presumably lead the application to abort, for example, failing to read the valid key, and exceptions that result in feature incomplete.
* **WARN**  
  Server logs potentially harmful situations, such as failing to find resources, or finding invalid queries or formulas with grammar errors when loading a catalog.
* **INFO**  
  Server logs an outline of program workflow, and dump global variables, including a single thread, multiple threads, the time for when to begin to fetch data, and success in exporting to the specified format.
* **DEBUG**  
  Server logs informational messages that highlight the application progress at a coarse-grained level, and important local variables, such as queries, parameters, formula values used when running reports, connection information, and SQL statements.
* **TRACE**  
  Server logs fine-grained informational events most useful in tracing an application, such as the report structure dump or report set dump.

## Applying Another Logging Framework

You can easily migrate to another logging framework in Server, by replacing the Log4j 2 libraries with the specific libraries of the logging framework.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) After changing the default logging framework Logi Report applies, you should use the corresponding libraries of the new logging framework when you call the Logi Report Java APIs.

### Using SimpleLogger

To log using SLF4J's SimpleLogger in Server, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl from `<install_root>\lib`, and add the two libraries of SimpleLogger, **slf4j-api** and **slf4j-simple** to the directory, for example, add slf4j-api-1.7.36.jar and slf4j-simple-1.7.36.jar.

You can configure the behavior of SimpleLogger by creating the **simplelogger.properties** configuration file and adding this file to the slf4j-simple library. For more information about SimpleLogger, go to <https://www.slf4j.org/api/org/slf4j/simple/SimpleLogger.html>. If you do not add the configuration file, Server outputs the log to **LogiReport.out.log** in `<install_root>\logs` by default, and you can use the `-Dorg.slf4j.simpleLogger.defaultLogLevel` option at command-line startup to specify the log level to be trace, debug, info, warn, or error.

### Using JUL (java.util.logging)

To log using SLF4J with JUL in Server, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl from `<install_root>\lib`, and add the JDK logging library **slf4j-jdk14** to the directory, for example, add slf4j-jdk14-1.7.36.jar.

You can perform logging configuration for JUL using its default configuration file **$JAVAHOME\jre\lib\logging.properties**. You can also create your own configuration file, and then use the `-Djava.util.logging.config.file` JVM option to add the file to the CLASSPATH environment variable of Server's startup file **JRServer.bat** in `<install_root>\bin`. For example:

`...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Djava.util.logging.config.file="C:\LogiReport\Server\mylog.properties" -Djreport.url.encoding="UTF-8"...`

For more information about JUL, go to <https://docs.oracle.com/javase/8/docs/technotes/guides/logging/index.html>.

### Using Logevents

To log using SLF4J with Logevents in Server, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl from `<install_root>\lib`, and add the two libraries of Logevents, **slf4j-api** and **logevents** to the directory, for example, add slf4j-api-1.7.36.jar and logevents-0.3.4.jar.

You can configure the behavior of Logevents by creating the **logevents.properties** configuration file in `<install_root>\bin`, and then using the `-Dlogevents.driectory` JVM option to add this file to the CLASSPATH environment variable of Server's startup file **JRServer.bat** in the same directory. For example:

`...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Dlogevents.directory="C://LogiReport//Server//logevents.properties" -Djreport.url.encoding="UTF-8"...`

If you do not add the configuration file, Server outputs the log to **LogiReport.out.log** in `<install_root>\logs` by default.

For more information about Logevents, go to <https://github.com/jhannes/logevents/blob/main/MANUAL.md>.

### Using Log4j

To log using SLF4J with Log4j in Server, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl from `<install_root>\lib`, and add the three libraries of Log4j, **log4j**, **slf4j-log4j12**, and **slf4j-api** to the directory, for example, add log4j-1.2.17.jar, slf4j-log4j12-1.7.25.jar, and slf4j-api-1.7.36.jar.

You can perform log configuration for Log4j by creating a configuration file, and then using the `-Dlog4j.configuration` JVM option to add this file to the CLASSPATH environment variable of Server's startup file **JRServer.bat** in `<install_root>\bin`. For example:

`...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Dlog4j.configuration="file:\C:\LogiReport\Server\log4j.properties" -Djreport.url.encoding="UTF-8"...`

For more information about Log4j, go to <https://logging.apache.org/log4j/1.2/manual.html>.

### Using reload4j

To log using SLF4J with reload4j in Server, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl from `<install_root>\lib`, and add the two libraries of reload4j, **reload4j** and **slf4j-reload4j** to the directory, for example, add reload4j-1.2.18.3.jar and slf4j-reload4j-1.7.36.jar.

You can perform log configuration for reload4j as you do for Log4j. For more information about reload4j, go to <https://reload4j.qos.ch/>.

### Using logback

To log using SLF4J with logback in Server, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl from `<install_root>\lib`, and add the two libraries of logback, **logback-classic** and **logback-core** to the directory, for example, add logback-classic-1.2.11.jar and logback-core-1.2.11.jar.

You can perform log configuration for logback by creating a configuration file, and then using the `-Dlogback.configurationFile` JVM option to add this file to the CLASSPATH environment variable of Server's startup file **JRServer.bat** in `<install_root>\bin`. For example:

`...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Dlogback.configurationFile="file:\C:\LogiReport\Server\logback.xml" -Djreport.url.encoding="UTF-8"...`

For more information about logback, go to <https://logback.qos.ch/documentation.html>.

## Configuring the Logging System on the Server Console

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** >  **Log**. Server displays the Log page.

   ![Log page](https://devnet.logianalytics.com/hc/article_attachments/9905779831447/config_log.gif)
2. From the **Log Type** drop-down list, select a log category.
   * **Engine**  
      Select the **Engine** log if you want to log the events related to running, creating, and exporting reports. Server uses the Engine to run reports.
   * **Page Report**  
      Select the **Page Report** log if you want to log the events related to modifying and saving page reports, including Ad Hoc and analysis features in Page Report Studio.
   * **Access**  
      Select the **Access** log if you want to log which users accessed report running and task scheduling services.
   * **Manage**  
      Select the **Manage** log if you want to log the events related to modifying settings on the Server Console or in the server.properties file.
   * **Error**  
      Select the **Error** log if you want to log errors in any of the categories.
   * **Event**  
      Select the **Event** log if you want to log the events related to the life cycle of the server instance, such as its start time and stop time.
   * **Debug**  
      Select the **Debug** log if you want to log the events most likely needed for debugging purposes, for instance, the SQL statements used to query the database.
   * **Performance**  
      Select the **Performance** log if you want to analyze the performance of reports or export operations.
   * **Dump**  
      Select the **Dump** log if you want to log events related to when an action started or ended during the process of running tasks. For example, when the task was submitted, when the task ran, when the Engine initiated, and when the Engine stopped.
3. From the **Log Level** drop-down list select the [log level](#LogLevel) of the specified log type.
4. From the **Additivity** drop-down list select **True** if you want child loggers to inherit all the appenders of the ancestors.
5. To output log contents to the FileAppender that requires a layout, select **File**, then:
   1. From the **Layout Type** drop-down list select the layout type you want to use to format the log contents: Pattern, HTML, XML, TTCC, or Simple.
   2. When you selected **Pattern** as the layout type, the **Pattern Conversion** option is available. Set the conversion pattern as required. The use of the following conversion characters results in slow generation of caller class or location information: %C, %F, %L and %M, so you should not use them unless execution speed is not an issue. For more information, see comments on conversion pattern in the **LogConfig.properties** file in the `<install_root>\bin` directory.
   3. In the **File Name** text box type the name of the log file to which you want the appender to output the log contents. The suffix of the log file name is .log. By default, Server saves the log file in the `<install_root>\logs` directory. However, you can
      type the file name with an absolute path to save the file to the location you want,
      for example, `E:/logs/Engine.log`.
   4. From the **Append** drop-down list select **False** if you want to replace the old contents of the specified file.
   5. From the **Buffered IO** drop-down list select **True** if you want to create a buffer for the log IO.
6. Server selects **RollingFile** by default, which outputs log contents to the RollingFileAppender that requires a layout. You can configure the [same settings](#File) as FileAppender for the RollingFileAppender. Besides, you can specify the maximum file size of the appender in the **Maximum File Size** text box (the logging system will create a new rolling file when the file size exceeds the maximum file size), and specify the maximum number of the latest rolling files that the logging system can retain, in the **Maximum Backup Index** text box.
7. To output log contents to the DailyRollingFileAppender that requires a layout, select **DailyRollingFile**, configure the [same settings](#File) as FileAppender, then in the **Date Pattern** text box specify the data pattern to generate the daily rolling file.
8. To output log contents to a remote log server, select **Socket**, then:
   1. In the **Remote Host** text box, specify the host name where the Socket Server is.
   2. In the **Port** text box, specify the port number on which the Socket Server listens.
   3. In the **Delay** text box, specify the timeout interval for when a client attempts to create a socket connection.
   4. From the **Location Information** drop-down list select **True** if you want to output the log location information to the socket stream.

   The SocketAppender does not need a layout.
9. To output log contents to a remote syslog daemon, select **Syslog**, then:
   1. From the **Layout Type** drop-down list select the layout type for formatting the log contents: Pattern, HTML, XML, TTCC, or Simple.
   2. When you selected **Pattern** as the layout type, you can see the **Pattern Conversion** option. Set the conversion pattern as required.
   3. In the **Syslog Host** text box type the host name where the Syslog server is.
   4. From the **Facility** drop-down list select the facility name that the Syslog uses.
   5. From the **Facility Printing** drop-down list select **True** if you want to print the facility information.
10. To output log contents to the standard stream of Java console, select **Console**. Then from the **Layout Type** drop-down list select the layout type for formatting the log contents. When you selected **Pattern** as the layout type, you can see the **Pattern Conversion** option. Set the conversion pattern as required. From the **Target** drop-down list select the standard IO target of the Console.
    * **System.out**  
       Select if you to output log contents to the standard output stream of the console.
    * **System.err**  
       Select if you to output log contents to the standard error stream of the console.
11. Select **Save** to apply the settings.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741401425047-Configuring-Connection-Pool)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741416077591-Configuring-Export-Settings)
