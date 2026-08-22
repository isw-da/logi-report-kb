---
title: "Configuring the Logging System"
id: 5735516331543
section: "Setting Up the Report Designing Environment - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735516331543-Configuring-the-Logging-System
updated_at: 2022-11-02T08:07:38Z
---

# Configuring the Logging System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532271383-Updating-the-Designer-License-Key)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/6417117277591-Configuring-Proxy-for-Connecting-to-REST-Web-Service)

# Configuring the Logging System

Logi Report provides a robust and flexible logging system that implements the SLF4J (Simple Logging Facade for Java) solution, enabling you to plug in the logging framework you want to use easily. This topic introduces the default Logi Report logging system that is based on Apache Log4j 2 and how you can configure it to serve your requirements. It also describes how you can use SLF4J with different logging frameworks in Designer.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9898419824023/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

This topic contains the following sections:

* [Using the Default Log4j 2-Based Logging System](#Default)
  + [Configuring Logs](#DConfig)
  + [Configuring Output Log Appenders](#DAppender)
  + [Setting the Log Level](#DLevel)
* [Applying Another Logging Framework](#Another)
  + [Using SimpleLogger](#SimpleLogger)
  + [Using JUL (java.util.logging)](#JUL)
  + [Using Logevents](#Logevents)
  + [Using Log4j](#Log4j)
  + [Using reload4j](#reload4j)
  + [Using logback](#logback)

## Using the Default Log4j 2-Based Logging System

Logi Report uses SLF4J with Apache Log4j 2 by default. This logging system has the following significant benefits:

* Easy to configure and manage.
* Compatible with your application that also uses the Log4j 2 libraries.
* Can be configured to output the log information of different modules separately or to output them all together.

### Configuring Logs

To configure the behavior of Logi Report's default logging system, perform either of the following:

* Use the **LogConfig.properties** file in the `<designer_install_root>\bin` directory.
* Use command options at [command-line startup](https://devnet.logianalytics.com/hc/en-us/articles/5735545183511-Starting-Designer-via-Command-Line).  
  + **-vDebug**  
    Set engine file's log level to INFO.
  + **-vError**  
    Set engine file's log level to ERROR.
  + **-log[:<file>]**  
    Output message to the specified file using the `-vDebug` level.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* Any settings made using the command options override the log level setting in LogConfig.properties. To log on console when using the `-vDebug` or `-vError` option, you need to configure the appender in LogConfig.properties first.
* The use of the following conversion characters results in slow generation of caller class or location information: %C, %F, %L, and %M. You should avoid using them unless execution speed is not an issue. For more information about conversion pattern, see the comments in LogConfig.properties.

### Configuring Output Log Appenders

The default logging system of Logi Report provides certain appenders to which you can output the log content. By default, the output file is in the
`<designer_install_root>\logs` directory. For example:

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

Logi Report's default logging system supports the following log levels, which are sorted according to the amount of the logged information, from the least to the most.

* **OFF**  
  No information logs.
* **ERROR**  
  The ERROR level specifies error events that may allow the application to continue running, such as failing to load a report, failing to find a catalog file, failing to parse a parameter, and failing to create DB buffer. It also specifies severe error events that presumably lead the application to abort, for example, failing to read the valid key, and exceptions that result in feature incomplete.
* **WARN**  
  The WARN level specifies potentially harmful situations, such as failing to find the resource, or having found invalid query or formula with grammar error when loading a catalog.
* **INFO**  
  The INFO level specifies an outline of program workflow, and dump global variables, including a single thread, multiple threads, the time for when to begin to fetch data, and success in exporting to the specified result format.
* **DEBUG**  
  The DEBUG level specifies informational messages that highlight the application progress at a coarse-grained level, and important local variables, such as query, parameter, formula value used when running reports, connection information, and SQL statement.
* **TRACE**  
  The TRACE level specifies fine-grained informational events most useful in tracing an application, such as the report structure dump or the result set dump.

You can specify the log level appropriately to get the most helpful log information. If you want to log the least amount of information, you can set the level to ERROR; if you want to log the most amount of information, set the level to TRACE. Setting the level to the highest could affect system performance and disk usage.

## Applying Another Logging Framework

You can easily migrate to another logging framework in Designer, by replacing the Log4j 2 libraries with the specific libraries of the logging framework.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) After changing the default logging framework Logi Report applies, you should use the corresponding libraries of the new logging framework when you call the Logi Report Java APIs.

### Using SimpleLogger

To log using SLF4J's SimpleLogger in Designer, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl in `<designer_install_root>\lib`, and add the two libraries of SimpleLogger, **slf4j-api** and **slf4j-simple** to the directory, for example, add slf4j-api-1.7.36.jar and slf4j-simple-1.7.36.jar.

You can configure the behavior of SimpleLogger by creating the **simplelogger.properties** configuration file and adding this file to the slf4j-simple library. For more information about SimpleLogger, go to <https://www.slf4j.org/api/org/slf4j/simple/SimpleLogger.html>. If you do not add the configuration file, Designer outputs the log to **LogiReport.out.log** in `<designer_install_root>\logs` by default, and you can use the `-Dorg.slf4j.simpleLogger.defaultLogLevel` option at [command-line startup](https://devnet.logianalytics.com/hc/en-us/articles/5735545183511-Starting-Designer-via-Command-Line) to specify the log level to be trace, debug, info, warn, error, or off.

### Using JUL (java.util.logging)

To log using SLF4J with JUL in Designer, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl in `<designer install_root>\lib`, and add the JDK logging library **slf4j-jdk14** to the directory, for example, add slf4j-jdk14-1.7.36.jar.

You can configure the behavior of JUL using its default configuration file **$JAVAHOME\jre\lib\logging.properties**. You can also create your own configuration file, and then use the `-Djava.util.logging.config.file` JVM option to add the file to the CLASSPATH environment variable of Designer's startup file **JReport.bat** in `<designer_install_root>\bin`, for example:

`...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Djava.util.logging.config.file="C:\LogiReport\Designer\mylog.properties" -Djreport.url.encoding="UTF-8"...`

For more information about JUL, go to <https://docs.oracle.com/javase/8/docs/technotes/guides/logging/index.html>.

### Using Logevents

To log using SLF4J with Logevents in Designer, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl in `<designer_install_root>\lib`, and add the two libraries of Logevents, **slf4j-api** and **logevents** to the directory, for example, add slf4j-api-1.7.36.jar and logevents-0.3.4.jar.

You can configure the behavior of Logevents by creating the **logevents.properties** configuration file in `<designer_install_root>\bin`, and then using the `-Dlogevents.driectory` JVM option to add this file to the CLASSPATH environment variable of Designer's startup file **JReport.bat** in the same directory, for example:

`...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Dlogevents.directory="C://LogiReport//Designer//logevents.properties" -Djreport.url.encoding="UTF-8"...`

If you do not add the configuration file, Designer outputs the log to **LogiReport.out.log** in `<designer_install_root>\logs` by default.

For more information about Logevents, go to <https://github.com/jhannes/logevents/blob/main/MANUAL.md>.

### Using Log4j

To log using SLF4J with Log4j in Designer, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl in `<designer_install_root>\lib`, and add the three libraries of Log4j, **log4j**, **slf4j-log4j12**, and **slf4j-api** to the directory, for example, add log4j-1.2.17.jar, slf4j-log4j12-1.7.25.jar, and slf4j-api-1.7.36.jar.

You can configure the behavior of Log4j by creating a configuration file, and then using the `-Dlog4j.configuration` JVM option to add this file to the CLASSPATH environment variable of Designer's startup file **JReport.bat** in `<designer_install_root>\bin`, for example:

`...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Dlog4j.configuration="file:\C:\LogiReport\Designer\log4j.properties" -Djreport.url.encoding="UTF-8"...`

For more information about Log4j, go to <https://logging.apache.org/log4j/1.2/manual.html>.

### Using reload4j

To log using SLF4J with reload4j in Designer, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl in `<designer_install_root>\lib`, and add the two libraries of reload4j, **reload4j** and **slf4j-reload4j** to the directory, for example, add reload4j-1.2.18.3.jar and slf4j-reload4j-1.7.36.jar.

You can perform log configuration for reload4j using the same method as you do for [Log4j](#Log4j). For more information about reload4j, go to <https://reload4j.qos.ch/>.

### Using logback

To log using SLF4J with logback in Designer, remove the three Log4j 2 libraries: log4j-api, log4j-core, and log4j-slf4j-impl in `<designer_install_root>\lib`, and add the two libraries of logback, **logback-classic** and **logback-core** to the directory, for example, add logback-classic-1.2.11.jar and logback-core-1.2.11.jar.

You can configure the behavior of logback by creating a configuration file, and then using the `-Dlogback.configurationFile` JVM option to add this file to the CLASSPATH environment variable of Designer's startup file **JReport.bat** in `<designer_install_root>\bin`, for example:

`...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Dlogback.configurationFile="file:\C:\LogiReport\Designer\logback.xml" -Djreport.url.encoding="UTF-8"...`

For more information about logback, go to <https://logback.qos.ch/documentation.html>.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532271383-Updating-the-Designer-License-Key)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/6417117277591-Configuring-Proxy-for-Connecting-to-REST-Web-Service)
