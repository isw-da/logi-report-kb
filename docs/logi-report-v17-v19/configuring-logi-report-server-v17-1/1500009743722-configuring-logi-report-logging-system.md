---
title: "Configuring Logi Report Logging System"
id: 1500009743722
section: "Configuring Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009743722-Configuring-Logi-Report-Logging-System
updated_at: 2021-07-24T00:49:26Z
---

# Configuring Logi Report Logging System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771641-Configuring-Connection-Pool)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743702-Configuring-Export-Settings)

# Configuring Logi Report Logging System

You can use the logging system to obtain meaningful and helpful Logi Report logging information conveniently. This topic describes how you can configure the logging system in the Server Console and using other methods.

Logi Report provides a robust, flexible, and configurable logging system that bases on log4j version 1.2.8. Logi Report also supports log4j versions from 1.2.8 to 1.3alpha7.

See the significant benefits of the Logi Report logging system:

* You can configure it to output the logging information of different modules separately or to output them all together.
* It is compatible with your application which is based on log4j.

When your Logi Report Server enables the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations) feature, each organization has its own log files. By default, there are some .log files in the `<install_root>\logs` folder, for non-organization logs. For each organization there is a specific folder using the organization name and containing a set of log files for the organization. When system admin customizes settings about server log (log level, etc.), Report Server applies the settings to all the organizations. Organization admin cannot configure logs.

**To configure the Logi Report logging system:**

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Configuration** >  **Log** from the drop-down menu. Server displays the Log page.

   ![Log page](https://devnet.logianalytics.com/hc/article_attachments/4404880564759/config_log.gif)
2. From the **Log Type** drop-down list, select a log category.
   * **Engine**  
      Uses the "Engine" log if you want to log the events related to running reports, that is creating report results or exporting reports. Logi Report Server uses the Engine component to run reports.
   * **Page Report**   
      Uses the "Page Report" log if you want to log the events related to end users modifying and saving page reports, including Ad Hoc and analysis features in Page Report Studio.
   * **Access**  
      Uses the "Access" log if you want to log which users accessed which services, such as report running service and task scheduling service.
   * **Manage**  
      Uses the "Manage" log if you want to log the events related to modifying settings in the Server Console or in server.properties.
   * **Error**  
      Uses the "Error" log if you want to log errors in any of the categories.
   * **Event**  
      Uses the "Event" log if you want to log the events related to the life cycle of the server instance, such as its start time and stop time.
   * **Debug**  
      Uses the "Debug" log if you want to log the events most likely needed for debugging purposes, such as the exact SQL statements used to query the database.
   * **Performance**  
      Uses the "Performance" log if you want to analyze the performance of report result or export operations.
   * **Dump**  
      Uses the "Dump" log if you want to log events related to at what time what action is started or ended during the process of running tasks. For example, when the task is submitted, when the task is run, when the Engine is initiated, and when the Engine is stopped.
3. From the **Log Level** drop-down list select the log level of the specified log type.

   The Logi Report logging system enables tracing using a log level in both normal and abnormal situations, for example, something expected or regular such as tracing a program workflow, logging runtime information and associated elements, and something unexpected or irregular like when a URL is unreachable, a file does not exist, or a table cannot be found in a data source. Log level is divided into the following eight levels, and is ordered according to the amount of information logged, from the least to the most. If you want the least amount of information to be logged, you can set log level to **FATAL**. If you want the most amount of information to be logged, you can set log level to **ALL**. Setting it to the highest level could affect system performance as well as disk usage.

   * **OFF**  
      Specifies not to use the log level.
   * **FATAL**  
      The FATAL level specifies severe error events that will presumably lead the application to abort, for example, failing to read the valid key, and exceptions that result in feature uncompleted.
   * **ERROR**  
      The ERROR level specifies error events that may allow the application to continue running, such as failing to load a report, failing to find a catalog file, failing to parse a parameter, and failing to create db buffer.
   * **WARN**  
      The WARN level specifies potentially harmful situations, such as failing to find the resource, or having found invalid query or formula with grammar error when loading a catalog.
   * **OUTLINE**  
      The OUTLINE level specifies an outline of program workflow, and dump global variables, including a single thread, multiple threads, the time for when to begin to fetch data, and success in exporting to the specified result format.
   * **INFO**  
      The INFO level specifies informational messages that highlight the application progress at a coarse-grained level, and important local variables, such as query, parameter, formula value used when running reports, connection information, and SQL statement.
   * **TRIVIAL**  
      The TRIVIAL Level specifies fine-grained informational events most useful in tracing an application. Such as the report structure dump, or the result set dump.
   * **ALL**  
      The ALL level logs all the information that the other levels log.
4. From the **Additivity** drop-down list specify whether a child logger will inherit all the appenders defined by its ancestors.
5. To output log contents to the FileAppender that requires a layout, select the **File** check box, then:
   1. From the Layout Type drop-down list select the layout type used to format the log contents: Pattern, HTML, XML, TTCC or Simple.
   2. When Pattern is selected as the layout type the Pattern Conversion option is available. Set the conversion pattern as required. The use of the following conversion characters results in the slow generation of caller class or location information: %C, %F, %L and %M , so their use should be avoided unless execution speed is not an issue. For more information about the pattern conversion see comments on conversion pattern in the LogConfig.properties file located in `<install_root>\bin` directory.
   3. In the File Name text box type the name of the log file to which the appender will output the log contents. The suffix of the log file name is .log. By default, the log file is saved in the `<install_root>\logs` directory, you can
      type the file name with an absolute path to save the file to your desired location,
      for example: `E:/logs/Engine.log`.
   4. From the Append drop-down list select whether to retain the old contents of the specified file.
   5. From the Buffered IO drop-down list specify whether to create a buffer for the log IO.
6. Report Server selects the **RollingFile** check box by default, which is to output log contents to the RollingFileAppender that requires a layout. You can configure the [same settings](#File) as FileAppender for the RollingFileAppender. Besides, you can specify the maximum file size of the appender in the **Maximum File Size** text box (the logging system will create a new rolling file when the file size exceeds the maximum file size) and specify the maximum number of the latest rolling files that the logging system can retain, in the **Maximum Backup Index** text box.
7. To output log contents to the DailyRollingFileAppender that requires a layout, select the **DailyRollingFile** check box, configure the [same settings](#File) as FileAppender, then in the **Date Pattern** text box specify the data pattern to generate the daily rolling file.
8. To output log contents to a remote log server, select the **Socket** check box, then:
   1. In the **Remote Host** text box, specify the host name where the Socket Server is located.
   2. In the **Port** text box, specify the port number on which the Socket Server listens.
   3. In the **Delay** text box, specify the timeout interval value for when a client attempts to create a socket connection.
   4. From the **Location Information** drop-down list select whether to output the log location information to the socket stream.

   The SocketAppender does not need a layout.
9. To output log contents to a remote syslog daemon, select the **Syslog** check box, then:
   1. From the **Layout Type** drop-down list select the layout type for formatting the log contents: Pattern, HTML, XML, TTCC, or Simple.
   2. When you select **Pattern** as the layout type you can see the Pattern Conversion option. Set the conversion pattern as required.
   3. In the **Syslog Host** text box specify the host name where the Syslog server is located.
   4. From the **Facility** drop-down list specify the facility name that the Syslog uses.
   5. From the **Facility Printing** drop-down list specify whether to print the facility information.
10. To output log contents to the standard stream of Java console, select the **Console** check box. Then from the **Layout Type** drop-down list select the layout type for formatting the log contents. When you select **Pattern** as the layout type you can see the **Pattern Conversion** option. Set the conversion pattern as required. From the **Target** drop-down list specify the standard IO target of the Console.
    * **System.out**  
       If selected, the log contents will be outputted to the standard output stream of the console.
    * **System.err**  
       If selected, the log contents will be outputted to the standard error stream of the console.
11. Select **Save** to apply the settings.

You can also configure the log by the following ways:

* Using the **LogConfig.properties** file in the `<install_root>\bin` directory.
* Using command options.  

  In comparison with earlier versions, the command options for log configuration have undergone a considerable change. The following table describes these options:

  | Options | Description |
  | --- | --- |
  | -vDebug | Enables Logi Report Engine to output messages to a file and sets engine log file's log level to INFO. |
  | -vError | Enables Logi Report Engine to output messages to a file and sets engine log file's log level to ERROR. |
  | -logall | Sets all loggers' log level to INFO. |
  | -log[:file Name] | Outputs the Logi Report Engine messages to the file as specified and uses the -vDebug level. |

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)Any settings that you made using the command options will override the log level setting in the LogConfig.properties file and on UI.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771641-Configuring-Connection-Pool)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743702-Configuring-Export-Settings)
