---
title: "Inserting Tables in a Report"
id: 12479958585485
section: "Working with Components in Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479958585485-Inserting-Tables-in-a-Report
updated_at: 2026-02-25T23:50:23Z
source_host: docs-report.zendesk.com
---
# 
Inserting Tables in a Report

 You can create tables in a report easily using the table wizard. However, the procedure you use with the wizard varies with the data resource type: business view or query resource. This topic introduces how you can create a table using the table wizard when you have different data resources.

This topic contains the following sections:

- Creating a Table Based on a Business View

- Creating a Table Based on a Query Resource

 A page report can apply either query resources or business views, which is determined by the Create Using Business View option at the time when you create the page report. Once defined, all data components in the page report can only use the specified data resource type.
            

## 
Creating a Table Based on a Business View

- Position the mouse pointer at the allowed report location where you want to insert the table.
				

- Do either of the following:
    
- From the Components panel, drag the required table type icon in the Grid category  to the destination. 

- Navigate to Insert > Table or Home > Insert > Table, then in the Table Type dialog box choose a type for the table and select OK.
        

Designer displays the Create Table dialog box. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens. When creating a table in a web report or library component, you get different screens according to the table type: group table or summary table.

- In the Data screen, specify the dataset you want to use to create the
     table.

- Specify the data to display in the table.
    To define data for a group table in a web report/library component, or for a table in a page report

- In the Display screen, add the detail fields you want to display in the table. You can specify a title for the table in the Title text box.
        

 The Resources box lists the data objects that you can use as detail fields in the table. These objects include: group objects  and detail objects  in the business view from which the dataset the table applies is created, and dynamic formulas used as Group  and dynamic formulas used as Detail  that you have added for the business view in the current report.

- To add a detail field, select an object in the Resources box and select Add or drag the object from the Resources box to the right box.

- In the Display Name column, select in the text box to edit the label for each detail column in the table. When you select the Auto Map Field Name checkbox in the text box, Designer applies the field's display name to label the detail column, and at runtime, Server maps the label to the dynamic display name of the field if the administrator defines it.

- Select a field in the right box and select Move Up or Move Down to adjust the display order of the detail fields in the table.

- Select Sort Fields By to specify how to sort the detail values.

- In the Group screen, specify the criteria for grouping data in the table.
        

- In the Summary screen, add summaries to calculate data in the table.
        

The Resources box lists the aggregation objects   in the business view from which the dataset the table applies is created, and the dynamic formulas used as Aggregation and  dynamic aggregations that you have created for the business view in the current report. You can add them as summaries to calculate data in the table.

- To add a summary in the table, in the right box, select the group to which to apply the summary (if you select Table, it is based on the whole business view), select an object in the Resources box and select Add or drag the object from the Resources box to the right box. You can add several summaries for any group level.

- Use Move Up and Move Down to adjust the display order of the summaries in a group or move a summary to another group.

- The Position and Column options work together to determine the positions of the summaries in the table.
- For a Group Above table, Designer places a summary added for the Table level  in the intersection of the table footer panel and the first two detail columns with its name label which is the display name of the field used for the summary by default; Designer places a summary added for a specific group in the intersection of the group's footer panel and the first two detail columns with its name label.

- For a table of any other type, you can customize the position of the summaries. When a summary is added for the Table level, you can place it and its name label in the intersection of the table footer panel (Footer)/table header panel (Header) and the first two detail columns (Detail)/a new summary column (Summary); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column.

To define data for a summary table in a web report/library component

- In the Columns screen, specify the columns you want to display in the table.
        

The Resources box lists the group objects  and aggregation objects  in the business view from which the dataset the table applies is created, and the   dynamic formulas used as Group , dynamic formulas used as Aggregation , and dynamic aggregations that you have added for the business view in the current report. You can create columns in the table from these objects.

- To add a column, select an object in the Resources box and select Add or drag the object from the Resources box to the right box. Designer automatically groups the table  by the added group objects and the position of the group objects in the right box determines the group level: the topmost group object the highest group level and the lowest group object the innermost group level. All the aggregation objects are parallel and calculate based on the innermost group.

- Select an object in the right box and select Move Up or Move Down.to adjust the display order of the columns in the table.

- For any group level, you can customize its sort manner and define Select N condition to show data of certain range in its groups.

- In the Summary screen, insert the aggregation objects selected in the Columns screen to the table header/footer and to the group headers/footers of existing groups as summaries: first select an aggregation object in the Resources box, then select the checkboxes representing the required locations. Designer places the summary  in the intersection of the corresponding summary column and the table/group header/footer panel.
        

-  In the Dataset Filter screen, filter the dataset the table applies. If you have added filter conditions to the dataset somewhere else, Designer displays the conditions in the screen. You can further edit the conditions. Be aware that a filter on a dataset applies to all data components in the same report that use this dataset. 

- In the Style screen, specify the layout and style of the table.
    

- By default, Designer places the table vertically. If you are creating the table in a page report, you can select Horizontally  in the Grow Report box to create a horizontal table.

- In the Style box, select the style of the table. If you have specified to insert the table into a banded object, the table inherits its parent's style by default; to apply another style to the table, clear Inherit Style and select the required style from the Style box.

- Select Finish to insert the table.

- If you have selected a panel in a banded object as the destination and used the ribbon option to insert the table, after finishing the Create Table dialog box, you need to select in the destination once again to insert the table there.

## 
Creating a Table Based on a Query Resource 

- Position the mouse pointer at the allowed report location where you want to insert the table.

- Do either of the following:
    
- From the Components panel, drag the icon representing the required table type in the Grid category  to the destination.

- Navigate to Insert > Table or Home > Insert > Table, then in the Table Type dialog box choose a type for the table.

Designer displays the Create Table dialog box. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.

- In the Data screen, specify the dataset you want to use to create the
     table.
    

- In the Display screen, add data fields  to display as detail fields in the table.
    

The Resources box lists all DBFields in the query resource from which the dataset the table applies is created, and the formulas and parameters that are valid to these DBFields in the current catalog. You can use them as detail fields in the table. 

- To add a detail field, select a field in the Resources box and select Add or drag  the field from the Resources box to the right box.

- By default, Designer applies the display names of the added fields to label the corresponding detail columns. To edit the label for a detail column, select in the Display Name text box and type a new name.

- Select a detail field in the right box and select Move Up or Move Down to adjust the display order of the detail fields in the table.

- Select Sort Fields By to specify how to sort the detail values.

 When you are creating a summary table, by default, Designer does not show the detail columns for the added detail fields after the table is generated. If you want to show the detail columns in a summary table, take the following steps after the table is created： 

-  Select the table, right-click it and select Show Column on the shortcut menu.

- In the Show Column dialog box, select the column names for the detail columns you want to show and select OK.

- In the Report Inspector, select the Table Detail node of the table, set the Invisible property to false.

- In the Group screen, specify the criteria for grouping data in the table.
    

- In the Summary screen, add summaries to calculate data in the table. 
    

The Resources box lists all DBFields in the query resource from which the dataset the table applies is created, and the formulas that are valid to these DBFields in the current catalog. You can create summaries based on these fields in the table. 

- To add a summary, select the group in the right box to which to apply the summary  (if you select Table, it is  based on the whole dataset), select a field in the Resources box and select Add or drag the field from the Resources box to the right box. You can add several summaries for any group level.

- Specify the aggregate function of each summary. If you select DistinctSum, you should select the ellipsis in the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the Select Fields dialog box.  After the table is created, Designer automatically gives the summaries proper name labels to help you clarify the meaning of the numbers.

- Use Move Up and Move Down to adjust the display order of the summaries in the current group or move a summary to another group.

- The Position and Column options work together to determine the positions of the summaries in the table.
- For a Group Above table, Designer places a summary added for the Table level in the intersection of the table footer panel and the first two detail columns with its name label which is the display name of the field used for the summary; Designer places a summary added for a specific group in the intersection of the group's footer panel and the first two detail columns with its name label.

- For a table of any other type, you can customize the position of the summaries. For a summary added for the Table level, you can place it and its name label in the intersection of the table footer panel (Footer)/table header panel (Header) and the first two detail columns (Detail)/a new summary column (Summary); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column.

Designer automatically adds the summaries created from the Summary screen to the current catalog as static summaries even when identical summaries already exist. Therefore, it is better not to create summaries here, instead, you can add dynamic summaries to the catalog and drag and drop the dynamic summaries into the table after you finish creating it.

- In the Filter screen, filter the table by adding conditions based on the fields it contains. Select here for how to define a filter.
    

- In the Style screen, specify the layout and style of the table.

- In the Grow Report box, select whether to place the table vertically or horizontally.

- In the Style box, select the style of the table. If you have specified to insert the table into a banded object, the table inherits its parent's style by default; to apply another style to the table, clear Inherit Style and select the required style from the Style box.
                

- Select Finish to insert the table.

- If you have selected a panel in a banded object as the destination and used the ribbon option to insert the table, after finishing the Create Table dialog box, you need to select in the destination once again to insert the table there.

- 
Report Engine cuts the table content in some pages that cannot display when the height of the table is higher than that of the page. However, when you export the table to Excel using Column Format or Data Format, or to Text with Delimited Format, or to XML, the table can display completely in the output.

- When you create a table of the Group Above or Group Left type, by default, Designer aligns all the summaries of the same functions  horizontally in the table. If you want to align them vertically, select Align summaries vertically in the Component category of the Options dialog box in advance.
