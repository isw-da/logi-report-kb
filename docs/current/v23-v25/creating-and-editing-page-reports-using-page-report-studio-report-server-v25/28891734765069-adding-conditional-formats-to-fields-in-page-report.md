---
title: "Adding Conditional Formats to Fields in Page Report"
id: 28891734765069
section: "Creating and Editing Page Reports Using Page Report Studio Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891734765069-Adding-Conditional-Formats-to-Fields-in-Page-Report
updated_at: 2026-02-26T02:13:39Z
source_host: docs-report.zendesk.com
---
# 
Adding Conditional Formats to Fields in Page Report 

This topic describes how you can add conditional formats to a data field in a page report, to highlight values that you want to view and act on. Then, when the specified condition is fulfilled, the format that you defined on the condition will apply to the field values automatically.

To add conditional formats to a field:

- Right-click the field and select Conditional Formatting from the shortcut menu. Server displays the Conditional Formatting dialog box. 
    

- Select the Add button  to open the Edit Conditions dialog box to define the condition.
    

You can use the basic or advanced mode of the dialog box to define either simple or complex condition expressions. See Applying Filters to Datasets for more information on how to define a condition.

When you are adding conditional format to a data field in a crosstab, you can find the Toggle to Formula button  next to the value text box of a condition line. Select the button and you can select a field from the list to use its value in the condition. Server displays these types of fields in the list, which are of the same data type as the field on which the condition is based.

- Crosstab formulas.

- 
Dynamic resources and aggregation objects if the crosstab uses a business view.

- Select OK to save the condition.
    Server displays and highlights the new condition  in the Condition box in the Conditional Formatting dialog box.

- In the Format box, set the text format you want to apply to the values of the field when the specified condition is fulfilled, such as font face, font size, and font color. Select Blinking Text if you want to make the values blink, then, in the Duration text box, set how long it takes the values to complete the transition from the foreground color to the transparent color, in seconds. The blink settings work in the HTML output too. 

- Repeat the preceding steps to add more conditions and define the format for each condition.

- To edit a condition, select the condition in the Condition box, and select the Edit button . Then, in the Edit Conditions dialog box, edit the condition expressions as required.

- To remove a condition and the corresponding format, select the condition in the Condition box and select the Remove button .

- To adjust the priority of a condition, select the condition in the Condition box, and then select the Move Up button  or Move Down button .

- Select OK to apply the conditional formats to the field.

To make the blink settings of a conditional format take effect, you need to make sure the web browser you use supports CSS3 animation, such as Firefox, Safari, and Chrome.
