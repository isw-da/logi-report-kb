---
title: "Customizing Business Views for Reports"
id: 45204021379981
section: "Managing Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204021379981-Customizing-Business-Views-for-Reports
updated_at: 2026-04-30T14:10:28Z
source_host: logi-report-v26.insightsoftware.com
---
# 

            Customizing Business Views for Reports

This topic describes how you can customize business views for reports as an administrator. 

For a report you created in Report Designer while its Constrained Data property is false, or for a report you created on Server, you can customize the business views for the report. In this way, the combination of the customized business views and the business views used by the report are available to the report.

This topic contains the following sections:

- Selecting Business Views for a Report Using the Properties Dialog Box

- Importing Business Views for Reports Using the Administration Menu

## 
Selecting Business Views for a Report Using the Properties Dialog Box

- 
Access the Properties dialog box of the report that has a catalog available in the server resource tree and that is not in the My Shared folder.

- Select the Available Business Views tab.

- Select the business views for the report to use.

- Select All if you want to select all the listed business views.

- To export the selected business views to a plain text file, select Export. The default file name is Report_File_Name.bvlst.

- Select OK to apply the selected business views to the report.

## 
Importing Business Views for Reports Using the Administration Menu

- On the system toolbar of the Server Console, navigate to Administration > Other > Business Views for Reports. Server displays the page:
              

- Select Browse to select a plain text file in which you specify business views using a JSON array like ["Data Source 1.BV1","Data Source 1.BV2"]. For example, you can select a file that you exported the selected business views to when selecting business views for a report using the Properties dialog box.          

- Select OK to import the business views from the file.
				

- Select the reports you want to use the imported business views.

- Select All if you want to select all the listed reports.

- Select OK to apply the imported business views to the selected reports.

When you work with a report in the Web Report Studio and Page Report Studio, 

- Whether you can see a business view available to the report depends on whether you have the permission. For more information, see Defining Business View Security in a Catalog.

- If you created the report in Report Designer and enabled its Constrained Data property, only the business views that the report uses are available to the report. In this case, if the report uses no business views, you cannot add any new data components in the report.
