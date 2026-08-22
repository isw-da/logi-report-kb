---
title: "Configuring the Logging System"
id: 4405664603159
section: "Setting Up the Report Designing Environment - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664603159-Configuring-the-Logging-System
updated_at: 2022-10-14T07:11:03Z
---

# Configuring the Logging System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664605079-Updating-the-Designer-License-Key)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661947543-Introducing-the-Designer-Reporting-Environment)

# Configuring the Logging System

Logi Report provides a robust, flexible, and configurable logging system that is based on Apache Log4j 2. You can use the logging system to obtain meaningful and helpful Logi Report log information in a convenient way. This topic describes the benefits of the Logi Report logging system and how you can configure it to serve your requirements.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420542088087/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

This topic contains the following sections:

* [Benefits of the Logi Report Logging System](#Benefits)
* [Configuring Logs](#Log)
* [Configuring Output Log Appenders](#Appender)
* [Setting the Log Level](#Level)
* [Effect of Log Configurations on Performance](#Effect)

## Benefits of the Logi Report Logging System

The significant benefits of the Logi Report logging system are:

* Easy to configure and manage.
* Compatible with your application that also uses the Log4j library.
* Can be configured to output the log information of different modules separately or to output them all together.

## Configuring Logs

You can perform the log configuration tasks in two ways:

* Use the file **LogConfig.properties** located in the `<install_root>\bin` directory.
* Use command options.  

  In comparison with earlier versions, the command options used for log configuration have undergone a considerable change. The following are descriptions of these options:

  + **-vDebug**  
    Set engine file's log level to INFO.
  + **-vError**  
    Set engine file's log level to ERROR.
  + **-log[:<file>]**  
    Output message to the file as specified using the -vDebug level.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Any settings made using command options override the log level setting in LogConfig.properties. To log on console when using the two commands: -vDebug or -vError, you need to configure the appender in LogConfig.properties first.

## Configuring Output Log Appenders

The Logi Report logging system provides certain appenders, to which you can output the log content. By default, the output file is located in the `<install_root>\logs` directory. For example:

* RollingFile
* DailyRollingFile
* Console

All the log categories use one appender by default, which is RollingFile. You can also define different output appenders or files for different log categories in LogConfig.properties. For example, to add another log appender, Console, you can edit LogConfig.properties as follows:

`appenders=, RollingFile, Console  
...  
appender.console.type=Console  
appender.console.name=STDOUT  
appender.console.layout.type=PatternLayout  
appender.console.layout.pattern=%m[%p][%C]%n  
...`

## Setting the Log Level

Logi Report supports the following log levels and sorts them according to the amount of the logged information, from the least to the most. You can specify the log level appropriately to get the most helpful log information. If you want to log the least amount of information, you can set the level to FATAL; if you want to log the most amount of information, set the level to TRIVIAL. Setting the level to the highest could affect system performance and disk usage.

* **OFF**  
  No information logs.
* **FATAL**  
  The FATAL level specifies severe error events that presumably lead the application to abort, for example, failing to read the valid key, and exceptions that result in feature incomplete.
* **ERROR**  
  The ERROR level specifies error events that may allow the application to continue running, such as failing to load a report, failing to find a catalog file, failing to parse a parameter, and failing to create DB buffer.
* **WARN**  
  The WARN level specifies potentially harmful situations, such as failing to find the resource, or having found invalid query or formula with grammar error when loading a catalog.
* **OUTLINE**  
  The OUTLINE level specifies an outline of program workflow, and dump global variables, including a single thread, multiple threads, the time for when to begin to fetch data, and success in exporting to the specified result format.
* **INFO**  
  The INFO level specifies informational messages that highlight the application progress at a coarse-grained level, and important local variables, such as query, parameter, formula value used when running reports, connection information, and SQL statement.
* **TRIVIAL**  
  The TRIVIAL level specifies fine-grained informational events most useful in tracing an application, such as the report structure dump or the result set dump.

## Effect of Log Configurations on Performance

The configuration properties have effect on performance. Pay attention to the following when you configure the logging system:

* The log level affects the amount of logging output. The higher the level, the more the output; however, the effect on performance is negligible.
* The use of the following conversion characters results in slow generation of caller class or location information: %C, %F, %L, and %M. You should avoid using them unless execution speed is not an issue. For more information about conversion pattern, see the comments in LogConfig.properties.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664605079-Updating-the-Designer-License-Key)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661947543-Introducing-the-Designer-Reporting-Environment)
