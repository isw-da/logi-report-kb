---
title: "Starting Designer via Command Line"
id: 5735545183511
section: "Setting Up the Report Designing Environment - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735545183511-Starting-Designer-via-Command-Line
updated_at: 2022-11-02T07:58:04Z
---

# Starting Designer via Command Line

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525621783-Using-the-Designer-Launch-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735532271383-Updating-the-Designer-License-Key)

# Starting Designer via Command Line

You can start Designer from the Command Prompt window. This method is optional on some platforms (Windows for example) and preferred on others. Using command-line startup enables you to use the command-line syntax options. This topic describes the command line for starting Designer and each option in the command line.

You can use the following command line to start Designer. Note that the setup process creates several startup batch files which may contain additional options.

`java -Dreporthome=path -classpath path jet.builder.JReport -vError -vDebug -help`

* **-Dreporthome**  
  Specify the directory where you install Designer. This option is required. When you set the report home, upon starting, Designer tries to find jslc.dat and report.ini in `<install_root>\bin` and checks whether they are valid. jslc.dat is the license control file. If you open report.ini, you can find configuration information, including the temp path, template path, and the help path. Designer uses the temp path for exporting temporary files, so you should make sure that the temp folder specified in report.ini actually exists.
* **-classpath** path  
  Tell the Java interpreter the class path. It is usually used for appending the Designer lib path to the Java class path.

  For example, assume that you have installed Designer in `C:\LogiReport\Designer` and Java JDK in `C:\java`, set this option to: `-classpath C:\java\lib\classes.zip;C:\LogiReport\designer\lib\report.jar;`
* **-Djava.compiler**=NONE  
  Turn off just in time compiling, which sometimes creates problems.
* **-Djrpt.outer**=true  
  Enable Logi Report Engine to generate an SQL statement with full outer join syntax instead of with abbreviated syntax.
* **-Xmx1024m**  
  Specify the maximum Java heap size.
* **-vError**/**-vDebug**  
  Specify the engine file's log level. See [Configuring the Logging System](https://devnet.logianalytics.com/hc/en-us/articles/5735516331543-Configuring-the-Logging-System).
* **-help**  
  Output the help message.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525621783-Using-the-Designer-Launch-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735532271383-Updating-the-Designer-License-Key)
