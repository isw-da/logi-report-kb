---
title: "Using the Designer Launch Files"
id: 4405661770647
section: "Setting Up the Report Designing Environment - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661770647-Using-the-Designer-Launch-Files
updated_at: 2022-01-27T20:34:48Z
---

# Using the Designer Launch Files

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661774871-Solving-Installation-Problems)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661769495-Starting-Designer-via-Command-Line)

# Using the Designer Launch Files

After you install Designer successfully, you can find a set of utilities in the `<install_root>\bin` directory. You can edit all of these batch files (Windows)/script files (UNIX/Linux) to suit different circumstances if you know their functions for sure. This topic describes the usages of the launch files.

| File | Description | Usage | Options |
| --- | --- | --- | --- |
| CatDr.bat CatDr.sh | This tool is for starting the Catalog Doctor in order to make changes to the catalog. | java <-Dreporthome=reporthome> jet.builder.JReport [-options] [reportfile] | * **-help** Print out this message. * **-vDebug** Enable output debug message. * **-vError** Enable output error message. * -**log[:<file>]** Output message to `.\<file>` or the default. |
| This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.cqrtrans.bat cqrtrans.sh | This tool is for converting String values in the specified [cached query result (CQR) file](https://devnet.logianalytics.com/hc/en-us/articles/4405664683031-Working-with-Cached-Query-Results) to the designated characters. To help diagnose your issue, Logi Report support would need the CQR file for your report. For security concern, you can use this tool to convert the String values in the file before sending it, to protect your data from being revealed. The converted data cannot be restored by any means. | cqrtrans srcFile targetFile transformer Or:  cqrtrans "srcFile" "targetFile" "transformer" (you should quote the argument when it contains space).  **Example:** cqrtrans c:/source.cqr c:/result.cqr abcd | * **srcFile** Specify the full path of the cached query result file that you want to convert. * **targetFile** Specify the full path of the converted file. * **transformer** Specify the string you want to use to replace strings in the cached query result file. It can be any Unicode characters with the minimum length of one character and maximum length of 64 characters. By default, Designer uses some characters from the common base64 alphabet characters '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'. |
| DJReport.bat DJReport.sh | This tool is for starting Designer in logging mode. In case of problems, you are requested to launch Designer with this batch file/script file in order to track detailed log information. Running this batch file/script file generates log files in the `<install_root>\logs` directory. | java <-Dreporthome=reporthome> com.jinfonet.designer.JReport [-options][reportfile] | * **-help** Print out this message. * **-vDebug** Enable output debug message. * **-vError** Enable output error message. |
| EConvert.bat EConvert.sh | This tool is for removing the evaluation mark from reports. If you have purchased the Logi Report product and are successful in running Designer with the new key, but the evaluation watermarks are still visible, you need to run this batch file to remove the evaluation watermarks. Run the batch file with the report names to be converted with the full path as parameter. | java -Dreporthome=<drive>:<path> jet.report.EvlConverter[[drive:][path][filename] +][drive:][path][filename]Econvert.bat [ReportName.cls] **Example:** Econvert.bat C:\LogiReport\Designer\Demo\Reports\TutorialReports\\*.cls | - |
| jrenv.bat jrenv.sh | This tool is for generating the report environment file report.env in the current directory. This file can help the Logi Analytics support staff assist you when you run into problems. | - | - |
| JReport.bat  JReport.sh | This tool is for starting Designer. | java <-Dreporthome=reporthome> com.jinfonet.designer.JReport [-options][reportfile] | * **-help** Print out this message. * **-vDebug** Enable output debug message. * **-vError** Enable output error message.   Note icon You may need to set an appropriate *-Dfile.encoding* option in the file to start Designer in order to view characters correctly. |
| JRTutorial.bat JRTutorial.sh | This tool is for running this batch file to display the Tutorial manual. | - | - |
| ModelWizard.bat ModelWizard.sh | This tool is for creating and [importing ObjectDataSource](https://devnet.logianalytics.com/hc/en-us/articles/4405661426711-Using-Data-Sources-via-OOJDBC-in-a-Catalog). | java com.jinfonet.jdbc.model.wizard.ModelWizard [-options] | * **-help** Print out this message. * **-vDebug** Enable output debug message. * **-vError** Enable output error message. * **-log[:<file>]** Output message to JGUIEditor.log or `.\<file>`. |
| NJReport.bat  NJReport.sh | This tool is for starting Designer without the command window. | java <-Dreporthome=reporthome> com.jinfonet.designer.JReport [-options][reportfile] | * **-help** Print out this message. * **-vDebug** Enable output debug message. * **-vError** Enable output error message.   Note icon You may need to set an appropriate *-Dfile.encoding* option in the file to start Designer in order to view characters correctly. |
| [PageSetup.bat PageSetup.sh](#PageProperties) | This tool is for updating the page properties for multiple reports in the specified catalog at a time. | - | - |
| PropConvert.bat PropConvert.sh | This tool is for converting property values. Running this batch file displays a window from which you can modify many properties of a selected report file. This is most useful when you want to modify several properties using the same value at the same time. For example, if a Label and several DBFields share the same background of blue, and now you want to change them all to transparent, you can simply use this tool. | - | - |
| rp.bat rp.sh | This tool is for replacing user ID and license key. | rp UID Key | - |
| [rptconv.bat rptconv.sh](#Convert) | This tool is for converting reports of the old releases to the current. | rptconv "-source=source\_path" ["-target=destination\_path"] [-r] [-s] | * **-source** Specify the source path of the reports to be converted. * **-target**  Specify the destination path for the converted reports. * **-r**  Replace the source report with the converted version. If you set this option, Designer ignores ["-target=destination\_path"].  If you do not specify both "-r" and "-target", the converted reports are saved in the same directory as the source reports and named as "converted\_SourceReportName". * **-s** Convert all the reports in the specified directory, including the reports in all subdirectories. |
| setenv.bat setenv.sh | This tool is for generating the report environment variables before starting Designer. | - | - |

## Updating the Page Properties of Multiple Reports

You can run PageSetup.bat/PageSetup.sh to update the page properties of all the reports in a specified catalog at a time conveniently.

1. Run **PageSetup.bat** or **PageSetup.sh** to display the Page Setup for All Report dialog box.

   ![Page Setup for All Report - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420542093079/install_files_pggnl.gif)
2. Select **Browse** to specify the catalog that contains the reports the page properties of which you want to batch update.
3. In the **General** tab, edit the [page properties](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Setting) you want to change for the reports.
4. In the Export tab, edit [the page properties for the outputs of the reports in each export format](https://devnet.logianalytics.com/hc/en-us/articles/4405664595479-Exporting-Reports#Page): select a format from the **Export To** drop-down list, from the **Use General Settings** drop-down list, specify whether to use the settings you define in the General tab for this format, and if you select **false**, specify the size, orientation, and margin for the pages of the report outputs in this format accordingly.

   ![Page Setup for All Report - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4420550849943/install_files_pgexpt.gif)
5. Select **Apply to All** and a Warning dialog box displays, listing the page properties that will be updated.
6. Select **OK** to update the specified page properties for all the reports in the catalog.

   For any property that you do not specify in the dialog box, Designer remains its original value in all the reports.

## Converting Reports to the Current Release

The following shows some examples of running rptconv.bat/rptconv.sh to convert reports of an old release to the current.

**To convert a single report**

* `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" "–target=C:\temp"` 

  This converts C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls to C:\temp\Payroll Report.cls.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" "–target=C:\temp\1.cls.xml"` 

  This converts C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls, saves the converted report to `C:\temp`, and names it as "1.cls.xml" (if the license allows).
* `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls"` 

  This converts C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls, saves the converted report in the same directory, and names it as "converted\_Payroll Report.cls".
* `rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" -r` 

  This overwrites C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls.

**To convert all reports (\*.cls, \*.rpt, \*.clx, \*.cls.xml) in a directory**

* `rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp"` 

  This converts all the reports in `C:\LogiReport\Designer\demo\reports` and saves the converted reports to `C:\temp`. The converted reports use the same file names as source reports.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp" -s` 

  This converts all the reports in `C:\LogiReport\Designer\demo\reports` and in the subdirectories and saves the converted reports to `C:\temp`. The converted reports take the same file names and directory structure as the source reports.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp\*.cls" -s` 

  This converts all the reports in `C:\LogiReport\Designer\demo\reports` and in the subdirectories and saves the converted reports to `C:\temp`. The converted reports take the same directory structure as the source reports and use .cls as the extension of their file names.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports" -r -s`

  This converts all the reports in `C:\LogiReport\Designer\demo\reports` and in the subdirectories. The converted reports overwrite the source reports.
* `rptconv "-source=C:\LogiReport\Designer\demo\reports"` 

  This converts all the reports in `C:\LogiReport\Designer\demo\reports`. Designer saves all the converted reports in the same directory and names them as "converted\_SourceReportName".

**To convert a group of reports with the same suffixes in a directory**

The usage is similar to converting a directory. You can specify the wildcard to filter reports, for example:

`rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\*.cls" "–target=C:\temp"`

This converts all the reports with the .cls extension in `C:\LogiReport\Designer\demo\reports\SampleReports` and saves the converted reports to `C:\temp`.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* There must be one and only one catalog file in the directory where the reports to be converted reside.
* If the reports to be converted contain UDO or UDF, make sure you include the corresponding classes or jars in the class path of rptconv.bat/rptconv.sh.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661774871-Solving-Installation-Problems)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661769495-Starting-Designer-via-Command-Line)
