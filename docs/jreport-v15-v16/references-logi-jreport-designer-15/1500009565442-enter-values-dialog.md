---
title: "Enter Values Dialog"
id: 1500009565442
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565442-Enter-Values-Dialog
updated_at: 2021-07-24T05:55:22Z
---

# Enter Values Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586681-Enter-Parameter-Values-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565462-Excel-Option-Dialog)

# Enter Values Dialog

The Enter Values dialog appears when you select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) in the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009586681-Enter-Parameter-Values-Dialog) dialog (the button is available when you set the parameter's Allow Multiple Values to true while creating it). This dialog helps you to specify multiple values for the parameter. [See the dialog](javascript:%20void(null)).

![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889364759/entervlu.gif)

**Available Values**

Lists all predefined parameter values for selection. When the parameter is bound with a column, but the Display Column is different from the Bind Column, values of the Display Column are listed here.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893920663/btn_addarrow1.gif)

Adds the selected values from the Available Values box to the Selected Values box.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889365015/btn_rmvarrow1.gif)

Removes the selected values from the Selected Values box.

![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404893920919/btn_addall1.gif)

Adds all the selected values from the Available Values box to the Selected Values box.

![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404889365271/btn_rmvall1.gif)

Removes all the selected values from the Selected Values box.

**Selected Values**

Lists the values selected. The selected values are case sensitive.

**Search**

This option is available when you set the parameter's Allow Type-in of Value to false while creating it. It is used to search for values among the available values. After you type text in the Search text box, the matched text in the available values will be highlighted.

**Enter Values**

This option is available when you set the parameter's Allow Type-in of Value to true while creating it.

Enter a value manually in the text box and then select the button next to add the value to the Selected Values box. When the parameter is bound with a column, but the display column is different from the bind column, make sure the value you enter is that of the bind column.

![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404889299735/btn_clndr.gif)

Opens the [Calendar](https://devnet.logianalytics.com/hc/en-us/articles/1500009564742-Calendar-Dialog) dialog to specify a date and time value. Available only for Date, DateTime, or Time parameter which allows for type-in values and is not bound with any column.

**All**

If selected, it means that the parameter value result is all the values in the DBMS. This option is available when you set the parameter's Enable the "All" Option to true while creating it. This is translated in SQL to remove the parameter which may select more values than listed in the available values list.

For example, when the parameter query is:

`SELECT CUSTOMERS.CUSTOMERID,CUSTOMERS.CUSTOMERNAME FROM CUSTOMERS where CUSTOMERS.CUSTOMERID>0 and CUSTOMERS.CUSTOMERID<4`

When you select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893920919/btn_addall1.gif) to add 1, 2 and 3 as the parameter values, which are all the available values, the SQL is:

`(CUSTOMERS.CUSTOMERID IN ( 1,2,3))`

Run the same report again and this time check the All checkbox in the Enter Values dialog, the query is then:

`( 1 = 1)`

In this case, you will get more customers even though available values are only 1 – 3.

**Note:** When a multi-value parameter is inserted as a field into a report and All is selected as the value, the field will show the string "All". If the parameter allows type-in values, "All" means all possible values of the parameter data type; if the parameter does not, "All" represents all the values of the parameter that come from the DBMS.

**OK**

Closes the dialog and applies the selected values to the parameter.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586681-Enter-Parameter-Values-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565462-Excel-Option-Dialog)
