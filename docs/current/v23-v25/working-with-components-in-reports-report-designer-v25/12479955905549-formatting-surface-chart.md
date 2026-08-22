---
title: "Formatting Surface Chart"
id: 12479955905549
section: "Working with Components in Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479955905549-Formatting-Surface-Chart
updated_at: 2026-02-25T23:50:34Z
source_host: docs-report.zendesk.com
---
# 
Formatting Surface Chart

This topic describes how you can format the surface of a surface chart.

- Right-click any vertex in the surface chart and select Format Surface  on the shortcut menu, or double-click any vertex in the surface chart. Designer displays the Format Surface dialog box.

- In the Fill tab, specify the color pattern to fill the range sections in the surface chart.
- Make your choice for the Self Settings option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the Pattern List property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the range sections in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later. 

- Specify the color and transparency to fill the selected range sections in the same data series (to change the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color in the text box).

- You can also select Color List to specify the color pattern for range sections in the same data series respectively in the Color List dialog box.

- In the Border tab, select Show Border if you want to show the border of the range sections in the surface chart, then specify the border properties.

- Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.

- In the Path box, specify the fill pattern of the border: Outline Path or Fill Path.

- In the Dash box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.

- In the Radius box, specify the radius size of the rounded corners of the border. When Use Depth is false and Show Border is selected, a rounded corner bar will be drawn.

- Skip the Data Label tab because Designer does not support displaying data labels in surface charts.

- In the Hint tab, specify properties of the chart hint. A hint displays the value a vertex in the surface chart represents when you point to the vertex in Designer view mode, in HTML output, or at runtime.    

- Clear Show Category and Series if you do not want to include the category and series values in the hint.

- Specify whether to scale big and small numbers in the hint.

- Select Customize Chart Value Name to use customized names for the fields on the value axis in the hint and select the ellipsis to customize the names as you want.

 You should not edit  the Show Tips property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint. 

- Select OK to accept the changes and close the dialog box.
