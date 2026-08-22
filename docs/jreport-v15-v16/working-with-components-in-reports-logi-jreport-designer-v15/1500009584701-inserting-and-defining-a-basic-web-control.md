---
title: "Inserting and Defining a Basic Web Control"
id: 1500009584701
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584701-Inserting-and-Defining-a-Basic-Web-Control
updated_at: 2021-07-24T05:55:52Z
---

# Inserting and Defining a Basic Web Control

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584641-Using-Basic-Web-Controls)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563922-Binding-a-Link-to-a-Basic-Web-Control)

# Inserting and Defining a Basic Web Control

The basic web controls can be inserted into report areas listed in [Component placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports#Relationship). This topic shows how to insert and define values of the web controls separately.

Below is a list of the properties in a basic web control:

> * [Text field](#TextField)
> * [Password](#Password)
> * [Text Area](#TextArea)
> * [Checkbox/Radio Button](#Checkbox)
> * [Image Button](#ImageButton)
> * [Button](#Button)
> * [List/Drop-down List](#List)

## Text Field

A text field is a text box that displays information in one row. You can specify the number of characters to display and the maximum number of characters allowed in a text field.

**To insert a text field and define its values:**

1. Do one of the following to insert the text field:

   * Drag the **Text Field** button ![Text Field](https://devnet.logianalytics.com/hc/article_attachments/4404893815575/btn_insttxtfld.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Text Field**, then select the mouse button in the destination.
2. Right-click the text field and select **Display Type** from the shortcut menu. The Display Type dialog appears.

   ![Display Type dialog - Text Field](https://devnet.logianalytics.com/hc/article_attachments/4404889371159/dsplytp_txtfld.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#TextField), enter the name, value for the text field in the Name and Value fields.
4. In the Tool Tip field, enter the tip you want to show for the text field. Then at server runtime or in HTML results, when you hover the mouse over the text field, the tooltip will be displayed.
5. Set the number of characters in the Display Width field, and the maximum number of characters the user can enter in the Max Length field.
6. Check the **Read Only** checkbox if you would like to set this text field to be read-only.
7. Check the **Disabled** checkbox if you want to make the text field disabled.
8. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584661-Applying-Web-Actions-to-a-Basic-Web-Control) to the text field in the Web Behaviors box.
9. Upon finishing, select the **OK** button to close this dialog.

## Password

Password is a [text field](#TextField) in which the typed password is displayed as asterisks. You can specify the number of characters to display and the maximum number of characters allowed in a password.

**To insert a password and define its values:**

1. Do one of the following to insert the password:

   * Drag the  **Password** button ![Password button](https://devnet.logianalytics.com/hc/article_attachments/4404889399831/btn_instpswrd.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Password**, then select the mouse button in the destination.
2. Right-click the password and select **Display Type** from the shortcut menu. The Display Type dialog appears.
3. Define the values for the password as for a text field.

## Text Area

A text area is a text box that displays information in multiple rows. You can specify the maximum number of characters allowed in a text area. When the input text reaches the width of the text area, the following text will auto wrap to the next row, and so on.

For text area, there are three options that are useless: Number of Lines and Auto Wrap in the Display Type dialog, and Maximum Width in the Report Inspector.

**To insert a text area and define its values:**

1. Do one of the following to insert the text area:

   * Drag the **Text Area** button ![Text Area button](https://devnet.logianalytics.com/hc/article_attachments/4404893972247/btn_insttxtarea.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Text Area**, then select the mouse button in the destination.
2. Right-click the text area and select **Display Type** from the shortcut menu. The Display Type dialog appears.

   ![Display Type dialog - Text Area](https://devnet.logianalytics.com/hc/article_attachments/4404893931159/dsplytp_txtarea.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#TextArea), enter the name, value of the text area in the Name and Value fields.
4. In the Tool Tip field, enter the tip you want to show for the text area. Then at server runtime or in HTML results, when you hover the mouse over the text area, the tooltip will be displayed.
5. In the Display Width field, specify the maximum number of characters allowed in the text area.
6. Check the **Read Only** option if you would like to set this text area to be read-only.
7. Check the **Disabled** checkbox if you want to make the text area disabled.
8. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584661-Applying-Web-Actions-to-a-Basic-Web-Control) to the text area in the Web Behaviors box.
9. Upon finishing, select the **OK** button to close this dialog.

## Checkbox/Radio Button

A checkbox or a radio button is a button used to specify the value of a Boolean type option. When the button is selected, the option is enabled, and when unselected, the option is disabled. A checkbox can work alone while two or more radio buttons need to work together to enable only one from multiple options.

The way to insert and define the values of a checkbox and radio button is the same.

1. Do one of the following to insert the checkbox/radio button:

   * Drag the button of **Checkbox**![Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4404893815959/btn_instchkbx.gif) or **Radio Button ![Radio Button](https://devnet.logianalytics.com/hc/article_attachments/4404893972503/btn_instrdobtn.gif)** from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Checkbox**/**Radio Button**, then select the mouse button in the destination.
2. Right-click the checkbox/radio button and select **Display Type** from the shortcut menu. The Display Type dialog appears.

   ![Display Type dialog - Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4404893931415/dsplytp_bx.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#Checkbox), specify the name, value of the checkbox/radio button in the Name and Value fields.
4. In the Tool Tip field, enter the tip you want to show for the checkbox/radio button. Then at server runtime or in HTML results, when you hover the mouse over the checkbox/radio button, the tooltip will be displayed.
5. Set Initially Checked to **true** if you want the checkbox/radio button to be selected by default.
6. Check the **Disabled** checkbox if you want to make the checkbox/radio button disabled.
7. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584661-Applying-Web-Actions-to-a-Basic-Web-Control) to the checkbox/radio button in the Web Behaviors box.
8. Upon finishing, select **OK** to close this dialog.

## Image Button

An image button allows you to import an image from your local disk as a button.

**To insert an image button and define its values:**

1. Do one of the following to insert the image button:
   * Drag the button of  **Image Button** ![Image Button](https://devnet.logianalytics.com/hc/article_attachments/4404893972759/btn_instimgbtn.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Image Button**, then select the mouse button in the destination.
2. Right-click the image button and select **Display Type** from the shortcut menu. The Display Type dialog appears.

   ![Display Type - Image Button](https://devnet.logianalytics.com/hc/article_attachments/4404889371671/dsplytp_imgbtn.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#ImageButton), select the **Browse** button to specify the image source. For a DBField, formula, or a summary, you can also check the **From DBField** radio button to make the value of the DBField/formula/summary the image source. If you choose this option, the Decode Type drop-down list is enabled, from which you can specify the type for decoding the image.
4. Enter the name, value of the image button in the Name and Value fields.
5. Type a string in the Alternate Text field to serve as content when the image cannot be rendered.
6. In the Tool Tip field, enter the tip you want to show for the image button. Then at server runtime or in HTML results, when you hover the mouse over the image button, the tooltip will be displayed.
7. Check the **Disabled** checkbox if you want to make the image button disabled.
8. Specify the scaling mode of the image button from the Scaling Mode drop-down list, and the maximum scaling ratio in the Max Ratio field. By default the scaling ratio of the image button is not limited. If it is set to any value greater than 0, the actual scaling ratio is less than or equal to it.
9. Specify the size of the image button.
   * If you choose to use the original size of the image, check the **Original Size** option.
   * If you want to use customized image size, uncheck **Original Size**, and then set the display width and height of the image in the Width and Height fields. Check the **Constrain Proportion** option if you want to constrain aspect ratio of the image when setting the width and height.
10. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584661-Applying-Web-Actions-to-a-Basic-Web-Control) to the image button in the Web Behaviors box.
11. Upon finishing, select the **OK** button to close the dialog.

## Button

A button can be used for submitting or resetting a form.

**To insert a button and define its values:**

1. Do one of the following to insert the button:
   * Drag **Button ![Button](https://devnet.logianalytics.com/hc/article_attachments/4404893973015/btn_instbtn.gif)** from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Button**, then select the mouse button in the destination.
2. Right-click the button and select **Display Type** from the shortcut menu. The Display Type dialog appears.

   ![Display Type dialog - Button](https://devnet.logianalytics.com/hc/article_attachments/4404893931671/dsplytp_btn.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#Button), enter the name, value of the button in the Name and Value fields.
4. In the Tool Tip field, enter the tip you want to show for the button. Then at server runtime or in HTML results, when you hover the mouse over the button, the tooltip will be displayed.
5. Select the action of the button: None, Submit Form or Reset Form.
6. Check the **Disabled** checkbox if you want to make the button disabled.
7. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584661-Applying-Web-Actions-to-a-Basic-Web-Control) to the button in the Web Behaviors box.
8. Upon finishing, select **OK** to close this dialog.

## List/Drop-down List

Lists and drop-down lists are generally called multi-valued containers. They both provide a list of values for users to select from. A list displays values in a box with or without scrollbar and is suitable for showing just a few values. A drop-down list is a good choice for providing a long list of values while taking smaller room and presenting more values at the first sight.

**To insert a list/drop-down list and define its values:**

1. Do one of the following to insert the list/drop-down list:

   * Drag the button of **List**![List button](https://devnet.logianalytics.com/hc/article_attachments/4404893816471/btn_instlist.gif) or **Drop-down List ![Drop-down List button](https://devnet.logianalytics.com/hc/article_attachments/4404893816727/btn_instdrpdnlst.gif)** button from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **List**/**Drop-down List**, then select the mouse button in the destination.
2. Right-click the list/drop-down list and select **Display Type** from the shortcut menu. The Display Type dialog appears.

   ![Display Type dialog - Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4404889371927/dsplytp_drpdwnlst.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#DropdownList), enter a name for the list/drop-down list in the Name field.
4. In the Tool Tip field, enter the tooltip you want to show for the list/drop-down list. Then at server runtime or in HTML results, when you hover the mouse over the list/drop-down list, the tooltip will be displayed.
5. Specify the item labels and the value of each item in the items box by inputting some strings as the labels and values respectively.

   If you want to use a DBField/formula field/parameter field to control the value, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the Value column to insert one with the Insert Fields dialog, and then select the format for the inserted field from the drop-down list in the Item Label column. Check the **All** radio button in the Insert Field dialog if you want to add an All value to the list/drop-down list. Then when All is selected as value of the list/drop-down list at runtime, all filter actions defined on the list/drop-down list will not take effect, and if you applied some other web action that needs value from the list/drop-down list, a Null value will be returned.
6. If the display type is defined as List, you can check the **Allow Multiple Selections** checkbox if you want to allow multiple items to be selected.
7. In the Selected field, specify the selected value for the list/drop-down list.
8. If you want to disable the list/drop-down list, check the **Disabled** option.
9. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584661-Applying-Web-Actions-to-a-Basic-Web-Control) to the list/drop-down list in the Web Behaviors box.
10. When done, select **OK** to apply the settings.

**Notes:**

* The display type of a basic web control can also be changed after it has been created. Basic web controls other than list and drop-down list can be converted to each other, and can be displayed as a [general type](https://devnet.logianalytics.com/hc/en-us/articles/1500009563422-Changing-the-Display-Type-of-a-Label). You may notice that these web controls have a common Class Type property value "Label" in the Report Inspector, and this signifies that these web controls are labels in nature.
* List and drop-down list can be converted to each other, however they cannot be displayed as any other type.
* DBFields, parameter fields, formula fields, summary fields, special fields, and images can also be displayed as a basic web control type. From this view, these objects can be considered as basic web controls too.
* Some of the basic web control values can be controlled by formulas. To control a value by a formula, select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) behind the text field of the value and then select a formula from the drop-down list. If the given formulas cannot meet your requirements, select the <CREATE FORMULA> item in the list to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula) as required.
* If you have specified a tooltip for any basic web control, the tooltip is displayed differently on different browsers:

  + On Internet Explorer, the tip text is automatically wrapped if its length exceeds the maximal tip width the browser allows. In addition, for Internet Explorer, you can manually make some text displayed in a new line by adding &#10 or &#13 ahead of the text when editing it in the Tool Tip field.
  + On Firefox, the tip text is displayed in one line with the maximal tip width the browser allows, and the text that cannot be displayed within the width will be cut off and replaced by ellipsis.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584641-Using-Basic-Web-Controls)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563922-Binding-a-Link-to-a-Basic-Web-Control)
