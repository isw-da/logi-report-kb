---
title: "Edit Display Name for Component Dialog"
id: 1500009630661
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630661-Edit-Display-Name-for-Component-Dialog
updated_at: 2021-07-24T16:04:48Z
---

# Edit Display Name for Component Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630641-Edit-Display-Name-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog)

# Edit Display Name for Component Dialog

The Edit Display Name for Component dialog helps you to define in which actions [display names of the fields will take part](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets#Customize) in the data component at runtime. It appears when you select the Advanced button in the [Edit Display Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009630641-Edit-Display-Name-Dialog) dialog, or right-click a data component created using a query resource in a page report and select Edit Display Name from the shortcut menu.

![Edit Display Name for Component dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904199703/edtdsplynmcmpnt.gif)

The following are details about options in the dialog:

**Component**

* If the dialog is opened by selecting the Advanced button in the Edit Display Name dialog, in the drop-down list, all the data components in current page report will be listed.
* If the dialog is opened by selecting Edit Display Name on the shortcut menu of a data component in the design area, only the specified component will be listed in this drop-down list.

**Resource Name**

Displays the names of the fields in the selected component.

**Display Name**

Shows the display names of the fields in the selected component.

**Action columns**

Indicates whether the actions are enabled for the fields. When an action is enabled for a field, the field's display name instead of the mapping name will be shown in the corresponding dialog or submenu in Page Report Studio; when not enabled, end users will not be able to perform this action on the field in Page Report Studio. If the display name of any field is set to be blank, the field will not be available for any of the actions below. Select the box on the column header to enable the corresponding action on all fields.

* **Sort**  
   Specifies whether to enable the Sort action on the fields. The Sort column is disabled when the selected component is a crosstab or chart.
* **Filter**  
   Specifies whether to enable the Filter action on the fields.
* **Go**  
   Specifies whether to enable the Go action on the fields. The Go column is disabled when the selected component is a crosstab.
* **Search**  
   Specifies whether to enable the Search action on the fields. The Search column is disabled when the selected component is a crosstab or chart.
* **Sort in Group**  
   For a grouped banded object or table, end users can also choose to sort the groups at certain group level based on a specified field in each group in Page Report Studio. Here you can decide whether to enable this Sort in Group action on the fields by selecting the corresponding checkboxes.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630641-Edit-Display-Name-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog)
