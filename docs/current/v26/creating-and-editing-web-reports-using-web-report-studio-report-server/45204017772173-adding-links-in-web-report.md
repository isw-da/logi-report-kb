---
title: "Adding Links in Web Report"
id: 45204017772173
section: "Creating and Editing Web Reports Using Web Report Studio Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204017772173-Adding-Links-in-Web-Report
updated_at: 2026-04-30T14:10:59Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Adding Links in Web Report

You can add links in a web report to link the report with other reports, locations specified by URLs, email addresses, or Blob data type fields, to gain access to the linked targets by selecting the corresponding trigger objects in the report. This topic describes how you can add, open, edit, and remove links in web reports. 

The links can either be simple links or conditional links. Using conditional links, you can make different targets loaded based on different conditions.

You can use the following objects as the trigger objects of links: labels, images, data fields, formula fields, parameter fields, special fields, and the category (X) axis labels, legend labels, and data markers of charts.

This topic contains the following sections:

- Adding a Link

- Linking to Another Report

- Linking to URL

- Linking to an Email

- Linking to a Blob Data Type Field

- Opening a Link

- Editing a Link

- Removing a Link

- Example of Adding a Conditional Link

## 
Adding a Link

To add a simple link in a report:

- Right-click the object that you want to use as the trigger object of the link and select Link on the shortcut menu. Server displays the Insert Link dialog box.

- From the Link Type drop-down list, select the target to which you want to link the object: Report, URL, E-mail, or Content.

- Specify the options for the link target.

- Select OK to create the link.

To add a conditional link to an object:

- Right-click the object that you use as the trigger object of the link and select Link from the shortcut menu. Server displays the Insert Link dialog box.

- Select Conditional Link.

- Select the Add button . Server displays the Edit Conditions dialog box.

- Define a condition using either simple expressions or complex expressions according to your requirements.
    Server displays and highlights the newly added condition in the Condition box in the Insert Link dialog box.

- From the Link Type drop-down list, select the target to which to link the object under this condition: Report, URL, E-mail, or Content.

- Specify the options for the link target.

- Repeat the preceding steps to add more conditions and define the link target for each condition.

- To edit a condition, select the condition in the Condition box, then select the Edit button . In the Edit Conditions dialog box, edit the expressions as required. 

- To remove a condition and the corresponding format, select the condition in the Condition box and select the Remove button . 

- To adjust the priority of a condition, select the condition in the Condition box and then select the Move Up button  or the Move Down button .  

- Select OK to finish defining the conditional link.

For an illustrated example, see Example of Adding a Conditional Link.

### 
Linking to Another Report

You can link a report to another report, then when you select the trigger object in the primary report, you will be able to jump to the linked report to obtain information about the trigger object.

- In the Insert Link dialog box, select Report as the link type.  
    

- Select Browse beside the Report text box. Server displays the Select a Report dialog box.

- Select the target web report you want as the linked report.

- Select OK.

- Select the window or frame in which to load the linked report from the Target drop-down list.

- You can select More to display more options for setting the link.

- In the Filter tab, select the Add Component button  above the Components box. 

- Select a data component in the linked report to interlink with the primary report. You can add only one data component at a time. If there are multiple data components in the linked report and you want to interlink some or all of them with the primary report, you need to select the Add Component button  several times to add them one by one.

- Specify the filter conditions based on which you want to set up the link relationship between the primary report and the selected data components in the linked report (linked data components). However, depending on where the trigger object is in the primary report, you are not able to define filter conditions under some circumstances. For example, if the trigger object is a label in the report body, Server does not activate the Add Condition button  above the Field Conditions box.
				

- Select a linked data component in the Components box.

- Select  the Add Condition button above the Field Conditions box. Server adds a condition line.

- Select the primary field from the Fields (Primary) drop-down list. The provided field list contains all view elements in the business view used by the data component that contains the trigger object, as well as the dynamic formulas in the primary report. When the trigger object is one of the following, Server displays Current Field in the Fields (Primary) drop-down list. Select it if you want to use the  data field that is related to the trigger object in the filter condition.

- A column/row field in a crosstab.

- A data field, formula field, summary field, or the special field Group Name in a banded object or table.

- The chart legend labels which are bound with the category/series field of a chart, or the category axis labels of a chart.

When the trigger object is the data marker in a chart, Server displays Current Category and Current Series (if the chart has the series axis) in the Fields (Primary) drop-down list. Select it if you want to apply the corresponding chart category or series field in the filter condition.

- Choose an operator from the OP drop-down list. The operator can be "=", "<>", "<", ">", "<=", ">=", "IN", or "NOT IN".

- Select the linked field  from the Fields (Linked) drop-down list, where Server lists the view elements in the business view used by the linked data component which are of the same data type as the selected primary field.When you select Current Field, Current Category, or Current Series in the Fields (Primary) drop-down list, if the business view of the linked data component contains the data field, which is of the same data type and the same name as the data field that is related to the trigger object in the primary report, Server displays the Corresponding Field item in the Fields (Linked) drop-down list. Select it to use this corresponding field in the linked data component in the filter condition. 

When you define a filter condition as Current Field/Category/Series = Corresponding Field, you are able to set up dynamic links with filters automatically generated from the drilling path. For example, if the data field  related to the trigger object in the primary report is the group object Country, which is contained in a hierarchy and its one-level-lower group is City, after you drill  from Country down to City in the primary report and trigger the link on any city, you can get data of the specified city in the linked data component.

When the Corresponding Field item is not available, and you want to use it, you can customize the mapping relationship between Current Field in the primary report and Corresponding Field in the linked report. To do this, select  the Mapping Table button . Server displays the Mapping Table dialog box. In the Current Field column, Server displays the business view of the data component that contains the trigger object. Select the field that is related to the trigger object. Next, in the Corresponding Field column, select a field that is of the same data type and that has the same values as the current field you specified, from the business view of the linked data component to map to the current field. Select OK. Server closes the Mapping Table dialog box and displays the Corresponding Field item in the Fields (Linked) drop-down list for you to select.

- You can specify more conditions by selecting the Add Condition button  and then specifying the primary field, the operator, and the corresponding linked field. The relationship between these conditions is "AND", which means that Web Report Studio fetches data for the linked data component which meets all the conditions.

- Repeat the preceding steps to set link conditions between the primary report and other linked data components.

- 
To apply the on-screen filters  in the primary report  to the selected data components of the linked report (linked data components):
			

- Select a linked data component from the Components box.

- Select Pass on-screen filters to the linked components.

- When the data component containing the trigger object in the primary report  and the linked data component use different business views, Server activates the Mapping Table button. In this case, you need to select the button to define the mapping relationship based on which to pass the on-screen filters in the primary report  to the linked data component using the Mapping Table dialog box.

- Select the add button  to add a mapping line.

- Select the field that is bound with an on-screen filter in the primary report from the Fields (Primary) drop-down list.

- Server lists all available fields in the business view used by the linked data component which are of the same data type as the selected on-screen filter field in the Fields (Linked) drop-down list. Select a field whose values are the same as those of the on-screen filter field.
        A mapping relationship is now set up. When you trigger the link, Web Report Studio applies the corresponding on-screen filter in the primary report  to the selected linked field in the linked data component.

- Add more mapping lines and define the mapping relationship between the on-screen filter fields in the primary report with appropriate fields in the linked data component. 

- Select OK to go back to the Insert Link dialog box. 

- Repeat the preceding steps to apply the on-screen filters in the primary report to other linked data components.

- From the Default Linked Component drop-down list, select the component to display by default in the linked report when you trigger the link in the export outputs.
    For example, a linked report contains a chart and a table, and you select the table  as the default linked component. When you export the primary report to PDF with linked report and trigger the link in the PDF output, the page that contains the table  displays by default. You can scroll to view the chart.

- If the linked report contains one or more parameters, Server activates the Parameters tab. In this tab, you can assign fields of the primary report to parameters of the linked report to use the field values for the parameters automatically when running the linked report from the link. If the selected field is a parameter field, you can choose Current Value to use its most recently specified value or Initial Value to use its original value for the parameter in the linked report.
    

- If you would like to pass the values of the filter objects like filter controls in the primary report to filter objects in the linked report, go to the Advanced tab to set up the relationship between the filter objects.
    

- Select the Add button  to add a line. 

- In the Primary Report Property/Object column, select the ellipsis button . Server displays the Select Value dialog box.

- Select a filter object in the primary report.

- Select OK. 

- In the Linked Report Property/Object column, select the ellipsis button . Server displays the Select Value dialog box.

- Select a filter object in the linked report. You need to make sure that values of the filter object in the primary report can apply to the filter object in the linked report in the same line. 

- Select OK. 

- Follow the preceding steps to set up the relationship between more filter objects.

- Select OK to apply the settings.

Then when you are in the View Mode of Web Report Studio, you can trigger the link to open the linked report. The link is also available when you run the primary report in HTML, PDF, or Excel with  the Run Linked Report option being selected.

If the linked report opens in the same frame as the primary report in Web Report Studio, you can select the Back button  on the toolbar to go back to the primary report. Select the Visited Reports button  and you get a menu which lists the original report and the linked targets you have just visited within the link chain. The item selected on the drop-down list is the currently open page. Select another item and Server directs you to that target.

- When linking reports, you need to avoid link loops. For example, if you have linked report A to report B, then you cannot link report B back to report A again.

- The conditions that you specified in the Filter tab are used for filtering when you trigger the link in Web Report Studio, that is, Server only displays the data that meet the conditions in the linked report. However, when you trigger the link in the HTML, PDF, or Excel output, the conditions are used for setting up search criteria between the two linked reports, which means after you select the trigger object in the primary report, Server displays the pages containing the data that meet the conditions in the linked report.

- When you specify the filter condition between the primary report and linked report as Current Field = Corresponding Field, if there is not a matched corresponding field in the linked report, Web Report Studio ignores the condition, which means after you trigger the link, you get a linked report which is not filtered. In the meantime, Web Report Studio adds an error message into log to record the issue.

### 
Linking to URL

- In the Insert Link dialog box, select URL as the link type. 
    

- Type the URL in the Hyperlink text box directly. 

- Select Add Dynamic Field if you want to insert a field into the URL to compose a dynamic URL. Server displays the Select Field dialog box.
			

- Select a field.
                For example, suppose you define the link on the Country field and compose the URL as follows: type http://www.google.com/search?q= into the Hyperlink text box, then select Add Dynamic Field to insert the field Country at the end of the URL. You can then select any country value to open a specific URL that directs to a specific country. 

- When Server enables All Available Values, you can select it if you want to display in the URL all the runtime values of the field that you selected here, instead of only one value. When you select a field that is the same as the current field or one of the parent group fields, the value in the URL is always one value which is related to the value that you select to open the URL.
                In the URL result, Report quotes each field value with a pair of single quotes, separates multiple values by a comma, and always applies the date format yyyy-MM-dd instead of the customized layout format to keep high data precision.

- Select OK to close the Select Field dialog box.

- Select the frame from the Target drop-down list.
    The Target property works when you trigger the link in Web Report Studio. When you trigger the link in JDashboard, except for Same Frame, Server treats all the other targets as New Window.

- Select OK to set up the link.  

Then when you are in the View Mode of Web Report Studio, you can trigger the link to open the URL. The link is also available when you run the report in HTML, PDF, or Excel.

### 
Linking to an Email

- In the Insert Link dialog box, select E-mail as the link type.
    

- Type the email address in the Hyperlink text box directly. 

- You can select Add Dynamic Field to insert a field into the email address via the Select Field dialog box to compose a dynamic email address.

- Select OK to set up the link.

Then when you are in the View Mode of Web Report Studio, you can trigger the link to open the email. You can further customize the email and send it. The link is also available when you run the report in the HTML, PDF, or Excel format.

Email address syntax

When composing the email address, you need to follow the syntax: sAddress[sHeaders]. See the details about the syntax.

- 
sAddress
One or more valid email addresses separated by a semicolon. You must use Internet-safe characters, such as %20 for the space character. 

- 
sHeaders
Optional. One or more name-value pairs. You should prefix the first pair by a "?" and any additional pairs by a "&". The name can be one of the following strings:
    
- 
CC
        Addresses to be included in the "cc" (carbon copy) section of the message.

- 
BCC
        Addresses to be included in the "bcc" (blind carbon copy) section of the message.

- 
subject
        Text to appear in the subject line of the message. 

- 
body
        Text to appear in the body of the message.

Here are some examples:

- user@example.com

- user1@example.com;user2@example.com

- 
${Customer Name}@jinfonet.com, here ${Customer Name} is a field name. Fields can work in the hyperlink only when you insert them via the Add Dynamic Field option.

- 
salesmanager@${Country}.jinfonet.com, here ${Country} is a field name.

- 
user@example.com?CC=user1@example.com&BCC=user2@example.com&subject=TestLinkToEmail&Body=Version%20x.x%0D%0A%0D%0ATest%20Link%20To%20E-mailHere is the email result:

### 
Linking to a Blob Data Type Field

When you link a report with Blob data type fields, Web Report Studio binds the Blob data type fields to the trigger objects of the links and displays them as hyperlinks. You can then download the Blob contents by selecting the hyperlinks in the report.

In Web Report Studio, Blob could be image, Binary, Blob, Clob, LongBlob, LongClob, Varbinary, and Longvarbinary.

To link a report to a Blob data type field:

- In the Insert Link dialog box, select Content as the link type.

Depending on the location of the trigger object, you are not able to link the report with Blob data type fields under some special circumstances. For example, if the trigger object is a label in the report body, after you choose the Content link type, Server disables all the other settings in the dialog box.

- From the Query drop-down list, select the business view which contains the required Blob data type field. Server lists the business views that come from the same data source connection as the business view the current report uses.

- From the Content Type drop-down list, select the content type for the Blob type data. You can also select the button  to bind the content type with a string-type business view element in the selected business view, or with a dynamic formula in the current report. 

- In the File Name text box, type a file name for the linked Blob type data. You can also select the button  to select a string-type view element in the selected business view, or a dynamic formula in the current report, to control the file name. 

- From the Content drop-down list, choose a Blob data type field in the selected business view. 

- Select the More button to display more link options.

- In the Filter tab, specify the filter conditions between the business view used by the current report and the business view that contains the linked Blob contents:
    
- Select the button  above the Field Conditions box. Server adds a condition line. 

- Select the view element you want in the business view used by the current report or a dynamic formula in the current report as the primary field from the Fields (Primary) drop-down list. Select Current Field if you want to use the field that is related to the trigger object of the link in the filter condition.

- Choose an operator from the drop-down list in the OP column.

- Select the linked field  from the Fields (Linked) drop-down list. Server lists all the view elements in the business view containing the linked Blob contents which are of the same data type as the selected field in the Fields (Primary) column.When you select Current Field in the Fields (Primary) drop-down list, if the business view containing the linked Blob contents has the view element which is of the same data type and the same name  as the field that is related to the trigger object, Server lists the item Corresponding Field in the Fields (Linked) drop-down list. Select it to use this corresponding field in the business view of the Blob contents in the filter condition.

- You can specify more conditions by selecting  the button  and then specifying the fields and operators accordingly. The relationship between these link conditions is AND, which means that Web Report Studio fetches the linked Blob type data which meets all the conditions.

- If the business view that contains the linked Blob contents uses parameters, Server enables the Parameters tab. In this tab, you can assign fields of the business view used by the current report to the parameters. Then, when accessing the Blob type data from the link, Server assigns the field values to the parameters automatically.

- Select OK to apply the settings.

Then when you are in the View Mode of Web Report Studio, you can trigger the link to download the Blob contents according to the specified conditions. The link is also available when you run the report  in the HTML, PDF, or Excel format.

## 
Opening a Link

To open a link, switch Web Report Studio to View Mode, then right-click the trigger object and select Show Linked Target from the shortcut menu.

If you created the web report in Web Report Studio, you can also directly select the trigger object to open the link, while for a web report created in Report Designer, whether you can do this depends on whether the report designer gave the Link action the highest Click Priority at report design time. If the priority of the go-down action is the highest and the trigger object is in a hierarchy, you can select the object to open the link only after you have gone down to the lowest level of the hierarchy.

## 
Editing a Link

To edit a link, right-click its trigger object and select Edit Link from the shortcut menu. In the Edit Link dialog box, edit the link according to your requirement. 

## 
Removing a Link

To remove a link, right-click its trigger object and select Remove Link on the shortcut menu. In the warning message dialog box, select Yes to confirm the removal.

## 
Example of Adding a Conditional Link

The following example shows the use of conditional link and dynamic field.

- In Web Report Studio create a summary table based on WorldWideSalesBV in Data Source 1, showing Product Name, Total Sales, and Total Cost, and use Basic as the report style.

-  Right-click on any Product Name value and select Link from the shortcut menu.
Server displays the Insert Link dialog box.    

- Select Conditional Link.

- Select the Add button . Server displays the Edit Conditions dialog box. 

- Define a condition:
    

- Select OK. Server adds the condition in the Condition box.

We will link the field to a URL target based on the condition.

- From the Link Type drop-down list in the Insert Link dialog box, select URL. Server displays the Confirm dialog box.

- Select OK.

- In the Hyperlink text box, type http://www.google.com/search?q=.

- Select Add Dynamic Field to insert the field Product Name at the end of the URL. 
    

For the product names other than Blue Mountain and Breakfast Blend, we will link them to an email target.

- Select Others. Server creates a condition named Others.

- From the Link Type drop-down list, select E-mail. Server displays the Confirm dialog box.

- Select OK.

- In the Hyperlink text box, type @example.com.

- Select Add Dynamic Field to insert the field Product Name right ahead of @. 
    

- Select OK in the Insert Link dialog box to finish defining the links.

Next, we can select the product names in the table to view the link result. 

- Switch Web Report Studio to View Mode.

- Select Blue Mountain. Server displays a Google search result page with the keyword Blue Mountain.
    

- Select Breakfast Blend. Server displays a Google search result page with the keyword Breakfast Blend.

- Select Sumatra. Server displays an email.
