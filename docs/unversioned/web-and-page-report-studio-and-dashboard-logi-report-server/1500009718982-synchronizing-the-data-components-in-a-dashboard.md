---
title: "Synchronizing the Data Components in a Dashboard"
id: 1500009718982
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718982-Synchronizing-the-Data-Components-in-a-Dashboard
updated_at: 2021-07-25T07:20:12Z
---

# Synchronizing the Data Components in a Dashboard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718922-Manipulating-Data-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745061-Filtering-the-Data-Components-in-a-Dashboard)

# Synchronizing the Data Components in a Dashboard

It is important for different parts of a visualization to be fully consistent. When you filter or sort on any data, you will want this to be reflected on all or a certain set of data components (crosstabs, tables, charts, KPIs and geographic maps) in the same dashboard. Logi Report allows you to achieve the synchronization by means of sending and receiving messages in a dashboard.

The messages that can be sent and received in a dashboard for synchronization includes the built-in messages Filter, Sort, Parameter and On-screen Filter, and user customized messages. The built-in messages are predefined with corresponding web actions.

Sending and receiving messages can also be predefined when creating library components in Logi Report Designer. For details, refer to Delivering Messages Between Library Components in the *Logi Report Designer Guide*.

Select the following links to view the topics:

* [Sending Synchronization](#Send)
* [Receiving Synchronization](#Receive)

## Sending Synchronization

Synchronization messages can be sent out when selecting specific objects in a dashboard, which include independent labels (labels outside of data components), labels in tables/crosstabs/KPIs, data fields, special fields, data markers, legend and category axis labels of charts, markers and areas in geographic maps, parameter controls, and the Submit button of parameter form controls. These objects are referred to as the synchronization trigger objects.

You can send out synchronization messages automatically using built-in messages or define customized messages on your own. In a customized message you can specify to send out multiple messages from one trigger object and edit the message information as you want. The following built-in messages are provided:

* **Filter**  
   The built-in Filter message is sent out for asking the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two Filter messages one after another, the latest always replaces the earlier.
* **Sort**  
   The built-in Sort message is sent out for asking the message receivers to sort themselves according to the sort condition defined in the message.
* **Parameter**  
   The built-in Parameter message is sent out for asking the message receivers to re-run using the available parameter values in the message.
* **On-screen Filter**  
   The built-in On-screen Filter message is sent out for asking the message receivers to filter themselves according to the filter condition defined in the message. When a data component receives two On-screen Filter messages one after another, the filter conditions in the two messages are combined using the AND logic. However if the two conditions conflict with each other, for example, the first is *Country=USA* and the second *City=London*, the first will be cleared and the final filter condition applied to the data component will be *City=London*.

When a data component receives a Filter message and an On-screen Filter message, the filter conditions in the two messages are combined using the AND Logic. If the On-screen Filter message comes after the Filter message, the value list of the On-screen Filter is obtained from the data component after being applied the Filter message. However if the Filter message comes after the On-screen Filter message, the value list of the Filter is from the data component before being applied the On-screen Filter, which may result in null data.

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

**To send out a built-in synchronization message:**

Select a trigger object, right-click it and select **Send Sync** > **Filter**/**Sort**/**Parameter****/On-screen Filter** on the shortcut menu (for the Submit button of a parameter form control, only Parameter is available). Then when the trigger object is clicked, a corresponding built-in message will be sent out. If the trigger object is an independent label, you need to manually [specify the message receivers](#Receive); if it is one of the other objects, the message will be automatically received by data components in the current dashboard as follows:

* For the Filter or On-screen Filter message, Logi Report will determine the data components that can automatically receive the message and make them filtered according to the default filter condition *"Current Field=Current Value*". For example, the data components that contain the business view object the display name or instance name of which is the same as that of the trigger object are able to automatically receive the message and filter the business view object based on the clicked value of the trigger object.
* For the Sort message, Logi Report will determine the data components that can automatically receive the message and make them sorted based on the default sort condition *"Current Field Ascending"*. For example, the data components that contain the business view object the display name or instance name of which is the same as that of the trigger object are able to automatically receive the message and sort values of the business view object in ascending order.
* For a Parameter message, it will include all the available parameters used by the library component in which the trigger object is placed. The data components that contain any of the parameters will automatically receive the message and re-run with the parameter values in the message. However to make the Parameter message meaningful, you are recommended to insert a parameter form control into the library component of the message sender to include all the parameters used by the library component, thus when the data components receive the message, they can use the parameter values provided in the parameter form control to re-run.

If you want to view or edit the message a data component automatically receives, you can [make use of its Receive Sync](#Receive) dialog box. While for the Parameter message, if some data components are contained in one library component, the dialog box is only available on the first data component in the library component.

**To send out a customized message**:

1. Right-click a trigger object and select **Send Sync** > **Customize** from the shortcut menu. Report Server displays the [Send Sync](https://devnet.logianalytics.com/hc/en-us/articles/1500009747101-Send-Sync) dialog box.

   ![Send Sync dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936891671/sndsync.gif)
2. In the message box on the left, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) to add a message line, select the type of the message from the Message Type drop-down list, which can be one of the built-in messages Filter, Sort, Parameter and On-screen Filter, or User Defined. A message name is then automatically displayed in the Message Name column. You can double-click in the column to edit the message name.

   If the object has been predefined to send messages in Logi Report Designer, they will be listed in the message box marked with ![Lock button](https://devnet.logianalytics.com/hc/article_attachments/4404936891927/btn_dshbrd_lock.gif) and you cannot modify them.
3. In the message information box on the right, define the message as you want.
   * For the Filter message, specify the field to be filtered, the filter operator and the value using which to filter the field. To make the condition dynamic, select the values under the Dynamic Key node.
   * For the Sort message, specify the field to be sorted and the sort order. To make the condition dynamic, select the values under the Dynamic Key node.
   * For the Parameter message, specify the parameter name and value. To make the condition dynamic, select the values under the Dynamic Key node.
   * For the On-screen Filter message, specify the field to be filtered and the value using which to filter the field. To make the condition dynamic, select the values under the Dynamic Key node.
   * For a user defined message,
     1. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) above the message information box to add a message key-value line.
     2. In the Key Name column, specify a key from the drop-down list or select the **<Input...>** item from the list and then type a key into the text box. To make the condition dynamic, select the values under the Dynamic Key node.
     3. In the Value column, specify the value of the key from the drop-down list or select **<Input...>** from the list and then type a value into the text box. To make the condition dynamic, select the values under the Dynamic Key node.
     4. You can add more key-value lines and specify the key and value in each line.

        To delete a message key-value line, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404942567703/btn_dshbrd_rmv1.gif).

     **Tip:** You can also create a blank user defined message without specifying the key and value.
4. Repeat the above two steps to add more messages on the object.

   To delete a message, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404942567703/btn_dshbrd_rmv1.gif) above the message box. Messages predefined in Logi Report Designer cannot be removed.

   To disable some messages, clear the check boxes in the Enable column. Disabled messages will not be triggered.
5. Select **OK** to accept the settings.

## Receiving Synchronization

The data components (tables, charts, crosstabs, KPIs and geographic maps) in a dashboard can be used as the message receivers to receive messages that are sent out from any objects in the dashboard. When a data component receives a message, it will perform the actions defined in the message, such as filtering, sorting itself using conditions defined in the message, re-running with parameter values in the message, changing its object properties, removing filter conditions applied on it, or going to a lower or upper level of its data. You can make multiple data components receive the same message and respond to the same action with the same conditions so as to achieve data synchronization between the data components.

To make a data component in a dashboard receive messages and respond to corresponding web actions, take the following steps:

1. Right-click anywhere on a data component and select **Receive Sync**  from the shortcut menu. Report Server displays the [Receive Sync](https://devnet.logianalytics.com/hc/en-us/articles/1500009747021-Receive-Sync) dialog box.

   ![Receive Sync dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936892951/rcvsync.gif)

   If the data component has been predefined to receive messages in Logi Report Designer, they will be listed in the dialog box marked with ![Lock button](https://devnet.logianalytics.com/hc/article_attachments/4404936891927/btn_dshbrd_lock.gif).
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) to add a message line.
3. The Sync From drop-down list displays all the trigger objects in the current dashboard. Select the trigger object the message sent out by which you want the data component to receive.
4. All the messages that have been defined on the selected trigger object are listed in the Message Name drop-down list. Select the message the data component is going to receive. If the selected message is a built-in message, the action bound with the message is then displayed in
   the Actions column.
5. You can double-click in the Action Description column to add a description for the action the message will respond.
6. Specify how the data component will respond when it receives the message.
   * If the to be received message is a built-in Filter message, the data component will filter itself according to the filter conditions defined in the message. You can further [edit the filter conditions](#BFilter) if you want.
   * If the to be received message is a built-in Sort message, the data component will sort itself according to the sort conditions defined in the message. You can further [edit the sort conditions](#BSort) if you want.
   * If the to be received message is a built-in Parameter message, the data component will re-run using the parameter values in the message. You can further [edit the parameter values](#BParameter) if you want.
   * If the to be received message is a built-in On-screen Filter message, the data component will filter itself according to the filter conditions defined in the message. You can further [edit the filter conditions](#BOnScreenFilter) if you want.
   * If the to be received message is a user define message, you can specify the web action the data component will respond to when it receives the message and define how the action will be performed. The following web actions are supported: [Filter](#UFilter), [On-screen Filter](#UOnScreenFilter), [Remove Filter](#URemoveFilter), [Sort](#USort), [Parameter](#UParameter), [Property](#UProperty), [Go Down](#UGoDown), [Go Up](#UGoUp) and [Go To](#UGoTo).
7. Repeat the above steps to add more messages to receive and define how to respond to the messages.

   To delete a message, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404942567703/btn_dshbrd_rmv1.gif) above the message information box. The messages predefined in Logi Report Designer cannot be removed.

   To disable some messages, clear the check boxes in the Enable column. Disabled messages will not be received by the data component.
8. Upon finish, select **OK** to accept the settings and close the dialog box.

**Note:** In the drop-down lists for editing the conditions to respond a message, you may find that some items have the icon ![Message Key icon](https://devnet.logianalytics.com/hc/article_attachments/4404936954263/btn_dshbrd_msgkey.gif) ahead of them and they are listed under the Message Key node. If you choose an item of this type, it means the item will not be used directly in a condition, instead it will be mapped to a key in the message and Logi Report will find the value that is specified to the key from the message first and then use that value to compose the condition.

**To edit the filter conditions for the built-in Filter message:**

1. In the Receive Sync dialog box, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column. Report Server displays the [Web Action - Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009720342-Web-Action-Filter) dialog box.

   ![Web Action - Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942568727/wbactn_fltr.gif)
2. Specify the filter condition by selecting the field on which the filter will be based from the Filter On drop-down list, the operator to compose the condition from the Operator drop-down list and the value of how to filter the field from the Value drop-down list.

   If you choose to type the value manually, when multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
3. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) to add more filter conditions to filter other field values and specify the relationship between the conditions in the More column.

   To delete a filter condition, select the condition and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404942567703/btn_dshbrd_rmv1.gif).
4. Select **OK** to finish defining the filter conditions.

**To edit the sort conditions for the built-in Sort message:**

1. In the Receive Sync dialog box, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column. Report Server displays the [Web Action - Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009747201-Web-Action-Sort) dialog box.

   ![Web Action - Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936888343/wbactn_sort.gif)
2. Specify the sort condition by selecting the field on which to sort the records from the Sort On drop-down list, and in which order to sort the records from the Sort Value drop-down list.
3. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) to add more sort conditions to sort other fields.

   To delete a sort condition, select the condition and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404942567703/btn_dshbrd_rmv1.gif).
4. Select **OK** to finish defining the sort conditions.

**To edit the parameter values for the built-in Parameter message:**

1. In the Receive Sync dialog box, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column. Report Server displays the [Web Action - Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009720442-Web-Action-Parameter) dialog box.

   ![Web Action - Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936889111/wbactn_param.gif)
2. Specify the parameter and the value of the parameter from the Parameter Name and Parameter Value drop-down lists. The operator can only be =.

   Parameter Name\* in the Parameter Name drop-down list means that all the parameters defined in the message will be used to re-run the data component, and its corresponding value can only be Parameter Value\* that represents all the parameter values.
3. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) to add more parameter lines to specify other parameter values. If you specify a parameter value more than once, the last setting takes effect.

   To delete a parameter line, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404942567703/btn_dshbrd_rmv1.gif).
4. Select **OK** to accept the settings. Then at runtime, when the data component receives the message, it will re-run itself, using the predefined parameter values.

**To edit the filter conditions for the built-in On-screen Filter message:**

1. In the Receive Sync dialog box, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column. Report Server displays the [Web Action - On-screen Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009720422-Web-Action-On-screen-Filter) dialog box.

   ![Web Action - On-screen Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942567959/wbactn_onscrnfltr.gif)
2. Specify the filter condition by selecting the field on which the filter will be based from the Filter On drop-down list and the value of how to filter the field from the Value drop-down list.

   If you choose to type the value manually, when multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
3. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) to add more filter conditions to filter other field values.

   To delete a filter condition, select the condition and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404942567703/btn_dshbrd_rmv1.gif).
4. Select **OK** to finish defining the filter conditions.

**To respond the Filter web action for a user defined message:**

The Filter web action enables you to filter the records of the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*Filter** from the drop-down list of the Actions column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action - Filter dialog box, [specify the filter condition](#BFilter) as required.
3. Select **OK** to accept the settings.

**To respond the On-screen Filter web action for a user defined message:**

The On-screen Filter web action enables you to filter the records of the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*On-screen Filter** from the drop-down list of the Actions column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action - On-screen Filter dialog box, [specify the filter condition](#BOnScreenFilter) as required.
3. Select **OK** to accept the settings.

**To respond the Remove Filter web action for a user defined message:**

The Remove Filter web action enables you to remove the filters from the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*Remove Filter** from the drop-down list of the Actions column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column. Report Server displays the [Web Action - Remove Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009747181-Web-Action-Remove-Filter) dialog box.

   ![Web Action - Remove Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936888855/wbactn_rmvfltr.gif)
2. Specify the filters you want to remove from the data component: to remove the filters that are created via the [Filter option on a field’s shortcut menu](https://devnet.logianalytics.com/hc/en-us/articles/1500009718922-Manipulating-Data-Components#Filter), the Filter web action and the Filter dialog box, select **Remove Filters**; to remove the on-screen filters created by the On-screen Filter web action, select **Remove \*On-screen Filters**.
3. By default, all the on-screen filters will be removed from the data component when Remove \*On-screen Filters is selected. If you only want to remove the filter conditions that are related to certain data fields, clear the **All Fields** option, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) to add a condition line, select in the line and select a field from the drop-down list or select **<Input...>** and type the field name manually. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) to add more fields. To remove an unwanted field, select it and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404942567703/btn_dshbrd_rmv1.gif).
4. Select **OK** to accept the settings.

**To respond the Sort web action for a user defined message:**

The Sort web action enables you to sort the records of the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*Sort** from the drop-down list of the Actions column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action - Sort dialog box, [specify the sort condition](#BSort) as required.
3. Select **OK** to accept the settings.

**To respond the Parameter web action for a user defined message:**

The Parameter web action enables you to run a data component, especially a data component with parameters using predefined parameter values, or re-run the data component with predefined parameter values when the message is received.

1. In the Receive Sync dialog box, select **\*Parameter** from the drop-down list of the Actions column, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action - Parameter dialog box, [specify the parameters](#BParameter)  as required.

   If the specified data component contains parameters, the parameters will be automatically listed in the parameters box. Specify the value for each parameter.
3. Select **OK** to accept the settings.

**To respond the Property web action for a user defined message:**

The Property web action enables you to change the properties of the data component when it receives the message.

1. In the Receive Sync dialog box, select **\*Property** from the drop-down list of the Actions column.
2. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column. Report Server displays the [Web Action - Change Property](https://devnet.logianalytics.com/hc/en-us/articles/1500009747161-Web-Action-Change-Property) dialog box.

   ![Web Action - Change Property dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936889879/wbactn_prpty.gif)
3. Specify the property you want to change and the value for it respectively from the Properties and Value drop-down lists. Only the properties of the data component itself can be changed.
4. You can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936888599/btn_dshbrd_add1.gif) to add more property lines to change values of other properties.

   To delete a property line, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404942567703/btn_dshbrd_rmv1.gif).
5. Select **OK** to accept the settings.

**To respond the Go Down web action for a user defined message:**

The Go Down web action enables you to drill data of the data component to the lower-level group according to a predefined hierarchy in the business view the data component uses when it receives the message. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

1. In the Receive Sync dialog box, select **\*Go Down** from the drop-down list of the Actions column.
2. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column. Report Server displays the [Web Action - Go Down](https://devnet.logianalytics.com/hc/en-us/articles/1500009720362-Web-Action-Go-Down)  dialog box.

   ![Web Action - Go Down dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942568471/wbactn_godwn.gif)
3. In the Go Down On column, select the group on which the go-down action will be performed. For a geographic map, it is Current Layer and cannot be changed.
4. In the Use Hierarchy column, select the hierarchy based on which the go-down action will be performed.
   You can also use a web control in the dashboard to retrieve a hierarchy name. For a geographic map, the Built-in hierarchy is used and cannot be changed.
5. In the By Value column, type a value of the specified group field to go down to the lower level with the filter condition *SpecifiedGroupField=TheValue*. You can also use a web control to retrieve a value.
6. Select **OK** to accept the settings.

**To respond the Go Up web action for a user defined message:**

The Go Up web action enables you to drill data of the data component to the upper-level group according to a predefined hierarchy in the business view the data component uses when it receives the message. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

1. In the Receive Sync dialog box, select **\*Go Up** from the drop-down list of the Actions column.
2. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column. Report Server displays the [Web Action - Go Up](https://devnet.logianalytics.com/hc/en-us/articles/1500009720402-Web-Action-Go-Up)  dialog box.

   ![Web Action - Go Up dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936889367/wbactn_goup.gif)
3. In the Go Up On column, select the group on which the go-up action will be performed. For a geographic map, it is Current Layer and cannot be changed.
4. In the Use Hierarchy column, select the hierarchy that the go-up action will be performed according to. You can also use a web control in the dashboard to retrieve a hierarchy name. For a geographic map, the Built-in hierarchy is used and cannot be changed.
5. Select **OK** to accept the settings.

**To respond the Go To web action for a user defined message:**

The Go To web action enables you to change a data field of the data component when it receives the message. It is available to tables, charts and crosstabs.

1. In the Receive Sync dialog box, select **\*Go To** from the drop-down list of the Actions column.
2. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936888087/btn_dshbrd_edt1.gif) in the Actions column. Report Server displays the [Web Action - Go To](https://devnet.logianalytics.com/hc/en-us/articles/1500009720382-Web-Action-Go-To) dialog box.

   ![Web Action - Go To dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936889623/wbactn_goto.gif)
3. In the Go To On column, select the field on which the go-to action will be performed.
4. In the To Column column, select another field to change the Go To On field to. You can also use a web control in the dashboard to retrieve a field name.
5. To apply the go-to action by filtering the Go To On field at the same time, select the **By Value** check box and then type the value by which to filter the field or select a web control to retrieve the value at runtime. Skip this step if you select to perform the action on a crosstab aggregate field.
6. Select **OK** to accept the settings.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718922-Manipulating-Data-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745061-Filtering-the-Data-Components-in-a-Dashboard)
