---
title: "Insert Aggregation Dialog"
id: 1500010031422
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031422-Insert-Aggregation-Dialog
updated_at: 2021-07-24T10:38:40Z
---

# Insert Aggregation Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066861-Information-Bus-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066881-Insert-Detail-Column-Dialog)

# Insert Aggregation Dialog

The Insert Aggregation dialog helps you to [add an aggregation in a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010063741-Modifying-Crosstabs#InsertAgg) based on the selected field. It appears when you drag a field that can be used as aggregate field from the Data panel to the aggregation area in a crosstab.

![Insert Aggregation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909185559/instaggrgt.gif)

**Aggregate Function**

Specifies the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) for the aggregation. When DistinctSum is selected, the following option is available and should be set:

* **Distinct On**  
   Specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.

If the selected field has been predefined with an aggregate function, the option is Aggregation. The name of the field is displayed in the text box and cannot be edited.

**Label**

Specifies the label text of the new aggregation in the crosstab. You can leave it blank.

**Auto Map Field Name**

The option is available when inserting an aggregation into a crosstab that is created using a business view. It specifies whether to automatically map the label text to the dynamic display name of the field used for the aggregation at runtime.

**OK**

Inserts the aggregate field and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066861-Information-Bus-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066881-Insert-Detail-Column-Dialog)
