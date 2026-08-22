---
title: "Adding Conditional Formats to Data Fields in Web Report"
id: 5741490590615
section: "Web Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741490590615-Adding-Conditional-Formats-to-Data-Fields-in-Web-Report
updated_at: 2022-10-31T17:18:31Z
---

# Adding Conditional Formats to Data Fields in Web Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741484852887-Using-Web-Controls-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741490884759-Applying-Parameters-to-Web-Report)

# Adding Conditional Formats to Data Fields in Web Report

You can add conditional formats to the data fields in tables, banded objects, and crosstabs in a web report. This topic describes how you can add conditional formats.

When a specified condition is fulfilled, Server applies the format that you defined for the condition to the field values automatically. This is very useful to highlight values that you need to pay attention to or act on.

**To add conditional formats to a data field:**

1. Right-click the data field and select **Conditional Formatting** from the shortcut menu. Server displays the [Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457508759-Conditional-Formatting-Dialog-Box-Properties).

   ![Conditional Formatting dialog](https://devnet.logianalytics.com/hc/article_attachments/9905655469463/cndtnlfmt.gif)
2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif). Server displays the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741422694679-Edit-Conditions-Dialog-Box-Properties).

   ![Edit Conditions dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/9905655497367/edtcndtn_basic.gif)

   There are the basic and advanced modes of the dialog box for you to define either simple expressions or complex expressions. See [Applying a Filter to Datasets for Data Components](https://devnet.logianalytics.com/hc/en-us/articles/5741470839191-Applying-Filters-in-Web-Report#Expression) for more information about how to define a condition.

   When you are adding conditional format to a data field in a crosstab, you can find the **Toggle to Formula** button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9905634004631/btn_fmla1.gif) next to the value text box of a condition line. Select this button and then you can select a [dynamic resource](https://devnet.logianalytics.com/hc/en-us/articles/5741476426263-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-) or an aggregation object from the drop-down list to use its value in the condition. Server lists the resources of the same data type as the field on which the condition is based. You can also [create a crosstab formula](https://devnet.logianalytics.com/hc/en-us/articles/5741476426263-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-#CrosstabFormula) here.
3. Select **OK** to save the condition.

   Server displays and highlights the condition in the Condition box in the Conditional Formatting dialog box.
4. In the Format box, set the format to apply to values of the field when the specified condition is fulfilled, for example, the font face, font size, and font color.
5. Select **Blinking Text** if you want to make the values blink, then in the **Duration** text box, set how long it takes the values to complete the transition from the foreground color to the transparent color, in seconds. The blink settings work in the HTML report output too.
6. Repeat the preceding steps to add more conditions and define the format for each condition.
7. To edit a condition, select it in the Condition box, then select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905655522327/btn_pgrpt_edit.gif). In the Edit Conditions dialog box, edit the expressions as you want.
8. To remove a condition and the corresponding format, select the condition in the Condition box and select the **Remove** button![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif).
9. To adjust the priority of a condition, select the condition in the Condition box and then select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905634194455/btn_mvup1.gif) or **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905618988823/btn_mvdown1.gif).
10. Select **OK** to apply the conditional formats to the field.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)To make the blink settings of a conditional format take effect, you need to make sure the web browser you use supports CSS3 animation, such as Firefox, Safari, and Chrome.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741484852887-Using-Web-Controls-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741490884759-Applying-Parameters-to-Web-Report)
