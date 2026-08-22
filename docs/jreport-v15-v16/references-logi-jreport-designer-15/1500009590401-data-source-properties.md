---
title: "Data Source Properties"
id: 1500009590401
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590401-Data-Source-Properties
updated_at: 2021-07-24T05:54:27Z
---

# Data Source Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568722-Group-Object-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568742-Data-Source-Security-Properties)

# Data Source Properties

The properties of a data source are as follows:

| Property Name | Description |
| --- | --- |
| [Display Rounding Mode](#Round) | Specifies the rounding mode for displaying numeric data values in reports and library components that are created on this data source. Choose an option from the drop-down list.  * **Up** -   Rounding mode to round away from zero. Always increments the digit prior to a non-zero discarded fraction. * **Down** -   Rounding mode to round towards zero. Never increments the digit prior to a discarded fraction (that is, truncates). * **Ceiling** -   Rounding mode to round towards positive infinity. If the result is positive, behaves as for Up; if negative, behaves as for Down. * **Floor** -   Rounding mode to round towards negative infinity. If the result is positive, behaves as for Down; if negative, behaves as for Up. * **Half up** -   Rounding mode to round towards "nearest neighbor" unless both neighbors are equidistant, in which case round up. Behaves as for Up if the discarded fraction is >= 0.5; otherwise, behaves as for Down. * **Half down** -   Rounding mode to round towards "nearest neighbor" unless both neighbors are equidistant, in which case round down. Behaves as for Up if the discarded fraction is > 0.5; otherwise, behaves as for Down. * **Half even** -   Rounding mode to round towards the "nearest neighbor" unless both neighbors are equidistant, in which case, round towards the even neighbor. Behaves as for Half up if the digit to the left of the discarded fraction is odd; behaves as for Half down if it's even.   For more information about the rounding mode, refer to <http://docs.oracle.com/javase/7/docs/api/java/math/RoundingMode.html>.  Data Type: Enumeration |
| Is Default | Specifies whether the data source is the default data source for the current catalog. One catalog must have one and only one default data source. Data type: Boolean |
| Name | Specifies the name of the data source. Data type: String |
| Pre-join | Specifies whether or not to apply the pre-join information defined on the data source when building a query or defining join relationships in business views in the same data source. Data type: Boolean |

## Display Rounding Mode

| Input number | Input rounded to one digit with Up rounding | Input rounded to one digit with Down rounding | Input rounded to one digit with Ceiling rounding | Input rounded to one digit with Floor rounding | Input rounded to one digit with Half up rounding | Input rounded to one digit with Half down rounding | Input rounded to one digit with Half even rounding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5.5 | 6 | 5 | 6 | 5 | 6 | 5 | 6 |
| 2.5 | 3 | 2 | 3 | 2 | 3 | 2 | 2 |
| 1.6 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| 1.1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| 1.0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| -1.0 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
| -1.1 | -2 | -1 | -1 | -2 | -1 | -1 | -1 |
| -1.6 | -2 | -1 | -1 | -2 | -2 | -2 | -2 |
| -2.5 | -3 | -2 | -2 | -3 | -3 | -2 | -2 |
| -5.5 | -6 | -5 | -5 | -6 | -6 | -5 | -6 |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568722-Group-Object-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568742-Data-Source-Security-Properties)
