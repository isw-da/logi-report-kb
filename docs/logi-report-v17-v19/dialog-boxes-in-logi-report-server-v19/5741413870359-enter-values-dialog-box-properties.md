---
title: "Enter Values Dialog Box Properties"
id: 5741413870359
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741413870359-Enter-Values-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:56Z
---

# Enter Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741442503831-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741405863703-JDashboard-Profile-Properties)

# Enter Values Dialog Box Properties

Use the Enter Values dialog box to [specify multiple values for a parameter](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values#MultiValue). This topic describes how to select or type multiple values.

Server displays the dialog box when you select the arrow ![More button](https://devnet.logianalytics.com/hc/article_attachments/9905631409303/btn_srchtlbr_adv.gif) in the value combo box while specifying values for a parameter that enables multiple values.

![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/9905659393815/entervlu.gif)

**All Values**

Server displays this option when the parameter's **Enable the "All Values" Option** property is **true**. By default, Server selects this option and applies all the values of the parameter. In this case, when you insert the parameter as a field into a report, the field will show the string **All**.

Clear **All Values** if you want to customize the values. Then Server enables the following options.

**Available Values**

Server lists the predefined parameter values for selection. When the parameter is bound with a column, but the display column is different from the bound column, it lists the values of the display column here.

When the parameter has more than 500 values, after you scroll down to the bottom of the value list, Server automatically loads more values into the list.

* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**  
  Select to open the search box to search for values among the available values. To start the search, type the text you want to search for, and Server lists the values that contain the matched text. The search results are case insensitive and do not match whole word.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905659372695/btn_sort2.gif)**Sort button**  
  Select to open the Sort menu to sort the values in the ascending or descending order or following the original order as in the database.

**Enter Values**

Server displays this option when the parameter's **Allow Type-in of Value** property is **true**. You can add values for the parameter manually.

When the parameter is of the Date, DateTime, or Time type, you can select the Calendar icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/9905758429207/btn_clndr_18x18.gif) to open the calendar to specify a date and time value.

**Selected Values**

Server lists the values that you have selected. The selected values are case sensitive.

![Add Values](https://devnet.logianalytics.com/hc/article_attachments/9905636390807/btn_add.gif) **Add button**

Select to add the selected values from the Available Values box to the Selected Values box, or add the value you typed in the Enter Values text box to the Selected Values box.

![Remove Values](https://devnet.logianalytics.com/hc/article_attachments/9905657793175/btn_rmv.gif) **Remove button**

Select to remove the selected values from the Selected Values box.

![Add All Values](https://devnet.logianalytics.com/hc/article_attachments/9905659411351/btn_addall.gif) **Add All button**

Select to add all the listed values from the Available Values box to the Selected Values box.

![Remove All Values](https://devnet.logianalytics.com/hc/article_attachments/9905659441303/btn_rmvall.gif)**Remove All button**

Select to remove all the values from the Selected Values box.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741442503831-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741405863703-JDashboard-Profile-Properties)
