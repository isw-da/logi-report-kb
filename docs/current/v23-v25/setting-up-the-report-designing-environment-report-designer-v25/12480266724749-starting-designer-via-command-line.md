---
title: "Starting Designer via Command Line"
id: 12480266724749
section: "Setting Up the Report Designing Environment - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480266724749-Starting-Designer-via-Command-Line
updated_at: 2026-02-25T23:48:25Z
source_host: docs-report.zendesk.com
---
# Starting Designer via Command Line

You can start Designer from the Command Prompt window. This method is optional on some platforms (Windows for example) and preferred on others. Using command-line startup enables you to use the command-line syntax options. This topic describes the command line for starting Designer and each option in the command line.

You can use the following command line to start Designer. Note that the setup process creates several startup batch files which may contain additional options.

java -Dreporthome=path -classpath path jet.builder.JReport -vError -vDebug -help

- 
-Dreporthome
Specify the directory where  you install Designer. This option is required. When you set the report home, upon starting, Designer tries to find jslc.dat and report.ini in <install_root>\bin and checks whether they are valid. jslc.dat is the license control file. If you open report.ini, you can find configuration information, including the temp path, template path, and the help path. Designer uses the temp path for exporting temporary files, so you should make sure that the temp folder specified in report.ini actually exists.

- 
-classpath path
Tell the Java interpreter the class path. It is usually used for appending the Designer lib path to the Java class path. For example, assume that you have installed Designer  in C:\LogiReport\Designer and Java JDK in C:\java, set this option to: -classpath C:\java\lib\classes.zip;C:\LogiReport\designer\lib\report.jar;

- 
-Djava.compiler=NONE
Turn off just in time compiling, which sometimes creates problems.

- 
-Djrpt.outer=true
Enable Report Engine to generate an SQL statement with full outer join syntax instead of with abbreviated syntax.

- 
-Xmx1024m
Specify the maximum Java heap size.

- 
-vError/-vDebug
Specify the engine file's log level. See Configuring the Logging System.

- 
-help
Output the help message.
