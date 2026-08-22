---
title: "Creating a Summary"
id: 1500009589741
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589741-Creating-a-Summary
updated_at: 2021-07-24T05:54:35Z
---

# Creating a Summary

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589761-Summary-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views)

# Creating a Summary

To create a summary in a catalog, follow the steps below:

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog).
2. In the Catalog Manager, expand the data source in which to create the summary, then:
   * Select the **Summaries** node or any existing summary in the data source and select **New Summary**  on the Catalog Manager toolbar.
   * Right-click the **Summaries** node in the data source and select **New Summary**  on the shortcut menu.

   The [New Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009566842-New-Summary-Dialog) dialog appears.

   ![New Summary dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893837079/nwsum.gif)
3. Select **<Create>** in the Summaries drop-down list.
4. Select a function from the Aggregate Function drop-down list for your field to be summed by.
5. Select a field for the summary to compute from the Resource box, then select ![Add Sum On button](https://devnet.logianalytics.com/hc/article_attachments/4404889307799/btn_sumon.gif) next to Summary On.
6. If required, specify to which group the summary will be applied.
   * If Static Summary is checked, select the field from the Resource box and then select ![Add Group By button](https://devnet.logianalytics.com/hc/article_attachments/4404889307799/btn_sumon.gif) next to Group By. And if the field you select is of Numeric/String/Date/Time type, you can further specify to which level the data will be grouped by by selecting a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field) from the Special Function drop-down list. If Customize is selected, you can [set the function by yourself](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field#Customized)  in the Customized Function dialog.

   Static summaries can only be used in a group with exactly the same group by field. It will be invalid anywhere else. For example, if your data component is grouped by 3 groups, you would need 4 static summaries, one for each group plus one for the final total.

   * If Dynamic Summary is checked, first select **Up** or **Down** from the Group By drop-down list, then in the combo box, select a value or input an integer, which should be between 0 to 127, to specify the group on which the summary will take effect.

     Normally you want to display the value of the group where you use the summary so leave the value 0. For example, if you select Up or Down and input 0 in the combo box and insert this summary into any group, the summary will take effect on this group; if you select Up and input 1 and insert this summary to a group, the summary will take effect on the group higher than the group where the summary is inserted, and if you specify Down and 1, it will take effect on the lower group.

     The advantage of dynamic summaries is you can create one summary and use it on every group level. Using the example above with 3 groups and a final total, you still only need one dynamic summary instead of 4 static summaries since the dynamic summary can be used for each group and for the final report. Using dynamic summaries will enable you to keep a much cleaner catalog without hundreds of static summaries that can only be used in one report at one level.
7. Select the **OK** button.
8. In the Enter Summary Name dialog, provide a name for the summary and select **OK**. The summary is now created in the catalog.

**Notes:**

* If the dynamic summary is to be used in a chart, when defining the summary, you must choose Down from the Group By drop-down list; if it is to be inserted to other data components, the summary must be defined on Up level.
* When you insert a static summary into a report and there is no corresponding group level to match settings of the static summary, an error message will be generated.
* If you want to insert a summary defined with a special function into a table or banded object, there must be a group with the same special function in the table or banded object.
* All summaries created automatically by the banded report wizard and table report wizard are static summaries used only for a single report on a single group. When you use the wizard to create a lot of reports in your catalog it will become very messy with many duplicate summaries. It is better to create dynamic summaries and add them to your reports after you generate them with the wizards.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589761-Summary-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views)
