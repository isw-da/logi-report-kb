---
title: "User Defined Function Editor Dialog Box"
id: 1500010099101
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099101-User-Defined-Function-Editor-Dialog-Box
updated_at: 2021-07-23T19:16:06Z
---

# User Defined Function Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060802-Update-Procedures-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box)

# User Defined Function Editor Dialog Box

The User Defined Function Editor dialog box helps you to [write a user-defined function (UDF)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099441-Using-User-Defined-Formula-Functions) which can be called in a formula or another user-defined function. It appears when you do either of the following:

* In the Catalog Manager, right-click the User Defined Functions node, select New Function on the shortcut menu, type a name for the new function and then select OK, or right-click a UDF and select Edit from the shortcut menu.
* In the Data panel, right-click a UDF and select Edit from the shortcut menu.
* Select <New Function…> under the User Defined Functions node where a formula list is provided.

![User Defined Function Editor](https://devnet.logianalytics.com/hc/article_attachments/4404856869399/udfedtr.gif)

The following lists all the options that are provided in the editor. Some of them are not available depending on where the editor is opened.

**Menu**

* **File**
  + **New Function**  
    Creates a new function.
  + **New Summary**  
    Opens the [New Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098061-New-Summary-Dialog-Box) to create a new summary.
  + **New Parameter**  
    Opens the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098041-New-Parameter-Dialog-Box) to create a new parameter.
  + **Import UDF Classes**  
    Opens the [UDF Classes dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099081-UDF-Classes-Dialog-Box) to import user-defined formula classes.
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
    Brings out the [Find/Replace dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097361-Find-Replace-Dialog-Box). You can then search for text in the editing panel, and replace the found text with different text.
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
    Tests the syntax of your function. If the syntax is incorrect, Logi Report gives the opportunity to correct the errors.
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
    A [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) is provided for you to insert the HEX code of a color.
  + **Auto Finish**  
     Enables the automatic input of the other part of a sign pair right after you type in the first part when editing functions.
  + **User Defined Function References**  
    Shows the user-defined functions that reference the selected UDF method in the Functions panel.
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
* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/4404856883351/btn_cut.gif)**Cut**  
  Cuts the selected text in the editing panel.
* ![Copy button](https://devnet.logianalytics.com/hc/article_attachments/4404848484631/btn_copy.gif)**Copy**  
  Copies the selected text in the editing panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/4404848485015/btn_paste.gif)**Paste**  
  Pastes the text that was previously cut or copied in the editing panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404848485271/btn_delete.gif)**Delete**  
  Deletes the selected text in the editing panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404856883863/btn_undo.gif)**Undo**  
   Undoes an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404856884119/btn_redo.gif)**Redo**  
   Cancels undoing an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404848376087/btn_fnd.gif)**Search**  
  Searches for text in the editing panel, and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404856870295/btn_check.gif)**Check**  
   Tests the syntax of your function. If the syntax is incorrect, Logi Report gives the opportunity to correct the errors.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404856870039/btn_bkmrk.gif)**Add Bookmark**  
  Adds a bookmark to a specific position.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404856887575/btn_prvs.gif)**Go to Previous Bookmark**  
  Goes to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404848485655/btn_nxt.gif)**Go to Next Bookmark**  
  Goes to the next bookmark.
* ![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4404848485911/btn_clear.gif)**Clear All Bookmarks**  
  Clears all of the bookmarks.
* ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4404856869783/btn_cmtuncmnt.gif)**Comment/Uncomment**  
  Adds or removes comments.
* ![Add Operators button](https://devnet.logianalytics.com/hc/article_attachments/4404848486295/btn_cmptdclmn.gif)**Add Operators**  
  Selects a general operator to be used in the editing panel.
* ![Color Converter button](https://devnet.logianalytics.com/hc/article_attachments/4404848486551/btn_color.gif)**Color Converter**  
  A [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) is provided for you to insert the HEX code of a color.

**Fields panel**

Displays a list of fields that are available to functions. Those fields may contain table columns, business view elements, formulas, summaries, parameters and special fields. Select one field and double-click it to insert it into the editing panel at the insertion point.

**Functions panel**

Displays a list of the Logi Report built-in functions and user-defined functions that are available to functions. When you select one function and double-click it, Logi Report will insert the selected function into the editing panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

**Operators panel**

Displays a list of the operators that are available to functions. Select one operator and double-click it to insert it into the editing panel at the insertion point.

**Function text panel**

In this panel, you can build and edit your function. There are several ways to work with functions:

* Select function components from the Fields, Functions and Operators panels, and then double-click the components, Logi Report will then insert them in the function;
* Type your function in the editing panel directly;
* Use the above two methods together;
* Paste function text from the text document of other programs.

The line numbers of the function are marked in the left of the panel to help you check it easily.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060802-Update-Procedures-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box)
