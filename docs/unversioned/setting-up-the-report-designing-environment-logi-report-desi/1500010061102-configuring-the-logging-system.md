---
title: "Configuring the Logging System"
id: 1500010061102
section: "Setting Up the Report Designing Environment - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061102-Configuring-the-Logging-System
updated_at: 2022-10-14T07:15:59Z
---

# Configuring the Logging System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4404857194903-Updating-the-Designer-License-Key)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062842-Introducing-the-Designer-Reporting-Environment)

# Configuring the Logging System

Logi Report provides a robust, flexible, and configurable logging system that is based on Apache Log4j 2. You can use the logging system to obtain meaningful and helpful Logi Report log information in a convenient way. This topic describes the advantages of the Logi Report logging system and how you can configure it to serve your requirements.

This topic contains the following sections:

* [Benefits of the Logi Report Logging System](#Benefits)
* [Configuring Logs](#Log)
* [Configuring Output Log Appenders](#Appender)
* [Logging Information Using the Trace and Error Type](#Information)
* [Configuration Settings - Effect on Performance](#Effect)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

## Benefits of the Logi Report Logging System

The significant benefits of the Logi Report logging system are:

* It is easy to configure and manage.
* It is compatible with your application that also uses the Log4j library.
* It can be configured to output the log information of different modules separately or to output them all together.
* It supports setting levels of the trace and error types separately.

## Configuring Logs

You can perform the log configuration tasks in two ways:

* Using the LogConfig.properties file located in `<install_root>\bin` directory.
* Using command options.  

  In comparison with earlier versions, the command options used for log configuration have undergone a considerable change. The following are descriptions of these options:

  + **-vDebug**  
    Set engine log file's trace level to INFO and error level to WARN.
  + **-vError**  
    Set engine log file's trace level to OFF and error level to ERROR.
  + **-log[:<file>]**  
    Output message to the file as specified and uses the -vDebug level.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Any settings made using the command options override the trace and error type level settings in the LogConfig.properties file. To log on console when using the two commands above: -vDebug or -vError, you need to configure the appender in LogConfig.properties first.

## Configuring Output Log Appenders

The Logi Report logging system provides certain appenders to which you can output the log content. By default, the output file is located in the `<install_root>\logs` directory. For example:

* RollingFile
* DailyRollingFile
* Console

All the log categories use one appender by default, which is RollingFile. You can also define different output appenders or files for different log categories in the LogConfig.properties file. For example, to add another log appender, Console, you can edit LogConfig.properties as follows:

`log4j.logger.com.jinfonet.designer=, RollingFile, Console  
...  
log4j.appender.RootConsole=org.apache.log4j.ConsoleAppender  
log4j.appender.RootConsole.layout=com.jinfonet.util.JRPatternLayout  
log4j.appender.RootConsole.layout.ConversionPattern=%m [%t][%p][%d{HH:mm:ss,SSS}]%n  
log4j.appender.RootConsole.threshold=ON  
log4j.appender.RootConsole.target=System.out  
...`

## Logging Information Using the Trace and Error Type

The Logi Report logging system enables you to log situations by using the trace and error type.

* Trace - You can use this type for logging something expectable or regular, such as tracing a program workflow, logging runtime information, and associated elements.
* Error - You can use this type for logging something unexpected or irregular, for example, when a URL is unreachable, a file does not exist, or a table cannot be found in a data source.

Logi Report divides the trace type into four levels, and sorts them according to the amount of information logged, from the least to the most. These levels are OFF, OUTLINE, INFO, and TRIVIAL. Similarly, Logi Report divides the error type into four levels, and sorts them according to the amount of information logged, from the least to the most. These levels are OFF, FATAL, ERROR, and WARN. If you want the least amount of information to be logged, you can set the trace level to OUTLINE and error level to ERROR; if you want the most amount of information to be logged, you can set the trace level to TRIVIAL and error level to WARN. Setting the levels to the highest could affect system performance as well as disk usage.

The following explains the levels of each type. You can set the level appropriately so as to get the most helpful log information.

**Trace levels**

* **OFF**  
  It means not to use the Trace level.
* **OUTLINE**  
  The OUTLINE level specifies an outline of program workflow, and dump global variables, including a single thread, multiple threads, the time for when to begin to fetch data, and success in exporting to the specified result format.
* **INFO**  
  The INFO level specifies informational messages that highlight the application progress at a coarse-grained level, and important local variables, such as query, parameter, formula value used when running reports, connection information, and SQL statement.
* **TRIVIAL**  
  The TRIVIAL level specifies fine-grained informational events most useful in tracing an application, such as the report structure dump or the result set dump.

**Error levels**

* **OFF**  
  It means not to use the Error level.
* **FATAL**  
  The FATAL level specifies severe error events that presumably lead the application to abort, for example, failing to read the valid key, and exceptions that result in feature incomplete.
* **ERROR**  
  The ERROR level specifies error events that may allow the application to continue running, such as failing to load a report, failing to find a catalog file, failing to parse a parameter, and failing to create DB buffer.
* **WARN**  
  The WARN level specifies potentially harmful situations, such as failing to find the resource, or having found invalid query or formula with grammar error when loading a catalog.

## Configuration Settings - Effect on Performance

The configuration properties have effect on performance. Pay attention to the following when you configure the logging system:

* The levels of the trace and error types affect the amount of logging output. The higher the level, the more the output. However, the effect on performance is negligible.
* The use of the following conversion characters in the ConversionPattern property results in the slow generation of caller class or location information: %C, %F, %L, and %M. You should avoid using them unless execution speed is not an issue. For information about the ConversionPattern property, see the comments in LogConfig.properties.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4404857194903-Updating-the-Designer-License-Key)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062842-Introducing-the-Designer-Reporting-Environment)
