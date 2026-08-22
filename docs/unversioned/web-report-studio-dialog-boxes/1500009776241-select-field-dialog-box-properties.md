---
title: "Select Field Dialog Box Properties"
id: 1500009776241
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776241-Select-Field-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:12Z
---

# Select Field Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776221-Select-Data-Source-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776261-Select-Fields-Dialog-Box-Properties)

# Select Field Dialog Box Properties

This topic describes how you can use the Select Field dialog box to select the fields that you want. The dialog box varies according to different sources that you opened it from.

---

When you select **+** on the title bar of the **Filter** panel to open the Select Field dialog box, you see the following properties in the dialog box:

![Select Field dialog - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404880190871/slctfld.gif)

**Select Fields**

Select the fields of the same data type to add into the Filter panel. You cannot add incomparable data type fields to the Filter panel together, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Select to select an order from the drop-down list with which to sort the view elements. Once you changed the order, it applies to all the resource trees where you see the business view elements.

The order can be one of the following:

* **Predefined Order**  
  Select if you want to sort the view elements in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the view elements by resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the view elements in alphabetical order. Logi Report sorts the elements that are not in any category first, and then the categories. It also sorts the elements in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Select to launch the search bar to search for view elements.

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

**Apply To**

Select the data components in the current report to which you want to apply the filter.

**OK**

Select **OK** to apply the field you selected here.

**Cancel**

Select **Cancel** to close the dialog box without selecting a field.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Select Field dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without selecting a field.

---

When you select **Add Dynamic Field** in the [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009747642-Insert-Link-Dialog-Box-Properties) dialog box or [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009775181-Edit-Link-Dialog-Box-Properties) dialog box when the link type is URL or E-mail, you see the following properties in the Select Field dialog box:

![Select Field dialog - Add Dynamic Field](https://devnet.logianalytics.com/hc/article_attachments/4404885332503/slctfld1.gif)

**Resources box**

Server lists all the elements in the current business view and dynamic resources in the current report. Select a field from the resource tree to insert it into the URL or e-mail address to compose a dynamic hyperlink. You should make sure the field you select contains the information to compose a correct URL or e-mail address.

* **Current Field**  
  Select this item to use the field that is related to the trigger object of the link to compose the URL or e-mail address.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Select to select an [order](#Order) from the drop-down list with which to sort the view elements. Once you changed the order, it applies to all the resource trees where you see the business view elements.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Select to launch the [search bar](#Search) to search for view elements.

**![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")All Available Values**

Select this property if you want to display in the URL all the runtime values of the field that you selected here, instead of only one value. You can select this property when you are linking an object in a chart, table, banded object, or crosstab (excluding its summaries) to URL, and when you did not select **Current Field**.

**OK**

Select **OK** to apply the field you selected here.

**Cancel**

Select **Cancel** to close the dialog box without selecting a field.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Select Field dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without selecting a field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776221-Select-Data-Source-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776261-Select-Fields-Dialog-Box-Properties)
