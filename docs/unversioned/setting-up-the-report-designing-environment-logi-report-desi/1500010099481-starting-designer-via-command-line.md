---
title: "Starting Designer via Command Line"
id: 1500010099481
section: "Setting Up the Report Designing Environment - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099481-Starting-Designer-via-Command-Line
updated_at: 2021-07-23T19:16:14Z
---

# Starting Designer via Command Line

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099501-Using-the-Designer-Launch-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4404857194903-Updating-the-Designer-License-Key)

# Starting Designer via Command Line

You can launch Designer from the Command Prompt window. This method is optional on some platforms (Windows for example) and preferred on others. Using command-line startup enables you to use the command-line syntax options. This topic describes the command line for starting Designer and each parameter in the command line.

You can use the following command line to launch Designer. Note that the setup process creates several startup batch files which may contain additional parameters.

`java -Dreporthome=path -classpath path jet.builder.JReport -vError -vDebug -help`

* **-Dreporthome**  
  Specify the directory where you install Designer. This parameter is required. When you set the report home, upon launching, Designer tries to find jslc.dat and report.ini files in `<install_root>\bin` and checks whether they are valid. jslc.dat is the License control file. If you open report.ini, you can find configuration information, including the temp path, template path, and the help path. Designer uses the temp path for exporting temporary files, so you should make sure that the temp folder specified in report.ini actually exists.  

  Assume that you have installed Designer in `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer`, this parameter is `-Dreporthome=C:\(Undefined variable: Logi_Variables.LogiReport)\Designer.`
* **-classpath** path  
  Tell the Java interpreter the class path. It is usually used for appending the Designer lib path to the Java class path. For example, assume that you have installed Designer in `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer` and Java (JDK1.x.x) in `C:\java`, this parameter is then:

  `-classpath C:\java\lib\classes.zip;C:\(Undefined variable: Logi_Variables.LogiReport)\designer\lib\report.jar;`
* **-Djava.compiler**=NONE  
  Turn off just in time compiling, which sometimes creates problems.
* **-Djrpt.outer**=true  
  Enable Logi Report Engine to generate an SQL statement with full outer join syntax instead of with abbreviated syntax.
* **-Xmx1024m**  
  Set the maximum Java heap size.
* **Logging and debugging switches**  
  You can use the following two command switches together to track detail debug and error information.
  + **-vError** - Enable Designer to output error messages. If you start Designer with this parameter in the command line, correspondingly in the LogConfig.properties file, Designer sets value of the engine Error level to ERROR and value of the engine Trace level to OFF.
  + **-vDebug** - Enable Designer to output information and warning messages. If you start Designer with this parameter in the command line, correspondingly in the LogConfig.properties file, Designer sets value of the engine Error level to WARN and value of the engine Trace level to INFO.

  You can specify the log file format, such as Text or HTML. You can then decide whether or not to append the log files to an existing file, or to create a new file. You can even specify the log layout using the abundant options that Logi Report provides. To do this, you need to edit the file LogConfig.properties in `<install_root>\bin`. For detailed information on how to configure logging and debugging information, see the comments in LogConfig.properites file.
* **-help**  
  Output the help message.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099501-Using-the-Designer-Launch-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4404857194903-Updating-the-Designer-License-Key)
