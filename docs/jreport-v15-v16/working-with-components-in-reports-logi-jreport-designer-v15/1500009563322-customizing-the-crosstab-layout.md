---
title: "Customizing the Crosstab Layout"
id: 1500009563322
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout
updated_at: 2021-07-24T05:56:02Z
---

# Customizing the Crosstab Layout

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583901-Modifying-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583841-Defining-Comparison-Functions-in-a-Crosstab)

# Customizing the Crosstab Layout

When you create or edit a crosstab, you can use the Layout screen of the crosstab wizard to customize the layout of the crosstab according to specific data displayed in the crosstab so as to make the data more intuitive and readable.

![Crosstab Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404893946647/crstbwzd_layout.gif)

The following are properties that are provided in the Layout screen:

**Aggregate**

Specifies properties of the aggregate fields.

* **Vertical Layout**  
   If selected, the aggregate fields will be arranged vertically.
  + **Number of Rows**  
     Specifies the number of rows to be displayed in the crosstab. By default, it is -1, which means that there is only one column with which to arrange the aggregate fields vertically; if it is set to 1, that means there will be only one row to arrange the aggregate fields horizontally; if it is set to a number larger than 1, that means there will be this number of aggregate rows to arrange all the aggregate fields horizontally; if this number is larger than the number of aggregate fields in the crosstab, it will be treated as -1.
* **Horizontal Layout**  
   If selected, the aggregate fields will be arranged horizontally.
  Usually when there are multiple aggregates listed the horizontal layout is a more natural layout for users to view data as it looks more like a table.
  + **Number of Columns**   
     Specifies the number of columns to be displayed in the crosstab. By default, it is -1, which means that there is only one row with which to arrange the aggregate fields horizontally; if it is set to 1, that means there will be only one column to arrange the aggregate fields vertically; if it is set to a number larger than 1, that means there will be this number of aggregate columns to arrange all the aggregate fields vertically; if this number is 0 or it is larger than the number of aggregate fields in the crosstab, it will be treated as -1.
* **Repeat Aggregate**  
   Specifies whether or not to repeat the crosstab for different aggregate fields. If checked, the value set for Number of Rows or Number of Columns will be ignored.   

  Assume that you have created a crosstab on the query WorldWideSales in the catalog file SampleReports.cat as follows: added Product ID as the column field, added Country as the row field, added Quantity and Discount as the aggregate fields and specified the functions as Sum, and applied the style Classic to the crosstab.

  + If checked, one cell will contain only one aggregate field value, while for the other aggregate fields, the crosstab will repeat. The crosstab will be shown as follows:

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404893987479/dlg_crstab1.gif)
  + If unchecked, one crosstab cell accommodates the values of all aggregate fields. The crosstab will be shown as follows:

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889410967/dlg_crstab2.gif)
* **Outside Aggregate Title**  
   Specifies whether to place the summary label on the leftmost column when the aggregate layout is vertical, or on the topmost row of the crosstab when the aggregate layout is horizontal.

**Suppress Row Grand Totals**

Specifies whether or not to show the grand totals of row groups. If required, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) to open the [Suppress Row Grand Totals](https://devnet.logianalytics.com/hc/en-us/articles/1500009588881-Suppress-Row-Grand-Totals-Dialog) dialog to specify which grand totals of the row groups will be suppressed and which will be shown.

**Suppress Column Grand Totals**

Specifies whether or not to show the grand totals of column groups. If required, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) to open the [Suppress Column Grand Totals](https://devnet.logianalytics.com/hc/en-us/articles/1500009567602-Suppress-Column-Grand-Totals-Dialog) dialog to specify which grand totals of the column groups will be suppressed and which will be shown.

**Suppress Row Subtotal**

Specifies whether or not to show the subtotals of rows. If required, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) to open the [Suppress Row Subtotal](https://devnet.logianalytics.com/hc/en-us/articles/1500009588901-Suppress-Row-Subtotal-Dialog) dialog to specify which subtotals of the rows will be suppressed and which will be shown.

**Suppress Column Subtotal**

Specifies whether or not to show the subtotals of columns. If required, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) to open the [Suppress Column Subtotal](https://devnet.logianalytics.com/hc/en-us/articles/1500009567622-Suppress-Column-Subtotal-Dialog) dialog to specify which subtotals of the columns will be suppressed and which will be shown.

**Repeat Column Header**

Specifies whether or not the header of columns will appear on every page, if a crosstab spans more than one page.

**Use Table Style**

Specifies whether to add headers to the Total rows and columns.

**Column Totals On**

Specifies the position of total columns on the left or right of the aggregates.

**Row Totals On**

Specifies the position of total rows on the top or bottom of the aggregates.

Besides using the wizard, you can also customize the layout of a crosstab in a [page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009591341-Properties-of-Crosstab-in-Page-Report#Property), [web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592021-Properties-of-Crosstab-in-Web-Report#Property) or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009590721-Properties-of-Crosstab-in-Library-Component#Property) by setting properties in the Report Inspector.

## Example of customizing the crosstab layout

Suppose you want to have a crosstab to show the total cost, quantity and sales of different product categories and types for different customers in China and Germany, you can create it as follows:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. [Create a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Create).
3. [Insert a crosstab in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009583881-Inserting-a-Crosstab#Web) as follows: use WorldWideSalesBV in Data Source 1, show Product Type and Category in the Products table on the columns, Country and Customer Name in the Customers table on the rows, Total Quantity, Total Cost and Total Sales as the aggregate fields, specify the field names as the display names to label the rows, columns and summaries, and add a filter condition *@Country = China Or @Country = Germany*.

   ![Create Crosstab wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404893987735/cmpnt_crstb_cstmz1.gif)
4. Save the report and select **View** > **Preview As** > **Web Report Result** to preview the report and it appears as follows:

   ![Cross tab Web Report Result](https://devnet.logianalytics.com/hc/article_attachments/4404889411351/cmpnt_crstb_cstmz2.gif)
5. Close the report and return to the **Design** tab in Logi JReport Designer.
6. Right-click the crosstab and select **Crosstab Wizard** from the shortcut menu.
7. In the Crosstab Wizard, select **Layout** to switch to the screen.
8. Check **Repeat Aggregate** to show the aggregate field values for each customer in their own cells.
9. Check **Horizontal Layout**  to arrange the aggregate fields horizontally and specify the option Number of Columns to **2**.
10. Select **left** from the Column Totals On drop-down list and **top** from the Row Totals On drop-down list.

    It is better to uncheck Outside Aggregate Title, as the labels of the aggregate fields would be far from their values. It is also suggested that you uncheck Use Table Style, otherwise the row and column headers will be repeated too much. As for suppress related properties, you can specify them as required. You can decide which part of the aggregate field values to see. Here, we keep the default settings of these properties.
11. Save the report and preview it again. The crosstab now appears as follows:

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404893988119/cmpnt_crstb_cstmz3.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583901-Modifying-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583841-Defining-Comparison-Functions-in-a-Crosstab)
