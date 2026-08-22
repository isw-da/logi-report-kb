---
title: "Customizing Field Display Names for Datasets in a Report"
id: 5735569625367
section: "Manipulating Report Datasets - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735569625367-Customizing-Field-Display-Names-for-Datasets-in-a-Report
updated_at: 2022-11-02T08:17:39Z
---

# Customizing Field Display Names for Datasets in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533990295-Editing-Properties-of-Datasets-in-a-Report-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520464535-Working-with-Components-in-Reports)

# Customizing Field Display Names for Datasets in a Report

For datasets created on query resources in a page report, you can customize display names of the data fields in the datasets, so that when users run the page report in Page Report Studio and perform operations such as Sort and Filter on data components in the page report, they will be able to work with intuitive field names. You can also specify the actions in which the customized display names will participate for each data component in the page report. This topic describes how you can customize field display names for datasets in a query-based page report.

1. Open the page report.
2. Navigate to **Report** > **Edit Display Name**. Designer displays the [Edit Display Name dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522519831-Edit-Display-Name-Dialog-Box).

   ![Edit Display Name dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898458554775/edtdsplynm.gif)
3. From the **Report Dataset** drop-down list, which contains all datasets used in the page report, select a dataset and Designer displays all the data fields in the dataset in the mapping name box.
4. To make the resource names sort automatically, select **Auto Sort**.
5. Specify the display names for the data fields in the **Display Name** column. You can also select a formula as the display name of the data field. If you set the display name of any data field to be blank, the field will not be shown in the lists where display names are used in Page Report Studio.
6. Select another dataset and repeat the preceding steps to edit the display names of data fields in it.
7. You can select **Advanced** to further customize the display names for data components in the page report using the [Edit Display Name for Component dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735500381463-Edit-Display-Name-for-Component-Dialog-Box).

   ![Edit Display Name for Component dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475626903/edtdsplynmcmpnt.gif)
8. From the **Component** drop-down list, select the data component in the page report that you want to customize.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can also right-click a data component that uses a query resource in a page report and then select **Edit Display Name** from the shortcut menu to display the Edit Display Name for Component dialog box (if you open the dialog box in this way, Designer only lists the component that you right-click on in the Component drop-down list).
9. In the action columns, select the corresponding checkboxes to indicate whether to enable the actions for the data fields. Select the checkbox on the action column header if you want to enable the action for all data fields. If any action is not supported on the selected data component, Designer disables the corresponding column. When you select an action for a data field, users see the field's display name instead of mapping name in the corresponding dialog box or submenu in Page Report Studio. If you clear the check box for any field in any action column, the field will not be available for the action. Moreover, if you set the display name of any field to be blank, all actions will be disabled for the field, meaning, users will not be able to perform all these actions on the field in Page Report Studio.
10. Select **OK** to accept the changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533990295-Editing-Properties-of-Datasets-in-a-Report-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520464535-Working-with-Components-in-Reports)
