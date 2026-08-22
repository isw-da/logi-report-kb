---
title: "Conditional Formatting"
id: 5735519685015
section: "Logi Report Feature Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735519685015-Conditional-Formatting
updated_at: 2022-11-02T04:11:47Z
---

# Conditional Formatting

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735506098327-Compound-Crosstabs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735497901207-CSS-Styles)

# Conditional Formatting

Conditional formatting is very useful when you want to highlight significant data values in a report.

## Conditional Formatting in Tables/Crosstabs/Banded Objects

You can apply different conditional formats to the data fields in a table, crosstab, or banded object, then when a specified condition is fulfilled, Logi Report automatically applies the format bound with the condition to the field values. You can add conditional formatting at both report design time and Server runtime.

![Crosstab Conditional Formatting](https://devnet.logianalytics.com/hc/article_attachments/9898538005655/cndtnfmt.gif)

## Conditional Formatting in Charts

You can add different color patterns to the data markers of a chart based on different value ranges. Currently, Logi Report supports the feature on Bar, Bench, Pie, Donut, Area (Area 2-D and Area 3-D types), 2-D Line, and Heat Map charts at report design time only.

There are two types of conditional formatting for charts: Single Color with Condition and Multiple Colors with Condition. With a single color, you can make the data marker that meets the specified condition apply the color pattern bound with the condition. By using multiple colors, you can divide each data marker into different parts based on different value ranges along the direction of the value axis, and then specify different conditional colors to different value ranges.

The following example uses Single Color with Condition.

![Chart Conditional Formatting](https://devnet.logianalytics.com/hc/article_attachments/9898538021527/cndtnfmt_chart.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735506098327-Compound-Crosstabs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735497901207-CSS-Styles)
