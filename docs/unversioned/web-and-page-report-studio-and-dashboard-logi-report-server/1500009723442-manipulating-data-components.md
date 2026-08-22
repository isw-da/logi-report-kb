---
title: "Manipulating Data Components"
id: 1500009723442
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009723442-Manipulating-Data-Components
updated_at: 2021-07-25T07:18:53Z
---

# Manipulating Data Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750541-Applying-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750401-Drilling-Through-the-Report-Data)

# Manipulating Data Components

You can manipulate data components, which refer to crosstabs, tables, banded objects, charts and geographic maps, in Page Report Studio. However for the data components created in Logi Report Designer, to perform some of the manipulation actions requires that the data fields used by the components can be converted to corresponding view elements. The actions include:

* Converting between charts and crosstabs
* Modifying the chart definition
* Adding and converting columns, and aggregating on detail columns in tables
* Adding view elements to data components by dragging them from the Resource View panel

  **Tip:** To display the Resource View panel, select **Menu** > **View** > **Resource View** or the **Resource View** button ![Resource View button](https://devnet.logianalytics.com/hc/article_attachments/4404936772247/btn_pgrpt_resvw.gif) on the toolbar. You can use the search bar at the top of the panel to search for any desired resource in a fast and convenient way.

In addition, a [Logi Report Live license for Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009749561-Logi-Report-licenses#ServerLive) is required in order to use the features involving business view or changes of report template. If you do not have the license, contact your Logi Analytics account manager to obtain it.

The following shows manipulating on specific data components in detail. Most of the manipulations require selecting the component first. To select a component, select anywhere in the component, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) appears at its upper left corner, select the icon.

* [Manipulating a Chart](#Chart)
* [Manipulating a Crosstab](#Crosstab)
* [Manipulating a Table](#Table)
* [Manipulating a Banded Object](#Banded)
* [Manipulating Geographic Map Group Markers](#Map)

## Manipulating a Chart

For heat maps, Page Report Studio only supports the Show Tips feature on them but does not support other chart actions.

* **Changing the chart type**
  + Right-click on the chart and on the shortcut menu, select the required type from the Chart Type submenu, which lists all the chart types and subtypes (the current one and the inapplicable subtypes are grayed out).

    ![Change Chart Type](https://devnet.logianalytics.com/hc/article_attachments/4404942490135/pgrpt_edit_manplt_cht.gif)
  + Select the chart, select the **Chart Type** button ![Chart Type button](https://devnet.logianalytics.com/hc/article_attachments/4404936773015/btn_pgrpt_chttype.gif) on the toolbar, and then select a suitable subtype from the drop-down menu.
* **Modifying the definition of a chart**  
   You can modify the definition of a chart, including the chart type, data display, and style. To do this:
  1. Right-click on the chart and select **Chart Wizard** from the shortcut menu to display the [Chart Definition](https://devnet.logianalytics.com/hc/en-us/articles/1500009719162-Chart-Definition) dialog box.
  2. In the Chart Type tab of the Chart Definition dialog box, specify the type for the chart.

     ![Chart Definition dialog - Chart Type tab](https://devnet.logianalytics.com/hc/article_attachments/4404942490391/chtdef_type.gif)
  3. In the Display tab, change the group and aggregation object used by the chart.

     ![Chart Definition dialog - Display tab](https://devnet.logianalytics.com/hc/article_attachments/4404936779159/chtdef_dsply.gif)
  4. In the Style tab, modify the style for the chart as required. When there is only one style available, this style will be applied to the chart by default and the Style tab will be hidden from the dialog box.
  5. Upon finishing, select **OK** to apply the modifications.

  For details about how to define a chart, see [Creating a Chart Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750341-Creating-Page-Reports#Chart).
* **Converting a chart into a crosstab**
  1. Select anywhere in the chart to select the chart, then do any of following:
     + Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) or any part of the chart except for the legend and label, then select **To Crosstab** on the shortcut menu.
     + Select **Menu** > **Report** > **To Crosstab**.

     Report Server displays the [To Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009746621-To-Crosstab) dialog box.
  2. In the Display tab, select a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) in the Resources box and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif) to add it as a group field to the Columns or Rows box; add the aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) to the Summaries box to summarize data in the crosstab. For each column/row/summary field, you can select in the Display Name text box and type a name to label the corresponding column header/row header/summary, or select the **Auto Map Field Name** check box beside the text box if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field (when the text box is blank and the check box is not selected, no label will be created). In the Sort column, specify a sort manner on a group object. To adjust the display order of the aggregation objects, select one in the Summaries box and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif).

     ![To Crosstab dialog - Display tab](https://devnet.logianalytics.com/hc/article_attachments/4404936779415/tocrstb_dsply.gif)
  3. In the Style tab, apply a style to the crosstab as required.

     If the chart is in a table or banded object, by default, the crosstab converted from the chart will take on the style of the table or banded object. If you want to apply another style to the crosstab, clear the **Inherit Style** option and choose the desired style in the Style box. However, when there is only one style available, this style will be applied to the crosstab by default and the Style tab will be hidden from the dialog box.
  4. Select **OK** to finish the conversion.

  **Note:** If the chart is created on a business view in Page Report Studio, it can contain additional values which are supported only in chart. Therefore when you convert a chart with additional values into crosstab, the additional values are not converted together with the chart.
* **Formatting chart elements**   
   The elements in a chart can be formatted to suit your requirement.

+ To format the platform/paper/legend of a chart, right-click on the chart and select **Format Platform**/**Format Paper**/**Format Legend** from the shortcut menu. In the [Format Platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009745741-Format-Platform) dialog box/[Format Paper](https://devnet.logianalytics.com/hc/en-us/articles/1500009745701-Format-Paper) dialog box/[Format Legend](https://devnet.logianalytics.com/hc/en-us/articles/1500009745661-Format-Legend) dialog box, specify the settings as required.
+ To format an axis, right-click on the chart and select the axis from the Format Axis submenu. In the [Format Category (X) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009719382-Format-Category-X-Axis) dialog box, [Format Value (Y) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009745881-Format-Value-Y-Axis) dialog box or [Format Value (Y2) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009745901-Format-Value-Y2-Axis) dialog box, specify the axis settings.
+ To format the graph such as the areas, bars or lines of a chart, right-click on the chart and select **Format Graph** from the shortcut menu (for a combo chart, the option name is Format Graph (Y) and Format Graph (Y2)). In the [Format Area](https://devnet.logianalytics.com/hc/en-us/articles/1500009745521-Format-Area) dialog box, [Format Bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009745541-Format-Bar) dialog box, [Format Bench](https://devnet.logianalytics.com/hc/en-us/articles/1500009745561-Format-Bench) dialog box, [Format Donut](https://devnet.logianalytics.com/hc/en-us/articles/1500009745601-Format-Donut) dialog box, [Format Line](https://devnet.logianalytics.com/hc/en-us/articles/1500009745681-Format-Line) dialog box, [Format Pie](https://devnet.logianalytics.com/hc/en-us/articles/1500009745721-Format-Pie) dialog box, [Format Radar](https://devnet.logianalytics.com/hc/en-us/articles/1500009745781-Format-Radar) dialog box, [Format Scatter](https://devnet.logianalytics.com/hc/en-us/articles/1500009745821-Format-Scatter) dialog box, [Format Stock](https://devnet.logianalytics.com/hc/en-us/articles/1500009719482-Format-Stock) dialog box, [Format Surface](https://devnet.logianalytics.com/hc/en-us/articles/1500009745841-Format-Surface) dialog box, [Format Activity Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009745501-Format-Activity-Gauge) dialog box, [Format Bar Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009719362-Format-Bar-Gauge) dialog box, [Format Bubble Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009745581-Format-Bubble-Gauge) dialog box, [Format Dial Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009719402-Format-Dial-Gauge) dialog box or [Format Solid Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009719462-Format-Solid-Gauge) dialog box, set the graph settings as required.
+ For a pie chart, if you specify to display KPI values on it, you can format the KPI value labels, for example, edit the size and border of the labels, change the label font size, font color, and so on. To do this, right-click on the chart and select **Format KPI Label**  from the shortcut menu, then in the [Format KPI Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009745641-Format-KPI-Label) dialog box, set the properties according to your requirements.

  When an activity, bar, dial or solid gauge chart displays the gauge labels, pointer labels and target labels, you can also format the labels accordingly. To do this, right-click on the chart and select **Format Gauge Label**/**Format Pointer Label**/**Format Target Label** from the shortcut menu, then in the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009745621-Format-Gauge-Label) dialog box/[Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009745761-Format-Pointer-Label) dialog box/[Format Target Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009745861-Format-Target-Label) dialog box, specify the properties.

  A chart created in Logi Report Designer can have chart labels, and these labels can be further formatted in Page Report Studio. To format a chart label, right-click the label and select **Format Label** from the shortcut menu. In the [Format Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009719422-Format-Label) dialog box, specify the properties.

## Manipulating a Crosstab

* **Rotating a crosstab**  
   Columns and rows in a crosstab can be exchanged. This operation is called rotating a crosstab.

  To rotate a crosstab, first select it, and then do one of the following:

  + Select **Menu** > **Report** > **Rotate Crosstab**.
  + Select the **Rotate** button ![Rotate button](https://devnet.logianalytics.com/hc/article_attachments/4404942448663/btn_rotate.gif) on the toolbar.
  + Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the crosstab and select **Rotate Crosstab** from the shortcut menu.

    ![Rotate Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404942490647/pgrpt_edit_manplt_crstb1.gif)
* **Converting a crosstab into a chart**
  1. Select the crosstab and do any of following:
     + Select **Menu** > **Report** > **To Chart**.
     + Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) and select **To Chart** from the shortcut menu.

     Report Server displays the [To Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009746601-To-Chart) dialog box.
  2. In the Chart Type tab, specify a suitable type for the chart. With a certain type specified, you can further define the chart as a combo chart by selecting **<Add Combo Type>** in the Chart Type Groups box.

     ![To Chart dialog - Chart Type tab](https://devnet.logianalytics.com/hc/article_attachments/4404936779671/tochart_type.gif)
  3. In the Display tab, the Resources box lists all the group and aggregation objects used in the selected crosstab. The chart can only be defined based on these objects. Add a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources box to the Category box, and so to the Series box, and aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) to the Show Values box respectively.

     ![To Chart dialog - Display tab](https://devnet.logianalytics.com/hc/article_attachments/4404942490903/tochart_dsply.gif)
  4. In the Style tab, set the style for the chart as required.

     If the crosstab is in a banded object, by default, the chart converted from the crosstab will take on the style of the banded object. If you want to apply another style to the chart, clear the **Inherit Style** option and choose the desired style in the Style box. However, when there is only one style available, this style will be applied to the chart by default and the Style tab will be hidden from the dialog box.
  5. Select the **OK** button to finish the conversion.
* **Auto fitting values in a crosstab**  
   When the values in the crosstab row/column headers or aggregation cells need more space to completely display, right-click any value in the row/column header or aggregation cell and select **Autofit**  from the shortcut menu. Page Report Studio then adjusts the width of the corresponding cells to match the contents in them.
* **Changing the group index in a crosstab**  
   The group index in a crosstab can be modified, namely you can move a group to a higher or lower level. To do this, drag a value in the row/column header to the required destination till a highlighted line appears, then release the mouse. You can also drag a column header to a row level and vice versa.

  ![Change Group Index](https://devnet.logianalytics.com/hc/article_attachments/4404936779927/pgrpt_edit_manplt_crstb6.gif)
* **Changing the aggregate function for an aggregation in a crosstab**  
   Right-click the aggregation that is based on a detail object and select **Switch Function** from the shortcut menu, then choose a new function from the submenu. If DistinctSum is selected as the function, you will be prompted with the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009746281-Select-Fields) dialog box to specify the detail objects according to whose unique values to calculate DistinctSum.
* **Removing column/row headers or aggregations from a crosstab**   
  Drag a value in the header or any aggregation value outside the report page. A message box is then prompted you whether or not to remove the field. Select **OK** to confirm the removal.

From the Resource View panel, you can drag view elements and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009750421-Using-Dynamic-Resources)  into a crosstab to add new column/row headers and aggregations in the crosstab. To do this, first select the crosstab to locate the business view it uses in the Resource View panel, then:

* **To add a column header**:  
   Drag a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) or dynamic formula used as Group ![Dynamic Formula Used as Group](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resource View panel and move the mouse pointer above or below an existing column header until a highlighted horizontal line appears, then release the mouse.

  ![Add Column Header](https://devnet.logianalytics.com/hc/article_attachments/4404936780183/pgrpt_edit_manplt_crstb2.gif)

  + When the crosstab has no column/row/aggregation labels, the new column header will be directly placed where the highlighted line lies.
  + When you have specified any labels to label the column headers/row headers/aggregations in the crosstab using wizard, Report Server displays the [Insert Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009745961-Insert-Column) dialog box. You can specify a label to label the new column header. Select **OK** and the new column header will be placed where the highlighted line lies.

    ![Insert Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936780439/insrtclmn.gif)
* **To add a row header:**  
   Drag a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) or dynamic formula used as Group ![Dynamic Formula Used as Group](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resource View panel and move the mouse pointer to the left or right of an existing row header until a highlighted vertical line appears, then release the mouse.

  ![Add Row Header](https://devnet.logianalytics.com/hc/article_attachments/4404936780695/pgrpt_edit_manplt_crstb3.gif)

  + When the crosstab has no column/row/aggregation labels, the new row header will be directly placed where the highlighted line lies.
  + When you have specified any labels to label the column headers/row headers/aggregations in the crosstab using wizard, Report Server displays the [Insert Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009746001-Insert-Row) dialog box. You can specify a label to label the new row header. Select **OK** and the new column header will be placed where the highlighted line lies.

    ![Insert Row dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936780951/insrtrw.gif)
* **To add an aggregation in the crosstab:**   
   Drag a detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif), aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif), dynamic formula used as Detail ![Dynamic Formula Used as Detail](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif), dynamic formula used as Aggregation ![Dynamic Formula Used as Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) or dynamic aggregation ![Dynamic Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) from the Resource View panel and move the mouse pointer above or under the desired aggregation, then release the mouse.
  The position determines whether detail aggregations, subtotals or grand totals will be created in the crosstab.

  ![Insert Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404942491287/pgrpt_edit_manplt_crstb4.gif)

  + If the selected object has predefined aggregate function,
    - When the crosstab has no column/row/aggregation labels, the object is inserted into the specified position directly.
    - When you have specified any labels to label the column headers/row headers/aggregations in the crosstab using wizard, Report Server displays the [Insert Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009745941-Insert-Aggregation) dialog box. By default the display name of the object will be used to label the new aggregation; to edit the label text for the new aggregation, select in the Label text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** option. Then select **OK** and the aggregation is inserted to the specified position.

      ![Insert Aggregation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942491543/pgrpt_edit_manplt_crstb5.gif)
  + If the selected object has no predefined aggregate function, Report Server displays the Insert Aggregation dialog box. From the Aggregate Function drop-down list, select the function for calculating the object. When DistinctSum is selected, you should select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) next to the Distinct On text box to specify one or more detail objects according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009746281-Select-Fields) dialog box. By default the display name of the object will be used to label the new aggregation; to edit the label text for the new aggregation, select in the Label text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** option. Select **OK** and the aggregation is inserted to the specified position. However, whether the label you specify would be displayed depends on if you have added any labels to label the column headers/row headers/aggregations in the crosstab using wizard and if there is appropriate position to place the label in the current crosstab. If no label is defined in the wizard, the label you add in the Insert Aggregation dialog box will be ignored.

## Manipulating a Table

* **Rotating a table**  
  You can rotate a table to switch its appearance between the horizontal and vertical layout modes by selecting it and doing one of the following:
  + Select **Menu** > **Report** > **Rotate Table**.
  + Select the **Rotate** button ![Rotate button](https://devnet.logianalytics.com/hc/article_attachments/4404942448663/btn_rotate.gif) on the toolbar.
  + Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the table and select **Rotate Table** from the shortcut menu.

    ![Rotate Table](https://devnet.logianalytics.com/hc/article_attachments/4404936781207/pgrpt_edit_manplt_tb1.gif)
* **Showing table columns**  
   You can specify which columns will be shown in a table. To do this, right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the table, then on the shortcut menu, select the names of the columns you want to show from the Show Column submenu.
* **Hiding/Deleting table columns**  
   To hide or remove a specific column in a table, right-click the column header and select **Hide Column** or **Remove Column** from the shortcut menu. When a column is hidden, you can show it again using the Show Column shortcut menu.
* **Adjusting the width of table columns according to contents**  
   When the contents in a table column need more space to completely display, you can adjust the width of the table column according to the contents. However to use this feature you need to first enable the Autofit property for either the label or DBField in the column (to enable the property, right-click the label in the column header or any value in the column and select **Properties** on the shortcut menu, then in the Font tab of the Label Properties dialog box or Data Field Properties dialog box, select **Autofit**), then right-click the column header and select **Autofit** from the shortcut menu.
* **Changing group direction**  
   You can make the group headers that are placed horizontally in a table to be displayed vertically. To do this, right-click the group header row or a value of the group and select **Vertical to Detail** from the shortcut menu.

  For groups displayed vertically in group columns, you can specify to place them horizontally in the table. To do this, right-click a blank cell or a value in the group column and select **Horizontal to Detail** from the shortcut menu.
* **Inserting table columns**  
  A table could contain the following types of columns: detail column, summary column and group column. You can insert them with the corresponding shortcut menu commands.
  + **To insert a common column into a table:**
    1. Right-click any column header or the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the table, then select **Insert** > **Common Column** on the shortcut menu.
    2. Drag object from the Resource View panel to the column header to add it in the column [using the method of replacing the field in a column](#Replace).
  + **To insert a detail or summary column into a table:**
    1. Right-click any column header or the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the table, then select **Insert** > **Detail Column**/**Summary Column**  from the shortcut menu.
    2. In the corresponding insert column dialog box, specify the resource you want to use for the new column, then select **OK**.

       ![Insert Summary Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942491799/insrtsumclmn.gif)
  + **To insert a group column into a table:**
    1. Right-click any column header or the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the table, then select **Insert** > **Group Column** from the shortcut menu. Report Server displays the [Insert Group Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009719562-Insert-Group-Column) dialog box, with the existing groups the table contains listed in an indented structure in the right box. You can edit the groups if you want.

       ![Insert Group Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936781463/insrtgrpclmn.gif)
    2. From the Resources box on the left, select the group object you want to use for the new group column and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif) to add it to the right box as the group-by field, then specify the sort direction of the group in the Sort column.
    3. Select the newly added group-by field and specify its position in the table:
       - **Group Above**  
          Specifies to place the group-by field in its own row above the detail information.
       - **Group Left Above**  
          Specifies to place the group-by field in its own row and column above and left of the detail information.
       - **Group Left**  
          Specifies to place the group-by field in its own column left of the detail information.
    4. Repeat the above steps to add more group columns if you want. You can make use of the ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif) buttons to adjust the group levels.
    5. Select **OK** to insert the group columns.

  **Note:** If you right-click any column header and use its shortcut menu to insert a common, detail or summary column, the Insert Column dialog box will appear for you to specify the position of the column to be inserted, which can be before or after the selected column, however, if you use the table shortcut menu to insert the column,

  + If it is a common column, the column will be inserted as the last column in the table.
  + If it is a detail/summary column, the column will be inserted after the last detail/summary column, or as the last column in the table when there is no detail/summary column.
* **Converting table columns**  
   You can convert a group column into a detail column. For a detail column, when the object in it can be used as group-by field, you can also convert it to a group column.
  + To convert a group column into a detail column, right-click in the column header and select **Convert to Detail**  from the shortcut menu, then the conversion is done.
  + **To convert a detail column into a group column:**
    1. Right-click in the column header and select **Convert to Group** from the shortcut menu.
    2. In the Select Group Position dialog box, specify the position for the newly converted group-by field.

       ![Select Group Position dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936781847/slctgrppstn.gif)

       - **Group Above**  
          If selected, a new group header panel is added to hold the group-by field and the detail column is removed.
       - **Group Left Above**  
          If selected, the detail column is converted to a group column and a new group header panel is added to hold the group-by field.
       - **Group Left**  
          If selected, the detail column is converted to a group column and the group-by field is placed in the column.
    3. Select **OK** to save the changes.
* **Aggregating on a detail column**  
   You can summarize the data in a detail column. To do this:
  1. Right-click in the column header and select **Aggregate On** from the shortcut menu. Report Server displays the [Aggregate On](https://devnet.logianalytics.com/hc/en-us/articles/1500009719082-Aggregate-On) dialog box.

     ![Aggregate On dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936782103/agrgton.gif)
  2. From the Function drop-down list, specify a function to summarize the data.
     When DistinctSum is selected, you should select ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404942451479/btn_chsr2.gif) next to the Distinct On text box to specify one or more group and detail objects according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009746281-Select-Fields) dialog box.

     For the usage about each function, refer to Aggregate Functions in the *Logi Report Designer Guide*.
  3. When done, select **OK**.
     + If the table has groups, you will find data in each group level and the whole table are summarized respectively in the column.
     + If the table has no groups, the summary will be based on the whole table.

  When you finish summarizing a detail column, you will find a [dynamic aggregation object](https://devnet.logianalytics.com/hc/en-us/articles/1500009750421-Using-Dynamic-Resources#Agg) is created at the same time which is given a default name Function\_DetailFieldName in the Dynamic Resources > Aggregations list of the Resource View panel and you can use it again in the current report.
* **Adjusting the order of columns and rows in a table**  
   To adjust the order of columns, drag a column header to the left or right boundary of another column header, when a highlighted line appears along the target column boundary, release the mouse.

  ![Adjust Column Order](https://devnet.logianalytics.com/hc/article_attachments/4404936782359/pgrpt_edit_manplt_tb2.gif)

  When a table contains several group rows, you can adjust the order of the group rows to edit the group levels. To do this, drag a value in a group row above or below another group row until a horizontally highlighted line appears, then release the mouse.

  ![Adjust Group Order](https://devnet.logianalytics.com/hc/article_attachments/4404942492311/pgrpt_edit_manplt_tb3.gif)

From the Resource View panel, you can drag view elements and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009750421-Using-Dynamic-Resources) into a table to replace the existing fields or add new columns/rows in the table. To do this, first select the table to locate the business view it uses in the Resource View panel, then:

* **To replace the field in a table column**:  
   Drag the required object from the Resource View panel and move the mouse pointer to the column header until the label in the header is highlighted, then release the mouse.

  ![Replace the Field in a Table Column](https://devnet.logianalytics.com/hc/article_attachments/4404936782615/pgrpt_edit_manplt_tb4.gif)
* **To add new table columns and rows:**  
   Drag the required object from the Resource View panel and move the mouse pointer to an existing column or row boundary until a highlighted line appears suggesting the position, then release the mouse. Depending on the object you select and the position where you drop the object, as well as the current table group structure, Page Report Studio determines whether a detail column, a summary column, a group column or a group row is added.
* **To add object values to a table column**  
  Drag the required object from the Resource View panel and move the mouse pointer to any value in the target column and release the mouse.

  ![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4404942492567/pgrpt_edit_manplt_tb5.gif)

  Values of the selected object are then added in the column together with the existing values.

  ![Add Value Result](https://devnet.logianalytics.com/hc/article_attachments/4404936782871/pgrpt_edit_manplt_tb6.gif)

## Manipulating a Banded Object

* **Hiding/Showing DBFields and field labels in a banded object**  
   The DBFields and their corresponding labels in a banded object can be hidden or shown. To do this, right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the banded object, then on the shortcut menu, select the DBFields and labels you want to show from the Show Field submenu. For a DBField or label that is shown, it will be marked with a check mark, and vise verse. You can also hide a DBField or label by right-clicking it and selecting **Hide** from the shortcut menu.

  ![Show Fields and Labels](https://devnet.logianalytics.com/hc/article_attachments/4404936783127/pgrpt_edit_manplt_bd1.gif)
* **Hiding/Showing a panel in a banded object**  
   A panel in a banded object can be hidden or shown. To do this, right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the banded object, then on the shortcut menu, select the item which indicates the panel name from the Show submenu. For a panel which is shown, the item is with a check mark, and vice versa. You can also hide a panel by right-clicking it and selecting **Hide** from the shortcut menu.
* **Resetting data in a banded object**  
   After sorting and filtering data in a banded object, you can right-click an object in the banded object and select the **Reset** item from the shortcut menu to reproduce the data of the banded object using the data cached in the data buffer. This will clear all sort and filter conditions from the banded object.
* **Expanding/Collapsing a group panel in a banded object**  
   You can expand and collapse the group panels in a banded object created in Logi Report Designer if it is enabled with the feature. For details, refer to Expanding/Collapsing the Group Records in Banded Objects in the *Logi Report Designer Guide*.

From the Resource View panel, you can drag view elements and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009750421-Using-Dynamic-Resources) into a banded object to add new groups and detail fields in the banded object. To do this, first select the banded object to locate the business view it uses in the Resource View panel, then:

* **To add a group:**  
   Drag a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) or dynamic formula used as Group ![Dynamic Formula Used as Group](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resource View panel and move the mouse pointer above or below any existing group until a highlighted horizontal line appears and the tip Group Header shows up (if there is no existing group in the banded object, move to the bottom boundary of the column header until the tip Banded Page Header and a highlighted horizontal line show up), then release the mouse.

  ![Add Banded Object Group](https://devnet.logianalytics.com/hc/article_attachments/4404942492823/pgrpt_edit_manplt_bd2.gif)
* **To add a detail field:**  
   Any type of the view elements and dynamic resources can be used as detail fields in a banded object. Drag an object from the Resource View panel and move the mouse pointer to the detail panel until the tip Detail Panel shows up, then release the mouse.

  ![Add Banded Detail](https://devnet.logianalytics.com/hc/article_attachments/4404942493335/pgrpt_edit_manplt_bd3.gif)

## Manipulating Geographic Map Group Markers

* **Going up/down on geographic map group markers**
  + For the group level that is higher than some other group levels in a geographic map component, point to its group marker, right-click it and select **Go Down** from the shortcut menu to jump one group level down.
  + For the group level that is lower than some other group levels in a geographic map component, point to its group marker, right-click it and select **Go Up** from the shortcut menu to jump one group level up.
* **Showing/Hiding geographic map group markers**  
   By default, all visible group markers are shown. To hide them, right-click the geographic map (not the group markers) and select **Hide Markers** from the shortcut menu. If you want to show them again, right-click the geographic map and select **Show Markers** from the shortcut menu.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750541-Applying-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750401-Drilling-Through-the-Report-Data)
