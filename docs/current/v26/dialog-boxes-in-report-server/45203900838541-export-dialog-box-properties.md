---
title: "Export Dialog Box Properties"
id: 45203900838541
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203900838541-Export-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:18Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Export Dialog Box Properties 

You can use the Export dialog box to set settings for exporting reports to different formats. This topic describes the properties in the dialog box.

File Name

Specify the name of the output file.

View Report Result

Select if you want to directly open the report in the web browser that supports the format.

Save to File System

Select if you want  the web browser to prompt you to save the output file to a specified folder.

Save to Version System

Select if you want to save the report as a version in Report Server's versioning system.

Select Report Tabs

Select the report tabs you want to export, in the order as listed. If the report has only one report tab, Server select it by default.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Select Format

Select the format in which you want to export the report.

More/Less Options

Select to show/hide the additional properties for exporting the report to the specified format.

- 
Style Group
  If you have specified a style group via the Override Style Group property in the server profile, Server selects the style group by default. You can choose another style group from the list to apply to the exported output. If the page report was created in Report Designer, when you select <No Style>, the style group property predefined for the specific export format in Report Designer will apply.

- 
Other properties
  Specify the properties for the selected format: 
    
- PDF

- HTML

- Excel

- Text

- RTF

- XML

- PostScript

- 
Page Report Result
- 
Use Custom File Extension
Select if you want the output file to have no file extension or want to use a different file extension from the default one    (.rsd).

- 
Zip Result
            Select to compress the result and make its size smaller. 

OK

Select to export the report with the settings you specified here. If you have selected multiple report tabs to export at one time, and you have not specified parameter values for some of them, the Enter Parameter Values dialog box will pop up for you to specify their parameter values.

Cancel

Select to close the dialog box without exporting the report.

Help

Select to view information about the dialog box.
