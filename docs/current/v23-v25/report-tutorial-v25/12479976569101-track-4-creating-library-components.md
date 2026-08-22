---
title: "Track 4: Creating Library Components"
id: 12479976569101
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479976569101-Track-4-Creating-Library-Components
updated_at: 2025-05-30T02:58:13Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Track 4: Creating Library Components

Library components are used by end users to build dashboards using JDashboard, a separately licensed product on Server. Library components are created and edited in Designer, and then published along with their catalog to the component library on Server for use in dashboards.

In this track, you have been asked to create two library components as a report developer, based on the business view WorldWideSalesBV created in the previous track. One library component should contain a table that shows each product's order details, including order ID, quantity, unit price, and the total sales for each order, and the other library component contains a chart that demonstrates the total sales of each product. You also need to use some features that are specific to library components only, such as Message, Slider, and Configuration Panel.

This track contains the following tasks:

- Task 1: Create Two Library Components 

- Task 2: Deliver a Message Between the Library Components 

- Task 3: Insert a Slider to Filter Data 

- Task 4: Use Text Field in the Configuration Panel to Change Property Value

 To perform this track, you should have a JDashboard license for Designer. In the meantime, JDashboard is in maintenance mode, and we will not be adding new features to it. If you need more information, contact Customer Service.
    

## 
Task 1: Create Two Library Components

First, we create two library components, including a table and a chart.

- Select Logi Report Designer in the Logi Report folder on the Start menu to open Designer.

-     Designer displays the main window and shows the Start Page by default. Close the Start Page.

- Navigate to File > Open Catalog.

- In the Open Catalog File dialog box, browse to select the JinfonetGourmetJava.cat catalog file in <install_root>\Demo\Reports\JinfonetGourmetJava, then select Open.

- Select Yes in the Warning dialog box. Designer displays the Catalog Manager. Close it because we do not use it in this lesson.
    

- Navigate to File > New > Library Component. Designer displays the Select Component for Library Component dialog box. 

-  Type Product Order Details in the Library Component Title text box, keep the default component type Table (Group Above), then select OK. 
    

-  In the Data screen of the Table Wizard dialog box, select WorldWideSalesBV and select Next.

- In the Display Screen, drag the following fields one by one to display in the table: Order ID, Quantity, Unit Price, and Total. Select Next.
    

- In the Group screen, add Product Name as the group-by field.

- Select Style on the screen navigation bar to switch to the screen and select Commercial from the style list. Select Finish to create the table.

- Resize the group-by field to make sure all the product names can display completely. 

- Navigate to File > Save to save the library component as  ProductOrderDetails.lc. 

Next, we create the second library component that contains the chart.

- Navigate to File >  New > Library Component.

- In the Select Component for Library Component dialog box, type Product Sales as the library component title, select Chartfrom the component type box and select OK. Designer displays the Chart Wizard dialog box.

- In the Data screen, select WorldWideSalesBV, then select Next.

- Keep the default selections in the Type screen. Select Next.

- In the Display Screen, add Product Name to the X-Axis box and Total Sales to the Bar Length box.
    

- Select Style on the screen navigation bar to switch to the screen, then select Classic as the chart style. 

- Select Finish to create the chart.

- Double-click any bar of the chart. Designer displays the Format Bar dialog box.

- Switch to the Fill tab and select Vary Colors by Color List to fill each bar with a different color schema.
    

-  Select OK to apply the setting and close the dialog box. The chart displays as follows in design view. 

-  Navigate to File > Save to save the library component as ProductSales.lc. 

## 
Task 2: Deliver a Message Between the Library Components 

In order for end users to view sales information by order ID in the table, we want to deliver a built-in message 0002-Sort between the two library components. We use the chart to send the message, and the table to receive the message.

-  Double-click any bar in the chart. Designer displays the Format Bar dialog box.

- Switch to the Behaviors tab, select Select from the drop-down list in the Events column, then select the ellipsis in the Actions column.
    

- In the Web Action List dialog box, select the *SendMessage action and select OK.

-  In the Send Message - Web Action Builder dialog box, select the built-in message 0002 - Sort from the Message drop-down list, then in the Value column, select Descending from the drop-down list for Sort Order.
    

- Select OK to close the Send Message - Web Action Builder dialog box.

- Select OK in the Format Bar dialog box to finish defining the message.

- Navigate to File > Save to save the library component. 

Next, we define to make the table receive the sort message that is sent out from the chart once end users perform the Select action  on the chart bars in JDashboard. 

- Navigate to Window > Switch Windows > ProductOrderDetails.lc to switch to the table library component.

- Select the table, right-click on it and select Receive Message from the shortcut menu.

- In the Receive Message dialog box, select Add to add a message line, select the built-in message 0002 - Sort from the drop-down list of the Message ID column, then select the ellipsis in the Actions column.
    

- In the Sort dialog box, select Order ID from the Sort On column and Descending from the Sort Value column. Select OK to close the dialog box.
    

- Select OK in the Receive Message dialog box to finish defining the message.

- Save the library component.

By now, we have finished defining the message between the chart and table, which applies like this: when  end users select any bar on the chart in JDashboard, the chart sends out the built-in message 0002 - Sort to the table, and when the table receives the message, it sorts the order IDs descending.

## 
Task 3: Insert a Slider to Filter Data 

To help end users easily get product sales information in a specific time period, we insert a slider to filter on the Order Date field for the table.

- Navigate to Insert > Web Controls >  Filter Control.

- In the Insert Filter Control dialog box, select the Range Slider control type, from the Select Fields drop-down list, select Order Date, then select outside the drop-down list in the dialog box to finish selecting field. You can also select Customize Initial Values to customize the values you want to show on the slider. Here, we use all values in the Order Date field on the slider.   

- Select OK to insert the slider. 

- Save the library component.

## 
Task 4: Use Text Field in the Configuration Panel to Change Property Value 

In this task, we insert a text field into the configuration panel of the table library component, then we bind the Change Property web behavior to the text field, so that end users can use it to dynamically change the background color of the Quantity field at runtime. 

- Select Display Configuration Panel on the top-right corner to display the panel.

- Navigate to Insert > Web Controls > Text Field to insert a text field in the configuration panel.

- Right-click the text field and navigate to Web Behaviors > Change Property on the shortcut menu. Designer displays the Change Property - Web Behavior dialog box.

- Select Quantity from the Apply Action To drop-down list, Background from the Properties drop-down list, and TextField from the Value drop-down list, then select OK.
At runtime, users can  type a hexadecimal RGB value in the text field to change the background color of the Quantity field in JDashboard. 

Next, we add a label ahead of the text field to help end users identify what it is used for.

- Navigate to Insert >  Label to add a label ahead of the text field. 

- Double-click the label and edit its text to Background Color of Quantity, then resize the label to display the whole text in it completely.
    

- Save the library component.

Previous Topic  Next Topic
