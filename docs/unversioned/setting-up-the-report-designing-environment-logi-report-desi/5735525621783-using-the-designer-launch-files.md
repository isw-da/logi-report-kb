---
title: "Using the Designer Launch Files"
id: 5735525621783
section: "Setting Up the Report Designing Environment - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735525621783-Using-the-Designer-Launch-Files
updated_at: 2022-11-02T07:58:05Z
---

# Using the Designer Launch Files

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532240023-Solving-Installation-Problems)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735545183511-Starting-Designer-via-Command-Line)

# Using the Designer Launch Files

After you install Designer successfully, you can find a set of utilities in the `<install_root>\bin` directory. You can edit all of these batch files (Windows)/script files (UNIX/Linux) to suit different circumstances if you know their functions for sure. This topic describes the usages of the launch files.

| File | Description | Usage | Options |
| --- | --- | --- | --- |
| CatDr.bat CatDr.sh | You can use this tool to start the [Catalog Doctor](https://devnet.logianalytics.com/hc/en-us/articles/5735498397591-Maintaining-Catalogs-with-the-Catalog-Doctor) to maintain and diagnose catalogs. | java <-Dreporthome=reporthome> jet.builder.JReport [-options] [reportfile] | * **-help** Output the help message. * **-vDebug** Set engine file's log level to INFO. * **-vError** Set engine file's log level to ERROR. * -**log[:<file>]** Output message to `.\<file>` or the default. |
| cqrtrans.bat cqrtrans.sh | You can use this tool to convert String values in the specified [cached query result (CQR) file](https://devnet.logianalytics.com/hc/en-us/articles/5735586187287-Working-with-Cached-Query-Results) to the designated characters. To help diagnose your issue, Logi Report Support would need the CQR file for your report. For security concern, you can use this tool to convert the String values in the file before sending it, to protect your data from being revealed. The converted data cannot be restored by any means. | cqrtrans srcFile targetFile transformer Or:  cqrtrans "srcFile" "targetFile" "transformer" (you should quote the argument when it contains space).  **Example:**`cqrtrans c:/source.cqr c:/result.cqr abcd` | * **srcFile** Specify the full path of the cached query result file that you want to convert. * **targetFile** Specify the full path of the converted file. * **transformer** Specify the string you want to use to replace strings in the cached query result file. It can be any Unicode characters with the minimum length of one character and maximum length of 64 characters. By default, Designer uses some characters from the common base64 alphabet characters '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'. |
| DJReport.bat DJReport.sh | You can use this tool to start Designer in logging mode. In case of problems, you are requested to launch Designer with this batch file/script file in order to track detailed log information. Running this batch file/script file generates log files in the `<install_root>\logs` directory. | java <-Dreporthome=reporthome> com.jinfonet.designer.JReport [-options][reportfile] | * **-help** Output the help message. * **-vDebug** Set engine file's log level to INFO. * **-vError** Set engine file's log level to ERROR. |
| EConvert.bat EConvert.sh | You can use this tool to remove the evaluation mark from reports. If you have purchased the Logi Report product and are successful in running Designer with the new key, but the evaluation watermark is still visible, you need to run this batch file to remove the evaluation watermark. Run the batch file with the report names to be converted with the full path as parameter. | java -Dreporthome=<drive>:<path> jet.report.EvlConverter[[drive:][path][filename] +][drive:][path][filename]Econvert.bat [ReportName.cls] **Example:**`Econvert.bat C:\LogiReport\Designer\Demo\Reports\TutorialReports\*.cls` | - |
| jrenv.bat jrenv.sh | You can use this tool to generate the report environment file report.env in the current directory. This file can help the Logi Analytics support staff assist you when you run into problems. | - | - |
| JReport.bat  JReport.sh | You can use this tool to start Designer. | java <-Dreporthome=reporthome> com.jinfonet.designer.JReport [-options][reportfile] | * **-help** Output the help message. * **-vDebug** Set engine file's log level to INFO. * **-vError** Set engine file's log level to ERROR.   Note icon You may need to set an appropriate `-Dfile.encoding` option in the file to start Designer in order to view characters correctly. |
| JRTutorial.bat JRTutorial.sh | You can use this tool to display the Tutorial manual. | - | - |
| ModelWizard.bat ModelWizard.sh | You can use this tool to create and [import ObjectDataSource](https://devnet.logianalytics.com/hc/en-us/articles/5735521522455-Using-Data-Sources-via-OOJDBC-in-a-Catalog). | java com.jinfonet.jdbc.model.wizard.ModelWizard [-options] | * **-help** Output the help message. * **-vDebug** Set engine file's log level to INFO. * **-vError** Set engine file's log level to ERROR. * **-log[:<file>]** Output message to JGUIEditor.log or `.\<file>`. |
| NJReport.bat  NJReport.sh | You can use this tool to start Designer without the command window. | java <-Dreporthome=reporthome> com.jinfonet.designer.JReport [-options][reportfile] | * **-help** Output the help message. * **-vDebug** Set engine file's log level to INFO. * **-vError** Set engine file's log level to ERROR.   Note icon You may need to set an appropriate `-Dfile.encoding` option in the file to start Designer in order to view characters correctly. |
| [PageSetup.bat PageSetup.sh](#PageProperties) | You can use this tool to update the page properties for multiple reports in the specified catalog at a time. | - | - |
| PropConvert.bat PropConvert.sh | You can use this tool to convert property values. Running this batch file displays a window from which you can modify many properties of a selected report file. This is most useful when you want to modify several properties using the same value at the same time. For example, if a Label and several DBFields share the same background of blue, and now you want to change them all to transparent, you can simply use this tool. | - | - |
| rp.bat rp.sh | You can use this tool to replace the Designer user ID and license key. | rp UID Key | - |
| [rptconv.bat rptconv.sh](#Convert) | You can use this tool to convert reports created by earlier releases to the current. | rptconv "-source=source\_path" ["-target=destination\_path"] [-r] [-s] | * **-source** Specify the source path of the reports to be converted. * **-target**  Specify the destination path for the converted reports. * **-r**  Replace the source report with the converted version. When you set this option, Designer ignores `["-target=destination_path"]`. * **-s** Convert all reports in the specified directory, including the reports in all subdirectories.   Note icon If you do not specify both `-r` and `-target`, Designer saves the converted reports in the same directory as the source reports and names them converted\_SourceReportName. |
| setenv.bat setenv.sh | You can use this tool to generate the report environment variables before starting Designer. | - | - |

## Updating the Page Properties of Multiple Reports

You can run PageSetup.bat/PageSetup.sh to update the page properties of all reports in a specified catalog at a time conveniently.

1. Run **PageSetup.bat** or **PageSetup.sh** to display the Page Setup for All Report dialog box.

   ![Page Setup for All Report - General tab](https://devnet.logianalytics.com/hc/article_attachments/9898459583895/install_files_pggnl.gif)
2. Select **Browse** to specify the catalog that contains the reports the page properties of which you want to batch update.
3. In the **General** tab, edit the [page properties](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Setting) you want to change for the reports.
4. In the Export tab, edit [the page properties for the outputs of the reports in each export format](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports#Page): select a format from the **Export To** drop-down list, from the **Use General Settings** drop-down list, specify whether to use the settings you define in the General tab for this format, and if you select **false**, specify the size, orientation, and margin for the pages of the report outputs in this format accordingly.

   ![Page Setup for All Report - Export tab](https://devnet.logianalytics.com/hc/article_attachments/9898459591063/install_files_pgexpt.gif)
5. Select **Apply to All** and a Warning dialog box displays, listing the page properties that will be updated.
6. Select **OK** to update the specified page properties for all reports in the catalog. For any property that you do not specify in the dialog box, Designer keeps its original value in all the reports.

## Converting Reports to the Current Release

The following are examples of running rptconv.bat/rptconv.sh to convert reports created by earlier releases to the current.

**To convert a single report**

* `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" "–target=C:\temp"` 

  This converts C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls to C:\temp\Payroll Report.cls.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" "–target=C:\temp\1.cls.xml"` 

  This converts C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls, saves the converted report to `C:\temp`, and names it 1.cls.xml (if the license allows).
* `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls"` 

  This converts C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls, saves the converted report in the same directory, and names it converted\_Payroll Report.cls.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" -r` 

  This overwrites C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls.

**To convert all reports (\*.cls, \*.rpt, \*.clx, \*.cls.xml) in a directory**

* `rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp"` 

  This converts all reports in `C:\LogiReport\Designer\demo\reports` and saves the converted reports to `C:\temp`. The converted reports use the same file names as the source reports.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp" -s` 

  This converts all reports in `C:\LogiReport\Designer\demo\reports` and in the subdirectories and saves the converted reports to `C:\temp`. The converted reports apply the same file names and directory structure as the source reports.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp\*.cls" -s` 

  This converts all reports in `C:\LogiReport\Designer\demo\reports` and in the subdirectories and saves the converted reports to `C:\temp`. The converted reports apply the same directory structure as the source reports and use .cls as the file name extension.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports" -r -s`

  This converts all reports in `C:\LogiReport\Designer\demo\reports` and in the subdirectories. The converted reports overwrite the source reports.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports"` 

  This converts all reports in `C:\LogiReport\Designer\demo\reports` and saves the converted reports in the same directory as "converted\_SourceReportName".

**To convert a group of reports with the same suffixes in a directory**

The usage is similar to converting a directory. You can specify the wildcard to filter reports, for example:

`rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\*.cls" "–target=C:\temp"`

This converts all reports with the .cls extension in `C:\LogiReport\Designer\demo\reports\SampleReports` and saves the converted reports to `C:\temp`.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* There must be one and only one catalog file in the directory where the reports to be converted reside.
* If the reports to be converted contain UDO or UDF, make sure you include the corresponding classes or jars in the class path of rptconv.bat/rptconv.sh.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532240023-Solving-Installation-Problems)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735545183511-Starting-Designer-via-Command-Line)
