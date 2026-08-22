---
title: "Command-Line Startup"
id: 1500010033282
section: "Setting Up the Report Designing Environment - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010033282-Command-Line-Startup
updated_at: 2021-07-24T10:38:12Z
---

# Command-Line Startup

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033302-Logi-JReport-Designer-Launch-Files) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034942-Report-Development-Environment)

# Command-Line Startup

You can launch Logi JReport Designer from the Command Prompt window. This method is optional on some platforms (Windows for example) and preferred on others. Using command-line startup enables you to use the command-line syntax options.

`java -Dreporthome=path -classpath path jet.builder.JReport -vError -vDebug -help`

The command line arguments for Logi JReport Designer are described below. Note that the setup process creates several startup batch files which may contain additional parameters.

* **-Dreporthome**  
   Specifies the directory where Logi JReport Designer has been installed. This parameter is required. When you set the report home, upon launching, Logi JReport will try to find jslc.dat and report.ini files in `<install_root>\bin` and check whether they are valid. jslc.dat is the License control file. If you open report.ini, you will find configuration information, including the temp path, template path and the help path. Logi JReport uses the temp path for exporting temporary files, so you should make sure that the temp folder specified in report.ini actually exists.  

  Assume that Logi JReport Designer has been installed in `C:\JReport\Designer`, this parameter is `-Dreporthome=C:\JReport\Designer.`
* **-classpath** path  
   Tells the Java interpreter the class path. It is usually used for appending the Logi JReport Designer lib path to the Java class path. For example, assume that Logi JReport Designer has been installed in `C:\JReport\Designer` and Java (JDK1.x.x) has been installed in `C:\java`, this parameter is then:

  `-classpath C:\java\lib\classes.zip;C:\JReport\designer\lib\report.jar;`
* **-Djava.compiler**=NONE  
   Turns off just in time compiling, which sometimes creates problems.
* **-Djrpt.outer**=true  
   Enables Logi JReport Engine to generate an SQL statement with full outer join syntax instead of with abbreviated syntax.
* **-Xmx1024m**  
   Sets the maximum Java heap size.
* **Logging and debugging switches**  
   You can use the following two command switches together to track detail debug and error information.
  + **-vError** - Enables Logi JReport Designer to output error messages. If you start Designer with this command in the command-line, correspondingly in the LogConfig.properties file, value of the engine Error level will be set to ERROR and value of the engine Trace level will be set to OFF.
  + **-vDebug** - Enables Logi JReport Designer to output information and warning messages. If you start Designer with this command in the command-line, correspondingly in the LogConfig.properties file, value of the engine Error level will be set to WARN and value of the engine Trace level will be set to INFO.

  You can specify the log file format, such as Text, or HTML. You can then decide whether or not to append the log files to an existing file, or to create a new file. You can even specify the log layout using the abundant options that Logi JReport provides. To do this, you need to edit the file LogConfig.properties in `<install_root>\bin`. For detailed information on how to configure logging and debugging information, see the LogConfig.properites file.
* **-help**  
   Prints the help message.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033302-Logi-JReport-Designer-Launch-Files) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034942-Report-Development-Environment)
