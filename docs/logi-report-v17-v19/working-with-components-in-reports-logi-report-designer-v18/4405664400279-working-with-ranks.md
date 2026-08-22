---
title: "Working with Ranks"
id: 4405664400279
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664400279-Working-with-Ranks
updated_at: 2022-01-27T20:34:33Z
---

# Working with Ranks

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661349911-Working-with-Barcodes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661787159-Applying-National-Language-Support)

# Working with Ranks

A rank is a component that is based on the value of another component - a DBField, formula, summary, or parameter. You can map one or more values for these fields to an image known as the rank. The Rank component enables you to convert raw data values to easy-to-understand graphical cues or to hide sensitive details but still convey the general data value users. This topic describes how you can insert ranks in a report.

You can also create a rank component by first inserting a label, DBField, formula, summary, parameter, or special field, and then [changing its display type as rank](https://devnet.logianalytics.com/hc/en-us/articles/4405661930647-Changing-the-Display-Type-of-Objects-in-Reports#Rank).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) You can use ranks in page reports that use query resources only, and where you can insert a rank in a page report depends on what you have selected as its source (see [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship) for more information).

**To insert a rank into a query-based page report**

1. Position the mouse pointer at the destination where you want to insert the rank.
2. Do one of the following:
   * From the **Components** panel, drag the **Rank** icon ![Rank icon](https://devnet.logianalytics.com/hc/article_attachments/4420542104727/icon_rank.gif) in the **Visual** category to the report.
   * Navigate to **Insert** > **Rank**.
   * Navigate to **Home** > **Insert** > **Rank**.

   Designer displays the [Rank Expert dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664556055-Rank-Expert-Dialog-Box).

   ![Rank dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556131991/rank.gif)
3. The **Rank Resources** drop-down list displays the dataset available for the current insertion, and the list box below shows its fields, including DBFields, formulas, summaries, and parameters.

   Select the field you want to insert as rank from the list box. You can also create formulas, summaries, and parameters here.
4. Select **Browse** to select an image file to be the default image. A value that does not fit any of the specified value ranges applies this image file by default.
5. In the **Default Image Alternate Text** text box, type a string to serve as the content when the default image cannot display.
6. In the **Value Range** box, select in the cell of the corresponding column to specify the minimum value, maximum value, image, and alternate text of the first range.
7. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add and define more ranges. To delete a range, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to adjust the order of the ranges.

   Designer displays a value, which is larger than or equal to the minimum value of a range and less than the maximum value, as the image, or the alternate text if the image cannot be loaded or is not available. For a value belonging to two or more overlapping ranges, Designer applies the highest range in the Value Range box.

   Suppose that you want to define product quality rank based on customer grading, and you want to define three levels:

   * 50-70, Poor
   * 71-90, Good
   * 91-100, Excellent

   You can specify the ranges as follows in the Value Range box:

   1. In the first range line, set the minimum and maximum values as **50** and **70** respectively in the cells of the Minimum and Maximum columns. Go to the Image cell, and then select **<Browse...>** to select an image to represent the rank. In the **Alternate Text** cell, type **Poor**.
   2. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) to add another range line. Set the minimum and maximum values to **71** and **90**, select another image to represent the rank and type **Good** in the Alternate Text cell.
   3. Add one more range line, and set the values, image, and name for **Excellent** in the same way.
8. Select **Insert** in the dialog box.
9. Select in the location where you want to place the rank.

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the rank component example, open `<install_root>\Demo\Reports\SampleComponents\Rank.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661349911-Working-with-Barcodes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661787159-Applying-National-Language-Support)
