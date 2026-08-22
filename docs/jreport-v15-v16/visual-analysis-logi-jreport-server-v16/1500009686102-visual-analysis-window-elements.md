---
title: "Visual Analysis Window Elements"
id: 1500009686102
section: "Visual Analysis Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686102-Visual-Analysis-Window-Elements
updated_at: 2021-11-03T06:58:38Z
---

# Visual Analysis Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686082-Starting-a-Visual-Analysis-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009711801-Performing-Visual-Analysis)

# Visual Analysis Window Elements

Elements on the Visual Analysis window are divided into three sections:

* [Toolbar](#Toobar)
* [Left Panels](#Leftpanel)
* [Presentation Area](#Presentation)

## Toolbar

**![Menu button](https://devnet.logianalytics.com/hc/article_attachments/4412112642327/btn_va_menu.gif) Menu**

* **New**  
   Starts a new visual analysis in a new Visual Analysis window.
* **Open**  
   Opens an existing analysis template in a new Visual Analysis window via the [Open](https://devnet.logianalytics.com/hc/en-us/articles/1500009689242-Open) dialog.
* **Save**  
   Saves the changes to the current analysis template.
* **Save As**  
   Saves the current analysis template with a different name or location or [as a new version](https://devnet.logianalytics.com/hc/en-us/articles/1500009717981-Creating-Versions#Save) in the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009715401-Save-As) dialog.
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
* **Help**: Displays the Visual Analysis user's guide.
* **Exit**: Exits the Visual Analysis window.

![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4412139484183/btn_undo.gif)**Undo**

Undoes the last operation.

![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4412139484439/btn_redo.gif)**Redo**

Reverses the operation of Undo.

![Refresh button](https://devnet.logianalytics.com/hc/article_attachments/4412139483927/btn_refresh.gif)**Refresh**

Refreshes the current data result.

![Open button](https://devnet.logianalytics.com/hc/article_attachments/4412139483415/btn_open.gif) **Open**

Opens an existing analysis template in a new Visual Analysis window via the Open dialog.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/4412112482455/btn_save.gif) **Save**

Saves the changes made during the visual analysis.

![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4412112482711/btn_saveas.gif)**Save As**

Saves the current analysis template with a different name or location or [as a new version](https://devnet.logianalytics.com/hc/en-us/articles/1500009717981-Creating-Versions#Save) in the Save As dialog.

![Swap button](https://devnet.logianalytics.com/hc/article_attachments/4412131377687/btn_rotate.gif)**Swap**

Exchanges the columns and rows in the data presentation area.

**![View mode list](https://devnet.logianalytics.com/hc/article_attachments/4412139623575/btn_va_view.gif) View mode**

Specifies the [view mode](#View) from the drop-down list.

## Left Panels

**Data Source panel**

This panel lists all the fields in the selected business view. It provides data resources to the Filters panel and to the presentation area.

**Filters panel**

This panel lists the filters being used. You can add new filters by dragging group fields from the Data Source panel into the Filters panel. The newly added filters provide full values by default.

## Presentation Area

This is where you perform visual analysis operations. Follow the instructions in this area to drag data fields from the Data Source panel to the desired positions in the presentation area. As you start to drag a field, the possible places where you can drop it are highlighted with an orange border. As you add groups to the rows or columns the crosstab expands to include the new group and all of the aggregations are recalculated.

Only group and aggregation fields can be added into the data presentation area.

![Presentation Area](https://devnet.logianalytics.com/hc/article_attachments/4412112642583/va_wndw_prst.gif)

The following are details about each element:

**Column and Row control boxes**

* ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4412139624983/btn_va_drpgrpclmn.gif)  
   Group fields can be added to this control box to become column headers.
* ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4412112643095/btn_va_drpaggclmn.gif)  
   Aggregation fields can be added to this control box to become column headers. The fields are used to draw axes horizontally at the bottom.
* ![Row box](https://devnet.logianalytics.com/hc/article_attachments/4412139626135/btn_va_drpgrprw.gif)  
   Group fields can be added to this control box to become row headers.
* ![Row box](https://devnet.logianalytics.com/hc/article_attachments/4412139626391/btn_va_drpaggrw.gif)  
   Aggregation fields can be added to this control box to become row headers. The fields are used to draw axes vertically on the left.

**Display Type button**

Specifies the display type of the data values displayed in the data presentation area. The following display types are supported:

* ![Text Type](https://devnet.logianalytics.com/hc/article_attachments/4412139626647/btn_va_dsplytyp_txt.gif)**Text**  
   The data values are displayed in text. This type requires that a data field is defined by the label legend ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4412139626903/btn_va_lbl.gif) in the legend section.
* ![Bar Type](https://devnet.logianalytics.com/hc/article_attachments/4412112643351/btn_va_dsplytyp_bar.gif)**Bar**  
   The data values are displayed in bar chart.
* ![Line Type](https://devnet.logianalytics.com/hc/article_attachments/4412139627159/btn_va_dsplytyp_ln.gif)**Line**  
   The data values are displayed in line chart.
* ![Pie Type](https://devnet.logianalytics.com/hc/article_attachments/4412131518743/btn_va_dsplytyp_pie.gif)**Pie**  
   The data values are displayed in pie chart.
* ![Shape Type](https://devnet.logianalytics.com/hc/article_attachments/4412139627415/btn_va_dsplytyp_shp.gif)**Shape**  
   The data values are displayed as shape diagrams.

**Legend section**

The following introduces all available legend types. Some legend types are specific to certain display types.

* **![Color button](https://devnet.logianalytics.com/hc/article_attachments/4412112644375/btn_va_clr.gif) Color**  
   The color legend allows you to identify the members of a data field by colors.

  Data fields that can be bound with the color legend should be either of the following:

  + One or more group fields.
  + One single aggregation field.

  Multiple aggregation fields and the combination of group and aggregation fields are not supported.

  For a single field, each field member is marked by a distinct color. For multiple group fields, each combination of the members of the fields is marked by a distinct color.
* **![Label button](https://devnet.logianalytics.com/hc/article_attachments/4412139626903/btn_va_lbl.gif) Label**  
   The label legend can be bound with multiple data fields to provide label text to the members of the data fields.
* **![Size button](https://devnet.logianalytics.com/hc/article_attachments/4412139627671/btn_va_sz.gif) Size**  
   The size legend can be bound with at most one data field to identify the members of the data field by sizes.
* **![Slice button](https://devnet.logianalytics.com/hc/article_attachments/4412139627927/btn_va_angl.gif) Slice**  
   The slice legend can be bound with at most one aggregation field to identify the members of the aggregation field by sections divided from the center point in pies. It is available to the Pie display type only.
* **![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4412112644631/btn_va_shp.gif) Shape**  
   The shape legend can be bound with at most one data field to identify the members of the data field by shapes. It is available to the Shape display type only.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686082-Starting-a-Visual-Analysis-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009711801-Performing-Visual-Analysis)
