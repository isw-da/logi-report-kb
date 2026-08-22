---
title: "Modifying a Crosstab"
id: 1500009583901
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583901-Modifying-a-Crosstab
updated_at: 2021-07-24T05:56:02Z
---

# Modifying a Crosstab

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583881-Inserting-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout)

# Modifying a Crosstab

Once a crosstab has been created, you can further modify it by accessing its shortcut menu wizard which is composed by a set of screens that are similar to the wizard screens used to create the crosstab. For example, you can change the data used by the crosstab, reset the layout and style of the crosstab.

**To modify a crosstab after it has been created:**

1. Right-click the crosstab and select **Crosstab Wizard** from the shortcut menu to display the Crosstab Wizard.
2. In the Data screen, specify a new data source for the crosstab if required.
3. In the Display screen, specify the fields you want to display in the crosstab.
4. In the Layout screen, specify the layout of the crosstab.
5. In the Style screen, set a style for the crosstab.
6. Upon finishing, select **Finish** to accept the changes.

**See also:**

* [Inserting a Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009583881-Inserting-a-Crosstab) for details about how to define a crosstab.
* Crosstab Wizard for [query based](https://devnet.logianalytics.com/hc/en-us/articles/1500009585941-Crosstab-Wizard-Dialog-Query-Based-) or [business view based](https://devnet.logianalytics.com/hc/en-us/articles/1500009564862-Crosstab-Wizard-Dialog-Business-View-Based-) for detailed explanation about options in the wizard.

After finishing the modification, you can also apply some filter conditions to narrow down the records displayed in the crosstab the same as you do for a table (for details, see [Filtering the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data)). However, if the crosstab is created on an HDS, the conditions you define in the Edit Filter dialog will not be applied when the crosstab runs due to the [specialty of HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009584761-Developing-Reports-from-HDS). Therefore, if you want to filter the data displayed in such kind of crosstabs, you need to make use of the [dataset filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets#Filter).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583881-Inserting-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout)
