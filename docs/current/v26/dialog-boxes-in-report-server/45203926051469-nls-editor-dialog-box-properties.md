---
title: "NLS Editor Dialog Box Properties"
id: 45203926051469
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203926051469-NLS-Editor-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:09Z
source_host: logi-report-v26.insightsoftware.com
---
# 
NLS Editor Dialog Box Properties

This topic describes how you can use the NLS Editor dialog box to edit NLS for the specified resource. 

Server displays the dialog box when an administrator selects the NLS Editor button  on the floating toolbar of a catalog, report, library component, or dashboard in the Resources page of the Server Console.

Report/Component/Dashboard

The name of the report/library component/dashboard. Available only when you are editing NLS for a report, library component, or dashboard.

Edit Subreport's NLS 

Select to edit each subreport's NLS. Available only when the report has subreports.

After you select Edit Subreport's NLS, Server displays a dialog box showing all the subreports of the report. To edit a subreport's NLS, select Edit NLS for it. The method of editing NLS for a subreport is the same as that for the primary report.

Catalog

The name of the catalog or the catalog that the report/library component/dashboard uses.

Select Another Catalog

Select and then specify another catalog for the report/library component/dashboard in the Select Another Catalog dialog box . Available only when you are editing NLS for a report, library component, or dashboard.

Report/Component/Dashboard Version

Select the report/library component/dashboard version you want to apply the NLS settings to. Available only when you are editing NLS for a report, library component, or dashboard.

Catalog Version 

Specify the catalog version.

Language

Server lists the languages into which you want to translate the display text in the catalog/report/library component/dashboard. If you cannot find the language you need, select  the Add button  above the box to add the language. 

Add button

- When you are editing NLS for a report, library component, or dashboard, select the button, and Server opens the Add Language dialog box for you to add a language.

- When you are editing NLS for a catalog, select the button, and Server opens the Select Language Source dialog box  for you to choose where you want to get a language.

Remove button

Select to remove the selected language from the Language box. 

Display Tab

Specify the translation of every display text in the catalog/report/library component/dashboard. You can select a column header to sort the items by that column in the ascending or descending order.

- 
Search box
  Type a keyword, and then select the Search icon  or press Enter to start searching. Server searches in both Key and Translate columns.

- 
Add button
  Select to open the Add Display dialog box to add available display text in the objects of the catalog/report/library component/dashboard for the target language.

- 
Remove button
   Select to remove the selected items for the target language.

- 
Type
    The type of the display text items.
      
- 
Column
          This type is only for page reports running in Page Report Studio. It is the type of display text of columns.

- 
DisplayName
          Type of display text of object display names.

- 
Metadata
          Type of display text of metadata. Metadata mainly refers to catalog resources, such as table/view columns, business views, formulas, summaries, and parameters.

- 
Label
          Type of display text of labels, some web controls, and UDOs.

- 
Prompt
          Type of display text of parameter prompt values.

- 
Title
          Type of display text of filter controls and library components.

- 
TOC
          Type of display text in the TOC tree.

- 
Key
  Keys to indicate the objects in the original language.

- 
Translate
  Specify the translation of the keys in the target language. 

Format tab

Specify the format for all fields in the catalog/report/library component/dashboard. You can select a column header to sort the items by that column in the ascending or descending order.

- 
Search box
  Type a keyword, and then select the Search icon  or press Enter to start searching. Server searches in both Key and Format columns.

- 
Add button
  Select to open the Add Format dialog box to add available formats in the objects of the catalog/report/library component/dashboard for the target language.

- 
Remove button
  Select to remove the selected items for the target language.

- 
Key
 Keys to indicate the formats in the original language.

- 
Format
Specify the formats for the keys in the target language.

Font tab

Specify font properties for all fields in the catalog/report/library component/dashboard. You can select a column header to sort the items by that column in the ascending or descending order.

- 
Search box
 Type a keyword, and then select the Search icon  or press Enter to start searching. Server searches in both the Font Face and Font Size columns.

- 
Add button
  Select to open the Add Font dialog box to add available fonts in the objects of the catalog/report/library component/dashboard for the target language.

- 
Remove button
  Select to remove the selected items for the target language.

- 
Key
  Keys to indicate the fonts in the original language.

- 
Font Face
  Specify the font face for the keys in the target language.

- 
Font Size
  Specify the font size for the keys in the target language.

Add to Global NLS

Select to add the selected display/format/font items to the target language's global NLS resource library. If some of the items already exist in the global NLS resource library of the target language, Server displays the Add to Global NLS dialog box for you to handle the duplication.

This property is not available to organization admin. 

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
