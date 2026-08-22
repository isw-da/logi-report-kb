---
title: "Lesson 6: Creating a Crosstab Report"
id: 28897651782925
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897651782925-Lesson-6-Creating-a-Crosstab-Report
updated_at: 2026-02-26T02:10:42Z
source_host: docs-report.zendesk.com
---
# Lesson 6: Creating a Crosstab Report

A report with quantities of different products that are sold in different regions and their sales totals is needed. You are required to create a crosstab that can clearly represent the necessary information, which enables the sales manager to easily compare the sales of different products in different regions.

Here is the sketch that is given to you:

Follow these tasks to create the report:

- Task 1: Create the Crosstab

- Task 2: Format the Crosstab

- Task 3: Change the Page Layout

- Task 4: Save the Report Style as .CSS

## 
Task 1: Create the Crosstab

Before taking this task, make sure you have enabled the "Insert field name label with field" option in the Options dialog box as described at the last step of Lesson 3; otherwise, Designer does not insert the name labels together with the fields when you add fields to the crosstab.

- In Designer, navigate to File > New > Page Report. Be sure that JinfonetGourmetJava.cat is the current catalog because this is the catalog we use in this track. For information about specifying this catalog, see Task 1, Steps 3 and 4 of Lesson 1.    

- In the Select Component for Page Report dialog box, select Crosstab and select OK.
    

- In the Data screen of the Crosstab Wizard dialog box, select <New Query...> in the Queries node of Data Source 1,  type ProductSalesAnalysis in the Enter Query Name dialog box and select OK.

- In the Add Tables/Views/Queries dialog box, expand the JDBC connection node and then the Tables node, then select the Customers, Orders, Orders Detail, and Products tables and select Add to add them to the query. Select OK to close the dialog box.

- In the Query Editor dialog box, Designer joins the tables together automatically based on the auto join criteria. Select all the columns in the Orders Detail table. For the Customers table, select the following columns: Customer Name, Customers_City, Customers_State, Customers_Country, Customers_Territory, and Customers_Region, and for the Products table, the following columns:  Products_Product ID, Product Name, Category, Product Type Name, and Price. 
    

You may notice that here we do not select any columns in the Orders table, that is because in this report, columns in this table are not needed but we need this table to create joins between tables in the query.

- Select OK to create the query.

- Select Next in the Crosstab Wizard dialog box.

- In the Display screen, drag Category from the Resources box to the Columns box, drag Customers_Country to the Rows box, and drag  Quantity and  the formula Total to the Summaries box one by one, then double-click in the Aggregate text box and select  Sum from the drop-down list to change the aggregate function of the two summaries.
    

- Select  Style on the screen navigation bar to switch to the screen and select the Basic style to apply to the crosstab.

- Select Finish to create the crosstab report. 

## 
Task 2: Format the Crosstab

In this task, we format the crosstab to make it look more professional.

- Right-click on the crosstab and navigate to Position > Absolute on the shortcut menu, then drag it to the following position:
      

By setting the Position property of an object to "absolute", Designer locates the object at the position specified by drag-and-drop editing or by setting its X and Y coordinate property values.

- Drag the Label icon  from the Components panel to add three labels in the report, then double-click each label to edit the text respectively to Product Sales Analysis, Units, and  Sales.

- Resize and adjust the crosstab and the three labels to place them as follows:
    

Next, we edit properties of the crosstab report objects in the Report Inspector to improve the appearance of the report. 

- Select the Units label and edit its Bold property to true, Background property to Gray and Foreground property to White.
    

- Select the Sales label and edit its Bold property to true, Background property to 0x99ccff and Foreground property to White. 

- Select the field on the column header (Category field) and edit its Background property to 0x99ccff and Forground to White.
    

- 
Select the two Total cells, the field on the row header (Customers_Country field), and the four ##### cells in the crosstab, then specify their Foreground property to Gray; select the four ##### cells and change their Format property to #,###.
    

- Select the four #,###.00 cells, change their Foreground property to 0x99ccff, Bold property to true, and Format property to $#,###.00.
    

- Select the Product Sales Analysis label, set its Bold property to true, Font Size property to 18, and Foreground property to Red, then resize it to display its text completely.  
  

- On the report tab bar, right-click the report tab and select Rename to rename it to ProductSales.
    

- Navigate to File > Save to save the report as ProductSalesAnalysis.cls.
  

- Select the View tab to preview the crosstab. 

 If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the JinfonetGourmetJava.cat catalog file in <install_root>\Demo\Reports\TutorialReports.    

## 
Task 3: Change the Page Layout

When previewing the report, we can see that Designer displays the crosstab in two pages. However, for a crosstab, such a layout is not convenient for analyzing data. Designer provides the Page Mode feature, which you can apply to specify how to layout the report pages: in pagination mode or continuous mode. When a report is in continuous mode, Designer lays out the whole report in a single page.

- Clear Page Layout in the View ribbon.

- Select the View tab to view the report again. Now, Designer displays the crosstab in a single page. We can scroll to have a complete view of the crosstab.

For a crosstab component, when it is in continuous page mode, you can further set another two properties to determine how many rows and columns we would like to view.

- Select the crosstab, and set its Items per Row Block and Items per Column Block property values to 3 in the Report Inspector.

- View the report. Designer now displays only three items in the row and column blocks.
    

- Select Page Layout in the View ribbon to switch back to pagination mode. The two properties cannot take effect now.

- Navigate to File > Save to save the report again. 

## 
Task 4: Save the Report Style as .CSS

After formatting the report step by step in the Task 2, we can save the properties into a CSS style file, which we can apply  to other crosstab reports directly.

- Select the crosstab, right-click and select Save Style from the shortcut menu.

- Keep the default settings in the New CSS Style dialog box and select OK.
    

- In the Save CSS As dialog box, type Crosstab.css in the File Name text box, then select Save to save the file to the default directory <install_root>\style.
    Designer displays the CSS Style Definition for CrosstabObject dialog box.

- Add all the properties of the crosstab from the All Properties box to the Selected Properties box by selecting Add All.

- Select Save to save these properties in Crosstab.css.

Now, we have saved the style of the crosstab report as a CSS file. We can apply properties in the file to the corresponding components of other reports directly by selecting the CSS file from the <Import CSS File...> drop-down list in the Home ribbon in Designer.
