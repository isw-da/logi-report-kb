---
title: "Adding Conditional Formats to Fields"
id: 1500009691622
section: "Editing Page Reports in Page Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691622-Adding-Conditional-Formats-to-Fields
updated_at: 2021-11-03T06:56:48Z
---

# Adding Conditional Formats to Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718141-Going)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691602-Applying-Filters)

# Adding Conditional Formats to Fields

You can add conditional formats to the data fields as well as the special fields Page Number and User Name in a report, then when a specified condition is fulfilled, the format defined on the condition will be applied to the field values automatically. This is very useful to highlight values that might need to be acted.

**To add conditional formats to a field:**

1. Right-click the field and select **Conditional Formatting**  from the shortcut menu. The [Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009687102-Conditional-Formatting) dialog appears.

   ![Conditional Formatting dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112547351/cndtnlfmt.gif)
2. Select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4412131380631/btn_add1.gif) to open the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009712961-Edit-Conditions) dialog to define the condition as required.

   ![Edit Conditions dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4412131425943/edtcndtn_basic.gif)

   There are the basic and advanced modes of the dialog for you to define either simple or complex condition expressions. See [Applying a Filter to the Business View for a Data Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009691602-Applying-Filters#Filter) for more information on how to define a condition.

   When you are adding conditional format to a data field in a crosstab, you can find the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4412112517271/btn_fmla1.gif) next to the value text box of a condition line. Select the button and you can select an object from the drop-down list to use its value in the condition. The following objects that are of the same data type as the field on which the condition is based are provided in the drop-down list:

   * Crosstab formulas if the crosstab is created on a query resource
   * [Dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009691582-Using-Dynamic-Resources) and aggregation objects if the crosstab is created on a business view
3. Select **OK** to save the condition.

   The newly added condition is now displayed and highlighted in the Condition box in the Conditional Formatting dialog.
4. In the Format box, set the format which will be applied to values of the field when the specified condition is fulfilled, for example, the font face, font size, font color, and so on. Check **Blinking Text** if you want to make the values blink, then in the Duration text box, set how long it takes the values to complete the transition from the foreground color to the transparent color, in seconds. The blink settings work in the HTML result of the report too.
5. Repeat the above steps to add more conditions and define the format for each condition as required.

   To edit a condition, select the condition in the Condition box, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131399959/btn_pgrpt_edit.gif). In the Edit Conditions dialog, edit the condition expressions as required.

   To remove a condition and the corresponding format, select the condition in the Condition box and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif).

   To adjust the priority of a condition, select the condition in the Condition box and then select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412131400215/btn_mvup1.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412139498007/btn_mvdown1.gif).
6. Select **OK** to apply the conditional formats to the field.

**Note:** To make the blink settings of a conditional format take effect, you need to make sure the web browser you use supports CSS3 animation, such as Firefox, Safari, Chrome and Internet Explorer 10 or above.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718141-Going)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691602-Applying-Filters)
