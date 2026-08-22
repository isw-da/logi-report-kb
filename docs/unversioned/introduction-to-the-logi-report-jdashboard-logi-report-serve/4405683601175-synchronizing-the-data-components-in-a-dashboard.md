---
title: "Synchronizing the Data Components in a Dashboard"
id: 4405683601175
section: "Introduction to the Logi Report JDashboard Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683601175-Synchronizing-the-Data-Components-in-a-Dashboard
updated_at: 2022-01-27T07:58:33Z
---

# Synchronizing the Data Components in a Dashboard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690496279-Manipulating-Data-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690494487-Filtering-the-Data-Components-in-a-Dashboard)

# Synchronizing the Data Components in a Dashboard

This topic describes how to synchronize data components in a dashboard by sending and receiving built-in messages and customized messages.

It is important for different parts of a visualization to be fully consistent. When you filter or sort on any data, you will want this to be reflected on all or a certain set of data components (crosstabs, tables, charts, KPIs, and geographic maps) in the same dashboard. You achieve this synchronization when you send and receive messages between library components in a dashboard.

The messages that can be sent and received in a dashboard for synchronization includes the built-in messages Filter, Sort, Parameter, and On-screen Filter, and user customized messages. The built-in messages are predefined with corresponding web actions.

You can also predefine to send and receive messages when you create library components in Logi Report Designer. For more information, see Delivering Messages Between Library Components in the *Logi Report Designer Guide*.

This topic contains the following sections:

* [Sending Synchronization](#Send)
  + [Introduction to Built-In Messages](#BuiltInMessage)
  + [Sending Out a Built-In Message](#SendBuiltIn)
  + [Sending Out a Customized Message](#SendSync)
* [Receiving Synchronization](#Receive)

## Sending Synchronization

You can send out synchronization messages from specific objects in a dashboard, which include independent labels (labels outside of data components), labels in tables/crosstabs/KPIs, data fields, special fields, data markers, legend and category axis labels of charts, markers and areas in geographic maps, parameter controls, and the Submit button of parameter form controls. These objects are the synchronization trigger objects.

You can send out synchronization messages automatically using built-in messages or define customized messages on your own. In a customized message you can specify to send out multiple messages from one trigger object and edit the message information as you want.

### Introduction to Built-In Messages

Logi Report provides the following built-in messages:

* **Filter**  
   You send out the built-in Filter message to ask the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two Filter messages one after another, the latest always replaces the earlier.
* **Sort**  
   You send out the built-in Sort message to ask the message receivers to sort themselves according to the sort condition defined in the message.
* **Parameter**  
   You send out the built-in Parameter message to ask the message receivers to re-run using the available parameter values in the message.
* **On-screen Filter**  
   You send out the built-in On-screen Filter message to ask the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two On-screen Filter messages one after another, JDashboard combines the filter conditions in the two messages using the AND logic. However, if the two conditions conflict with each other, for example, the first is *Country=USA* and the second *City=London*, JDashboard will clear the first and apply the second filter condition *City=London* to the data component.

When a data component receives a Filter message and an On-screen Filter message, JDashboard combines the filter conditions in the two messages using the AND Logic. If the On-screen Filter message comes after the Filter message, JDashboard obtains the value list of the On-screen Filter from the data component after applying the Filter message to it. However, if the Filter message comes after the On-screen Filter message, the value list of the Filter is from the data component before JDashboard applies the On-screen Filter, which may result in null data.

The following examples show how Filter messages, On-screen Filter messages, and the combination of the two types work.

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

### Sending Out a Built-In Message

Select a trigger object, right-click it and select **Send Sync** > **Filter**/**Sort**/**Parameter****/On-screen Filter** on the shortcut menu (for the Submit button of a parameter form control, you can only select Parameter). Then when you select the trigger object, JDashboard sends out the corresponding built-in message. If the trigger object is an independent label, you need to manually [specify the message receivers](#Receive); if it is one of the other objects, data components in the current dashboard will automatically receive the message as follows:

* For the Filter or On-screen Filter message, Logi Report will determine the data components that can automatically receive the message and filter them according to the default filter condition *Current Field=Current Value*. For example, the data components that contain the business view object the display name or instance name of which is the same as that of the trigger object are able to automatically receive the message and filter the business view object based on the clicked value of the trigger object.
* For the Sort message, Logi Report will determine the data components that can automatically receive the message and sort them based on the default sort condition *Current Field Ascending*. For example, the data components that contain the business view object the display name or instance name of which is the same as that of the trigger object are able to automatically receive the message and sort values of the business view object in the ascending order.
* For the Parameter message, it will include all the available parameters of the library component in which the trigger object is. The data components that contain any of the parameters will automatically receive the message and re-run with the parameter values in the message. However, to make the Parameter message meaningful, you should insert a parameter form control into the library component that is the message sender to include all the parameters of the library component, thus when the data components receive the message, they can use the parameter values in the parameter form control to re-run.

If you want to view or edit the message a data component automatically receives, you can [make use of its Receive Sync](#Receive) dialog box. While for the Parameter message, if a library component contains several data components, JDashboard displays the dialog box only on the first data component in the library component.

### Sending Out a Customized Message

1. Right-click a trigger object and select **Send Sync** > **Customize** from the shortcut menu. JDashboard displays the [Send Sync](https://devnet.logianalytics.com/hc/en-us/articles/4405683723543-Send-Sync-Dialog-Box-Properties) dialog box.

   ![Send Sync dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453604887/sndsync.gif)
2. In the message box on the left, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) to add a message line, select the type of the message from the M**essage Type** drop-down list, which can be one of the built-in messages Filter, Sort, Parameter, and On-screen Filter, or User Defined. JDashboard displays a message name automatically in the Message Name column. You can double-click in the column to edit the message name.

   If the object has been predefined to send messages in Logi Report Designer, JDashboard will list them in the message box, marking with ![Lock button](https://devnet.logianalytics.com/hc/article_attachments/4420447274135/btn_dshbrd_lock.gif), and you cannot modify them.
3. In the message information box on the right, define the message.
   * For the Filter message, specify the field to be filtered, the filter operator, and the value using which to filter the field. To make the condition dynamic, select the values under the Dynamic Key node.
   * For the Sort message, specify the field to be sorted and the sort order. To make the condition dynamic, select the values under the **Dynamic Key** node.
   * For the Parameter message, specify the parameter name and value. To make the condition dynamic, select the values under the Dynamic Key node.
   * For the On-screen Filter message, specify the field to be filtered and the value using which to filter the field. To make the condition dynamic, select the values under the Dynamic Key node.
   * For a user defined message,
     1. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) above the message information box to add a message key-value line.
     2. In the **Key Name** column, specify a key from the drop-down list, or select the **<Input...>** item from the list and then type a key in the text box. To make the condition dynamic, select the values under the Dynamic Key node.
     3. In the **Value** column, specify the value of the key from the drop-down list, or select **<Input...>** from the list and then type a value into the text box. To make the condition dynamic, select the values under the Dynamic Key node.
     4. You can add more key-value lines and specify the key and value in each line.

        To delete a message key-value line, select it, and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420447268631/btn_dshbrd_rmv1.gif).

     **Tip:** You can also create a blank user defined message without specifying the key and value.
4. Repeat the preceding two steps to add more messages on the object.

   To delete a message, select it, and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420447268631/btn_dshbrd_rmv1.gif) above the message box. You cannot remove messages predefined in Logi Report Designer.

   To disable some messages, clear the checkboxes in the **Enable** column. JDashboard will not trigger disabled messages.
5. Select **OK** to accept the settings.

## Receiving Synchronization

You can use the data components (tables, charts, crosstabs, KPIs, and geographic maps) in a dashboard as the message receivers to receive messages that any objects in the dashboard sent out. When a data component receives a message, it will perform the actions defined in the message, such as filtering, sorting itself using conditions defined in the message, re-running with parameter values in the message, changing its object properties, removing filter conditions applied on it, and going to a lower or upper level of its data. You can make multiple data components receive the same message and respond to the same action with the same conditions, to achieve data synchronization between the data components.

To make a data component in a dashboard receive messages and respond to corresponding web actions, take the following steps:

1. Right-click anywhere on a data component and select **Receive Sync** from the shortcut menu. Server displays the [Receive Sync](https://devnet.logianalytics.com/hc/en-us/articles/4405683719063-Receive-Sync-Dialog-Box-Properties) dialog box.

   ![Receive Sync dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461679127/rcvsync.gif)

   If the data component has been predefined to receive messages in Logi Report Designer, JDashboard will list them in the dialog box and mark them with ![Lock button](https://devnet.logianalytics.com/hc/article_attachments/4420447274135/btn_dshbrd_lock.gif).
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) to add a message line.
3. The **Sync From** drop-down list displays all the trigger objects in the current dashboard. Select the trigger object that sent out the message which you want the data component to receive.
4. JDashboard lists the messages that have been defined on the selected trigger object, in the **Message Name** drop-down list. Select the message the data component is going to receive. If the selected message is a built-in message, JDashboard displays the action that is bound with the message, in
   the **Actions** column.
5. You can double-click in the **Action Description** column to add a description for the action the message will respond.
6. Specify how you want the data component to respond when it receives the message.
   * If the to be received message is a built-in Filter message, the data component will filter itself according to the filter conditions defined in the message. You can further [edit the filter conditions](#BFilter) if you want.
   * If the to be received message is a built-in Sort message, the data component will sort itself according to the sort conditions defined in the message. You can further [edit the sort conditions](#BSort) if you want.
   * If the to be received message is a built-in Parameter message, the data component will re-run using the parameter values in the message. You can further [edit the parameter values](#BParameter) if you want.
   * If the to be received message is a built-in On-screen Filter message, the data component will filter itself according to the filter conditions defined in the message. You can further [edit the filter conditions](#BOnScreenFilter) if you want.
   * If the to be received message is a user defined message, you can specify the web action the data component will respond to when it receives the message and define how to perform the action. You can specify the following web actions: [Filter](#UFilter), [On-screen Filter](#UOnScreenFilter), [Remove Filter](#URemoveFilter), [Sort](#USort), [Parameter](#UParameter), [Property](#UProperty), [Go Down](#UGoDown), [Go Up](#UGoUp), and [Go To](#UGoTo).
7. Repeat the preceding steps to add more messages to receive and define how to respond to the messages.

   To delete a message, select it, and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420447268631/btn_dshbrd_rmv1.gif) above the message information box. You cannot remove the messages that were predefined in Logi Report Designer.

   To disable some messages, clear them in the **Enable** column. The data component will not receive disabled messages.
8. Select **OK** to accept the settings and close the dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) In the drop-down lists for editing the conditions to respond a message, you may find that some items under the **Message Key** node have the icon ![Message Key icon](https://devnet.logianalytics.com/hc/article_attachments/4420461722647/btn_dshbrd_msgkey.gif) ahead of them. If you choose an item of this type, JDashboard will not use the item directly in a condition, instead map it to a key in the message. JDashboard will find the value that is specified to the key from the message first and then use that value to compose the condition.

**To edit the filter conditions for the built-in Filter message:**

1. In the Receive Sync dialog box, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the **Actions** column. JDashboard displays the [Web Action - Filter](https://devnet.logianalytics.com/hc/en-us/articles/4405690543767-Web-Action-Filter-Dialog-Box-Properties) dialog box.

   ![Web Action - Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453603351/wbactn_fltr.gif)
2. Specify the filter condition by selecting the field on which the filter will be based from the **Filter On** drop-down list, the operator to compose the condition from the **Operator** drop-down list, and the value of how to filter the field from the **Value** drop-down list.

   If you choose to type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
3. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) to add more filter conditions to filter other field values and then specify the relationship between the conditions in the **More** column.

   To delete a filter condition, select the condition and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420447268631/btn_dshbrd_rmv1.gif).
4. Select **OK** to finish defining the filter conditions.

**To edit the sort conditions for the built-in Sort message:**

1. In the Receive Sync dialog box, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the **Actions** column. JDashboard displays the [Web Action - Sort](https://devnet.logianalytics.com/hc/en-us/articles/4405683732247-Web-Action-Sort-Dialog-Box-Properties) dialog box.

   ![Web Action - Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447268119/wbactn_sort.gif)
2. Specify the sort condition by selecting the field on which to sort the records from the **Sort On** drop-down list, and in which order to sort the records from the **Sort Value** drop-down list.
3. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) to add more sort conditions to sort other fields.

   To delete a sort condition, select the condition and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420447268631/btn_dshbrd_rmv1.gif).
4. Select **OK** to finish defining the sort conditions.

**To edit the parameter values for the built-in Parameter message:**

1. In the Receive Sync dialog box, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column. JDashboard displays the [Web Action - Parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405683730199-Web-Action-Parameter-Dialog-Box-Properties) dialog box.

   ![Web Action - Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447270807/wbactn_param.gif)
2. Specify the parameter and the value of the parameter from the **Parameter Name** and **Parameter Value** drop-down lists. The operator can only be **=**.

   **Parameter Name\*** in the **Parameter Name** drop-down list means that JDashboard will use all the parameters defined in the message to re-run the data component, and its corresponding value can only be **Parameter Value\*** that represents all the parameter values.
3. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) to add more parameter lines to specify other parameter values. If you specify a parameter value more than once, the last setting takes effect.

   To delete a parameter line, select it, and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420447268631/btn_dshbrd_rmv1.gif).
4. Select **OK** to accept the settings. Then at runtime, when the data component receives the message, it will re-run itself, using the predefined parameter values.

**To edit the filter conditions for the built-in On-screen Filter message:**

1. In the Receive Sync dialog box, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column. JDashboard displays the [Web Action - On-screen Filter](https://devnet.logianalytics.com/hc/en-us/articles/4405683729175-Web-Action-On-screen-Filter-Dialog-Box-Properties) dialog box.

   ![Web Action - On-screen Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453602199/wbactn_onscrnfltr.gif)
2. Specify the filter condition by selecting the field on which the filter will be based from the **Filter On** drop-down list and the value of how to filter the field from the **Value** drop-down list.

   If you choose to type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
3. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) to add more filter conditions to filter other field values.

   To delete a filter condition, select the condition and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420447268631/btn_dshbrd_rmv1.gif).
4. Select **OK** to finish defining the filter conditions.

**To respond the Filter web action for a user defined message:**

You can use the **Filter** web action to filter the records of the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*Filter** from the drop-down list of the **Actions** column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action - Filter dialog box, [specify the filter condition](#BFilter).
3. Select **OK** to accept the settings.

**To respond the On-screen Filter web action for a user defined message:**

You can use the **On-screen Filter** web action to filter the records of the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*On-screen Filter** from the drop-down list of the **Actions** column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action - On-screen Filter dialog box, [specify the filter condition](#BOnScreenFilter).
3. Select **OK** to accept the settings.

**To respond the Remove Filter web action for a user defined message:**

You can use the **Remove Filter** web action to remove the filters from the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*Remove Filter** from the drop-down list of the **Actions** column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column. JDashboard displays the [Web Action - Remove Filter](https://devnet.logianalytics.com/hc/en-us/articles/4405683731223-Web-Action-Remove-Filter-Dialog-Box-Properties) dialog box.

   ![Web Action - Remove Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447268887/wbactn_rmvfltr.gif)
2. Specify the filters you want to remove from the data component: to remove the filters that are created via the [Filter option on a field’s shortcut menu](https://devnet.logianalytics.com/hc/en-us/articles/4405690496279-Manipulating-Data-Components#Filter), the Filter web action, and the Filter dialog box, select **Remove Filters**; to remove the on-screen filters created by the On-screen Filter web action, select **Remove \*On-screen Filters**.
3. By default, JDashboard will remove all the on-screen filters from the data component when you select **Remove \*On-screen Filters**. If you want to only remove the filter conditions that are related to certain data fields, clear the **All Fields** option, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) to add a condition line, select in the line and select a field from the drop-down list or select **<Input...>** and type the field name manually. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) to add more fields. To remove an unwanted field, select it, and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420447268631/btn_dshbrd_rmv1.gif).
4. Select **OK** to accept the settings.

**To respond the Sort web action for a user defined message:**

You can use the **Sort** web action to sort the records of the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*Sort** from the drop-down list of the **Actions** column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action - Sort dialog box, [specify the sort condition](#BSort).
3. Select **OK** to accept the settings.

**To respond the Parameter web action for a user defined message:**

You can use the **Parameter** web action to run a data component, especially a data component with parameters using predefined parameter values, or re-run the data component with predefined parameter values when the data component receives the message.

1. In the Receive Sync dialog box, select **\*Parameter** from the drop-down list of the **Actions** column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action - Parameter dialog box, [specify the parameters](#BParameter).

   If the specified data component contains parameters, JDashboard will list the parameters in the parameters box. Specify the value for each parameter.
3. Select **OK** to accept the settings.

**To respond the Property web action for a user defined message:**

You can use the **Property** web action to change the properties of the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*Property** from the drop-down list of the **Actions** column.
2. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column. JDashboard displays the [Web Action - Change Property](https://devnet.logianalytics.com/hc/en-us/articles/4405683725207-Web-Action-Change-Property-Dialog-Box-Properties) dialog box.

   ![Web Action - Change Property dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461675671/wbactn_prpty.gif)
3. Specify the property you want to change and the value for it respectively from the **Properties** and **Value** drop-down lists. You can only change the properties of the data component itself.
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447268375/btn_dshbrd_add1.gif) to add more property lines to change the values of other properties.

   To delete a property line, select it, and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420447268631/btn_dshbrd_rmv1.gif).
5. Select **OK** to accept the settings.

**To respond the Go Down web action for a user defined message:**

You can use the **Go Down** web action to drill data of the data component to the lower-level group according to a predefined hierarchy in the business view the data component uses when the data component receives the message. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

1. In the Receive Sync dialog box, select **\*Go Down** from the drop-down list of the **Actions** column.
2. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column. JDashboard displays the [Web Action - Go Down](https://devnet.logianalytics.com/hc/en-us/articles/4405690544663-Web-Action-Go-Down-Dialog-Box-Properties) dialog box.

   ![Web Action - Go Down dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453602967/wbactn_godwn.gif)
3. In the **Go Down On** column, select the group on which the go-down action will occur. For a geographic map, it is Current Layer and you cannot change it.
4. In the **Use Hierarchy** column, select the hierarchy based on which the go-down action will occur.
   You can also use a web control in the dashboard to retrieve a hierarchy name. For a geographic map, JDashboard applies the Built-in hierarchy and you cannot change it.
5. In the **By Value** column, type a value of the specified group field to go down to the lower level with the filter condition *SpecifiedGroupField=TheValue*. You can also use a web control to retrieve a value.
6. Select **OK** to accept the settings.

**To respond the Go Up web action for a user defined message:**

You can use the **Go Up** web action to drill data of the data component to the upper-level group according to a predefined hierarchy in the business view the data component uses when the data component receives the message. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

1. In the Receive Sync dialog box, select **\*Go Up** from the drop-down list of the **Actions** column.
2. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column. JDashboard displays the [Web Action - Go Up](https://devnet.logianalytics.com/hc/en-us/articles/4405683728151-Web-Action-Go-Up-Dialog-Box-Properties) dialog box.

   ![Web Action - Go Up dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453602711/wbactn_goup.gif)
3. In the **Go Up On** column, select the group on which the go-up action will occur. For a geographic map, it is Current Layer and you cannot change it.
4. In the **Use Hierarchy** column, select the hierarchy that the go-up action will occur according to. You can also use a web control in the dashboard to retrieve a hierarchy name. For a geographic map, JDashboard applies the Built-in hierarchy and you cannot change it.
5. Select **OK** to accept the settings.

**To respond the Go To web action for a user defined message:**

You can use the **Go To** web action to change a data field of the data component when it receives the message. It is available to tables, charts and crosstabs.

1. In the Receive Sync dialog box, select **\*Go To** from the drop-down list of the **Actions** column.
2. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420447267735/btn_dshbrd_edt1.gif) in the Actions column. JDashboard displays the [Web Action - Go To](https://devnet.logianalytics.com/hc/en-us/articles/4405683727127-Web-Action-Go-To-Dialog-Box-Properties) dialog box.

   ![Web Action - Go To dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461674775/wbactn_goto.gif)
3. In the **Go To On** column, select the field on which the go-to action will occur.
4. In the **To Column** column, select another field to change the **Go To On** field to. You can also use a web control in the dashboard to retrieve a field name.
5. To perform the go-to action by filtering the **Go To On** field at the same time, select **By Value** and then type the value by which to filter the field or select a web control to retrieve the value at runtime. Skip this step if you select to perform the action on a crosstab aggregate field.
6. Select **OK** to accept the settings.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690496279-Manipulating-Data-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690494487-Filtering-the-Data-Components-in-a-Dashboard)
