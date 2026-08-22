---
title: "Using Formulas to Control Object Properties"
id: 1500010061002
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties
updated_at: 2021-07-23T19:16:13Z
---

# Using Formulas to Control Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099441-Using-User-Defined-Formula-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries)

# Using Formulas to Control Object Properties

One of the most useful features of formulas is that you can use them to control the property values of objects at runtime. This provides you with much more control, enabling you to customize your report and have flexibility to control the way you want the objects to display based on the return values. This topic describes how you can use formulas to control object properties, and presents an example about using a formula to specify the background color of a banded panel dynamically.

This topic contains the following sections:

* [Setting a Formula as the Property Value](#Set)
* [Example: Changing the Banded Panel Background Color at Runtime](#)

## Setting a Formula as the Property Value

While editing the property values of an object in the Report Inspector, when you select on some properties, you may notice that the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) appears on the right of the drop-down arrow in the value cell. You can also get this button next to the value text boxes in some dialog boxes (for example, the Display Type dialog box and some chart format dialog boxes). For object properties and dialog box options of this type, you can use formulas to control their values.

To set a formula as the value of a property, select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) and it changes to another button ![X button](https://devnet.logianalytics.com/hc/article_attachments/4404848471319/btn_x.gif). Select the drop-down arrow in the value cell and Designer displays a drop-down list. You can then select an existing formula from the list or select the **<New Formula...>** item to create a formula to use for the property. For a crosstab in a query-based page report, if you have created [crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010094701-Using-Crosstab-Formulas) in the crosstab, they are also available in the drop-down list. You can select the **<New Crosstab Formula...>** item in the drop-down list to create a crosstab formula to use in the crosstab as well.

In addition, for properties of this type in the Report Inspector, besides using formulas, you can edit expressions via the Formula Editor to control their values by selecting the **<Edit Expression>** item in the drop-down list. An expression is in fact a formula that is local to this report and is not stored in the catalog. When you specify an expression as the value of a property, Designer displays the expression result in the value cell. It is best practice to use expressions whenever possible to save space in your catalog; however, if you need the formula in several reports, use a formula rather than an expression.

However, in a web report, library component, or business view-based page report, if you want to use formulas to control properties of the objects whose parent doesn't have a business view, for example, a label in the tabular cell of a web report, you need to first [bind a business view to the report body](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#BindData), then you can create [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) based on this business view to control the properties. Currently, you can only use formulas to control the Invisible and Suppress properties in web reports and library components.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* When you compose a new formula to control a property, make sure the data type of its return value is the same as the value type of the property; otherwise, Designer does not add the new formula as the value of the property, although it still creates the formula in the current catalog or for the current report.
* When using a formula to control the property of a data field such as a DBField, formula, summary, or parameter, you can declare a variable "declare" statement `<DATATYPE> __currentfield;` to refer to the data field, where *\_\_currentfield* is the reserved variable name and *<DATATYPE>* is the data type of the data field. At runtime, *\_\_currentfield* automatically obtains the value of the data field.

## Example: Changing the Banded Panel Background Color at Runtime

This example uses the formula "MColor" to control the Background property of the detail panel of a banded report at runtime. You can find this formula in Data Source 1 of the SampleReports catalog. The following is the content of the formula:

`String sc = "" + (@MColor_RecordNumber *10 );  
Number idx = InStr(".",sc);  
if(idx != -1)  
    sc = Left(sc, idx);  
if(Length(sc) < 2)  
    sc = "0" + sc;  
String s = "0x00" + sc + "7f";  
return s`

In this formula, we vary the middle hexadecimal digits of the RGB color values. The Red value is fixed at 0x00, the Blue value is fixed at 0x7f. The Green value changes according to the number of records displayed. Record 1 uses color 0x00107f, Record 2 uses 0x00207f, and so on.

Take the following steps to apply the formula to change the background color dynamically:

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`..
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) based on a query stored in Data Source 1 of the catalog.
3. In the design area, select the detail panel (DT) of the banded object.
4. In the Properties sheet of the Report Inspector, select the value cell of the property **Background**, and select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif). From the drop-down list, select **MColor**.
5. Select the **View** tab to preview the report. Designer displays the report somewhat as follows, depending on the report you use.

   ![Using Formula to Control Report Property](https://devnet.logianalytics.com/hc/article_attachments/4404856870807/fmla_inprpty.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099441-Using-User-Defined-Formula-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries)
