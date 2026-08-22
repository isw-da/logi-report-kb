---
title: "Using Formulas to Control Object Properties"
id: 1500009568362
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties
updated_at: 2021-07-24T05:54:36Z
---

# Using Formulas to Control Object Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568342-DBArray-in-Formulas)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568382-Summaries)

# Using Formulas to Control Object Properties

One of the most useful features that formulas have is that you can use formulas to control the property values of objects at runtime. This provides you much more control, allowing you to customize your report and have flexibility to control the way objects are displayed based on the data values. However this feature is not supported in page reports that are created on business views, and in web reports and library components, only the Invisible property can be controlled by formulas.

Below is a list of the sections covered in this topic:

> * [How to Set a Dormula as the Property Value](#Set)
> * [Using Formulas to Control Showing or Hiding Objects](#Hide)
> * [Example: Changing the Banded Panel Background Color at Runtime](#)

## How to Set a Formula as the Property Value

While editing the property values of an object in the Report Inspector, when you select on some properties you may notice that a button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) appears on the right of the drop-down arrow in the value cell, and when you select this button, it will change to be another button ![X button](https://devnet.logianalytics.com/hc/article_attachments/4404889308055/btn_x.gif). Then when you select the drop-down arrow in the value cell, a drop-down list is displayed. If you select one item in the list, the property will be controlled according to the return value of the formula. You can also find the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) next to the value text boxes of some options in certain dialogs (for example, the Display Type dialog). For those options, you can use formulas to control their values as well.

Usually when you open the drop-down list of this kind of property or option, there is no formula to be selected directly unless:

* **For a query based page report**  
   You have created some formulas in the same catalog data source as the query on which the page report is built. You can also select the <New Formula...> item in the drop-down list to create one as required. For a crosstab in a query based page report, if you have created some [crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009583861-Using-Crosstab-Formulas) in the crosstab, they are also available in the drop-down list. You can select the <New Crosstab Formula...> item in the drop-down list to create one to use in the crosstab as well.
* **For a web report or library component**   
   You have created some [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) in the corresponding business view.

For properties of this kind in the Report Inspector, in addition to using formulas you can edit expressions via the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586941-Formula-Editor-Dialog) to control their values by selecting the <Edit Expression> item in the drop-down list. An expression is in fact a formula that is local to this report and is not stored in the catalog. When an expression is specified as the value of a property, the expression result will be displayed in the value cell. It is best to use expressions whenever possible to save space in your catalog; however, if the formula is needed by several reports then use a formula rather than an expression.

**Note:** When you compose a new formula to control a property, make sure the data type of its return value is the same as the value type of the property. Otherwise, the new formula will not be added as value of the property, although it will still be created in the current catalog data source/business view.

## Using Formulas to Control Showing or Hiding Objects

In a web report or library component, only the Invisible property can be controlled by formulas. However for any object whose parent doesn't have a dataset, for example, a label in the tabular cell of a web report, if you want to use a formula to control its Invisible property, you need to first bind a business view to the web report or library component, then you can create dynamic formulas of Boolean type based on this business view to control the property.

1. Select **Report** > **Bind Data**. The [Bind Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009564602-Bind-Data-Dialog) dialog appears.

   ![Bind Data dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893837719/bddt.gif)
2. Select a business view in the current catalog.
3. Select **OK** to bind the business view to the web report or library component.
4. Select any blank area in the report body. The business view bound to the web report or library component is displayed in the Data panel.
5. Expand the **Dynamic Resources** > **Formulas** node, select **<New Formula…>**, then create the formula as required.
6. Find the Invisible property of the desired object in the Report Inspector, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) in the value cell and select the drop-down arrow. The formula you just created is listed in the drop-down list. Select it to control the property value. You can also select the **<New Formula>** item from the drop-down list to create a new one to use.

> Then at runtime, whether the object is shown or hidden will be determined by the return value of the formula. A return value of true will hide the component.

## Example: Changing the Banded Panel Background Color at Runtime

This example uses the formula MColor to control the Background property of the detail panel of a banded report at runtime. You can find this formula in Data Source 1 of the catalog SampleReports. The following is the content of the formula:

|  |
| --- |
| ``` String sc = "" + (@MColor_RecordNumber *10 ); Number idx = InStr(".",sc); if(idx != -1)           sc = Left(sc, idx); if(Length(sc) < 2)           sc = "0" + sc; String s = "0x00" + sc + "7f"; return s ``` |

In this example we will vary the middle hexadecimal digits of the RGB color values. The Red value is fixed at 0x00, the Blue value is fixed at 0x7f. The Green value will change according to the number of records displayed. Record 1 will use color 0x00107f, Record 2 will use 0x00207f, and so on.

Take the following steps:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on a query stored in Data Source 1 of the catalog.
3. In the design area, select the detail panel (DP) of the banded object.
4. In the Properties sheet of the Report Inspector, select the value cell of the property Background, and select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif). From the drop-down list, select **MColor**.
5. Select the **View** tab to view the report. The report will be shown somewhat as follows, depending on the report you use.

   ![View Report](https://devnet.logianalytics.com/hc/article_attachments/4404889308311/formula_inprpty.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568342-DBArray-in-Formulas)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568382-Summaries)
