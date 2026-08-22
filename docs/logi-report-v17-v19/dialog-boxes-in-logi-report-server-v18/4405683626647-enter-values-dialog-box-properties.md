---
title: "Enter Values Dialog Box Properties"
id: 4405683626647
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683626647-Enter-Values-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:38Z
---

# Enter Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683625623-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683627671-Export-Dialog-Box-Properties)

# Enter Values Dialog Box Properties

You can use the Enter Values dialog box to [specify multiple values for a parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405683596567-Specifying-Parameter-Values-for-a-Dashboard#MultiValue). This topic describes how to select or type multiple values.

![Enter Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420447328023/entervlu.gif)

**All Values**

Server displays this property when the parameter's **Enable the "All Values" Option** property is **true**. By default, Server selects **All Values** and applies all the values of the parameter. In this case, when you insert the parameter as a field into a report, the field will show the string **All**.

Clear **All Values** if you want to customize the values. Then Server enables the following properties.

**Available Values**

Server lists the predefined parameter values (500 at most) for selection. When the parameter is bound with a column, but the display column is different from the bound column, Server lists the values of the display column here.

**Enter Value**

Server displays this property when the parameter's **Allow Type-in of Value** property is **true**. You can add values for the parameter manually.

* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4420461463447/btn_clndr.gif)**Calendar icon**  
  Server displays this icon when the parameter is of the Date, DateTime, or Time type. Select the icon to open the calendar to specify a date and time value.

**Search**

Server displays this property when the parameter's **Allow Type-in of Value** property is **false**. You can search for values among the available values. The search results are case insensitive and do not match the whole word.

**Selected Values**

Server lists the values that you have selected. The selected values are case sensitive.

![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4420453404695/btn_add2.gif)

Select to add the selected values from the Available Values box to the Selected Values box, or to add the value you typed in the Enter Value text box to the Selected Values box.

![Remove Values](https://devnet.logianalytics.com/hc/article_attachments/4420461467415/btn_rmv1.gif)

Select to remove the selected values from the Selected Values box.

![Add All Values](https://devnet.logianalytics.com/hc/article_attachments/4420453404951/btn_addall1.gif)

Select to add all the listed values from the Available Values box to the Selected Values box.

![Remove All Values](https://devnet.logianalytics.com/hc/article_attachments/4420453405975/btn_rmvall1.gif)

Select to remove all the values from the Selected Values box.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683625623-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683627671-Export-Dialog-Box-Properties)
