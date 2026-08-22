---
title: "Previewing a Query"
id: 1500009592521
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592521-Previewing-a-Query
updated_at: 2021-07-24T05:53:53Z
---

# Previewing a Query

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570702-Adding-Formula-Fields-to-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570802-Creating-Union-Queries)

# Previewing a Query

To preview a query, follow the steps below:

1. In the Query Editor, select **Preview**. The Preview Option dialog appears.

   ![Preview Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889296663/prvwoptn.gif)
2. In the Max Records text box, specify the maximum number of records to be displayed.
3. In the Records per Page text box, specify the number of records displayed on one page.
4. In the Range box, specify the range of the records for previewing.

   * **Max Records**  
      If checked, the Max Records option will take effect.
   * **All**  
      If checked, all the records will be displayed when you preview the query, and the Max Records option will be disabled.
5. Select **OK**. If the query has parameters, you will be prompted to [enter the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009586681-Enter-Parameter-Values-Dialog).

   The Preview dialog appears showing the records. In the dialog, JTable is used to display the result set. When you open the dialog, the result set is cached, and when you close the dialog, the result set is released.

   ![Preview dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889296919/qury_prvw.gif)
6. Select ![First Page button](https://devnet.logianalytics.com/hc/article_attachments/4404893801623/btn_fstpg.gif), ![Previous Page button](https://devnet.logianalytics.com/hc/article_attachments/4404893801879/btn_prvspg.gif), ![Next Page button](https://devnet.logianalytics.com/hc/article_attachments/4404889284503/btn_nxtpg.gif) and ![Last Page button](https://devnet.logianalytics.com/hc/article_attachments/4404889284759/btn_lastpg.gif) to browse the records. If the type of the result set is TYPE\_FORWARD\_ONLY, the last page button will be disabled until you have browsed the last page.
7. To refetch the result set, select **Refetch**. Select **Stop** to stop Logi JReport from refetching the result set.
8. To print the result set, select **Print** . If you want to preview the result set before printing, select **Print Preview**.
9. If you want to set up the page parameters, select **Page Setup**.
10. Selectthe close button of the dialog to close the Preview dialog.

**Notes:**

* The values shown in the Preview Option dialog when it appears are the default values. These values can be specified in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog#Query) category in the Options dialog.
* If there are a large number of records in a query, it may take a long time when previewing the query and possibly run out of memory. In this case, it is best to use a parameter value which returns a small number of records.
* When you preview a query, values from [computed columns](https://devnet.logianalytics.com/hc/en-us/articles/1500009570682-Creating-Computed-Columns-in-a-Query) are shown in the Preview dialog, while results of [formula fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009570702-Adding-Formula-Fields-to-a-Query) are not shown.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570702-Adding-Formula-Fields-to-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570802-Creating-Union-Queries)
