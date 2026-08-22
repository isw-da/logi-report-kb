---
title: "Running Logi Report Server as a Standalone Server"
id: 4405690640535
section: "Starting, Accessing, and Shutting Down Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690640535-Running-Logi-Report-Server-as-a-Standalone-Server
updated_at: 2022-01-27T08:00:09Z
---

# Running Logi Report Server as a Standalone Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690638743-Setting-Up-Logi-Report-Server-Reporting-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683919383-Running-Logi-Report-Server-as-an-OS-Service)

# Running Logi Report Server as a Standalone Server

This topic describes how you can run Logi Report Server as a Standalone Server, using shortcuts, launch files, and Java.

This topic contains the following sections:

* [Starting Server Using Shortcuts](#Shortcut)
* [Starting Server Using Launch Files](#File)
* [Starting Server Using Java](#Java)

## Starting Server Using Shortcuts

After the installation finishes, Logi Report Server creates some shortcuts with which you can conveniently launch the Server.

**To start Logi Report Server using a shortcut:**

* Double-click the shortcut for Logi Report Server on your desktop.
* Select **Start Server** in the Logi Report folder on the Start menu.

## Starting Server Using Launch Files

After you have installed Logi Report Server, Server automatically generates many batch files in `<install_root>\bin`. They are for assisting you with using and maintaining Logi Report Server. You can edit the batch files to suit different circumstances. However, make sure that you understand their functions when you edit them.

See the Logi Report Server launch files in the following table.

| File | Description | Usage | Options |
| --- | --- | --- | --- |
| browser.bat | This tool detects the default client browser and installation path. [launchpad.bat](#launchpad) invokes it. | - | - |
| CmdSender.bat  CmdSender.sh | This tool is for sending commands to Logi Report Server. If you do not add the property "-s" or "-p", you should define the JVM system property "reporthome" so that CmdSender.bat/CmdSender.sh will use it to get data from the local machine. | cmdsender [-s:<server> -p:<port> -u:<user>] -w:<password> shutdown|localshutdown|(local:on|off) | * **-s**  The server host name. * **-p**  The server host port. * **-u**  The administrator username. * **-w**  The administrator password. * **shutdown**  Shut down the server. * **localshutdown**  Shut down the local server. * **local**  The administration tasks are available to local host only. * **gc**  Run the Java garbage collector. |
| DBMaintain.bat  DBMaintain.sh | This tool is for administrators to back up and restore Logi Report Server data. | DBMaintain -[?|cleanup|B<[systemtables|realmtables|profiling]:<filename>>|R<[systemtables|realmtables|profiling]:<filename>>] | * **-?**  Display the usage information and then exit. * **-cleanup**  Check the integrality of the server data and clean up the invalid data. * **-Bsystemtables:<filename>/-Brealmtables:<filename>/-Bprofiling:<filename>**  Back up the data in the database with the related data to a specified file. For example, to back up the server data realmtables to the file `c:\jsback.dat`, you can type:  `DBMaintain -Brealmtables:c:\jsback.dat` * **-B0realmtables:<filename>**  Only back up the data in the realm database. * **-Rsystemtables:<filename>/-Rrealmtables:<filename>/-Rprofiling:<filename>**  Restore the data including the related data outside the database from a specified file. For example, to restore server data realmtables from the file `c:\jsback.dat`, you can type:  `DBMaintain -Rrealmtables:c:\jsback.dat` * **-R0realmtables:<filename>**  Only restore the data in the realm database. |
| DJRServer.bat  DJRServer.sh | This tool launches Logi Report Server with debug and log information. The output log files are in the `<install_root>\logs` directory. In case of problems, you may run this batch to reproduce the problem. Open the files to see more information and find out the problem. You may have to send the log files to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) if you are unable to resolve the problem. | DJRServer [-?|-p <port>|-ap <adminport>|-realm <realmname>|-l backlog|-m <max>|-t <timeout>|-s <filename>|-web <directory>|-env|-silent||-local|-vDebug|-vError|-jrs.admin.server <host:port>|-cleanup] | * **-?**  Print the help message. * **-p <port>**  The port number to listen on. * **-ap <adminport>** The port number that the administration tools use. * **-realm <realmname>**  Active realm. * **-l <backlog>**  The maximum queue length for incoming connections. * **-m <max>**  The maximum number of connection handlers. * **-t <timeout>**  The connection timeout in milliseconds. * **-s <filename>**  The servlet property file name. If you do not provide this property, Server uses the file **servlet.properties** in `<install_root>\bin` as the servlet property file when launching Logi Report Server. * **-web <directory>**  The root directory when accessing the server via the web. Its default value is `<install_root>\public_html`. * **-env**  Print the environment. * **-silent**  No output to the console. * **-local**  The administration tasks are available on local host only. * **-vDebug** Logi Report Engine outputs messages to a file and sets all log files' log level to INFO. * **-vError** Logi Report Engine outputs messages to a file and sets all log files' log level to ERROR. * **-jrs.admin.server <host:port>**  The admin server host and RMI port. * **-cleanup**  Check the integrality of the server data and clean up the invalid data. |
| docker-container-migration.sh | [Select here](https://devnet.logianalytics.com/hc/en-us/articles/4405690618519-Migrating-Server-and-Server-Data#DataDocker) for more information. |  |  |
| JRServer.bat  JRServer.sh | This tool launches Logi Report Server in the standalone mode without any predefined properties. On Windows, you can start Server by double-clicking on JRServer.bat. If you cannot start Server in this way, Server displays the reason in the MS-DOS command console. | JRServer [-?|-p <port>|-ap <adminport>|-realm <realmname>|-l backlog|-m <max>|-t <timeout>|-s <filename>|-web <directory>|-env|-silent||-local|-vDebug|-vError|-logall|-jrs.admin.server <host:port>|-cleanup] Note icon   * You may need to set an appropriate property **-Dfile.encoding** in the file to start Logi Report Server to view characters correctly. * You may also need to set an appropriate property **-Dresolution** in the file to start Logi Report Server to set the system resolution in DPI. | * **-?**  Print the help message. * **-p <port>**  The port number to listen on. * **-ap <adminport>**  The port number that the administration tools use. * **-realm <realmname>**  Active realm. * **-l <backlog>**  The maximum queue length for incoming connections. * **-m <max>**  The maximum number of connection handlers. * **-t <timeout>**  The connection timeout in milliseconds. * **-s <filename>**  The servlet property file name. If you do not provide this property, Server uses the file servlet.properties in `<install_root>\bin` as the servlet property file when launching Logi Report Server. * **-web <directory>**  The root directory when accessing the server via the web. Its default value is `<install_root>\public_html`. * **-env**  Print the environment. * **-silent**  No output to the console. * **-local**  The administration tasks are available on local host only. * **-vDebug** Logi Report Engine outputs messages to a file and sets all log files' log level to INFO. * **-vError** Logi Report Engine outputs messages to a file and sets all log files' log level to ERROR. * **-log[:file Name]** (deprecated)  Output the Logi Report Engine messages to the log file as specified using the -vDebug level. * **-logall**  Set all loggers' log level to INFO. * **-jrs.admin.server <host:port>**  The admin server host and RMI port. * **-cleanup**  Check the integrality of the server data and clean up the invalid data. |
| jrenv.bat  jrenv.sh | This tool is for generating the report environment file **report.env** in the current directory. This file can help the Logi Analytics support staff assist you when you run into problems. | - | - |
| launchpad.bat | This tool starts Logi Report Server in the standalone mode and launches the Logi Report Server Start Page. | - | - |
| makewar.bat  makewar.sh | [Select here](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server#Tool) for more infomation. | - | - |
| MigrationBV52.bat  MigrationBV52.sh | This tool converts the resources from Logi Report versions lower than V5.2 Build 590 to the resources of Logi Report Server V8. If you install the new version to the same folder as the old one, you can omit the parameter. | MigrationBV52 [orgReportHome] | * **orgReporthome**  The reporthome of the original Logi Report Server. If you do not provide this parameter, Server uses the value of reporthome of new Logi Report Server. |
| MigrationV52.bat  MigrationV52.sh | This tool converts the resources of the versions between V5.2 Build 590 (included) and V6 (not included) to the resources of the latest Logi Report Server. If you install the new version to the same folder as the old one, you can omit the parameter. | MigrationV52 [orgReportHome] | * **orgReporthome**  The reporthome of the original Logi Report Server. If you do not provide this parameter, Server uses the value of reporthome of new Logi Report Server. |
| MigrationTool.bat  MigrationTool.sh | [Select here](https://devnet.logianalytics.com/hc/en-us/articles/4405690618519-Migrating-Server-and-Server-Data#Data) for more information. | - | - |
| NJRServer.bat  NJRServer.sh | This tool launches Logi Report Server without JIT option. If your server often stops responding with JIT option, try this batch file instead of **JRServer.bat**. | NJRServer [-?|-p <port>|-ap <adminport>|-realm <realmname>|-l backlog|-m <max>|-t <timeout>|-s <filename>|-web <directory>|-env|-silent||-local|-vDebug|-vError|-logall|-jrs.admin.server <host:port>|-cleanup] | * **-?**  Print the help message. * **-p <port>**  The port number to listen on. * **-ap <adminport>**  The port number that the administration tools use. * **-realm <realmname>**  Active realm. * **-l <backlog>**  The maximum queue length for incoming connections. * **-m <max>**  The maximum number of connection handlers. * **-t <timeout>**  The connection timeout in milliseconds. * **-s <filename>**  The servlet property file name. If you do not provide this property, Server uses the file **servlet.properties** in `<install_root>\bin` as the servlet property file when launching Logi Report Server. * **-web <directory>**  The root directory when accessing the server via the web. Its default value is `<install_root>\public_html`. * **-env**  Print the environment. * **-silent**  No output to the console. * **-local**  The administration tasks are available on local host only. * **-vDebug** Logi Report Engine outputs messages to a file and sets all log files' log level to INFO. * **-vError** Logi Report Engine outputs messages to a file and sets all log files' log level to ERROR. * **-log[:file Name]** (deprecated)  Output the Logi Report Engine messages to the log file as specified using the -vDebug level. * **-logall**  Set all loggers' log level to INFO. * **-jrs.admin.server <host:port>**  The admin server host and RMI port. * **-cleanup**  Check the integrality of the server data and clean up the invalid data. |
| register.bat | [browser.bat](#browser) invokes this file. | - | - |
| RMIAuthFileCreator.bat  RMIAuthFileCreator.sh | This tool generates the RMI authentication file. Logi Report Server uses the authentication file to secure remote objects. If you do not provde any properties, Server creates an authentication file named **rmi.auth** in  `<install_root>\bin`, using the user ID and install key of Logi Report Server. | RMIAuthFileCreator [authFileName [userid key]] | * **?**  Display the usage message. * **authFileName**  The RMI authentication file name. If you only provide this property, Server uses the user ID and install key of Logi Report Server to create the authentication file. * **userid**  The user ID to generate the contents of the authentication file. * **key**  The key to generate the contents of the authentication file. |
| rp.bat  rp.sh | This tool is for replacing user ID and license key. | rp UID Key | - |
| [rptconv.bat  rptconv.sh](#Example) | This tool is for converting old resources such as reports, visual analysis, library components, dashboards, and catalogs to be current version. | rptconv "-source=source\_path" ["-target=destination\_path"] [-r] [-s] | * **-source**  Source path of the resources that you want to convert. * **-target**   Destination path for the converted resources. * **-r**   Replace the source resource with the converted version. If you provide this property, Server ignores ["-target=destination\_path"].  If you provide neither "-r" nor "-target", Server saves the converted resources in the same directory as the source resources and names them as "converted\_SourceResourceName". * **-s**  Convert the resources in the specified directory, including the resources in the sub directories. |
| startConsole.bat | This tool launches the Server Console from the Start menu after Server starts. | - | - |
| stopServer.bat | This tool exits Logi Report Server from the Start menu. | - | - |
| stopServer.sh | This tool exits Logi Report Server. | - | - |

**Examples of running rptconv.bat/rptconv.sh to convert reports**

* **To convert a single resource:**

  `rptconv "-source=C:\LogiReport\Server\jreports\Payroll Report.cls" "–target=C:\temp"`

  This converts C:\LogiReport\Server\jreports\Payroll Report.cls to C:\temp\Payroll Report.cls.

  `rptconv "-source=C:\LogiReport\Server\jreports\Payroll Report.cls" "–target=C:\temp\1.cls.xml"`

  This converts C:\LogiReport\Server\jreports\Payroll Report.cls, saves the converted report to `C:\temp`, and names it as "1.cls.xml" (if license allows).

  `rptconv "-source=C:\LogiReport\Server\jreports\Payroll Report.cls"`

  This converts C:\LogiReport\Server\jreports\Payroll Report.cls, saves the converted report in the same directory, and names it as "converted\_Payroll Report.cls".

  `rptconv "-source=C:\LogiReport\Server\jreports\Payroll Report.cls" -r`

  This overwrites C:\LogiReport\Server\jreports\Payroll Report.cls.
* **To convert the resources (such as reports, visual analysis, library components, dashboards, and catalogs) in a directory:**

  `rptconv "-source=C:\LogiReport\Server\jreports" "–target=C:\temp"`

  This converts the resources in C:\LogiReport\Server\jreports and saves the converted resources to `C:\temp`. The converted resources use the same file names as source resources.

  `rptconv "-source=C:\LogiReport\Server\jreports" "–target=C:\temp" -s`

  This converts the resources in C:\LogiReport\Server\jreports and in the sub directories and saves the converted resources to `C:\temp`. The converted resources take the same file names and directory structure as source resources.

  `rptconv "-source=C:\LogiReport\Server\jreports" "–target=C:\temp\*.cls" -s`

  This converts the resources in C:\LogiReport\Server\jreports and in the sub directories and saves the converted resources to `C:\temp`. The converted resources take the same directory structure as source resources and the suffixes of their file names are all changed to ".cls".

  `rptconv "-source=C:\LogiReport\Server\jreports" -r -s`

  This converts the resources in C:\LogiReport\Server\jreports and in the sub directories. The converted resources overwrite the source resources.

  `rptconv "-source=C:\LogiReport\Server\jreports"`

  This converts the resources in C:\LogiReport\Server\jreports. Server saves the converted resources in the same directory and names them as "converted\_SourceResourceName".
* **To convert a type of resources with same suffixes in a directory:**

  The usage is similar to converting a directory. You can specify the wildcard to filter resources, for example:

  `rptconv "-source=C:\LogiReport\Server\jreports\*.cls" "–target=C:\temp"`

  This converts the reports with the suffix ".cls" in `C:\LogiReport\Server\jreports` and saves the converted reports to `C:\temp`.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* There must be one and only one catalog file in the directory where the resources you want to convert reside.
* If the resources that you want to convert contain UDO or UDF, make sure to include the corresponding classes or jars in the class path of rptconv.bat/rptconv.sh.

## Starting Server Using Java

The class of the standalone server is jet.server.JREntServer. You can start Logi Report Server with the following command instead of using the batch files:

`JAVA -classpath <classpath> -Djava.compiler=NONE -Dreporthome=<install_root> jet.server.JREntServer [options]`

* **-classpath**  
   The classpath must include the following packages originally in your `<install_root>\lib`: JRESServlets.jar; JREntServer.jar; JREngine.jar; jakarta.servlet-api-4.0.4.jar; log4j-core-2.17.1.jar; log4j-api-2.17.1.jar;
* **-Djava.compiler=NONE**  
   This is without JIT. This property is optional. However, if you encounter problems running the server and you think that they relate to the Java VM, you can try turning off the JIT compiler and then running again.
* **-Djreport.url.encoding**  
  The encoding to encode/decode escape characters in URL strings. If you do not provide this property, Server uses the system default encoding. For example: `java ... -Djreport.url.encoding=8859-1...`
* **-Dreporthome**  
   This is where you installed Logi Report Server. You need to provide this property. When you set the reporthome, upon launching, Logi Report will try to find the jslc.dat and report.ini files in  `<install_root>\bin` and check whether they are valid. Jslc.dat is the License control file. Open report.ini, and you will find the configuration information, including the temp, template, and the help path. Logi Report will use the temp path to export the temporary files so you should make sure that the temp folder specified in report.ini exists and has space available.
* **-Dfile.encoding**  
   The encoding to encode/decode escape characters in the server data. If you do not provide this property, Server uses the system default encoding. For example: `java ... -Dfile.encoding=8859-1...`
* **-Dresolution**  
   The system resolution in DPI. If you do not provide this property, Server uses the system default resolution, which is the resolution of your monitor. For example, `-Dresolution=96`.
* [**properties**]

  | Property | Description |
  | --- | --- |
  | -? | Print brief help message. |
  | -p port | The port that this server listens on. The default is 8888. |
  | -l backlog | Maximum length of queue for incoming connection indications. |
  | -m max | Maximum number of connection handlers. |
  | -t timeout | Connection timeout in milliseconds. |
  | -s filename | Servlet property file name. |
  | -realm realmname | Active realm when Server starts up. The specified realm should exist, otherwise Server uses an existing realm as the active realm. Server will then record a warning message in the log file, and set the selected active realm by the **server.realm.active** property in the **server.properties** file. |
  | -web directory | Web application server root directory. The default is `<install_root>\public_html`. |
  | -local | Administration on local host only. |
  | -vDebug | Logi Report Engine outputs messages to a file and sets engine log file's log level to INFO. |
  | -vError | Logi Report Engine outputs messages to a file and sets engine log file's log level to ERROR. |
  | -env | Print environment settings when Server starts up. |
  | -silent | Output nothing, not even the server start information. |
  | -log[:file Name] (deprecated) | Output the Logi Report Engine messages to the log file as specified using the -vDebug level. |
  | -logall | Set all loggers' log level to INFO. |
  | -jrs.admin.server host:port | The admin server host and RMI port. |
  | -cleanup | Check the integrality of the server data and clean up the invalid data. |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* For more information about how to configure the logging and debugging information, read the **LogConfig.properties** file in `<install_root>\bin`.
* You will use some of the common options in later topics. In addition, Logi Report has automatically generated batch files for you so that you do not have to write a complicated command line. You can find them in the `<install_root>\bin` directory.
* ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif)In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751-Statement-on-Log4j-and-Log4net-Vulnerabilities "Read this article to mitigate or remove a Log4j vulnerability from your version of Logi Report.").

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690638743-Setting-Up-Logi-Report-Server-Reporting-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683919383-Running-Logi-Report-Server-as-an-OS-Service)
