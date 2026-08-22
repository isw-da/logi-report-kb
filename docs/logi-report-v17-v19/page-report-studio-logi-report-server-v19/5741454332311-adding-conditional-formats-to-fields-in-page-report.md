---
title: "Adding Conditional Formats to Fields in Page Report"
id: 5741454332311
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741454332311-Adding-Conditional-Formats-to-Fields-in-Page-Report
updated_at: 2022-10-31T17:18:15Z
---

# Adding Conditional Formats to Fields in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741474913047-Going-Through-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report)

# Adding Conditional Formats to Fields in Page Report

This topic describes how you can add conditional formats to a data field in a page report, to highlight values that you want to view and act on. Then, when the specified condition is fulfilled, the format that you defined on the condition will apply to the field values automatically.

**To add conditional formats to a field:**

1. Right-click the field and select **Conditional Formatting** from the shortcut menu. Server displays the [Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741410129687-Conditional-Formatting-Dialog-Box-Properties).

   ![Conditional Formatting dialog](https://devnet.logianalytics.com/hc/article_attachments/9905673658775/cndtnlfmt.gif)
2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741397029783-Edit-Conditions-Dialog-Box-Properties) to define the condition.

   ![Edit Conditions dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/9905661756439/edtcndtn_basic.gif)

   You can use the basic or advanced mode of the dialog box to define either simple or complex condition expressions. See [Applying Filters to Datasets](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report#Filter) for more information on how to define a condition.

   When you are adding conditional format to a data field in a crosstab, you can find the **Toggle to Formula** button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9905634004631/btn_fmla1.gif) next to the value text box of a condition line. Select the button and you can select a field from the list to use its value in the condition. Server displays these types of fields in the list, which are of the same data type as the field on which the condition is based.

   * Crosstab formulas.
   * [Dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/5741438849559-Using-Dynamic-Resources-in-Page-Report) and aggregation objects if the crosstab uses a business view.
3. Select **OK** to save the condition.

   Server displays and highlights the new condition in the Condition box in the Conditional Formatting dialog box.
4. In the Format box, set the text format you want to apply to the values of the field when the specified condition is fulfilled, such as font face, font size, and font color. Select **Blinking Text** if you want to make the values blink, then, in the **Duration** text box, set how long it takes the values to complete the transition from the foreground color to the transparent color, in seconds. The blink settings work in the HTML output too.
5. Repeat the preceding steps to add more conditions and define the format for each condition.
6. To edit a condition, select the condition in the Condition box, and select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905655522327/btn_pgrpt_edit.gif). Then, in the Edit Conditions dialog box, edit the condition expressions as required.
7. To remove a condition and the corresponding format, select the condition in the Condition box and select the **Remove** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif).
8. To adjust the priority of a condition, select the condition in the Condition box, and then select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905634194455/btn_mvup1.gif) or **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905618988823/btn_mvdown1.gif).
9. Select **OK** to apply the conditional formats to the field.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)To make the blink settings of a conditional format take effect, you need to make sure the web browser you use supports CSS3 animation, such as Firefox, Safari, and Chrome.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741474913047-Going-Through-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report)
