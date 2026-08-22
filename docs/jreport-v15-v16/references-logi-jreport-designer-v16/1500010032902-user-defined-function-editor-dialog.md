---
title: "User Defined Function Editor Dialog"
id: 1500010032902
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010032902-User-Defined-Function-Editor-Dialog
updated_at: 2021-07-24T10:38:19Z
---

# User Defined Function Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032942-Update-Procedures-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog)

# User Defined Function Editor Dialog

The User Defined Function Editor helps you to [write a user defined function](https://devnet.logianalytics.com/hc/en-us/articles/1500010033242-User-Defined-Formula-Functions) which can be called in a formula or another user defined function. It appears when you do either of the following:

* In the Catalog Manager, right-click the User Defined Functions node, select New Function on the shortcut menu, input a name for the new function and then select OK, or right-click a function and Select Edit from its shortcut menu.
* Select <New Function…> under the User Defined Functions node where a formula list is provided.

![User Defined Function Editor](https://devnet.logianalytics.com/hc/article_attachments/4404909145623/udfedtr.gif)

The following lists all the options that are provided in the editor. Some of them are not available depending on where the editor is opened.

**Menu**

* **File**
  + **New Function**  
     Creates a new function.
  + **New Summary**  
     Opens the [New Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010031922-New-Summary-Dialog) dialog to create a new summary.
  + **New Parameter**  
     Opens the [New Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010067241-New-Parameter-Dialog) dialog to create a new parameter.
  + **Import UDF Classes**  
     Opens the [UDF Classes](https://devnet.logianalytics.com/hc/en-us/articles/1500010032882-UDF-Classes-Dialog) dialog to import user defined formula classes.
  + **Save**  
     Saves the function.
  + **Save As**  
     Saves the function with a different name.
  + **Close**  
     Closes the window.
* **Edit**
  + **Undo**  
     Undoes an action.
  + **Redo**  
     Redoes an action.
  + **Cut**  
     Cuts the selected text in the editing panel.
  + **Copy**  
     Copies the selected text in the editing panel.
  + **Paste**  
     Pastes the text that was previously cut or copied in the editing panel.
  + **Delete**  
     Deletes the selected text in the editing panel.
  + **Search**  
     Brings out the [Find/Replace](https://devnet.logianalytics.com/hc/en-us/articles/1500010066701-Find-Replace-Dialog) dialog. You can then search for text in the editing panel, and replace the found text with different text.
* **View**
  + **Fields Panel**  
     Specifies whether to show the Fields panel.
  + **Functions Panel**  
     Specifies whether to show the Functions panel.
  + **Operators Panel**  
     Specifies whether to show the Operators panel.
  + **Sort Tree**  
     Sorts functions in the Functions panel and fields in the Fields panel by names.
* **User Defined Function**
  + **Check**  
     Tests the syntax of your function. If the syntax is incorrect, JReport gives the opportunity to correct the errors.
  + **Add Bookmark**  
     Adds a bookmark to a specific position.
  + **Go to Previous Bookmark**  
     Goes to the previous bookmark.
  + **Go to Next Bookmark**  
     Goes to the next bookmark.
  + **Clear All Bookmarks**  
     Clears all of the bookmarks.
  + **Comment/Uncomment**  
     Adds or removes comments.
  + **Add Operators**  
     Specifies a general operator to be used in the editing panel.
  + **Color Converter**  
     A [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) is provided for you to insert the HEX code of a color.
  + **Auto Finish**  
     Enables the automatic input of the other part of a sign pair right after you type in the first part when editing functions.
  + **User Defined Function References**  
     Shows the user defined functions that reference the selected UDF method in the Functions panel.
* **Help**  
  Displays the help document about this feature.

**Toolbar**

Lists the commands on the toolbar.

* **New Function**  
   Creates a new function.
* **New Summary**  
   Creates a new summary.
* **New Parameter**  
   Creates a new parameter.
* **Save**  
   Saves the function.
* **Save As**  
   Saves the function with a different name.
* **Sort Tree**  
   Sorts functions in the Functions panel and fields in the Fields panel by names.
* **Fields Panel**  
   Specifies whether to show the Fields panel.
* **Functions Panel**  
   Specifies whether to show the Functions panel.
* **Operators Panel**  
   Specifies whether to show the Operators panel.
* **Help**  
   Displays the help document about this feature.
* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/4404901169943/btn_cut.gif)**Cut**  
   Cuts the selected text in the editing panel.
* **![Copy button](https://devnet.logianalytics.com/hc/article_attachments/4404901170199/btn_copy.gif)****Copy**  
   Copies the selected text in the editing panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/4404909152023/btn_paste.gif)**Paste**  
   Pastes the text that was previously cut or copied in the editing panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404901170455/btn_delete.gif)**Delete**  
   Deletes the selected text in the editing panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404909152279/btn_undo.gif)**Undo**  
   Undoes an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404901170967/btn_redo.gif)**Redo**  
   Cancels undoing an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404901116183/btn_fnd.gif)**Search**  
   Searches for text in the editing panel, and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404901161623/btn_check.gif)**Check**  
   Tests the syntax of your function. If the syntax is incorrect, JReport gives the opportunity to correct the errors.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404909145879/btn_bkmrk.gif)**Add Bookmark**  
   Adds a bookmark to a specific position.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404901171223/btn_prvs.gif)**Go to Previous Bookmark**  
   Goes to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404901171479/btn_nxt.gif)**Go to Next Bookmark**  
   Goes to the next bookmark.
* ![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4404901171735/btn_clear.gif)**Clear All Bookmarks**  
   Clears all of the bookmarks.
* ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4404901161367/btn_cmtuncmnt.gif)**Comment/Uncomment**  
   Adds or removes comments.
* ![Add Operators button](https://devnet.logianalytics.com/hc/article_attachments/4404901171991/btn_cmptdclmn.gif)**Add Operators**  
   Selects a general operator to be used in the editing panel.
* ![Color Converter button](https://devnet.logianalytics.com/hc/article_attachments/4404901172247/btn_color.gif)**Color Converter**  
   A color palette is provided for you to insert the HEX code of a color.

**Fields panel**

Displays a list of fields that are available to functions. Those fields may contain table columns, business view elements, formulas, summaries, parameters and special fields. Select one field and double-click it to insert it into the editing panel at the insertion point.

**Functions panel**

Displays a list of the JReport built-in functions and user defined functions that are available to functions. When you select one function and double-click it, JReport will insert the selected function into the editing panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

**Operators panel**

Displays a list of the operators that are available to functions. Select one operator and double-click it to insert it into the editing panel at the insertion point.

**Function text panel**

In this panel, you can build and edit your function. There are several ways to work with functions:

* Select function components from the Fields, Functions and Operators panels, and then double-click the components, JReport will then insert them in the function;
* Type your function in the editing panel directly;
* Use the above two methods together;
* Paste function text from the text document of other programs.

The line numbers of the function are marked in the left of the panel to help you check it easily.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032942-Update-Procedures-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog)
