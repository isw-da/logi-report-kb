---
title: "Save As Dialog Box Properties"
id: 28891656504845
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891656504845-Save-As-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:52Z
source_host: docs-report.zendesk.com
---
# 
Save As Dialog Box Properties 

You can use the Save As dialog box to save a report as a new file or as a new version. This topic describes the properties in the dialog box.

Save In 

Specify the directory in the server resource tree where you want to save the report. Use the navigation button  to go to the parent folder. You cannot save resources in the root folder.

The resource table shows the reports in the current directory. You can select the column names to change the order of the reports in the table.

- 
Name
    Report file names.

- 
Size
 Report file size.

- 
Type
    Report file type.

- 
Last Modified
    Last modified time of the report files.

File Name

Specify the name for the report you want to save, without suffix. 

Type

Select the type of the saved report.

- 
Page Report (.cls)
Select to save the report as a binary formatting file. This is the format that provides optimal performance in the Report toolset.

- 
Report Template (.rpt)
    Select to save the report as a text file, which you can edit in any text editor.

- 
Self Contained Page Report (.clx)
    Select to save the report as a binary report file, which contains not only the report's layout but also the catalog with its own resources.

- 
Page Report XML Format (.cls.xml)
 Select to save the report as an XML file following the XML standard, which you can edit using external XML editors besides Report Designer and Page Report Studio. You cannot save page reports that contain customized user defined objects (UDO) to XML. Using the XML format is better for checking into source code control systems than using the binary formats.

Advanced/Simple

Select to display or hide the following properties. 

- 
Catalog
  Server displays the following two properties when you did not clear Select Catalog Linking Model in the Page Report Studio profile.
    
- 
Set Original Catalog as Linked Catalog into Saved Report
      Select if you want to link the saved report with the catalog. The saved report will run with the catalog even if the two are in different folders. If later you update the catalog, the saved report will run with the latest version of the catalog.

- 
Set Catalog Copy to Target Folder
 Select if you want to copy the catalog to the folder where you save the report. The saved report will run with the copied catalog. 

- 
Save Sort Criteria
  Select to save the changes you made by sorting.

- 
Save Filter Criteria
  Select to save the changes you made by filtering.

- 
Description
Provide a description for the saved report.

OK

Select to save the report and exit the dialog box.

Cancel

Select to close the dialog box without saving the report.

Help

Select to view information about the dialog box.
