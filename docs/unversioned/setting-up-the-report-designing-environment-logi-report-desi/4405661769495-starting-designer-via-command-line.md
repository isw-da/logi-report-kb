---
title: "Starting Designer via Command Line"
id: 4405661769495
section: "Setting Up the Report Designing Environment - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661769495-Starting-Designer-via-Command-Line
updated_at: 2022-10-10T08:17:59Z
---

# Starting Designer via Command Line

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661770647-Using-the-Designer-Launch-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664605079-Updating-the-Designer-License-Key)

# Starting Designer via Command Line

You can start Designer from the Command Prompt window. This method is optional on some platforms (Windows for example) and preferred on others. Using command-line startup enables you to use the command-line syntax options. This topic describes the command line for starting Designer and each parameter in the command line.

You can use the following command line to start Designer. Note that the setup process creates several startup batch files which may contain additional parameters.

`java -Dreporthome=path -classpath path jet.builder.JReport -vError -vDebug -help`

* **-Dreporthome**  
  Specify the directory where you install Designer. This parameter is required. When you set the report home, upon starting, Designer tries to find jslc.dat and report.ini files in `<install_root>\bin` and checks whether they are valid. jslc.dat is the License control file. If you open report.ini, you can find configuration information, including the temp path, template path, and the help path. Designer uses the temp path for exporting temporary files, so you should make sure that the temp folder specified in report.ini actually exists.  

  Assume that you have installed Designer in `C:\LogiReport\Designer`, this parameter is `-Dreporthome=C:\LogiReport\Designer.`
* **-classpath** path  
  Tell the Java interpreter the class path. It is usually used for appending the Designer lib path to the Java class path. For example, assume that you have installed Designer in `C:\LogiReport\Designer` and Java (JDK1.x.x) in `C:\java`, this parameter is then:

  `-classpath C:\java\lib\classes.zip;C:\LogiReport\designer\lib\report.jar;`
* **-Djava.compiler**=NONE  
  Turn off just in time compiling, which sometimes creates problems.
* **-Djrpt.outer**=true  
  Enable Logi Report Engine to generate an SQL statement with full outer join syntax instead of with abbreviated syntax.
* **-Xmx1024m**  
  Set the maximum Java heap size.
* **-vError**/**-vDebug**  
  Specify the engine file's log level. See [Configuring Logs](https://devnet.logianalytics.com/hc/en-us/articles/4405664603159-Configuring-the-Logging-System#Log).
* **-help**  
  Output the help message.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661770647-Using-the-Designer-Launch-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664605079-Updating-the-Designer-License-Key)
