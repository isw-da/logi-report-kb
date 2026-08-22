---
title: "Configuring Logi Report Logging System"
id: 4405690489111
section: "Configuring Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690489111-Configuring-Logi-Report-Logging-System
updated_at: 2022-01-27T08:00:08Z
---

# Configuring Logi Report Logging System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690490903-Configuring-Connection-Pool)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690487319-Configuring-Export-Settings)

# Configuring Logi Report Logging System

You can use the logging system to obtain meaningful and helpful Logi Report logging information conveniently. This topic describes how you can configure the logging system on the Server Console and using other methods.

Logi Report provides a robust, flexible, and configurable logging system based on log4j 2.17.1.

See the significant benefits of the Logi Report logging system:

* You can configure it to output the logging information of different modules separately or to output them all together.
* It is compatible with your application which is based on log4j.

When your Logi Report Server enables the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations) feature, each organization has its own log files. By default, there are some .log files in the `<install_root>\logs` folder, for non-organization logs. For each organization there is a specific folder using the organization name and containing a set of log files for the organization. When system admin customizes settings about server log (for example, log level), Server applies the settings to all the organizations. Organization admin cannot configure logs.

**To configure the Logi Report logging system:**

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** >  **Log**. Server displays the Log page.

   ![Log page](https://devnet.logianalytics.com/hc/article_attachments/4420453671447/config_log.gif)
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
3. From the **Log Level** drop-down list select the log level of the specified log type.

   The Logi Report logging system can trace both normal and abnormal situations using a log level, for example, something expected or regular such as tracing a program workflow, logging runtime information and associated elements, and something unexpected or irregular like when a URL is unreachable, a file does not exist, or a table cannot be found in a data source. Server divides log level into the following eight levels, and order them according to the amount of information logged, from the least to the most. If you want to log the least amount of information, you can set log level to **FATAL**. If you want to log the most amount of information, you can set log level to **ALL**. Setting the highest level could affect system performance as well as disk usage.

   * **OFF**  
      Select if you do not want to use any log level.
   * **FATAL**  
      Select the **FATAL** level if you want to log severe error events that will presumably lead the application to abort, for example, failing to read the valid key, and exceptions that result in feature uncompleted.
   * **ERROR**  
      Select the **ERROR** level if you want to log error events that may allow the application to continue running, such as failing to load a report, failing to find a catalog file, failing to parse a parameter, and failing to create a database buffer.
   * **WARN**  
      Select the **WARN** level if you want to log potentially harmful situations, such as failing to find resources, or finding invalid queries or formulas with grammar errors when loading a catalog.
   * **OUTLINE**  
      Select the **OUTLINE** level if you want to log an outline of program workflow, and dump global variables, including a single thread, multiple threads, the time for when to begin to fetch data, and success in exporting to the specified format.
   * **INFO**  
      Select the **INFO** level if you want to log informational messages that highlight the application progress at a coarse-grained level, and important local variables, such as queries, parameters, formula values used when running reports, connection information, and SQL statements.
   * **TRIVIAL**  
      Select the **TRIVIAL** Level if you want to log fine-grained informational events most useful in tracing an application, such as the report structure dump, or the report set dump.
   * **ALL**  
      Select the **ALL** level if you want to log all the information that the other levels log.
4. From the **Additivity** drop-down list select **True** if you want child loggers to inherit all the appenders of the ancestors.
5. To output log contents to the FileAppender that requires a layout, select **File**, then:
   1. From the **Layout Type** drop-down list select the layout type you want to use to format the log contents: Pattern, HTML, XML, TTCC, or Simple.
   2. When you selected **Pattern** as the layout type, the **Pattern Conversion** option is available. Set the conversion pattern as required. The use of the following conversion characters results in slow generation of caller class or location information: %C, %F, %L and %M, so you should not use them unless execution speed is not an issue. For more information, see comments on conversion pattern in the **LogConfig.properties** file in the `<install_root>\bin` directory.
   3. In the **File Name** text box type the name of the log file to which you want the appender to output the log contents. The suffix of the log file name is .log. By default, Server saves the log file in the `<install_root>\logs` directory. However, you can
      type the file name with an absolute path to save the file to your desired location,
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

You can also configure the log by the following ways:

* Using the **LogConfig.properties** file in the `<install_root>\bin` directory.
* Using command options.  

  | Options | Description |
  | --- | --- |
  | -vDebug | Use this option if you want Logi Report Engine to output messages to a file and set engine log file's log level to INFO. |
  | -vError | Use this option if you want Logi Report Engine to output messages to a file and set engine log file's log level to ERROR. |
  | -logall | Use this option if you want to set all loggers' log level to INFO. |
  | -log[:file Name] | Use this option if you want to output the Logi Report Engine messages to the file as specified and use the -vDebug level. |

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) Any settings that you made using the command options will override the log level setting in the LogConfig.properties file and on UI.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif)In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751-Statement-on-Log4j-and-Log4net-Vulnerabilities "Read this article to mitigate or remove a Log4j vulnerability from your version of Logi Report.").

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690490903-Configuring-Connection-Pool)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690487319-Configuring-Export-Settings)
