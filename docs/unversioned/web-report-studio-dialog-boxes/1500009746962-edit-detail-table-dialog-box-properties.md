---
title: "Edit Detail Table Dialog Box Properties"
id: 1500009746962
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746962-Edit-Detail-Table-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:29Z
---

# Edit Detail Table Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746942-Edit-Conditions-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775141-Edit-Filter-Control-Dialog-Box-Properties)

# Edit Detail Table Dialog Box Properties

This topic describes how you can use the Edit Detail Table dialog box to edit the fields to display in the table when performing the [go-to-detail action](https://devnet.logianalytics.com/hc/en-us/articles/1500009778781-Going-Through-Web-Report-Data#Go-to-detail) on the summary. Server displays the dialog box when you right-click a summary value (for a chart it is any data marker) and select **Edit Detail Table** from the shortcut menu.

![Edit Detail Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880186007/edtdtltbl.gif)

**Resources**

Displays all the group and detail objects in the selected business view.

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

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected view element to be displayed in the table.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

Removes the selected view element.

**Field**

Lists the view elements that have been added to the detail table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected view element higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected view element lower in the list.

**Target**

Specifies the window or frame in which to load the detail table.

* **New Window**  
   Loads the detail table into a new window.
* **Same Frame**  
   Loads the detail table into the same frame or window where the main report is.
* **Other Frame**  
   Loads the detail table into some other available frame. Type the frame name into the text box to find the frame. If the frame does not exist, the detail table report will be loaded into a new window.
* **<Server Setting>**  
   Loads the detail table according to setting of the [Target of Detail Table Report and Links](https://devnet.logianalytics.com/hc/en-us/articles/1500009750242-Customizing-Web-Report-Studio-Profile#Target) option in the Web Report Studio profile.

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Cancels the changes and exits the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746942-Edit-Conditions-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775141-Edit-Filter-Control-Dialog-Box-Properties)
