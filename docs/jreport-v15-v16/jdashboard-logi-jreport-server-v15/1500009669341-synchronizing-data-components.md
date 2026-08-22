---
title: "Synchronizing Data Components"
id: 1500009669341
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669341-Synchronizing-Data-Components
updated_at: 2021-07-24T20:55:17Z
---

# Synchronizing Data Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669301-Manipulating-Data-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data)

# Synchronizing Data Components

It is important for different parts of a visualization to be fully consistent. When you filter or sort on any data, you will want this to be reflected on all or a certain set of data components (crosstabs, tables, charts, KPI components, and geographic maps) in the same dashboard. Logi JReport allows you to achieve the synchronization by means of sending and receiving messages in a dashboard.

The messages that can be sent and received in a dashboard for synchronization includes the built-in messages Filter, Sort and Parameter, and user customized messages. The built-in messages are predefined with corresponding web actions.

Sending and receiving messages can also be predefined when creating library components in Logi JReport Designer. For details refer to "Delivering Messages Between Library Components" in the *Logi JReport Designer User's Guide*.

Below is a list of the sections in this topic:

* [Sending Synchronization](#Send)
* [Receiving Synchronization](#Receive)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Sending Synchronization

Synchronization messages can be sent out when selecting specific objects in a dashboard, which include independent labels (labels outside of data components), labels in tables/crosstabs/KPI components, data fields, special fields, data markers, legend and category axis labels of charts, markers and areas in geographic maps, parameter controls, and the Submit button of parameter form controls. These objects are referred to as the synchronization trigger objects.

You can either make synchronization messages sent out automatically by using the built-in messages or define customized messages on your own. In a customized message you can specify to send out multiple messages from one trigger object and edit the message information as you want. The following built-in messages are provided:

* **Filter**  
   The Filter built-in message is sent out for asking the message receivers to filter themselves based on the filter condition defined in the message.
* **Sort**  
   The Sort built-in message is sent out for asking the message receivers to sort themselves based on the sort condition defined in the message.
* **Parameter**  
   The Parameter built-in message is sent out for asking the message receivers to re-run using the available parameter values in the message.

**To send out a built-in synchronization message:**

Select a trigger object, right-click it and select **Send Sync** > **Filter**/**Sort**/**Parameter** on the shortcut menu (Filter and Sort are not available for the Submit button of parameter form controls). Then when the trigger object is selected, a corresponding built-in message will be sent out. If the trigger object is an independent label, you need to manually [specify the message receivers](#Receive); if it is one of the other objects, the message will be automatically received by data components in the current dashboard as follows:

* For the Filter message, Logi JReport will determine the data components that can automatically receive the message and make them filtered based on the default filter condition *Current Field = Current Value*. For example, the data components that contain the business view object the display name or instance name of which is the same as that of the trigger object are able to automatically receive the message and filter the business view object based on the selected value of the trigger object.
* For the Sort message, Logi JReport will determine the data components that can automatically receive the message and make them sorted based on the default sort condition *Current Field Ascending*. For example, the data components that contain the business view object the display name or instance name of which is the same as that of the trigger object are able to automatically receive the message and sort values of the business view object in ascending order.
* For a Parameter message, it will include all the available parameters used by the library component in which the trigger object is placed. The data components that contain any of the parameters will automatically receive the message and re-run with the parameter values in the message. However to make the Parameter message meaningful, you are recommended to insert a parameter form control into the library component of the message sender to include all the parameters used by the library component, thus when the data components receive the message, they can use the parameter values provided in the parameter form control to re-run.

If you want to view or edit the message a data component automatically receives, you can [make use of its Receive Sync](#Receive) dialog. While for the Parameter message, if some data components are contained in one library component, the dialog is only available on the first data component in the library component.

**To send out a customized message**:

1. Right-select a trigger object and select **Send Sync** > **Customize** from the shortcut menu. The [Send Sync](https://devnet.logianalytics.com/hc/en-us/articles/1500009646282-Send-Sync) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920581655/sndsync.gif)
2. In the message box on the left, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579351/btn_dshbrd_add1.gif) to add a message line, select the type of the message from the Message Type drop-down list, which can be one of the built-in messages Filter, Sort and Parameter or User-Defined. A message name is then automatically displayed in the Message Name column. Double-select in the column to edit the message name if needed.

   If the object has been predefined to send messages in Logi JReport Designer, they will be listed in the message box marked with ![](https://devnet.logianalytics.com/hc/article_attachments/4404920581911/btn_dshbrd_lock.gif) and you cannot modify them.
3. In the message information box on the left, define the message as you want.
   * For the Filter message, specify the field to be filtered, the filter operator and the value using which to filter the field. To make the condition dynamic, select the values under the Dynamic Key node.
   * For the Sort message, specify the field to be sorted and the sort order. To make the condition dynamic, select the values under the Dynamic Key node.
   * For the Parameter message, specify the parameter name and value. To make the condition dynamic, select the values under the Dynamic Key node.
   * For a user-defined message,
     1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579351/btn_dshbrd_add1.gif) above the message information box to add a message key-value line.
     2. In the Key Name column, specify a key from the drop-down list or select the **<Input...>** item from the list and then input a key into the text box. To make the condition dynamic, select the values under the Dynamic Key node.
     3. In the Value column, specify the value of the key from the drop-down list or select **<Input...>** from the list and then input a value into the text box. To make the condition dynamic, select the values under the Dynamic Key node.
     4. If necessary, add more key-value lines and specify the key and value in each line.

        To delete a message key-value line, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926747159/btn_dshbrd_rmv1.gif).

     **Tip:** You can also create a blank user-defined message without specifying the key and value.
4. Repeat the above two steps to add more messages on the object.

   To delete a message, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926747159/btn_dshbrd_rmv1.gif) above the message box. Messages predefined in Logi JReport Designer cannot be removed.

   To disable some messages, uncheck the checkboxes in the Enable column. Disabled messages will not be triggered.
5. When done, select **OK** to accept the settings.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Receiving Synchronization

The data components (tables, charts, crosstabs, KPI components, and geographic maps) in a dashboard can be used as the message receivers to receive messages that are sent out from any objects in the dashboard. When a data component receives a message, it will perform the actions defined in the message, such as filtering, sorting itself using conditions defined in the message, re-running with parameter values in the message, or changing its object properties. You can make multiple data components receive the same message and respond the same action with the same conditions so as to achieve the data synchronization between the data components.

To make a data component in a dashboard receive messages and respond corresponding web actions, take the following steps:

1. Right-select anywhere on a data component and select **Receive Sync**  from the shortcut menu. The [Receive Sync](https://devnet.logianalytics.com/hc/en-us/articles/1500009670421-Receive-Sync) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920584855/rcvsync.gif)

   If the data component has been predefined to receive messages in Logi JReport Designer, they will be listed in the dialog marked with ![](https://devnet.logianalytics.com/hc/article_attachments/4404920581911/btn_dshbrd_lock.gif).
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579351/btn_dshbrd_add1.gif) to add a message line.
3. The Sync From drop-down list displays all the trigger objects in the current dashboard. Select the trigger object the message sent out by which you want the data component to receive.
4. All the messages that have been defined on the selected trigger object are listed in the Message Name drop-down list. Select the message the data component is going to receive. If the selected message is a built-in message, the action bound with the message is then displayed in
   the Actions column.
5. Double-select in the Action Description column to add a description for the action the message will respond if necessary.
6. Specify how the data component will respond when it receives the message.
   * If the to be received message is a built-in Filter message, the data component will filter itself based on the filter conditions defined in the message. You can further [edit the filter conditions](#BFilter) if you want.
   * If the to be received message is a built-in Sort message, the data component will sort itself based on the sort conditions defined in the message. You can further [edit the sort conditions](#BSort) if you want.
   * If the to be received message is a built-in Parameter message, the data component will re-run using the parameter values in the message. You can further [edit the parameter values](#BParameter) if you want.
   * If the to be received message is a user define message, you can specify the web action such as [Filter](#UFilter), [Sort](#USort), [Parameter](#UParameter) and [Property](#UProperty) the data component will respond when it receives the message and define how the action will be performed.
7. Repeat the above steps to add more messages to receive and define how to respond the messages.

   To delete a message, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926747159/btn_dshbrd_rmv1.gif) above the message information box. The messages predefined in Logi JReport Designer cannot be removed.

   To disable some messages, uncheck the checkboxes in the Enable column. Disabled messages will not be received by the data component.
8. Upon finish, select **OK** to accept the settings and close the dialog.

**To edit the filter conditions for the built-in Filter message:**

1. In the Receive Message dialog, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920578711/btn_dshbrd_edt1.gif) in the Actions column. The [Web Action](https://devnet.logianalytics.com/hc/en-us/articles/1500009670581-Web-Action#Filter) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579095/wbactn_fltr.gif)
2. Specify the filter condition by selecting the field on which the filter will be based from the Filter On drop-down list, the operator to compose the condition from the Operator drop-down list and the value of how to filter the field from the Value drop-down list.
3. If necessary, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579351/btn_dshbrd_add1.gif) to add more filter conditions to filter other field values and specify the relationship between the conditions in the More column.

   To delete a filter condition, select the condition and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926747159/btn_dshbrd_rmv1.gif).
4. Select **OK** to finish defining the filter conditions.

**To edit the sort conditions for the built-in Sort message:**

1. In the Receive Message dialog, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920578711/btn_dshbrd_edt1.gif) in the Actions column. The [Web Action](https://devnet.logianalytics.com/hc/en-us/articles/1500009670581-Web-Action#Sort) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579607/wbactn_sort.gif)
2. Specify the sort condition by selecting the field on which to sort the records from the Sort On drop-down list, and in which order to sort the records from the Sort Value drop-down list.
3. If necessary, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579351/btn_dshbrd_add1.gif) to add more sort conditions to sort other fields.

   To delete a sort condition, select the condition and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926747159/btn_dshbrd_rmv1.gif).
4. Select **OK** to finish defining the sort conditions.

**To edit the parameter values for the built-in Parameter message:**

1. In the Receive Message dialog, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920578711/btn_dshbrd_edt1.gif) in the Actions column. The [Web Action](https://devnet.logianalytics.com/hc/en-us/articles/1500009670581-Web-Action#Parameter) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579863/wbactn_param.gif)
2. Specify the parameter and the value of the parameter from the Parameter Name and Value drop-down lists. The operator can only be =.

   Parameter Name\* in the Parameter Name drop-down list means that all the parameters defined in the message will be used to re-run the data component, and its corresponding value can only be Parameter Value\* that represents all the parameter values..

   In the Parameter Name and Value drop-down list, you may also find some items have the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920647575/btn_dshbrd_msgvalue.gif) ahead of them and they are listed under the Message Key node. If you choose an item of this type, it means the item will not be used directly in the parameter condition, instead, it will be mapped to a key in the message and Logi JReport will search for the value that is specified to the key from the message first and then use that value to compose the parameter condition.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579351/btn_dshbrd_add1.gif) to add more parameter lines to specify other parameter values. If you specify a parameter value more than once, the last setting takes effect.

   To delete a parameter line, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926747159/btn_dshbrd_rmv1.gif).
4. Select **OK** to accept the settings. Then at runtime, when the data component receives the message, it will re-run itself, using the predefined parameter values.

**To respond the Filter web action for a user-defined message:**

The Filter web action enables you to filter the records of the data component when it receives the message.

1. In the Receive Message dialog, Select **\*Filter** from the drop-down list of the Actions column, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920578711/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action dialog, [specify the filter condition](#BFilter) as required.
3. Select **OK** to accept the settings.

**To respond the Sort web action for a user-defined message:**

The Sort web action enables you to sort the records of the data component when it receives the message.

1. In the Receive Message dialog, select **\*Sort** from the drop-down list of the Actions column, then select select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920578711/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action dialog, [specify the sort condition](#BSort) as required.
3. Select **OK** to accept the settings.

**To respond the Parameter web action for a user-defined message:**

The Parameter web action enables you to run a data component, especially a data component with parameters using predefined parameter values, or re-run the data component with predefined parameter values when the message is received.

1. In the Receive Message dialog, select **\*Parameter** from the drop-down list of the Actions column, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920578711/btn_dshbrd_edt1.gif) in the Actions column.
2. In the Web Action dialog, [specify the parameters](#BParameter)  as required.

   If the specified data component contains parameters, the parameters will be automatically listed in the parameters box. Specify the value for each parameter.
3. Select **OK** to accept the settings.

**To respond the Property web action for a user-defined message:**

The Property web action enables you to change properties of the data component itself when it receives the message.

1. In the Receive Message dialog, select **\*Property** from the drop-down list of the Actions column.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920578711/btn_dshbrd_edt1.gif) in the Actions column. The [Web Action](https://devnet.logianalytics.com/hc/en-us/articles/1500009670581-Web-Action#Property) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926747671/wbactn_prpty.gif)
3. Specify the property you want to change and the value for it respectively from the Properties and Value drop-down lists. Only the properties of the data component itself can be changed.

   In the two drop-down lists, you may find some items have the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920647575/btn_dshbrd_msgvalue.gif) ahead of them and they are listed under the Message Key node. If you choose an item of this type, it means the item will not be used directly in the property changing condition, instead, it will be mapped to a key in the message and Logi JReport will search for the value that is specified to the key from the message first and then use that value to compose the property changing condition.
4. If necessary, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920579351/btn_dshbrd_add1.gif) to add more property lines to change values of other properties.

   To delete a property line, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926747159/btn_dshbrd_rmv1.gif).
5. Select **OK** to accept the settings.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669301-Manipulating-Data-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data)
