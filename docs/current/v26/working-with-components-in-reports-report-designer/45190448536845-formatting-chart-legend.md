---
title: "Formatting Chart Legend"
id: 45190448536845
section: "Working with Components in Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190448536845-Formatting-Chart-Legend
updated_at: 2026-04-30T15:12:09Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Formatting Chart Legend

This topic describes how you can format the legend of chart.

- Right-click any chart element and select Format Legend from the shortcut menu, or double-click the legend of the chart. Designer displays the Format Legend dialog box.

- In the Fill tab, specify the color and transparency to fill the legend (to change the color, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value of a color in the text box).

- In the Border tab, specify properties for the border of the legend.
    

- From the Border Type drop-down list, select how you want to display the border.

- Specify the color, transparency, line style, thickness, ending style, and line joint mode of the border.

- In the Path box, specify the fill pattern of the border: Outline Path or Fill Path.

- In the Dash box, select to automatically adjust the dash size or use fixed dash size if you select a dash line style for the border.

- In the Radius box, specify the radius size of the rounded corners of the border. When Use Depth is false and Show Border is selected, a rounded corner bar will be drawn.

- When you select the Line Joint option as "joint round", you can set the radius for the border joint in the Radius text box.

- In the Placement tab, specify how you want to place the legend in the chart.
    

- In the Position box, specify whether to place the legend on the left, right, top, or bottom of the chart, and then select the alignment accordingly in the Alignment box. If you select Customized, you can manually drag the legend on the chart in the design area to specify its location. Usually, it is easier to select the legend and use the grab handles to resize and move the legend as needed anywhere in the chart.

- In the Legend Label Gap box, specify the vertical and horizontal margin between the legend entries and legend border, and the vertical and horizontal spacing between the legend entry labels.

- Select Reverse Legend if you want to arrange the legend entries  in a reverse order.

- Select Show Scrollbar to show the legend scroll bar to fully view the legend content when the content does not fit into the legend.

- Select Truncate to truncate the legend entry label text when the text overflows the label.

- In the Font tab, specify the font properties of the legend entry labels, including the font face, size, color, transparency, rotation angle, and shearing angle. You can also apply some special effects to the entry labels, such as italicizing the labels and adding a horizontal line under the labels.
    

- In the Orientation tab,  specify the rotation angle for the legend entry labels. You can either drag the Text hand in the Orientation box or type a value in the Angle text box to set the angle.
    

- In the Format tab, specify the data format of the legend entry labels.

- Select a category from the Category box, then select a format from the Format box and select Add to add it to the Stack box. Select here for more information about each format.

- When the formats Designer provides in the Format box cannot meet your requirement, you can define the format in the Properties text box and add it as the format of the selected category. You can add more than one format, but for each category, only one format is allowed.

- If you do not need a format anymore, select it in the Stack box and select Remove to clear it.

- Set the Auto Scale in Number option to specify whether to automatically scale the big and small Number values.

 The data format you specify for the legend entry labels takes effect only when you set the Label Format Source property of the legend to "Legend Label Format" in the Report Inspector.

- In the Mark tab, specify properties of the legend entry marks.
    

- By default, Designer selects Customize, meaning, you can customize the style of the legend entry marks by yourself. To specify the style for a mark item, select the item in the Mark Items box and then select the style from the drop-down list in the box. You can select Add to add more items to the Mark Items box and define their style. To delete a mark item, select it and select Remove; to adjust the order of the items, select a mark item and select Move Up or Move Down. The entry marks repeat within the mark items you define. If you define more mark items than the actual entry marks, Designer ignores the redundant mark items.

- In the Icon box, specify  the width and height of the legend entry marks, the horizontal and vertical alignment of the marks relative to the entry labels, and the gap between each entry mark and entry label.

- In the Border box, set the color, style, thickness, and transparency of the mark border. If the chart uses a query resource, you can use a formula to control the border color and transparency.

- For a line chart, you can also select Use Node as Mark or Use Line and Node as Mark to apply the style and color of the line nodes or lines and line nodes automatically to the legend entry marks. When you select either of these two options, Designer disables the Mark Items and Border boxes, but you can still specify the mark properties in the Icon box.

- Designer enables options in the Label tab, when the legend entry labels show values of the field on the category or series axis of the chart. You can customize the text of the entry labels as follows: clear Auto, then from the Label Text drop-down list, select a field the values of which you prefer to display as the entry labels, or use a formula to control the label text; you can also select  and type the text you want to display in the labels in the text box.    

- For a chart in a library component, you can specify web behaviors for it in the Behaviors tab,  to enable users to trigger different web actions when they perform specific operations such as Click and Mouse Over on the     legend at runtime. 

- Select OK to apply the settings and close the dialog box.
