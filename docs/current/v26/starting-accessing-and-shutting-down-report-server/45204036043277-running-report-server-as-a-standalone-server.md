---
title: "Running Report Server as a Standalone Server"
id: 45204036043277
section: "Starting, Accessing, and Shutting Down Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204036043277-Running-Report-Server-as-a-Standalone-Server
updated_at: 2026-04-30T14:10:25Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Running Report Server as a Standalone Server 

This topic describes how you can run Report Server as a Standalone Server, using shortcuts, launch files, and Java commands.

Usually, you can start Server using these ways:

- Double-click the shortcut for Server on your desktop, for example, Logi Report Server 23.1.
                

- Take Logi Report 23.1 as an example. Select Logi Report 23.1 > Start Server on the Start menu of your computer.

- Run the JRServer.bat or      JRServer.sh file in <install_root>\bin.

- If your Server is not starting up, please stop Server using either of the following ways and then restart Server.
        
- Take Report 23.1 as an example. Select Logi Report 23.1 > Stop Server on the Start menu of your computer.

- Run the stopServer.bat or      stopServer.sh file in <install_root>\bin.

- 	If you find that the port you have used to install Server is being held up by another process, you can run "netstat -ano | findstr :<port>" to find which process is using the port. You can then use the task manager to terminate the task holding up the port.

This topic contains the following sections:

- Starting Server Using Java Commands

- Using Launch Files

## 
Starting Server Using Java Commands

The class of the standalone Report Server is jet.server.JREntServer. You can start  Server with the following commands:

JAVA -classpath <classpath> -Djava.compiler=NONE -Dreporthome=<install_root> jet.server.JREntServer [options]

- 
-classpath
    The classpath must include the following packages originally in your <install_root>\lib: JRESServlets.jar; JREntServer.jar; JREngine.jar; jakarta.servlet-api-4.0.4.jar; log4j-core-2.17.2.jar; log4j-api-2.17.2.jar;

- 
-Djava.compiler=NONE
    This is without JIT. This property is optional. However, if you encounter problems running the server and you think that they relate to the Java VM, you can try turning off the JIT compiler and then running again.

- 
-Djreport.url.encoding
The encoding to encode/decode escape characters in URL strings. If you do not provide this property, Server uses the system default encoding. For example: java ... -Djreport.url.encoding=8859-1...

- 
-Dreporthome
    This is where you installed Report Server. You need to provide this property. When you set the reporthome, upon launching, Report will try to find the jslc.dat and report.ini files in  <install_root>\bin and check whether they are valid. Jslc.dat is the License control file. Open report.ini, and you will find the configuration information, including the temp, template, and the help path. Report will use the temp path to export the temporary files so you should make sure that the temp folder specified in report.ini exists and has space available.

- 
-Dfile.encoding
 The encoding to encode/decode escape characters in the server data. If you do not provide this property, Server uses the system default encoding. For example: java ... -Dfile.encoding=8859-1...

- 
-Dresolution
    The system resolution in DPI. If you do not provide this property, Server uses the system default resolution, which is the resolution of your monitor. For example, -Dresolution=96.

- 
[Other properties]
				
| Property | Description |
| --- | --- |
| -? | Print brief help message. |
| -p port | The port that the server listens on. The default is 8888. |
| -realm realmname | Active realm when Server starts up. The specified realm should exist, otherwise Server uses an existing realm as the active realm. Server will then record a warning message in the log file, and set the selected active realm by the server.realm.active property in the server.properties file. |
| -l backlog | Maximum length of queue for incoming connection indications. |
| -m max | Maximum number of connection handlers. |
| -t timeout | Connection timeout in milliseconds. |
| -s filename | Servlet property file name. If you do not set this property, Server uses the servlet.properties file in \bin as the servlet property file when launching Server. |
| -web directory | The root directory when accessing the server via the web. The default is \public_html. |
| -env | Print environment settings when Server starts up. |
| -silent | Output nothing, not even the server start information. |
| -local | Administration on local host only. |
| -vDebug | Set engine log file's log level to DEBUG. |
| -vError | Set engine log file's log level to ERROR. |
| -logall | Set all loggers' log level to DEBUG. |
| -jrs.admin.server [host:port] | The admin server host and RMI port. |
| -cleanup | Check the integrality of the server data and clean up the invalid data. |

- For more information about how to configure the logging and debugging information, read the LogConfig.properties file in <install_root>\bin.

- You will use some of the common options in later topics. In addition, Report has automatically generated batch files for you so that you do not have to write a complicated command line. You can find them in <install_root>\bin. 

- In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, see Statement on Log4j and Log4Net Vulnerabilities.

## 
Using Launch Files

After you have installed Report Server, Server automatically generates many batch files in <install_root>\bin. They assist you with using and maintaining Server. You can edit the batch files to suit different circumstances. However, make sure that you understand their functions when you edit them.
		

See the Server launch files in the following table.

| File | Description | Usage | Options |
| --- | --- | --- | --- |
| browser.bat | This tool detects the default client browser and installation path. launchpad.bat invokes it. | - | - |
| CmdSender.bat CmdSender.sh | This tool is for sending commands to Report Server. If you do not add the property "-s" or "-p", you should define the JVM system property "reporthome" so that CmdSender.bat/CmdSender.sh will use it to get data from the local machine. | cmdsender [-s: -p: -u:] -w: shutdown\|localshutdown\|(local:on\|off) | -s The server host name. -p The server host port. -u The administrator username. -w The administrator password. shutdown Shut down the server. localshutdown Shut down the local server. local The administration tasks are available to local host only. gc Run the Java garbage collector. |
| DBMaintain.bat DBMaintain.sh | This tool is for administrators to back up and restore Report Server data. | DBMaintain -[?\|cleanup\|B>\|R>] | -? Display the usage information and then exit. -cleanup Check the integrality of the server data and clean up the invalid data. -Bsystemtables:/-Brealmtables:/-Bprofiling: Back up the data in the database with the related data to a specified file. For example, to back up the server data realmtables to the file c:\jsback.dat, you can type: DBMaintain -Brealmtables:c:\jsback.dat -B0realmtables: Only back up the data in the realm database. -Rsystemtables:/-Rrealmtables:/-Rprofiling: Restore the data including the related data outside the database from a specified file. For example, to restore server data realmtables from the file c:\jsback.dat, you can type: DBMaintain -Rrealmtables:c:\jsback.dat -R0realmtables: Only restore the data in the realm database. |
| DJRServer.bat DJRServer.sh | This tool launches Report Server with debug and log information. The output log files are in \logs. You may run this batch to reproduce problems. Open the log files to see more information and find out the problems. You may have to send the log files to Customer Service if you are unable to resolve the problems. | DJRServer [-?\|-p \|-ap \|-realm \|-l backlog\|-m \|-t \|-s \|-web \|-env\|-silent\|\|-local\|-vDebug\|-vError\|-jrs.admin.server \|-cleanup] | See the properties. |
| docker-container-migration.sh | Select here for more information. |  |  |
| JRServer.bat JRServer.sh | This tool launches Report Server in the standalone mode without any predefined properties. On Windows, you can start Server by double-clicking on JRServer.bat. If you cannot start Server in this way, Server displays the reason in the MS-DOS command console. | JRServer [-?\|-p \|-ap \|-realm \|-l backlog\|-m \|-t \|-s \|-web \|-env\|-silent\|\|-local\|-vDebug\|-vError\|-logall\|-jrs.admin.server \|-cleanup] You may need to set an appropriate property -Dfile.encoding in the file to start Report Server to view characters correctly. You may also need to set an appropriate property -Dresolution in the file to start Report Server to set the system resolution in DPI. | See the properties. |
| jrenv.bat jrenv.sh | This tool is for generating the report environment file report.env in the current directory. This file can help the Logi Analytics support staff assist you when you run into problems. | - | - |
| launchpad.bat | This tool starts Report Server in the standalone mode and launches the Report Server Start Page. | - | - |
| makewar.bat makewar.sh | Select here for more information. | - | - |
| MigrationBV52.bat MigrationBV52.sh | This tool converts the resources from Report versions lower than V5.2 Build 590 to the resources of Report Server V8. If you install the new version to the same folder as the old one, you can omit the parameter. | MigrationBV52 [orgReportHome] | orgReporthome The reporthome of the original Report Server. If you do not provide this parameter, Server uses the value of reporthome of new Report Server. |
| MigrationV52.bat MigrationV52.sh | This tool converts the resources of the versions between V5.2 Build 590 (included) and V6 (not included) to the resources of the latest Report Server. If you install the new version to the same folder as the old one, you can omit the parameter. | MigrationV52 [orgReportHome] | orgReporthome The reporthome of the original Report Server. If you do not provide this parameter, Server uses the value of reporthome of new Report Server. |
| MigrationTool.bat MigrationTool.sh | Select here for more information. | - | - |
| NJRServer.bat NJRServer.sh | This tool launches Report Server without JIT option. If your server often stops responding with JIT option, try this batch file instead of JRServer.bat. | NJRServer [-?\|-p \|-ap \|-realm \|-l backlog\|-m \|-t \|-s \|-web \|-env\|-silent\|\|-local\|-vDebug\|-vError\|-logall\|-jrs.admin.server \|-cleanup] | See the properties. |
| register.bat | browser.bat invokes this file. | - | - |
| RMIAuthFileCreator.bat RMIAuthFileCreator.sh | This tool generates the RMI authentication file. Report Server uses the authentication file to secure remote objects. If you do not provide any properties, Server creates an authentication file named rmi.auth in \bin, using the user ID and install key of Report Server. | RMIAuthFileCreator [authFileName [userid key]] | ? Display the usage message. authFileName The RMI authentication file name. If you only provide this property, Server uses the user ID and install key of Report Server to create the authentication file. userid The user ID to generate the contents of the authentication file. key The key to generate the contents of the authentication file. |
| rp.bat rp.sh | This tool is for replacing user ID and license key. | rp UID Key | - |
| rptconv.bat rptconv.sh | This tool is for converting old resources such as reports, visual analysis, library components, dashboards, and catalogs to be current version. | rptconv "-source=source_path" ["-target=destination_path"] [-r] [-s] | -source Source path of the resources that you want to convert. -target Destination path for the converted resources. -r Replace the source resource with the converted version. If you provide this property, Server ignores ["-target=destination_path"]. If you provide neither "-r" nor "-target", Server saves the converted resources in the same directory as the source resources and names them as "converted_SourceResourceName". -s Convert the resources in the specified directory, including the resources in the sub directories.  -cat Specify the catalog file for the list of files to be converted from the specified directory. -mapfile Specify a JSON file to match the report to the catalog based on the “-source=path” directory. The JSON data should be in the format: “res”:[{“rpts”: [report1, report2],”cat”: catalog}] To convert a catalog, report, or dashboard for a specific server, use the rptconv command with the “-svr=path” option. -svr Specify the server reporthome.If both the “-mapfile” and “-cat” options are provided simultaneously, the script will prioritize options with this order -mapfile > -cat > default |
| startConsole.bat | This tool launches the Server Console from the Start menu after Server starts. | - | - |
| stopServer.bat | This tool exits Report Server from the Start menu. | - | - |
| stopServer.sh | This tool exits Report Server. | - | - |

Examples of running rptconv.bat/rptconv.sh to convert reports 

- 
To convert a single resource:rptconv "-source=C:\LogiReport\Server\jreports\Payroll Report.cls" "–target=C:\temp"

This converts C:\LogiReport\Server\jreports\Payroll Report.cls to C:\temp\Payroll Report.cls. 

rptconv "-source=C:\LogiReport\Server\jreports\Payroll Report.cls" "–target=C:\temp\1.cls.xml"

This converts C:\LogiReport\Server\jreports\Payroll Report.cls, saves the converted report to C:\temp, and names it as "1.cls.xml" (if license allows). 

rptconv "-source=C:\LogiReport\Server\jreports\Payroll Report.cls"

This converts C:\LogiReport\Server\jreports\Payroll Report.cls, saves the converted report in the same directory, and names it as "converted_Payroll Report.cls". 

rptconv "-source=C:\LogiReport\Server\jreports\Payroll Report.cls" -r 

This overwrites C:\LogiReport\Server\jreports\Payroll Report.cls.

- 
To convert the resources (such as reports, visual analysis, library components, dashboards, and catalogs) in a directory:rptconv "-source=C:\LogiReport\Server\jreports" "–target=C:\temp"

This converts the resources in C:\LogiReport\Server\jreports and saves the converted resources to C:\temp. The converted resources use the same file names as source resources. 

rptconv "-source=C:\LogiReport\Server\jreports" "–target=C:\temp" -s 

This converts the resources in C:\LogiReport\Server\jreports and in the sub directories and saves the converted resources to C:\temp. The converted resources take the same file names and directory structure as source resources.

rptconv "-source=C:\LogiReport\Server\jreports" "–target=C:\temp\*.cls" -s 

This converts the resources in C:\LogiReport\Server\jreports and in the sub directories and saves the converted resources to C:\temp. The converted resources take the same directory structure as source resources and the suffixes of their file names are all changed to ".cls". 

rptconv "-source=C:\LogiReport\Server\jreports" -r -s 

This converts the resources in C:\LogiReport\Server\jreports and in the sub directories. The converted resources overwrite the source resources. 

rptconv "-source=C:\LogiReport\Server\jreports"

This converts the resources in C:\LogiReport\Server\jreports. Server saves the converted resources in the same directory and names them as "converted_SourceResourceName". 

- 
To convert a type of resources with same suffixes in a directory:The usage is similar to converting a directory. You can specify the wildcard to filter resources, for example: 

rptconv "-source=C:\LogiReport\Server\jreports\*.cls" "–target=C:\temp"

This converts the reports with the suffix ".cls" in C:\LogiReport\Server\jreports and saves the converted reports to C:\temp.

- There must be one and only one catalog file in the directory where the resources you want to convert reside. 

- If the resources that you want to convert contain UDO or UDF, make sure to include the corresponding classes or jars in the class path of rptconv.bat/rptconv.sh.
