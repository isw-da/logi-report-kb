---
title: "Enter Values Dialog Box"
id: 4405661537687
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661537687-Enter-Values-Dialog-Box
updated_at: 2022-01-27T20:36:20Z
---

# Enter Values Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664471063-Enter-Parameter-Values-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661538839-Excel-Option-Dialog-Box)

# Enter Values Dialog Box

You can use the Enter Values dialog box to [specify multiple values for a parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405661802903-Specifying-Parameter-Values#Multiple). This topic describes the options in the dialog box.

Designer displays the Enter Values dialog box when you select ![Drop-down button](https://devnet.logianalytics.com/hc/article_attachments/4420542152983/btn_drpdwn.gif) in the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664471063-Enter-Parameter-Values-Dialog-Box) if the parameter allows for multiple values.

![Enter Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542153495/entervlu.gif)

You see the following options in the dialog box:

**All Values**

Designer displays this option when the Enable the "All Values" Option property of the parameter is "true". Select it if you want to apply all values to the parameter, which can be all values of the parameter determined by Logi Report Engine, all values in the database, or all the available values according to the [Scope of All Values](https://devnet.logianalytics.com/hc/en-us/articles/4405664612887-Creating-Parameters-in-a-Catalog#AllScope) setting of the parameter.

Only when you clear this option, Designer enables the following options for adding values.

**Available Values**

This box lists all the available values of the parameter for selection. When the parameter is bound with a column, but the display column is different from the bound column, Designer lists values of the display column in the box.

**Enter Values**

Designer displays this option when the parameter's Allow Type-in of Value property is "true". You can use it to add values for the parameter manually.

* ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4420550878743/btn_clndr.gif)**Calendar button**  
  Designer displays this button only when the parameter is of the Date, Time, or DateTime type. Select it to open the calendar widget to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/4405661802903-Specifying-Parameter-Values#Date).

**Selected Values**

This box lists the values that you select to apply to the parameter. The selected values are case sensitive.

![Sort icon](https://devnet.logianalytics.com/hc/article_attachments/4420542068375/btn_sort2.gif)**Sort icon**

Select to display the Sort drop-down menu to select the order to sort the values.

* **Ascending**  
  Select to sort the values in ascending order.
* **Descending**  
  Select to sort the values in descending order.
* **No Sort**  
  Select to list the values as how you add them if the parameter is a type-in parameter, or based on their original order in the database if the parameter is bound with a column. It is the default order.

The change of sort order is a one-off action which Designer does not remember after you exit the dialog box, meaning, each time when you open the dialog box, Designer always applies No Sort to the values.

![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4420542068631/btn_srch.gif)**Search icon**

Select to open the search box to search for values. To start searching, type the text you want to search for in the search box and Designer lists the values containing the matched text.

You can use the following options in the search box:

* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4420550825111/btn_srchbox_adv.gif)**Drop-down icon**  
  Select to list more search options.
  + **Highlight All**  
    Select to highlight all the matched text.
  + **Match Case**  
    Select to search for text that meets the case of the text you type.
  + **Match Whole Word**  
    Select to search for text that looks the same as the text you type.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420550826007/btn_close1.gif)**Delete icon**  
  Select to close the search box and cancel the search.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550925975/btn_addarrow1.gif)**Add button**

Select to add the specified values from the Available Values box to the Selected Values box, or add the value you type in the Enter Values text box to the Selected Values box.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550926231/btn_rmvarrow1.gif)**Remove button**

Select to remove the specified values from the Selected Values box.

![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4420556198551/btn_addall1.gif)**Add All button**

Select to add all the listed values from the Available Values box to the Selected Values box.

![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4420556198935/btn_rmvall1.gif)**Remove All button**

Select to remove all the values from the Selected Values box.

**OK**

Select to apply the specified values for the parameter and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664471063-Enter-Parameter-Values-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661538839-Excel-Option-Dialog-Box)
