---
title: "Delivering Messages Between Library Components"
id: 1500010101301
section: "Creating Datasets and Designing Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components
updated_at: 2021-07-23T19:16:49Z
---

# Delivering Messages Between Library Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101161-Creating-Bursting-Reports)

# Delivering Messages Between Library Components

A message is a carrier of information that you can deliver between library components. It makes the runtime data synchronization possible. For example, you have two library components containing a crosstab and a table respectively, and both have the field Country. When you select any of the Country value in the crosstab at runtime, you want the crosstab and table to be filtered to show data of this country only. To achieve such synchronization, you can send out a filter message from the Country field in the crosstab and make the crosstab itself and the table receive the same message. This topic introduces the types of messages Logi Report provides, describes how you can deliver messages between library components, and also presents an example to help you better know about the feature.

Logi Report also supports defining messages at runtime in JDashboard. For more information, see Synchronizing the Data Components in a Dashboard in the *Logi Report Server Guide*.

This topic contains the following sections:

* [Message Types](#Intro)
* [Sending Messages](#Send)
* [Receiving Messages](#Receive)
* [Example of Delivering a Message](#Example)

## Message Types

The messages that you can deliver between library components include the built-in messages Filter, Sort, Parameter, and On-screen Filter, and user customized messages. In a customized message, you can specify to send out multiple messages from one object on different trigger events and edit the message information as you want.

A message consists of the message ID, message name, and message value set. A message ID is a natural number. Logi Report reserves the IDs from 1 to 1000, which are used for built-in messages, so you can only use IDs beyond 1000 to identify user-defined messages. A message name is the name of a message. A message value set is a set of key-value pairs. Each key-value pair has one key and one value. A key or a value can be static or dynamic. A key is of String type, and each value has its own data type, which can be Number, Integer, String, Date, Time, DateTime, Boolean, or Currency.

**Logi Report built-in messages**

Logi Report provides the following built-in messages:

* **Filter**  
  You can send out a built-in Filter message to ask the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two Filter messages one after another, the latest always replaces the earlier.
* **Sort**  
  You can send out a built-in Sort message to ask the message receivers to sort themselves according to the sort condition defined in the message.
* **Parameter**  
  You can send out a built-in Parameter message to ask the library components that contain the message receivers to re-run using the specified parameter values in the message. It has two sub types:
  + **Automatic**  
    This Parameter message type automatically contains all the parameters the current library component uses.
  + **Customized**  
    Using this Parameter message type, you can customize the parameter you want to include in the message.
* **On-screen Filter**  
  You can send out a built-in On-screen Filter message to ask the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two On-screen Filter messages one after another, the filter conditions in the two messages are combined using the "AND" logic. However, if the two conditions conflict with each other, for example, the first is "Country=USA" and the second "City=London", Logi Report Engine clears the first condition and the final filter condition applied to the data component is "City=London".

When a data component receives a Filter message and an On-screen Filter message, Logi Report Engine combines the filter conditions in the two messages using the "AND" logic. If the On-screen Filter message comes after the Filter message, the value list of the on-screen filter is from the data component after it applies the Filter message. However, if the Filter message comes after the On-screen Filter message, the value list of the filter is from the data component before it applies the on-screen filter, which may result in null data.

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

## Sending Messages

An object in a library component can send out different messages when different events occur on it to ask the message receivers to perform specific web actions defined in the messages.

You can use the following objects in the library component body as the trigger objects to send out messages: labels, data fields (DBFields, formula fields, parameter fields, and summary fields), special fields, the category axis, legend and data markers of charts, markers and areas in geographic maps, parameter controls, and the Submit button of parameter form controls.

**To send out a message:**

Select the trigger object, right-click it and select **Send Message** > **Filter**/**Sort**/**Parameter**/**On-screen Filter/Customize** on the shortcut menu (for the Submit button of a parameter form control, only Parameter and Customize are available).

* If you select Filter, a built-in Filter message is sent out when the "select" event occurs on the object at runtime, which asks the message receivers to filter themselves using the default filter condition "*Current Field=Current Value*". You can edit the filter condition when specifying the message receivers.
* If you select Sort, a built-in Sort message is sent out when the "select" event occurs on the object at runtime, which asks the message receivers to sort themselves using the default sort condition "*Current Field Ascending*". You can edit the sort condition when specifying the message receivers.
* If you select Parameter, a built-in Parameter message of the Automatic type that contains all the parameter values in the current library component is sent out when the "select" event occurs on the object at runtime, which asks the library components that contain the message receivers to re-run using the same parameter values. You can edit the parameter values when specifying the message receivers.
* If you select On-screen Filter, a built-in On-screen Filter message is sent out when the "select" event occurs on the object at runtime, which asks the message receivers to filter themselves using the default filter condition "*Current Field=Current Value*". You can edit the filter condition when specifying the message receivers.
* If you select Customize, you can define the message by yourself in the [Send Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098781-Send-Message-Dialog-Box).

  ![Send Message dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848402839/sndmsg.gif)

  1. Select a [trigger event](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Event) in the **Events** box, then select on the name of the event to select it.
  2. From the **Message** drop-down list, select [the message type](https://devnet.logianalytics.com/hc/en-us/articles/1500010060502-Send-Message-Web-Action-Builder-Dialog-Box#Message) to be sent out when the selected event occurs on the object at runtime.
  3. Define the message as you want.

     For the built-in message, you can edit the condition of how to perform the web action bound with the message in the **Value** column. To make the condition dynamic, select the values under the **Dynamic Key** node.

     For a user-defined message,

     1. Specify the ID and name of the message in the **ID** and **Name** text boxes. The ID should be a natural number beyond 1000.
     2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a message key-value line.
     3. In the **Key** column, specify a key from the drop-down list or select the **<Input...>** item from the list and then type a key in the text box.
     4. In the **Value** column, specify the value of the key from the drop-down list or select **<Input...>** from the list and then type a value in the text box.
     5. If you choose to type the value by yourself in the above step, you need to specify the data type of the value. If you select the value from the Value drop-down list, Designer automatically displays the data type of the value in the **Data Type** column and you cannot change it.
     6. You can add more key-value lines and specify the key, data type, and value in each line.

        To delete a message key-value line, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the message key-value lines, select a line and select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button.

     ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You can also create a blank user-defined message by only specifying the ID and name of the message.
  4. Repeat the above steps to define other messages that you want to send out from the object on different events.
  5. Select **OK** to accept the settings.

In addition to the above method, you can also use the Send Message web action to send out messages. To do this:

1. Do one of the following:
   * Right-click a data field or a label in a table/crosstab, or a label, a basic web control, a parameter control, or the Submit button of a parameter form control which is not in the library component's configuration panel, select **Display Type** from the shortcut menu. In the Display Type dialog box, select a trigger event from the drop-down list in the **Events** column and select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the **Actions** column.
   * In the **Behaviors** tab of some chart format dialog boxes, select a trigger event from the drop-down list in the Events column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the Actions column.
   * While creating or editing a geographic map, in the **Display** screen of the map wizard, select a group level and select the **Web Behaviors** button. In the Web Behaviors dialog box, select a trigger event from the drop-down list in the Events column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the Actions column.
2. In the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box), select **\*SendMessage** and select **OK**. Designer displays the [Send Message - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060502-Send-Message-Web-Action-Builder-Dialog-Box).

   ![Send Message - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856823447/sndmsgwbactnbld.gif)
3. [Define the message](#Message) that you want to trigger on the specified event.
4. Select **OK** to confirm the settings.
5. In the dialog box that you return to, add more event lines and repeat the above steps to specify to send out more messages as you want.
6. Select **OK** to finish defining the messages to send out.

## Receiving Messages

The data components (tables, charts, crosstabs, KPIs, and geographic maps) in a library component can receive messages that are sent out from the current library component or another one. When a data component receives a message at runtime, it performs the web actions defined in the message, such as filtering and sorting itself using conditions specified in the message, running the current or another library component with predefined parameter values, changing its object properties, removing filter conditions, or drilling through data.

To make a data component receive messages and respond corresponding web actions, take the following steps:

1. Right-click the data component and select **Receive Message** from the shortcut menu. Designer displays the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098381-Receive-Message-Dialog-Box).

   ![Receive Message dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848404375/rcvmsg.gif)
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a message line.
3. From the **Message ID** column, select the message you want the data component to receive.
   * [0001 - Filter](#BFilter)  
     When the data component receives this message, it filters itself based on the filter condition defined in the message.
   * [0002 - Sort](#BSort)  
     When the data component receives this message, it sorts itself based on the sort condition defined in the message. Not available to KPI.
   * [0003 - Parameter](#BParameter)  
     When the data component receives this message, the library component that contains the data component re-runs with the parameter values defined in the message.
   * [0004 - On-screen Filter](#BOnScreenFilter)  
     When the data component receives this message, it filters itself based on the filter condition defined in the message.
   * **User Defined**  
     A data component in a library component can also receive user-defined messages and then respond the web actions such as [Filter](#UFilter), [On-screen Filter](#UOnScreenFilter), [Remove Filter](#URemoveFilter), [Sort](#USort), [Parameter](#UParameter), [Change Property](#UProperty), [Go Down](#UGoDown), [Go Up](#UGoUp), and [Go To](#UGoTo).
4. If you select a built-in message, you cannot change the action the message responds, but you can edit how to perform the action as you want.

   If you select a user-defined message, you can specify the action the data component responds when it receives the message and define how to perform the action.
5. Repeat the above steps to add more messages to receive and define the actions to respond the messages.

   To delete a message, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the display order of the messages in the message box, select a message and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
6. Select **OK** to finish setting the messages the data component is going to receive.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) In the drop-down lists for editing the conditions to respond a message, you may find that some items have the icon ![Message Key icon](https://devnet.logianalytics.com/hc/article_attachments/4404848404759/btn_msgkey.gif) ahead of them and they are listed under the Message Key node. If you choose an item of this type, it means that at runtime Logi Report Engine does not use the item directly in a condition, instead it maps the item to a key in the message and finds the value that the report user specifies to the key from the message first and then uses that value to compose the condition.

The following explains in detail how to make a data component receive different messages:

**To receive the built-in Filter message:**

1. In the Receive Message dialog box, select **0001 - Filter** from the drop-down list in the **Message ID** column. Designer automatically applies the filter condition defined in the message.
2. If you want to edit the filter condition, select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif). Designer displays the [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096841-Filter-Dialog-Box).

   ![Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848405015/fltr2.gif)
3. Specify the filter condition by selecting the field on which the filter is based from the **Filter On** drop-down list, the operator to compose the condition from the **Operator** drop-down list, and the value of how to filter the field from the **Value** drop-down list (to specify the value by yourself, select **<Input...>** and type the value in the text box).

   When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more filter conditions to filter other field values and specify the relationship between the conditions in the **More** column.

   To delete a filter condition, select the condition and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the filter conditions, select a condition and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
5. Select **OK** to finish defining the filter conditions.

**To receive the built-in Sort message:**

1. In the Receive Message dialog box, select **0002 - Sort**  from the drop-down list in the **Message ID** column. Designer automatically applies the sort conditions defined in the message.
2. If you want to edit the sort condition, select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif). Designer displays the [Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060522-Sort-Dialog-Box).

   ![Receive Message dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856823959/sort.gif)
3. Specify the sort condition by selecting the field on which to sort the records from the **Sort On** drop-down list, and in which order to sort the records from the **Sort Value** drop-down list.
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more sort conditions to sort other fields.

   To delete a sort condition, select the condition and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the sort conditions, select a condition and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
5. Select **OK** to finish defining the sort conditions.

**To receive the built-in Parameter message:**

1. In the Receive Message dialog box, select **0003 - Parameter**  from the drop-down list in the **Message ID** column.
2. Choose a message type from the **Message Info** column: Automatic or Customized.
   * When you select **Automatic**, Designer automatically applies all the parameter values specified in the sent message. If you want to edit the parameters,
     1. Select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif). Designer displays the [Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060162-Parameter-Dialog-Box#BParam).

        ![Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856824215/prm2.gif)
     2. Specify the parameter and the value of the parameter from the **Parameter Name** and **Value** drop-down lists. The operator can only be "=".

        "Parameter Name\*" in the Parameter Name drop-down list means to re-run the library component using parameters defined in the sent message, and its corresponding value can only be "Parameter Value\*" that represents all the parameter values.
     3. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more parameter lines to specify other parameter values. If you specify a parameter value more than once, the last setting takes effect.

        To delete a parameter line, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the parameters, select a parameter line and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
     4. Select **OK** to accept the settings. Then at runtime, when the data component receives the message, the library component which contains it re-runs with all the predefined parameter values.
   * When you select **Customized**, Designer automatically applies the parameter value defined in the sent message. If you want to edit the parameter,
     1. Select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) to open the Parameter dialog box.

        ![Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856824471/prm1.gif)
     2. Specify the parameter and the value of the parameter from the **Parameter Name** and **Value** drop-down lists. The operator can only be "=".
     3. Select **OK** to accept the settings. Then at runtime, when the data component receives the message, the library component which contains it re-runs with the predefined parameter value.

**To receive the built-in On-screen Filter message:**

1. In the Receive Message dialog box, select **0004 - On-screen Filter** from the drop-down list in the **Message ID** column. Designer automatically applies the filter condition defined in the message.
2. If you want to edit the filter condition, select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif). Designer displays the [On-screen Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060022-On-screen-Filter-Dialog-Box).

   ![On-screen Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856824983/onscrnfltr.gif)
3. Specify the filter condition by selecting the field on which the filter is based from the **Filter On** drop-down list, and the value of how to filter the field from the **Value** drop-down list list (to specify the value by yourself, select **<Input...>** and type the value in the text box).

   When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more filter conditions to filter other field values.
   If a filter condition is not necessary, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).
5. Select **OK** to finish defining the filter conditions.

**To receive a user-defined message and respond the Filter web action:**

The Filter web action enables you to filter the records of the data component when it receives the message.

1. In the Receive Message dialog box, specify the ID and name of the user-defined message in the **Message ID** column and **Message Name** column respectively, then select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).
2. In the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box), select **\*Filter** in the **Action Name** column and select **OK**.
3. In the Filter dialog box, [specify the filter conditions](#BFilter) as required.
4. Select **OK** to accept the settings.

**To receive a user-defined message and respond the On-screen Filter web action:**

The On-screen Filter web action enables you to filter the records of the data component when it receives the message.

1. In the Receive Message dialog box, specify the ID and name of the user-defined message in the **Message ID** column and **Message Name** column respectively, then select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).
2. In the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box), select **\*On-screen Filter** in the **Action Name** column and select **OK**.
3. In the On-screen Filter dialog box, [specify the filter conditions](#BOnScreenFilter) as required.
4. Select **OK** to accept the settings.

**To receive a user-defined message and respond the Remove Filter web action:**

The Remove Filter web action enables you to remove filters from the data component when it receives the message.

1. In the Receive Message dialog box, specify the ID and name of the user-defined message in the **Message ID** column and **Message Name** column **separately**, then select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).
2. In the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box), select **\*Remove Filter** in the **Action Name** column and select **OK**. Designer displays the [Remove Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060262-Remove-Filter-Dialog-Box).

   ![Remove Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856825495/rmvfltr.gif)
3. Specify the filters you want to remove from the data component when it receives the message.

* **Remove Filters**  
  Select to remove the filters created via the Filter dialog box, the Filter option on a field’s shortcut menu, and the Filter web action.
* **Remove \*On-screen Filters**  
  Select to remove the filters created by the \*On-screen Filter web action.

4. By default, JDashboard removes all the on-screen filters from the data component when it receives the message at runtime if you select Remove \*On-screen Filters. If you only want to remove the filter conditions that are related to certain data fields, clear the **All Fields** option, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a condition line, select in the line and select a field from the drop-down list or select **<Input...>** and type the field name in the text box. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more fields. To delete an unwanted field, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).
5. Select **OK** to accept the settings.

**To receive a user-defined message and respond the Sort web action:**

The Sort web action enables you to sort the records of the data component when it receives the message.

1. In the Receive Message dialog box, specify the ID and name of the user-defined message in the **Message ID** column and **Message Name** column respectively, then select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).
2. In the Web Action List dialog box, select **\*Sort** in the **Action Name** column and select **OK**.
3. In the Sort dialog box, [specify the sort conditions](#BSort) as required.
4. Select **OK** to accept the settings.

**To receive a user-defined message and respond the Parameter web action:**

The Parameter web action enables you to run a library component, especially a library component with parameters using predefined parameter values, or re-run the current library component with predefined parameter values when the message is received.

1. In the Receive Message dialog box, specify the ID and name of the user-defined message in the **Message ID** column and **Message Name** column **separately**, then select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).
2. In the Web Action List dialog box, select **\*Parameter** in the **Action Name** column and select **OK**. Designer displays the [Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060162-Parameter-Dialog-Box#UParam).

   ![Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848405655/prm.gif)
3. Specify the handler to receive the parameters of the web action. The handler may be the default one in the current Server, or in another Server specified by **Customized Path**.
4. Specify whether to apply the action to run another library component or refresh the current. If you choose to run another library component, select the **Browse** button to specify the library component, then select the window or frame in which to open the library component from the **Target Frame** drop-down list.
5. If the specified library component contains parameters, Designer automatically lists the parameters in the parameters box. Specify the value for each parameter. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more parameter lines to specify other parameter values.

   To delete a parameter line, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the parameters, select a parameter line and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
6. Select **OK** to accept the settings.

**To receive a user-defined message and respond the Change Property web action:**

The Change Property web action enables you to change properties of the data component when it receives the message.

1. In the Receive Message dialog box, specify the ID and name of the user-defined message in the **Message ID** column and **Message Name** column respectively, then select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).
2. In the Web Action List dialog box, select **\*Property** in the **Action Name** column and select **OK**. Designer displays the [Change Property dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058142-Change-Property-Dialog-Box).

   ![Change Property dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848405911/chgpty.gif)
3. Specify the property you want to change and the value for it respectively from the **Properties** and **Value** drop-down lists. You can also type the property name by yourself. You can only change the properties of the data component itself at runtime.
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more property conditions to change values of other properties.

   To delete a property condition, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the property conditions, select a property line and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
5. Select **OK** to accept the settings.

**To receive a user-defined message and respond the Go Down web action:**

The Go Down web action enables you to drill data of the data component to a lower-level group according to the predefined [hierarchy](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business view the data component uses when it receives the message. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

1. In the Receive Message dialog box, specify the ID and name of the user-defined message in the **Message ID** column and **Message Name** column respectively, then select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).
2. In the Web Action List dialog box, select **\*Go Down** in the **Action Name** column and select **OK**. Designer displays the [Go Down dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059482-Go-Down-Dialog-Box).

   ![Go Down dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856826007/godwn.gif)
3. In the **Go Down On** column, select the group on which to perform the go-down action. For a geographic map, it is **Current Layer** and you cannot change it.
4. In the **Use Hierarchy** column, select the hierarchy based on which to perform the go-down action.
   You can also use a web control in the library component to retrieve a hierarchy name at runtime. For a geographic map, the **Built-in** hierarchy is used and you cannot change it.
5. In the **By Value** column, type a value of the specified group field to go down to the lower level with the filter condition "*SpecifiedGroupField=TheValue*". You can also use a web control to retrieve a value at runtime.
6. Select **OK** to accept the settings.

**To receive a user-defined message and respond the Go Up web action:**

The Go Up web action enables you to drill data of the data component to a upper-level group according to the predefined [hierarchy](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business view the data component uses when it receives the message. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

1. In the Receive Message dialog box, specify the ID and name of the user-defined message in the **Message ID** column and **Message Name** column respectively, then select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).
2. In the Web Action List dialog box, select **\*Go Up** in the **Action Name** column and select **OK**. Designer displays the [Go Up dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097421-Go-Up-Dialog-Box).

   ![Go Up dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856826519/goup.gif)
3. In the **Go Up On** column, select the group on which to perform the go-up action. For a geographic map, it is **Current Layer** and you cannot change it.
4. In the **Use Hierarchy** column, select the hierarchy according to which to perform the go-up action.
   You can also use a web control in the library component to retrieve a hierarchy name at runtime. For a geographic map, the **Built-in** hierarchy is used and you cannot change it.
5. Select **OK** to accept the settings.

**To receive a user-defined message and respond the Go To web action:**

The Go To web action enables you to change a data field of the data component when it receives the message. It is available to tables, charts, and crosstabs.

1. In the Receive Message dialog box, specify the ID and name of the user-defined message in the **Message ID** column and **Message Name** column respectively, then select in the **Actions** column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).
2. In the Web Action List dialog box, select **\*Go To** in the **Action Name** column and select **OK**. Designer displays the [Go To dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059522-Go-To-Dialog-Box).

   ![Go To dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848406423/goto.gif)
3. In the **Go To On** column, select the field on which to perform the go-to action.
4. In the **To Column** column, select another field to change the "Go To On" field to.
   You can also use a web control in the library component to retrieve a field name at runtime.
5. To apply the go-to action by filtering the "Go To On" field at the same time, select the **By Value** checkbox and then type the value by which to filter the field or select a web control in the library component to retrieve the value at runtime. Skip this step if you select to perform the action on a crosstab aggregate field.
6. Select **OK** to accept the settings.

## Example of Delivering a Message

This example demonstrates how you can deliver a filter user-defined message between two library components in order to synchronize the data components in them. It contains the following tasks:

* [Task 1: Create two library components](#Task1)
* [Task 2: Send out a filter user-defined message from the chart](#Task2)
* [Task 3: Make the two data components receive the same message](#Task3)
* [Task 4: Publish the library components](#Task4)
* [Task 5: Deliver the message in a dashboard for data synchronization](#Task5)

**Task 1: Create two library components**

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Use the business view **SaleStat** in Data Source 1 to [create two library components](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#LC) and save them as "Component 1.lc" and "Component 2.lc".

   For Component 1, create a chart which displays in the clustered bar 2-D chart type, shows Assigned Region on X-Axis and Total Actual as Bar Length. For Component 2, create a crosstab using Order ID and Assigned Region respectively as the row and column fields, and Total Actual as the summary field. Apply the style Commercial to both of them.

**Task 2: Send out a filter user-defined message from the chart**

In this task, we send a filter user-defined message from the chart in Component 1 when the "select" event occurs on any legend entry value.

1. Open **Component 1.lc**.
2. Double-click any bar of the chart, then in the **Fill** tab of the Format Bar dialog box, select **Vary Colors by Color List** to make the bar colors vary. Select **OK** to accept the change and close the dialog box.
3. Right-click the chart legend and select **Send Message** > **Customize**  on the shortcut menu. Designer displays the Send Message dialog box.
4. In the **Events** box, select **Select** as the trigger event, then select on the event to activate the message options on the right.
5. From the **Message** drop-down list, select **User Defined**, then type **1001** and **Filter - Assigned Region** as the message ID and name.
6. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a message line.
7. Select the **<Input>** item from the drop-down list in the **Key** column and type **Assigned Region** in the text box.
8. Select **Current Value** from the drop-down list in the **Value** column. Designer displays **String** automatically in the **Data Type** column.

   ![Send Message dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848406935/rpt_lc_msg_eg_send.gif)
9. Select **OK** to finish defining the message to send out from the chart.
10. Save the library component.

**Task 3: Make the two data components receive the same message**

In this task, we make the chart and crosstab in the two library components receive the same filter message to filter on the Assigned Region values when they receive the message that is sent out from a chart legend entry.

1. Right-click the chart platform and select **Receive Message** from the shortcut menu. Designer displays the Receive Message dialog box.
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a message line.
3. Select the **<Input>** item from the drop-down list in the **Message ID** column, then type **1001** in the text box.
4. Type **Filter - Assigned Region** in the text box of the **Message Name** column.
5. Select the blank text box in the **Actions** column, then select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif).

   ![Receive Message dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856826903/rpt_lc_msg_eg_recv1.gif)
6. In the Web Action List dialog box, select **\*Filter** and select **OK**. Designer displays the Filter dialog box.
7. Select **Assigned Region** from the **Filter On** drop-down list, keep the default operator, then select **<Input>** under the **Message Key** node in the **Value** drop-down list and type **Assigned Region** in the text box.

   ![Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848407191/rpt_lc_msg_eg_recv2.gif)
8. Select **OK** to go back to the Receive Message dialog box. The message Component 1 receives is defined as follows:

   ![Receive Message dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848407447/rpt_lc_msg_eg_recv3.gif)
9. Select **OK**, then save the library component.
10. Open **Component 2.lc**.
11. Right-click the crosstab and select **Receive Message** from the shortcut menu.
12. In the Receive Message dialog box, specify the message the crosstab receives [as shown above](#Chart).
13. Save the two library components.

**Task 4: Publish the library components**

Start Server and publish the library components along with the catalog SampleReports.cat to the component library in Server. For more information about publishing resources from Designer to Server, see [Publishing Resources Remotely](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#Remotely).

**Task 5: Deliver the message in a dashboard for data synchronization**

1. Open the Server Console > Resources page, select **New** > **Dashboard** on the task bar. Server creates a blank dashboard in JDashboard.
2. In the Resources panel, browse to the folder where you have published the two library components.
3. Drag and drop the two library components to the dashboard.

   ![Components in Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404856827159/rpt_lc_msg_eg_msg1.gif)
4. Select **Asia-Pacific** in the chart legend to send out the message. Logi Report Engine filters both the chart and the crosstab to show data in the Asia-Pacific region only.

   ![Data in the Asia-Pacific Region for Chart and Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404856827415/rpt_lc_msg_eg_msg2.gif)
5. Select the **Clear Filters** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404848408727/rpt_lc_msg_eg_clrfltr.gif) on the toolbar to clear the filter in both components.
6. Select **Europe, Middle East, Africa** in the chart legend. The chart and crosstab now shows data for this region.

   ![Data in Europe, Middle East, and Africa for Chart and Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404848408983/rpt_lc_msg_eg_msg3.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101161-Creating-Bursting-Reports)
