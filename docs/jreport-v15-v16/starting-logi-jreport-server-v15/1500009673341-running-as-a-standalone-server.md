---
title: "Running as a Standalone Server"
id: 1500009673341
section: "Starting Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673341-Running-as-a-Standalone-Server
updated_at: 2021-07-24T20:54:07Z
---

# Running as a Standalone Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648622-Setting-Up-the-Reporting-Environment)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648642-Running-as-an-OS-Service)

# Running as a Standalone Server

This topic introduces how to run Logi JReport Server Guide v15 Server as a standalone server.

Below is a list of the sections covered in this topic:

* [Starting Using Shortcuts](#Shortcut)
* [Starting Using Launch Files](#File)
* [Starting Using Java](#Java)

## Starting Using Shortcuts

After the installation finishes, some shortcuts are created with which you can conveniently launch Logi JReport Server.

**To start Logi JReport Server using shortcut:**

* Double-select the **Logi JReport Server 15** shortcut on your desktop.
* Select **Start** > **Logi JReport 15** > **Start Server**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Starting Using Launch Files

After you have installed Logi JReport Server, many batch files are automatically generated in `<install_root>\bin`. They are for assisting you with using and maintaining Logi JReport Server. All of these batch files can be edited to suit different circumstances. However, make sure that you understand their functions when you want to edit them.

The following table lists the Logi JReport Server launch files.

| File | Description | Usage | Options |
| --- | --- | --- | --- |
| browser.bat | This tool detects the default client browser and installation path. It is invoked by [launchpad.bat](#launchpad). | - | - |
| CmdSender.bat  CmdSender.sh | This tool is for sending commands to Logi JReport Server. If the option "-s" or "-p" is not used, the JVM system property "reporthome" must be defined so that CmdSender.bat/CmdSender.sh will use it to get data from the local machine. | cmdsender [-s:<server> -p:<port> -u:<user>] -w:<password> shutdown|localshutdown|(local:on|off) | * **-s**  The server host name. * **-p**  The administration port. * **-u**  The admin user name. * **-w**  The admin password. * **shutdown**  Shuts down the server. * **localshutdown**  Shuts down the local server. * **local**  The administration tasks are available to local host only. * **gc**  Run the Java garbage collector. |
| DBMaintain.bat  DBMaintain.sh | This tool is for administrators to back up and restore Logi JReport Server data. | DBMaintain -[?|cleanup|B<[systemtables|realmtables|profiling]:<filename>>|R<[systemtables|realmtables|profiling]:<filename>>] | * **-?**  Displays the usage information and then exits. * **-cleanup**  Checks integrality of the server data and cleans up the invalid data. * **-Bsystemtables:<filename>/-Brealmtables:<filename>/-Bprofiling:<filename>**  Backs up the data in the database with the related data to a specified file. For example, for backing up the server data realmtables to file `c:\jsback.dat`, you can type:  `DBMaintain -Brealmtables:c:\jsback.dat` * **-B0realmtables:<filename>**  Only backs up the data in the realm database. * **-Rsystemtables:<filename>/-Rrealmtables:<filename>/-Rprofiling:<filename>**  Restores the data including the related data outside the database from a specified file. For example, for restoring server data realmtables from the file `c:\jsback.dat`, you can type:  `DBMaintain -Rrealmtables:c:\jsback.dat` * **-R0realmtables:<filename>**  Only restores the data in the realm database. |
| DJRServer.bat  DJRServer.sh | This tool is used to launch Logi JReport Server with debug and log information. The output log files are in the `<install_root>\logs` directory. In case of problems, you may run this batch to reproduce the problem. Open the files to see the detail information and find out the problem. Send the log files to [support@jinfonet.com](mailto:support@jinfonet.com) if you are unable to resolve the problem. | DJRServer [-?|-p <port>|-ap <adminport>|-realm <realmname>|-l backlog|-m <max>|-t <timeout>|-s <filename>|-web <directory>|-env|-silent||-local|-vDebug|-vError|-jrs.admin.server <host:port>|-cleanup] | * **-?**  Prints this help message. * **-p <port>**  The port number to listen on. * **-ap <adminport>** The port number which is used by the administration tools. * **-realm <realmname>**  Specifies the active realm. * **-l <backlog>**  The maximum queue length for incoming connections. * **-m <max>**  The maximum number of connection handlers. * **-t <timeout>**  The connection timeout in milliseconds. * **-s <filename>**  The servlet property file name. If this option is not used, the file servlet.properties in `<install_root>\bin` will be used as the servlet property file when launching Logi JReport Server. * **-web <directory>**  The root directory when accessing the server via the web. Its default value is `<intall_root>\public_html`. * **-env**  Prints the environment. * **-silent**  No output is sent to the console. * **-local**  The administration tasks are available on local host only. * **-vDebug**  Enables Logi JReport Engine to output messages to a file and sets all log files' log level to INFO. * **-vError**  Enables Logi JReport Engine to output messages to a file and sets all log files' log level to ERROR. * **-jrs.admin.server <host:port>**  The admin server host and RMI port. * **-cleanup**  Checks integrality of the server data and cleans up the invalid data. |
| JRServer.bat  JRServer.sh | This tool is used to launch Logi JReport Server in standalone mode without any predefined options. On Windows, you can start server by double-clicking on JRServer.bat. If you cannot start the server successfully in this way, the reason will be displayed in the MS-DOS command prompt. | JRServer [-?|-p <port>|-ap <adminport>|-realm <realmname>|-l backlog|-m <max>|-t <timeout>|-s <filename>|-web <directory>|-env|-silent||-local|-vDebug|-vError|-logall|-jrs.admin.server <host:port>|-cleanup] **Notes:**   * You may need to set an appropriate -Dfile.encoding option in the file to start Logi JReport Server in order to view characters correctly. * You may also need to set an appropriate -Dresolution option in the file to start Logi JReport Server in order to set the system resolution in DPI. | * **-?**  Prints this help message. * **-p <port>**  The port number to listen on. * **-ap <adminport>**  The port number which is used by the administration tools. * **-realm <realmname>**  Specifies the active realm. * **-l <backlog>**  The maximum queue length for incoming connections. * **-m <max>**  The maximum number of connection handlers. * **-t <timeout>**  The connection timeout in milliseconds. * **-s <filename>**  The servlet property file name. If this option is not used, the file servlet.properties in `<install_root>\bin` will be used as the servlet property file when launching Logi JReport Server. * **-web <directory>**  The root directory when accessing the server via the web. Its default value is `<intall_root>\public_html`. * **-env**  Prints the environment. * **-silent**  No output to the console. * **-local**  The administration tasks are available on local host only. * **-vDebug**  Enables Logi JReport Engine to output messages to a file and sets all log files' log level to INFO. * **-vError**  Enables Logi JReport Engine to output messages to a file and sets all log files' log level to ERROR. * **-log[:file Name]** (deprecated)  Outputs Logi JReport Engine messages to the log file as specified and uses the -vDebug level. * **-logall**  Sets all loggers' log level to INFO. * **-jrs.admin.server <host:port>**  The admin server host and RMI port. * **-cleanup**  Checks integrality of the server data and cleans up the invalid data. |
| jrenv.bat  jrenv.sh | This tool is for generating the report environment file report.env in the current directory. This file can help the Jinfonet support staff assist you when you run into problems. | - | - |
| launchpad.bat | This tool is used to start Logi JReport Server in the standalone mode and launch the Logi JReport Server Start Page. | - | - |
| makewar.bat  makewar.sh | See [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server#Tool). | - | - |
| MigrationBV52.bat  MigrationBV52.sh | This tool is used to convert all the resources from Logi JReport versions which are lower than V5.2 Build 590 to the resources of Logi JReport Server V8. If you install the new version to the same folder as the old one, the parameter can be omitted. | MigrationBV52 [orgReportHome] | * **orgReporthome**  The reporthome of the original Logi JReport Server. If this parameter is not provided, the value of "reporthome" of new Logi JReport Server will be used as its value. |
| MigrationV52.bat  MigrationV52.sh | This tool is used to convert all the resources of which the versions are between V5.2 Build 590 (included) and V6 (not included) to the resources of the latest Logi JReport Server. If you install the new version to the same folder as the old one, the parameter can be omitted. | MigrationV52 [orgReportHome] | * **orgReporthome**  The reporthome of the original Logi JReport Server. If this parameter is not provided, the value of "reporthome" of new Logi JReport Server will be used as its value. |
| NJRServer.bat  NJRServer.sh | This tool is used to launch Logi JReport Server without JIT option. If your server often crashes with JIT option, try this batch file instead of JRServer.bat. | NJRServer [-?|-p <port>|-ap <adminport>|-realm <realmname>|-l backlog|-m <max>|-t <timeout>|-s <filename>|-web <directory>|-env|-silent||-local|-vDebug|-vError|-logall|-jrs.admin.server <host:port>|-cleanup] | * **-?**  Prints this help message. * **-p <port>**  The port number to listen on. * **-ap <adminport>**  The port number which is used by the administration tools. * **-realm <realmname>**  Specifies the active realm. * **-l <backlog>**  The maximum queue length for incoming connections. * **-m <max>**  The maximum number of connection handlers. * **-t <timeout>**  The connection timeout in milliseconds. * **-s <filename>**  The servlet property file name. If this option is not used, the file servlet.properties in `<install_root>\bin` will be used as the servlet property file when launching Logi JReport Server. * **-web <directory>**  The root directory when accessing the server via the web. Its default value is `<intall_root>\public_html`. * **-env**  Prints the environment. * **-silent**  No output to the console. * **-local**  The administration tasks are available on local host only. * **-vDebug**  Enables Logi JReport Engine to output messages to a file and sets all log files' log level to INFO. * **-vError**  Enables Logi JReport Engine to output messages to a file and sets all log files' log level to ERROR. * **-log[:file Name]** (deprecated)  Outputs Logi JReport Engine messages to the log file as specified and uses the -vDebug level. * **-logall**  Sets all loggers' log level to INFO. * **-jrs.admin.server <host:port>**  The admin server host and RMI port. * **-cleanup**  Checks integrality of the server data and cleans up the invalid data. |
| register.bat | It is invoked by [browser.bat](#browser). | - | - |
| RMIAuthFileCreator.bat  RMIAuthFileCreator.sh | This tool is used to generate the rmi authentication file. Logi JReport Server uses the authentication file to secure remote objects. If no argument was provided, an authentication file named "rmi.auth" will be created in  `<install_root>\bin`, using the user ID and install key of Logi JReport Server. | RMIAuthFileCreator [authFileName [userid key]] | * **?**  Shows the usage message. * **authFileName**  The RMI authentication file name. If only input this argument, the user ID and install key of Logi JReport Server will be used to create the authentication file. * **userid**  The user ID, which will be used to generate the contents of the authentication file. * **key**  The key which will be used to generate contents of the authentication file. |
| rp.bat  rp.sh | This tool is for replacing user ID and license key. | rp UID Key | - |
| [rptconv.bat  rptconv.sh](#Example) | This tool is for converting old resources such as reports, visual analysis, library components, dashboards, catalogs etc. to be current version. | rptconv "-source=source\_path" ["-target=destination\_path"] [-r] [-s] | * **-source**  Specify the source path of the resources that are to be converted. * **-target**   Specify the destination path for the converted resources. * **-r**   Replace the source resource with the converted version. If this option is set, ["-target=destination\_path"] is ignored.  If both "-r" and "-target" are not specified, the converted resources are saved in the same directory as the source resources and named as "converted\_SourceResourceName". * **-s**  Convert all the resources in the specified directory, including the resources in all subdirectories. |
| startAdministration.bat | This tool is used to launch the Logi JReport Administration page from the Start menu after the server is started. | - | - |
| startConsole.bat | This tool is used to launch the Logi JReport Console page from the Start menu after the server is started. | - | - |
| stopServer.bat | This tool is used to exit Logi JReport Server from the Start menu. | - | - |
| stopServer.sh | This tool is used to exit Logi JReport Server. | - | - |

**Examples of running rptconv.bat/rptconv.sh to convert reports**

* **To convert a single resource:**

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports\InvoiceReport.cls" "–target=C:\temp"`

  This will convert C:\Logi JReport\Server\Logi JReports\InvoiceReport.cls to C:\temp\InvoiceReport.cls.

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports\InvoiceReport.cls" "–target=C:\temp\1.cls.xml"`

  This will convert C:\Logi JReport\Server\Logi JReports\InvoiceReport.cls, save the converted report to `C:\temp`, and name it as "1.cls.xml" (if license allows).

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports\InvoiceReport.cls"`

  This will convert C:\Logi JReport\Server\Logi JReports\InvoiceReport.cls, save the converted report in the same directory, and name it as "converted\_InvoiceReport.cls".

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports\InvoiceReport.cls" -r`

  This will overwrite C:\Logi JReport\Server\Logi JReports\InvoiceReport.cls.
* **To convert all resources (reports, visual analysis, library components, dashboards, catalogs etc.) in a directory:**

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports" "–target=C:\temp"`

  This will convert all the resources in C:\Logi JReport\Server\Logi JReports and save the converted resources to `C:\temp`. The converted resources use the same file names as source resources.

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports" "–target=C:\temp" -s`

  This will convert all the resources in C:\Logi JReport\Server\Logi JReports and in the subdirectories and save the converted resources to `C:\temp`. The converted resources take the same file names and directory structure as source resources.

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports" "–target=C:\temp\*.cls" -s`

  This will convert all the resources in C:\Logi JReport\Server\Logi JReports and in the subdirectories and save the converted resources to `C:\temp`. The converted resources take the same directory structure as source resources and the suffixes of their file names are all changed to ".cls".

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports" -r -s`

  This will convert all the resources in C:\Logi JReport\Server\Logi JReports and in the subdirectories. The converted resources overwrite the source resources.

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports"`

  This will convert all the resources in C:\Logi JReport\Server\Logi JReports. All the converted resources are saved in the same directory and named as "converted\_SourceResourceName".
* **To convert a type of resources with same suffixes in a directory:**

  The usage is similar to converting a directory. You can specify the wildcard to filter resources, for example:

  `rptconv "-source=C:\Logi JReport\Server\Logi JReports\*.cls" "–target=C:\temp"`

  This will convert all the reports with the suffix ".cls" in `C:\Logi JReport\Server\Logi JReports` and save the converted reports to `C:\temp`.

**Notes:**

* There must be one and only one catalog file in the directory where the resources to be converted reside.
* If the resources to be converted contain UDO or UDF, make sure the corresponding classes or jars are included in the class path of rptconv.bat/rptconv.sh.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Starting Using Java

The class of the standalone server is jet.server.JREntServer. You can start Logi JReport Server with the following command instead of using the generated batch files:

`JAVA -classpath <classpath> -Djava.compiler=NONE -Dreporthome=<install_root> jet.server.JREntServer [options]`

* **-classpath**  
   The classpath must include the following packages originally in your `<install_root>\lib`: JRESServlets.jar; JREntServer.jar; JREngine.jar; javax.servlet-api-3.1.0.jar; log4j-core-2.7.jar; log4j-api-2.7.jar;
* **-Djava.compiler=NONE**  
   This is without JIT. This is not a required option. However, if you encounter problems running the server and you think that they relate to the Java VM, you can try turning off the JIT compiler and then running again.
* **-DLogi JReport.url.encoding**  
   Specifies the encoding to encode/decode escape characters in URL strings. If not specified, the system default encoding will be used. For example: java ... -DLogi JReport.url.encoding=8859-1...
* **-Dreporthome**  
   This is where Logi JReport Server is installed. It is the Destination Location you specified when you installed it. This option is required. When you set the reporthome, upon launching, Logi JReport will try to find the jslc.dat and report.ini files in  `<install_root>\bin` and check whether they are valid. Jslc.dat is the License control file. Open report.ini, and you will find the configuration information, including the temp, template and the help path. Logi JReport will use the temp path to export the temporary files so you should make sure that the temp folder specified in report.ini exists and has space available.
* **-Dfile.encoding**  
   Specifies the encoding to encode/decode escape characters in the server data. If not specified, the system default encoding will be used. For example: java ... -Dfile.encoding=8859-1...
* **-Dresolution**  
   Sets the system resolution in DPI. If not specified, the system default resolution will be used, which is the resolution of your monitor, for example, -Dresolution=96.
* [**options**]

  | Option | Description |
  | --- | --- |
  | -? | Print brief help message. |
  | -p port | The port that this server listens on, default is 8888. |
  | -ap adminport | The port number that the remote administration uses, default is 8889. |
  | -l backlog | Maximum length of queue for incoming connection indications. |
  | -m max | Maximum number of connection handlers. |
  | -t timeout | Connection timeout in milliseconds. |
  | -s filename | Servlet property file name. |
  | -realm realmname | Active realm when the server starts up. The specified realm should exist, otherwise the server will use an existing realm as the active realm. The server will then record a warning message in the log file, and set the selected active realm by the server.realm.active property in the server.properties file. |
  | -web directory | Web application server root directory, default is `<intall_root>\public_html`. |
  | -local | Administration on local host only. |
  | -vDebug | Enables Logi JReport Engine to output messages to a file and sets engine log file's log level to INFO. |
  | -vError | Enables Logi JReport Engine to output messages to a file and sets engine log file's log level to ERROR. |
  | -env | Print environment settings when the server starts up. |
  | -silent | Outputs nothing, not even the server start information. |
  | -log[:file Name] (deprecated) | Outputs Logi JReport Engine messages to the log file as specified and uses the -vDebug level. |
  | -logall | Sets all loggers' log level to INFO. |
  | -jrs.admin.server host:port | The admin server host and RMI port. |
  | -cleanup | Checks integrality of the server data and cleans up the invalid data. |

**Notes:**

* For detailed information on how to configure the logging and debugging information, read the LogConfig.properties file in `<install_root>\bin`.
* Some of the common options will be used in later topics. In addition, Logi JReport has automatically generated some batch files for you so that you do not have to write a complicated command line. You can find these in the `<install_root>\bin` directory.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648622-Setting-Up-the-Reporting-Environment)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648642-Running-as-an-OS-Service)
