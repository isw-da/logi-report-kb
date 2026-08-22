---
title: "Formatting Stock Chart"
id: 28897778222861
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897778222861-Formatting-Stock-Chart
updated_at: 2024-09-30T09:11:41Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Formatting Stock Chart

This topic describes how you can format a stock chart.

- Right-click any stock line in the stock chart and select Format Stock on the shortcut menu, or double-click any stock line. Designer displays the Format Stock dialog box.

- In the General tab, specify the color and thickness of the stock lines (to change the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color in the text box). For an Open-High-Low-Close stock chart, you can also specify the up color to indicate that the opening price is lower than the closing price, the down color to indicate that the opening price is higher than the closing price, and the width of the stock bars.

- For an Open-High-Low-Close stock chart, in the Border tab, select Show Border if you want to display border for the stock bars, then specify the border properties.    

- Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.

- In the Path box, specify the fill pattern of the border: Outline Path or Fill Path.

- In the Dash box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.

- Skip the Data Label tab because Designer does not support displaying data labels in stock charts.

- In the Hint tab, specify properties of the chart hint. A hint displays the value a stock line represents when you point to the stock line in Designer view mode, in HTML output, or at runtime. 

- Clear Show Category and Series if you do not want to include the category and series values in the hint.

- Specify whether to scale big and small numbers in the hint.

- Select Customize Chart Value Name to use customized names for the fields on the value axis in the hint and select the ellipsis to customize the names as you want.

 You should not edit  the Show Tips property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint. 

- Select OK to accept the changes and close the dialog box.

Previous Topic  Next Topic
