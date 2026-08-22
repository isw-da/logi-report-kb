---
title: "Formatting Scatter Chart"
id: 45190424361229
section: "Working with Components in Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190424361229-Formatting-Scatter-Chart
updated_at: 2026-04-30T15:12:12Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Formatting Scatter Chart

This topic describes how you can format a scatter chart.

-  Right-click any scatter marker in the scatter chart and select Format Scatter on the shortcut menu, or double-click any scatter marker in the chart. Designer displays the Format Scatter dialog box.

- In the General tab, set the general properties of the scatter chart. 
    
- In the Layout box, select None if you do not want to use lines to connect the markers in the scatter chart, or select Straight Line or Curved Line to connect the markers using lines of the corresponding style.

- In the Line box, specify the thickness of the lines that connect the markers in the scatter chart.

- In the Node box, specify the style, width, and height of the markers in the scatter chart. 

- In the Fill tab, set the color pattern to fill the scatter markers.
    

- Make your choice for the Self Settings option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the Pattern List property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the scatter markers in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later. 

- Specify the color and transparency to fill the selected scatter markers in the same data series (to change the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color in the text box)

- You can also select Color List to specify the color pattern for scatter markers in the same data series respectively in the Color List dialog box.

- Skip the Data Label tab because Designer does not support displaying data labels in scatter charts.

- In the Hint tab, specify properties of the chart hint. A hint displays the value a marker in the scatter chart represents when you point to the marker in Designer view mode, in HTML output, or at runtime. 
    

- Clear Show Category and Series if you do not want to include the category and series values in the hint.

- Specify whether to scale big and small numbers in the hint.

- Select Customize Chart Value Name to use customized names for the fields on the value axis in the hint and select the ellipsis to customize the names as you want.

 You should not edit  the Show Tips property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint. 

- Select OK to apply the settings and close the dialog box.
