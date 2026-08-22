---
title: "Custom Sort Dialog Box Properties"
id: 1500009775101
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775101-Custom-Sort-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:32Z
---

# Custom Sort Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774981-Cube-Status-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746882-Customize-Gauge-Angle-Dialog-Box-Properties)

# Custom Sort Dialog Box Properties

This topic describes how you can use the Custom Sort dialog box to set the [sort manner of the detail data](https://devnet.logianalytics.com/hc/en-us/articles/1500009750122-Inserting-Components-in-Web-Report#Sort) in a table, or the [sort manner of a specific group](https://devnet.logianalytics.com/hc/en-us/articles/1500009750122-Inserting-Components-in-Web-Report#GroupSort) in a table or chart.

Server displays the dialog box when you do either of the following:

* Select the Sort Fields By button in the Display tab of the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776521-Table-Wizard-Properties#Display) or [Insert Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009776041-Insert-Table-Dialog-Box-Properties#Display) dialog box, or in the Display tab for table in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776601-Web-Report-Wizard-Properties#Table).
* Select Custom Sort from the Sort column in the Group/Columns tab of the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776521-Table-Wizard-Properties), [Insert Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009776041-Insert-Table-Dialog-Box-Properties) dialog box, or [Convert to Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009746822-Convert-to-Table-Dialog-Box-Properties) dialog box, or in the Group/Columns tab for table in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776601-Web-Report-Wizard-Properties#Table).
* Select the Sort Field By button in the Details tab for table in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776601-Web-Report-Wizard-Properties#Table), or in the Details tab of the [Convert to Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009746822-Convert-to-Table-Dialog-Box-Properties) dialog box.
* Select Custom Sort from the Based On drop-down list in the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500009746902-Category-Options-Dialog-Box-Properties), [Group Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500009775881-Group-Options-Dialog-Box-Properties), or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500009747962-Series-Options-Dialog-Box-Properties).

![Custom Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880169879/cstmsrt.gif)

**Resources**

Lists the view elements in the business view the current table or chart uses, which can be used as the sort-by fields. If the dialog box is opened from the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776601-Web-Report-Wizard-Properties), the dynamic resources created for the business view are also listed.

![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880163863/btn_wbrpt_edit.gif)

Edits the selected dynamic resource.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected dynamic resource.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

* **Predefined Order**  
  Select if you want to sort the view elements in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the view elements by resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the view elements in alphabetical order. Logi Report sorts the elements that are not in any category first, and then the categories. It also sorts the elements in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the search bar to search for view elements.

See the following options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **X**  
  Select to close the search bar or clear the typed text.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
  When you selected **Highlight All**, you can use this button to go to the previous matched text.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
   When you selected **Highlight All**, you can use this button to go to the next matched text.

**Sort By**

Displays the fields on which the sorting will be based.

**Sort**

Specifies the sort manner.

* **Ascend**  
   If selected, the table detail data or the specified group will be sorted based on values of the specified sort-by field in ascending order.
* **Descend**  
   If selected, the table detail data or the specified group will be sorted based on values of the specified sort-by field in descending order.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected field as the sort-by field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

Removes the selected sort-by field.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected sort-by field higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected sort-by field lower in the list.

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774981-Cube-Status-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746882-Customize-Gauge-Angle-Dialog-Box-Properties)
