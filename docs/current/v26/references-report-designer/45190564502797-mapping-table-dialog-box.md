---
title: "Mapping Table Dialog Box"
id: 45190564502797
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190564502797-Mapping-Table-Dialog-Box
updated_at: 2026-04-30T15:13:58Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Mapping Table Dialog Box

You can use the Mapping Table dialog box to define the mappings based on which to pass on-screen filters in the primary report to the linked report, or to customize mappings between Current Field/Category/Series of the primary report and Corresponding Field of the linked report to apply dynamic filter conditions between the two reports. This topic describes the options in the dialog box.
    

Designer displays the Mapping Table dialog box when you select Mapping Table or  in the Insert Link dialog box or Edit Link dialog box.

Designer displays these options:

Fields (Primary)/Current Field

This column shows the fields in the primary report that you select to set up the mappings.

This drop-down list in the column contains all fields in the data resource used by the data component that contains the trigger object in the primary report. Select a field that is bound with an on-screen filter to define the mapping, or select a field to use as Current Field/Category/Series  of the primary report in the filter condition.

Fields (Linked)/Corresponding Field

This column shows the fields in the linked report that you select to set up the mappings.

This drop-down list in the column contains all fields in the data resource used by the selected component in the linked report, which are of the same data type as the specified primary report field. Select a field in the linked data component whose values are the same as those of the specified primary report field to apply the on-screen filter bound with the primary report field to the  linked report field, or select a field to use as Corresponding Field of the linked data component in the filter condition.

Add button

Select to add a mapping line.

Remove button

Select to delete the specified mapping line.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
