---
title: "Delivering Messages Between Library Components"
id: 45190720977805
section: "Designing Your Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190720977805-Delivering-Messages-Between-Library-Components
updated_at: 2026-04-30T15:16:06Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Delivering Messages Between Library Components

A message is a carrier of information that you can deliver between library components. It makes the runtime data synchronization possible. For example, you have two library components containing a crosstab and a table respectively, and both have the field Country. When you select any of the Country value in the crosstab at runtime, you want the crosstab and table to be filtered to show data of this country only. To achieve such synchronization, you can send out a filter message from the Country field in the crosstab and make the crosstab itself and the table receive the same message. This topic introduces the types of messages Report provides, describes how you can deliver messages between library components, and also presents an example to help you better know about the feature.

Report also supports defining messages at runtime in JDashboard. For more information, see Synchronizing the Data Components in a Dashboard in the Report Server Guide. 

 JDashboard is in maintenance mode, and we will not be adding new features to it. If you need more information, contact Customer Service.

This topic contains the following sections:

- Message Types 

- Sending Messages

- Receiving Messages

- Example: Delivering a Message  Between Library Components

## 
Message Types 

The messages that you can deliver between library components include the built-in messages Filter, Sort, Parameter, and On-screen Filter, and user customized messages. In a customized message, you can specify to send out multiple messages from one object on different trigger events and edit the message information as you want.

A message consists of the message ID, message name, and message value set. A message ID is a natural number. Report reserves the IDs from 1 to 1000, which are used for built-in messages, so you can only use IDs beyond 1000 to identify user-defined messages. A message name is the name of a message. A message value set is a set of key-value pairs. Each key-value pair has one key and one value. A key or a value can be static or dynamic. A key is of the String data type, and each value has its own data type, which can be Number, Integer, String, Date, Time, DateTime, Boolean, or Currency.

Report provides the following built-in messages:

- 
Filter
You can send out a built-in Filter message to ask the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two Filter messages one after another, the latest always replaces the earlier.

- 
Sort
You can send out a built-in Sort message to ask the message receivers to sort themselves according to the sort condition defined in the message. 

- 
Parameter
You can send out a built-in Parameter message to ask the library components that contain the message receivers to rerun using the specified parameter values in the message. It has two subtypes:
			
- 
Automatic
This Parameter message type automatically contains all the parameters the current library component uses.  You can apply it to rerun the library components containing the message receivers using the same parameter values.

- 
Customized
Using this Parameter message type, you can customize the parameter you want to include in the message.

 For compatibility with earlier versions, Designer converts the Parameter message defined in a previous version to the Customized type and the Parameters message to the Automatic type.

- 
On-screen Filter
You can send out a built-in On-screen Filter message to ask the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two On-screen Filter messages one after another, the filter conditions in the two messages are combined using the "AND" logic. However, if the two conditions conflict with each other, for example, the first is "Country=USA" and the second "City=London", Report Engine clears the first condition and the final filter condition applied to the data component is "City=London".

When a data component receives a Filter message and an On-screen Filter message, Report Engine combines the filter conditions in the two messages  using the "AND" logic. If the On-screen Filter message comes after the Filter message, the value list of the on-screen filter is from the data component after it applies the Filter message. However, if the Filter message comes after the On-screen Filter message, the value list of the filter is from the data component before it applies the on-screen filter, which may result in null data.

The following shows examples of how Filter messages, On-screen Filter messages, and the combination of the two types work.

| Example # | The First Filter Message | The Second Filter Message | Result |
| --- | --- | --- | --- |
| 1 | Filter: Country=USA | Filter: City=London | City=London |
| 2 | Filter: Country=USA | Filter: Sales Year=2019 | Sales Year=2019 |
| 3 | On-screen Filter: Country=USA | On-screen Filter： City=London | City=London |
| 4 | On-screen Filter： Country=USA | On-screen Filter： Sales Year=2019 | Sales Year=2019 and Country=USA |
| 5 | Filter: Country=USA | On-screen Filter: Sales Year=2019 | Sales Year=2019 and Country=USA |
| 6 | On-screen Filter: Country=USA | Filter： Country=France | Null |
| 7 | On-screen Filter: Country=USA | Filter： City=London | Null |
| 8 | On-screen Filter： Country=USA | Filter： Sales Year=2019 | Sales Year=2019 and Country=USA |

 

## 
Sending Messages

 An object in a library component can send out different messages when different events occur on it to ask the message receivers to perform specific web actions defined in the messages.

You can use the following objects in the library component body  as the trigger objects to send out messages: labels, data fields (DBFields, formula fields, parameter fields, and summary fields), special fields, the category axis, legend and data markers of charts, markers and areas in geographic maps, parameter controls, and the Submit button of parameter form controls.

To send out a message

Select the trigger object, right-click it and navigate to Send Message > Filter/Sort/Parameter/On-screen Filter/Customize on the shortcut menu (for the Submit button of a parameter form control, only Parameter and Customize are available).

- If you select Filter, a built-in Filter message is sent out when the Click  event occurs on the object at runtime, which asks the message receivers to filter themselves using the default filter condition "Current Field=Current Value". You can edit the filter condition when specifying the message receivers.

- If you select Sort, a built-in Sort message is sent out when the Click event occurs on the object at runtime, which asks the message receivers to sort themselves using the default sort condition "Current Field Ascending". You can edit the sort condition when specifying the message receivers.

- If you select Parameter, a built-in Parameter message of the Automatic type that contains all the parameter values in the current library component is sent out when the Click event occurs on the object at runtime, which asks the library components that contain the message receivers to rerun using the same parameter values. You can edit the parameter values when specifying the message receivers. 

- If you select On-screen Filter, a built-in On-screen Filter message is sent out when the Click event occurs on the object at runtime, which  asks the message receivers to filter themselves using the default filter condition "Current Field=Current Value". You can edit the filter condition when specifying the message receivers.

- If you select Customize, you can define the message by yourself in the Send Message dialog box.
				

- Select a trigger event in the Events box, then select on the name of the event to select it.

- 
From the Message drop-down list, select the message you want to send out when the specified event occurs on the object at runtime.

- Define the message.
						
- For the built-in message, you can edit the condition of how to perform the web action bound with the message in the Value column. To make the condition dynamic, select the values under the Dynamic Key node.

- For a user-defined message,
- Specify the ID and name of the message in the ID and Name text boxes. The ID should be a natural number beyond 1000.

- Select Add to add a message key-value line.

- In the Key column, specify a key from the drop-down list or select <Input...> from the list and then type a key in the text box.

- In the Value column, specify the value of the key from the drop-down list or select <Input...> from the list and then type a value in the text box.

- If you choose to type the value by yourself in the preceding step, you need to specify the data type of the value. If you select the value from the Value drop-down list, Designer automatically displays the data type of the value  in the Data Type column and you cannot change it. 

- Add more key-value lines and specify the key, data type, and value in each line. To delete a message key-value line, select it and select Remove. You can also use Move Up and Move Down to adjust the order of the message key-value lines.

 You can also create a blank user-defined message by only specifying the ID and name of the message.

- Repeat the preceding steps to define other messages that you want to send out from the object on different events.

- Select OK to accept the settings.

In addition to the previous method, you can also use the Send Message web action to send out messages.

 

## 
Receiving Messages

The data components (tables, charts, crosstabs, KPIs, and geographic maps) in a library component can receive messages that are sent out from the current library component or another one. When a data component receives a message at runtime, it performs the web actions defined in the message, such as filtering and sorting itself using conditions specified in the message, running the current or another library component with predefined parameter values, changing its object properties, removing filter conditions, or drilling through data.

To make a data component receive messages and respond corresponding web actions, take the following steps: 

- Right-click the data component and select Receive Message from the shortcut menu. Designer displays the Receive Message dialog box.
			

- Select Add to add a message line.

- From the Message ID column, select the message you want the data component to receive.
			
- 
0001 - Filter
When the data component receives this message, it filters itself based on the filter condition defined in the message.

- 
0002 - Sort
When the data component receives this message, it sorts itself based on the sort condition defined in the message. Not available to KPI.

- 
0003 - Parameter
When the data component receives this message, the library component that contains the data component reruns with the parameter values defined in the message. 

- 
0004 - On-screen Filter
When the data component receives this message, it filters itself based on the filter condition defined in the message.

- 
User Defined
A data component in a library component can also receive user-defined messages and then respond the web actions such as Filter, On-screen Filter, Remove Filter, Sort, Parameter, Change Property, Go Down, Go Up, and Go To.

- If you select a built-in message, you cannot change the action the message responds, but you can edit how to perform the action  as you want. If you select a user-defined message, you can specify the action the data component responds when it receives the message and define how to perform the action.

- Repeat the preceding steps to add more messages to receive and define the actions to respond the messages.
			To delete a message, select it and select Remove. You can also use Move Up and Move Down to adjust the display order of the messages in the message box.

- Select OK to finish setting the messages the data component is going to receive.

 In the drop-down lists for editing the conditions to respond a message, you may find that some items have the icon  ahead of them and they are listed under the Message Key node. If you choose an item of this type, it means that at runtime Report Engine does not use the item directly in a condition, instead, it maps the item to a key in the message and finds the value that users specify to the key from the message first and then uses that value to compose the condition.

The following describes in detail how to make a data component receive different messages. 

To receive the built-in Filter message

- In the Receive Message dialog box, select 0001 - Filter from the drop-down list in the Message ID column. Designer automatically applies the filter condition defined in the message.

- If you want to edit the filter condition, select in the Actions column and select the ellipsis. Designer displays the Filter dialog box.
			

- Specify the filter condition by selecting the field based on which to filter the data component from the Filter On drop-down list, the operator to compose the condition from the Operator drop-down list, and the value of how to filter the field from the Value drop-down list  (to specify the value by yourself, select <Input...> and type the value in the text box). When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".

- Select Add to add more condition lines and specify the filter conditions. To delete a filter condition, select it and select Remove. You can also use Move Up and Move Down to adjust the order of the condition lines.

- In the More column, specify the relationship between the filter conditions: "And" or "Or".

- Select OK to finish defining the filter conditions. 

To receive the built-in Sort message

- In the Receive Message dialog box, select 0002 - Sort from the drop-down list in the Message ID column. Designer automatically applies the sort conditions defined in the message.

- If you want to edit the sort condition, select in the Actions column and select the ellipsis. Designer displays the Sort dialog box.
			

- Specify the sort condition by selecting the field on which to sort the data component from the Sort On drop-down list, and the order to perform the sort  from the Sort Value drop-down list.

- Select Add to add more condition lines and specify the sort conditions. To delete a sort condition, select it and select Remove.

- Adjust the order of the sort conditions using Move Up and Move Down. The order determines the sort priority of the conditions at runtime.		

- Select OK to finish defining the sort conditions.

To receive the built-in Parameter message

- In the Receive Message dialog box, select 0003 - Parameter from the drop-down list in the Message ID column. 

- Choose a message type from the Message Info column: Automatic or Customized.
				
- When you select Automatic, Designer automatically applies all the parameter values specified in the sent message. If you want to edit the parameters,
						
- Select in the Actions column and select the ellipsis. Designer displays the Parameter dialog box.
							

- Specify the parameter and the value of the parameter from the Parameter Name and Value drop-down lists. The operator can only be "=". "Parameter Name*" in the Parameter Name drop-down list means to rerun  the library component using parameters defined in the sent message, and its corresponding value can only be "Parameter Value*" that represents all the parameter values.

- Select Add to add more parameter lines to specify other parameter values. If you specify a parameter value more than once, the last setting takes effect. To delete a parameter, select it and select Remove. You can also use Move Up and  Move Down to adjust the order of the parameter lines.

- Select OK to accept the settings. Then at runtime, when the data component receives the message, the library component which contains it reruns with all the predefined parameter values.

- When you select Customized, Designer automatically applies the parameter value defined in the sent message. If you want to edit the parameter,
						
- Select in the Actions column and select the ellipsis to open the Parameter dialog box.
			

- Specify the parameter and the value of the parameter from the Parameter Name and Value drop-down lists. The operator can only be "=".

- Select OK to accept the settings. Then at runtime, when the data component receives the message, the library component which contains it reruns with the predefined parameter value.

To receive the built-in On-screen Filter message

- In the Receive Message dialog box, select 0004 - On-screen Filter from the drop-down list in the Message ID column. Designer automatically applies the filter condition defined in the message.

- If you want to edit the filter condition, select in the Actions column and select the ellipsis. Designer displays the On-screen Filter dialog box.
			

- Specify the filter condition by selecting the field based on which to filter the data component from the Filter On drop-down list, and the value of how to filter the field from the Value drop-down list  (to specify the value by yourself, select <Input...> and type the value in the text box). When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".

- Select Add to add more condition lines and specify the filter conditions. To delete a filter condition, select it and select Remove.

- Select OK to finish defining the filter conditions. 

To receive a user-defined message and respond the Filter web action

You can use the Filter web action to filter the data component when it receives the message.

- In the Receive Message dialog box, specify the ID and name of the user-defined message in the Message ID and Message Name columns respectively, then select in the Actions column and select the ellipsis.
    

- In the Web Action List dialog box, select *Filter in the Action Name column and select OK.

- In the Filter dialog box, specify the filter conditions.

- Select OK to accept the settings.

To receive a user-defined message and respond the On-screen Filter web action

You can use the On-screen Filter web action to filter the data component when it receives the message.

- In the Receive Message dialog box, specify the ID and name of the user-defined message in the Message ID and Message Name columns respectively, then select in the Actions column and select the ellipsis.
    

- In the Web Action List dialog box, select *On-screen Filter in the Action Name column and select OK.

- In the On-screen Filter dialog box, specify the filter conditions.

- Select OK to accept the settings.

To receive a user-defined message and respond the Remove Filter web action

You can use the Remove Filter web action to remove filters from the data component when it receives the message.

- In the Receive Message dialog box, specify the ID and name of the user-defined message in the Message ID and Message Name columns respectively, then select in the Actions column and select the ellipsis.
    

- In the Web Action List dialog box, select *Remove Filter in the Action Name column and select OK. Designer displays the Remove Filter dialog box. 

- Specify the filters you want to remove from the data component when it receives the message. 

- 
Remove Filters
Select to remove the filters created via the Filter dialog box, the Filter option on a field’s shortcut menu, and the Filter web action.

- 
Remove *On-screen Filters
Select to remove the filters created by the *On-screen Filter web action.

- By default, JDashboard removes all the on-screen filters  from the data component when it receives the message at runtime if you select Remove *On-screen Filters. If you only want to remove the filter conditions that are related to certain data fields, clear All Fields, then select Add to add a field line, select in the line and select a field from the drop-down list or select <Input...> and type the field name in the text box. Repeat this to add all the required fields. To delete a field, select it and select Remove.

- Select OK to accept the settings.

To receive a user-defined message and respond the Sort web action

You can use the Sort web action to sort data of the data component when it receives the message.

- In the Receive Message dialog box, specify the ID and name of the user-defined message in the Message ID and Message Name columns respectively, then select in the Actions column and select the ellipsis.
    

- In the Web Action List dialog box, select *Sort in the Action Name column and select OK.

- In the Sort dialog box, specify the sort conditions.

- Select OK to accept the settings.

To receive a user-defined message and respond the Parameter web action

You can use the Parameter web action  to run a library component, especially a library component with parameters using predefined parameter values, or rerun the current library component with predefined parameter values when the data component receives the message.

- In the Receive Message dialog box, specify the ID and name of the user-defined message in the Message ID and Message Name columns respectively, then select in the Actions column and select the ellipsis.
    

- In the Web Action List dialog box, select *Parameter in the Action Name column and select OK. Designer displays the Parameter dialog box.
			

- Specify the handler to receive the parameters of the web action. The handler may be the default one in the current server, or in another server specified by Customized Path.

- Specify how to apply the action: run another library component or refresh the current library component.

-  If you choose to run another library component by the action, select Browse to specify the library component, then select the window or frame to open the library component from the Target Frame drop-down list. 

- If the specified library component contains parameters, Designer automatically lists the parameters in the parameter box. Specify the value for each parameter.

- Select Add to add more parameter lines to specify other parameter values. To delete a parameter, select it and select Remove. You can also use Move Up and  Move Down to adjust the order of the parameter lines.

- Select OK to accept the settings.

To receive a user-defined message and respond the Change Property web action

You can use the Change Property web action to change properties of the data component when it receives the message.

- In the Receive Message dialog box, specify the ID and name of the user-defined message in the Message ID and Message Name columns respectively, then select in the Actions column and select the ellipsis.
    

- In the Web Action List dialog box, select *Property in the Action Name column and select OK. Designer displays the Change Property dialog box.
			

- In the Properties column, select the property of the data component you want to change. You can also type the property name by yourself.

- In the Value column, specify the value of the property.

- Select Add to add more condition lines and specify the property conditions. To delete a property condition, select it and select Remove. You can also use Move Up and  Move Down to adjust the order of the condition lines.

- Select OK to accept the settings.

To receive a user-defined message and respond the Go Down web action

You can use the Go Down web action to drill data of the data component to a lower-level group according to the predefined hierarchy in the business view the data component uses when it receives the message.

The Go Down web action works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

- In the Receive Message dialog box, specify the ID and name of the user-defined message in the Message ID and Message Name columns respectively, then select in the Actions column and select the ellipsis.
    

-  In the Web Action List dialog box, select *Go Down in the Action Name column and select OK. Designer displays the Go Down dialog box.
			

- In the Go Down On column, select the group in the data component on which to perform the go-down action. For a geographic map, it is "Current Layer" and you cannot change it.

- In the Use Hierarchy column, select the hierarchy based on which to perform the go-down action. 
			You can also use a web control in the library component to retrieve a hierarchy name at runtime. For a geographic map, the "Built-in" hierarchy is used and you cannot change it.

- In the By Value column, type a value of the specified group field to go down to the lower level with the filter condition "SpecifiedGroupField=TheValue". You can also use a web control to retrieve a value at runtime.

- Select OK to accept the settings.

To receive a user-defined message and respond the Go Up web action

You can use the Go Up web action to drill data of the data component to a upper-level group according to the predefined hierarchy in the business view the data component uses when it receives the message.

The Go Up web action works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

- In the Receive Message dialog box, specify the ID and name of the user-defined message in the Message ID and Message Name columns respectively, then select in the Actions column and select the ellipsis.
     

-  In the Web Action List dialog box, select *Go Up in the Action Name column and select OK. Designer displays the Go Up dialog box.
			

- In the Go Up On column, select a group in the data component on which to perform the go-up action. For a geographic map, it is "Current Layer" and you cannot change it.

- In the Use Hierarchy column, select the hierarchy according to which to perform the go-up action. 
			You can also use a web control in the library component to retrieve a hierarchy name at runtime. For a geographic map, the "Built-in" hierarchy is used and you cannot change it.

- Select OK to accept the settings.

To receive a user-defined message and respond the Go To web action

You can use the Go To web action to change a data field of the data component when it receives the message.

The Go To web action works on the groups of tables, the column/row fields and aggregations of crosstabs, and the category and series fields of charts.

- In the Receive Message dialog box, specify the ID and name of the user-defined message in the Message ID and Message Name columns respectively, then select in the Actions column and select the ellipsis.
    

- In the Web Action List dialog box, select *Go To in the Action Name column and select OK. Designer displays the Go To dialog box.
			

- In the Go To On column, select the field on which to perform the go-to action.

- In the To Column column, select another field to change the "Go To On" field to. 
			You can also use a web control in the library component to retrieve a field name at runtime.

- To apply the go-to action by filtering the "Go To On" field at the same time, select By Value and then type the value by which to filter the field or select a web control in the library component to retrieve the value at runtime. Skip this step if you select to perform the action on a crosstab aggregate field.

- Select OK to accept the settings.

 

## 
Example: Delivering a Message  Between Library Components

This example demonstrates how you can deliver a filter user-defined message between two library components in order to synchronize the data components in them. It contains the following tasks:

- Task 1: Create two library components

- Task 2: Send out a filter user-defined message from the chart

- Task 3: Make the two data components receive the same message

- Task 4: Publish the library components

- Task 5: Deliver the message in a dashboard for data synchronization

Task 1: Create two library components

- Make sure SampleReports.cat is the currently open catalog file. If not, navigate to File > Open Catalog to open it from <install_root>\Demo\Reports\SampleReports.

- Use the business view SaleStat in Data Source 1 of the catalog to create two library components and save them as "Component 1.lc" and "Component 2.lc".
			
- In Component 1, create a chart that displays in the Clustered Bar 2-D chart type, shows Assigned Region on the category axis and Total Actual on the value axis, and applies the Commercial style.

- In Component 2, create a crosstab using Order ID and Assigned Region as the row and column fields, and Total Actual as the aggregate field, and applying the Commercial style too.

Task 2: Send out a filter user-defined message from the chart

In this task, we send a filter user-defined message from the chart in Component 1 when the "select" event occurs on any legend entry value.

- Open Component 1.lc.

- Double-click any bar of the chart, then in the Fill tab of the Format Bar dialog box, select Vary Colors by Color List to make the bar colors vary. Select OK to accept the change and close the dialog box. 

- Right-click the chart legend and navigate to Send Message > Customize  on the shortcut menu. Designer displays the Send Message dialog box.

- In the Events box, select Select as the trigger event, then select on the event to activate the message options on the right.

- From the Message drop-down list, select User Defined, then type 1001 and Filter - Assigned Region as the message ID and name.

- Select Add to add a message line.

- Select <Input> from the drop-down list in the Key column and type Assigned Region in the text box.

- Select Current Value from the drop-down list in the Value column. Designer displays String automatically in the Data Type column.
			

- Select OK to finish defining the message to send out from the chart.

- Save the library component. 

Task 3: Make the two data components receive the same message

In this task, we make the chart and crosstab in the two library components receive the same filter message to filter on the Assigned Region values when they receive the message that is sent out from a chart legend entry. 

- Right-click the chart platform and select Receive Message from the shortcut menu. Designer displays the Receive Message dialog box.
			

- Select Add to add a message line.

- Select <Input> from the drop-down list in the Message ID column, then type 1001 in the column.

- Select in the Message Name column and type Filter - Assigned Region.

- Select in the Actions column and select the ellipsis.
			

- In the Web Action List dialog box, select *Filter and select OK. Designer displays the Filter dialog box.

- Select Assigned Region from the Filter On drop-down list, keep the default operator, then select <Input> under the Message Key node in the Value drop-down list and type Assigned Region. Select OK to apply the filter condition in the message.			

- In the Receive Message dialog box, select OK to finish defining the message the chart receives.			

- Save the library component. 

- Open Component 2.lc.

- Right-click the crosstab and select Receive Message from the shortcut menu.

- In the Receive Message dialog box, specify the message the crosstab receives as described in the previous steps.

- Save the two library components.

Task 4: Publish the library components

Start Server and publish the library components along with the catalog SampleReports.cat to the component library on Server. For more information about publishing resources from Designer to Server, see Publishing Resources Remotely.

Task 5: Deliver the message in a dashboard for data synchronization

- In the Resources page of the Server Console, navigate to New > Dashboard on the task bar. Server creates a blank dashboard in JDashboard.

- In the Resources panel, browse to the folder where you have published the two library components.

- Drag the two library components to the dashboard.
			

- Select Asia-Pacific in the chart legend to send out the message. JDashboard filters both the chart and the crosstab to show data in the Asia-Pacific region only.
			

- Select Clear Filters on the toolbar to clear the filter in both components.

- Select Europe, Middle East, Africa in the chart legend. The chart and crosstab now shows data for  this region.
