---
title: "Edit Display Name for Component Dialog"
id: 1500009586421
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586421-Edit-Display-Name-for-Component-Dialog
updated_at: 2021-07-24T05:55:26Z
---

# Edit Display Name for Component Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586401-Edit-Display-Name-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog)

# Edit Display Name for Component Dialog

The Edit Display Name for Component dialog appears when you select the Advanced button in the [Edit Display Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009586401-Edit-Display-Name-Dialog) dialog, or right-click a data component and select Edit Display Name from the shortcut menu in the design area. It helps you to define in which actions [display names of fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009592861-Customizing-the-Field-Display-Names) in the data component will take part in Page Report Studio. [See the dialog](javascript:%20void(null)).

![Edit Display Name for Component dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893809559/edtdsplynmcmpnt.gif)

The following are details about options in the dialog:

**Component**

* If the dialog is opened by selecting the Advanced button in the Edit Display Name dialog, in the drop-down list, all the data components in current report will be listed.
* If the dialog is opened by selecting Edit Display Name on the shortcut menu of a data component in the design area, only the specified component will be listed in this drop-down list.

**Resource Name**

Displays the names of fields in the selected component.

**Display Name**

Shows the display names for fields in the selected component.

**Action columns**

Indicates whether the actions are enabled for the fields. When an action is enabled for a field, the field's display name instead of the mapping name will be shown in the corresponding dialog or submenu in Page Report Studio; when not enabled, end users will not be able to perform this action on the field in Page Report Studio. If the display name of any field is set to be blank, the field will not be available for any of the actions below. Check the box on the column header to enable the corresponding action on all fields.

* **Sort**  
   Specifies whether to enable the Sort action on the fields. The Sort column is disabled when the selected component is a crosstab or chart.
* **Filter**Specifies whether to enable the Filter action on the fields.
* **Go**  
   Specifies whether to enable the Go action on the fields. The Go column is disabled when the selected component is a crosstab.
* **Search**  
   Specifies whether to enable the Search action on the fields. The Search column is disabled when the selected component is a crosstab or chart.
* **Sort in Group**  
   For a grouped banded object or table, end users can also choose to sort the groups at certain group level based on a specified field in each group in Page Report Studio. Here you can decide whether to enable this Sort in Group action on the fields by checking the corresponding checkboxes.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586401-Edit-Display-Name-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog)
