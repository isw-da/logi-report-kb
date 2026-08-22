---
title: "Enter Values Dialog Box Properties"
id: 4405690548759
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690548759-Enter-Values-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:01Z
---

# Enter Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683747607-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683748759-JDashboard-Profile-Properties)

# Enter Values Dialog Box Properties

Use the Enter Values dialog box to [specify multiple values for a parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405684003607-Specifying-Parameter-Values#MultiValue). This topic describes how to select or type multiple values.

Server displays the dialog box when you select the arrow ![More button](https://devnet.logianalytics.com/hc/article_attachments/4420447073047/btn_srchtlbr_adv.gif) in the value combo box while specifying values for a parameter that enables multiple values.

![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453479575/entervlu.gif)

**All Values**

Server displays this option when the parameter's **Enable the "All Values" Option** property is **true**. By default, Server selects this option and applies all the values of the parameter. In this case, when you insert the parameter as a field into a report, the field will show the string **All**.

Clear **All Values** if you want to customize the values. Then Server enables the following options.

**Available Values**

Server lists the predefined parameter values for selection. When the parameter is bound with a column, but the display column is different from the bound column, it lists the values of the display column here.

When the parameter has more than 500 values, after you scroll down to the bottom of the value list, Server automatically loads more values into the list.

* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)**Search button**  
  Select to open the search box to search for values among the available values. To start the search, type the text you want to search for, and Server lists the values that contain the matched text. The search results are case insensitive and do not match whole word.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420447138711/btn_sort2.gif)**Sort button**  
  Select to open the Sort menu to sort the values in the ascending or descending order or following the original order as in the database.

**Enter Values**

Server displays this option when the parameter's **Allow Type-in of Value** property is **true**. You can add values for the parameter manually.

When the parameter is of the Date, DateTime, or Time type, you can select the Calendar icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4420453597719/btn_clndr_18x18.gif) to open the calendar to specify a date and time value.

**Selected Values**

Server lists the values that you have selected. The selected values are case sensitive.

![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4420447121559/btn_add.gif) **Add button**

Select to add the selected values from the Available Values box to the Selected Values box, or add the value you typed in the Enter Values text box to the Selected Values box.

![Remove Values](https://devnet.logianalytics.com/hc/article_attachments/4420461527319/btn_rmv.gif) **Remove button**

Select to remove the selected values from the Selected Values box.

![Add All Values](https://devnet.logianalytics.com/hc/article_attachments/4420447138967/btn_addall.gif) **Add All button**

Select to add all the listed values from the Available Values box to the Selected Values box.

![Remove All Values](https://devnet.logianalytics.com/hc/article_attachments/4420461549975/btn_rmvall.gif)**Remove All button**

Select to remove all the values from the Selected Values box.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683747607-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683748759-JDashboard-Profile-Properties)
