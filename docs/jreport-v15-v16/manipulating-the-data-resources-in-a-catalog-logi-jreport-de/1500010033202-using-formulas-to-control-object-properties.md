---
title: "Using Formulas to Control Object Properties"
id: 1500010033202
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties
updated_at: 2021-07-24T10:38:13Z
---

# Using Formulas to Control Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033242-User-Defined-Formula-Functions) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries)

# Using Formulas to Control Object Properties

One of the most useful features of formulas is that you can use them to control the property values of objects at runtime. This provides you with much more control, allowing you to customize your report and have flexibility to control the way objects are displayed based on the returned values.

Below is a list of the sections covered in this topic:

* [Setting a Formula as the Property Value](#Set)
* [Using Formulas to Control Showing or Hiding Objects](#Hide)
* [Example: Changing the Banded Panel Background Color at Runtime](#)

## Setting a Formula as the Property Value

While editing the property values of an object in the Report Inspector, when you select on some properties you may notice that a button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) appears on the right of the drop-down arrow in the value cell. The button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) can also be seen next to the value text boxes in some dialogs (for example, the Display Type dialog, some chart format dialogs). For such Report Inspector properties and dialog options, you can use formulas to control their values.

To set a formula as the value of a property, select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and it changes to another button ![X button](https://devnet.logianalytics.com/hc/article_attachments/4404901161879/btn_x.gif). Select the drop-down arrow in the value cell and a drop-down list is displayed. You can then select an existing formula in the list or select the <New Formula...> item to create one to use for the property. For a crosstab in a query based page report, if you have created [crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010063701-Using-Crosstab-Formulas) in the crosstab, they are also available in the drop-down list. You can also select the <New Crosstab Formula...> item in the drop-down list to create one to use in the crosstab as well.

In addition, for properties of this type in the Report Inspector, besides using formulas you can edit expressions via the Formula Editor to control their values by selecting the <Edit Expression> item in the drop-down list. An expression is in fact a formula that is local to this report and is not stored in the catalog. When an expression is specified as the value of a property, the expression result will be displayed in the value cell. It is best to use expressions whenever possible to save space in your catalog; however if the formula is needed by several reports then use a formula rather than an expression.

**Notes****:**

* When you compose a new formula to control a property, make sure the data type of its return value is the same as the value type of the property. Otherwise, the new formula will not be added as the value of the property, although it will still be created in the current catalog or for the current report.
* When using a formula to control the property of a data field such as a DBField, formula, summary, or parameter, you can declare a variable declare statement `<DATATYPE> __currentfield;` to refer to the data field, where *\_\_currentfield* is the reserved variable name and *<DATATYPE>* is the data type of the data field. At runtime *\_\_currentfield* will automatically obtain the value of the data field.

## Using Formulas to Control Showing or Hiding Objects

In a web report or library component, the Invisible property can be controlled by formulas in the Report Inspector. However for any object whose parent doesn't have a business view, for example, a label in the tabular cell of a web report, if you want to use a formula to control its Invisible property, you need to first bind a business view to the web report or library component, then you can create dynamic formulas of Boolean type based on this business view to control the property.

1. Select **Report** > **Bind Data**. The [Bind Data](https://devnet.logianalytics.com/hc/en-us/articles/1500010029802-Bind-Data-Dialog) dialog appears.

   ![Bind Data dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901162135/bddt.gif)
2. Select a business view in the current catalog.
3. Select **OK** to bind the business view to the web report or library component.
4. Select any blank area in the report body. The business view bound to the web report or library component is displayed in the Data panel.
5. Expand the **Dynamic Resources** > **Formulas** node, select **<New Formula…>**, then create the formula as required.
6. Find the Invisible property of the desired object in the Report Inspector, select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) in the value cell and select the drop-down arrow. The formula you just created is listed in the drop-down list. Select it to control the property value. You can also select the <New Formula> item from the drop-down list to create a new one to use.

> Then at runtime, whether the object is shown or hidden will be determined by the return value of the formula. A return value of true will hide the object.

**Tip**: The Suppress property of banded objects and banded panels in web reports can also be controlled by formulas in the Report Inspector.

## Example: Changing the Banded Panel Background Color at Runtime

This example uses the formula MColor to control the Background property of the detail panel of a banded report at runtime. You can find this formula in Data Source 1 of the catalog SampleReports. The following is the content of the formula:

`String sc = "" + (@MColor_RecordNumber *10 );  
Number idx = InStr(".",sc);  
if(idx != -1)  
    sc = Left(sc, idx);  
if(Length(sc) < 2)  
    sc = "0" + sc;  
String s = "0x00" + sc + "7f";  
return s`

In this example we will vary the middle hexadecimal digits of the RGB color values. The Red value is fixed at 0x00, the Blue value is fixed at 0x7f. The Green value will change according to the number of records displayed. Record 1 will use color 0x00107f, Record 2 will use 0x00207f, and so on.

Take the following steps:

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) based on a query stored in Data Source 1 of the catalog.
3. In the design area, select the detail panel (DT) of the banded object.
4. In the Properties sheet of the Report Inspector, select the value cell of the property Background, and select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif). From the drop-down list, select **MColor**.
5. Select the **View** tab to view the report. The report will be shown somewhat as follows, depending on the report you use.

   ![Using Formula to Control Report Property](https://devnet.logianalytics.com/hc/article_attachments/4404901162391/fmla_inprpty.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033242-User-Defined-Formula-Functions) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries)
