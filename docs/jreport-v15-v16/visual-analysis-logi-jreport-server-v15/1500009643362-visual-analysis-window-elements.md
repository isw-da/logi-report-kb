---
title: "Visual Analysis Window Elements"
id: 1500009643362
section: "Visual Analysis Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009643362-Visual-Analysis-Window-Elements
updated_at: 2021-07-24T20:55:33Z
---

# Visual Analysis Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009667861-Starting-a-Visual-Analysis-Session)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643282-Performing-Visual-Analysis)

# Visual Analysis Window Elements

The Visual Analysis window contains the following elements:

* [Toolbar](#Toobar)
* [Left Panels](#Leftpanel)
* [Presentation Area](#Presentation)

## Toolbar

**![Menu button](https://devnet.logianalytics.com/hc/article_attachments/4404920661911/btn_va_menu.gif) Menu**

* **New**  
   Starts a new visual analysis in a new Visual Analysis window.
* **Open**  
   Opens an existing analysis template in a new Visual Analysis window via the [Open](https://devnet.logianalytics.com/hc/en-us/articles/1500009671421-Open) dialog.
* **Save**  
   Saves the changes to the current analysis template.
* **Save As**  
   Saves the current analysis template with a different name or location or [as a new version](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions#Save) in the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009647002-Save-As) dialog.
* **Undo**  
   Undoes the last operation.
* **Redo**  
   Reverses the operation of Undo.
* **Clear Filters**  
   Clears the filters in the Filters panel.
* **Swap**  
   Exchanges the row headers and the column headers.
* **View**  
   Specifies the view mode:
  + **Normal View**  
     The Logi JReport smart layout. Scrollbar will be provided horizontally or vertically if the available space cannot hold all the data.
  + **Fit Height**  
     All vertical data are displayed according to the available height.
  + **Fit Width**  
     All horizontal data are displayed according to the available width.
  + **Fit Visible**  
     The combination of Fit Width and Fit Height. All data are displayed horizontally and vertically according to the available space.

  In the Fit XXX mode, the column header height, row header width, and the header font size is the same as that in Normal View. The text in the header will be cut if it cannot be fully displayed.
* **Help**  
   Displays the Visual Analysis user's guide.
* **Exit**  
   Exits the Visual Analysis window.

![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404920359447/btn_undo.gif)**Undo**

Undoes the last operation.

![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404926629015/btn_redo.gif)**Redo**

Reverses the operation of Undo.

![Refresh button](https://devnet.logianalytics.com/hc/article_attachments/4404920358935/btn_refresh.gif)**Refresh**

Refreshes the current data result.

![Open button](https://devnet.logianalytics.com/hc/article_attachments/4404920357783/btn_open.gif) **Open**

Opens an existing analysis template in a new Visual Analysis window via the Open dialog.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404926628119/btn_save.gif) **Save**

Saves the changes made during the visual analysis.

![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404920358039/btn_saveas.gif)**Save As**

Saves the current analysis template with a different name or location or [as a new version](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions#Save) in the Save As dialog.

![Swap button](https://devnet.logianalytics.com/hc/article_attachments/4404920364567/btn_rotate.gif)**Swap**

Exchanges the columns and rows in the data presentation area.

**![View mode list](https://devnet.logianalytics.com/hc/article_attachments/4404926787735/btn_va_view.gif) View mode**

Specifies the [view mode](#View) from the drop-down list.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Left Panels

**Resources panel**

This panel lists all the fields in the selected business view. It provides data resources to the Filters panel and to the presentation area.

**Filters panel**

This panel lists the filters being used. You can add new filters by dragging group fields from the Resources panel into the Filters panel. The newly added filters provide full values by default.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Presentation Area

This is where you perform visual analysis actions. Follow the instructions in this area to drag data fields from the Resources panel to the desired positions in the presentation area. As you start to drag a field, the possible places where you can drop it are highlighted with a red border. As you add groups to the rows or columns the crosstab expands to include the new group and all of the aggregations are recalculated.

Only group and aggregation fields can be added into the data presentation area.

![Presentation Area](https://devnet.logianalytics.com/hc/article_attachments/4404920662167/va_wndw_prst.gif)

The following are details about each element:

**Column and Row control boxes**

* ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4404920662423/btn_va_drpgrpclmn.gif)  
   Group fields can be added to this control box to become column headers.
* ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4404920662679/btn_va_drpaggclmn.gif)  
   Aggregation fields can be added to this control box to become column headers. The fields are used to draw axes horizontally at the bottom.
* ![Row box](https://devnet.logianalytics.com/hc/article_attachments/4404920662935/btn_va_drpgrprw.gif)  
   Group fields can be added to this control box to become row headers.
* ![Row buox](https://devnet.logianalytics.com/hc/article_attachments/4404926787991/btn_va_drpaggrw.gif)  
   Aggregation fields can be added to this control box to become row headers. The fields are used to draw axes vertically on the left.

**Display Type button**

Specifies the display type of the data values displayed in the data presentation area. The following display types are supported:

* ![Text Type](https://devnet.logianalytics.com/hc/article_attachments/4404920663191/btn_va_dsplytyp_txt.gif)**Text**  
   The data values are displayed in text. This type requires that a data field is defined by the label legend ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404920663447/btn_va_lbl.gif) in the legend section.
* ![Bar Type](https://devnet.logianalytics.com/hc/article_attachments/4404920663703/btn_va_dsplytyp_bar.gif)**Bar**  
   The data values are displayed in bar chart.
* ![Line Type](https://devnet.logianalytics.com/hc/article_attachments/4404926788503/btn_va_dsplytyp_ln.gif)**Line**  
   The data values are displayed in line chart.
* ![Pie Type](https://devnet.logianalytics.com/hc/article_attachments/4404920663959/btn_va_dsplytyp_pie.gif)**Pie**  
   The data values are displayed in pie chart.
* ![Shape Type](https://devnet.logianalytics.com/hc/article_attachments/4404920664215/btn_va_dsplytyp_shp.gif)**Shape**  
   The data values are displayed as shape diagrams.

**Legend section**

The following introduces all available legend types. Some legend types are specific to certain display types.

* **![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404920664471/btn_va_clr.gif) Color**  
   The color legend allows you to identify the members of a data field by colors.

  Data fields that can be bound with the color legend should be either of the following:

  + One or more group fields.
  + One single aggregation field.

  Multiple aggregation fields and the combination of group and aggregation fields are not supported.

  For a single field, each field member is marked by a distinct color. For multiple group fields, each combination of the members of the fields is marked by a distinct color.
* **![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404920663447/btn_va_lbl.gif) Label**  
   The label legend can be bound with multiple data fields to provide label text to the members of the data fields.
* **![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404920664727/btn_va_sz.gif) Size**  
   The size legend can be bound with at most one data field to identify the members of the data field by sizes.
* **![Slice button](https://devnet.logianalytics.com/hc/article_attachments/4404920664983/btn_va_angl.gif) Slice**  
   The slice legend can be bound with at most one aggregation field to identify the members of the aggregation field by sections divided from the center point in pies. It is available to the Pie display type only.
* **![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404926788759/btn_va_shp.gif) Shape**  
   The shape legendcan be bound with at most one data field to identify the members of the data field by shapes.It is available to the Shape display type only.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009667861-Starting-a-Visual-Analysis-Session)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643282-Performing-Visual-Analysis)
