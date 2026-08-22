---
title: "Format Donut Dialog Box Properties"
id: 45203867571341
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203867571341-Format-Donut-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:23Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Format Donut Dialog Box Properties 

You can use the Format Donut dialog box to format the donuts of a donut chart. This topic describes the properties in the dialog box.

Static Data Label

Specify the properties of the static data labels on the donuts.

- 
Show Static Data Label
    Select true to show the static data labels on the donuts. Only when it is true can the following static data label properties work.

- 
Data Label Type
    Select the display type for the data values in the static data labels.
- 
category name
        Select to display the category name for each donut section.

- 
category name, percent 
        Select to display the category name and percentage for each donut section.

- 
category name, value 
        Select to display the category name and value for each donut section.

- 
category name, value, percent 
        Select to display the category name, value, and percentage for each donut section.

- 
percent
        Select to display the percentage of each donut section to the total.

- 
value
        Select to display the value for each donut section.

- 
value and percent
 Select to display the value and the percentage for each donut section.

- 
Position
    Specify the position of the static data labels on the donuts.
    
- 
Autofit
        Select to display the static data labels automatically.

- 
Sticker
        Select to display the static data labels beside the donut sections.

- 
Slim Leg
 Select to display the static data labels beside the donut sections and point to them by thin lines.
        - 
Line Color
            Specify the color of the thin lines that point to the static data labels.

- 
Best Fit
 Select to display the static data labels at the best position automatically.

- 
On Slices
        Select to display the static data labels on the donut sections (slices).

- 
Auto Scale in Number
When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart platform.

- 
Show Truncated Label
Select to truncate labels that would go beyond the boundaries on a donut chart paper instead of them being hidden altogether - the default behavior. Report displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name, when you enable this property. The truncated labels are also affected if you select the Position property of Best Fit (as seen above); where the label is cut off from the left or the right depending on the position of the label.

- 
Show Donut Name
    Select true to show the names of the donuts.

- 
Donut Hole
    Specify the percentage the hole's thickness will take from the total radius of the pie circle.

KPI Value

Specify the properties for the KPI values of the donuts.

- 
Show KPI Value
    Select to show KPI value for each donut and enable the two properties:
    
- 
KPI Value
        Specify the KPI value to display on each donut. By default, Server uses the total value of each donut as the KPI value. If you want to customize the value, clear Auto. Then, type a value in the text box, or select the formula button  and select a formula or summary from the list to use its value as the KPI value.

- 
Position
        Specify the position of the KPI value at the center, top, bottom of each donut, or select customized which enables setting the X and Y properties to change the position.

Graph Border 

Specify the properties for the border of the donuts.

- 
Show Border

Select to show the border and enable the border properties.
  

- 
Line Style

Select the line style of the border.

- 
Color

Specify the color of the border.

- 
Thickness

Specify the thickness of the border.

- 
Transparency

Specify the transparency for the border color.

- 
Radius

Specify the radius size of the rounded corners of the border.

Hint

Specify the data marker hint properties.

- 
Show Category and Series

Select to include the category and series values in the data marker hint.

- 
Auto Scale in Number
When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart platform.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
