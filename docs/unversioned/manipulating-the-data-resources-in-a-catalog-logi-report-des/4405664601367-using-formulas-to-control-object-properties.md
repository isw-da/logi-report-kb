---
title: "Using Formulas to Control Object Properties"
id: 4405664601367
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties
updated_at: 2024-03-25T15:24:31Z
---

# Using Formulas to Control Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661765527-Using-User-Defined-Formula-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries)

# Using Formulas to Control Object Properties

One of the most useful features of formulas is that you can use them to control the property values of objects at runtime. This provides you with much more control, enabling you to customize your report and have flexibility to control the way you want the objects to display based on the return values. This topic describes how you can use formulas to control object properties, and presents an example about using a formula to specify the background color of a banded panel dynamically.

This topic contains the following sections:

* [Setting a Formula as the Property Value](#Set)
* [Example 1: Changing the Banded Panel Background Color at Runtime](#Example1)
* [Example 2: Showing a Label on Every Page Except the Last](#Example2)

## Setting a Formula as the Property Value

While editing the property values of an object in the Report Inspector, when you select some properties, you may notice that Designer displays the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) in their value cell (Designer also displays this button next to the value text boxes in some dialog boxes, for example, the Display Type dialog box and some chart format dialog boxes). For object properties and dialog box options of this type, you can use formulas to control their values.

To set a formula as the value of a property, select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) and it changes to another button ![X button](https://devnet.logianalytics.com/hc/article_attachments/4420556117783/btn_x.gif). Select the drop-down button in the value cell and Designer displays a drop-down list. You can then select an existing formula from the list or select **<New Formula...>** to create a formula to return value to the property. For a crosstab in a query-based page report, if you have created [crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405664393751-Using-Crosstab-Formulas) in the crosstab, they are also available in the drop-down list. You can select **<New Crosstab Formula...>** in the drop-down list to create a crosstab formula to use in the crosstab as well. However, when you want to use formulas to control properties of the objects whose parent does not relate with a data resource, for example, an object directly contained in the report body, you need to first [bind data to the report body](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#BindData).

In addition, for most properties of this type in the Report Inspector, besides using formulas, you can edit expressions using the Formula Editor to control their values. An expression is actually a formula that is local to this report and is not stored in the catalog. When you specify an expression as the value of a property, Designer displays the expression result in the value cell. It is best practice to use expressions whenever possible to save space in your catalog; however, if you need the formula in several reports, use a formula rather than an expression.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* When you compose a new formula to control a property, make sure the data type of its return value is the same as the value type of the property; otherwise, Designer does not add the new formula as the value of the property, although it still creates the formula in the current catalog or for the current report.
* When using a formula to control the property of a data field such as a DBField, formula, summary, or parameter, you can declare a variable "declare" statement `<DATATYPE> __currentfield;` to refer to the data field, where *\_\_currentfield* is the reserved variable name and *<DATATYPE>* is the data type of the data field. At runtime, *\_\_currentfield* automatically obtains the value of the data field.

## Example 1: Changing the Banded Panel Background Color at Runtime

This example uses the formula "MColor" to control the Background property of the detail panel of a banded report at runtime. You can find this formula in Data Source 1 of the SampleReports catalog.

The formula expression is:

`String sc = "" + (@MColor_RecordNumber *10 );  
Number idx = InStr(".",sc);  
if(idx != -1)  
    sc = Left(sc, idx);  
if(Length(sc) < 2)  
    sc = "0" + sc;  
String s = "0x00" + sc + "7f";  
return s`

In this formula, we vary the middle hexadecimal digits of the RGB color values. The Red value is fixed at 0x00, the Blue value is fixed at 0x7f. The Green value changes according to the number of records displayed. Record 1 uses color 0x00107f, Record 2 uses 0x00207f, and so on.

Take the following steps to apply the formula to change the background color dynamically.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`..
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#Page) using a query stored in Data Source 1 of the catalog.
3. In the design area, select the detail panel (DT) of the banded object.
4. In the Properties sheet of the Report Inspector, select the value cell of the property **Background**, and select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif). From the drop-down list, select **MColor**.
5. Select the **View** tab to preview the report. Designer displays the report somewhat as follows, depending on the report you use.

   ![Using Formula to Control Report Property](https://devnet.logianalytics.com/hc/article_attachments/4420556118039/fmla_inprpty1.gif)

## Example 2: Showing a Label on Every Page Except the Last

Suppose you have a report containing a banded object. You want to display the label "Continued on Next Page" on every page that has another following it. If you insert this label in the page header or page footer, every page including the last page contains the text. You can use formulas to control the visibility of the label to solve the problem.

1. Create three formulas.

   **Continue1**:  
   `global boolean j=true;  
   j=false;`

   **Continue2**:  
   `PageNumber;  
   j=true;`

   **Continue3**:  
   `PageNumber;  
   return j;`
2. Insert Continue1 into the banded header panel (BH), Continue2 into the banded footer panel (BF). To track the calculation, you can insert Continue3 into the banded page footer panel (BPF).
3. Insert another banded page header panel before the existing BPH.
4. Insert a label with the text "Continued on Next Page" in the newly added BPH panel and format the label as you want.

   ![Banded Object in Design View](https://devnet.logianalytics.com/hc/article_attachments/4420556118423/fmla_inprpty2.gif)
5. Select the **Continued on Next Page** label, then in the Report Inspector, select **Continue3** to control its **Invisible** property.
6. Set the **Record Location** property of the label to **Page Footer**, so that Continue3 returns value which is calculated in the banded page footer.

   Continue3 contains "PageNumber" so Logi Report Engine executes it as a page level formula in the order the formula is encountered rather than at the end of a group or the banded object.
7. Select the **View** tab to preview the banded object. The label "Continued on Next Page" displays on every page except the last one.

   ![Preview Banded Object Result](https://devnet.logianalytics.com/hc/article_attachments/4420556118807/fmla_inprpty3.gif)

   ![Preview Banded Object Result](https://devnet.logianalytics.com/hc/article_attachments/4420550851863/fmla_inprpty4.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661765527-Using-User-Defined-Formula-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries)
