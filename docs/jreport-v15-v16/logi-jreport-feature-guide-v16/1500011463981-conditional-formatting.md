---
title: "Conditional Formatting"
id: 1500011463981
section: "Logi JReport Feature Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463981-Conditional-Formatting
updated_at: 2021-07-24T10:39:49Z
---

# Conditional Formatting

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011464001-Compound-Crosstabs) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463961-CSS-Styles)

# Conditional Formatting

Conditional formatting is very useful when you want to highlight significant data values in a report.

## Conditional Formatting in Tables/Crosstabs/Banded Objects

Different conditional formats can be added to the data fields in a table, crosstab or banded object, then when a specified condition is fulfilled, the format bound with the condition will be applied to the field values automatically.

Conditional formatting in tables, crosstabs and banded objects are supported both at report design time and server runtime.

![Crosstab Conditional Formatting](https://devnet.logianalytics.com/hc/article_attachments/4404901360663/cndtnfmt.gif)

## Conditional Formatting in Charts

Different color patterns can be applied to the data markers of a chart based on different value ranges. Currently the feature is supported on bar, bench, pie, donut, area (Area 2-D and Area 3-D types), 2-D line and heat map charts at report design time only.

There are two types of conditional formatting for charts: Single Color with Condition and Multiple Colors with Condition. With a single color, you can make the data marker that meets the specified condition apply the color pattern bound with the condition. By using multiple colors, you can divide each data marker into different parts based on different value ranges along the direction of the value axis, and then specify different conditional colors to different value ranges.

The following example uses Single Color with Condition.

![Chart Conditional Formatting](https://devnet.logianalytics.com/hc/article_attachments/4404901360919/cndtnfmt_chart.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011464001-Compound-Crosstabs) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463961-CSS-Styles)
