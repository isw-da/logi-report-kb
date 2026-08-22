---
title: "Applying Web Actions to a Label"
id: 1500009584021
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label
updated_at: 2021-07-24T05:56:01Z
---

# Applying Web Actions to a Label

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563422-Changing-the-Display-Type-of-a-Label)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583921-DBFields)

# Applying Web Actions to a Label

A label in a page report that is created using query resources or in a library component can be bound with web actions. This allows you to customize a label to make it respond to interactive events, and execute corresponding actions such as sorting and filtering. For example, you can insert a label in Logi JReport Designer and associate an action with the label's onclick event. Then at runtime when end users run the report and select the label, the defined operation will be executed.

The following table lists the events that can be used to trigger web actions:

| Events | Description |
| --- | --- |
| Blur | Fires when the object loses the input focus. |
| Data Change | Fires when the contents of the object or selection have changed. |
| Select | Fires when the user selects the left mouse button on the object. |
| onContextMenu | Fires when the user selects the right mouse button on the object, opening the shortcut menu. |
| Double\_Select | Fires when the user double-clicks the object. |
| Focus | Fires when the object receives focus. |
| Key Down | Fires when the user presses a key. |
| Key Press | Fires when the user presses an alphanumeric key. |
| Key Up | Fires when the user releases a key. |
| Mouse Down | Fires when the user selects the object with either mouse button. |
| Mouse Move | Fires when the user moves the mouse over the object. |
| Mouse Out | Fires when the user moves the mouse pointer outside the boundaries of the object. |
| Mouse Over | Fires when the user moves the mouse pointer into the object. |
| Mouse Up | Fires when the user releases a mouse button while the mouse is over the object. |
| Resize | Fires when the size of the object is about to change. |
| Scroll | Fires when the user repositions the scroll box in the scrollbar on the object. |
| Select | Fires when the current selection changes. |

**To bind web actions to a label:**

1. Right-click the label and select **Display Type** from the shortcut menu.
2. In the Web Behaviors box of the Display Type dialog, choose an event from the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box.
3. In the Web Action List dialog, select the required action and then select **OK**.

   ![Web Action List dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889313687/wbactnlst.gif)

   * If the selected web action is [Filter](#Filter), [Sort](#Sort), [Parameter](#Parameter), [Property](#Property), [SendMessage](#Message) or [Customized Control](#CC), the corresponding web action builder dialog appears. Specify the settings according to your requirements.
   * If [Customized Control from Lib](#CC) is selected, the Customized Control Manager dialog is displayed, which shows all the customized control files in the customized control library. Select the one you want and select **OK**.
   * If the selected action needs no parameter, the Web Action List dialog is closed.
   * If the selected web action needs parameters, the [Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009588221-Parameters-Dialog) dialog appears for you to input the parameter values. For parameters that refer to instance name, you can input the mapping name of the instance, or the display name plus the prefix "&" as the parameter value.
4. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) in the Display Type dialog and repeat the above steps to add more web actions. If a web action is not required, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.
5. Adjust the order of the added web actions by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif). Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
6. Select **OK** to apply the settings and close the Display Type dialog.

Then, at runtime, when any of the specified events occurs on the label, the web action defined on the event will be triggered.

**Notes:**

* Web actions are not supported on web reports and page reports that are created using business views.
* The Property and Send Message web actions are available to library components only.
* You can define your own web actions by adding API functions into both the file API.js located at `<designer_install_root>\lib\html\javascript\dhtml` and the same-name file located at `<server_install_root>\public_html\dhtmljsp\js`.

Below is a list of the sections covered in this topic:

> * [Filter](#Filter)
> * [Sort](#Sort)
> * [Parameter](#Parameter)
> * [Customized Control](#CC)
> * [Property](#Property)
> * [SendMessage](#Message)

## Filter

The Filter web action enables you to filter the records in a data component.

**To apply the Filter web action:**

1. In the Web Action List dialog, select  **\*Filter** and select **OK**. The [Filter - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009586901-Filter-Web-Action-Builder-Dialog) dialog appears.

   ![Filter - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889361943/wbactnbldr_fltr.gif)
2. From the Get Input From drop-down list, specify where to get the input, which may be a form, or other in report.
3. From the Apply Action To drop-down list, select a data component in the current report, whose records will be filtered.
4. In the Filter On column, specify the field on which to filter the records. The field may be a column in the component, or be specified by the value of a web control.
5. Specify the operator and value. The value may be input by yourself, or be the value of a web control.
6. If necessary, specify **And** or **Or** in the More column so as to add a new filter condition or you can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a new filter condition.

   To delete a filter condition, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif). To adjust the order of the filter conditions, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif).
7. Select **OK** to accept the filter conditions.

At runtime, when the specified event occurs on the label, the selected data component will be filtered based on the predefined conditions.

## Sort

The Sort web action enables you to sort the records in a data component.

**To apply the Sort web action:**

1. In the Web Action List dialog, select **\*Sort** and select **OK**. The [Sort - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009588801-Sort-Web-Action-Builder-Dialog) dialog appears.

   ![Sort - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893986583/wbactnbldr_srt.gif)
2. From the Get Input From drop-down list, specify where to get the input, which may be a form, or other in report.
3. From the Apply Action To drop-down list, select a data component in the current report, whose records will be sorted.
4. In the Sort On column, specify the field on which to sort the records. The field may be a column in the component, or be specified by the value of a web control.
5. Specify the sort value. The value may be Ascending or Descending, or be the value of a web control.
6. If necessary, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a new sort condition.

   To delete a sort condition, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif). To adjust the order of the sort conditions, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif).
7. Select **OK** to accept the sort conditions.

At runtime, when the specified event occurs on the label, the selected data component will be sorted based on the predefined conditions.

## Parameter

The Parameter web action enables you to run a report, especially a report with parameters.

**To apply the Parameter web action:**

1. In the Web Action List dialog, select **\*Parameter** and select **OK**. The [Parameter - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009588241-Parameter-Web-Action-Builder-Dialog) dialog appears.

   ![Parameter - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893860119/wbactnbldr_prm.gif)
2. Specify the handler which will receive the parameters of the web action. The handler may be the default one in the current server, or in another server specified by Customized Path.
3. From the Get Input From drop-down list, specify where to get the input, which may be a form, or other in report.
4. Specifies whether to apply the action to run a report or refresh the current report. If you choose to run a report, select the **Browse** button to specify the report or use a [web control](https://devnet.logianalytics.com/hc/en-us/articles/1500009584641-Using-Basic-Web-Controls) to retrieve the report name at runtime, then select the window or frame in which the report will be opened from the Target Frame drop-down list.
5. The parameters used by the specified report are automatically listed in the parameters box. Specify the value for each parameter.
6. Select **OK** to accept the parameter values.

At runtime, when the specified event occurs on the label, the selected report will run using the specified parameter values.

## Customized Control

With the Customized Control web action, you can customize dialogs to perform web actions such as sorting and filtering in tables in page reports that are creating using query resources. For the usage of this web action, see [Using Customized Controls in a Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009584281-Using-Customized-Controls-in-a-Table).

## Property

The Property web action enables you to make the properties of an object change at runtime, however, it is available to the following objects in library components only: fields and labels in tables/crosstabs, some chart elements such as legend, chart axis and so on, markers and areas in geographic maps, as well as labels, parameter controls and the Submit buttons of parameter form controls which are not in the library components' configuration panels.

**To apply the Property web action:**

1. In the Web Action List dialog, select  **\*Property**  and select **OK**. The [Change Property - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009585801-Change-Property-Web-Action-Builder-Dialog) dialog appears.

   ![Change Property - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893953047/cptywbactnbld.gif)
2. From the Apply Action To drop-down list, select the object the properties of which you want to change.
3. In the Properties column, specify the property you want to change. All the properties of the object you select from the Apply Action To drop-down list are listed here.
4. In the Value column, input the value of the property.
5. If necessary, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a new line to change a property.

   To delete a property line, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif). To adjust the order of the properties, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif).
6. Select **OK** to accept the property values.

At runtime, when the specified event occurs on the label, the property values will be applied to the selected object.

## SendMessage

The Send Message web action enables you to send out a message when a specific event occurs on an object in a library component. The message will apply to any library components that are receiving the message when displayed in the same dashboard. For more information about this web action, refer to [Sending Out Messages](https://devnet.logianalytics.com/hc/en-us/articles/1500009570862-Sending-Messages#Action).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563422-Changing-the-Display-Type-of-a-Label)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583921-DBFields)
