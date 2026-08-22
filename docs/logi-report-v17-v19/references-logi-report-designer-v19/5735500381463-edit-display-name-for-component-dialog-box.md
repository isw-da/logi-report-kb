---
title: "Edit Display Name for Component Dialog Box"
id: 5735500381463
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735500381463-Edit-Display-Name-for-Component-Dialog-Box
updated_at: 2022-11-02T04:14:57Z
---

# Edit Display Name for Component Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735522519831-Edit-Display-Name-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522539031-Edit-Filter-Dialog-Box)

# Edit Display Name for Component Dialog Box

You can use the Edit Display Name for Component dialog box to define for which actions [display names of the fields will take effect](https://devnet.logianalytics.com/hc/en-us/articles/5735569625367-Customizing-Field-Display-Names-for-Datasets-in-a-Report) in the data component at runtime. This topic describes the options in the dialog box.

Designer displays the Edit Display Name for Component dialog box when you select Advanced in the [Edit Display Name dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522519831-Edit-Display-Name-Dialog-Box), or right-click a data component in a query-based page report and select Edit Display Name from the shortcut menu.

![Edit Display Name for Component dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475626903/edtdsplynmcmpnt.gif)

Designer displays these options:

**Component**

Select the data component for which to edit the display names.

* If you open the dialog box by selecting Advanced in the Edit Display Name dialog box, Designer lists all the data components in current page report in this drop-down list.
* If you open the dialog box by selecting Edit Display Name on the shortcut menu of a data component in the design area, Designer only lists the specified component in this drop-down list.

**Resource Name**

This column shows the names of the data fields in the selected component.

**Display Name**

This column shows the display names you specify for the data fields in the selected component.

**Action columns**

You can specify in the action columns whether an action is enabled for the fields. When you enable an action for a field, the field's display name instead of the mapping name are shown in the corresponding dialog box or submenu in Page Report Studio; otherwise, users are not able to perform this action on the field in Page Report Studio. If you set the display name of any field to blank, the field is not available for any of the following actions. Select the checkbox on the column header to enable the corresponding action on all fields.

* **Sort**  
  Select to enable the Sort action on the fields. Designer disables the Sort column when the selected component is a crosstab or chart.
* **Filter**  
  Select to enable the Filter action on the fields.
* **Go**  
  Select to enable the Go action on the fields. Designer disables the Go column when the selected component is a crosstab.
* **Search**  
  Select to enable the Search action on the fields. Designer disables the Search column when the selected component is a crosstab or chart.
* **Sort in Group**  
  For a grouped banded object or table, users can also choose to sort the groups at certain group level based on a specified field in each group in Page Report Studio. Here you can decide whether to enable this Sort in Group action on the fields by selecting the corresponding checkboxes.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735522519831-Edit-Display-Name-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522539031-Edit-Filter-Dialog-Box)
