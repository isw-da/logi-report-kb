---
title: "Using the Designer Launch Files"
id: 1500009634281
section: "Setting Up the Report Designing Environment - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634281-Using-the-Designer-Launch-Files
updated_at: 2021-07-24T16:03:55Z
---

# Using the Designer Launch Files

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611302-Upgrading-Reports-from-v7-or-Prior-to-v17) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634261-Starting-Designer-via-Command-Line)

# Using the Designer Launch Files

After you have successfully installed Logi Report Designer, you can find a set of utilities in the `<install_root>\bin` directory. You can edit all of these batch files (Windows)/script files (Unix/Linux) to suit different circumstances if you know their functions for sure. This topic introduces the usages of the Logi Report Designer launch files.

| File | Description | Usage | Options |
| --- | --- | --- | --- |
| CatDr.bat  CatDr.sh | This tool is for starting the Catalog Doctor in order to make changes to the catalog. | java <-Dreporthome=reporthome> jet.builder.JReport [-options] [reportfile] | * **-help** Prints out this message. * **-vDebug** Enables output debug message. * **-vError** Enables output error message. * -**log[:<file>]** Outputs message to `.\<file>` or the default. |
| DJReport.bat  DJReport.sh | This tool is for starting Logi Report Designer in logging mode. In case of problems, you are requested to launch Logi Report Designer with this batch file/script file in order to track detailed log information. Running this batch file/script file generates log files in the `<install_root>\logs` directory. | java <-Dreporthome=reporthome> com.jinfonet.designer.JReport [-options][reportfile] | * **-help** Prints out this message. * **-vDebug** Enables output debug message. * **-vError** Enables output error message. |
| EConvert.bat  EConvert.sh | This tool is for removing the evaluation mark from reports. If you have purchased the Logi Report product and are successful in running Logi Report Designer with the new key, but the evaluation watermarks are still visible, you will need to run this batch file to remove the evaluation watermarks. Run the batch file with the report names to be converted with the full path as parameter. | java -Dreporthome=<drive>:<path> jet.report.EvlConverter[[drive:][path][filename] +][drive:][path][filename]Econvert.bat [ReportName.cls] **Example:** Econvert.bat C:\LogiReport\Designer\Demo\Reports\TutorialReports\\*.cls | - |
| jrenv.bat  jrenv.sh | This tool is for generating the report environment file report.env in the current directory. This file can help the Logi Analytics support staff assist you when you run into problems. | - | - |
| JReport.bat  JReport.sh | This tool is for starting Logi Report Designer. | java <-Dreporthome=reporthome> com.jinfonet.designer.JReport [-options][reportfile] | * **-help** Prints out this message. * **-vDebug** Enables output debug message. * **-vError** Enables output error message.   **Note:** You may need to set an appropriate -Dfile.encoding option in the file to start Logi Report Designer in order to view characters correctly. |
| JRTutorial.bat  JRTutorial.sh | This tool is for running this batch file to display the tutorial help. | - | - |
| ModelWizard.bat  ModelWizard.sh | This tool is for creating and [importing ObjectDataSource](https://devnet.logianalytics.com/hc/en-us/articles/1500009606842-Using-Data-Sources-via-OOJDBC). These can be used to create data sources for text files and Excel files. | java com.jinfonet.jdbc.model.wizard.ModelWizard [-options] | * **-help** Prints out this message. * **-vDebug** Enables output debug message. * **-vError** Enables output error message. * **-log[:<file>]** Outputs message to JGUIEditor.log or `.\<file>`. |
| NJReport.bat  NJReport.sh | This tool is for starting Logi Report Designer without the command window. | java <-Dreporthome=reporthome> com.jinfonet.designer.JReport [-options][reportfile] | * **-help** Prints out this message. * **-vDebug** Enables output debug message. * **-vError** Enables output error message.   **Note:** You may need to set an appropriate -Dfile.encoding option in the file to start Logi Report Designer in order to view characters correctly. |
| PropConvert.bat  PropConvert.sh | This tool is for converting property values. Running this batch file will display a window from which you can modify many properties of a selected report file. This is most useful when you want to modify several properties using the same value at the same time. For example, if a Label and several DBFields share the same background of blue, and now you want to change them all to transparent, you can simply use this tool. | - | - |
| rp.bat  rp.sh | This tool is for replacing user ID and license key. | rp UID Key | - |
| [rptconv.bat  rptconv.sh](#Convert) | This tool is for converting an old report schema to the current version. | rptconv "-source=source\_path" ["-target=destination\_path"] [-r] [-s] | * **-source** Specifies the source path of the reports that are to be converted. * **-target**  Specifies the destination path for the converted reports. * **-r**  Replaces the source report with the converted version. If this option is set, ["-target=destination\_path"] will be ignored.  If both "-r" and "-target" are not specified, the converted reports are saved in the same directory as the source reports and named as "converted\_SourceReportName". * **-s** Converts all the reports in the specified directory, including the reports in all subdirectories. |
| setenv.bat  setenv.sh | This tool is for generating the report environment variables before starting Logi Report Designer. | - | - |

**Examples of running rptconv.bat/rptconv.sh to convert reports**

* **To convert a single report:**

  `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" "–target=C:\temp"`

  This will convert C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls to C:\temp\Payroll Report.cls.

  `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" "–target=C:\temp\1.cls.xml"`

  This will convert C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls, save the converted report to `C:\temp`, and name it as "1.cls.xml" (if license allows).

  `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls"`

  This will convert C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls, save the converted report in the same directory, and name it as "converted\_Payroll Report.cls".

  `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" -r`

  This will overwrite C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls.
* **To convert all reports (\*.cls, \*.rpt, \*.clx, \*.cls.xml) in a directory:**

  `rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp"`

  This will convert all the reports in `C:\LogiReport\Designer\demo\reports` and save the converted reports to `C:\temp`. The converted reports use the same file names as source reports.

  `rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp" -s`

  This will convert all the reports in `C:\LogiReport\Designer\demo\reports` and in the subdirectories and save the converted reports to `C:\temp`. The converted reports take the same file names and directory structure as source reports.

  `rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp\*.cls" -s`

  This will convert all the reports in `C:\LogiReport\Designer\demo\reports` and in the subdirectories and save the converted reports to `C:\temp`. The converted reports take the same directory structure as source reports and the suffixes of their file names are all changed to ".cls".

  `rptconv "-source=C:\LogiReport\Designer\demo\reports" -r -s`

  This will convert all the reports in `C:\LogiReport\Designer\demo\reports` and in the subdirectories. The converted reports overwrite the source reports.

  `rptconv "-source=C:\LogiReport\Designer\demo\reports"`

  This will convert all the reports in `C:\LogiReport\Designer\demo\reports`. All the converted reports are saved in the same directory and named as "converted\_SourceReportName".
* **To convert a group of reports with the same suffixes in a directory:**

  The usage is similar to converting a directory. You can specify the wildcard to filter reports, for example:

  `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\*.cls" "–target=C:\temp"`

  This will convert all the reports with the suffix ".cls" in `C:\LogiReport\Designer\demo\reports\SampleReports` and save the converted reports to `C:\temp`.

**Notes:**

* There must be one and only one catalog file in the directory where the reports to be converted reside.
* If the reports to be converted contain UDO or UDF, make sure the corresponding classes or jars are included in the class path of rptconv.bat/rptconv.sh.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611302-Upgrading-Reports-from-v7-or-Prior-to-v17) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634261-Starting-Designer-via-Command-Line)
