---
title: "Refresh Object Properties"
id: 1500011552882
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011552882-Refresh-Object-Properties
updated_at: 2021-07-24T16:05:32Z
---

# Refresh Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009612242-Dataset-Properties) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635341-DBField-Properties)

# Refresh Object Properties

This topic lists the properties of a Refresh Object in a library component.

The Refresh Object is used to customize the auto refresh action for each business view used by the data components in a library component.

| Property Name | Description |
| --- | --- |
| General | |
| Business View Name | Displays the name of the business view for which the refresh object is created. This property is read only. Data type: String |
| Data Source Name | Displays the name of the data source in which the business view is created. This property is read only. Data type: String |
| Name | Displays the name of the refresh object, which by default is the business view name. This property is read only. Data type: String |
| Query Name | Displays the name of the query on which the business view is created. Data type: String |
| [Refresh](#AutoRefresh) | |
| Enable Auto Refresh | Specifies whether to make the data components that are created on the business view automatically refresh themselves at runtime based on a defined interval. Data type: Boolean |
| Incremental Fetch | Specifies whether to fetch incremental data only when an auto refresh takes place. Enabled when Enable Auto Refresh is set to true. If set to true, you can select  in the value cell to open the [Incremental Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009608802-Incremental-Condition-Dialog) dialog to specify conditions to filter the incremental data. This property does not work on crosstabs and real time charts. Data type: Boolean |
| Interval | Specifies the time interval between two auto refreshes. It ranges from 0 to 86400 seconds. Enabled when Enable Auto Refresh is set to true. Type a numeric value to change the interval. Data type: Integer |
| Unique Key | Specifies the unique key used to delete duplicated data from the incremental data filtered by incremental condition. Select  in the value cell to open the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009610762-Unique-Key-dialog-Dialog) dialog to specify the key. It is meaningful to specify the property when Incremental Fetch is set to true. Data type: Array |
| Value Number | Specifies the number of records that can be displayed in the data components. The earliest records will be removed when records exceed the specified number. Type a numeric value to change the number. It is meaningful to specify the property when Incremental Fetch is set to true. Data type: Integer |

## Customizing the Auto Refresh Action for a Library Component

If you want the data components that use the same business view in a library component automatically refresh themselves at runtime based on a defined interval, you can set the Enable Auto Refresh property to true and specify the interval between two auto refreshes using the Interval property.

In addition, Logi Report supports fetching incremental data only when an auto refresh takes place. To achieve this:

1. Set the Incremental Fetch property to **true**, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the value cell of the property. The [Incremental Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009608802-Incremental-Condition-Dialog) dialog appears.

   ![Incremental Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904202007/incrmntlcndtn.gif)
2. Specify the condition to filter the incremental data as required.
   1. Select the **Add Condition** button to add a condition line.
   2. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) next to the field text box, then in the View Element Resources dialog, locate the element you want to filter and double-click it, or select the element and select **OK**. You can also type in the name of the view element manually as *@ElementName* in the text box.
   3. From the operator drop-down list, select the operator with which to compose the filter expression.
   4. In the value drop-down list, specify how to filter the business view element.

      To specify the value, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) next to the drop-down list, then in the Values dialog switch to the **Value** tab. All values of the selected element are listed. Double-click the required value and close the dialog. However if you choose to manually type in the element name in step b, you need to select the element in the Fields tab of the Values dialog once again to get its value list. You can also select the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName) or a parameter in the Fields tab as the value to filter the element dynamically (for the usage of parameters in filter conditions, see the example in [Dynamically filtering queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#FilterQuery)), or select a formula to use its returned value in the filter. If you are familiar with the values of the selected view element, you can clear the text <Select a value> and type the value manually in the text box (when the selected operator requires multiple values, you will have to specify the values manually). When you type in the value, if multiple values are required, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

      You can also select any of the following from the value drop-down list as the value:

      * **MaxExistValue**  
         If selected, the maximum data value in the specified business view element from the last refresh time will be used as the value to filter the business view element.
      * **MinExistValue**  
        If selected, the minimum data value in the specified business view element from the last refresh time will be used as the value to filter the business view element.
      * **LastRefreshTime**  
        If selected, the previous refresh time will be used as the value to filter the business view element.
   5. Select **Add Condition** to add more condition lines, specify the condition in each line, and define the logic (And or Or) between the condition lines.

      To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

      To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

      To delete a condition line, select it and select the **Delete** button.
3. Select **OK** to save the incremental condition.
4. To add a unique key to delete duplicated data from the incremental data filtered by incremental condition, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the value cell of the Unique Key property. The [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009610762-Unique-Key-dialog-Dialog) dialog appears.

   ![Unique Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911644567/unqkey.gif)
5. From the Resources box, select the business view element to use as the unique key and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) to add it to the right box. You can add more than one element to the unique key.

   Once a unique key is defined, each time when the data components that use the business view automatically updates themselves, the data that has the same unique key value as the previously loaded data records will be filtered and only data with different unique key value will be added to the data components. For instance, if you add the fields Country and Product ID as the unique key for a business view, when a record with the product ID 1 in USA has already been loaded into the data components, no more records of this product ID in USA will be added to the data components because they have the same unique key value. The most common usage is with a time field so when a time is part of the unique key the data will be updated each time new records are added to the database with more recent times.
6. Select **OK** to save the unique key.
7. You can type the number of records that can be displayed in the data components in the value cell of the Value Number property. The earliest records will be removed when records exceed the specified number.

When the library component is used in a dashboard at runtime, the data components in the library component that use the specified business view will be automatically refreshed based on the predefined conditions. End users can also customize the auto refresh action in JDashboard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009612242-Dataset-Properties) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635341-DBField-Properties)
