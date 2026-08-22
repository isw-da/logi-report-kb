---
title: "Manipulating Data Components"
id: 1500009649422
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649422-Manipulating-Data-Components
updated_at: 2021-07-24T20:53:55Z
---

# Manipulating Data Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674041-Applying-Web-Controls)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649302-Drilling-Through-the-Report-Data)

# Manipulating Data Components

You can manipulate data components, which refer to crosstabs, tables, banded objects, charts and geographic maps, in Page Report Studio. However for the data components created in Logi JReport Designer, to perform some of the manipulation actions requires that the data fields used by the components can be converted to corresponding view elements. The actions include:

* Converting between charts and crosstabs
* Modifying the chart definition
* Adding and converting columns, and aggregating on detail columns in tables

In addition, a [Logi JReport Live license for Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648262-Logi-JReport-Licenses#ServerLive) is required in order to use the features involving business view or changes of report template. If you do not have the license, contact your Jinfonet Software account manager to obtain it.

The following shows manipulating on specific data components in detail. Most of the manipulations require selecting the component first. To select a component, select anywhere in the component, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, select the icon.

Below is a list of the sections covered in this topic:

* [Manipulating a Crosstab](#Crosstab)
* [Manipulating a Table](#Table)
* [Manipulating a Chart](#Chart)
* [Manipulating a Banded Object](#Banded)
* [Manipulating Geographic Map Group Markers](#Map)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Manipulating a Crosstab

* **Changing the group index in a crosstab**  
   The group index in a crosstab can be modified, namely, you can move a group to a higher or lower level. This operation can be performed on crosstabs containing two or more groups. To do this, you can simply drag a group object (row/column header) to the required destination till a blue line appears. You can also drag a column header to a row level and vice versa.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404920452887/pgrpt_edit_manplt_crstb.gif)
* **Rotating a crosstab**  
   Columns and rows in a crosstab can be exchanged. This operation is called rotating a crosstab.

  To rotate a crosstab, first select it, and then do one of the following:

  + Select **Menu** > **Report** > **Rotate Crosstab**.
  + Select the **Rotate** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920364567/btn_rotate.gif) on the toolbar.
  + Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the crosstab and select **Rotate** from the shortcut menu.
* **Adjusting the width of crosstab fields according to the contents**  
   When the contents in the field of a crosstab need more space to completely display, you can adjust the width of the field according to its contents. To achieve it, first select the field, then right-click on it and select **Autofit**  from the shortcut menu.
* **Adding row/column headers by dragging**  
   To drag a group field into a crosstab to become a column header, drag it from the Resource View panel and then move the mouse pointer to a border of a column header until a highlighted horizontal line appears, then release the mouse.

  ![Add Column Header image](https://devnet.logianalytics.com/hc/article_attachments/4404926674711/pgrpt_edit_manplt_crstb2.gif)

  + When the crosstab has no column/row/summary labels, the new column header will be directly placed where the highlighted line lies.
  + When you have specified any labels to label the columns/rows/summaries in the crosstab using wizard, the [Insert Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009645262-Insert-Column) dialog appears. You can specify a label to label the new column header if necessary. Select **OK** and the new column header will be placed where the highlighted line lies.

    ![Insert Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404920453783/insrtclmn.gif)

  To drag a group field into a crosstab to become a row header, drag it from the Resource View panel and then move the mouse pointer to a border of the row header until a highlighted vertical line appears, then release the mouse.

  ![Add Row Header image](https://devnet.logianalytics.com/hc/article_attachments/4404920454295/pgrpt_edit_manplt_crstb3.gif)

  + When the crosstab has no column/row/summary labels, the new row header will be directly placed where the highlighted line lies.
  + When you have specified any labels to label the columns/rows/summaries in the crosstab using wizard, the [Insert Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009669801-Insert-Row) dialog appears. You can specify a label to label the new row header if necessary. Select **OK** and the new column header will be placed where the highlighted line lies.

    ![Insert Row dialog](https://devnet.logianalytics.com/hc/article_attachments/4404920454551/insrtrw.gif)
* **Inserting aggregate fields by dragging**  
  You can drag and drop fields (detail fields, aggregation fields, and dynamic formulas/aggregations) from the Resource View panel to a crosstab to add them as aggregate fields to summarize data in the crosstab. To do this, in the Resource View panel, drag the required field and move the mouse pointer above or under the desired subtotal or grand total cell until a highlighted horizontal line appears, then release the mouse.

  ![Insert Aggregation image](https://devnet.logianalytics.com/hc/article_attachments/4404926675991/pgrpt_edit_manplt_crstb4.gif)

  + If the selected field has predefined aggregate function,
    - When the crosstab has no column/row/summary labels, the field is inserted into the specified position directly.
    - When you have specified any labels to label the columns/rows/summaries in the crosstab using wizard, the [Insert Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009645242-Insert-Aggregation) dialog appears. You can specify a label to label the newly created summaries if necessary. Select **OK** and the field is inserted to the specified position.

      ![Insert Aggregation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404926676247/pgrpt_edit_manplt_crstb5.gif)
  + If the selected field has no predefined aggregate function, the Insert Aggregation dialog appears. From the Aggregate Function drop-down list, select the function to summarize the field, then input a label to label the newly created summaries if necessary. Select **OK** and the field is inserted to the specified position. However, whether the label you specify would be generated depends on if you have added any labels to label the columns/rows/summaries in the crosstab using wizard. If no label is defined in the wizard, the label you add in the Insert Aggregation dialog will be ignored. After the field is inserted in the crosstab, you can switch the aggregate function it uses at anytime. To do this, right-click the field and select **Switch Function** from the shortcut menu, then choose a new function from the submenu.
* **Converting a crosstab into a chart**
  1. Select anywhere in the crosstab, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, select the icon to select the crosstab, then do any of following:
     + Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) and select **To Chart** from the shortcut menu.
     + Select **Menu** > **Report** > **To Chart**.

     The [To Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009670121-To-Chart) dialog appears.
  2. In the Chart Type tab, specify a suitable type for the chart. With a certain type specified, you can further define the chart as a combo chart by selecting **<Add Combo Type>** in the Chart Type Groups box.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920455191/tochart_type.gif)
  3. In the Display tab, the Resources box lists all the view elements used in the selected crosstab including group and aggregation objects. The chart can only be defined based on the view elements listed. Add a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) from the Resources box to the Category box, and so to the Series box, and aggregation objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) to the Show Values box respectively.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920455703/tochart_dsply.gif)
  4. In the Style tab, set the style for the chart as required.

     If the crosstab is in a banded object, by default, the chart converted from the crosstab will take on the style of the banded object. If you want to apply another style to the chart, uncheck the **Inherit Style** option and choose the desired style in the Style box. However, when there is only one style available, this style will be applied to the chart by default and the Style tab will be hidden from the dialog.
  5. Select the **OK** button to finish the conversion.
* **Expanding/Collapsing a crosstab**  
   For a crosstab created in Logi JReport Designer, if it has more than one row/column group level, you can specify whether or not to enable the crosstab to be expanded in Page Report Studio, and set the default expanding/collapsing state of groups in outer levels. For details, see "Expanding/Collapsing a Crosstab" in the *Logi JReport Designer User's Guide*.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Manipulating a Table

* **Adjusting order of columns in a table**  
   The order of columns in a table can be easily adjusted. To do this, drag a column header to the left or right boundary of another column header, when a blue line appears along the column boundary, release the mouse button, and you will see the order change.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404920457111/pgrpt_edit_manplt_tb1.gif)

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926677655/pgrpt_edit_manplt_tb2.gif)

  The above description is for a vertical table. With regard to a horizontal table, you can do the same actions on its row headers.
* **Adjusting grouping order in a table**  
   A table may contain several group levels. The order of the group levels can also be adjusted. To do this, drag a group field value to the required position until a blue line appears.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926677911/pgrpt_edit_manplt_tb3.gif)
* **Hiding/Deleting table columns**  
   A table column (for a horizontal table, the "column" corresponds to a field row) can be hidden or removed. To do this, select the cell of the column in the table header and right-click, then select **Hide Column** or **Remove Column** from the shortcut menu, and the column will be hidden or removed from the table.
* **Showing table columns**  
   You can specify which columns will be shown in a table. To do this, right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the table, then on the shortcut menu, check the names of the columns you want to show from the Show Column submenu.
* **Adjusting the width of table columns according to contents**  
   When the contents in cells of a table column need more space to completely display, you can adjust the width of the table column according to the contents. To do this, right-click the cell of the column in the table header, then select **Autofit** from the shortcut menu.
* **Changing group direction**  
   You can make the group headers that are placed horizontally in a table to be displayed vertically. To do this, right-click the group header row and select **Vertical to Detail** from the shortcut menu. In addition, if the first column of a table is group column, you can specify to place the group column horizontally in a table. To do this, right-click the cell of the group column in the table header, and select **Horizontal to Detail** from the shortcut menu.
* **Rotating a table**  
   You can rotate a table to switch its appearance between the horizontal and vertical layout modes by doing one of the following:
  + Select **Menu**> **Report** > **Rotate Table**.
  + Select the **Rotate** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920364567/btn_rotate.gif) on the toolbar.
  + Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the table and select **Rotate** from the shortcut menu.
* **Inserting table columns**  
   You can insert a new column in a table and it could be a common column, detail column, summary column, or group column.
  + **To insert a common column into a table:**
    1. Right-select any cell in the table header, or right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the table.
    2. On the shortcut menu, select **Insert** > **Common** **Column**.
  + **To insert a detail or summary column into a table:**
    1. Right-select any cell in the table header, or right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the table, then select **Insert** > **Detail Column**/**Summary Column**  from the shortcut menu.
    2. In the corresponding insert column dialog, specify the resource you want to use for the new column, then select **OK**.

       ![](https://devnet.logianalytics.com/hc/article_attachments/4404926678167/insrtsumclmn.gif)
  + **To insert a group column into a table:**
    1. Right-select any cell in the table header, or right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the table, then select **Insert** > **Group Column** from the shortcut menu. The [Insert Group Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009645322-Insert-Group-Column) dialog appears.

       ![](https://devnet.logianalytics.com/hc/article_attachments/4404920461719/insrtgrpclmn.gif)
    2. Select the group object you want to use for the new group column from the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) to add it as the group by field, then specify the sorting direction of the group in the Sort column.
    3. Specify the positions of the group by fields: Group Above, Group Left Above, or Group Left.
    4. Repeat the above steps to add more groups if required.
    5. Select **OK** to insert the columns.

       The next time when you open the Insert Group Column dialog to add more group columns, all the added group by fields will be listed in the dialog. You can choose to remove or edit them if required.

  **Note:** If you right-click any cell in the table header and use its shortcut menu to insert a common, detail or summary column, the Insert Column dialog will appear for you to specify the position of the column to be inserted, which can be before or after the column in which the cell you select on is, however, if you use the table shortcut menu to insert the column,

  + If it is a common column, the column will be inserted as the last column in the table.
  + If it is a detail/summary column, the column will be inserted after the last detail/summary column, or as the last column in the table when there is no detail/summary column.
* **Converting table columns**  
   You can convert a group column into a detail column, and vice versa.
  + To convert a group column into a detail column, select the cell of the group column in the table header, right-click and select **Convert to Detail**  from the shortcut menu, then the conversion is done.
  + **To convert a detail column into a group column:**
    1. Select the cell of the detail column you want to convert in the table header, right-click and select **Convert to Group** from the shortcut menu.
    2. In the Select Group Position dialog, specify the position for the newly converted group by field.

       ![](https://devnet.logianalytics.com/hc/article_attachments/4404920462359/slctgrppstn.gif)

       - **Group Above**  
          Specifies to place the group by field in its own row above the detail columns.
       - **Group Left Above**  
          Specifies to place the group by field in its own row and column above and left of the detail columns.
       - **Group Left**  
          Specifies to place the group by field in its own column left of the detail columns.
    3. Select **OK** to save the changes.
* **Aggregating on a detail column**  
   You can summarize the data in a detail column if required. To do this:
  1. Select the cell of the detail column in the table header, right-click it and select **Aggregate On** from the shortcut menu. The Aggregate On dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920462615/agrgton.gif)
  2. From the Function drop-down list, specify a [function](https://devnet.logianalytics.com/hc/en-us/articles/1500009648102-Math-) to summarize the data.
  3. When done, select **OK**.
     + If the table has groups, you will find data in each group level and the whole table are summarized respectively in the column.
     + If the table has no groups, the summary will be based on the whole table.

  When you finish summarizing a detail column, you will find a [dynamic aggregation object](https://devnet.logianalytics.com/hc/en-us/articles/1500009649362-Using-Dynamic-Resources#Agg) is created at the same time which is given a default name Function\_DetailFieldName in the Dynamic Resource > Aggregations list in the Resources View panel and you can use it again in the current report if required.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Manipulating a Chart

* **Changing the chart type**
  + Right-select the chart and on the shortcut menu, select the required type from the Chart Type submenu, which lists all the chart types and subtypes (the current one and the inapplicable subtypes are grayed out).
  + Select the chart, select the **Chat Type** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926666775/btn_pgrpt_chttype.gif) on the toolbar, and then select a suitable subtype from the drop-down menu.
* **Modifying the definition of a chart**  
   You can modify the definition of a chart, including the chart type, data display, and style. To do this:
  1. Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the chart or any part of the chart other than the legend and label to show a shortcut menu, and then select **Format Chart** from the shortcut menu to display the [Chart Definition](https://devnet.logianalytics.com/hc/en-us/articles/1500009669481-Chart-Definition) dialog.
  2. In the Chart Type tab of the Chart Definition dialog, specify the type for the chart.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404926679191/chtdef_type.gif)
  3. In the Display tab, change the group and aggregation object used by the chart.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920462871/chtdef_dsply.gif)
  4. In the Style tab, modify the style for the chart as required. When there is only one style available, this style will be applied to the chart by default and the Style tab will be hidden from the dialog.
  5. Upon finishing, select **OK** to apply the modifications.

  For details about how to define a chart, see [Creating a Chart Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009673901-Creating-Page-Reports#Chart).
* **Converting a chart into a crosstab**
  1. Select anywhere in the chart, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, select the icon to select the chart, then do any of following:
     + Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) or any part of the chart except for the legend and label, then select **To Crosstab** on the shortcut menu.
     + Select **Menu** > **Report** > **To Crosstab**.

     The [To Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009670141-To-Crosstab) dialog appears.
  2. In the Display tab,
     select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) to add it as a group field to the Columns or Rows box; select an aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) to add it as an aggregate field to the Summaries box. Repeat these to add more aggregate fields.
     In the Display Name column, you can edit the display names of the added group and aggregate fields. By default the display names are blank and no labels will be created for the added fields to name the columns/rows/summaries in the generated crosstab. You can make Logi JReport automatically provide the display names to the added fields. To enable the feature, go to Logi JReport Console/Administration page > Profile > Customize Profile > Common tab, select **Add Labels for Crosstab Rows and Columns** and/or **Add Labels for Crosstab Summaries** as required. In the Sort column, specify a sort manner on a group field.

     If you want to remove any group/aggregate field, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif). To adjust the order of the group/aggregate fields, select a group/aggregate field and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif).

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404926679447/tocrstb_dsply.gif)
  3. In the Style tab, apply a style to the crosstab as required.

     If the chart is in a table or banded object, by default, the crosstab converted from the chart will take on the style of the table or banded object. If you want to apply another style to the crosstab, uncheck the **Inherit Style** option and choose the desired style in the Style box. However, when there is only one style available, this style will be applied to the crosstab by default and the Style tab will be hidden from the dialog.
  4. Select **OK** to finish the conversion.

  **Note:** If the chart is created on a business view in Page Report Studio, it can contain additional values which are supported only in chart. Therefore when you convert a chart with additional values into crosstab, the additional values are not converted together with the chart.
* **Formatting chart elements**   
   The elements (platform, paper, legend, axes and labels) in a chart can be formatted to suit your requirement.

+ To format the platform/paper/legend of a chart, right-click on the chart and select **Format Platform**/**Format Paper**/**Format Legend** from the shortcut menu. In the displayed dialog, specify the settings as required. For details about the format options, refer to [Format Platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009669741-Format-Platform) dialog, [Format Paper](https://devnet.logianalytics.com/hc/en-us/articles/1500009645142-Format-Paper) dialog and [Format Legend](https://devnet.logianalytics.com/hc/en-us/articles/1500009669721-Format-Legend) dialog.
+ To format an axis, right-click on the chart and select the axis from the Format Axis submenu. In the displayed dialog, specify the axis settings as required. For details about the format options, refer to [Format Category(X) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009669681-Format-Category-X-Axis) dialog, [Format Value(Y) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009645162-Format-Value-Y-Axis) dialog and [Format Value(Y2) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009669761-Format-Value-Y2-Axis) dialog.
+ To format a label, right-click the label and select **Format Label** from the shortcut menu. In the [Format Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009669701-Format-Label) dialog, set the properties according to your requirement.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Manipulating a Banded Object

* **Hiding/Showing a panel in a banded object**  
   A panel in a banded object can be hidden or shown. To do this, right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the banded object, then on the shortcut menu, select the item which indicates the panel name from the Show submenu. For a panel which is shown, the item is with a check mark, and vice versa. This operation is also applicable for hiding/showing a row in a table.
* **Hiding/Showing DBFields and labels in a banded object**  
   The DBFields and their corresponding labels in a banded object can be hidden or shown. To do this, right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the banded object, then on the shortcut menu, select the fields and labels you want to show from the Show Field submenu. For a field or label that is shown, it will be marked with a check mark, and vise verse.
* **Resetting data in a banded object**  
   After sorting and filtering data in a banded object, you can right-click an object in the banded object and select the **Reset** item from the shortcut menu to reproduce the data of the banded object using the data cached in the data buffer. This will clear all sort and filter conditions from the banded object.
* **Expanding/Collapsing a group panel in a banded object**  
   You can expand and collapse the group panels in a banded object created in Logi JReport Designer if it is enabled with the feature. For details, see "Managing the Data of a Banded Object" in the *Logi JReport Designer User's Guide*.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Manipulating Geographic Map Group Markers

* **Going up/down on geographic map group markers**
  + For the group level that is higher than some other group levels in a geographic map component, point to its group marker, right-click it and select **Go Down** from the shortcut menu to jump one group level down.
  + For the group level that is lower than some other group levels in a geographic map component, point to its group marker, right-click it and select **Go Up** from the shortcut menu to jump one group level up.
* **Showing/Hiding geographic map group markers**  
   By default, all visible group markers are shown. To hide them, right-click the geographic map (not the group markers) and select Hide Markers from the shortcut menu. If you want to show them again, right-click the geographic map and select Show Markers from the shortcut menu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674041-Applying-Web-Controls)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649302-Drilling-Through-the-Report-Data)
