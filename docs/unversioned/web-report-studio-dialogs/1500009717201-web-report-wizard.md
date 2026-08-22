---
title: "Web Report Wizard"
id: 1500009717201
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717201-Web-Report-Wizard
updated_at: 2021-11-03T06:57:02Z
---

# Web Report Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009690922-User-Defined-Function-Editor)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717221-Windows-Media-Properties)

# Web Report Wizard

The Web Report Wizard guides you through the process of creating a web report, and contains the following screens: [Page](#Page), [Layout](#Layout), [Bind Data](#Bind)  and [Style](#Style). This dialog appears when you select New > Web Report on the task bar of the Resources page in the Logi JReport Server console, or select Menu > File > New Report or the New Report button ![](https://devnet.logianalytics.com/hc/article_attachments/4412139483159/btn_newobj.gif) on the toolbar in Web Report Studio.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412131442327/btn_wbrpt_help.gif)

Displays the help document about this feature.

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Save**

Saves the report to the server resource tree.

**Run**

Opens the report in Web Report Studio in Edit Mode.

## Page

Specifies the page settings of the report.

![Web Report Wizard - Page screen](https://devnet.logianalytics.com/hc/article_attachments/4412131400471/wbrptwzd_page.gif)

**Templates**

Specifies the template to be applied to the report.

* **Blank**   
   Specifies to use the blank template.
* **Template1**   
   Specifies to use Template1, in which you can specify the report title and company logo.
* **Template2**   
   Specifies to use Template2, in which you can specify the company logo, company title, report title and sub title.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009716761-Page-Setup) dialog to specify the page properties.

**Report Title**

Specifies the display name of the report title.

**Company Logo**

Specifies the company logo image file. Select ![Insert Image](https://devnet.logianalytics.com/hc/article_attachments/4412139488919/btn_chsr2.gif) to select the image in the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009716581-Insert-Image) dialog.

**Company Title 1**

Specifies the display name of the company title 1.

**Company Title 2**

Specifies the display name of the company title 2.

**Sub Title**

Specifies the display name of the sub title.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4412131381399/btn_wbrpt_font.gif)

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

## Layout

Specifies the layout of the report.

![Web Report Wizard - Layout screen](https://devnet.logianalytics.com/hc/article_attachments/4412139511447/wbrptwzd_layout.gif)

**Layouts**

Lists the built-in layouts for arranging components in the report. Choose the layout you want to use for the report.

**Buttons**

The buttons are enabled when a cell in the editing layout box is selected.

* **Horizontal Split**  
   Splits the selected cell into two cells horizontally.
* **Vertical Split**  
   Splits the selected cell into two cells vertically.
* **Merge**  
   Merges the selected adjacent cells that form a rectangular into one cell.
* **Align**  
   Specifies how the component aligns in the cell. Enabled when Use Tabular is checked.
  + **Left**  
     Aligns the component to the left of the cell.
  + **Center**  
     Aligns the component to the center of the cell.
  + **Right**  
     Aligns the component to the right of the cell.

**Use Tabular**

Specifies whether to use a tabular to lay out the components in the report.

**Editing layout box**

Specifies the component to be inserted into the selected cell.

* **Existing Components**  
   Specifies a component from the ones existing in the open report to create the report.
* **New Components**  
   Specifies the component you want to place in the cell: Table,
  Crosstab, Chart, Banded or Blank.

## Bind Data

Specifies the data source and the fields to be displayed in each component selected in the Layout screen. This screen differs according to the following component types: [Table](#Table), [Crosstab](#Crosstab), [Chart](#Chart) and [Banded](#Banded). When the component type is specified as Blank, the screen is disabled.

### For Table Component

![Web Report Wizard - Bind Data screen - Table](https://devnet.logianalytics.com/hc/article_attachments/4412112517527/wbrptwzd_bnddt_table.gif)

**Table Title**

Specifies the title of the table. The title is a special label bound with the table. Though it can be positioned freely in a report, once you remove the table from the report, the title will be removed too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4412131381399/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the table title.

**Data Source**

Specifies the business view in the current catalog on which the table will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009716841-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Table type drop-down menu**

Specifies the type of the table. The tabs available in the screen differ according to the selected table type. When a group table type is selected, you can define the table in the Details, Group and Summary tabs respectively; when the summary table type is selected, only the Columns and Summary tabs are available.

* **Group Above**  
   Creates a table with group information above the detail row.
* **Group Left**  
   Creates a table with group information left to the detail row.
* **Group Left Above**  
   Creates a table with group information left above the detail row.
* **Summary Table**  
  Creates a table with only group and summary information.

The tabs for defining a table are different according to the following table types:

* [For Group Left, Group Above and Group Left Above](#GroupTable)
* [For Summary Table](#SummaryTable)

#### For Group Left, Group Above and Group Left Above

**Details Tab**

Specifies the detail fields that you want to display in the table.

* **Resources** :   
   Displays the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) and detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4412139491991/btn_bvdtl.gif) in the selected business view. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-#DynamicFormula) to use in the table.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
   Sorts the objects in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.
  + **Predefined Order**  
     Sorts the objects in the order defined in the Business View Editor on Logi JReport Designer.
  + **Resource Types**  
     Sorts the objects by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
  + **Alphabetical Order**  
     Sorts the objects in alphabetical order. Objects that are not in any category will be sorted first, then the categories, and the objects in each category will also be sorted alphabetically.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).
* ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)  
   Adds the selected object to display in the table.
* ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)  
   Removes the selected object.
* **Field**  
   Lists the objects that have been added to the table as detail fields.
* **Label**  
   Specifies the text for the labels of the detail fields, which by default are the display names of the added objects. You can select in the text boxes to edit the label text, or check the Auto Map Field Name checkboxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)  
   Moves the selected object one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)  
   Moves the selected object one step down.
* **Sort Fields By**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009715841-Custom-Sort) dialog to specify how to sort data in the table.

**Group tab**

Specifies the fields to group the data in the table.

* **Resources**  
   Displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) you can use to group data in the table. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-#DynamicFormula) to use in the table.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
   Sorts the objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).
* ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)  
   Adds the selected object as a group-by field.
* ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)  
   Removes the selected object.
* **Field**  
   Lists all the objects that have been added to the table as the group-by fields.
* **Sort**  
   Specifies the sort order for groups at the specific group level.
  + **Ascend**  
     Groups will be sorted in an ascending order (A, B, C).
  + **Descend**  
     Groups will be sorted in a descending order (C, B, A).
  + **No Sort**  
     Groups will be sorted in the original order in database.
  + **Custom Sort**  
     Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009715841-Custom-Sort) dialog to set how groups will be sorted.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)  
   Moves the selected group one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)  
   Moves the selected group one step down.

**Summary tab**

Specifies the fields on which to create summaries in the table.

* **Resources**  
   Displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4412131382167/btn_bvaggrgtn.gif) you can use to create summaries in the table. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-) to use in the table.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
   Sorts the objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).
* ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)  
   Adds the selected object as the summary field.
* ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)  
   Removes the selected object.
* **Field**  
   Lists the groups that have been added in the table and the objects added to summarize data in each group.
* **Row**  
   Specifies to put the summary field in the header or footer row. If the summary is calculated on a group-by field, it will be put in the group header or footer of the corresponding group; if the summary is calculated on the table, it will be put in the table header or footer. Available only when the table is Group Left type.
* **Column**  
   Specifies to put the summary field in the specified detail column. If no column is selected, the summary field will be displayed in a separate summary column. Available only when the table is Group Left type.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)  
   Moves the selected object one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)  
   Moves the selected object one step down.

#### For Summary Table

**Columns tab**

Specifies the fields that you want to display as the columns of the table.

* **Resources**   
   Displays all the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) and aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4412131382167/btn_bvaggrgtn.gif) in the selected business view. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-) to use in the table.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
   Sorts the objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).
* ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)  
   Adds the selected object to display in the table.
* ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)  
   Removes the selected object.
* **Column**  
   Lists the objects that have been added to the table.
* **Sort**  
   Specifies the sort order for groups at the specific group level.
  + **Ascend**  
     Groups will be sorted in an ascending order (A, B, C).
  + **Descend**  
     Groups will be sorted in a descending order (C, B, A).
  + **No Sort**  
     Groups will be sorted in the original order in database.
  + **Custom Sort**  
     Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009715841-Custom-Sort) dialog to set how groups will be sorted.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)  
   Moves the selected object one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)  
   Moves the selected object one step down.

**Summary tab**

Specifies to insert aggregations to the header/footer rows of the table and groups.

* **Resources**  
   Displays the aggregations that are added in the Columns tab.
* **Summarized Fields**  
   Displays the groups that are added in the Columns tab under the Table node.
* **Header**  
   Represents the table header or the group header of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding header rows.
* **Footer**  
   Represents the table footer or the group footer of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding footer rows.

### For Crosstab Component

![Web Report Wizard - Bind Data screen - Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4412139538199/wbrptwzd_bnddt_crstb.gif)

**Crosstab Title**

Specifies the title of the crosstab. The title is a special label bound with the crosstab. Though it can be positioned freely in a report, once you remove the crosstab from the report, the title will be removed too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4412131381399/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the crosstab title.

**Data Source**

Specifies the business view in the current catalog on which the crosstab will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009716841-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Data tab**

Specifies the column, row and aggregate fields to display in the crosstab.

* **Resources**  
   Displays the group, detail, and aggregation objects in the selected business view. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-) to use in the crosstab.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)  
     Edits the selected dynamic resource.
  + ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
     Removes the selected dynamic resource.
  + ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
     Sorts the objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.
  + ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
     Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).
* **Columns/Rows**  
   Specifies the column/row fields to display in the crosstab.
  + **Field**  
     Lists the objects that will be displayed on the columns/rows of the crosstab.
  + **Label**  
     Specifies the text of the labels for the column/row headers. You can select the text boxes to edit the label text, or check the Auto Map Field Name checkboxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
  + **Sort**  
     Specifies the sort order of the group objects.
* **Summaries**  
   Specifies the aggregate fields to display in the crosstab.
  + **Field**  
     Lists the objects that you select to create summaries.
  + **Label**  
     Specifies the text of the labels for the summaries. You can select the text boxes to edit the label text, or check the Auto Map Field Name checkboxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
  + **Aggregate**  
     Specifies the functions used to summarize data of the detail objects.
  + **Comparison Function**  
     Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009715701-Comparison-Function) dialog to add a comparison function as an aggregate for the crosstab.
* ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)  
   Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) to display on the columns of the crosstab.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4412131392151/btn_addrow.gif)  
   Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) to display on the rows of the crosstab.
* ![Add Summary](https://devnet.logianalytics.com/hc/article_attachments/4412112504343/btn_addsum.gif)  
   Adds the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4412131382167/btn_bvaggrgtn.gif) and detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4412139491991/btn_bvdtl.gif) to be the summary field of the crosstab.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)  
   Moves the selected object one level up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)  
   Moves the selected object one level down.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected object.

**Layout tab**

Specifies the layout of the crosstab.

* **Aggregate**Specifies properties of the aggregate fields.

  + **Vertical Layout**  
     If selected, the aggregate fields will be arranged vertically.
    - **Number of Rows**  
       Specifies the number of rows to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a row so that the aggregate fields are positioned in one column vertically. 0 and a number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of rows (3 for example) less than the number of aggregate fields (6 for example), there will be 3 rows to hold the 6 fields with each row containing 2 fields.
  + **Horizontal Layout**  
     If selected, the aggregate fields will be arranged horizontally. When you have multiple aggregate fields in the crosstab, using horizontal layout can make the report more readable.
    - **Number of Columns**  
       Specifies the number of columns to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a column so that the aggregate fields are positioned in one row horizontally. 0 and a number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of columns (3 for example) less than the number of aggregate fields (6 for example), there will be 3 columns to hold the 6 fields with each column containing 2 fields.
* **Suppress Row Grand Totals**  
   Specifies whether or not to show the grand total row in the crosstab.
* **Suppress Column Grand Totals**  
   Specifies whether or not to show the grand total column in the crosstab.
* **Suppress Row Subtotals**  
   Specifies whether or not to show the subtotals of the row fields in the crosstab. You can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4412139533719/btn_chsr4.gif) to customize which subtotals of the row fields will be suppressed and which will be shown in the [Suppress Row Subtotals](https://devnet.logianalytics.com/hc/en-us/articles/1500009717041-Suppress-Row-Subtotals) dialog.
* **Suppress Column Subtotals**  
   Specifies whether or not to show the subtotals of the column fields in the crosstab. You can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4412139533719/btn_chsr4.gif) to customize which subtotals of the column fields will be suppressed and which will be shown in the [Suppress Column Subtotals](https://devnet.logianalytics.com/hc/en-us/articles/1500009690762-Suppress-Column-Subtotals) dialog.
* **Column Totals On**Specifies the position of subtotal and grand total columns on the left or right of the detail aggregations.
* **Row Totals On**  
   Specifies the position of subtotal and grand total rows on the top or bottom of the detail aggregations.

### For Chart Component

![Web Report Wizard - Bind Data screen - Common Chart](https://devnet.logianalytics.com/hc/article_attachments/4412112575383/wbrptwzd_bnddt_chart.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4412131381399/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the chart title.

**Data Source**

Specifies the business view in the current catalog on which the chart will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009716841-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Resources**

Displays the group, detail, and aggregation objects in the selected business view. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-) to use in the chart.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
   Sorts the objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)

Adds the selected object to the chart.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)

Removes the selected object.

The other options for defining the chart component varies according to different chart types: [common chart types](#Common), [organization chart](#Org), [heat map](#Map).

#### For Common Chart Types

**Value box**

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects.

* **Primary Axis**  
   Adds a chart type to the primary axis.
* **Secondary Axis**  
   Adds a chart type to the secondary axis. Active only when the option Secondary Axis is checked. Not available to gauge chart.
* **X-Axis**  
   Lists the value you want to show on the X axis of the bubble chart.
* **Y-Axis**  
   Lists the value you want to show on the Y axis of the bubble chart.
* **Size**   
   Lists the value you want to show as the bubble size.

![Add Combo Chart](https://devnet.logianalytics.com/hc/article_attachments/4412112505111/btn_wbrpt_adcmbtyp.gif)

Adds a combo chart to the Primary Axis or Secondary Axis. Not available to gauge chart.

![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)

Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009689762-Edit-Additional-Value) dialog to edit the selected additional value.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)

Moves the selected object one level up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)

Moves the selected object one level down.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4412131380631/btn_add1.gif)

Adds a new pair of Y Axis and Radius for the bubble chart.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)

Removes the selected resource.

**Secondary Axis**

Specifies whether to show the secondary axis in the chart. Not available to gauge chart.

**Category box**

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) that will be displayed on the category axis of the chart.

For a real time chart, if no object is specified on the category axis, Use System Refresh Time will be automatically displayed in the category box, namely, the time at which the chart refreshes itself will be used as the category value.

**Series box**

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) that will be displayed on the series axis of the chart. Not available to real time chart.

![Top N button](https://devnet.logianalytics.com/hc/article_attachments/4412139502103/btn_wbrpt_topn.gif)

Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009689722-Category-Options) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009716881-Series-Options) dialog to define the sort order of the category or series values and specify the number of the category or series values that will be displayed in the chart.

**Motion Bar for Playable Chart**

Lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) you want to use as the motion field. A motion field can only be of Integer, Date or Time data type. Available to single bar, bench and bubble chart types only.

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

Specifies to run the chart in real time mode, which means it will be updated automatically using real time data. Available to single bar, bench, line, and area chart types only.

* **Use System Time for Category**  
   Specifies to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
   Specifies the time interval at which the chart will get data and refresh itself automatically.
* **Show Most Recent N Points**  
   Specifies the number of records that will be kept for the real time data on the chart.
* **Incremental Fetch**  
   Opens the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009717181-Unique-Key) dialog to configure a unique key for the real time chart.

#### For Organization Chart

Specifies the data displayed in the chart.

**Value box**

* **Primary Axis**  
   Select Org from the chart type drop-down menu.
* **Node**  
   Adds a field from the Resources box which identifies the entity by selecting both the field and Node and then selecting ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif).
* **Parent**  
   Adds a field from the Resources box which shows the "reporting to" relationship among the entity members, that is, which child node field member reports to or belongs to which child node field member, by selecting both the field and Parent and then selecting ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif).
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected child node or parent field.

**Properties**

The Properties box presents a node model of the org chart. Data fields, labels and images can be inserted into the node as the information about the entity in the org chart, using ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif). By default all added objects are placed at the left top of the node, you need to adjust their positions and sizes in the node. You can also resize the node if required.

To remove an object from the node, select it and then select ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif).

#### For Heat Map

**Chart type drop-down list**

Displays Heat Map as the selected chart type.

**Area**

Lists the fields used to group the data to different areas. There should be at least one group. When there are multiple groups, their levels are defined by their positions from top down. The group at the top is of the highest level and the bottom the lowest.

* **Color by**  
   Specifies whether to color by a group. 0-n groups can be used as the color-by fields.
* **Label by**  
   Specifies whether to show the group name in the innermost rectangle.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)  
   Moves the selected group field one level up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)  
   Moves the selected group field one level down.
* ![Top N button](https://devnet.logianalytics.com/hc/article_attachments/4412139502103/btn_wbrpt_topn.gif)  
   Opens the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009690322-Group-Options) dialog to define the sort order of the group values and specify the number of the group values that will be displayed in the chart.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected group field.

**Property**

Lists the summary fields used as size-by/color-by or displayed in the innermost rectangle.

* **Size by**  
   Specifies to size by one summary or none.
* **Color by**  
   Specifies to color by one summary or none.
* **Label by**  
   Specifies whether to show a summary in the innermost rectangle.

### For Banded Object Component

![Web Report Wizard - Bind Data screen - Banded](https://devnet.logianalytics.com/hc/article_attachments/4412112575639/wbrptwzd_bnddt_banded.gif)

**Banded Title**

Specifies the title of the banded object. The title is a special label bound with the banded object. Though it can be positioned freely in a report, once you remove the banded object from the report, the title will be removed too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4412131381399/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the banded object title.

**Data Source**

Specifies the business view in the current catalog on which the banded object will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009716841-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Details tab**

Specifies the detail fields that you want to display in the banded object.

* **Resources**   
   Displays the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) and detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4412139491991/btn_bvdtl.gif) in the selected business view. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-#DynamicFormula) to use in the banded object.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
   Sorts the objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).
* ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)  
   Adds the selected object to display in the banded object.
* ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)  
   Removes the selected object.
* **Field**  
   Lists all the objects that have been added to the banded object as detail fields.
* **Label**  
   Specifies the text for the labels of the added objects, which by default are the display names of the objects. You can select in the text boxes to edit the label text, or check the Auto Map Field Name checkboxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)  
   Moves the selected object one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)  
   Moves the selected object one step down.
* **Sort Fields By**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009715841-Custom-Sort) dialog to specify how to sort data in the banded object.

**Group tab**

Specifies the fields to group the data in the banded object.

* **Resources**  
   Displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) you can use to group data in the banded object. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-#DynamicFormula) to use in the banded object.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
   Sorts the objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).
* ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)  
   Adds the selected object as a group-by field.
* ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)  
   Removes the selected object.
* **Field**  
   Lists all the objects that have been added to the banded object as group-by fields.
* **Sort**  
   Specifies the sort order for groups at the specific group level.
  + **Ascend**  
     Groups will be sorted in an ascending order (A, B, C).
  + **Descend**  
     Groups will be sorted in a descending order (C, B, A).
  + **No Sort**  
     Groups will be sorted in the original order in database.
  + **Custom Sort**  
     Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009715841-Custom-Sort) dialog to set how groups will be sorted.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)  
   Moves the selected group one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)  
   Moves the selected group one step down.

**Summary tab**

Specifies the fields on which to create summaries in the banded object.

* **Resources**  
   Displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4412131382167/btn_bvaggrgtn.gif) you can use to create summaries in the banded object. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-) to use in the banded object.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131385239/btn_wbrpt_edit.gif)  
   Edits the selected dynamic resource.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected dynamic resource.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)  
   Sorts the objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).
* ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)  
   Adds the selected object as the summary field.
* ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)  
   Removes the selected object.
* **Field**  
   Lists the groups that have been added in the banded object and the objects added to summarize data in each group.
* **Row**  
   Specifies to put the summary field in the header or footer row. If the summary is calculated on a group-by field, it will be put in the group header or footer of the corresponding group; if the summary is calculated on the banded object, it will be put in the banded header or footer.
* **Column**  
   Works together with the Row option to specify the location where a summary will be placed.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)  
   Moves the selected object one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)  
   Moves the selected object one step down.

## Style

Specifies the style of the report.

![Web Report Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4412139511703/wbrptwzd_style.gif)

**Styles**

Lists all the available styles for you to select from. No style will be applied when you select None.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009690922-User-Defined-Function-Editor)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717221-Windows-Media-Properties)
