---
title: "Starting Designer via Command Line"
id: 1500009634261
section: "Setting Up the Report Designing Environment - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634261-Starting-Designer-via-Command-Line
updated_at: 2021-07-24T16:03:55Z
---

# Starting Designer via Command Line

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634281-Using-the-Designer-Launch-Files) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636261-Report-Development-Environment)

# Starting Designer via Command Line

You can launch Logi Report Designer from the Command Prompt window. This method is optional on some platforms (Windows for example) and preferred on others. Using command-line startup enables you to use the command-line syntax options. This topic describes the command line for starting Designer and each parameter in the command line.

You can use the following command line to launch Designer. Note that the setup process creates several startup batch files which may contain additional parameters.

`java -Dreporthome=path -classpath path jet.builder.JReport -vError -vDebug -help`

* **-Dreporthome**  
  Specifies the directory where Designer has been installed. This parameter is required. When you set the report home, upon launching, Logi Report will try to find jslc.dat and report.ini files in `<install_root>\bin` and check whether they are valid. jslc.dat is the License control file. If you open report.ini, you will find configuration information, including the temp path, template path and the help path. Logi Report uses the temp path for exporting temporary files, so you should make sure that the temp folder specified in report.ini actually exists.  

  Assume that you have installed Designer in `C:\LogiReport\Designer`, this parameter is `-Dreporthome=C:\LogiReport\Designer.`
* **-classpath** path  
  Tells the Java interpreter the class path. It is usually used for appending the Logi Report Designer lib path to the Java class path. For example, assume that you have installed Designer in `C:\LogiReport\Designer` and Java (JDK1.x.x) in `C:\java`, this parameter is then:

  `-classpath C:\java\lib\classes.zip;C:\LogiReport\designer\lib\report.jar;`
* **-Djava.compiler**=NONE  
  Turns off just in time compiling, which sometimes creates problems.
* **-Djrpt.outer**=true  
  Enables Logi Report Engine to generate an SQL statement with full outer join syntax instead of with abbreviated syntax.
* **-Xmx1024m**  
  Sets the maximum Java heap size.
* **Logging and debugging switches**  
  You can use the following two command switches together to track detail debug and error information.
  + **-vError** - Enables Designer to output error messages. If you start Designer with this parameter in the command line, correspondingly in the LogConfig.properties file, value of the engine Error level will be set to ERROR and value of the engine Trace level will be set to OFF.
  + **-vDebug** - Enables Designer to output information and warning messages. If you start Designer with this parameter in the command line, correspondingly in the LogConfig.properties file, value of the engine Error level will be set to WARN and value of the engine Trace level will be set to INFO.

  You can specify the log file format, such as Text, or HTML. You can then decide whether or not to append the log files to an existing file, or to create a new file. You can even specify the log layout using the abundant options that Logi Report provides. To do this, you need to edit the file LogConfig.properties in `<install_root>\bin`. For detailed information on how to configure logging and debugging information, see the comments in LogConfig.properites file.
* **-help**  
  Outputs the help message.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634281-Using-the-Designer-Launch-Files) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636261-Report-Development-Environment)
