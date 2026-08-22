---
title: "Unique Key dialog Dialog"
id: 1500009567822
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009567822-Unique-Key-dialog-Dialog
updated_at: 2021-07-24T05:54:44Z
---

# Unique Key dialog Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567802-UDF-Classes-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567842-Update-Procedures-Dialog)

# Unique Key Dialog

The Unique Key dialog appears when you select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell of the Unique Key property of of a refresh object in a library component in the Report Inspector, or select the Incremental Fetch button in the Display screen of the chart wizard. It helps you to specify a unique key to ensure there are no duplicated records in the library component or [real time chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009583761-Creating-a-Real-Time-Chart).  [See the dialog](javascript:%20void(null)).

![Unique Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893845527/unqkey.gif)

The following are details about options in the dialog:

**Resources**

Lists all the available data resources in the dataset used by the library component or real time chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected fields to the Unique Key box.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)

Removes the selected fields from the Unique Key box.

**Unique Key**

Lists the fields you have added as the unique key, which is used to guarantee there are no two records with the same unique key value in the library component or real time chart.

Take a real time chart for example. When a real time chart is specified with a unique key, each time when the chart automatically updates itself, the data that has the same unique key values as the previously loaded data records will be filtered and only data with different unique key values will be added to the chart. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, no more records of this product ID in USA will be added to the real time chart because they have the same unique key value. The most common usage is with a time field so when a time is part of the unique key the data in the chart will be updated each time new records are added to the database with more recent times.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567802-UDF-Classes-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567842-Update-Procedures-Dialog)
