---
title: "Crosstab Wizard Dialog (Business View Based)"
id: 1500009564862
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564862-Crosstab-Wizard-Dialog-Business-View-Based
updated_at: 2021-07-24T05:55:33Z
---

# Crosstab Wizard Dialog (Business View Based)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564842-Crosstab-Formula-Editor-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585941-Crosstab-Wizard-Dialog-Query-Based-)

# Crosstab Wizard Dialog (Business View Based)

The Crosstab Wizard dialog that is based on business view appears when you do one of the following:

* Select the Crosstab component and select OK in the [Select Component for Library Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009567402-Select-Component-for-Library-Component-Dialog) dialog.
* In the [Select Component for Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009567422-Select-Component-for-Page-Report-Dialog) dialog, check Create Using Business View, select the Crosstab component, and select OK.
* When creating a new report tab in a page report which uses business view as the data resource, in the [Select Component for Page Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009588661-Select-Component-for-Page-Report-Tab-Dialog) dialog, select the Crosstab component and select OK.
* Right-click a crosstab created on a business view and select Crosstab Wizard on the shortcut menu.

The wizard helps you to [create a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component) in a library component or page report, or [modify an existing crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009583901-Modifying-a-Crosstab), and consists of the following screens:

* [Data](#Data)
* [Display](#Display)
* [Filter](#Filter)
* [Layout](#Layout)
* [Style](#Style)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or modifying the crosstab and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Data

Specifies the data source for the crosstab.  [See the screen](javascript:%20void(null)).

![Crosstab Wizard for Web Report or Library Component - Data](https://devnet.logianalytics.com/hc/article_attachments/4404889385239/crstbwzd_dt_wb.gif)

**Resources**

Lists all the business views in the current catalog. Specify the one you want to use.

## Display

Specifies the fields to display in the crosstab. [See the screen](javascript:%20void(null)).

![Crosstab Wizard for Web Report or Library Component - Display](https://devnet.logianalytics.com/hc/article_attachments/4404889385623/crstbwzd_dsply_wb.gif)

**Title**

Specifies the title of the crosstab.

**Resources**

Lists all the available data resources. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the crosstab.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected field to be displayed on the columns of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/4404889377431/btn_addrow.gif)

Adds the selected field to be displayed on the rows of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/4404889377687/btn_addsum.gif)

Adds the selected field on which to create summaries.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected field in the crosstab with the specified field in the Resources box.

**Columns/Rows**

* **Field**  
   Lists the fields that will be displayed on the columns/rows of the crosstab.
* **Label**  
   Specifies the display names for the selected fields. By default these are blank and no names will be created for the fields to label the columns/rows. You can double-click the cells to edit them if required.
* **Color**  
   Specifies the background color of the selected fields.

**Summaries**

* **Field**  
   Lists the fields that you select to create summaries.
* **Aggregate**  
   Specifies the functions used to summarize data of the selected fields. For details about each function, see [Math functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions).
* **Label**  
   Specifies the display names for the selected fields. By default these are blank and no names will be created for the fields to label the summaries. You can double-click the cells to edit them if required.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009585881-Comparison-Function-Dialog) dialog to add a comparison function as an aggregate for the crosstab.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404893939351/btn_sort1.gif)

Specifies in which manner to sort the field values.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893939607/btn_mvup1.gif)

Moves the specified field one step up.

![Mvoe Down button](https://devnet.logianalytics.com/hc/article_attachments/4404893939863/btn_mvdwn1.gif)

Moves the specified field one step down.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the specified field that is not required from the crosstab.

## Filter

Specifies to filter data displayed in the crosstab. This screen is available only when you create a crosstab. [See the screen](javascript:%20void(null)).

![Crosstab Wizard for Web Report or Library Component - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404889386135/crstbwzd_fltr_wb.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Layout

Specifies the layout of the crosstab. [See the screen](javascript:%20void(null)).

![Layout](https://devnet.logianalytics.com/hc/article_attachments/4404893947159/crstbwzd_layout_wb.gif)

For details about options in the screen, refer to [Customizing Crosstab Layout](https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout).

## Style

Specifies the style of the crosstab. [See the screen](javascript:%20void(null)).

![Crosstab Wizard for Web Report or Library Component - Style](https://devnet.logianalytics.com/hc/article_attachments/4404893947415/crstbwzd_sty_wb.gif)

**Style**

Specifies the style of the crosstab.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the crosstab.

**Inherit Style**

Specifies whether to make the crosstab take the style of its parent. This options is available only when the crosstab is inserted in a banded object in a page report.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) dialog to specify page properties. Available only when you create a crosstab in a page report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564842-Crosstab-Formula-Editor-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585941-Crosstab-Wizard-Dialog-Query-Based-)
