---
title: "Track 3: Creating Web Reports"
id: 28897690741517
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897690741517-Track-3-Creating-Web-Reports
updated_at: 2026-02-26T02:10:42Z
source_host: docs-report.zendesk.com
---
# Track 3: Creating Web Reports

Report provides the web reporting solution that is aimed at easier and faster report creation and design, faster report execution, easier customization, and better presentation style using the newest Web technology. Web reports are viewed using a new interactive viewer called Web Report Studio, which provides a much nicer end user experience with many powerful features for interfacing with a report such as changing parameters without rerunning the report.

In Designer, report developers can create, open, and edit web reports; web reports end users create on Server can also be downloaded to Designer for further editing.

In this track, you have been asked to create a web report as the role of a report developer, based on the business view WorldWideSalesBV created in the previous track. The report should show each product's sales information, including order ID, order date, quantity, unit price, discount, and the total sales for each order. In order for end users to get sales information within a specific range conveniently, such as country or product name, you also need to add filter controls for dynamically filtering the data according to their requirements. 

This track contains the following tasks:

- Task 1: Create the Initial Report

- Task 2: Improve the Report Layout

- Task 3: Format the Report Components

- Task 4: Preview the Report in Web Report Studio

 To perform this track, you should have a Live license for Designer. If you need more information, contact Customer Service.
    

## 
Task 1: Create the Initial Report

- Select Logi Report Designer in the Logi Report folder on the Start menu to open Designer.
   

- Designer displays the main window and shows the Start Page by default. Close the Start Page.

- Navigate to File > Open Catalog.

- In the Open Catalog File dialog box, browse to select the JinfonetGourmetJava.cat catalog file in <install_root>\Demo\Reports\JinfonetGourmetJava, then select Open.

- Select Yes in the Warning dialog box. Designer displays the Catalog Manager. Close it because we do not use it in this lesson.    

- Navigate to File > New > Web Report. Designer creates a blank web report with a one-cell tabular.  

- Right-click the report body, select Split from the shortcut menu.
    

- In the Split Cell dialog box, set both numbers to 2, then select OK.

The report body is now hosted by four tabular cells. We want to put the filter controls in the left cells, and place a chart and a table in the right cells. First we create a chart to demonstrate the total sales of each product.

- Select the right cell in the first tabular row, then navigate to Insert > Chart. Designer displays the Create Chart dialog box.

- In the Data screen, select WorldWideSalesBV. Select Next.

- In the Type screen, keep the default chart type Clustered Bar 2-D and select Next.

- In the Display Screen, drag Product Name from the Resources box to the X-Axis box and Total Sales to the Bar Length box.
     

- Select Style on the screen navigation bar to switch to the screen, select Classic as the chart style.

- Select Finish to create the chart.

Next, we create a table to display the sales information just below the chart. 

- Select the right cell in the second tabular row, then navigate to Insert >  Table.

- In the Table Type dialog box, keep the default selection and select OK. Designer displays the Create Table dialog box.

- In the Data screen, select WorldWideSalesBV and select Next. You can also select More Option and select the dataset the chart applies from the existing dataset list to share the same dataset between both components.

- In the Display Screen, drag the following objects from the Resources box to display in the table one by one: Order ID, Order Date, Quantity, Unit Price, Discount, and Total. Select Next.
    

- In the Group screen, add Country and Product Name as the group-by fields (Country is the higher group level). 

- Select Style to switch to the screen, then select Classic as the table style too. 

- Select Finish to create the table.

Next, we add two Text List filter controls to the report, so that at runtime end users can select one or more values in the filter controls to dynamically filter the chart and table. 

- Select the tabular cell on the left of the chart, navigate to Insert > Web Controls > Filter Control.

- In the Insert Filter Control dialog box, keep the default filter control type in the Control Type drop-down list, select the group object Country from the Select Fields drop-down list, select outside the field drop-down list in the dialog box to finish selecting field, then select OK to insert the filter control.
    

- Select the tabular cell on the left of the table and insert another filter control in the cell, based on the field Product Name using the same way.

We also want to add a navigation control to help end users deal with the filter applying status in both filter controls in the report: go back to the previous filter applying status, go forward to the next, or clear all the filter applying histories. We place the navigation control above the chart in the report.

- Right-click the blank area in the cell containing the chart and select Insert Row Above from the shortcut menu.

- Select the right cell in the newly added tabular row, then navigate to Insert > Web Controls > Navigation Control. 

Lastly, we insert an image to show the title of the report in the report page header panel.

- Select the blank cell above the navigation control, then navigate to Insert > Image.

- In the Select an Image dialog box, double-click ProductSalesHeader.gif to insert the image.
			By now, we have added all the components we need in separate tabular cells.

## 
Task 2: Improve the Report Layout 

In this task, we make some changes to the position and size of the components to improve the report layout. 

- Select Tabular Cell 1 (the cell holding the image) in the report structure tree in the Report Inspector and edit its Height property to 0.9.
			

- Change the height of the image to make it fully occupy the cell it is in. 

- Select the tabular cell holding the navigation control, then drag the bottom border of the cell to make its height  fit the height of the navigation control.

- Select the tabular cell that contains the table and drag its left border to widen the cell.

- Select the table and drag its right border to fully display all columns in it.

- Resize the chart to make it fully occupy the cell it is in.

The cell above the Country filter control is empty, so next we merge it with the cell that holds the Country filter control. 

- Select the empty cell and the cell containing the Country filter control, then right-click and select Merge from the shortcut menu.

- Resize the two filter controls to make them fully occupy the cells they are in.
    The report shows as follows in design view now:

## 
Task 3: Format the Report Components 

To improve the report appearance, we need to further format the components in the report. Let's start with the chart.

- Right-click on the chart and select Hide Legend from the shortcut menu.

- Right-click on any bar, then navigate to Format Axes > Format Value (Y) Axis on the shortcut menu. 

- In the Format Value (Y) Axis dialog box, go to the Format tab, select Number in the Category box, select $#,##0 in the Format box, then select Add to add the format to the Stack box. Select OK to exit the dialog box.
     

Next, we format the table by editing its object properties in the Report Inspector. 

- In the report structure tree of the Report Inspector, select the Table Header node and edit its Background property to 0x7da1d1.
    

- Select the Table Group Header node and set its Background property to 0xd9d9d9, then select Table Group Header 1 and set its Background property to 0xeeeeee.

- In the table, select the two group-by fields in the group headers (GH), resize them horizontally to make sure the country and product names do not get truncated, then in the Report Inspector, set the Foreground property of the two fields to 0x7da1d1.

- Select the Order Date DBField in the detail row (TD), then change its Format property to MM/dd/yyyy in the Report Inspector.

- Select the Unit Price and Total DBFields in the detail row and edit their Format property to $#,###.00.

-  Select the Discount DBField in the detail row, then type #,##0.00 in the value cell of  its Format property.
    The chart and table now look as follows:

Next, we format the two filter controls and the navigation control.

- Select the two filter controls in the report, then in the Report Inspector, set their Border Color property to 0x7ca2cf, and edit Background and Foreground in the Title property group to 0x7ca2cf and White.
			

- Select the three buttons in the navigation control, then edit their Bold property to true, Background to 0x7ca2cf, and Foreground to White.
    The report applies the formatting and displays as follows in design view:

- Navigate to File > Save to save the report as Products.wls.

## 
Task 4: Preview the Report in Web Report Studio 

In this task, we use the Preview as Web Report Result command of Designer to preview the report and test the filter controls in the report. However, this command is enabled only if you have selected the Server for Previewing Reports option when installing  Designer.

- Navigate to View > Preview As > Web Report Result. The report runs in Web Report Studio in your default web browser.
    You may find that the report layout is not so perfect because Web Report Studio adopts responsive view by default to suit different mobile devices. To close responsive view, select Customize Toolbar Items on the toolbar and select Close Responsive Mode from the menu list. The Close Responsive Mode button  then appears on the toolbar. Select the button to close responsive view.

We can use the filter controls to dynamically change the report data. Since the chart and table apply the same business view and the filter controls use fields from this business view, Web Report Studio applies the filters created via the filter controls  to both of them at the same time. First, we want to view the sales in Canada.

- Select Canada in the Country filter control. Web Report Studio refreshes the chart and table to display the data for Canada only.
    

- To further view the product Kona Mountain's sales in Canada, select Kona Mountain in the Product Name filter control. Web Report Studio refreshes the report to show the corresponding data.
    

Next, we want to view the sales of Blue Mountain, Breakfest Blend, and French Roast in all countries. Since the current report data is for Kona Mountain's sales in Canada, we need to remove the filters first. 

- Select Clear on the title bar of each filter control to clear the value selection in them. You can also use the navigation control in the report to achieve the same goal: select Back twice to undo what you have just done in the previous two steps, or select Clear to simply clear the filter conditions in all filter controls.

- Select and hold the Ctrl key, then select Blue Mountain, Breakfest Blend, and French Roast in the Product Name filter control. The report now shows as follows:
    

- Exit Web Report Studio.
    You can go to Creating a Web Report Using the Quick Start Method and Creating a Web Report Using the Wizard to get more information about working with Web Report Studio.
