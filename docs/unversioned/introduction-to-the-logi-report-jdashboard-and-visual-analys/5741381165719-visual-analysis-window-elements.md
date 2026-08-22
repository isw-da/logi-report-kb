---
title: "Visual Analysis Window Elements"
id: 5741381165719
section: "Introduction to the Logi Report JDashboard and Visual Analysis Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741381165719-Visual-Analysis-Window-Elements
updated_at: 2022-10-31T17:15:41Z
---

# Visual Analysis Window Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741363150231-Starting-a-Visual-Analysis-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741385892759-Performing-Visual-Analysis)

# Visual Analysis Window Elements

The Visual Analysis window has a toolbar at the top, the Resources panel and Filters panel on the left, the presentation area in the middle, and a legend on the right. This topic describes the elements on the Visual Analysis window.

This topic contains the following sections:

* [Toolbar](#Toolbar)
* [Resources panel](#ResourcesPanel)
* [Filters panel](#FiltersPanel)
* [Presentation Area](#Presentation)
* [Display Type](#DisplayType)
* [Legend](#Legend)

## Toolbar

**![Menu button](https://devnet.logianalytics.com/hc/article_attachments/9905831768215/btn_va_menu.gif) Menu**

Select to open a drop-down menu which contains the following options.

* **New**  
   Select to start a new visual analysis in a new Visual Analysis window.
* **Open**  
   Select to open an existing analysis template in a new Visual Analysis window using the [Open](https://devnet.logianalytics.com/hc/en-us/articles/5741443764887-Open-Dialog-Box-Properties) dialog box.
* **Save**  
   Select to save the changes you made to the current analysis template.
* **Save As**  
   Select to save the current analysis template with a different name or location or [as a new version](https://devnet.logianalytics.com/hc/en-us/articles/5741462158487-Creating-Versions#Save) using the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/5741449076887-Save-As-Dialog-Box-Properties) dialog box.
* **Undo**  
   Select to undo the last operation.
* **Redo**  
   Select to reverse the operation of **Undo**.
* **Clear Filters**  
   Select to clear the filters in the **Filters** panel.
* **Swap**  
   Select to exchange the row headers and the column headers.
* **View**  
   Select to choose the view mode:
  + **Normal View**  
     The Logi Report smart layout. A scroll bar appears horizontally or vertically if the available space cannot hold all the data.
  + **Fit Height**  
     Select to display all data according to the available height.
  + **Fit Width**  
     Select to display all data according to the available width.
  + **Fit Visible**  
     Select to use the combination of **Fit Width** and **Fit Height**. Server displays all data according to the available space horizontally and vertically.

  In the Fit XXX mode, the column header height, row header width, and the header font size is the same as that in **Normal View**. Server displays a part of the text in the header if there is not enough space for the text.
* **Help**Select to display the Visual Analysis user documentation.
* **Exit**Select to exit the Visual Analysis window.

![Undo button](https://devnet.logianalytics.com/hc/article_attachments/9905616106263/btn_undo.gif)**Undo**

Select to undo the last operation.

![Redo button](https://devnet.logianalytics.com/hc/article_attachments/9905616128151/btn_redo.gif)**Redo**

Select to reverse the operation of **Undo**.

![Refresh button](https://devnet.logianalytics.com/hc/article_attachments/9905616092439/btn_refresh.gif)**Refresh**

Select to refresh the current data.

![Open button](https://devnet.logianalytics.com/hc/article_attachments/9905577968791/btn_open.gif) **Open**

Select to open an existing analysis template in a new Visual Analysis window using the Open dialog box.

![Save button](https://devnet.logianalytics.com/hc/article_attachments/9905577991703/btn_save.gif) **Save**

Select to save the changes you made during the visual analysis.

![Save As button](https://devnet.logianalytics.com/hc/article_attachments/9905615943319/btn_saveas.gif)**Save As**

Select to save the current analysis template with a different name or location or [as a new version](https://devnet.logianalytics.com/hc/en-us/articles/5741462158487-Creating-Versions#Save) using the Save As dialog box.

![Swap button](https://devnet.logianalytics.com/hc/article_attachments/9905616609943/btn_rotate.gif)**Swap**

Select to exchange the columns and rows in the data presentation area.

**![View mode list](https://devnet.logianalytics.com/hc/article_attachments/9905820078231/btn_va_view.gif) View mode**

Select the [view mode](#View) from the drop-down list.

## Resources panel

This panel lists all the fields in the current business view. You can drag data resources from the Resources panel to the **Filters** panel, the presentation area, and the legend section.

## Filters panel

This panel lists the filters in use. You can add new filters by dragging group fields from the Resources panel into the Filters panel. The newly added filters use all data by default.

## Presentation Area

This is where you perform visual analysis operations. Follow the instructions in this area to drag data fields from the Resources panel to the positions you want in the presentation area. As you start to drag a field, Server highlights the possible places where you can drop it, with an orange border. When you add a group as a row or column, the crosstab expands to include the new group and recalculates all the aggregations.

You can only add group and aggregation fields into the data presentation area.

![Presentation Area](https://devnet.logianalytics.com/hc/article_attachments/9905831820823/va_wndw_prst.gif)

The following describes the Column and Row control boxes:

* ![Column box](https://devnet.logianalytics.com/hc/article_attachments/9905831841303/btn_va_drpgrpclmn.gif)  
   You can add group fields to this control box to become column headers.
* ![Column box](https://devnet.logianalytics.com/hc/article_attachments/9905820151447/btn_va_drpaggclmn.gif)  
   You can add aggregation fields to this control box to become column headers. Server uses the fields to draw axes horizontally at the bottom.
* ![Row box](https://devnet.logianalytics.com/hc/article_attachments/9905820191255/btn_va_drpgrprw.gif)  
   You can add group fields to this control box to become row headers.
* ![Row box](https://devnet.logianalytics.com/hc/article_attachments/9905831926679/btn_va_drpaggrw.gif)  
   You can add aggregation fields to this control box to become row headers. Server uses the fields to draw axes vertically on the left.

## Display Type

Server displays the **Display Type** button at the upper left of the presentation area. It controls the display type of the data values in the data presentation area. You can select from the following display types:

* ![Text Type](https://devnet.logianalytics.com/hc/article_attachments/9905820243479/btn_va_dsplytyp_txt.gif)**Text**  
   Select to display the data values as text. You should add a data field to the label legend ![Label button](https://devnet.logianalytics.com/hc/article_attachments/9905831967255/btn_va_lbl.gif) in the legend section.
* ![Bar Type](https://devnet.logianalytics.com/hc/article_attachments/9905831982615/btn_va_dsplytyp_bar.gif)**Bar**  
   Select to display the data values in bar chart.
* ![Line Type](https://devnet.logianalytics.com/hc/article_attachments/9905820313623/btn_va_dsplytyp_ln.gif)**Line**  
   Select to display the data values in line chart.
* ![Pie Type](https://devnet.logianalytics.com/hc/article_attachments/9905820347287/btn_va_dsplytyp_pie.gif)**Pie**  
   Select to display the data values in pie chart.
* ![Shape Type](https://devnet.logianalytics.com/hc/article_attachments/9905820371863/btn_va_dsplytyp_shp.gif)**Shape**  
   Select to display the data values as shape diagrams.

## Legend

Server displays the legend section on the right of the presentation area. The following introduces all available legend types. Some legend types are specific to certain display types.

* **![Color button](https://devnet.logianalytics.com/hc/article_attachments/9905820408727/btn_va_clr.gif) Color**  
   You can use the color legend to identify the members of a data field by colors.

  You can only bind either of the following data fields with the color legend:

  + One or more group fields.
  + One aggregation field.

  For a single field, Server marks each field member by a distinct color. For multiple group fields, Server marks each combination of the members of the fields by a distinct color.
* **![Label button](https://devnet.logianalytics.com/hc/article_attachments/9905831967255/btn_va_lbl.gif) Label**  
   You can bind the label legend with multiple data fields to provide label text to the members of the data fields.
* **![Size button](https://devnet.logianalytics.com/hc/article_attachments/9905832117527/btn_va_sz.gif) Size**  
   You can bind the size legend with at most one data field to identify the members of the data field by sizes.
* **![Slice button](https://devnet.logianalytics.com/hc/article_attachments/9905832169495/btn_va_angl.gif) Slice**  
   You can bind the slice legend with at most one aggregation field to identify the members of the aggregation field by pie slices. It is available to the Pie display type only.
* **![Shape button](https://devnet.logianalytics.com/hc/article_attachments/9905832196887/btn_va_shp.gif) Shape**  
   You can bind the shape legend with at most one data field to identify the members of the data field by shapes. It is available to the Shape display type only.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741363150231-Starting-a-Visual-Analysis-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741385892759-Performing-Visual-Analysis)
