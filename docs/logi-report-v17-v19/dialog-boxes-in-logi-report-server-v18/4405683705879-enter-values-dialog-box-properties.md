---
title: "Enter Values Dialog Box Properties"
id: 4405683705879
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683705879-Enter-Values-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:54Z
---

# Enter Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690534551-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690535447-Export-Dialog-Box-Properties)

# Enter Values Dialog Box Properties

Use the Enter Values dialog box to [specify multiple values for the parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405683596567-Specifying-Parameter-Values-for-a-Dashboard#MultiValue). This topic describes how to select or type multiple values.

Server displays the dialog box when you select the value combo box while specifying values for a parameter that enables multiple values.

![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461690263/entervlu.gif)

**All Values**

Server displays this option when the parameter's **Enable the "All Values" Option** property is **true**. By default, Server selects this option and applies all the values of the parameter. In this case, when you insert the parameter as a field into a dashboard, the field will show the string **All**.

Clear this option if you want to customize the values. Then, Server enables the following properties.

**Available Values**

Server lists the predefined parameter values (500 at most) for selection. When the parameter is bound with a column, but the display column is different from the bound column, Server lists the values of the display column here.

**Enter Value**

Server displays this property when the parameter's **Allow Type-in of Value** property is **true**. You can add values for the parameter manually.

When the parameter is of the Date, DateTime, or Time type, you can select the calendar icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4420461463447/btn_clndr.gif) to open the calendar to specify a date and time value.

**Search**

Server displays this property when the parameter's **Allow Type-in of Value** property is **false**. You can search for values among the available values. The search results are case insensitive and do not match whole word.

**Selected Values**

Server lists the values that you have selected. The selected values are case sensitive.

![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4420453404695/btn_add2.gif)**Add button**

Select to add the selected values from the Available Values box to the Selected Values box, or add the value you typed in the Enter Value text box to the Selected Values box.

![Remove Values](https://devnet.logianalytics.com/hc/article_attachments/4420461467415/btn_rmv1.gif)**Remove button**

Select to remove the selected values from the Selected Values box.

![Add All Values](https://devnet.logianalytics.com/hc/article_attachments/4420453404951/btn_addall1.gif)**Add All button**

Select to add all the listed values from the Available Values box to the Selected Values box.

![Remove All Values](https://devnet.logianalytics.com/hc/article_attachments/4420453405975/btn_rmvall1.gif)**Remove All button**

Select to remove all the values from the Selected Values box.

**OK**

Select to apply the specified values for the parameter.

**Cancel**

Select to close the dialog box without changing the parameter values.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the Enter Values dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without changing the parameter values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690534551-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690535447-Export-Dialog-Box-Properties)
