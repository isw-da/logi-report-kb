---
title: "Customizing the Field Display Names"
id: 1500009592861
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592861-Customizing-the-Field-Display-Names
updated_at: 2021-07-24T05:53:49Z
---

# Customizing the Field Display Names

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592841-Obtaining-Detailed-Information-from-a-Banded-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570962-Predefining-Sort-and-Filter-Conditions)

# Customizing the Field Display Names

In Page Report Studio, you can go around report data, sort report data on certain fields, search a report for some text, and filter the report data using filter conditions. When you perform these operations, you will be working with field mapping names. However, with just the field mapping names, you may find it inconvenient for end users, especially when the field mapping name is obscure. To help you, Logi JReport provides a display name customizing function for you to define the column names as required, and also to specify the actions which the display names will take part in.

To customize the field display names, follow the steps below:

1. Open a page report in Logi JReport Designer.
2. Select  **Report** > **Edit Display Name** to display the Edit Display Name dialog.

   ![Edit Display Name dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893809303/edtdsplynm.gif)
3. Select a dataset from the Report Dataset drop-down list, and all the fields in the dataset will be shown in the mapping name box.
4. To make the resource names sort automatically, check the **Auto Sort** checkbox.
5. Specify the display names for the fields in the Display Name column. A formula can be selected as the display name of the field.
6. Select another dataset and repeat the above steps to edit the display names of fields in it.
7. If required, you can select the **Advanced** button to further customize the display names in specific components in the Edit Display Name for Component dialog.

   ![Edit Display Name for Component dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893809559/edtdsplynmcmpnt.gif)
8. From the Component drop-down list, select the component you want to customize.

   **Tip:** You can also right-click a component and then select Edit Display Name from the shortcut menu to display the Edit Display Name for Component dialog. However, if the dialog is opened in this way, only the component you right-click on will be listed in the Component drop-down list.
9. In the action columns, check the corresponding checkboxes to indicate whether the actions are enabled for the fields. Check the checkbox on the action column header if you want the corresponding action to be enabled for all fields. If any action is not supported on the selected component type, the corresponding column will be disabled.

   When an action is checked for a field, the field's display name instead of mapping name will be shown in the corresponding dialog or submenu in Page Report Studio. If you uncheck the box for any field in any action column, the field will not be available for the action. Moreover, if you set the display name of any field to be blank in the Edit Display Name dialog, all actions will be disabled for the field, which means end users will not be able to perform all these actions on the field in Page Report Studio.
10. Upon finishing, select **OK** to accept the changes.

**Note:** If you set the display name of any field to be blank, the field will not be shown in the lists where display names are displayed in Page Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592841-Obtaining-Detailed-Information-from-a-Banded-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570962-Predefining-Sort-and-Filter-Conditions)
