---
title: "Using Formulas to Control Object Properties"
id: 5735545031703
section: "Manipulating Data Resources in a Catalog - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties
updated_at: 2022-11-02T07:58:00Z
---

# Using Formulas to Control Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735545091095-Using-User-Defined-Formula-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries)

# Using Formulas to Control Object Properties

One of the most useful features of formulas is that you can use them to control the property values of objects at runtime. This provides you with much more control, enabling you to customize your report and have flexibility to control the way you want the objects to display based on the return values. This topic describes how you can use formulas to control object properties and presents two examples to illustrate the usage of formulas in properties.

This topic contains the following sections:

* [Setting a Formula as the Property Value](#Set)
* [Example 1: Changing the Banded Panel Background Color at Runtime](#Example1)
* [Example 2: Showing a Label on Every Page Except the Last](#Example2)

## Setting a Formula as the Property Value

While editing the property values of an object in the Report Inspector, when you select some properties, you may notice that Designer displays the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) in the value cell (Designer also displays the button next to the value text boxes in some dialog boxes, for example, the Display Type dialog box and some chart format dialog boxes). For object properties of this type, you can use formulas to control their values.

To set a formula as the value of a property, select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and it changes to another button ![X button](https://devnet.logianalytics.com/hc/article_attachments/9898459676183/btn_x.gif). Select the drop-down list in the value cell and Designer displays a formula list.

![Formula List for Property Value](https://devnet.logianalytics.com/hc/article_attachments/9898476745751/fmla_inprpty5.gif)

You can specify the formula you want to use to return value for the property using one of the following methods:

* Select an existing formula from the drop-down list. For a query-based page report, Designer lists the formulas in the current catalog that are valid for the property; for a business view-based report, you can only select from the valid [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Formula) in the current report. Designer then displays the name of the formula prefixed by the "@" symbol as the property value.
* Select **<New Formula...>** to create a formula in the current catalog or a dynamic formula in the current report to use for the property. You should make sure the data type of the new formula's return value is the same as the value type of the property and the formula is valid for the property, for example, you can only use constant level and record level pass one formula for some properties. Otherwise, Designer does not add the new formula as the value of the property, although it still creates the formula in the current catalog or for the current report.
* Select **<Edit Expression...>** to edit an expression using the Formula Editor to control the property value. An expression is actually a formula that is local to this report and is not saved in the catalog. When you specify an expression as the value of a property, Designer displays the expression result in the value cell.
* When the object is in a crosstab in a page or web report, you can also use a [crosstab formula](https://devnet.logianalytics.com/hc/en-us/articles/5735520960151-Using-Crosstab-Formulas) to return value to the property.

However, when you want to use formulas to control properties of the objects whose parent does not relate with a data resource, for example, an object directly contained in the report body, you need to first [bind a dataset to the report body](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#BindDataReport).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* Some properties must be known by Logi Report Engine before a page break, so that it can lay out the object correctly. In a formula or expression, the [PageNumber](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#Page) special field is the switch for setting the page break calculation time. If a formula or expression references PageNumber, the calculation time is after the page break; otherwise, the calculation time is before the page break. For most properties, you can control their values by formula or expression at any time without concerning about the page break.
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

In this formula, we vary the middle hexadecimal digits of the RGB color values. The Red value is fixed at 0x00, the Blue value is fixed at 0x7f. The Green value changes according to the number of records the banded object displays. Record 1 uses color 0x00107f, Record 2 uses 0x00207f, and so on.

Take the following steps to apply the formula to change the background color dynamically.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`..
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports#Page) using a query in Data Source 1 of the catalog.
3. In the design area, select the detail panel (DT) of the banded object.
4. In the Properties sheet of the Report Inspector, select the value cell of the **Background** property, then select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select **MColor** from the drop-down list.
5. Select the **View** tab to preview the report. Designer displays the report somewhat as follows, depending on the report you use.

   ![Using Formula to Control Report Property](https://devnet.logianalytics.com/hc/article_attachments/9898476752919/fmla_inprpty1.gif)

## Example 2: Showing a Label on Every Page Except the Last

Suppose you have a report containing a banded object. You want to display the "Continued on Next Page" label on every page that has another following it. If you insert this label in the page header or page footer, every page including the last page contains the text. You can use formulas to control the visibility of the label to solve the problem.

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
2. Insert Continue1 in the banded header panel (BH), Continue2 in the banded footer panel (BF). To track the calculation, you can insert Continue3 in the banded page footer panel (BPF).
3. Right-click the banded page header panel (BPH) and select **Insert Panel Before** to insert another BPH before the existing BPH.
4. Insert a label with the text "Continued on Next Page" in the newly added BPH panel and format the label as you want.

   ![Banded Object in Design View](https://devnet.logianalytics.com/hc/article_attachments/9898459720215/fmla_inprpty2.gif)
5. Select the **Continued on Next Page** label, then in the Report Inspector, select **Continue3** to control its **Invisible** property.
6. Set the **Record Location** property of the label to **Page Footer**. Continue3 references the Page Number special field so Logi Report Engine executes it as a [page level formula](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#Page) in the order the formula is encountered rather than at the end of a group or the banded object. Here, Continue3 returns value which Logi Report Engine calculates in the banded page footer.
7. Select the **View** tab to preview the banded object. The "Continued on Next Page" label displays on every page except the last page.

   ![Preview Banded Object Result](https://devnet.logianalytics.com/hc/article_attachments/9898476794391/fmla_inprpty3.gif)

   ![Preview Banded Object Result](https://devnet.logianalytics.com/hc/article_attachments/9898476808343/fmla_inprpty4.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735545091095-Using-User-Defined-Formula-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries)
