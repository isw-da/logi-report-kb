---
title: "Adding Conditional Formats to Data Fields"
id: 1500009724722
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724722-Adding-Conditional-Formats-to-Data-Fields
updated_at: 2021-07-25T07:18:35Z
---

# Adding Conditional Formats to Data Fields

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751581-Using-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724862-Applying-Parameters)

# Adding Conditional Formats to Data Fields

You can add conditional formats to the data fields in tables, banded objects and crosstabs in a report, then when a specified condition is fulfilled, the format defined on the condition will be applied to the field values automatically. This is very useful to highlight values that might need to be acted.

**To add conditional formats to a data field:**

1. Right-click the data field and select **Conditional Formatting**  from the shortcut menu. Report Server displays the [Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009748121-Conditional-Formatting) dialog box.

   ![Conditional Formatting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942469015/cndtnlfmt.gif)
2. Select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to open the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009721522-Edit-Conditions) dialog box to define a condition.

   ![Edit Conditions dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4404942469271/edtcndtn_basic.gif)

   There are the basic and advanced modes of the dialog box for you to define either simple expressions or complex expressions. See [Applying a Filter to the Business View for a Data Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters#Expression)for more information on how to define a condition.

   When you are adding conditional format to a data field in a crosstab, you can find the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936750871/btn_fmla1.gif) next to the value text box of a condition line. Select the button and you can select a [dynamic resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) or an aggregation object from the drop-down list to use its value in the condition. The listed resources are of the same data type as the field on which the condition is based.
3. Select **OK** to save the condition.

   The newly added condition is now displayed and highlighted in the Condition box in the Conditional Formatting dialog box.
4. In the Format box, set the format which will be applied to values of the field when the specified condition is fulfilled, for example, the font face, font size, font color, and so on. Select **Blinking Text** if you want to make the values blink, then in the Duration text box, set how long it takes the values to complete the transition from the foreground color to the transparent color, in seconds. The blink settings work in the HTML result of the report too.
5. Repeat the above steps to add more conditions and define the format for each condition.

   To edit a condition, select the condition in the Condition box, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936751127/btn_pgrpt_edit.gif). In the Edit Conditions dialog box, edit the expressions as required.

   To remove a condition and the corresponding format, select the condition in the Condition box and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).

   To adjust the priority of a condition, select the condition in the Condition box and then select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404936751383/btn_mvup1.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif).
6. Select **OK** to apply the conditional formats to the field.

**Note:** To make the blink settings of a conditional format take effect, you need to make sure the web browser you use supports CSS3 animation, such as Firefox, Safari, Chrome and Internet Explorer 10 or above.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751581-Using-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724862-Applying-Parameters)
