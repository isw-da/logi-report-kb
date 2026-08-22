---
title: "Visual Analysis Window Elements"
id: 1500009770681
section: "Using Visual Analysis to Analyze Data Intuitively and Instantly Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009770681-Visual-Analysis-Window-Elements
updated_at: 2021-07-24T00:49:40Z
---

# Visual Analysis Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742962-Starting-a-Visual-Analysis-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009742922-Performing-Visual-Analysis)

# Visual Analysis Window Elements

The Visual Analysis window has a toolbar at the top, a Resources panel and a Filters panel on the left, the presentation area in the middle, and a legend on the right.

This topic contains the following sections:

* [Toolbar](#Toolbar)
* [Resources panel](#ResourcesPanel)
* [Filters panel](#FiltersPanel)
* [Presentation Area](#Presentation)
* [Display Type](#DisplayType)
* [Legend](#Legend)

## Toolbar

**![Menu button](https://devnet.logianalytics.com/hc/article_attachments/4404880583831/btn_va_menu.gif) Menu**

Lists the following options in the drop-down list.

* **New**  
   Starts a new visual analysis in a new Visual Analysis window.
* **Open**  
   Opens an existing analysis template in a new Visual Analysis window via the [Open](https://devnet.logianalytics.com/hc/en-us/articles/1500009746602-Open-Dialog-Box-Properties) dialog box.
* **Save**  
   Saves the changes to the current analysis template.
* **Save As**  
   Saves the current analysis template with a different name or location or [as a new version](https://devnet.logianalytics.com/hc/en-us/articles/1500009748782-Creating-Versions#Save) in the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009746642-Save-As-Dialog-Box-Properties) dialog box.
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
     The Logi Report smart layout. A scrollbar will appear horizontally or vertically if the available space cannot hold all the data.
  + **Fit Height**  
     Displays all data according to the available height.
  + **Fit Width**  
     Displays all data according to the available width.
  + **Fit Visible**  
     The combination of Fit Width and Fit Height. All data are displayed horizontally and vertically according to the available space.

  In the Fit XXX mode, the column header height, row header width, and the header font size is the same as that in Normal View. The text in the header will be cut if it cannot be fully displayed.
* **Help**Displays the Visual Analysis user documentation.
* **Exit**Exits the Visual Analysis window.

![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404880138391/btn_undo.gif)**Undo**

Undoes the last operation.

![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404880138647/btn_redo.gif)**Redo**

Reverses the operation of Undo.

![Refresh button](https://devnet.logianalytics.com/hc/article_attachments/4404880138135/btn_refresh.gif)**Refresh**

Refreshes the current data result.

![Open button](https://devnet.logianalytics.com/hc/article_attachments/4404880136471/btn_open.gif) **Open**

Opens an existing analysis template in a new Visual Analysis window via the Open dialog box.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404885307671/btn_save.gif) **Save**

Saves the changes made during the visual analysis.

![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404880136727/btn_saveas.gif)**Save As**

Saves the current analysis template with a different name or location or [as a new version](https://devnet.logianalytics.com/hc/en-us/articles/1500009748782-Creating-Versions#Save) in the Save As dialog box.

![Swap button](https://devnet.logianalytics.com/hc/article_attachments/4404880141335/btn_rotate.gif)**Swap**

Exchanges the columns and rows in the data presentation area.

**![View mode list](https://devnet.logianalytics.com/hc/article_attachments/4404885618071/btn_va_view.gif) View mode**

Specifies the [view mode](#View) from the drop-down list.

## Resources panel

This panel lists all the fields in the selected business view. You can drag data resources from the Resources panel to the Filters panel, the presentation area, and the legend section.

## Filters panel

This panel lists the filters in use. You can add new filters by dragging group fields from the Resources panel into the Filters panel. The newly added filters provide full values by default.

## Presentation Area

This is where you perform visual analysis operations. Follow the instructions in this area to drag data fields from the Resources panel to the desired positions in the presentation area. As you start to drag a field, the possible places where you can drop it are highlighted with an orange border. As you add groups to the rows or columns the crosstab expands to include the new group and all of the aggregations are recalculated.

Only group and aggregation fields can be added into the data presentation area.

![Presentation Area](https://devnet.logianalytics.com/hc/article_attachments/4404880584343/va_wndw_prst.gif)

The following are details about the Column and Row control boxes:

* ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4404880584727/btn_va_drpgrpclmn.gif)  
   Group fields can be added to this control box to become column headers.
* ![Column box](https://devnet.logianalytics.com/hc/article_attachments/4404880585239/btn_va_drpaggclmn.gif)  
   Aggregation fields can be added to this control box to become column headers. The fields are used to draw axes horizontally at the bottom.
* ![Row box](https://devnet.logianalytics.com/hc/article_attachments/4404880585623/btn_va_drpgrprw.gif)  
   Group fields can be added to this control box to become row headers.
* ![Row box](https://devnet.logianalytics.com/hc/article_attachments/4404880586135/btn_va_drpaggrw.gif)  
   Aggregation fields can be added to this control box to become row headers. The fields are used to draw axes vertically on the left.

## Display Type

The Display Type button is located at the top left of the presentation area. It specifies the display type of the data values displayed in the data presentation area. The following display types are supported:

* ![Text Type](https://devnet.logianalytics.com/hc/article_attachments/4404885618327/btn_va_dsplytyp_txt.gif)**Text**  
   The data values are displayed in text. This type requires that a data field is defined by the label legend ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404880586903/btn_va_lbl.gif) in the legend section.
* ![Bar Type](https://devnet.logianalytics.com/hc/article_attachments/4404885618583/btn_va_dsplytyp_bar.gif)**Bar**  
   The data values are displayed in bar chart.
* ![Line Type](https://devnet.logianalytics.com/hc/article_attachments/4404880587415/btn_va_dsplytyp_ln.gif)**Line**  
   The data values are displayed in line chart.
* ![Pie Type](https://devnet.logianalytics.com/hc/article_attachments/4404880587927/btn_va_dsplytyp_pie.gif)**Pie**  
   The data values are displayed in pie chart.
* ![Shape Type](https://devnet.logianalytics.com/hc/article_attachments/4404880588183/btn_va_dsplytyp_shp.gif)**Shape**  
   The data values are displayed as shape diagrams.

## Legend

The legend section is on the right of the presentation area. The following introduces all available legend types. Some legend types are specific to certain display types.

* **![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404880588567/btn_va_clr.gif) Color**  
   The color legend enables you to identify the members of a data field by colors.

  You can bind either of the following data fields with the color legend:

  + One or more group fields.
  + One single aggregation field.

  Multiple aggregation fields and the combination of group and aggregation fields are not supported.

  For a single field, each field member is marked by a distinct color. For multiple group fields, each combination of the members of the fields is marked by a distinct color.
* **![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404880586903/btn_va_lbl.gif) Label**  
   The label legend can be bound with multiple data fields to provide label text to the members of the data fields.
* **![Size button](https://devnet.logianalytics.com/hc/article_attachments/4404880589207/btn_va_sz.gif) Size**  
   The size legend can be bound with at most one data field to identify the members of the data field by sizes.
* **![Slice button](https://devnet.logianalytics.com/hc/article_attachments/4404885619223/btn_va_angl.gif) Slice**  
   The slice legend can be bound with at most one aggregation field to identify the members of the aggregation field by sections divided from the center point in pies. It is available to the Pie display type only.
* **![Shape button](https://devnet.logianalytics.com/hc/article_attachments/4404880589719/btn_va_shp.gif) Shape**  
   The shape legend can be bound with at most one data field to identify the members of the data field by shapes. It is available to the Shape display type only.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742962-Starting-a-Visual-Analysis-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009742922-Performing-Visual-Analysis)
