---
title: "Enter Values Dialog Box Properties"
id: 1500009774001
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009774001-Enter-Values-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:46Z
---

# Enter Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746022-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774401-Folder-Properties)

# Enter Values Dialog Box Properties

Use the Enter Values dialog box to [specify multiple values for a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009778361-Specifying-Parameter-Values#MultiValue). This topic describes how to select or type multiple values.

Logi Report displays the dialog box when you select the down arrow ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404885328919/btn_mvdown1.gif) in the value combo box while specifying values for a parameter that enables multiple values.

![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885374871/entervlu.gif)

**All Values**

Logi Report displays this option when the parameter's **Enable the "All Values" Option** property is **true**. By default, Logi Report selects this option and applies all the values of the parameter. In this case, when you insert the parameter as a field into a report, the field will show the string **All**.

Clear this option if you want to customize the values. Then Logi Report enables the following options.

**Available Values**

Logi Report lists the predefined parameter values for selection. When the parameter is bound with a column, but the display column is different from the bound column, it lists the values of the display column here.

When the parameter has more than 500 values, after you scroll down to the bottom of the value list, more values will be automatically loaded into the list.

* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)**Search**  
  Select to open the search box to search for values among the available values. To start the search, type the text you want to search for and Logi Report lists the values that contain the matched text. The search results are case insensitive and do not match whole word.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404885374487/btn_sort2.gif)**Sort**  
  Select to open the Sort drop-down menu to sort the values in the ascending or descending order or following the original order as in the database.

**Enter Values**

Logi Report displays this option when the parameter's **Allow Type-in of Value** property is **true**. You can add values for the parameter manually.

* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif)**Calendar icon**  
  Select this icon to open the calendar to specify a date and time value. Logi Report displays this icon only when the parameter is of the Date, DateTime, or Time type.

**Selected Values**

Logi Report lists the values that you have selected. The selected values are case sensitive.

![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4404880219927/btn_add.gif)

Select to add the selected values from the Available Values box to the Selected Values box, or add the value you typed in the Enter Values text box to the Selected Values box.

![Remove Values](https://devnet.logianalytics.com/hc/article_attachments/4404880220567/btn_rmv.gif)

Select to remove the selected values from the Selected Values box.

![Add All Values](https://devnet.logianalytics.com/hc/article_attachments/4404885375127/btn_addall.gif)

Select to add all the listed values from the Available Values box to the Selected Values box.

![Remove All Values](https://devnet.logianalytics.com/hc/article_attachments/4404880236567/btn_rmvall.gif)

Select to remove all the values from the Selected Values box.

**OK**

Select **OK** to select the specified values for the parameter.

**Cancel**

Select **Cancel** to close the dialog box without changing the parameter values.

**Help**

Select **Help** to view information about the Enter Values dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746022-Enter-Parameter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774401-Folder-Properties)
