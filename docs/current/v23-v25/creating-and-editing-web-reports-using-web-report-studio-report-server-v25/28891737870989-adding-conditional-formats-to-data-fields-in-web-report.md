---
title: "Adding Conditional Formats to Data Fields in Web Report"
id: 28891737870989
section: "Creating and Editing Web Reports Using Web Report Studio Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891737870989-Adding-Conditional-Formats-to-Data-Fields-in-Web-Report
updated_at: 2026-02-26T02:13:57Z
source_host: docs-report.zendesk.com
---
# 
Adding Conditional Formats to Data Fields in Web Report

You can add conditional formats to the data fields in tables, banded objects, and crosstabs in a web report. This topic describes how you can add conditional formats.

When a specified condition is fulfilled, Server applies the format that you defined for the condition to the field values automatically. This is very useful to highlight values that you need to pay attention to or act on.

To add conditional formats to a data field:

- Right-click the data field and select Conditional Formatting from the shortcut menu. Server displays the Conditional Formatting dialog box.
    

- Select the Add button . Server displays the Edit Conditions dialog box.
    

There are the basic and advanced modes of the dialog box for you to define either simple expressions or complex expressions. See Applying a Filter to Datasets for Data Components for more information about how to define a condition.

When you are adding conditional format to a data field in a crosstab, you can find the Toggle to Formula button  next to the value text box of a condition line. Select this button and then you can select a dynamic resource or an aggregation object from the drop-down list to use its value in the condition. Server lists the resources of the same data type as the field on which the condition is based. You can also create a crosstab formula here.

- Select OK to save the condition.Server displays and highlights the condition in the Condition box in the Conditional Formatting dialog box.

- In the Format box, set the format to apply to values of the field when the specified condition is fulfilled, for example, the font face, font size, and font color. 

- Select Blinking Text if you want to make the values blink, then in the Duration text box, set how long it takes the values to complete the transition from the foreground color to the transparent color, in seconds. The blink settings work in the HTML report output too. 

- Repeat the preceding steps to add more conditions and define the format for each condition.

- To edit a condition, select it in the Condition box, then select the Edit button . In the Edit Conditions dialog box, edit the expressions as you want. 

- To remove a condition and the corresponding format, select the condition in the Condition box and select the Remove button.

- To adjust the priority of a condition, select the condition in the Condition box and then select the Move Up button  or Move Down button .

- Select OK to apply the conditional formats to the field.

To make the blink settings of a conditional format take effect, you need to make sure the web browser you use supports CSS3 animation, such as Firefox, Safari, and Chrome.
