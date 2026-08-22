---
title: "Managing Data of a Banded Object"
id: 1500009562862
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562862-Managing-Data-of-a-Banded-Object
updated_at: 2021-07-24T05:56:11Z
---

# Managing Data of a Banded Object

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583341-Modifying-a-Banded-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562882-Managing-Banded-Panels)

# Managing Data of a Banded Object

With Logi JReport Designer, you can group, sort, and filter data in a banded object easily so as to organize data in the banded object in a more readable way. The operations for setting group, sort and filter conditions for a banded object are similar to those for a table, so you can refer to the following topics on table for details:

* [Grouping the data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data)
* [Sorting the data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data)
* [Filtering the data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data)

**Note:** When a banded object is created on an HDS, the conditions you define in the Edit Filter dialog will not be applied when the banded object runs due to the [specialty of HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009584761-Developing-Reports-from-HDS). Therefore, if you want to filter the data displayed in such kind of banded objects, you need to make use of the [dataset filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets#Filter).

In addition, you can insert a web control, Expand/Collapse Group, to the group header panel of a banded object so that end users in Page Report Studio can use the web control to expand/collapse records in the groups of the banded object. Note that, this feature works only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode).

**To insert to a Expand/Collapse Group web control in a banded object:**

1. Make sure to uncheck the **Page Layout** command on the View menu.
2. Select the group header panel, then select **Insert** > **Web Control** > **Expand/Collapse Group**.
3. Select on the group header panel, and the web control will be inserted there.

After publishing the report to Logi JReport Server and run it in Page Report Studio, end users will be able to use the web control which appears like a plus or minus sign to expand or collapse a group (that is, to show or hide the details of that group). Furthermore, you can use two properties of a group panel to set the expanding/collapsing state of all groups in the corresponding group level. That is, the Expand Detail Data property controls whether or not to expand the groups, and the Shrink Footer property controls whether or not to hide the group footer panel when collapsing the group.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583341-Modifying-a-Banded-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562882-Managing-Banded-Panels)
