---
title: "Performing Visual Analysis"
id: 1500009744041
section: "Using Visual Analysis Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744041-Performing-Visual-Analysis
updated_at: 2021-07-25T07:20:27Z
---

# Performing Visual Analysis

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718242-Visual-Analysis-Window-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744061-Saving-Analysis-Templates)

# Performing Visual Analysis

You can make use of the Visual Analysis window to analyze the data in a business view intuitively and conveniently, after you access it in your browser by any of the ways introduced in [Starting a Visual Analysis Session](https://devnet.logianalytics.com/hc/en-us/articles/1500009744081-Starting-a-Visual-Analysis-Session). This topic describes how you can add data fields, change their display types, work with the five legends, filter and sort data, and switch view mode.

Note that you can only add group and aggregation fields into the data presentation area.

Select the following links to view the topics:

* [Adding Data Fields as Column or Row Headers](#Add)
* [Changing the Display Type of the Data Values](#DisplayType)
* [Working With the Color Legend](#ColorLegend)
* [Working With the Size Legend](#SizeLegend)
* [Working With the Label Legend](#LabelLegend)
* [Working With the Slice Legend](#SliceLegend)
* [Working With the Shape Legend](#ShapeLegend)
* [Showing the Tip Information of the Data Values](#Tip)
* [Exchanging Columns and Rows](#Exchange)
* [Filtering Data](#Filter)
* [Sorting a Row/Column Header Field](#Sort)
* [Undoing/Redoing Actions](#Undo)
* [Refreshing the Current Data View](#Refresh)
* [Switching Fields Between Legends](#SwitchLegend)
* [Showing/Hiding the Row/Column Title/Header](#ShowHide)
* [Switching the View Mode](#ViewMode)
* [Examples of Using Different Display Types](#Example)

## Adding Data Fields as Column or Row Headers

You can add group and aggregation fields as column or row headers. Drag a data field from the resources panel and drop it to the proper control box, following the instructions of the four control boxes highlighted in the below image. You can select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) beside the four control boxes to add a group or an aggregation field from a list of group fields or aggregation fields in the current business view.

![Add Field as Header](https://devnet.logianalytics.com/hc/article_attachments/4404942614167/va_prfrm_hdr.gif)

When you add an aggregation as a header, the aggregation will be used to draw axes in the header cells.

You can add multiple fields as column or row headers. For column headers, the order of the group fields or the aggregation fields from left to right decides the grouping order from the first level to the last level. That is, the grouping order is from left to right. For example, there are Year, Region, and Category group fields added as the column headers and are displayed from left to right. Year will be the first level group, Region the second, and Category the last. For row headers, the grouping order is from bottom to top.

When you drag a field to be a header, you can decide its position if there are already existing fields. If you are not satisfied with the current grouping order, you can adjust the order of the fields by dragging and dropping.

To remove a data field from being a column or row header, drag the field outside of its control box, or right-click the field and select **Delete** from the shortcut menu.

## Changing the Display Type of the Data Values

To specify the way of presenting the data values, select the **Display Type** button which may vary with the context and select the required [display type](https://devnet.logianalytics.com/hc/en-us/articles/1500009718242-Visual-Analysis-Window-Elements#DisplayType) from the type list.

## Working With the Color Legend

You can use the color legend to identify the members of a data field by colors.

* **Adding data fields to the color legend**  
   Drag the field from the resources panel to ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif) in the legend section. If group fields are already added in the color legend, dragging an aggregation field to the legend will remove all the existing group fields from the legend; if an aggregation field is already added in the color legend, dragging another group field or aggregation field to the legend will remove the existing aggregation field from the legend.
* **Moving a color legend field to another legend**  
   Drag the field to the target legend button, or right-click on the field name and select the proper item:
  + **As Size**  
     Moves the field from the color legend to the size legend.
  + **As Label**   
     Moves the field from the color legend to the label legend.
  + **As Slice**  
     Moves the field from the color legend to the slice legend.
  + **As Shape**  
     Moves the field from the color legend to the shape legend.

* **Replacing a data field**  
   To replace a group field in the color legend with another group field, drag the new field and drop it to the existing field name in the color legend until the name bar is highlighted.

  To replace an aggregation field with another aggregation field, drag the new field and drop it to ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif)or drop it to the existing field name in the color legend until the name bar is highlighted.
* **Changing the field order**  
   When multiple group fields are bound with the color legend, you can change their order. By default, the bound fields are listed from top to bottom. Drag a field that is not at the bottom of the list to ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif) and the field will be moved to the bottom of the list.
* **Removing a data field from the color legend**  
   Drag and drop the field name outside of its position.
* **Customizing color when color legend is bound with no field**  
   If no field is bound with the color legend, the color legend will use one single color. Select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif) and you will be able to select a color in the color palette, or select **More Colors** to select a color within a wider range.

  ![Color Palette](https://devnet.logianalytics.com/hc/article_attachments/4404942614423/va_prfrm_clrlst.gif)

  + **Recent Colors**  
     Recent used colors are listed here. It is session level. You can select a recent color to apply it.
  + **More Colors**  
     Opens the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009748041-Color-Picker) dialog box in which you can select a color within a wider range.
* **Customizing color when color legend is bound with fields**  
   If group fields are bound with the color legend, the colors will be discrete colors that come from a pattern. To change the color, select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif) to access the [Edit Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009721042-Edit-Color) dialog box.

  If an aggregation field is bound with the color legend, the colors will be gradient colors which also come from a pattern. To change the color, select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif) to access the [Edit Gradient Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009748061-Edit-Gradient-Color) dialog box.

## Working With the Size Legend

You can use the size legend to identify the members of a data field by sizes.

* **Adding data field to the size legend**  
   Drag the field from the resources panel to ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404936968471/btn_va_sz.gif) in the legend section. The size legend can be bound with one field only, so when you drag a different field to ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404936968471/btn_va_sz.gif) which is already bound with a field, the new field will replace the existing field.
* **Adjusting the size legend**  
   Select ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404936968471/btn_va_sz.gif) and you will be able to adjust the size legend in percentage. The range is from 1% to 200%.
* **Moving the size legend field to another legend**  
   Drag the field to the target legend button, or right-click on the field name and select the proper item:
  + **As Color**  
     Moves the field from the size legend to the color legend.
  + **As Label**  
     Moves the field from the size legend to the label legend.
  + **As Slice**  
     Moves the field from the size legend to the slice legend.
  + **As Shape**  
     Moves the field from the size legend to the shape legend.
* **Removing the size legend field**  
   Drag and drop the field name outside of its position.

## Working With the Label Legend

You can use the label legend to show the labels of the members of a data field.

* **Adding data fields to the label legend**   
   For example, to show the country names in the data values displayed in the data presentation area, drag the Country field to ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404942613143/btn_va_lbl.gif) in the legend section.
* **Moving a label legend field to another legend**  
   Drag the field to the target legend button, or right-click on the field name and select the proper item:
  + **As Color**  
     Moves the field from the label legend to the color legend.
  + **As Size**  
     Moves the field from the label legend to the size legend.
  + **As Slice**  
     Moves the field from the label legend to the slice legend.
  + **As Shape**  
     Moves the field from the label legend to the shape legend.
* **Replacing a data field**  
   Drag the new field and drop it to ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404942613143/btn_va_lbl.gif)or drop it to the existing field name in the label legend until the name is highlighted.
* **Changing the field order**  
   When multiple data fields are bound with the label legend, you can change their order. By default, the bound fields are listed from top to bottom. Drag a field that is not at the bottom of the list to ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404942613143/btn_va_lbl.gif) and the field will be moved to the bottom of the list.
* **Removing a data field from the label legend**  
   Drag and drop the field name outside of its position.

## Working With the Slice Legend

You can use the slice legend to make the pie divided around the center according to an aggregation field. The slice legend is available when the display type is Pie.

* **Adding data field to the slice legend**  
   Drag the field from the resources panel to ![Slice button](https://devnet.logianalytics.com/hc/article_attachments/4404942613911/btn_va_angl.gif) in the legend section. The slice legend can be bound with one aggregation field only, so when you drag a different aggregation field to ![Slice button](https://devnet.logianalytics.com/hc/article_attachments/4404942613911/btn_va_angl.gif) which is already bound with a field, the new field will replace the existing field.
* **Moving the slice legend field to another legend**  
   Drag the field to the target legend button, or right-click on the field name and select the proper item:
  + **As Color**  
     Moves the field from the slice legend to the color legend.
  + **As Size**  
     Moves the field from the slice legend to the size legend.
  + **As Label**   
     Moves the field from the slice legend to the label legend.
* **Removing the slice legend field**  
   Drag and drop the field name outside of its position.

## Working With the Shape Legend

You can use the shape legend to identify the members of a data field by shapes. The shape legend is available when the display type is Shape.

* **Adding data field to the shape legend**

  Drag the field from the resources panel to ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404936968727/btn_va_shp.gif) in the legend section. The shape legend can be bound with one data field only, so when you drag a different field to **![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404936968727/btn_va_shp.gif)** which is already bound with a field, the new field will replace the existing field.
* **Moving the shape legend field to another legend**  
  Drag the field to the target legend button, or right-click on the field name and select the proper item:
  + **As Color**  
     Moves the field from the shape legend to the color legend.
  + **As Size**  
     Moves the field from the shape legend to the size legend.
  + **As Label**  
     Moves the field from the shape legend to the label legend.
* **Removing the shape legend field**  
  Drag and drop the field name outside of its position.
* **Customizing shape when shape legend is bound with no field**

  If no field is bound with the shape legend, the shape legend will use one shape. To change the shape, select **![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404936968727/btn_va_shp.gif)**and then select a shape from the shape list.

  ![Shape list](https://devnet.logianalytics.com/hc/article_attachments/4404936969111/va_prfrm_shplst.gif)

  The first shape is the default applied shape.
* **Customizing shape when shape legend is bound with a field**  
   If a data field is bound with the shape legend, to change the shapes for members of the field, select **![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404936968727/btn_va_shp.gif)** and edit the shapes in the [Edit Shapes](https://devnet.logianalytics.com/hc/en-us/articles/1500009721062-Edit-Shapes) dialog box.

## Showing the Tip Information of the Data Values

Put the mouse pointer on any value in the data presentation area, and Report Server displays a tip box showing the detailed information of the value.

## Exchanging Columns and Rows

To exchange the positions of the columns and rows, select the **Swap** button ![Swap button](https://devnet.logianalytics.com/hc/article_attachments/4404942448663/btn_rotate.gif) on the toolbar.

## Filtering Data

You can create one or more filters based on group fields in Visual Analysis. To do this, take either of the following ways:

* Drag a group field from the resources panel into the Filters panel.
* In the data presentation area, right-click a group field and select **Use as Filter** from the shortcut menu.

A filter is then added in the Filters panel with all the values of the group field being applied. You can select the desired values in the filter to filter values in the data presentation area.

To remove a filter, drag its field outside of the Filters panel.

When you move the mouse pointer on the Filters panel title bar, you can see an arrow button ![More Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) on the right. Select the arrow and there are two options:

* **Reset All Filters**  
   Resets the values of all the filters to the initial state.
* **Clear All Filters**  
   Removes all the filters from the Filters panel. You can also remove all the filters from the Filters panel by selecting the Menu button **![Menu button](https://devnet.logianalytics.com/hc/article_attachments/4404936966039/btn_va_menu.gif)** on the toolbar and then selecting Clear Filters.

Move the mouse pointer on a filter's title bar and you will see more filter options:

![Filter Options](https://devnet.logianalytics.com/hc/article_attachments/4404942614679/va_prfrm_fltr.gif)

* ![Reset button](https://devnet.logianalytics.com/hc/article_attachments/4404942451223/btn_clear.gif)**Reset**  
  Resets the values of the filter to the initial state.
* ![Reverse button](https://devnet.logianalytics.com/hc/article_attachments/4404936969623/btn_va_fltr_rvs.gif)**Reverse**  
  Applies the other unselected filter values instead of the selected ones.
* ![More Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) **More Options**  
   Changes the display type of the filter:
  + **Check box**  
    The field values are displayed with check boxes and multiple values can be selected.
  + **Radio**  
    The field values are displayed with radio buttons and only one single value can be selected except for all values.
  + **Range Slider**  
    The field values are displayed with a slider and a range of values can be selected.
  + **Slider**  
    The field values are displayed with a slider and only one single value can be selected except for all values.

## Sorting a Row/Column Header Field

To sort a data field in the row/column header, right-click it and select **Sort** from the shortcut menu. In the [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009721122-Sort) dialog box, choose a way to specify the sort order.

![Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936874391/sort.gif)

* Set the order to be Ascending or Descending. If you want to perform the sort based on another field, select the **Sort Using Another Field** radio button and then select a field from the drop-down list that follows. For example, when you set the sort order to Ascending and specify to use the field Total Sales to perform the sort action, the final sort result will be that Total Sales is sorted in the ascending order.
* Select the **Customize** option to adjust the order of the members of the current data field manually. Use the arrow buttons to adjust the order of the members.

## Undoing/Redoing Actions

You can undo or redo some actions. To do this, select the **Undo** button ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404942446103/btn_undo.gif) or **Redo** button ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404936716567/btn_redo.gif) on the toolbar.

## Refreshing the Current Data View

Select the **Refresh** button ![Refresh button](https://devnet.logianalytics.com/hc/article_attachments/4404936716311/btn_refresh.gif) on the toolbar.

## Switching Fields Between Legends

Within a display type, after a field is bound with a legend type, you can directly drag the field to another legend type, or use the menu after you right-click the field name bar under the original legend.

## Showing/Hiding the Row/Column Title/Header

To show or hide the row/column title or header, right-click a related row/column control box and then select or unselect **Show Title** or **Show Header** on the shortcut menu.

## Switching the View Mode

To switch the view mode, select the **Menu** button **![Menu button](https://devnet.logianalytics.com/hc/article_attachments/4404936966039/btn_va_menu.gif)** on the toolbar and then select an item on the [View](https://devnet.logianalytics.com/hc/en-us/articles/1500009718242-Visual-Analysis-Window-Elements#View) list. Or select an item from the view mode drop-down list on the toolbar.

There are also some quick ways to switch between the modes:

* Under the Normal View mode, double-click any position in the data area, the view mode will be switched to Fit Visible.
* Under the Fit XXX mode, double-click any position in the data area, the view mode will be switched to Normal View.

The view mode status will not be saved when saving the analysis template.

## Examples of Using Different Display Types

The following examples use the business view **WorldWideSalesBV** in /SampleReports.

* [Example 1: Displaying the data values in text](#Text)
* [Example 2: Displaying the data values as bar](#Bar)
* [Example 3: Displaying the data values as line](#Line)
* [Example 4: Displaying the data values as pie](#Pie)
* [Example 5: Displaying the data values as shape](#Shape)

**Example 1: Displaying the data values in text**

1. Make sure you do not change the display type, which is Text by default.
2. To view total sales, drag **Total Sales** from the resources panel and drop it to ![](https://devnet.logianalytics.com/hc/article_attachments/4404942613143/btn_va_lbl.gif) in the legend section.

   ![Drag Total Sales as Label](https://devnet.logianalytics.com/hc/article_attachments/4404936969879/va_prfrm_txt1.gif)

   There is only one value in the data presentation area which is the total sales in the whole business view.
3. Now let's view total sales in different years. Drag **Sales Year** to the column control box ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4404936966551/btn_va_drpgrpclmn.gif).

   ![Drag Sales Year as Column](https://devnet.logianalytics.com/hc/article_attachments/4404936970135/va_prfrm_txt2.gif)
4. To add product category as the row header, drag **Category** to the row control box ![Row box](https://devnet.logianalytics.com/hc/article_attachments/4404936967063/btn_va_drpgrprw.gif).

   ![Drag Category as Row](https://devnet.logianalytics.com/hc/article_attachments/4404936970391/va_prfrm_txt3.gif)
5. Drag **Region** as a column header right to Sales Year.

   ![Drag Region as Column](https://devnet.logianalytics.com/hc/article_attachments/4404936970647/va_prfrm_txtrgnadd.gif)

   Then get the following:

   ![Result](https://devnet.logianalytics.com/hc/article_attachments/4404936970903/va_prfrm_txtrgn.gif)
6. We will move Sales Year from the column header to row header by dragging.

   ![Swap Column and Row](https://devnet.logianalytics.com/hc/article_attachments/4404936971159/va_prfrm_txt4.gif)
7. We will filter the data with product type. Drag **Product Type** from the resources panel to the Filters panel.

   ![Add Filter on Product Type](https://devnet.logianalytics.com/hc/article_attachments/4404942615063/va_prfrm_txt5.gif)
8. Deselect **Regular**. Only the data about Decaf will be displayed.

   ![Results for Decaf](https://devnet.logianalytics.com/hc/article_attachments/4404936971543/va_prfrm_txt6.gif)

**Example 2: Displaying the data values as bar**

1. Select the **Display Type** button ![Display Type button](https://devnet.logianalytics.com/hc/article_attachments/4404942612887/btn_va_dsplytyp_txt.gif) and then select ![Bar Type](https://devnet.logianalytics.com/hc/article_attachments/4404936967575/btn_va_dsplytyp_bar.gif) from the type list.
2. Drag **Sales Year** to the row control box ![Row box](https://devnet.logianalytics.com/hc/article_attachments/4404936967063/btn_va_drpgrprw.gif) and **Total Sales** to the row control box ![Row box](https://devnet.logianalytics.com/hc/article_attachments/4404936967319/btn_va_drpaggrw.gif). The Total Sales field is used to draw axes in the row header.

   ![Add Rows](https://devnet.logianalytics.com/hc/article_attachments/4404942615319/va_prfrm_bar1.gif)
3. To mark different regions by color, drag **Region** to ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif) in the legend section.

   ![Add Region as Color Legend](https://devnet.logianalytics.com/hc/article_attachments/4404942615575/va_prfrm_bar2.gif)
4. Drag **Category** to the column control box ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4404936966551/btn_va_drpgrpclmn.gif) as the column header.

   ![Drag Category as Column](https://devnet.logianalytics.com/hc/article_attachments/4404936971799/va_prfrm_bar3.gif)
5. To show the total cost in each region by size, drag **Total Cost** to ![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404936968471/btn_va_sz.gif) in the legend section.

   ![Add Total Cost as Size Legend](https://devnet.logianalytics.com/hc/article_attachments/4404936972055/va_prfrm_bar4.gif)

**Example 3: Displaying the data values as line**

1. Select the **Display Type** button ![Display Type button](https://devnet.logianalytics.com/hc/article_attachments/4404942612887/btn_va_dsplytyp_txt.gif) and then select ![Line Type](https://devnet.logianalytics.com/hc/article_attachments/4404942613399/btn_va_dsplytyp_ln.gif) from the type list.
2. Drag **Total Sales** to the row control box ![Row box](https://devnet.logianalytics.com/hc/article_attachments/4404936967319/btn_va_drpaggrw.gif) as the axis and **Sales Quarter** to the column control box ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4404936966551/btn_va_drpgrpclmn.gif) to demonstrate the sales trend along the quarters.

   ![Add Row and Column](https://devnet.logianalytics.com/hc/article_attachments/4404942615831/va_prfrm_ln1.gif)
3. To view the sales trend along the quarters in each region, drag **Region** to ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif) in the legend section.

   ![Add Region as Color Legend](https://devnet.logianalytics.com/hc/article_attachments/4404942616087/va_prfrm_ln2.gif)

**Example 4: Displaying the data values as pie**

1. Select the **Display Type** button ![Display Type button](https://devnet.logianalytics.com/hc/article_attachments/4404942612887/btn_va_dsplytyp_txt.gif) and then select![Pie Type](https://devnet.logianalytics.com/hc/article_attachments/4404936967831/btn_va_dsplytyp_pie.gif) from the type list.
2. To mark different regions in different color in the pie, drag **Region** to ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif) in the legend section.

   ![Add Region as Color Legend](https://devnet.logianalytics.com/hc/article_attachments/4404936972311/va_prfrm_pie1.gif)
3. To demonstrate the total sales of each region by portion in the pie, drag the field **Total Sales** to ![Slice button](https://devnet.logianalytics.com/hc/article_attachments/4404942613911/btn_va_angl.gif) in the legend section.

   ![Add Total Sales as Slice Legend](https://devnet.logianalytics.com/hc/article_attachments/4404936972567/va_prfrm_pie2.gif)
4. To view the total sales in different years, drag the field **Sales Year** to the column control box ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4404936966551/btn_va_drpgrpclmn.gif).

   ![Add Sales Year as Column](https://devnet.logianalytics.com/hc/article_attachments/4404942616471/va_prfrm_pie3.gif)

**Example 5: Displaying the data values as shape**

1. Select the **Display Type** button ![Display Type button](https://devnet.logianalytics.com/hc/article_attachments/4404942612887/btn_va_dsplytyp_txt.gif) and then select ![Shape Type](https://devnet.logianalytics.com/hc/article_attachments/4404936968087/btn_va_dsplytyp_shp.gif) from the type list.
2. Add **Category** as the column header and **Total Sales**  as the row axis.

   ![Add Column and Row](https://devnet.logianalytics.com/hc/article_attachments/4404936972823/va_prfrm_shp1.gif)
3. To mark different regions with different shapes, drag **Region** to ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404936968727/btn_va_shp.gif) in the legend section.

   ![Add Region as Shape Legend](https://devnet.logianalytics.com/hc/article_attachments/4404936973079/va_prfrm_shp2.gif)
4. To change the shape pattern, select ![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404936968727/btn_va_shp.gif). Then in the Edit Shapes dialog box, select **Pattern3** from the drop-down list and select **OK**.

   ![Format Shape](https://devnet.logianalytics.com/hc/article_attachments/4404942616727/va_prfrm_shp3.gif)
5. To distinguish the shapes by color, drag **Region** to ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404942613655/btn_va_clr.gif) in the legend section.

   ![Add Region as Color Legend](https://devnet.logianalytics.com/hc/article_attachments/4404942616983/va_prfrm_shp4.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718242-Visual-Analysis-Window-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744061-Saving-Analysis-Templates)
