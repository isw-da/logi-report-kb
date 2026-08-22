---
title: "Formatting Area Chart"
id: 28897774215437
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897774215437-Formatting-Area-Chart
updated_at: 2024-09-30T09:08:20Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Formatting Area Chart

This topic describes how you can format the area of an area chart.

- Right-click any area in the area chart and select Format 2D Area or Format 3D Area on the shortcut menu, or double-click any area in the chart. Designer displays the Format Area dialog box. 

- In the General tab, specify general properties of the areas.
- Select the layout of the areas in the Layout box.

- Select Ignore Null Value if you want to draw the areas  from the previous data values to the next data values directly when null data values appear to avoid breaks on the areas.
    

- For a 2-D area chart, if you want to add a 3-dimensional effect to the areas, set Use Depth to true and the specify the depth and direction. If the chart uses a query resource, you can use a formula to control the Use Depth option. You can also select to show the lines that represent the data categories by selecting High-Low Lines.

- In the Fill tab, specify the fill type and the color pattern to fill the areas.

- When you select the Use Single Color fill type,
- Make your choice for the Self Settings option. When Self Settings is cleared (the default behavior), Designer synchronizes the color pattern that you specify here with the Pattern List property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart. When you select Self Settings, it indicates that the color pattern is private to the current data markers themselves (the areas in this case), which Designer remembers and applies to data markers of the new type automatically if you change the type of the chart later.  

- Specify the color and transparency  to fill the current area, that is, the area you have right-clicked on to open the Format Area dialog box (to change the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color in the text box).

- You can also select Color List to specify the color pattern for each area in the area chart using the Color List dialog box.

- For an Area 2-D or Area 3-D chart, you can select the Use Multiple Colors with Condition fill type to divide each area into several parts based on different value ranges along the direction of the value axis and apply separate color patterns to these different value ranges. See Adding Conditional Color Fills to Charts.

- In the Border tab, select Show Border if you want to display  border for the areas, then specify the border properties.   

- Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.

- In the Path box, specify the fill pattern of the border: Outline Path or Fill Path.

- In the Dash box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.

- In the Data Label tab, specify properties of the static data labels in the area chart.    

- For a 2-D area chart, in the Static Data Label box, select Show Static Data Label if you want to show static data labels for the area nodes, then specify the position of the data labels relative to the area nodes, the type of the data labels, whether to scale big and small numbers in the data labels, and whether to hide the data label when its value is 0.

- In the Font and Effects box, specify the font format and special effects of the data labels, such as the font face, font size, font color, and the font style of the data labels.

- In the Hint tab, specify properties of the chart hint. A hint displays the value an area represents when you point to the area in Designer view mode, in HTML output, or at runtime. 

- Clear Show Category and Series if you do not want to include the category and series values in the hint.

- Specify whether to scale big and small numbers in the hint.

- Select Customize Chart Value Name to use customized names for the fields on the value axis in the hint and select the ellipsis to customize the names as you want.

 You should not edit  the Show Tips property of the Chart Paper object in the Report Inspector which is "true" by default, if you want to display the hint. 

- For an area chart in a library component, you can specify web behaviors for it in the Behaviors tab,  to enable users to trigger different web actions when they perform specific operations such as Click and Mouse Over on the     areas at runtime.

- Select OK to accept the changes and close the dialog box.

- If the chart is a combo chart composed by areas and bars/lines, when you set the depth properties for the areas, Designer applies them to the bars/lines as well, and vice versa.

- For a 3-D area chart, Designer disables the Show Static Data Label option in the Data Label tab in the Format Area dialog box. However, you can still see the data labels by pointing to the areas when viewing the report in Designer view mode, in HTML output, or in Page Report Studio.

Previous Topic  Next Topic
