---
title: "Conditional Formatting"
id: 45190391802637
section: "Report Feature Guide"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190391802637-Conditional-Formatting
updated_at: 2026-04-30T15:11:41Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Conditional Formatting

 Conditional formatting is very useful when you want to highlight significant data values in a report.

## Conditional Formatting in Tables/Crosstabs/Banded Objects

You can apply different conditional formats  to the data fields in a table, crosstab, or banded object, then when a specified condition is fulfilled, Report  automatically applies the format bound with the condition to the field values. You can add conditional formatting at both report design time and Server runtime.

## Conditional Formatting in Charts

You can add different color patterns to the data markers of a chart based on different value ranges. Currently, Report supports the feature  on Bar, Bench, Pie, Donut, Area (Area 2-D and Area 3-D types), 2-D Line, and Heat Map charts at report design time only.

There are two types of conditional formatting for charts: Single Color with Condition and Multiple Colors with Condition. With a single color, you can make the data marker that meets the specified condition apply the color pattern bound with the condition. By using multiple colors, you can divide each data marker into different parts based on different value ranges along the direction of the value axis, and then specify different conditional colors to different value ranges.

The following example uses Single Color with Condition.
