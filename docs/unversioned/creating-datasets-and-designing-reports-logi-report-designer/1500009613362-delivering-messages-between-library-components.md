---
title: "Delivering Messages Between Library Components "
id: 1500009613362
section: "Creating Datasets and Designing Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009613362-Delivering-Messages-Between-Library-Components
updated_at: 2021-07-24T16:03:21Z
---

# Delivering Messages Between Library Components 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636121-Creating-Bursting-Reports)

# Delivering Messages Between Library Components

A message is a carrier of information that can be delivered between library components. It makes the runtime data synchronization possible. For example, you have two library components containing a crosstab and a table respectively, and both have the field Country. When you select any of the Country value in the crosstab at runtime, you want the crosstab and table to be filtered to show data of this country only. To achieve such synchronization, you can send out a filter message from the Country field in the crosstab and make the crosstab itself and the table receive the same message.

Messages can also be defined at runtime in JDashboard. For details, see Synchronizing Data Components in the *Logi Report Server Guide*.

This topic includes the following sections:

* [Message Types](#Intro)
* [Sending Messages](#Send)
* [Receiving Messages](#Receive)
* [Example of Delivering a Message](#Example)

## Message Types

The messages that can be delivered between library components include the built-in messages Filter, Sort, Parameter and On-screen Filter, and user customized messages. In a customized message, users can specify to send out multiple messages from one object on different trigger events and edit the message information as they want.

A message consists of message ID, message name and message value set. A message ID is a natural number. Logi Report reserves the IDs from 1 to 1000, which are used for built-in messages, so you can only use IDs beyond 1000 to identify user defined messages. A message name is the name of a message. A message value set is a set of key-value pairs. Each key-value pair has one key and one value. A key or a value can be static or dynamic. A key is of String type, and each value has its own data type, which can be Number, Integer, String, Date, Time, Date Time, Boolean or Currency.

**Logi Report built-in messages**

Logi Report provides the following built-in messages:

* **Filter**  
   The built-in Filter message is sent out for asking the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two Filter messages one after another, the latest always replaces the earlier.
* **Sort**  
   The built-in Sort message is sent out for asking the message receivers to sort themselves according to the sort condition defined in the message.
* **Parameter**  
  The built-in Parameter message is sent out for asking the library components that contain the message receivers to re-run using the specified parameter values in the message. It has two sub types:
  + **Automatic**  
     This Parameter message type automatically contains all the parameters used in the current library component.
  + **Customized**  
     Using this Parameter message type, you can customize the parameter you want to include in the message.
* **On-screen Filter**  
   The built-in On-screen Filter message is sent out for asking the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two On-screen Filter messages one after another, the filter conditions in the two messages are combined using the AND logic. However if the two conditions conflict with each other, for example, the first is *Country=USA* and the second *City=London*, the first will be cleared and the final filter condition applied to the data component will be *City=London*.

When a data component receives a Filter message and an On-screen Filter message, the filter conditions in the two messages are combined using the AND Logic. If the On-screen Filter message comes after the Filter message, the value list of the on-screen filter is obtained from the data component after being applied the Filter message. However if the Filter message comes after the On-screen Filter message, the value list of the filter is from the data component before being applied the on-screen filter, which may result in null data.

The following shows examples of how Filter messages, On-screen Filter messages and the combination of the two types work.

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

## Sending Messages

An object in a library component can send out different messages when different events occur on it to ask the message receivers to perform specific web actions defined in the messages.

The following objects in the library component body can be used as the trigger objects to send out messages: labels, data fields (DBFields, formula fields, parameter fields, summary fields), special fields, the category axis, legend and data markers of charts, markers and areas in geographic maps, parameter controls, and the Submit button of parameter form controls.

**To send out a message:**

Select the trigger object, right-click it and select **Send Message** > **Filter**/**Sort**/**Parameter**/**On-screen Filter/Customize** on the shortcut menu (for the Submit button of a parameter form control, only Parameter and Customize are available).

* If Filter is selected, a built-in Filter message will be sent out when the select event occurs on the object at runtime, which will ask the message receivers to filter themselves using the default filter condition *"Current Field=Current Value*". You can edit the filter condition when specifying the message receivers.
* If Sort is selected, a built-in Sort message will be sent out when the select event occurs on the object at runtime, which will ask the message receivers to sort themselves using the default sort condition "*Current Field Ascending"*. You can edit the sort condition when specifying the message receivers.
* If Parameter is selected, a built-in Parameter message of the Automatic type that contains all the parameter values in the current library component will be sent out when the select event occurs on the object at runtime, which will ask the library components that contain the message receivers to re-run using the same parameter values. You can edit the parameter values when specifying the message receivers.
* If On-screen Filter is selected, a built-in On-screen Filter message will be sent out when the select event occurs on the object at runtime, which will ask the message receivers to filter themselves using the default filter condition "*Current Field=Current Value"*. You can edit the filter condition when specifying the message receivers.
* If Customize is selected, you can define the message by yourself in the [Send Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009633601-Send-Message-Dialog) dialog.

  ![Send Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904181527/sndmsg.gif)

  1. Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) in the Events box, then select on the name of the event to select it.
  2. From the Message drop-down list, select [the message type](https://devnet.logianalytics.com/hc/en-us/articles/1500009610422-Send-Message-Web-Action-Builder-Dialog#Message) to be sent out when the selected event is triggered on the object at runtime.
  3. Define the message as you want.

     For the built-in message, you can edit the condition of how to perform the web action bound with the message in the Value column. To make the condition dynamic, select the values under the Dynamic Key node.

     For a user defined message,

     1. Specify the ID and Name of the message in the ID and Name text boxes. The ID should be a natural number beyond 1000.
     2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a message key-value line.
     3. In the Key column, specify a key from the drop-down list or select the **<Input...>** item from the list and then type a key in the text box.
     4. In the Value column, specify the value of the key from the drop-down list or select **<Input...>** from the list and then type a value in the text box.
     5. If you choose to type in the value by yourself in the above step, you need to specify the data type of the value. If the value is selected from the Value drop-down list, the data type of the value is automatically displayed in the Data Type column and cannot be changed.
     6. You can add more key-value lines and specify the key, data type and value in each line.

        To delete a message key-value line, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). To adjust the order of the lines, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif).

     **Tip:** You can also create a blank user defined message by only specifying the ID and name of the message.
  4. Repeat the above steps to define other messages that will be sent out from the object on different events.
  5. Select **OK** to accept the settings.

In addition to the above method, you can also use the Send Message web action to send out messages. To do this:

1. Do one of the following:
   * Right-click a data field or a label in a table/crosstab, or a label, a basic web control, a parameter control or the Submit button of a parameter form control which is not in the library component's configuration panel, select **Display Type** from the shortcut menu. In the Display Type dialog, select a trigger event from the drop-down list in the Events column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the Actions column.
   * In the Behaviors tab of some chart format dialogs, select a trigger event from the drop-down list in the Events column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the Actions column.
   * While creating or editing a geographic map, in the Display screen of the map wizard, select a group level and select the **Web Behaviors** button. In the Web Behaviors dialog, select a trigger event from the drop-down list in the Events column, select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the Actions column.
2. In the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog, select **\*SendMessage** and select **OK**. The [Send Message - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009610422-Send-Message-Web-Action-Builder-Dialog) dialog appears.

   ![Send Message - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904183703/sndmsgwbactnbld.gif)
3. [Define the message](#Message) that will be triggered on the specified event.
4. Select **OK** to confirm the settings.
5. In the dialog you are returned to, add more event lines and repeat the above steps to specify to send out more messages as you want.
6. Select **OK** to finish defining the messages to send out.

## Receiving Messages

The data components (tables, charts, crosstabs, KPIs and geographic maps) in a library component can receive messages that are sent out from the current library component or another one. When a data component receives a message at runtime, it will perform the web actions defined in the message, such as filtering, sorting itself using conditions specified in the message, running the current or another library component with predefined parameter values, changing its object properties, removing filter conditions, or drilling through data.

To make a data component receive messages and respond corresponding web actions, take the following steps:

1. Right-click the data component and select **Receive Message** from the shortcut menu. The [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009610002-Receive-Message-Dialog) dialog appears.

   ![Receive Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911616023/rcvmsg.gif)
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a message line.
3. Select the message you want the data component to receive from the Message ID column.
   * [0001 - Filter](#BFilter)  
      When the data component receives this message, it will filter itself based on the filter condition defined in the message.
   * [0002 - Sort](#BSort)  
      When the data component receives this message, it will sort itself based on the sort condition defined in the message. Not available to KPI.
   * [0003 - Parameter](#BParameter)  
      When the data component receives this message, the library component that contains the data component will re-run with the parameter values defined in the message.
   * [0004 - On-screen Filter](#BOnScreenFilter)  
     When the data component receives this message, it will filter itself based on the filter condition defined in the message.
   * **User Defined**  
      A data component in a library component can also receive user defined messages and then respond the web actions such as [Filter](#UFilter), [On-screen Filter](#UOnScreenFilter), [Remove Filter](#URemoveFilter), [Sort](#USort), [Parameter](#UParameter), [Change Property](#UProperty), [Go Down](#UGoDown), [Go Up](#UGoUp) and [Go To](#UGoTo).
4. If a built-in message is selected, the action the message will respond cannot be changed, but you can edit how the action will be performed as you want.

   If a user define message is selected, you can specify the action the data component will respond when it receives the message and define how the action will be performed.
5. Repeat the above steps to add more messages to receive and define the actions to respond the messages.

   To delete a message, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). To adjust the display order of the messages in the message box, select a message and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif).
6. Upon finish, select **OK** to close the dialog.

**Note:** In the drop-down lists for editing the conditions to respond a message, you may find that some items have the icon ![Message Key icon](https://devnet.logianalytics.com/hc/article_attachments/4404904184215/btn_msgkey.gif) ahead of them and they are listed under the Message Key node. If you choose an item of this type, it means the item will not be used directly in a condition, instead it will be mapped to a key in the message and Logi Report will find the value that is specified to the key from the message first and then use that value to compose the condition.

The following details how to make a data component receive different messages.

**To receive the built-in Filter message:**

1. In the Receive Message dialog, select **0001 - Filter** from the drop-down list of the Message ID column. The filter condition defined in the message will be automatically applied.
2. If you want to edit the filter condition, select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. The [Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009631201-Filter-Dialog) dialog appears.

   ![Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911616279/fltr2.gif)
3. Specify the filter condition by selecting the field on which the filter will be based from the Filter On drop-down list, the operator to compose the condition from the Operator drop-down list and the value of how to filter the field from the Value drop-down list.

   If you choose to type in the value manually, when multiple values are required, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add more filter conditions to filter other field values and specify the relationship between the conditions in the More column.

   To delete a filter condition, select the condition and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). To adjust the order of the filter conditions, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif).
5. Select **OK** to finish defining the filter conditions.

**To receive the built-in Sort message:**

1. In the Receive Message dialog, select **0002 - Sort**  from the drop-down list of the Message ID column. The sort conditions defined in the message will be automatically applied.
2. If you want to edit the sort condition, select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. The [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009610442-Sort-Dialog) dialog appears.

   ![Receive Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911616535/sort.gif)
3. Specify the sort condition by selecting the field on which to sort the records from the Sort On drop-down list, and in which order to sort the records from the Sort Value drop-down list.
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add more sort conditions to sort other fields.

   To delete a sort condition, select the condition and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). To adjust the order of the sort conditions, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif).
5. Select **OK** to finish defining the sort conditions.

**To receive the built-in Parameter message:**

1. In the Receive Message dialog, select **0003 - Parameter**  from the drop-down list of the Message ID column.
2. Choose a message type from the Message Info column: Automatic or Customized.
   * When Automatic is selected, all the parameter values specified in the sent message will be automatically applied. If you want to edit the parameters,
     1. Select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. The [Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009632921-Parameter-Dialog#BParam) dialog appears.

        ![Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904184471/prm2.gif)
     2. Specify the parameter and the value of the parameter from the Parameter Name and Value drop-down lists. The operator can only be =.

        Parameter Name\* in the Parameter Name drop-down list means that all the parameters defined in the message will be used to re-run the library component, and its corresponding value can only be Parameter Value\* that represents all the parameter values.
     3. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add more parameter lines to specify other parameter values. If you specify a parameter value more than once, the last setting takes effect.

        To delete a parameter line, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). To adjust the order of the parameters, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif).
     4. Select **OK** to accept the settings. Then at runtime, when the data component receives the message, the library component which contains it will re-run, using all the predefined parameter values.
   * When Customized is selected, the parameter value defined in the sent message will be automatically applied. If you want to edit the parameter,
     1. Select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box to open the Parameter dialog.

        ![Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911616791/prm1.gif)
     2. Specify the parameter and the value of the parameter from the Parameter Name and Value drop-down lists. The operator can only be =.
     3. Select **OK** to accept the settings. Then at runtime, when the data component receives the message, the library component which contains it will re-run, using the predefined parameter value.

**To receive the built-in On-screen Filter message:**

1. In the Receive Message dialog, select **0004 - On-screen Filter** from the drop-down list of the Message ID column. The filter condition defined in the message will be automatically applied.
2. If you want to edit the filter condition, select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box. The [On-screen Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009632801-On-screen-Filter-Dialog) dialog appears.

   ![On-screen Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904184727/onscrnfltr.gif)
3. Specify the filter condition by selecting the field on which the filter will be based from the Filter On drop-down list, and the value of how to filter the field from the Value drop-down list.

   If you choose to type in the value manually, when multiple values are required, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add more filter conditions to filter other field values.

   To delete a filter condition, select the condition and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).
5. Select **OK** to finish defining the filter conditions.

**To receive a user defined message and respond the Filter web action:**

The Filter web action enables you to filter the records of the data component when it receives the message.

1. In the Receive Message dialog, specify the ID and name of the user defined message in the Message ID column and Message Name column separately, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box.
2. In the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog, select **\*Filter** in the Action Name column and select **OK**.
3. In the Filter dialog, [specify the filter conditions](#BFilter) as required.
4. Select **OK** to accept the settings.

**To receive a user defined message and respond the On-screen Filter web action:**

The On-screen Filter web action enables you to filter the records of the data component when it receives the message.

1. In the Receive Message dialog, specify the ID and name of the user defined message in the Message ID column and Message Name column separately, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box.
2. In the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog, select **\*On-screen Filter** in the Action Name column and select **OK**.
3. In the On-screen Filter dialog, [specify the filter conditions](#BOnScreenFilter) as required.
4. Select **OK** to accept the settings.

**To receive a user defined message and respond the Remove Filter web action:**

The Remove Filter web action enables you to remove filters from the data component when it receives the message.

1. In the Receive Message dialog, specify the ID and name of the user defined message in the Message ID column and Message Name column separately, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box.
2. In the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog, select **\*Remove Filter** in the Action Name column and select **OK**. The [Remove Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009633301-Remove-Filter-Dialog) dialog appears.

   ![Remove Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911617047/rmvfltr.gif)
3. Specify the filters you want to remove from the data component when it receives the message.

* **Remove Filters**  
   If the option is selected, the filters created via the Filter dialog, the Filter option on a field’s shortcut menu, and the \*Filter web action will all be removed.
* **Remove \*On-screen Filters**  
   If the option is selected, the filters created by the \*On-screen Filter web action will be removed.

4. By default, all the on-screen filters will be removed from the data component when Remove \*On-screen Filters is selected. If you only want to remove the filter conditions that are related to certain data fields, clear the **All Fields** option, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a condition line, select in the line and select a field from the drop-down list or select **<Input...>** and type in the field name manually. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add more fields. To remove an unwanted field, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).
5. Select **OK** to accept the settings.

**To receive a user defined message and respond the Sort web action:**

The Sort web action enables you to sort the records of the data component when it receives the message.

1. In the Receive Message dialog, specify the ID and name of the user defined message in the Message ID column and Message Name column separately, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box.
2. In the Web Action List dialog, select **\*Sort** in the Action Name column and select **OK**.
3. In the Sort dialog, [specify the sort conditions](#BSort) as required.
4. Select **OK** to accept the settings.

**To receive a user defined message and respond the Parameter web action:**

The Parameter web action enables you to run a library component, especially a library component with parameters using predefined parameter values, or re-run the current library component with predefined parameter values when the message is received.

1. In the Receive Message dialog, specify the ID and name of the user defined message in the Message ID column and Message Name column separately, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box.
2. In the Web Action List dialog, select **\*Parameter** in the Action Name column and select **OK**. The [Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009632921-Parameter-Dialog#UParam) dialog appears.

   ![Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904185111/prm.gif)
3. Specify the handler which will receive the parameters of the web action. The handler may be the default one in the current server, or in another server specified by Customized Path.
4. Specifies whether to apply the action to run another library component or refresh the current. If you choose to run another library component, select the **Browse** button to specify the library component, then select the window or frame in which the library component will be opened from the Target Frame drop-down list.
5. If the specified library component contains parameters, the parameters will be automatically listed in the parameters box. Specify the value for each parameter. You can also select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add more parameter lines to specify other parameter values.
6. To delete a parameter line, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). To adjust the order of the parameters, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif).
7. Select **OK** to accept the settings.

**To receive a user defined message and respond the Change Property web action:**

The Change Property web action enables you to change properties of the data component when it receives the message.

1. In the Receive Message dialog, specify the ID and name of the user defined message in the Message ID column and Message Name column separately, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box.
2. In the Web Action List dialog, select **\*Property** in the Action Name column and select **OK**. The [Change Property](https://devnet.logianalytics.com/hc/en-us/articles/1500009629961-Change-Property-Dialog) dialog appears.

   ![Change Property dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904185367/chgpty.gif)
3. Specify the property you want to change and the value for it respectively from the Properties and Value drop-down lists. You can also type in the property name by yourself. Only properties of the data component itself can be changed at runtime.
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add more property lines to change values of other properties.

   To delete a property line, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). To adjust the order of the properties, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif).
5. Select **OK** to accept the settings.

**To receive a user defined message and respond the Go Down web action:**

The Go Down web action enables you to drill data of the data component to a lower-level group according to the predefined [hierarchy](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business view the data component uses when it receives the message. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

1. In the Receive Message dialog, specify the ID and name of the user defined message in the Message ID column and Message Name column separately, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box.
2. In the Web Action List dialog, select  **\*Go Down** and select **OK**. The [Go Down](https://devnet.logianalytics.com/hc/en-us/articles/1500009631761-Go-Down-Dialog) dialog appears.

   ![Go Down dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911617303/godwn.gif)
3. In the Go Down On column, select the group on which the go-down action will be performed. For a geographic map, it is Current Layer and cannot be changed.
4. In the Use Hierarchy column, select the hierarchy based on which the go-down action will be performed.
   You can also use a web control in the library component to retrieve a hierarchy name at runtime. For a geographic map, the Built-in hierarchy is used and cannot be changed.
5. In the By Value column, type in a value of the specified group field to go down to the lower level with the filter condition *SpecifiedGroupField=TheValue*. You can also use a web control to retrieve a value at runtime.
6. Select **OK** to accept the settings.

**To receive a user defined message and respond the Go Up web action:**

The Go Up web action enables you to drill data of the data component to a upper-level group according to the predefined [hierarchy](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business view the data component uses when it receives the message. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

1. In the Receive Message dialog, specify the ID and name of the user defined message in the Message ID column and Message Name column separately, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box.
2. In the Web Action List dialog, select  **\*Go Up** and select **OK**. The [Go Up](https://devnet.logianalytics.com/hc/en-us/articles/1500009631841-Go-Up-Dialog) dialog appears.

   ![Go Up dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911617559/goup.gif)
3. In the Go Up On column, select the group on which the go-up action will be performed. For a geographic map, it is Current Layer and cannot be changed.
4. In the Use Hierarchy column, select the hierarchy that the go-up action will be performed according to.
   You can also use a web control in the library component to retrieve a hierarchy name at runtime. For a geographic map, the Built-in hierarchy is used and cannot be changed.
5. Select **OK** to accept the settings.

**To receive a user defined message and respond the Go To web action:**

The Go To web action enables you to change a data field of the data component when it receives the message. It is available to tables, charts and crosstabs.

1. In the Receive Message dialog, specify the ID and name of the user defined message in the Message ID column and Message Name column separately, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box.
2. In the Web Action List dialog, select  **\*Go To** and select **OK**. The [Go To](https://devnet.logianalytics.com/hc/en-us/articles/1500009631801-Go-To-Dialog) dialog appears.

   ![Go To dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911617815/goto.gif)
3. In the Go To On column, select the field on which the go-to action will be performed.
4. In the To Column column, select another field to change the Go To On field to.
   You can also use a web control in the library component to retrieve a field name at runtime.
5. To apply the go-to action by filtering the Go To On field at the same time, select the **By Value** checkbox and then type in the value by which to filter the field or select a web control in the library component to retrieve the value at runtime. Skip this step if you select to perform the action on a crosstab aggregate field.
6. Select **OK** to accept the settings.

## Example of Delivering a Message

This example demonstrates how to deliver a filter user defined message between two library components in order to synchronize the data components in them. It contains the following tasks:

* [Task 1: Create two library components](#Task1)
* [Task 2: Send out a filter user defined message from the chart](#Task2)
* [Task 3: Make the two data components receive the same message](#Task3)
* [Task 4: Publish the library components to Logi Report Server](#Task4)
* [Task 5: Deliver the message in a dashboard for data synchronization](#Task5)

**Task 1: Create two library components**

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Use the business view SaleStat in Data Source 1 to [create two library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#LC) and save them as Component 1.lc and Component 2.lc.

   For Component 1, create a chart which displays in the clustered bar 2-D chart type, shows Assigned Region on X-Axis and Total Actual as Bar Length. For Component 2, create a crosstab using Order ID and Assigned Region respectively as the row and column fields, and Total Actual as the summary field. Apply the style Commercial to both of them.

**Task 2: Send out a filter user defined message from the chart**

In this task, we will send a filter user defined message from the chart in Component 1 when the select event occurs on any legend entry value.

1. Open Component 1.lc.
2. Double-click any bar of the chart, then in the Fill tab of the Format Bar dialog, select **Vary Colors by Color List** to make the bar colors vary. Select **OK** to accept the change and close the dialog.
3. Right-click the chart legend and select **Send Message** > **Customize**  on the shortcut menu to bring out the Send Message dialog.
4. In the Events box, select **Select** as the trigger event, then select on the event to activate the message options on the right.
5. From the Message drop-down list, select **User Defined**, then type **1001** and **Filter - Assigned Region** as the message ID and name.
6. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a message line.
7. Select the **<Input>** item from the drop-down list in the Key column and type **Assigned Region** in the text box.
8. Select **Current Value** from the drop-down list in the Value column. String is displayed automatically in the Data Type column.

   The message is defined as follows:

   ![Send Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911618071/rpt_lc_msg_eg_send.gif)
9. Select **OK** to finish defining the message to be sent out.
10. Save the library component.

**Task 3: Make the two data components receive the same message**

In this task we will make the chart and crosstab in the two library components receive the same filter message to filter on the Assigned Region values when they receive the message sent out from a chart legend entry.

1. Right-click the chart platform and select **Receive Message** from the shortcut menu to display the Receive Message dialog.
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a message line.
3. Select the **<Input>** item from the drop-down list in the Message ID column, then type **1001** in the text box.
4. Type **Filter - Assigned Region** in the text box of the Message Name column.
5. Select the blank text box in the Actions column, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears.

   ![Receive Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911618327/rpt_lc_msg_eg_recv1.gif)
6. In the Web Action List dialog, select **\*Filter** and select **OK** to display the Filter dialog.
7. Select **Assigned Region** from the Filter On drop-down list, keep the default operator, then select **<Input>** under the Message Key node in the Value drop-down list and type**Assigned Region** in the text box.

   ![Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911618583/rpt_lc_msg_eg_recv2.gif)
8. Select **OK** to go back to the Receive Message dialog. The message Component 1 receives is defined as follows:

   ![Receive Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911618839/rpt_lc_msg_eg_recv3.gif)
9. Select **OK**, then save the library component.
10. Open Component 2.lc.
11. Right-click the crosstab and select **Receive Message** from the shortcut menu.
12. In the Receive Message dialog, specify the message the crosstab is going to receive [as shown above](#Chart).
13. Save the library components.

**Task 4: Publish the library components**

Start Logi Report Server and publish the library components along with the catalog SampleReports.cat to the component library in Logi Report Server. For details about publishing resources from Logi Report Designer to Logi Report Server, see [Publishing resources remotely](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources#Remotely).

**Task 5: Deliver the message in a dashboard for data synchronization**

1. Open the Logi Report Server console > Resources page, select **New** > **Dashboard** on the task bar. A blank dashboard is displayed in JDashboard.
2. In the Resources panel and browse to the folder where the two library components are published.
3. Drag and drop the two library components to the dashboard.

   ![Components in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404911619095/rpt_lc_msg_eg_msg1.gif)
4. Select **Asia-Pacific** in the chart legend to send out the message. The chart and the crosstab are both filtered to show data in the Asia-Pacific region only.

   ![Data in the Asia-Pacific Region for Chart and Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404904185623/rpt_lc_msg_eg_msg2.gif)
5. Select the **Clear Filters** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404904185879/rpt_lc_msg_eg_clrfltr.gif) on the toolbar to clear the filter in both components.
6. Select **Europe, Middle East, Africa** in the chart legend and the chart and crosstab are filtered based on this region now.

   ![Data in Europe, Middle East, and Africa for Chart and Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404911619351/rpt_lc_msg_eg_msg3.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636121-Creating-Bursting-Reports)
