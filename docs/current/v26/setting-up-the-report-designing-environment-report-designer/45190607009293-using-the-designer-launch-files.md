---
title: "Using the Designer Launch Files"
id: 45190607009293
section: "Setting Up the Report Designing Environment - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190607009293-Using-the-Designer-Launch-Files
updated_at: 2026-04-30T15:15:15Z
source_host: logi-report-v26.insightsoftware.com
---
# Using the Designer Launch Files

After you install Designer successfully, you can find a set of utilities in the <install_root>\bin directory. You can edit all of these batch files (Windows)/script files (UNIX/Linux) to suit different circumstances if you know their functions for sure. This topic describes the usages of the launch files. 

| File | Description | Usage | Options |
| --- | --- | --- | --- |
| CatDr.bat CatDr.sh | You can use this tool to start the Catalog Doctor to maintain and diagnose catalogs. | java  jet.builder.JReport [-options] [reportfile] | -help Output the help message. -vDebug Set engine file's log level to INFO. -vError Set engine file's log level to ERROR. -log[:] Output message to .\ or the default. |
| cqrtrans.bat cqrtrans.sh | You can use this tool to convert String values in the specified cached query result (CQR) file to the designated characters. To help diagnose your issue, Report Support would need the CQR file for your report. For security concern, you can use this tool to convert the String values in the file before sending it, to protect your data from being revealed. The converted data cannot be restored by any means. | cqrtrans srcFile targetFile transformer Or: cqrtrans "srcFile" "targetFile" "transformer" (you should quote the argument when it contains space). Example:cqrtrans c:/source.cqr c:/result.cqr abcd | srcFile Specify the full path of the cached query result file that you want to convert. targetFile Specify the full path of the converted file. transformer Specify the string you want to use to replace strings in the cached query result file. It can be any Unicode characters with the minimum length of one character and maximum length of 64 characters. By default, Designer uses some characters from the common base64 alphabet characters '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'. |
| DJReport.bat DJReport.sh | You can use this tool to start Designer in logging mode. In case of problems, you are requested to launch Designer with this batch file/script file in order to track detailed log information. Running this batch file/script file generates log files in the \logs directory. | java  com.jinfonet.designer.JReport [-options][reportfile] | -help Output the help message. -vDebug Set engine file's log level to INFO. -vError Set engine file's log level to ERROR. |
| EConvert.bat EConvert.sh | You can use this tool to remove the evaluation mark from reports. If you have purchased the Report product and are successful in running Designer with the new key, but the evaluation watermark is still visible, you need to run this batch file to remove the evaluation watermark. Run the batch file with the report names to be converted with the full path as parameter. | java -Dreporthome=: jet.report.EvlConverter[[drive:][path][filename] +][drive:][path][filename]Econvert.bat [ReportName.cls] Example:Econvert.bat C:\LogiReport\Designer\Demo\Reports\TutorialReports\*.cls | - |
| jrenv.bat jrenv.sh | You can use this tool to generate the report environment file report.env in the current directory. This file can help the Logi Analytics support staff assist you when you run into problems. | - | - |
| JReport.bat JReport.sh | You can use this tool to start Designer. | java  com.jinfonet.designer.JReport [-options][reportfile] | -help Output the help message. -vDebug Set engine file's log level to INFO. -vError Set engine file's log level to ERROR. You may need to set an appropriate -Dfile.encoding option in the file to start Designer in order to view characters correctly. |
| JRTutorial.bat JRTutorial.sh | You can use this tool to display the Tutorial manual. | - | - |
| ModelWizard.bat ModelWizard.sh | You can use this tool to create and import ObjectDataSource. | java com.jinfonet.jdbc.model.wizard.ModelWizard [-options] | -help Output the help message. -vDebug Set engine file's log level to INFO. -vError Set engine file's log level to ERROR. -log[:] Output message to JGUIEditor.log or .\. |
| NJReport.bat NJReport.sh | You can use this tool to start Designer without the command window. | java  com.jinfonet.designer.JReport [-options][reportfile] | -help Output the help message. -vDebug Set engine file's log level to INFO. -vError Set engine file's log level to ERROR. You may need to set an appropriate -Dfile.encoding option in the file to start Designer in order to view characters correctly. |
| PageSetup.bat PageSetup.sh | You can use this tool to update the page properties for multiple reports in the specified catalog at a time. | - | - |
| PropConvert.bat PropConvert.sh | You can use this tool to convert property values. Running this batch file displays a window from which you can modify many properties of a selected report file. This is most useful when you want to modify several properties using the same value at the same time. For example, if a Label and several DBFields share the same background of blue, and now you want to change them all to transparent, you can simply use this tool. | - | - |
| rp.bat rp.sh | You can use this tool to replace the Designer user ID and license key. | rp UID Key | - |
| rptconv.bat rptconv.sh | You can use this tool to convert reports created by earlier releases to the current. | rptconv "-source=source_path" ["-target=destination_path"] [-r] [-s] | -source Specify the source path of the reports to be converted. -target Specify the destination path for the converted reports. -r Replace the source report with the converted version. When you set this option, Designer ignores ["-target=destination_path"]. -s Convert all reports in the specified directory, including the reports in all subdirectories.  -cat Specify the catalog file for the list of files to be converted from the specified directory. -mapfile Specify a JSON file to match the report to the catalog based on the “-source=path” directory. The JSON data should be in the format: “res”:[{“rpts”: [report1, report2],”cat”: catalog}].If both the “-mapfile” and “-cat” options are provided simultaneously, the script will prioritize options with this order -mapfile > -cat > default. If you do not specify both -r and -target, Designer saves the converted reports in the same directory as the source reports and names them converted_SourceReportName. |
| setenv.bat setenv.sh | You can use this tool to generate the report environment variables before starting Designer. | - | - |

 

## 
Updating the Page Properties of Multiple Reports

You can run PageSetup.bat/PageSetup.sh to update the page properties of all reports in a specified catalog at a time conveniently.

- Run PageSetup.bat or PageSetup.sh to display the Page Setup for All Report dialog box.

- Select Browse to specify the catalog that contains the reports the page properties of which you want to batch update.

- In the General tab, edit the page properties you want to change for the reports.

- In the Export tab, edit the page properties for the outputs of the reports in each export format: select a format from the Export To drop-down list, from the Use General Settings drop-down list, specify whether to use the settings you define in the General tab for this format, and if you select false, specify the size, orientation, and margin for the pages of the report outputs in this format accordingly.

- Select Apply to All and a Warning dialog box displays, listing the page properties that will be updated.

- Select OK to update the specified page properties for all reports in the catalog. For any property that you do not specify in the dialog box, Designer keeps its original value in all the reports.

 

## 
Converting Reports to the Current Release

The following are examples of running rptconv.bat/rptconv.sh to convert reports created by earlier releases to the current. 

To convert a single report

- 
rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" "–target=C:\temp" This converts C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls to C:\temp\Payroll Report.cls. 

- 
rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" "–target=C:\temp\1.cls.xml" This converts C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls, saves the converted report to C:\temp, and names it 1.cls.xml (if the license allows). 

- 
rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" This converts C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls, saves the converted report in the same directory, and names it converted_Payroll Report.cls. 

- 
rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls" -r This overwrites C:\LogiReport\Designer\demo\reports\SampleReports\Payroll Report.cls.

To convert all reports (*.cls, *.rpt, *.clx, *.cls.xml) in a directory

- 
rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp" This converts all reports in C:\LogiReport\Designer\demo\reports and saves the converted reports to C:\temp. The converted reports use the same file names as the source reports. 

- 
rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp" -s This converts all reports in C:\LogiReport\Designer\demo\reports and in the subdirectories and saves the converted reports to C:\temp. The converted reports apply the same file names and directory structure as the source reports.

- 
rptconv "-source=C:\LogiReport\Designer\demo\reports" "–target=C:\temp\*.cls" -s This converts all reports in C:\LogiReport\Designer\demo\reports and in the subdirectories and saves the converted reports to C:\temp. The converted reports apply the same directory structure as the source reports and use .cls  as the file name extension. 

- 
rptconv "-source=C:\LogiReport\Designer\demo\reports" -r -sThis converts all reports in C:\LogiReport\Designer\demo\reports and in the subdirectories. The converted reports overwrite the source reports. 

- 
rptconv "-source=C:\LogiReport\Designer\demo\reports" This converts all reports in C:\LogiReport\Designer\demo\reports and saves the converted reports in the same directory as "converted_SourceReportName". 

To convert a group of reports with the same suffixes in a directory

The usage is similar to converting a directory. You can specify the wildcard to filter reports, for example: 

rptconv "-source=C:\LogiReport\Designer\demo\reports\SampleReports\*.cls" "–target=C:\temp" 

This converts all reports with the .cls extension in C:\LogiReport\Designer\demo\reports\SampleReports and saves the converted reports to C:\temp.

- There must be one and only one catalog file in the directory where the reports to be converted reside. 

- If the reports to be converted contain UDO or UDF, make sure you include the corresponding classes or jars in the class path of rptconv.bat/rptconv.sh.
