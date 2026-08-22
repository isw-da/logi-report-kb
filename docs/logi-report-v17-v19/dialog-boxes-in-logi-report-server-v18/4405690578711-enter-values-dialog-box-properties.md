---
title: "Enter Values Dialog Box Properties"
id: 4405690578711
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690578711-Enter-Values-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:15Z
---

# Enter Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683814423-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683815831-Export-Dialog-Box-Properties)

# Enter Values Dialog Box Properties

You can use the Enter Values dialog box to [specify multiple values for a parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405690688919-Applying-Parameters-to-Web-Report#MultiValue). This topic describes how to select or type multiple values.

Logi Report displays the dialog box when you select in the value combo box while specifying values for a parameter that enables multiple values.

![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453404439/entervlu.gif)

**All Values**

Logi Report displays this option when the parameter's **Enable the "All Values" Option** property is **true**. By default, Logi Report selects this option and applies all the values of the parameter. In this case, when you insert the parameter as a field into a report, the field will show the string **All**.

Clear this option if you want to customize the values. Then Logi Report enables the following options.

**Available Values**

Logi Report lists the predefined parameter values for selection. When the parameter is bound with a column, but the display column is different from the bound column, it lists the values of the display column here.

When the parameter has more than 500 values, after you scroll down to the bottom of the value list, more values will be automatically loaded into the list.

* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)**Search**  
  Select to open the search box to search for values among the available values. To start the search, type the text you want to search for and Logi Report lists the values that contain the matched text. The search results are case insensitive and do not match whole word.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif)**Sort**  
  Select to open the Sort drop-down menu to sort the values in the ascending or descending order or following the original order as in the database.

**Enter Values**

Logi Report displays this option when the parameter's **Allow Type-in of Value** property is **true**. You can add values for the parameter manually.

* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4420461463447/btn_clndr.gif)**Calendar icon**  
  Select this icon to open the calendar to specify a date and time value. Logi Report displays this icon only when the parameter is of the Date, DateTime, or Time type.

**Selected Values**

Logi Report lists the values that you have selected. The selected values are case sensitive.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420453404695/btn_add2.gif)

Select to add the selected values from the Available Values box to the Selected Values box, or add the value you typed in the Enter Values text box to the Selected Values box.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420461467415/btn_rmv1.gif)

Select to remove the selected values from the Selected Values box.

![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4420453404951/btn_addall1.gif)

Select to add all the listed values from the Available Values box to the Selected Values box.

![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4420453405975/btn_rmvall1.gif)

Select to remove all the values from the Selected Values box.

**OK**

Select **OK** to select the specified values for the parameter.

**Cancel**

Select **Cancel** to close the dialog box without changing the parameter values.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the Enter Values dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without changing the parameter values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683814423-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683815831-Export-Dialog-Box-Properties)
