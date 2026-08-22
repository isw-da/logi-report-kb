---
title: "Formatting Bubble Chart"
id: 45190455352717
section: "Working with Components in Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190455352717-Formatting-Bubble-Chart
updated_at: 2026-04-30T15:12:08Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Formatting Bubble Chart

This topic describes how you can format the bubbles in a bubble chart.

- Right-click any bubble in the bubble chart and select Format Bubble  on the shortcut menu, or double-click any bubble in the chart. Designer displays the Format Bubble dialog box.

- In the General tab, specify whether to apply a  three-dimensional visual effect  to the bubbles, and you can use the Cut Bubble Based on XY Area option to control whether to cut the bubbles when they are beyond the chart wall (the area formed by the X axis and Y axis). While, Designer still cuts the bubbles if they go beyond the chart paper.

- In the Fill tab, set the color pattern to fill the bubbles. 
    

- Make your choice for the Self Settings option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the Pattern List property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the bubbles in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later. 

- If the chart has no series field, set the color and transparency to fill all bubbles (to change the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color in the text box).

- If the chart has series field, set the color and transparency to fill the bubbles in the current data series, that is, the bubbles in the same data series as the one you have selected on to open the Format Bubble dialog box. You can also select Color List to specify the color pattern for bubbles in each data series respectively using the Color List dialog box. 

- In the Border tab, select Show Border if you want to display border for the bubbles, then specify the border properties. 

- Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.

- In the Path box, specify the fill pattern of the border: Outline Path or Fill Path.

- In the Dash box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.

- In the Radius box, specify the radius size of the rounded corners of the border. When Use Depth is false and Show Border is selected, a rounded corner bar will be drawn.

- Skip the Data Label tab because Designer does not support displaying data labels in bubble charts.

- In the Hint tab, specify properties of the chart hint.  A hint displays the value a bubble represents when you point to the bubble in Designer view mode, in HTML output, or at runtime. 
    

- Clear Show Category and Series if you do not want to include the category and series values in the hint.

- Specify whether to scale big and small numbers in the hint.

- Select Customize Chart Value Name to use customized names for the fields on the value axis in the hint and select the ellipsis to customize the names as you want.

 You should not edit  the Show Tips property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint. 

- Select OK to accept the changes and close the dialog box.
