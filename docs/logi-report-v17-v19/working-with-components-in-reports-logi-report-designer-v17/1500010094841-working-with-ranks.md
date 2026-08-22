---
title: "Working with Ranks"
id: 1500010094841
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094841-Working-with-Ranks
updated_at: 2021-07-23T19:14:48Z
---

# Working with Ranks

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094341-Working-with-Barcodes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support)

# Working with Ranks

A rank is a component that is based on the value of another component - a DBField, formula, summary, or parameter. You can map one or more values for these fields to an image known as the rank. The Rank component enables you to convert raw data values to easy-to-understand graphical cues or to hide sensitive details but still convey the general data value to the report users. This topic describes how you can insert ranks in a report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You can use ranks in page reports that use query resources only.

**To insert a rank into a query-based page report:**

1. Do one of the following:
   * From the **Components** panel, drag the **Rank** icon ![Rank icon](https://devnet.logianalytics.com/hc/article_attachments/4404848501015/icon_rank.gif) in the Visual category to the report.
   * Select **Insert** > **Rank**.
   * Select **Home** > **Insert** > **Rank**.

   Designer displays the [Rank Expert dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098361-Rank-Expert-Dialog-Box).

   ![Rank dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856900375/rank.gif)
2. The **Rank Resources** drop-down list displays the dataset available for the current insertion, and the list box below shows its fields, including DBFields, formulas, summaries, and parameters.

   Select the field you want to insert as rank from the list box. You can also create formulas, summaries, and parameters here.
3. Select the **Browse** button to select an image file to be the default image (Designer applies this image file if a value does not fit any of the specified value ranges).
4. Type the alternate text of the default image in the **Default Image Alternate Text** box, which shows when Designer cannot load the image or when it is not available.
5. In the **Value Range** box, select in the cell of the corresponding column to specify the minimum value, maximum value, image, and alternate text of the first range.
6. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add and define more ranges.

   To delete an unwanted range, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the ranges, select a range and select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button.

   Designer displays a value, which is larger than or equal to the minimum value of a range and less than the maximum value, as the image, or the alternate text if the image cannot be loaded or is not available. For a value belonging to two or more overlapping ranges, Designer applies the highest range in the Value Range box.

   Suppose that you want to define product quality rank based on customer grading, and you want to define three levels:

   * 50-70, Poor
   * 71-90, Good
   * 91-100, Excellent

   You can define as follows in the Value Range box:

   1. In the first range line, set the minimum and maximum values as **50** and **70** respectively in the cells of the Minimum and Maximum columns. Go to the Image cell, and then select **<Browse...>** to select an image to represent the rank. In the Alternate Text cell, type **Poor**.
   2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add another line. Set the minimum and maximum values as **71** and **90**, select another image to represent the rank and type **Good** in the Alternate Text cell.
   3. Add one more line, and set the values, image, and name for **Excellent** in the same way.
7. Select **Insert** in the dialog box, then select the mouse button in the location where you want to place the rank.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* Where you can insert a rank in a report depends on what you have selected as its source.
* You can also create a rank by first inserting a label, DBField, formula, summary, parameter, or special field, and then [changing its display type as rank](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports#Rank).

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the rank component example, open `<install_root>\Demo\Reports\SampleComponents\Rank.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094341-Working-with-Barcodes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support)
