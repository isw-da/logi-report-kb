---
title: "Using Basic Web Controls in a Report"
id: 4405661415703
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report
updated_at: 2022-01-27T20:34:38Z
---

# Using Basic Web Controls in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661412503-Using-Basic-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661414679-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component)

# Using Basic Web Controls in a Report

This topic introduces how you can insert and define values of basic web controls in a report. It also presents an example to demonstrate how you can use basic web controls in a page report to achieve specific goals.

This topic contains the following sections:

* [Inserting Basic Web Controls](#Insert)
  + [Inserting a Text Field/Password](#TextField)
  + [Inserting a Text Area](#TextArea)
  + [Inserting a Checkbox/Radio Button](#Checkbox)
  + [Inserting an Image Button](#ImageButton)
  + [Inserting a Button](#Button)
  + [Inserting a List/Drop-down List](#List)
* [Example: Using Web Controls in a Page Report](#Example)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) You cannot use basic web controls in business view-based page reports.

## Inserting Basic Web Controls

You can insert basic web controls in report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship) in a report.

The following are some tips for you when using basic web controls.

* When defining a basic web control in a page report that uses query resources, you can find the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) next to some options such as Name and Tool Tip in the Display Type dialog box. When this button is available, you can select it and [select a formula](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties) or DBField from the given drop-down list to control an option. If you select a DBField as the value of an option, Designer applies the first record of the field in the database.
* You can also change the [display type](https://devnet.logianalytics.com/hc/en-us/articles/4405661930647-Changing-the-Display-Type-of-Objects-in-Reports) of a basic web control after it is created. You can convert basic web controls other than list and drop-down list to each other and display them as a general type, and you may notice that these web controls have a common Class Type property value "Label" in the Report Inspector, which signifies that these web controls are labels in nature.

### Inserting a Text Field/Password

1. Position the mouse pointer at the destination where you want to insert the text field/password.
2. Do either of the following:
   * From the **Components** panel, drag the **Text Field** icon ![Text Field icon](https://devnet.logianalytics.com/hc/article_attachments/4420550962839/icon_txtfld.gif) or **Password** icon ![Password icon](https://devnet.logianalytics.com/hc/article_attachments/4420556229911/icon_pswd.gif) in the **Web Controls** category to the destination.
   * Navigate to **Home**/**Insert** > **Web Controls** > **Text Field**/**Password**. If the specified destination is not the report body or the page header/footer panel, move the mouse pointer to the desired position and select again.
3. Right-click the text field/password and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Text Field](https://devnet.logianalytics.com/hc/en-us/articles/4405664451863-Display-Type-Dialog-Box#TextField) type.

   ![Display Type dialog box - Text Field](https://devnet.logianalytics.com/hc/article_attachments/4420542161047/dsplytp_txtfld.gif)
4. In the **Web Options** panel, specify options of the text field/password.
   1. In the **Name** text box, specify the name of the text field/password.
   2. From the **Value** drop-down list, select **<Input...>** and type the value of the text field/password.
   3. In the **Tool Tip** text box, type the tool tip you want to show for the text field/password. The tool tip displays when users hover the mouse over the text field/password at runtime or in HTML output.
   4. Set the number of characters in the **Display Width** text box, and the maximum number of characters the user can specify in the **Max Length** text box.
   5. Select **Read Only** if you would like to set this text field/password to be read-only.
   6. Select **Disabled** if you want to disable the text field/password at runtime.
5. In the **Web Behaviors** panel, bind web actions to the text field/password to trigger specific operations at runtime.

   Adding web actions to a web control enables you to customize the web control to make it respond to interactive events, and execute corresponding actions such as sort and filter. For example, you can associate an action with a web control's select event, then at runtime, when users run the report and select the web control, Logi Report Engine executes the defined operation.

   **To bind web actions**

   1. Choose an event from the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif).

      Logi Report supports the following events for triggering web actions.

      | Event | Description |
      | --- | --- |
      | Blur | Fires when the object loses the input focus. |
      | Data Change | Fires when the contents of the object or selection changes. |
      | Click | Fires when users select the left mouse button on the object. |
      | onContextMenu | Fires when users select the right mouse button on the object, opening the shortcut menu. |
      | Double\_select | Fires when users double-click the object. |
      | Focus | Fires when the object receives focus. |
      | Key Down | Fires when users press a key. |
      | Key Press | Fires when users press an alphanumeric key. |
      | Key Up | Fires when users release a key. |
      | Mouse Down | Fires when users select the object with either mouse button. |
      | Mouse Move | Fires whens users move the mouse over the object. |
      | Mouse Out | Fires when users move the mouse pointer outside the boundaries of the object. |
      | Mouse Over | Fires when users move the mouse pointer into the object. |
      | Mouse Up | Fires when users release a mouse button while the mouse is over the object. |
      | Resize | Fires when the size of the object is about to change. |
      | Scroll | Fires when users reposition the scroll box in the scroll bar on the object. |
      | Select | Fires when the current selection changes. |
   2. In the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661744791-Web-Action-List-Dialog-Box), select the required action and select **OK**. Designer displays different web actions in the dialog box according to the report type.

      ![Web Action List dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550963095/wbactnlst.gif)

      * If you select one of the following web actions: [Parameter](#Parameter), [Filter](#Filter), [Sort](#Sort), [Property](#Property), [Go Down](#GoDown), [Go Up](#GoUp), [Go To](#GoTo), [Send Message](https://devnet.logianalytics.com/hc/en-us/articles/4405661935255-Delivering-Messages-Between-Library-Components#Action), or [Customized Control](https://devnet.logianalytics.com/hc/en-us/articles/4405661399959-Using-Customized-Controls-in-Tables), Designer displays the corresponding web action builder dialog box for you to build the action.
      * If you select [Customized Control from Lib](https://devnet.logianalytics.com/hc/en-us/articles/4405661399959-Using-Customized-Controls-in-Tables), Designer displays the [Manage Customized Controls dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661640855-Manage-Customized-Controls-Dialog-Box), which shows all the customized control files in the customized control library. Select the one you want and select **OK**.
      * If you select a user-defined action which requires no parameter, for example, user\_showTOC, Designer applies the action to the web control and closes the Web Action List dialog box. Such web actions are only available to page reports that use query resources.
      * If you select a user-defined action which needs parameters, for example, user\_zoomTo, Designer displays the Parameters dialog box, which lists the parameters the web action requires. Such web actions are only available to page reports that use query resources.

        The following shows a sample dialog box.

        ![Parameters dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542187287/cmpnt_wbcntrl_basic_rpt_prm.gif)

        Specify the parameter values in the **Value** column. For parameters that refer to instance name, you can type in the mapping name of the instance, or the display name plus the prefix "&" as the parameter value. For more information about the parameter values, see [Appendix 3: Parameters of User-Defined Web Actions](https://devnet.logianalytics.com/hc/en-us/articles/4405661328535-Appendix-3-Parameters-of-User-Defined-Web-Actions).

      You can also define your own web actions by adding API functions into the file **API.js** located at `<designer_install_root>\lib\html\javascript\dhtml` and the same name file located at `<server_install_root>\public_html\dhtmljsp\js`.
   3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) in the Display Type dialog box and repeat the preceding steps to add more web actions. To delete a web action, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).
   4. Adjust the order of the web actions by selecting a web action and selecting **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif). Then, when an event which has been bound with more than one action happens at runtime, Logi Report Engine triggers the upper action first.
6. Select **OK** to insert the text field/password.

---

The following details how to define a specific web action.

**Parameter**

You can use the Parameter web action to run a specified report, especially one with parameters using the predefined parameter values when the designated event occurs on the trigger object at runtime.

**To specify the Parameter web action**

1. In the Web Action List dialog box, select **\*Parameter** and select **OK**. Designer displays the [Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661672983-Parameter-Web-Action-Builder-Dialog-Box).

   ![Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556132503/prmwbactnbld.gif)
2. Specify the handler which receives the parameters of the web action. The handler may be the default one in the current server, or in another server specified by **Customized Path**.
3. From the **Get Input From** drop-down list, specify where to get the input, which may be a [form](https://devnet.logianalytics.com/hc/en-us/articles/4405661413527-Using-Forms-in-a-Page-Report) (available to page report only), a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Form) in the report, or "Other in report".
4. In the **Apply Action To** section, specify how to apply the action.
   * If you want to apply the action to run a report, select **Report** and select **Browse** to specify the report in the current catalog that you want to run when the event occurs on the trigger object at runtime; or select **Web Control** and select a web control in the current report to retrieve the report name at runtime. Then from the **Target Frame** drop-down list, select the window or frame to open the report.
   * Select **Refresh Current Report** if you want to refresh the current report when the event occurs on the trigger object at runtime.
5. In the parameter box, specify the parameters and the values with which to run or refresh the current report.
   * When you select Report and specify a report, if the report contains parameters, Designer loads the parameters automatically into the parameter box. Edit the value for each parameter.
   * When you select Web Control or Refresh Current Report, Designer lists all the parameters used by the current report in the parameter box if it contains parameters. Edit the value for each parameter.
6. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add more parameter lines to specify other parameter values. If you specify a parameter value more than once, the last setting takes effect. To delete a parameter, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the parameter lines.

   When specifying the name and value of a parameter, you can also use web controls in the current report to retrieve them from the values of the web controls at runtime.
7. Select **OK** to accept the parameter values.

**Filter**

You can use the Filter web action to filter a specified data component in a page report, or several data components at a time in a web report/library component based on predefined filter conditions when the designated event occurs on the trigger object at runtime.

**To specify the Filter web action in a page report**

1. In the Web Action List dialog box, select **\*Filter** and select **OK**. Designer displays the [Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661554839-Filter-Web-Action-Builder-Dialog-Box#Page).

   ![Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542151063/fltrwbactnbld-pg.gif)
2. From the **Get Input From** drop-down list, specify where to get the input, which can be a [form](https://devnet.logianalytics.com/hc/en-us/articles/4405661413527-Using-Forms-in-a-Page-Report), a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Form) in the current page report, or "Other in report".
3. From the **Apply Action To** drop-down list, select a data component in the page report the data of which you want to filter.
4. In the **Filter On** column, specify the field on which to filter data. You can filter on a DBField in the query that the specified data component uses or a formula related to the query, or select a web control in the page report to retrieve the field name at runtime.
5. In the **Operator** column, specify the operator to compose the filter condition.
6. In the **Value** column, specify the value of how to filter the field. You can select **<Input...>** from the drop-down list and type the value in the text box, or select a web control to retrieve it at runtime.

   When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
7. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add more condition lines and specify the filter conditions. To delete a filter condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the condition lines.
8. In the **More** column, specify the relationship between the filter conditions: "And" or "Or".
9. Select **OK** to accept the filter conditions.

**To specify the Filter web action in a web report/library component**

1. In the Web Action List dialog box, select **\*Filter** and select **OK**. Designer displays the [Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661554839-Filter-Web-Action-Builder-Dialog-Box#Web).

   ![Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550918039/fltrwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current web report/library component the data of which you want to filter.
3. From the **Get Input From** drop-down list, specify where to get the input, which can be a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Form) in the web report/library component, or "Other in report".
4. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add a filter condition line.
5. In the **Filter On** column, specify the field on which to filter data. You can filter on a field contained in the business view the specified data component uses, or select a web control in the web report/library component to retrieve the field name at runtime.
6. In the **Operator** column, specify the operator to compose the filter condition.
7. In the **Value** column, specify the value of how to filter the field. You can select **<Input...>** from the drop-down list and type the value in the text box, or select a web control to retrieve it at runtime.

   When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
8. Add more condition lines and specify the filter conditions. To delete a filter condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the condition lines.
9. In the **More** column, specify the relationship between the filter conditions: "And" or "Or".
10. Select other data components in the Apply Action To box and take the preceding steps to specify the filter conditions on them.
11. Select **OK** to accept the filter conditions.

**Sort**

You can use the Sort web action to sort a specified data component or group in a page report, or several data components and groups at a time in a web report/library component based on predefined sort conditions when the designated event occurs on the trigger object at runtime.

**To specify the Sort web action in a page report**

1. In the Web Action List dialog box, select **\*Sort** and select **OK**. Designer displays the [Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661722263-Sort-Web-Action-Builder-Dialog-Box#Page).

   ![Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556129559/sortwbactnbld-pg.gif)
2. From the **Get Input From** drop-down list, specify where to get the input, which can be a [form](https://devnet.logianalytics.com/hc/en-us/articles/4405661413527-Using-Forms-in-a-Page-Report), a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Form) in the current page report, or "Other in report".
3. From the **Apply Action To** drop-down list, select a data component in the current page report tab or a group of a table/banded object in the page report tab, the data of which you want to sort.
4. In the **Sort On** column,
   * If you select to sort a data component, you can sort on a field of the data component, or select a web control in the page report tab to retrieve the field name at runtime.
   * If you select to sort a group, leave the cell in the column blank or select a web control to retrieve the field name at runtime.
5. In the **Sort Value** column, specify the order to perform the sort: Ascending, Descending, or select a web control to get the sort order at runtime.
6. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add more condition lines and specify the sort conditions. To delete a sort condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).
7. Adjust the order of the sort conditions using **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif). The order determines the sort priority of the conditions at runtime.
8. Select **OK** to accept the sort conditions.

**To specify the Sort web action in a web report/library component**

1. In the Web Action List dialog box, select **\*Sort** and select **OK**. Designer displays the [Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661722263-Sort-Web-Action-Builder-Dialog-Box#Web).

   ![Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542101655/sortwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the web report/library component or a group of a table/banded object in the web report/library component, the data of which you want to sort.
3. From the **Get Input From** drop-down list, specify where to get the input, which can be a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Form) in the current page report, or "Other in report".
4. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add a sort condition.
5. In the **Sort On** column,
   * If you select to sort a data component, you can sort on a field of the data component, or select a web control in the web report/library component to retrieve the field name at runtime.
   * If you select to sort a group, leave the cell in the column blank or select a web control to retrieve the field name at runtime.
6. In the **Sort Value** column, specify the order to perform the sort: Ascending, Descending, or select a web control to get the sort order at runtime.
7. Add more condition lines and specify the sort conditions. To delete a sort condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif).
8. Adjust the order of the sort conditions using **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif). The order determines the sort priority of the conditions at runtime.
9. Select other data components and groups in the Apply Action To box and take the preceding steps to specify the sort conditions on them.
10. Select **OK** to accept the sort conditions.

**Property**

You can use the Property web action to change properties of the specified report objects when the designated event occurs on the trigger object at runtime. However, you can apply this web action in web reports and library components only.

**To specify the Property web action**

1. In the Web Action List dialog box, select **\*Property** and select **OK**. Designer displays the [Change Property - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661464727-Change-Property-Web-Action-Builder-Dialog-Box).

   ![Change Property - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556220439/chgptywbactnbld.gif)
2. In the **Apply Action To** box, select an object in the current web report/library component the properties of which you want to change.
3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add a property condition line.
4. In the **Properties** column, select the property of the object you want to change.
5. In the **Value** column, type the value of the property. You can also select a web control in the web report/library component to retrieve the value at runtime.
6. Add more condition lines and specify the property conditions. To delete a property condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the condition lines.
7. Select other objects in the Apply Action To box and take the preceding steps to specify their property values.
8. Select **OK** to accept the property values.

**Go Down**

You can use the Go Down web action to drill data of the specified data components to lower-level groups according to the predefined [hierarchies](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business views the data components use when the designated event occurs on the trigger object at runtime. However, you can apply this web action in web reports and library components only.

The Go Down web action works on the groups of tables and banded objects, the column and row fields of crosstabs, the category and series fields of charts, and the current layer of geographic maps.

**To specify the Go Down web action**

1. In the Web Action List dialog box, select **\*Go Down** and select **OK**. Designer displays the [Go Down - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664513431-Go-Down-Web-Action-Builder-Dialog-Box).

   ![Go Down - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556230551/godwnwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current web report/library component whose data you want to drill through.
3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add a condition line. You can add one condition only.
4. In the **Go Down On** column, select the group in the specified data component, on which to perform the go-down action. For a geographic map, it is "Current Layer" and you cannot change it.
5. In the **Use Hierarchy** column, select the hierarchy based on which to perform the go-down action.
   You can also select a web control in the web report/library component to retrieve a hierarchy name at runtime. For a geographic map, the "Built-in" hierarchy is used and you cannot change it.
6. In the **By Value** column, type a value of the specified group field to go down to the lower level with the filter condition "*SpecifiedGroupField=TheValue*". You can also use a web control to retrieve a value at runtime.
7. Select other data components in the Apply Action To box and take the preceding steps to define the go-down conditions for them.
8. Select **OK** to accept the conditions.

**Go Up**

You can use the Go Up web action to drill data of the specified data components to upper-level groups according to the predefined [hierarchies](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business views the data components use when the designated event occurs on the trigger object at runtime. However, you can apply this web action in web reports and library components only.

The Go Up web action works on the groups of tables and banded objects, the column and row fields of crosstabs, the category and series fields of charts, and the current layer of geographic maps.

**To specify the Go Up web action**

1. In the Web Action List dialog box, select **\*Go Up** and select **OK**. Designer displays the [Go Up - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661614615-Go-Up-Web-Action-Builder-Dialog-Box).

   ![Go Up - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542187799/goupwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current web report/library component whose data you want to drill through.
3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add a condition line. You can add one condition only.
4. In the **Go Up On** column, select a group in the specified data component, on which to perform the go-up action. For a geographic map, it is "Current Layer" and you cannot change it.
5. In the **Use Hierarchy** column, select the hierarchy based on which to perform the go-up action, or select a web control in the web report/library component to retrieve a hierarchy name at runtime. For a geographic map, the "Built-in" hierarchy is used and you cannot change it.
6. Select other data components in the Apply Action To box and take the preceding steps to define the go-up conditions for them.
7. Select **OK** to accept the conditions.

**Go To**

You can use the Go To web action enables you to change the data fields in the specified data components when the designated event occurs on the trigger object at runtime. However, you can apply this web action in web reports and library components only.

The Go To web action works on the groups of tables, the column/row fields and aggregations of crosstabs, and the category and series fields of charts.

**To specify the Go To web action**

1. In the Web Action List dialog box, select **\*Go To** and select **OK**. Designer displays the [Go To - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661611799-Go-To-Web-Action-Builder-Dialog-Box).

   ![Go To - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550892439/gotowbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current web report/library component whose data field you want to change.
3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add a condition line. You can add one condition only.
4. In the **Go To On** column, select a group for a table or chart, or a column/row field or aggregation for a crosstab, on which to perform the go-to action.
5. In the **To Column** column, select another group object in the business view the web report/library component uses to change the "Go To On" field to, or select a web control in the web report/library component to retrieve a group name at runtime.
6. To apply the go-to action by filtering the "Go To On" field at the same time, select **By Value**, then select **<Input...>** from the drop-down list and type the value by which to filter the field in the text box or select a web control to retrieve the value at runtime. Skip this step if you select to perform the action on a crosstab aggregation.
7. Select other data components in the Apply Action To box and take the preceding steps to define the go-to conditions for them.
8. Select **OK** to accept the conditions.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) When you select a web control in the condition to define a web action, Logi Report Engine should be able to retrieve a valid value from the web control at runtime in order to compose a valid condition; otherwise, nothing happens when the designated event occurs on the trigger object.

---

### Inserting a Text Area

1. Position the mouse pointer at the destination where you want to insert the text area.
2. Do either of the following:
   * From the **Components** panel, drag the **Text Area** icon ![Text Area icon](https://devnet.logianalytics.com/hc/article_attachments/4420542188311/icon_txtarea.gif) in the **Web Controls** category to the destination.
   * Navigate to **Home**/**Insert** > **Web Controls** > **Text Area**. If the specified destination is not the report body or the page header/footer panel, move the mouse pointer to the desired position and select again.
3. Right-click the text area and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Text Area](https://devnet.logianalytics.com/hc/en-us/articles/4405664451863-Display-Type-Dialog-Box#TextArea) type.

   ![Display Type dialog box - Text Area](https://devnet.logianalytics.com/hc/article_attachments/4420542161687/dsplytp_txtarea.gif)
4. In the **Name** text box, specify the name of the text area.
5. From the **Value** drop-down list, select **<Input...>** and type the value of the text area.
6. In the **Tool Tip** text box, type the tool tip you want to show for the text area. The tool tip displays when users hover the mouse over the text area at runtime or in HTML output.
7. In the **Display Width** text box, specify the maximum number of characters allowed in the text area.
8. In the **Number of Lines** text box, type the number of lines that is allowed in the text area.
9. Set **Auto Wrap** to **true** if you want to automatically wrap the text in the text area.
10. Select **Read Only** if you would like to set this text area to be read-only.
11. Select **Disabled** if you want to disable the text area at runtime.
12. In the **Web Behaviors** panel, [bind web actions](#Action) to the text area.
13. Select **OK** to insert the text area.

### Inserting a Checkbox/Radio Button

1. Position the mouse pointer at the destination where you want to insert the checkbox/radio button.
2. Do either of the following:
   * From the **Components** panel, drag the **Checkbox** icon ![Checkbox icon](https://devnet.logianalytics.com/hc/article_attachments/4420556230807/icon_chkbx.gif) or **Radio Button** icon ![Radio Button icon](https://devnet.logianalytics.com/hc/article_attachments/4420556231063/icon_rdobtn.gif) in the **Web Controls** category to the destination.
   * Navigate to **Home**/**Insert** > **Web Controls** > **Checkbox**/**Radio Button**. If the specified destination is not the report body or the page header/footer panel, move the mouse pointer to the desired position and select again.
3. Right-click the checkbox/radio button and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Checkbox](https://devnet.logianalytics.com/hc/en-us/articles/4405664451863-Display-Type-Dialog-Box#Checkbox)/[Radio Button](https://devnet.logianalytics.com/hc/en-us/articles/4405664451863-Display-Type-Dialog-Box#RadioButton) type.

   ![Display Type dialog box - Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4420542161943/dsplytp_bx.gif)
4. In the **Name** text box, specify the name of the checkbox/radio button.
5. From the **Value** drop-down list, select **<Input...>** and type the value of the checkbox/radio button.
6. In the **Tool Tip** text box, type the tool tip you want to show for the checkbox/radio button. The tool tip displays when users hover the mouse over the checkbox/radio button at runtime or in HTML output.
7. Set **Initially Checked** to **true** if you want to select the checkbox/radio button by default at runtime.
8. Select **Disabled** if you want to disable the checkbox/radio button at runtime.
9. In the **Web Behaviors** panel, [bind web actions](#Action) to the checkbox/radio button.
10. Select **OK** to insert the checkbox/radio button.

### Inserting an Image Button

1. Position the mouse pointer at the destination where you want to insert the image button.
2. Do either of the following:
   * From the **Components** panel, drag the **Image Button** icon ![Image Button icon](https://devnet.logianalytics.com/hc/article_attachments/4420542188567/icon_imgbtn.gif) in the **Web Controls** category to the destination.
   * Select **Web Controls** > **Image Button** on the **Home** or **Insert** menu tab. If the specified destination is not the report body or the page header/footer panel, move the mouse pointer to the desired position and select again.
3. In the Select an image dialog box, select the image to use for the image button.
4. Right-click the image button and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Image Button](https://devnet.logianalytics.com/hc/en-us/articles/4405664451863-Display-Type-Dialog-Box#ImageButton) type.

   ![Display Type - Image Button](https://devnet.logianalytics.com/hc/article_attachments/4420550943895/dsplytp_imgbtn.gif)
5. You can select **Browse** to change the image source.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) When you create an image button by editing the display type of a DBField, formula, or summary to Image Button, you can also select **From DBField** to use the value of the DBField/formula/summary as the image source. If you choose this option, Designer enables the **Decode Type** drop-down list, from which you can specify the type for decoding the image.
6. Type the name of the image button in the **Name** text box.
7. From the **Value** drop-down list, select **<Input...>** and type the value of the image button.
8. Type a string in the **Alternate Text** text box to serve as the content when the image cannot display.
9. In the **Tool Tip** text box, type the tool tip you want to show for the image button. The tool tip displays when users hover the mouse over the image button at runtime or in HTML output.
10. Select **Disabled** if you want to disable the image button at runtime.
11. In the **Max Ratio** text box, specify the maximum scaling ratio of the image. By default, the scaling ratio of the image is not limited. If you set the ratio to any value greater than 0, the actual scaling ratio is less than or equal to it.
12. By default, Designer displays the image in its original size. Clear **Original Size** if you want to use customized image size, then set the width and height of the area for displaying the image in the **Width** and **Height** text boxes, select **Constrain Proportion** to constrain the aspect ratio when setting the width and height, and specify the scaling mode of the image from the **Scaling Mode** drop-down list.

    The following are the available scaling modes. The specified scaling mode controls the image behavior when you adjust the size of the area for displaying the image.

    * **actual size**  
      Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
    * **fit image**  
      Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
    * **fit width**  
      Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
    * **fit height**  
      Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
    * **customize**  
      Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.
13. In the **Web Behaviors** panel, [bind web actions](#Action) to the image button.
14. Select **OK** to insert the image button.

### Inserting a Button

1. Position the mouse pointer at the destination where you want to insert the button.
2. Do either of the following:
   * From the **Components** panel, drag the **Button** icon ![Button icon](https://devnet.logianalytics.com/hc/article_attachments/4420556231319/icon_button.gif) in the **Web Controls** category to the destination.
   * Select **Web Controls** > **Button** on the **Home** or **Insert** menu tab. If the specified destination is not the report body or the page header/footer panel, move the mouse pointer to the desired position and select again.
3. Right-click the button and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [Button](https://devnet.logianalytics.com/hc/en-us/articles/4405664451863-Display-Type-Dialog-Box#Button) type.

   ![Display Type dialog box - Button](https://devnet.logianalytics.com/hc/article_attachments/4420556207383/dsplytp_btn.gif)
4. In the **Name** text box, specify the name of the button.
5. From the **Value** drop-down list, select **<Input...>** and type the value of the button.
6. In the **Tool Tip** text box, type the tool tip you want to show for the button. The tool tip displays when users hover the mouse over the button at runtime or in HTML output.
7. Select the action of the button: None, Submit Form, or Reset Form.
8. Select **Disabled** if you want to disable the button at runtime.
9. In the **Web Behaviors** panel, [bind web actions](#Action) to the button.
10. Select **OK** to insert the button.

### Inserting a List/Drop-down List

1. Position the mouse pointer at the destination where you want to insert the list/drop-down list.
2. Do either of the following:
   * From the **Components** panel, drag the **List**![List icon](https://devnet.logianalytics.com/hc/article_attachments/4420542188823/icon_list.gif) or **Drop-down List**![Drop-down List icon](https://devnet.logianalytics.com/hc/article_attachments/4420550963607/icon_drpdnlst.gif) icon in the **Web Controls** category to the destination.
   * Navigate to **Home**/**Insert** > **Web Controls** > **List**/**Drop-down List**. If the specified destination is not the report body or the page header/footer panel, move the mouse pointer to the desired position and select again.
3. Right-click the list/drop-down list and select **Display Type** from the shortcut menu.

   Designer displays the Display Type dialog box, showing the web options for the [List](https://devnet.logianalytics.com/hc/en-us/articles/4405664451863-Display-Type-Dialog-Box#List)/[Drop-down List](https://devnet.logianalytics.com/hc/en-us/articles/4405664451863-Display-Type-Dialog-Box#DropdownList) type.

   ![Display Type dialog box - List](https://devnet.logianalytics.com/hc/article_attachments/4420556231831/cmpnt_wbcntrl_basic_rpt_list.gif)
4. In the **Name** text box, specify the name of the list/drop-down list.
5. In the **Tool Tip** text box, type the tool tip you want to show for the list/drop-down list. The tool tip displays when users hover the mouse over the list/drop-down list at runtime or in HTML output.
6. Specify the item labels and the value of each item in the item box by inputting some strings as the labels and values respectively.

   If you want to use a DBField, formula field, or parameter field to control the value, select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif) in the **Value** cell to insert one using the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661626647-Insert-Fields-Dialog-Box), and then select the format for the inserted field from the drop-down list in the **Item Label** cell. Select **All** in the Insert Field dialog box if you want to add an "All" value to the list/drop-down list. Then, when users select "All" as value of the list/drop-down list at runtime, all filter actions defined on the list/drop-down list will not take effect, and if you apply some other web action that needs value from the list/drop-down list, Logi Report Engine returns a "Null" value.
7. In the **Selected** text box, specify the selected value for the list/drop-down list.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) When you create a list/drop-down list by editing the display type of a parameter to List/Drop-down List, Designer enables the Use Runtime Value option. You can select it to use the runtime value as the selected value of the list/drop-down list.
8. Select **Disabled** if you want to disable the list/drop-down list at runtime.
9. For a list web control, you can also specify the following settings:
   * Select **Allow Multiple Selections** if you want to allow multiple items to be selected in the list.
   * If you insert the list in a web report or library component, you can further specify to display the list as Text, Button, Checkbox, or Radio Button, use the vertical or horizontal layout to display items in the list, and specify the width/height of each item and the vertical/horizontal gap between two adjacent items in the list.
10. In the **Web Behaviors** panel, [bind web actions](#Action) to the list/drop-down list.
11. Select **OK** to insert the list/drop-down list.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you specify a tool tip for any basic web control, the tool tip displays differently on different browsers.

* On Internet Explorer, the tip text is automatically wrapped if its length exceeds the maximal tip width the browser allows. In addition, for Internet Explorer, you can manually add a new line by adding "&#10" or "&#13" ahead of the text when editing the tool tip.
* On Firefox, the tip text displays in one line with the maximal tip width the browser allows, and the text that it cannot display within the width is cut off and replaced by an ellipsis (...).

## Example: Using Web Controls in a Page Report

In the following example, we create a page report to guide you through the process of using web controls and applying web actions step by step. The example contains the following tasks:

* [Task 1: Create the sample report](#Task1)
* [Task 2: Apply a web action without parameters](#Task2)
* [Task 3: Apply web actions with parameters](#Task3)
* [Task 4: Apply a web action using the Action Builder](#Task4)
* [Task 5: Preview the report in Page Report Studio and apply the web actions](#Task5)

**Task 1: Create the sample report**

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Page Report** to create a page report with a banded object in its first report tab.
3. [Define the banded object](https://devnet.logianalytics.com/hc/en-us/articles/4405661347735-Inserting-Banded-Objects-in-a-Report#Query) as follows:
   * Use the query **WorldWideSales** in Data Source 1 of the catalog.
   * Display these detail fields: the DBFields **Customer ID**, **Product Name**, **Unit Price**, and **Quantity**, **Discount**, and the formula **Total**.
   * Apply the filter "COUNTRY = Canada AND PRODUCT TYPE NAME = Decaf".
   * Use the **Classic** style.
4. [Insert a crosstab into the report](https://devnet.logianalytics.com/hc/en-us/articles/4405664394775-Inserting-Crosstabs-in-a-Report) and place it below the banded object. The crosstab shares the same dataset with the banded object, contains the column field **Product Type Name**, row field **Region**, and aggregate field **Total** with the aggregate function **Sum**, and applies the **Classic** style too.
5. Navigate to **View** > **Page Header** to display this panel, then set its **Height** property to **1.5** in the Report Inspector to hold all the web controls.

   ![The Initial Report](https://devnet.logianalytics.com/hc/article_attachments/4420550964247/cmpnt_wbcntrl_basic_rpt_eg1.gif)
6. Save the report.

**Task 2: Apply a web action without parameters**

First, we want to enable users to select a button in the report to show the Search dialog box of Page Report Studio.

1. Select the page header panel.
2. Navigate to **Insert** > **Web Controls** > **Button** to insert a Button web control in it.
3. Right-click the button and select **Display Type** from the shortcut menu.
4. In the **Web Behaviors** box of the Display Type dialog box, specify the event to **Click**, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif).
5. In the Web Action List dialog box, select **user\_showSearchDialog** and select **OK**.

   ![Define Web Action for the Button](https://devnet.logianalytics.com/hc/article_attachments/4420556232087/cmpnt_wbcntrl_basic_rpt_eg2.gif)
6. Select **OK** in the Display Type dialog box to confirm the settings.
7. Double-click the button and edit its text set to **Search**.
8. Save the report.

**Task 3: Apply web actions with parameters**

Now we want to enable users to rotate the crosstab in the report and to change the report style.

1. Insert another Button web control in the page header panel of the report and place it next to the Search button.
2. Right-click the new button and select **Display Type** from the shortcut menu.
3. Specify the **Click** event and **user\_rotateCrosstab** web action to the button, then set **&CTCrossTab** as the value of the action parameter **instanceName** (you can get the instance name of an object via its Instance Name property in the Report Inspector, and you should prefix the "&" symbol to the name when setting the instanceName parameter).

   ![The Search Button](https://devnet.logianalytics.com/hc/article_attachments/4420556232343/cmpnt_wbcntrl_basic_rpt_eg3.gif)
4. In the Report Inspector, edit the **Text** property of the new button to **Rotate Crosstab**, and **Width** property to **1.5**.
5. Insert a Label object in the page header panel and place it below the two buttons, then resize the label and edit its text to "**Change Report Style To:**".
6. Insert a Drop-down List web control next to the label.
7. Right-click the drop-down list and select **Display Type** shortcut menu.
8. In the Display Type dialog box, add these items and corresponding values to the drop-down list (to add an item line, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif)):

   | Item Label | Value |
   | --- | --- |
   | Black | Black |
   | BottleGreen | BottleGreen |
   | Classic | Classic |
   | Commercial | Commercial |
   | DefaultSequential | DefaultSequential |
9. In the **Web Behaviors** box, specify the **Data Change** event and **user\_changeStyleTo** web action to the drop-down list, then specify the value of the action parameter **styleName** to **this.value**.

   ![The Style Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4420556232599/cmpnt_wbcntrl_basic_rpt_eg4.gif)
10. Save the report.

**Task 4: Apply a web action using the Action Builder**

Some web actions have its own Action Builder. Now we want to use the Sort Action Builder to enable users to sort the banded object by one of the specified fields.

1. Insert another Drop-down List web control into the page header panel, and place it below the existing web controls. The drop-down list displays as "Multi-Value Container 1" in the Report Inspector.
2. Right-click the drop-down list and select **Display Type** from the shortcut menu.
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
6. Change the height of the list to display its values completely.
7. Insert another Button web control and place it next to the list, then right-click the button and select **Display Type** on the shortcut menu.
8. In the Display Type dialog box, specify the event to **Click** and action to **Sort**, then in the Sort - Web Action Builder dialog box, keep the default selection for **Apply Action To** to sort the banded object, select **Multi-Value Container 1** from the **Sort On** column, and **Multi-Value Container 2** from the **Sort Value** column. Confirm the settings.

   ![Define the Sort Web Action](https://devnet.logianalytics.com/hc/article_attachments/4420556232983/cmpnt_wbcntrl_basic_rpt_eg5.gif)
9. Double-click the button and edit its text to **Sort**.
10. Save the report.

**Task 5: Preview the report in Page Report Studio and apply the web actions**

1. Navigate to **View** > **Preview As** > **Page Report Result** to preview the report in Page Report Studio.

   ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4420556233239/cmpnt_wbcntrl_basic_rpt_eg6.gif)
2. Select **Search**. Page Report Studio displays the Search dialog box.
3. Select **Rotate Crosstab**. Page Report Studio rotates the columns and rows of the crosstab.

   ![Rotate the Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4420556233495/cmpnt_wbcntrl_basic_rpt_eg7.gif)
4. Select a style from the **Change Report Style To** drop-down list, for example, select **BottleGreen**. The report now applies the new style.

   ![Change Report Style](https://devnet.logianalytics.com/hc/article_attachments/4420556233879/cmpnt_wbcntrl_basic_rpt_eg8.gif)
5. Select a field name from the second drop-down list and then the sort direction from the list. Here we select **Quantity** and **Descending** respectively, then select **Sort**.

   Page Report Studio sorts the banded object based on the Quantity values in descending order.

   ![Sort the Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4420550967703/cmpnt_wbcntrl_basic_rpt_eg9.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661412503-Using-Basic-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661414679-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component)
