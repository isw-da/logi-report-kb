---
title: "Track 3: Performing Visual Analysis "
id: 28897686268429
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897686268429-Track-3-Performing-Visual-Analysis
updated_at: 2026-02-26T02:10:53Z
source_host: docs-report.zendesk.com
---
# Track 3: Performing Visual Analysis

Visual Analysis is an in-context analysis tool to visualize the result of every step of your work. Simply by dragging  data fields to a layout module, you are able to visually analyze data in either text or graphs. Business views are the data sources used in Visual Analysis.

This track contains the following tasks: 

- Task 1: Analyzing by Text

- Task 2: Analyzing by Graphs

 To perform this track, you should have a Visual Analysis license. If you need more information, contact Customer Service.
    

## 
Task 1: Analyzing by Text

- In the Start Page of the Server Console, select Public Folder in the Open category to open the folder. 

- In the Resources page of the Server Console, navigate to New > Analysis on the task bar. 
    

Server displays Visual Analysis  in a new window and prompts the Select Data Source dialog box for you to select the data source that you want to use to perform the analysis. You can select a business view from all the public catalogs.

- Select WorldWideSalesBV in Data Source 1 of the SampleReports catalog and select OK. Visual Analysis lists the group  and aggregation  fields in the selected business view in the Data Source panel on the left. You can drag them to the data presentation area on the right to perform analysis.    
    

- From the Data Source panel, drag the group field Country to the row control box for grouping  as the row header.
    

- Drag the group field Category to the column control box for grouping  as the column header.
    

- Drag the aggregation field Total Sales to Label in the legend section. The report shows as follows. You can hover the mouse on any value to get the detailed information:
    

Next, we use the Filter panel to filter data in the report. 

- From the Data Source panel, drag Region to the Filters panel. Visual Analysis adds a filter based on this field  in the Filters panel.
    

- Clear <All> and then select Asia-Pacific. Visual Analysis refreshes the report  to show the countries in Asia-Pacific only.
    

- Select Save on the toolbar. Visual Analysis displays the Save As dialog box.

- Leave the save location be the My Reports folder, type ProductSales in the File Name text box, and select OK. Visual Analysis saves the current data state as an analysis template
 to the My Reports folder in the server resource tree.

## 
Task 2: Analyzing by Graphs 

In this task, we start a new Visual Analysis session to analyze data by graphs.

- Select Menu and select New from the drop-down menu. Visual Analysis displays a new tab in your browser window. 

- In the Select Data Source dialog box, select WorldWideSalesBV, then select OK. 

- In the data presentation area, select Display Type, then select Bar from the drop-down list. 

- From the Data Source panel, drag the aggregation field  Total Sales to the row control box used for aggregating .
    

- Drag the group field Sales Year  to the column control box used for grouping .
    

- Drag  Category to the right of Sales Year. When Visual Analysis displays an arrow, release the mouse (you can also use the Add button  beside a data control box to add a field from the resource list).
    

Visual Analysis displays the report as follows:

We want to analyze data of the two sales years by quarter, so next we replace Sales Year with Sales Quarter.

- From the Data Source panel, drag Sales Quarter over Sales Year. When Visual Analysis displays an arrow above Sales Year (in the center), release the mouse.
    

In the control box sections, you can also drag a field to the right/left or top/bottom to change the display order of the field, or drag a field out of its control box to remove it.

Next, we try another important feature of Visual Analysis, analyzing with the legend. 

- Drag Region to Color in the legend section. Visual Analysis marks data of each region by different color. You can select the Color button  to customize the colors if you want. Here we keep the default color pattern.
    

Visual Analysis displays the report with a scroll bar which is not convenient for comparing data. We can change the fit setting to improve the layout. 

- Enlarge the browser window size a bit, then select Fit Visible from the drop-down list of Normal View on the toolbar. Visual Analysis now fully displays the report according to the current window size.
    

- Hover the mouse on different color sections on a bar and you can see related information.
    

Visual Analysis supports the Sort feature on the fields used for grouping the columns and rows. Next, we want to sort the sales quarters based on their total sales in descending order. 

- Right-click Sales Quarter and select Sort from the shortcut menu.
    

- In the Sort dialog box, select Descending, select the Sort Using Another Field option and select Total Sales from the drop-down list. Select OK.
    

The report now displays as follows:

Lastly, we change the data display type to Pie so that it is easy to find out which region sales the most. 

- Select Display Type and then select Pie from the drop-down list.

- Remove Sales Quarter and Category from the column control boxes by dragging them out of their positions. 

- Move Total Sales from the row control box to Slice in the legend section. The report changes to the following, and we can see that North America occupies the largest amount of the total sales.

- Select Save on the toolbar to save the data state as an analysis template into the server resource tree.
