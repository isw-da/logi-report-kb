---
title: "Formatting Bar/Bench Chart"
id: 45190408201869
section: "Working with Components in Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190408201869-Formatting-Bar-Bench-Chart
updated_at: 2026-04-30T15:12:08Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Formatting Bar/Bench Chart

This topic describes how you can format the bars in a bar or bench chart.

- Right-click any bar/bench in the bar/bench chart and select Format 2D Bar or Format 3D Bar from the shortcut menu, or double-click any bar/bench in the chart. Designer displays the Format Bar dialog box. 

- In the General tab, specify the general properties of the bars.
    
- For a 2-D bar/bench chart, specify the style and layout of the bars. If you want to add a 3-dimensional effect to the bars, set Use Depth to true and specify the depth and direction. If the chart uses a query resource, you can use a formula to control the Use Depth option.

- For a 3-D bar/bench chart, specify the bar width as a percentage of the unit width, and the layout of the bars.

- For a 2-D bar/bench chart, in the Size tab, specify the size of the bars which can either be dynamic or fixed.
    
- To use dynamic bar width, make sure Fixed Bar Width is cleared, specify the general bar width as a percentage of the unit width. For a clustered 2-D bar/bench chart that contains data on the series axis or has more than one value on the value axis, you can specify the gap between the bars as a percentage of the unit width, and in the Individual Bar Width box, specify how much the selected bars in the same data series is wider or narrower than a general bar in percentage. You can also select Size List to specify the size for bars in the same data series respectively in the Size List dialog box.

- To use fixed bar width, select Fixed Bar Width, specify the general bar width. For a clustered 2-D bar/bench chart that contains data on the series axis or has more than one value on the value axis, you can specify the gap between the bars within a group, and the outer gap between bars out of a group. In the Individual Bar Width box, specify the width and gap for the selected bars in the same data series, or select Size List to specify the size for bars in the same data series respectively in the Size List dialog box. You can use formulas to control the options. To customize the bar gap by percentage, clear Fixed Bar Gap and specify the percentages of the bar width and bar gap within a group.

- In the Fill tab, specify the fill type and the color pattern to fill the bars.
    

- When you select the Use Single Color fill type,
- Make your choice for the Self Settings option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the Pattern List property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the bars in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.  

- If the chart has no series field, specify the color and transparency  to fill the bars (to change the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color in the text box). If you want to apply different colors to the bars, select Vary Colors by Color List, then select Color List to specify the color pattern for each bar in the Color List dialog box.

- If the chart has series field, specify the color and transparency to fill the bars in the current data series, that is, the bars in the same data series as the one you have selected on to open the Format Bar dialog box. You can also select Color List to specify the color pattern for bars in each data series respectively in the Color List dialog box if the chart is a clustered bar chart.

- When you select the Use Single Color with Condition or Use Multiple Color with Condition fill type, specify the conditions and the color pattern for each condition respectively. See Adding Conditional Color Fills to Charts.

- In the Border tab, select Show Border if you want to display  border for the bars/benches, then specify the border properties.

- Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.

- In the Path box, specify the fill pattern of the border: Outline Path or Fill Path.

- In the Dash box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.

- In the Radius box, specify the radius size of the rounded corners of the border. When Use Depth is false and Show Border is selected, a rounded corner bar will be drawn.

- In the Data Label tab, specify properties of the static data labels in the bar chart.    

- For a 2-D bar/bench chart, in the Static Data Label box, select Show Static Data Label if you want to show static data labels for the bars, then specify the position of the data labels relative to the bars, the type of the data labels, whether to scale big and small numbers in the data labels, and whether to hide the data label when its value is 0. When you select the Position option of "inside center", "inside top", or "inside bottom", Designer enables the Auto Arrange drop-down list, from which you can specify whether to display the data labels inside the bars at the best position.

- In the Font and Effects box, specify the font format and special effects of the data labels, such as the font face, font size, font color, and the font style of the data labels.

- In the Hint tab, specify properties of the chart hint.  A hint displays the value a bar represents when you point to the bar in Designer view mode, in HTML output, or at runtime.    

- Clear Show Category and Series if you do not want to include the category and series values in the hint.

- Specify whether to scale big and small numbers in the hint.

- Select Customize Chart Value Name to use customized names for the fields on the value axis in the hint and select the ellipsis to customize the names as you want.

 You should not edit  the Show Tips property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint. 

- For a bar chart in a library component, you can specify web behaviors for it in the Behaviors tab,  to enable users to trigger different web actions when they perform specific operations such as Click and Mouse Over on the     bars at runtime.

- Select OK to accept the changes and close the dialog box.

- If the chart is a combo chart composed by bars and areas/lines, when you set the depth properties for the bars, Designer applies them to the areas/lines as well, and vice versa.

- If you set the style of the bars to "Cylinder", the style can take effect only when you specify Use Depth to "true" at the same time.

- For a 3-D bar chart, Designer disables the Show Static Data Label option in the Data Label tab of the Format Bar dialog box. However, you can still see the data labels by pointing to the bars when viewing the report in Designer view mode, in HTML output, or in Page Report Studio.
