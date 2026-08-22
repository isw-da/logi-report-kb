---
title: "Select Field Dialog Box Properties"
id: 4405690604311
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690604311-Select-Field-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:27Z
---

# Select Field Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683878679-Select-Data-Source-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683879831-Select-Fields-Dialog-Box-Properties)

# Select Field Dialog Box Properties

This topic describes how you can use the Select Field dialog box to select the fields that you want. The dialog box varies according to different sources that you opened it from.

---

When you select **+** on the title bar of the **Filter** panel to open the Select Field dialog box, you see the following properties in the dialog box:

![Select Field dialog - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420453436055/slctfld.gif)

**Select Fields**

Select the fields of the same data type to add into the Filter panel. You cannot add incomparable data type fields to the Filter panel together, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

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

**Apply To**

Select the data components in the current report to which you want to apply the filter.

**OK**

Select **OK** to apply the field you selected here.

**Cancel**

Select **Cancel** to close the dialog box without selecting a field.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the Select Field dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without selecting a field.

---

When you select **Add Dynamic Field** in the [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/4405683857175-Insert-Link-Dialog-Box-Properties) dialog box or [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/4405683813143-Edit-Link-Dialog-Box-Properties) dialog box when the link type is URL or E-mail, you see the following properties in the Select Field dialog box:

![Select Field dialog - Add Dynamic Field](https://devnet.logianalytics.com/hc/article_attachments/4420461486743/slctfld1.gif)

**Resources box**

Server lists all the elements in the current business view and dynamic resources in the current report. Select a field from the resource tree to insert it into the URL or email address to compose a dynamic hyperlink. You should make sure the field you select contains the information to compose a correct URL or email address.

* **Current Field**  
  Select this item to use the field that is related to the trigger object of the link to compose the URL or email address.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif)

Select to select an [order](#Order) from the drop-down list with which to sort the view elements. Once you changed the order, it applies to all the resource trees where you see the business view elements.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)

Select to launch the [search bar](#Search) to search for view elements.

**All Available Values**

Select this property if you want to display in the URL all the runtime values of the field that you selected here, instead of only one value. You can select this property when you are linking an object in a chart, table, banded object, or crosstab (excluding its summaries) to URL, and when you did not select **Current Field**.

**OK**

Select **OK** to apply the field you selected here.

**Cancel**

Select **Cancel** to close the dialog box without selecting a field.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the Select Field dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without selecting a field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683878679-Select-Data-Source-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683879831-Select-Fields-Dialog-Box-Properties)
