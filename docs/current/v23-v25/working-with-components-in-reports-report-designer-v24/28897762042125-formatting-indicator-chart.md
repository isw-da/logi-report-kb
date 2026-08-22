---
title: "Formatting Indicator Chart"
id: 28897762042125
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897762042125-Formatting-Indicator-Chart
updated_at: 2024-09-30T09:08:19Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Formatting Indicator Chart

This topic describes how you can format the indicators in an indicator chart.

- Right-click an indicator in the indicator chart and select Format Indicator from the shortcut menu, or double-click any indicator in the chart. Designer displays the Format Indicator dialog box.

- In the General tab, specify the general properties of the indicators.
    
- In the Style box, specify to use an indicator or multiple indicators to show each value in the chart.

- In the Option box, set the left margin, top margin, range radius, and the shape of the indicators. If the indicator chart displays numeric values, select how to fill the indicators from the Fill Type drop-down list: select all to fill the whole indicator or based on max value to fill a portion of the indicators calculated based on the maximum value of the chart. When you select "based on max value", if a value is less than the minimum value, Designer does not fill the indicator; if a value is greater than the minimum value, Designer fills the portion of the value in the indicator which is divided by the maximum value.

- In the Border box, select Show Border if you want to show the border of the indicators, then specify properties of the border including the line style, thickness, color, and transparency (to change the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color in the text box). 

- 
If the  indicator chart displays numeric values, in the Value box, specify the maximum and minimum values to display in the chart. By default, Designer calculates the minimum and maximum values based on the real values in the chart using certain algorithm, which is the meaning of the default value "Auto".

- In the Value Label box, select Show Value to show the value labels for the indicators, then specify the position of the value labels relative to the indicators, and whether to scale big and small numbers in the values.

- In the Frame tab, specify properties for the frame of the indicator chart.
    

- In the Size box, specify the size of the frame.

- In the Fill box, specify the color and transparency to fill the frame.

- In the Border box, specify properties for the border of the frame, including the type, color, line style, transparency, thickness, ending style, line joint mode, fill pattern, and dash size.

- In the Category Label box, select Show Category Label to show the category labels for the indicators, which display the category value each indicator represents, and the position of the category labels relative to the indicators.

- In the Range Color tab, specify different colors or images to fill the indicators.
    
- If the indicator chart displays Boolean values, select in the Color and Name columns to specify the color from the color palette and  the name for the two values in the indicator chart. If you want to use images to represent the two values, select Show Image, then select  in the Image column and select the ellipsis to specify the image for each value.
      

- If the indicator chart displays String or numeric values:        

- By default, Designer provides three predefined value ranges and calculates the minimum and maximum values for each range using certain algorithm, which is the meaning of the default value "Auto": if the indicator chart displays numeric values, Designer calculates the minimum and maximum values according to the minimum and maximum values that you specify in the General tab; if the indicator chart displays String values, Designer calculates the minimum and maximum values according to how many values there are in the chart and the alphabetic order of the values. You can select in the corresponding columns to edit the minimum and maximum values, colors from the color palette, and names for the ranges according to your own requirements.

- Select Add to add and define more ranges.

- To delete a range, select it and select Remove.

- In the Others box, specify the name and color for the values that do not fall into any of the ranges you define.

- If you want to use images to represent the values, select Show Image and specify the image for each value range and the Others value group respectively.

 If you only edit the minimum and maximum values for one range but keep the default "Auto" value for all the rest ranges, Designer regards that there is only one value range in the indicator chart; therefore, you should either keep the default "Auto" value for all the ranges to let Designer calculates them for you, or edit them all to apply your own values.

- In the Hint tab, specify properties of the chart hint. A hint displays the value an indicator in the indicator chart represents when you point to the indicator in Designer view mode, in HTML result, or at runtime.
    

- Clear Show Category and Series if you do not want to include the category and series values in the hint.

- Specify whether to scale big and small numbers in the hint.

- Select Customize Chart Value Name to use customized names for the fields on the value axis in the hint and select the ellipsis to customize the names as you want.

 You should not edit  the Show Tips property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint. 

- For an indicator chart in a library component, you can specify web behaviors for it in the Behaviors tab,  to enable users to trigger different web actions when they perform specific operations such as Click and Mouse Over on the     indicators at runtime. 

- Select OK to accept the changes and close the dialog box.

Previous Topic  Next Topic
