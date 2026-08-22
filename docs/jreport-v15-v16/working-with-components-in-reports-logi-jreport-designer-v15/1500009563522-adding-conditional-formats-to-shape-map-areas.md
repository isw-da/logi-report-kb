---
title: "Adding Conditional Formats to Shape Map Areas"
id: 1500009563522
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563522-Adding-Conditional-Formats-to-Shape-Map-Areas
updated_at: 2021-07-24T05:55:59Z
---

# Adding Conditional Formats to Shape Map Areas

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584121-Binding-Data-to-a-Shape-Map)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584161-Binding-Links-to-Shape-Map-Areas)

# Adding Conditional Formats to Shape Map Areas

When the shape map areas are bound with data, you can add conditional formats to them, then when a specified condition is fulfilled, the format bound with the condition will be applied to the shape map areas automatically. This is very useful to highlight values that might need to be acted on by the end user.

**To add conditional formats to the map areas:**

1. In the Shape Map Editor, select the **Conditional Formatting** button ![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/4404889280535/btn_cndtnlfmt.gif) on the toolbar, or select **Menu > Format** > **Conditional Formatting**. The [Shape Map Area Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009587801-Shape-Map-Area-Condition-Formatting-Dialog) dialog appears.

   ![Shape Map Area Conditional Formatting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893867159/mpcndtnlfmt.gif)
2. Select the **Add** button below the Map Area Condition box. The [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#edit) dialog appears.

   ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893926679/edtcndtn.gif)
3. Select the **Add Condition** button to add a condition line.
4. From the field drop-down list, select the field on which the condition will be based.
5. Choose the operator with which to compose the condition expression from the operator drop-down list.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) next to the value box to specify the value of how to build the condition. You can also type in the value manually.
7. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
8. Select **OK** to save the condition.

   The newly added condition is then displayed in the Map Area Condition box in the Map Area Conditional Formatting dialog.
9. In the Format box of the Map Area Conditional Formatting dialog, set the format which will be applied to the specified map areas when the specified condition is fulfilled, including the fill color, border color, border style, and border width.
10. Repeat the above steps to add more conditions and define the format for each condition.

    To edit a condition, select the condition from the Map Area Condition box, select the **Edit** button, then edit the condition in the Edit Conditions dialog.

    To adjust the priority of the conditions, select a condition and select the **High** or **Low** button.

    To remove a condition and the corresponding format, select the condition from the Map Area Condition box and then select the **Remove** button.
11. When done, select **OK** to save and apply the settings.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584121-Binding-Data-to-a-Shape-Map)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584161-Binding-Links-to-Shape-Map-Areas)
