---
title: "Using Basic Web Controls in a Report"
id: 1500010057562
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report
updated_at: 2021-07-23T19:14:52Z
---

# Using Basic Web Controls in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095061-Using-Basic-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057542-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component)

# Using Basic Web Controls in a Report

This topic introduces how you can insert and define values of basic web controls in a report. It also presents an example to demonstrate how you can add web controls and apply web actions to the web controls to achieve specific goals.

You can use basic web controls in page reports using query resources, web reports, and library components.

This topic contains the following sections:

* [Inserting Basic Web Controls](#Insert)
  + [nserting a Text Field/Password](#TextField)
  + [Inserting a Text Area](#TextArea)
  + [Inserting a Checkbox/Radio Button](#Checkbox)
  + [Inserting an Image Button](#ImageButton)
  + [Inserting a Button](#Button)
  + [Inserting a List/Drop-down List](#List)
* [Example: Using Web Controls in a Page Report](#Example)

## Inserting Basic Web Controls

You can insert basic web controls in report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship) in a report.

The following are some tips for you when using the basic web controls:

* When defining a basic web control in a page report that uses query resources, you can find the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) next to some options such as Name and Tool Tip in the Display Type dialog box. When the button is available, you can select it and [select a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or DBField from the given drop-down list to control an option. If you select a DBField as the value of an option, Designer applies the first record of the field in the database.
* You can also change the [display type](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports) of a basic web control after it is created. You can convert basic web controls other than list and drop-down list to each other and display them as a general type, and you may notice that these web controls have a common Class Type property value "Label" in the Report Inspector, which signifies that these web controls are labels in nature.

### Inserting a Text Field/Password

1. Do one of the following to insert the text field/password:
   * From the **Components** panel, drag the **Text Field** icon ![Text Field icon](https://devnet.logianalytics.com/hc/article_attachments/4404848655511/icon_txtfld.gif) or **Password** icon ![Password icon](https://devnet.logianalytics.com/hc/article_attachments/4404857030295/icon_pswd.gif) in the Web Controls category to the destination.
   * Select **Insert** > **Web Controls** > **Text Field**/**Password** to insert it to the destination.
2. Right-click the text field/password and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Text Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box#TextField) type.

   ![Display Type dialog box - Text Field](https://devnet.logianalytics.com/hc/article_attachments/4404848591511/dsplytp_txtfld.gif)
3. In the **Web Options** panel, specify the options of the text field/password.
   1. In the **Name** text box, specify the name of the text field/password.
   2. From the **Value** drop-down list, select **<Input...>** and type the value of the text field/password.
   3. In the **Tool Tip** text box, type the tool tip you want to show for the text field/password. The tool tip displays when the report users hover the mouse over the text field/password at runtime or in HTML output.
   4. Set the number of characters in the **Display Width** text box, and the maximum number of characters the user can specify in the **Max Length** text box.
   5. Select **Read Only** if you would like to set this text field/password to be read-only.
   6. Select **Disabled** if you want to make the text field/password disabled.
4. In the **Web Behaviors** panel, bind web actions to the text field/password to trigger specific operations at runtime.

   Adding web actions to a web control enables you to customize the web control to make it respond to interactive events, and execute corresponding actions such as sorting and filtering. For example, you can associate an action with a web control's select event. Then, when the report users run the report at runtime and select the web control, Logi Report Engine executes the defined operation.

   1. Choose an event from the **Events** column, then select in the **Actions** column and select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the text box.

      Logi Report supports the following events for triggering web actions:

      | Event | Description |
      | --- | --- |
      | Blur | Fires when the object loses the input focus. |
      | Data Change | Fires when the contents of the object or selection changes. |
      | Select | Fires when the report users select the left mouse button on the object. |
      | onContextMenu | Fires when the report user select the right mouse button on the object, opening the shortcut menu. |
      | Double\_select | Fires when the report users double-click the object. |
      | Focus | Fires when the object receives focus. |
      | Key Down | Fires when the report users press a key. |
      | Key Press | Fires when the report users press an alphanumeric key. |
      | Key Up | Fires when the report user release a key. |
      | Mouse Down | Fires when the report user select the object with either mouse button. |
      | Mouse Move | Fires when the report user move the mouse over the object. |
      | Mouse Out | Fires when the report user move the mouse pointer outside the boundaries of the object. |
      | Mouse Over | Fires when the report users move the mouse pointer into the object. |
      | Mouse Up | Fires when the report user release a mouse button while the mouse is over the object. |
      | Resize | Fires when the size of the object is about to change. |
      | Scroll | Fires when the report user reposition the scroll box in the scrollbar on the object. |
      | Select | Fires when the current selection changes. |
   2. In the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box), select the required action and select **OK**. The web actions available in the dialog box vary according to the report type.

      ![Web Action List dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848483863/wbactnlst.gif)

      * If the selected web action is [Parameter](#Parameter), [Filter](#Filter), [Sort](#Sort), [Property](#Property), [Go Down](#GoDown), [Go Up](#GoUp), [Go To](#GoTo), [Send Message](https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components#Action), or [Customized Control](https://devnet.logianalytics.com/hc/en-us/articles/1500010057402-Using-Customized-Controls-in-Tables), Designer displays the corresponding web action builder dialog box. Specify the settings according to your requirements.
      * If you select [Customized Control from Lib](https://devnet.logianalytics.com/hc/en-us/articles/1500010057402-Using-Customized-Controls-in-Tables), Designer displays the [Manage Customized Controls dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097881-Manage-Customized-Controls-Dialog-Box), which shows all the customized control files in the customized control library. Select the one you want and select **OK**.
      * If the selected action needs no parameter, Designer closes the Web Action List dialog box. Such web actions are only available to page reports that use query resources.
      * If the selected web action needs parameters, Designer displays the Parameters dialog box, which lists the parameters the web action requires. The following shows a sample dialog box:

        ![Parameters dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848656279/cmpnt_wbcntrl_basic_rpt_prm.gif)

        Specify the parameter values in the **Value** column. For parameters that refer to instance name, you can type in the mapping name of the instance, or the display name plus the prefix "&" as the parameter value. For more information about the parameter values, see [Appendix 3: Parameters of User-Defined Web Actions](https://devnet.logianalytics.com/hc/en-us/articles/1500010094001-Appendix-3-Parameters-of-User-Defined-Web-Actions).

      ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You can define your own web actions by adding API functions into the file **API.js** located at `<designer_install_root>\lib\html\javascript\dhtml` and the same name file located at `<server_install_root>\public_html\dhtmljsp\js`.
   3. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) in the Display Type dialog box and repeat the above steps to add more web actions. If a web action is not required, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif) to delete it.
   4. Adjust the order of the added web actions by selecting a web action and selecting the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button. Then, when an event which has been bound with more than one action happens at runtime, Logi Report Engine triggers the upper action first.
5. Select **OK** to insert the text field.

---

The following details how to define a specific web action:

**Parameter**

The Parameter web action enables you to run a specified report, especially one with parameters using the predefined parameter values when the designated event occurs on the trigger object at runtime.

1. In the Web Action List dialog box, select **\*Parameter** and select **OK**. Designer displays the [Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098241-Parameter-Web-Action-Builder-Dialog-Box).

   ![Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856901399/prmwbactnbld.gif)
2. Specify the handler which receives the parameters of the web action. The handler may be the default one in the current server, or in another server specified by **Customized Path**.
3. From the **Get Input From** drop-down list, specify where to get the input, which may be a [form](https://devnet.logianalytics.com/hc/en-us/articles/1500010057522-Using-Forms-in-a-Page-Report) (available to page report only), a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls#Form) in the report, or **Other in report**.
4. Specify whether to apply the action to run a report or refresh the current report. If you choose to run a report, select the **Browse** button to specify the report or use a web control in the current page report tab or web report to retrieve the report name at runtime, then select the window or frame in which to open the report from the **Target Frame** drop-down list.
5. In the parameter box, specify the parameters and the values with which to run or refresh the report.

* When you select **Report** and specify a report, if the report contains parameters, Designer loads the parameters automatically into the parameter box. Edit the value for each parameter.
* When you select **Web Control** or **Refresh Current Report**, Designer lists all the parameters used by the current report in the parameter box if it contains parameters. Edit the value for each parameter.

6. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more parameter conditions and specify the parameter names and values according to your requirements.

   When specifying the name and value of a parameter, you can also use web controls in the current page report tab or web report to retrieve them from the values of the web controls at runtime, provided that the values of the web controls are valid to create a parameter condition at runtime.

   To delete a parameter condition, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the conditions, select a condition and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
7. Select **OK** to accept the parameter values.

**Filter**

The Filter web action enables you to filter the specified data components based on predefined filter conditions when the designated event occurs on the trigger object at runtime.

1. In the Web Action List dialog box, select **\*Filter** and select **OK**. Designer displays the [Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096901-Filter-Web-Action-Builder-Dialog-Box).

   ![Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848576279/fltrwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current report whose records you want to filter.
3. From the **Get Input From** drop-down list, specify where to get the input, which may be a [form](https://devnet.logianalytics.com/hc/en-us/articles/1500010057522-Using-Forms-in-a-Page-Report) (available to page report only), a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls#Form) in the report or library component, or **Other in report**.
4. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a filter condition line.
5. In the **Filter On** column, specify the field on which to filter the records. You can also use a web control in the current report to retrieve the field name at runtime.
6. Specify the operator to compose the filter condition.
7. In the **Value** column, specify the value of how to filter the field. You can specify the value by yourself, or use a web control to retrieve it.

   When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".

   If you want to use a web control to retrieve the value, you need to make sure its value is one of the specified field's so that Logi Report Engine is able to create a valid filter condition at runtime.
8. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more filter conditions
   according to your requirements.
9. In the **More** column, specify the relationship between the filter conditions: **And** or **Or**.

   To delete a filter condition, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the conditions, select a condition and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
10. Select other data components in the Apply Action To box and take the above steps to specify the filter conditions on them one by one.
11. Select **OK** to accept the filter conditions.

**Sort**

The Sort web action enables you to sort the specified data components based on predefined sort conditions when the designated event occurs on the trigger object at runtime.

1. In the Web Action List dialog box, select **\*Sort** and select **OK**. Designer displays the [Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098821-Sort-Web-Action-Builder-Dialog-Box).

   ![Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848493719/sortwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current report whose records you want to sort.
3. From the **Get Input From** drop-down list, specify where to get the input, which may be a [form](https://devnet.logianalytics.com/hc/en-us/articles/1500010057522-Using-Forms-in-a-Page-Report) (available to page report only), a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls#Form) in the report or library component, or **Other in report**.
4. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a sort condition line.
5. In the **Sort On** column, specify the field in the specified data component by which to sort the records. You can also use a web control in the current report to retrieve the field name at runtime. If you use a web control, you need to make sure that Logi Report can retrieve a valid field name from the value of the web control at runtime.
6. In the **Sort Value** column, specify the sort direction: **Ascending**, **Descending**, or be retrieved from a web control at runtime. If you use a web control, you need to make sure its value is valid for composing a sort condition at runtime.
7. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more sort conditions and specify the sort-by fields and sort direction according to your requirements.

   To delete a sort condition, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the sort conditions, select a condition and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif). The order determines the sort priority of the fields at runtime.
8. Select other data components in the Apply Action To box and take the above steps to specify the sort conditions on them one by one.
9. Select **OK** to accept the sort conditions.

**Property**

The Property web action enables you to change properties of the specified report objects when the designated event occurs on the trigger object at runtime.

You can apply the Property web action in web reports and library components only.

1. In the Web Action List dialog box, select **\*Property**  and select **OK**. Designer displays the [Change Property - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095661-Change-Property-Web-Action-Builder-Dialog-Box).

   ![Change Property - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848630423/chgptywbactnbld.gif)
2. In the **Apply Action To** box, select an object the properties of which you want to change.
3. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a property condition line.
4. In the **Properties** column, specify the property you want to change. All the properties of the selected object are available in the drop-down list.
5. In the **Value** column, type in the value of the property. You can also use a web control in the current report to retrieve the value at runtime. If you use a web control, you need to make sure that Logi Report Engine can retrieve a valid property value from the value of the web control at runtime.
6. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more property conditions and specify the properties and values according to your requirements.

   To delete a property condition, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the property conditions, select a condition and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
7. Select other objects in the Apply Action To box and take the above steps to specify their property values one by one.
8. Select **OK** to accept the property values.

**Go Down**

The Go Down web action enables you to drill data of the specified data components to lower-level groups according to the predefined [hierarchies](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business views the data components use when the designated event occurs on the trigger object at runtime. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

You can apply the Go Down web action in web reports and library components only.

1. In the Web Action List dialog box, select **\*Go Down** and select **OK**. Designer displays the [Go Down - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059502-Go-Down-Web-Action-Builder-Dialog-Box).

   ![Go Down - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848528663/godwnwbactnbld.gif)
2. In the **Apply Action To** box, select a data component whose data you want to drill through.
3. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a condition line. You can add one condition at most.
4. In the **Go Down On** column, select the group on which to perform the go-down action. For a geographic map, it is **Current Layer** and cannot be changed.
5. In the **Use Hierarchy** column, select the hierarchy based on which to perform the go-down action.
   You can also use a web control in the report to retrieve a hierarchy name at runtime. For a geographic map, the **Built-in** hierarchy is used and cannot be changed.
6. In the **By Value** column, type in a value of the specified group field to go down to the lower level with the filter condition "*SpecifiedGroupField=TheValue*". You can also use a web control to retrieve a value at runtime.
7. Select other data components in the Apply Action To box and take the above steps to define the go-down conditions for them one by one.
8. Select **OK** to accept the conditions.

**Go Up**

The Go Up web action enables you to drill data of the specified data components to upper-level groups according to the predefined [hierarchies](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business views the data components use when the designated event occurs on the trigger object at runtime. It works on the groups of tables and banded objects, the row and column headers of crosstabs, the category and series axes of charts, and the current layer of geographic maps.

You can apply the Go Up web action in web reports and library components only.

1. In the Web Action List dialog box, select **\*Go Up** and select **OK**. Designer displays the [Go Up - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097441-Go-Up-Web-Action-Builder-Dialog-Box).

   ![Go Up - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848528279/goupwbactnbld.gif)
2. In the **Apply Action To** box, select a data component whose data you want to drill through.
3. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a condition line. You can add one condition at most.
4. In the **Go Up On** column, select the group on which to perform the go-up action. For a geographic map, it is **Current Layer** and cannot be changed.
5. In the **Use Hierarchy** column, select the hierarchy based on which to perform the go-up action.
   You can also use a web control in the report to retrieve a hierarchy name at runtime. For a geographic map, the **Built-in** hierarchy is used and cannot be changed.
6. Select other data components in the Apply Action To box and take the above steps to define the go-up conditions for them one by one.
7. Select **OK** to accept the conditions.

**Go To**

The Go To web action enables you to change the data fields in the specified data components when the designated event occurs on the trigger object at runtime. It works on tables, charts, and crosstabs.

You can apply the Go To web action in web reports and library components only.

1. In the Web Action List dialog box, select **\*Go To** and select **OK**. Designer displays the [Go To - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097401-Go-To-Web-Action-Builder).

   ![Go To - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856923031/gotowbactnbld.gif)
2. In the **Apply Action To** box, select a data component whose data field you want to change.
3. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a condition line. You can add one condition at most.
4. In the **Go To On** column, select the field on which to perform the go-to action.
5. In the **To Column** column, select another field to change the Go To On field to. You can also use a web control in the report to retrieve a field name at runtime.
6. To apply the go-to action by filtering the Go To On field at the same time, select **By Value** and then type in the value by which to filter the field or select a web control in the report to retrieve the value at runtime. Skip this step if you select to perform the action on a crosstab aggregate field.
7. Select other data components in the Apply Action To box and take the above steps to define the go-to conditions for them one by one.
8. Select **OK** to accept the conditions.

---

### Inserting a Text Area

1. Do one of the following to insert the text area:
   * From the **Components** panel, drag the **Text Area** icon ![Text Area icon](https://devnet.logianalytics.com/hc/article_attachments/4404848656535/icon_txtarea.gif) in the Web Controls category to the destination.
   * Select **Insert** > **Web Controls** > **Text Area** to insert to the destination.
2. Right-click the text area and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Text Area](https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box#TextArea) type.

   ![Display Type dialog box - Text Area](https://devnet.logianalytics.com/hc/article_attachments/4404856982807/dsplytp_txtarea.gif)
3. In the **Name** text box, specify the name of the text area.
4. From the **Value** drop-down list, select **<Input...>** and type the value of the text area.
5. In the **Tool Tip** text box, type the tool tip you want to show for the text area. The tool tip displays when the report users hover the mouse over the text area at runtime or in HTML output.
6. In the **Display Width** text box, specify the maximum number of characters allowed in the text area.
7. In the **Number of Lines** text box, type the number of lines that is allowed in the text area.
8. Set **Auto Wrap** to **true** if you want to automatically wrap the text in the text area.
9. Select **Read Only** if you would like to set this text area to be read-only.
10. Select **Disabled** if you want to make the text area disabled.
11. In the **Web Behaviors** panel, [bind web actions](#Action) to the text area.
12. Select **OK** to insert the text area.

### Inserting a Checkbox/Radio Button

1. Do one of the following to insert the checkbox/radio button:
   * From the **Components** panel, drag the **Checkbox** icon ![Check Box icon](https://devnet.logianalytics.com/hc/article_attachments/4404848657047/icon_chkbx.gif) or **Radio Button** icon ![Radio Button icon](https://devnet.logianalytics.com/hc/article_attachments/4404848657303/icon_rdobtn.gif) in the Web Controls category to the destination.
   * Select **Insert** > **Web Controls** > **Checkbox**/**Radio Button** to insert to the destination.
2. Right-click the checkbox/radio button and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Checkbox](https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box#Checkbox)/[Radio Button](https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box#RadioButton) type.

   ![Display Type dialog box - Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4404848592151/dsplytp_bx.gif)
3. In the **Name** text box, specify the name of the checkbox/radio button.
4. From the **Value** drop-down list, select **<Input...>** and type the value of the checkbox/radio button.
5. In the **Tool Tip** text box, type the tool tip you want to show for the checkbox/radio button. The tool tip displays when the report users hover the mouse over the checkbox/radio button at runtime or in HTML output.
6. Set **Initially Checked** to **true** if you want the checkbox/radio button to be selected by default.
7. Select **Disabled** if you want to make the checkbox/radio button disabled.
8. In the **Web Behaviors** panel, [bind web actions](#Action) to the checkbox/radio button.
9. Select **OK** to insert the checkbox/radio button.

### Inserting an Image Button

1. Do one of the following to insert the image button:
   * From the **Components** panel, drag the **Image Button** icon ![Image Button icon](https://devnet.logianalytics.com/hc/article_attachments/4404848657559/icon_imgbtn.gif) in the Web Controls category to the destination.
   * Select **Insert** > **Web Controls** > **Image Button** to insert to the destination.
2. In the Select an image dialog box, select the image to use for the image button.
3. Right-click the image button and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Image Button](https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box#ImageButton) type.

   ![Display Type - Image Button](https://devnet.logianalytics.com/hc/article_attachments/4404856983447/dsplytp_imgbtn.gif)
4. You can select the **Browse** button to change the image source.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When you create an image button by editing the display type of a DBField, formula, or summary to Image Button, you can also select the **From DBField** radio button to make the value of the DBField/formula/summary the image source. If you choose this option, the **Decode Type** drop-down list is enabled, from which you can specify the type for decoding the image.
5. Type the name of the image button in the **Name** text box.
6. From the **Value** drop-down list, select **<Input...>** and type the value of the image button.
7. Type a string in the **Alternate Text** text box to serve as the content when the image cannot display.
8. In the **Tool Tip** text box, type the tool tip you want to show for the image button. The tool tip displays when the report users hover the mouse over the image button at runtime or in HTML output.
9. Select **Disabled** if you want to make the image button disabled.
10. In the **Max Ratio** text box, specify the maximum scaling ratio up to which the image can be scaled. By default, the scaling ratio of the image is not limited. If you set the ratio to any value greater than 0, the actual scaling ratio is less than or equal to it.
11. By default, Designer displays the image in its original size. Clear **Original Size** if you want to use customized image size, then set the width and height of the area for displaying the image in the **Width** and **Height** text boxes, select **Constrain Proportion** to constrain the aspect ratio when setting the width and height, and specify the scaling mode of the image from the **Scaling Mode** drop-down list.

    The following are the available scaling modes. The specified scaling mode controls the image behavior when you adjust the size of the area for displaying the image.

    * **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
    * **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
    * **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
    * **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
    * **customize** - Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.
12. In the **Web Behaviors** panel, [bind web actions](#Action) to the image button.
13. Select **OK** to insert the image button.

### Inserting a Button

1. Do one of the following to insert the button:
   * From the **Components** panel, drag the **Button** icon ![Button icon](https://devnet.logianalytics.com/hc/article_attachments/4404857031063/icon_button.gif) in the Web Controls category to the destination.
   * Select **Insert** > **Web Controls** > **Button** to insert to the destination.
2. Right-click the button and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Button](https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box#Button) type.

   ![Display Type dialog box - Button](https://devnet.logianalytics.com/hc/article_attachments/4404856983703/dsplytp_btn.gif)
3. In the **Name** text box, specify the name of the button.
4. From the **Value** drop-down list, select **<Input...>** and type the value of the button.
5. In the **Tool Tip** text box, type the tool tip you want to show for the button. The tool tip displays when the report users hover the mouse over the button at runtime or in HTML output.
6. Select the action of the button: **None**, **Submit Form**, or **Reset Form**.
7. Select **Disabled** if you want to make the button disabled.
8. In the **Web Behaviors** panel, [bind web actions](#Action) to the button.
9. Select **OK** to insert the button.

### Inserting a List/Drop-down List

1. Do one of the following to insert the list/drop-down list:
   * From the **Components** panel, drag the **List**![List icon](https://devnet.logianalytics.com/hc/article_attachments/4404848657943/icon_list.gif) or **Drop-down List**![Drop-down List icon](https://devnet.logianalytics.com/hc/article_attachments/4404848658455/icon_drpdnlst.gif) icon in the Web Controls category to the destination.
   * Select **Insert** > **Web Controls** > **List**/**Drop-down List** to insert to the destination.
2. Right-click the list/drop-down list and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [List](https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box#List)/[Drop-down List](https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box#DropdownList) type.

   ![Display Type dialog box - List](https://devnet.logianalytics.com/hc/article_attachments/4404857031575/cmpnt_wbcntrl_basic_rpt_list.gif)
3. In the **Name** text box, specify the name of the list/drop-down list.
4. In the **Tool Tip** text box, type the tool tip you want to show for the list/drop-down list. The tool tip displays when the report users hover the mouse over the list/drop-down list at runtime or in HTML output.
5. Specify the item labels and the value of each item in the items box by inputting some strings as the labels and values respectively.

   If you want to use a DBField, formula field, or parameter field to control the value, select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the **Value** cell to insert one from the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097601-Insert-Fields-Dialog-Box), and then select the format for the inserted field from the drop-down list in the **Item Label** cell. Select the **All** radio button in the Insert Field dialog box if you want to add an "All" value to the list/drop-down list. Then when the report users select "All" as value of the list/drop-down list at runtime, all filter actions defined on the list/drop-down list will not take effect, and if you applied some other web action that needs value from the list/drop-down list, Logi Report Engine returns a "Null" value.
6. In the **Selected** text box, specify the selected value for the list/drop-down list.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When you create a list/drop-down list by editing the display type of a parameter to List/Drop-down List, Designer enables the Use Runtime Value option. You can select it to use the runtime value as the selected value of the list/drop-down list.
7. If you want to disable the list/drop-down list, select the **Disabled** option.
8. For a list web control, you can select **Allow Multiple Selections** if you want to allow multiple items to be selected in the list. If you insert the list in a web report or library component, you can further specify to display the list as Text, Button, Checkbox, or Radio Button, use the vertical or horizontal layout to display items in the list, and specify the width/height of each item and the vertical/horizontal gap between two adjacent items in the list.
9. In the **Web Behaviors** panel, [bind web actions](#Action) to the list/drop-down list.
10. Select **OK** to insert the list/drop-down list.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If you specify a tool tip for any basic web control, the tool tip displays differently on different browsers:

* On Internet Explorer, the tip text is automatically wrapped if its length exceeds the maximal tip width the browser allows. In addition, for Internet Explorer, you can manually add a new line by adding "&#10" or "&#13" ahead of the text when editing the tool tip.
* On Firefox, the tip text displays in one line with the maximal tip width the browser allows, and the text that it cannot display within the width is cut off and replaced by an ellipsis (...).

## Example: Using Web Controls in a Page Report

In the following example, we create a page report to guide you through the process of using web controls and applying web actions step by step. The example contains the following tasks:

* [Task 1: Create the sample report](#Task1)
* [Task 2: Apply a web action without parameters](#Task2)
* [Task 3: Apply a web action with parameters](#Task3)
* [Task 4: Apply a web action with the Builder Wizard](#Task4)
* [Task 5: Preview the report in Page Report Studio and apply the web actions](#Task5)

**Task 1: Create the sample report**

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Page Report** to create a page report with a standard banded object in it. [Define the banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500010094301-Inserting-a-Banded-Object#Query) as follows:
   * Use the query WorldWideSales in Data Source 1 of the catalog.
   * Show the following detail fields: Country, Product Type Name, Product Name, Unit Price, Quantity, Discount, and the formula Total.
   * Apply the filter conditions "COUNTRY = Canada AND PRODUCT TYPE NAME = Decaf".
   * Use the Classic style.
3. [Insert a crosstab into the report](https://devnet.logianalytics.com/hc/en-us/articles/1500010057182-Inserting-Crosstabs-in-a-Report) and place it below the banded object. The crosstab shares the same dataset with the banded object, comprises the column field: Product Type Name, row field: Category, and aggregate field: Total (aggregate function: Sum) and applies the Classic style.
4. Select **View** > **Page Header**to have this panel visible, then set its **Height** property to **1.0** in the Report Inspector to hold all the web controls that we will insert in the report later.
5. Save the report.

**Task 2: Apply a web action without parameters**

First, we want to enable the report users to select a button in the report to show the Search dialog box of Page Report Studio. To achieve this:

1. Select the page header panel and select **Insert** > **Web Controls** >  **Button** to insert a Button web control in it.
2. Right-click the button and select **Display Type** from the shortcut menu.
3. In the Web Behaviors box of the Display Type dialog box, specify event to **Select**, then select in the Actions column and select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the text box.
4. In the Web Action List dialog box, choose **user\_showSearchDialog** to be web action of the button, then confirm the settings.
5. Go to the Report Inspector and set the **Text** property of this button to **Search**.
6. Save the report.

**Task 3: Apply a web action with parameters**

Now we want to enable the report users to rotate the crosstab in the report and to change the report style.

1. Insert another Button web control in the page header panel of the report and place it next to the Search button.
2. Specify the **Select** event and **user\_rotateCrosstab** action to the button as explained above, then set **&CT Crosstab** to be the value of the action parameter **instanceName** ("CT Crosstab" is the name of the crosstab we can see in the report structure panel of the Report Inspector, and here you should prefix the "&" symbol to the crosstab name).
3. In the Report Inspector, edit the **Text** property of the button to **Rotate Crosstab**.
4. Insert a Label object in the page header panel and place it below the two buttons, then resize the label and edit its text to "**Change Report Style To:**".
5. Insert a Drop-down List web control next to the label.
6. Right-click the drop-down list and select **Display Type** shortcut menu.
7. In the Display Type dialog box, add these items and corresponding values to the drop-down list (to add an item line, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)):

   | Item Label | Value |
   | --- | --- |
   | Classic | Classic |
   | Black | Black |
   | Bottle Green | BottleGreen |
   | Default | Default |
   | None | None |

   Then, in the Web Behaviors box of the dialog box, set **Event** to **Data Change**, **Action** to **user\_changeStyleTo**, and specify the value for the web action parameter **styleName** to **this.value**.

   ![Specify a Value for the Web Action Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404848659095/cmpnt_wbcntrl_basic_actn_eg0.gif)
8. Save the report.

**Task 4: Apply a web action with the Builder Wizard**

The actions Filter, Sort, and Parameter have a Builder Wizard. Now we want to use the wizard to enable the report users to sort records in the banded object by one of the specified fields.

1. Insert another Drop-down List web control into the page header panel, and place it below the above web controls. The drop-down list displays as "Multi-Value Container 1" in the Report Inspector.
2. Right-click the drop-down list and select **Display Type** shortcut menu.
3. In the Display Type dialog box, add these items and corresponding values to the drop-down list:

   | Item Label | Value |
   | --- | --- |
   | Unit Price | UNIT PRICE |
   | Quantity | QUANTITY |
4. Insert a List web control next to the drop-down list. The list displays as "Multi-Value Container 2" in the Report Inspector.
5. In the Display Type dialog box for this list, add these items and corresponding values:

   | Item Label | Value |
   | --- | --- |
   | Ascending | Ascending |
   | Descending | Descending |
6. Insert a Button web control and place it next to the list, then right-click the button and select **Display Type** on the shortcut menu.
7. In the Display Type dialog box, specify Event to **Select** and Action to **Sort**, then in the Sort - Web Action Builder dialog box, select **Multi-Value Container 1** from the **Sort On** column, and **Multi-Value Container 2** from the **Sort Value** column. Confirm the settings, and go to the Report Inspector to modify the **Text** property of the button to **Sort**.
8. Save the report.

**Task 5: Preview the report in Page Report Studio and apply the web actions**

1. Select **View** > **Preview As** > **Page Report Result** to preview this report in Page Report Studio.

   ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404857031831/cmpnt_wbcntrl_basic_actn_eg1.gif)
2. Select the **Search** button. Page Report Studio displays the Search dialog box.
3. Select the **Rotate Crosstab** button. Page Report Studio rotates the columns and rows of the crosstab.

   ![Rotated Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404857032215/cmpnt_wbcntrl_basic_actn_eg2.gif)
4. Select a style from the **Change Report Style To** drop-down list, for example, select **Bottle Green**, and the report style now changes to the selected one. It affects both the banded object and the crosstab.

   ![Change Report Style](https://devnet.logianalytics.com/hc/article_attachments/4404848659607/cmpnt_wbcntrl_basic_actn_eg3.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You may notice that the value of the drop-down list does not change to the selected one after the report style is updated. To update the drop-down list value to the current report style, you need to append another action "user\_changeCompProperty" to the event Data Change to the drop-down list.
5. Select a field name from the third drop-down list and then the sort direction from the list. Here we select **Unit Price** and **Descending** respectively, then select the **Sort** button.

   Page Report Studio sorts the records in the banded object based on the Unit Price values descending.

   ![Descendingly Sort the Banded Object Records Based on the Unit Price values](https://devnet.logianalytics.com/hc/article_attachments/4404848659863/cmpnt_wbcntrl_basic_actn_eg4.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095061-Using-Basic-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057542-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component)
