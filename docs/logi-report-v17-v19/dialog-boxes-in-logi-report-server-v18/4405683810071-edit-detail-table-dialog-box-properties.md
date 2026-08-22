---
title: "Edit Detail Table Dialog Box Properties"
id: 4405683810071
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683810071-Edit-Detail-Table-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:14Z
---

# Edit Detail Table Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683809047-Edit-Conditions-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683811095-Edit-Filter-Control-Dialog-Box-Properties)

# Edit Detail Table Dialog Box Properties

This topic describes how you can use the Edit Detail Table dialog box to edit the fields to display in the table when performing the [go-to-detail action](https://devnet.logianalytics.com/hc/en-us/articles/4405684039575-Going-Through-Web-Report-Data#Go-to-detail) on the summary.

Server displays the dialog box when you right-click a summary value (for a chart it is any data marker) and select **Edit Detail Table** from the shortcut menu.

![Edit Detail Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453432727/edtdtltbl.gif)

**Resources**

Server displays all the group and detail objects in the current business view.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif) **Sort button**

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view.

The order can be one of the following:

* **Predefined Order**  
  Select if you want to sort the resources in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the resources by the resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the resources in alphabetical order. Logi Report sorts the resources that are not in any category first, and then the categories. It also sorts the resources in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)**Search button**

Select to launch the search bar to search for view elements.

See the following properties in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4420453420055/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)****Close button**  
  Select to close the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4420447073047/btn_srchtlbr_adv.gif)**More Options button**  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4420453420311/btn_srchtlbr_prv.gif) **Previous button**  
  Select to go to the previous matched text when you have selected **Highlight All**.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4420447073431/btn_srchtlbr_nxt.gif)**Next button**  
   Select to go to the next matched text when you have selected **Highlight All**.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif)**Add button**

Select to add the selected view element to display in the table.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif)**Remove button**

Select to remove the selected view element.

**Field**

Server lists the view elements that you have added to the detail table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

**Target**

Specify the window or frame in which you want to load the detail table.

* **New Window**  
   Select to load the detail table into a new window.
* **Same Frame**  
   Select to load the detail table into the same frame or window where the main report is.
* **Other Frame**  
   Select to load the detail table into some other available frame. Type the frame name into the text box to find the frame. If it cannot find the frame, Server will load the detail table report into a new window.
* **<Server Setting>**  
   Select to load the detail table according to the setting of [Target of Detail Table Report and Links](https://devnet.logianalytics.com/hc/en-us/articles/4405684049047-Customizing-Web-Report-Studio-Profile#Target) in the Web Report Studio profile.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683809047-Edit-Conditions-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683811095-Edit-Filter-Control-Dialog-Box-Properties)
