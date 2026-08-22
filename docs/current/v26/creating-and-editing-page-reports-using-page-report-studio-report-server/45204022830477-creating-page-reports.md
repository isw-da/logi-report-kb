---
title: "Creating Page Reports"
id: 45204022830477
section: "Creating and Editing Page Reports Using Page Report Studio Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204022830477-Creating-Page-Reports
updated_at: 2026-04-30T14:10:37Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Creating Page Reports 

In Page Report Studio, you can create page reports or add new report tabs to the current page report if the corresponding catalog contains predefined business views. This topic describes how you can create page reports and report tabs.

Before you can create page reports, you should make sure that the Pop-up Blocker is not enabled on your web browser.

You need a Report Live license for Server to use this feature. For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

This topic contains the following sections:

- Creating a Page Report

- Creating a Banded Report
                

- Creating a Table Report
                

- Creating a Chart Report
                

- Creating a Crosstab Report
                

## 
Creating a Page Report

- Do any of the following:
    
- In the Server Start page, select Page Report in the Create category. Server displays a page. Specify the folder in which you want to create the report, then the catalog that contains the business view you want. Select OK. 

- On the Server Console, go to the Resources page, then:
        
- Select New > Page Report on the task bar. Server displays a page. Specify the folder in which to create the report, then the catalog that contains the required business view. Select OK.

- Open a folder that contains catalogs, select the catalog for the new report from the Catalog button  drop-down list, then select New > Page Report on the task bar.

- In Page Report Studio, navigate to Menu > File > New Page Report.

Server displays the New Page Report dialog box for you to create a page report with the first report tab in it.

- Specify the title of the report tab in the Report Title text box.

- In the Choose Report Layout box, select the layout with which you want to create the report tab.

- Select OK to create the report tab.
    
- If you selected Blank as the layout, Server creates a blank report tab. You can then use the Toolbox and the Resource View panels to add objects and view elements to the report tab.

- Select Blank Template to open Report Studio.	

- If you select the layout as Banded, Table, Chart, or Crosstab, Server displays the corresponding report wizard. Specify the settings according to your requirements.    Tip: In the report wizard, if there is only one business view in the current catalog, Server uses this business view to create the report tab by default, and hides the Data screen from the wizard. This is the same case when there is only one style available to apply to the report tab.

You can also use URL command to directly open the New Page Report dialog box to create a page report.

To create a report tab in an existing page report, in Page Report Studio, select Menu > File > New Page Report Tab or the Add button  on the toolbar. Server displays the New Report Tab dialog box. Specify the title and layout of the report tab, then select OK.

The following shows in detail how to create a report tab from a particular layout.

## 
Creating a Banded Report

A banded object is a kind of component that can present grouped data and detailed data, and is composed of several banded panels with which you can easily organize data fields and other elements.

To create a banded report:

- In the New Page Report dialog box, select Banded as the layout and select OK. Server displays the Banded Wizard.

- In the Data screen, select the business view or dataset in the current catalog, on which you want to create the banded object.
    

- In the Display screen, add detail objects  or group objects  from the Resources box to display as detail fields in the banded object. 

- To edit the display order of the objects, select one and then select the Move Up button  or Move Down button . 

- By default, Server uses the display names of the added objects to label the corresponding detail columns. To edit the label text for a detail column, select in the Display Name text box and type a new one. If you want to automatically map the label text to the dynamic display name of the object, select the Auto Map Field Name checkbox beside the text box.
    

- In the Group screen, add group objects  as the grouping criteria, then specify the sort direction of each group in the Sort column.
 To adjust the group levels, select a group and then select  or .
    

- In the Summary screen, add aggregation objects  to summarize data in the banded object: in the right box, specify the group to which you want to apply the aggregation, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select  or to adjust the order of the aggregations in the current group or move an aggregation to another group. By default, Server uses the display names of the added objects to label the corresponding summaries; to edit the label text for a summary, select in the Display Name text box and type a new one; if you want to automatically map the label text to the dynamic display name of the object, select the Auto Map Field Name checkbox beside the text box.
    

- In the Dataset> Filter screen, specify the filter you want to apply to the dataset of the data component. If the selected business view or dataset contains parameters, Server displays the Enter Parameter Values dialog box for you to specify values to the parameters before it displays the Dataset Filter screen.

- In the Style screen, apply a style to the banded object.

- Select Finish to create the report.

## 
Creating a Table Report

Tables give you great control over how to present data, including placing fields, grouping them, and sorting them.

To create a table report:

- In the New Page Report dialog box, select the table type you want in the Choose Report Layout box, then select OK. Server displays the Table Wizard.
    
- 
Table (Group Above)
        Select if you want to create a table with group information above the detail row.

- 
Table (Group Left)
        Select if you want to create a table with group information left to the detail row.

- 
Table (Group Left Above)
        Select if you want to create a table with group information left above the detail row.

- 
Summary Table
 Select if you want to create a table with only group and summary information. In a summary table, all the group names are in the group header of the innermost group.

- In the Data screen, select the business view or dataset in the current catalog, on which you want to build the table.

- In the Display screen, add detail objects  or group objects  from the Resources box to display as detail fields in the table. To edit the display order of the objects, select one and select the Move Up button  or Move Down button . By default, Server uses the display names of the added objects to label the corresponding detail columns; to edit the label text for a detail column, select in the Display Name text box and type a new one; if you want to automatically map the label text to the dynamic display name of the object, select the Auto Map Field Name checkbox beside the text box.  For a summary table, Server does not display the detail fields that you specified on the Display screen, in the generated table by default.

- In the Group screen, add group objects  as the grouping criteria, then specify the sort direction of each group in the Sort column. To adjust the group levels, select a group and select  or .    
    

- In the Summary screen, add aggregation objects  to summarize data in the table: in the right box, specify the group to which you want to apply the aggregation, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select  or to adjust the order of the aggregations in the current group or move an aggregation to another group. For the Group Left table, you can use the Row and Column columns to control the position of the aggregations in the table. By default, Server uses the display names of the added objects to label the corresponding summaries. If the table is not Group Left type, you can edit the label text for a summary: select in the Display Name text box and type a new one; if you want to automatically map the label text to the dynamic display name of the object, select the Auto Map Field Name checkbox beside the text box.
  

- In the Dataset> Filter screen, specify the filter you want to apply to the dataset of the data component. If the selected business view or dataset contains parameters, Server displays the Enter Parameter Values dialog box for you to specify values to the parameters before it displays the Dataset Filter screen.

- In the Style screen, apply a style to the table.

- Select Finish to create the report.

## 
Creating a Chart Report

A chart organizes and graphically presents data in a way that makes you easily see comparisons, trends, and patterns in data. It represents the report data in a visually straightforward form. 

For more information, select the following links to view topics in the Report Designer Guide:

- Chart Types

- How Data Is Represented in a Chart

- Chart Elements

To create a chart report in Page Report Studio:

- In the New Page Report dialog box, select Chart as the layout and select OK. Server displays the Chart Wizard.

- In the Data screen, select the business view or dataset in the current catalog, on which you want to build the chart.

- In the Type screen, specify the chart type.
    

A default chart type exists in the Chart Type Groups box. To replace it with another one, select a chart type from the Chart Type box. Server displays the thumbnails of the subtypes in this type, in the Subtype box. Select the required subtype to replace the default chart type.

If you want to create a combo chart, select <Add Combo Type> of Primary Axis or Secondary Axis in the Chart Type Groups box. Server adds an additional subtype. To replace the additional subtype, select it, then specify the required type and subtype respectively in the Chart Type and Sub Type boxes.

To add more subtypes, repeat the procedures. To remove a subtype, select it and then select the Remove button .

- In the Display screen, select a group object  in the Resources box and add it to the Category or Series box, the data of which Server displays on the corresponding axis. Select a subtype in the Show Values box, then add an aggregation object  or an additional value as the data of the subtype. You can add more than one aggregation object or additional value to a subtype. Each added subtype shall have at least one aggregation object or additional value.
 For a subtype that is a bubble chart, you can add two or three aggregation objects 
 to the subtype.
    

To add an additional value to a subtype:

- Select the subtype in the Show Values box.

- In the Resources box, expand Additional Values, then select Constant Value/Average Value.

- Select the Add button  beside the Show Values box. Server displays the Edit Additional Value dialog box.

- In the Name text box, specify the display name for the constant/average value.

- Type the constant value with numeric type in the Value text box, or select a field based on which Server calculates the average value, from the Based On drop-down list. 

- Select OK. Server adds the defined constant/average value to the subtype.
        If you want to further modify a constant/average value, select the value in the Show Values box, then select the Edit button . Server displays the Edit Additional Value dialog box for you to edit the value. 

- 
If you want to customize the sort order and define the Select N condition for values on the category/series axis of the chart, select Order/Select N in the Display screen, then define the condition in the Order/Select N dialog box:

- In the Order box, specify in which order you want to sort values on the category/series axis.

- In the Select N box, specify the Select N condition to All, Top, or Bottom. If you selected All, Server displays all category/series values in the chart; if you selected Top or Bottom, Server enables the text box next to it and you can specify an integer here, which means that Server displays the first or last N category/series values in the chart.

- Select Based On and specify values for the two drop-down lists that follow.
        If you do not select Based On, the order of the first or last N category/series values bases on what you specified in the Order box; if you select it, the order bases on values of a field on the value axis and the sort direction you specified in the drop-down lists next to Based On.

- If you selected Top or Bottom from the Select N drop-down list, you can select Other and then type a string in the next text box, so that the category/series values beyond the first or last N range will merge into the group with the name as that string.

- Select OK to accept the settings.

- In the Dataset> Filter screen, specify the filter you want to apply to the dataset of the data component. If the selected business view or dataset contains parameters, Server displays the Enter Parameter Values dialog box for you to specify values to the parameters before it displays the Dataset Filter screen.

- In the Style screen, apply a style to the chart.

- Select Finish to create the report.

## 
Creating a Crosstab Report

A crosstab summarizes data and presents the summaries in a compact row and column format. Report also supports a unique compound crosstab that enables you to put multiple compound row groups and column groups together and define summaries for every combination of a compound row group and column group. This makes far more sophisticated crosstab analysis possible.

- In the New Page Report dialog box, select Crosstab as the layout and select OK. Server displays the Crosstab Wizard.

- In the Data screen, select the business view or dataset in the current catalog, on which you want to build the crosstab.

- In the Display screen, specify the fields you want to display in the crosstab.
    

 From the Resources box, add group objects  to the Columns/Rows box to display on the column/row headers of the crosstab. If you want to display compound column/row groups in the crosstab, select the Add Compound Group button  under the bottom right corner of the Columns/Rows box to create the groups, then select each group and add the group objects to it. You can specify a sort manner on each group object in the Sort column. Add aggregation objects  from the Resources box to the Summaries box to create aggregations in the crosstab. If you have created compound column/row groups in the crosstab, you can create aggregations for each combination of the compound groups by selecting a compound column group and a compound row group and then adding the required aggregation objects. 
    

For each column/row/summary field, you can select in the Display Name text box and type a name to label the corresponding column header/row header/summary, or select the Auto Map Field Name checkbox beside the text box if you want to automatically map the label text to the dynamic display name of the field (when the text box is blank and you did not select the checkbox, Server does not create the label).

If you want to remove a group object, an aggregation object, or a compound column/row group, select it and then select the Remove button . To adjust the order of them, select one and then select  or .

- In the Dataset> Filter screen, specify the filter you want to apply to the dataset of the data component. If the selected business view or dataset contains parameters, Server displays the Enter Parameter Values dialog box for you to specify values to the parameters before it displays the Dataset Filter screen.

- In the Style screen, apply a style to the crosstab.

- Select Finish to create the report.

Tip: When you create a crosstab with a wizard, by default, Server does not create labels for its columns, rows, or summaries (the Display Name columns in the Columns, Rows, and Summaries boxes of the wizard are blank by default). You can make Page Report Studio automatically provide the display names of the added objects in the wizard, by setting the profile propertiesAdd Labels for Crosstab Rows and Columns and Add Labels for Crosstab Summaries. You can also customize the profile property Display Crosstab Summaries Vertically to make the summaries in crosstabs display horizontally in Page Report Studio.
