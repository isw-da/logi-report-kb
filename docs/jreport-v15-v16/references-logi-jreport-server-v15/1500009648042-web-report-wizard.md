---
title: "Web Report Wizard"
id: 1500009648042
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648042-Web-Report-Wizard
updated_at: 2021-07-24T20:54:18Z
---

# Web Report Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672641-Unique-Key)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648062-Windows-Media-Properties)

# Web Report Wizard

The Web Report Wizard appears when you select New > Web Report on the Logi JReport Console > Resources page, or select Menu > File > New Report or the New Report button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920357527/btn_newobj.gif) on the toolbar in Web Report Studio. It guides you through the process of creating a web report, and contains the following screens:

* [Page](#Page)
* [Layout](#Layout)
* [Bind Data](#Bind)
* [Style](#Style)

![](https://devnet.logianalytics.com/hc/article_attachments/4404926700567/btn_wbrpt_help.gif)

Displays the help document about this feature.

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Save**

Saves the report to the server resource tree.

**Run**

Opens the report in Web Report Studio in Edit Mode.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Page

Specifies the page settings of the report.  [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920402583/wbrptwzd_page.gif)

**Templates**

Specifies the template to be applied to the report.

* **Blank**   
   Specifies to use the blank template.
* **Template1**   
   Specifies to use Template1, in which you can specify the report title and company logo.
* **Template2**   
   Specifies to use Template2, in which you can specify the company logo, company title, report title and sub title.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009672341-Page-Setup) dialog to specify the page properties.

**Report Title**

Specifies the display name of the report title.

**Company Logo**

Specifies the company logo image file.

**Company Title 1**

Specifies the display name of the company title 1.

**Company Title 2**

Specifies the display name of the company title 2.

**Sub Title**

Specifies the display name of the sub title.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif)

Specifies the font properties for report title, sub title or company title.

* **Font**  
   Lists all the available font faces that can be selected to apply to the title.
* **Font Style**   
   Specifies the font style of the title. It can be one of the following: plain, bold, italic, and bold italic.
* **Size**  
   Specifies the font size of the title.
* **Align**  
   Specifies the position of the title to be left, right, center or justify.
* **Font Color**  
   Specifies the font color of the title.
* **Background Color**  
   Specifies the background color of the title.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920402327/btn_chsr2_29x20.gif)

Opens the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009647582-Insert-Image) dialog to customize the image for company logo.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Layout

Specifies the layout of the report. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920402839/wbrptwzd_layout.gif)

**Built-in layouts**

Lists the built-in layouts.

* **Default**  
   There is only a cell in the tabular.
* **Top and Bottom**  
   There are two cells in the tabular. One is at the top, and the other is at the bottom. Each cell uses half the height of the tabular.
* **T-Style**  
   There are two rows in the tabular. Each row uses half the height of the tabular. The top row has two cells with each using half the width of the row, and the bottom row has only a cell.
* **2×3**  
   There are six cells in the tabular. Each cell uses one third the height and one third the width of the tabular.
* **T-Style 2**  
   There are two rows in the tabular. Each row uses half the height of the tabular. The top row has only a cell, and the bottom row has two cells with each using half the width of the row.

**Toolbar**

The toolbar is enabled when a tabular cell in the below edit layout box is selected.

* **Horizontal Split**  
   Splits the selected tabular cell into two cells horizontally.
* **Vertical Split**  
   Splits the selected tabular cell into two cells vertically.
* **Merge**  
   Merges the selected adjacent tabular cells that form a rectangular into one cell.
* **Align**  
   Specifies how the component aligns in the tabular cell.
  + **Left**  
     Aligns the component to the left of the tabular cell.
  + **Center**  
     Aligns the component to the center of the tabular cell.
  + **Right**  
     Aligns the component to the right of the tabular cell.

**Edit layout box**

Specifies the component to be inserted into the selected tabular cell.

* **Existing Components**  
   Specifies a component from the ones existing in the open report to create the report.
* **New Components**  
   Specifies the component you want to place in the tabular cell.
  + **Table**  
     Creates a table in the tabular cell.
  + **Crosstab**  
     Creates a crosstab in the tabular cell.
  + **Chart**  
     Creates a chart in the tabular cell.
  + **Blank**  
     Creates nothing in the tabular cell.

**Tabular Cell Size**

Displays the size of the selected tabular cell, in percent.

* **Width**  
   Shows the width of the tabular cell.
* **Height**  
   Shows the height of the tabular cell.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Bind Data

Specifies the data source and the fields to be displayed in each component selected in the Layout screen. This screen differs according to the following component types: [table](#table), [crosstab](#crosstab), [chart](#chart). When the component type is specified as Blank, the screen is disabled.

### For Table Component

Specifies the data displayed in the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920403095/wbrptwzd_bnddt_table.gif)

**Table Title**

Specifies the title of the table. The title is a special label bound with the table. Though it can be positioned freely in a report, once you remove the table from the report, the title will be removed too.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the table title.

**Data Source**

Specifies the business view in the current catalog on which the table will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009672441-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Table type drop-down menu**

Specifies the type of the table. The tabs available in the screen differ according to the selected table type. When a group table type is selected, you can define the table in the Details, Group and Summary tabs respectively; when the summary table type is selected, only the Columns tab is available.

* **Group Above**  
   Creates a table with group information above the detail row.
* **Group Left**  
   Creates a table with group information left to the detail row.
* **Group Left Above**  
   Creates a table with group information left above the detail row.
* **Summary Table**  
  Creates a table with only group and summary information.

The tabs are different according to the following table types:

* [Group Left, Group Above and Group Left Above](#GroupTable)
* [Summary Table](#SummaryTable)

#### For Group Left, Group Above and Group Left Above

**Details Tab**

Specifies the fields that you want to display in the table.

* **Resources**   
   Displays all the view elements in the selected business view. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-#DynamicFormula) to use in the table.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)  
   Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.
  + **Predefined Order**  
     Sorts the view elements in the order defined in the Business View Editor on Logi JReport Designer.
  + **Resource Types**  
     Sorts the view elements by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
  + **Alphabetical Order**  
     Sorts the view elements in alphabetical order. Elements that are not in any category will be sorted first, then the categories, and the elements in each category will also be sorted alphabetically.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)  
   Launches the quick search toolbar to search for view elements. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)  
   Adds the selected view element to be displayed in the table.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif)  
   Removes the selected view element.
* **Field**  
   Lists the view elements that have been added to the table.
* **Label**  
   Specifies the display names of the added view elements.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)  
   Moves the selected view element one step up.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)  
   Moves the selected view element one step down.
* **Sort Fields By**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009647142-Custom-Sort) dialog to specify how to sort data in the table.

**Group tab**

Specifies the fields to group the data.

* **Resources**  
   Displays all the available group objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) you can use to group data in the table. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-#DynamicFormula) to use in the table.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)  
   Sorts the group objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)  
   Launches the quick search toolbar to search for group objects. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)  
   Adds the selected group object as a group by field.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif)  
   Removes the selected group object.
* **Field**  
   Lists all the group objects that have been added as the group by fields.
* **Sort**  
   Specifies the sort order for groups at the specific group level.
  + **Ascend**  
     Groups will be sorted in an ascending order (A, B, C).
  + **Descend**  
     Groups will be sorted in a descending order (C, B, A).
  + **No Sort**  
     Groups will be sorted in the original order in database.
  + **Custom Sort**  
     Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009647142-Custom-Sort) dialog to set how groups will be sorted.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)  
   Moves the selected group object one step up.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)  
   Moves the selected group object one step down.

**Summary tab**

Specifies the fields on which to create summaries.

* **Resources**  
   Displays all the available aggregation objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) you can use to create summaries in the table. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-) to use in the table.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)  
   Sorts the aggregation objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)  
   Launches the quick search toolbar to search for aggregation objects. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)  
   Adds the selected aggregation object as the summary field.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif)  
   Removes the selected aggregation object.
* **Field**  
   Lists the groups that have been added in the table and the aggregation objects added to summarize data in each group.
* **Row**  
   Specifies to put the summary field in the header or footer row. If the summary is calculated on a group by field, it will be put in the group header or footer row of the corresponding group; if the summary is calculated on the whole dataset, it will be put in the table header or footer row. Available only when the table is Group Left type.
* **Column**  
   Specifies to put the summary field in the specified detail column. If no column is selected, the summary field will be displayed in a separate summary column. Available only when the table is Group Left type.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)  
   Moves the selected aggregation object one step up.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)  
   Moves the selected aggregation object one step down.

#### For Summary Table

**Columns tab**

Specifies the fields to be displayed as the columns of the table.

* **Resources**   
   Displays all the group and aggregation objects in the selected business view. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-) to use in the table.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)  
   Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)  
   Launches the quick search toolbar to search for view elements. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)  
   Adds the selected view element to be displayed in the table.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif)  
   Removes the selected view element.
* **Column**  
   Lists the view elements that have been added to the table.
* **Sort**  
   Specifies the sort order for groups at the specific group level.
  + **Ascend**  
     Groups will be sorted in an ascending order (A, B, C).
  + **Descend**  
     Groups will be sorted in a descending order (C, B, A).
  + **No Sort**  
     Groups will be sorted in the original order in database.
  + **Custom Sort**  
     Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009647142-Custom-Sort) dialog to set how groups will be sorted.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)  
   Moves the selected view element one step up.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)  
   Moves the selected view element one step down.

**Summary tab**

Specifies to insert aggregations to the header/footer rows of the table and groups.

* **Resources**  
   Displays the aggregations selected in the Columns tab.
* **Summarized Fields**  
   Displays the group fields selected in the Columns tab under the Table node.
* **Header**  
   Represents the table header or the group header of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding header rows.
* **Footer**  
   Represents the table footer or the group footer of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding footer rows.

### For Crosstab Component

Specifies the data displayed in the crosstab. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920503063/wbrptwzd_bnddt_crstb.gif)

**Crosstab Title**

Specifies the title of the crosstab. The title is a special label bound with the crosstab. Though it can be positioned freely in a report, once you remove the crosstab from the report, the title will be removed too.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the crosstab title.

**Data Source**

Specifies the business view in the current catalog on which the crosstab will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009672441-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Resources**

Displays the elements in the selected business view. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-) to use in the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)

Edits the selected dynamic resource.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)

Removes the selected dynamic resource.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)

Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)

Launches the quick search toolbar to search for view elements. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)

Adds the selected group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) to be displayed on the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920379799/btn_addrow.gif)

Adds the selected group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) to be displayed on the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920380311/btn_addsum.gif)

Adds the selected aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) and detail object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif) to be the summary field of the crosstab.

**Columns/Rows**

* **Field**  
   Lists the group objects that will be displayed on the columns/rows of the crosstab.
* **Label**  
   Specifies the display names of the group objects. You can select in the cells to edit them if required.
* **Sort**  
   Specifies the sort order of the group objects.

**Summaries**

* **Field**  
   Lists the aggregation/detail objects that you select to create summaries.
* **Label**  
   Specifies the display names of the aggregation/detail objects. You can select in the cells to edit them if required.
* **Aggregation**  
   Specifies the functions used to summarize data of the detail objects.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009671541-Comparison-Function) dialog to add a comparison function as an aggregate for the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)

Moves the selected view element one level up.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)

Moves the selected view element one level down.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)

Removes the selected view element.

### For Chart Component

The screen for the chart component varies with different chart types: [common chart types](#Common), [organization chart](#Org), [heat map](#Map).

#### For Common Chart Types

Specifies the data displayed in the chart. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920503319/wbrptwzd_bnddt_chart.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the chart title.

**Data Source**

Specifies the business view in the current catalog on which the chart will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009672441-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Resources**

Displays the view elements in the selected business view. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-) to use in the chart.

* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)  
   Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)  
   Launches the quick search toolbar to search for view elements. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)

Adds the selected resource to be displayed in the chart.

**Value box**

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects.

* **Primary Axis**  
   Adds a chart type to the primary axis.
* **Secondary Axis**  
   Adds a chart type to the secondary axis. Active only when the option Secondary Axis is checked.
* **X-Axis**  
   Lists the value you want to show on the X axis of the bubble chart.
* **Y-Axis**  
   Lists the value you want to show on the Y axis of the bubble chart.
* **Size**   
   Lists the value you want to show as the bubble size.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920392343/btn_wbrpt_adcmbtyp.gif)

Adds a combo chart to the Primary Axis or Secondary Axis.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)

Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009647202-Edit-Additional-Value) dialog to edit the selected additional value.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)

Moves the selected view element one level up.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)

Moves the selected view element one level down.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif)

Adds a new pair of Y Axis and Radius for the bubble chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)

Removes the selected resource.

**Secondary Axis**

Specifies whether to show the secondary axis in the chart.

**Category box**

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) that will be displayed on the category axis of the chart.

For a real time chart, if no object is specified on the category axis, Use System Refresh Time will be automatically displayed in the category box, namely, the time at which the chart refreshes itself will be used as the category value.

**Series box**

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) that will be displayed on the series axis of the chart. Not available to real time chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920392855/btn_wbrpt_topn.gif)

Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009647162-Category-Options) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009647762-Series-Options) dialog to define the sort order of the category or series values and specify the number of the category or series values that will be displayed in the chart.

**Motion Bar for Playable Chart**

Lists the group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) you want to use as the motion field. A motion field can only be of Integer, Date or Time data type. Available to single bar, bench and bubble chart types only.

* **Special Function**  
   Available only when the motion field is of Date data type. Select it to define the special function.
  + **Field**  
     Displays on which field the special function will be applied.
  + **Function**  
     Specifies the special function to the field.
  + **OK**  
     Accepts the special function settings and leaves the dialog.
  + **Cancel**  
     Cancels the special function settings and leaves the dialog.

**Real Time**

Specifies to run the chart in real time mode, which means it will be updated automatically by using real time data. Available to single bar, bench, line, and area chart types only.

* **Use System Time for Category**  
   Specifies to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
   Specifies the time interval at which the chart will get data and refresh itself automatically.
* **Show Most Recent N Points**  
   Specifies the number of records that will be kept for the real time data on the chart.
* **Incremental Fetch**  
   Opens the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009672641-Unique-Key) dialog to configure a unique key for the real time chart.

#### For Organization Chart

Specifies the data displayed in the chart. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920503575/wbrptwzd_bnddt_chart_org.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the chart title.

**Data Source**

Specifies the business view in the current catalog on which the chart will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009672441-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Resources**

Displays the resources that can be added to org chart. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-) to use in the chart.

* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)  
   Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)  
   Launches the quick search toolbar to search for view elements. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).

**Value box**

* **Primary Axis**  
   Select Org from the chart type drop-down menu.
* **Node**  
   Adds a field from the Resources box which identifies the entity by selecting both the field and Node and then selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif).
* **Parent**  
   Adds a field from the Resources box which shows the "reporting to" relationship among the entity members, that is, which child node field member reports to or belongs to which child node field member, by selecting both the field and Parent and then selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif).
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected child node or parent field.

**Properties**

The Properties box presents a node model of the org chart. Data fields, labels and images can be inserted into the node as the information about the entity in the org chart, by using ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif). By default all added objects are placed at the left top of the node, you need to adjust their positions and sizes in the node. You can also resize the node if required.

To remove an object from the node, select it and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif).

#### For Heat Map

Specifies the data displayed in the chart. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920503831/wbrptwzd_bnddt_chart_htmp.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the chart title.

**Data Source**

Specifies the business view in the current catalog on which the chart will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009672441-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Resources**

Displays the resources that can be added to the chart. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-) to use in the chart.

* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)  
   Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)  
   Launches the quick search toolbar to search for view elements. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)

Adds the selected field into the Area or Property box.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif)

Removes the selected field from the Area or Property box.

**Chart type drop-down list**

Displays Heat Map as the selected chart type.

**Area**

Lists the fields used to group the data to different areas. There should be at least one group. When there are multiple groups, their levels are defined by their positions from top down. The group at the top is of the highest level and the bottom the lowest.

* **Color by**  
   Specifies whether to color by a group. 0-n groups can be used as the color-by fields.
* **Label by**  
   Specifies whether to show the group name in the innermost rectangle.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)  
   Moves the selected group field one level up.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)  
   Moves the selected group field one level down.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920392855/btn_wbrpt_topn.gif)  
   Opens the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009672121-Group-Options) dialog to define the sort order of the group values and specify the number of the group values that will be displayed in the chart.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected group field.

**Property**

Lists the summary fields used as size-by/color-by or displayed in the innermost rectangle.

* **Size by**  
   Specifies to size by one summary or none.
* **Color by**  
   Specifies to color by one summary or none.
* **Label by**  
   Specifies whether to show a summary in the innermost rectangle.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Style

Specifies the style of the report. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920403607/wbrptwzd_style.gif)

**Styles**

Lists all the available styles for you to select from. No style will be applied when you select None.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672641-Unique-Key)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648062-Windows-Media-Properties)
