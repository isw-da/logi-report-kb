---
title: "Formula Editor Dialog"
id: 1500009586941
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586941-Formula-Editor-Dialog
updated_at: 2021-07-24T05:55:19Z
---

# Formula Editor Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566242-Format-Wall-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587501-Geographic-Map-Wizard-Dialog-for-Library-Component-)

# Formula Editor Dialog

The Formula Editor appears when you do either of the following:

* In the Catalog Manager, right-click the Formulas node, select New Formula from the shortcut menu, input a name for the new formula and then select OK, or right-click a formula and select Edit Formula on its shortcut menu.
* In the Data panel of the Logi JReport Designer main window, or in the Resources box of the report wizard, expand the Dynamic Resources > Formulas node, select <New Formula…>.
* Select the Settings button in the General tab of the [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009588021-New-View-Element-Dialog) dialog or [Edit View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009586641-Edit-View-Element-Dialog) dialog.
* Select the <New Formula...> or <Edit Expression...> item in the value drop-down list of some properties.

It helps you to [write a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula) using the available resources, which may be used generally in Logi JReport, as a [dynamic resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) in the current web report or library component or page report based on business view, or as a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009562702-Business-View-Elements#CA) in a business view, or edit an expression using the available resources to [control the value of a property](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties). [See the editor](javascript:%20void(null)).

![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404889308567/fmlaedtr.gif)

The following lists all the options that are provided in the editor. Some of them are not available depending on where the editor is opened.

**Menu**

* **File**
  + **New Formula**  
     Creates a new formula.
  + **New Summary**  
     Opens the [New Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009566842-New-Summary-Dialog) dialog to create a new summary.
  + **New Parameter**  
     Opens the [New Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009566822-New-Parameter-Dialog) dialog to create a new parameter.
  + **Import UDF Classes**  
     Opens the [UDF Classes](https://devnet.logianalytics.com/hc/en-us/articles/1500009567802-UDF-Classes-Dialog) dialog to import user defined formula classes.
  + **Save**  
     Saves the formula.
  + **Save As**  
     Saves the formula with a different name.
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
     Brings out the [Find/Replace](https://devnet.logianalytics.com/hc/en-us/articles/1500009587461-Find-Replace-Dialog) dialog. You can then search for text in the editing panel, and replace the found text with different text.
* **View**
  + **Fields Panel**  
     Specifies whether to show the Fields panel.
  + **Functions Panel**  
     Specifies whether to show the Functions panel.
  + **Operators Panel**  
     Specifies whether to show the Operators panel.
  + **Sort Tree**  
     Sorts functions in the Functions panel and fields in the Fields panel by names.
* **Formula**
  + **Check**  
     Tests the syntax of your formula. If the syntax is incorrect, Logi JReport gives the opportunity to correct the errors.
  + **Add Bookmark**  
     Adds a bookmark to a specific position.
  + **Go to Previous Bookmark**  
     Goes to the previous bookmark.
  + **Go to Next Bookmark**  
     Goes to the next bookmark.
  + **Clear all Bookmarks**  
     Clears all of the bookmarks.
  + **Comment/Uncomment**  
     Adds or removes comments.
  + **Add Operators**  
     Specifies a general operator to be used in the editing panel.
  + **Color Converter**  
     A [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) is provided for you to insert the HEX code of a color.
  + **Auto Finish**  
     Enables the automatic input of the other part of a sign pair right after you type in the first part when editing formula.
  + **Formula References**  
     Shows the formulas that reference the selected UDF function in the Functions panel.
  + **Properties**  
     Shows properties of the formula in the Formula Properties dialog.
    - **Data Type**  
       The data type of the returned value of the formula.
    - **Precision**  
       The precision of the returned value of the formula. If the precision is set to 0, all characters of the returned value will be displayed; if it is set to N, only the first N characters will be displayed.
    - **Scale**  
       The number of digits to the right of the decimal point for the returned value of the formula.
* **Help**  
   Displays the help document about this feature.

**Toolbar**

Lists the commands on the toolbar.

* **New Formula**  
   Creates a new formula.
* **New Summary**  
   Creates a new summary.
* **New Parameter**  
   Creates a new parameter.
* **Save**  
   Saves the formula.
* **Save As**  
   Saves the formula with a different name.
* **Properties**  
   Specifies the precision and scale properties of the formula.
* **Sort Tree**  
   Sorts functions in the Functions panel and fields in the Fields panel by names.
* **Fields Panel**Specifies whether to show the Fields panel.
* **Functions Panel**  
   Specifies whether to show the Functions panel.
* **Operators Panel**  
   Specifies whether to show the Operators panel.
* **Help**  
   Displays the help document about this feature.
* **Use As**  
   Available when it is a dynamic formula. It specifies to use the formula as one of the following [view element types](https://devnet.logianalytics.com/hc/en-us/articles/1500009562702-Business-View-Elements): Group, Detail, or Aggregation. When you are creating a dynamic formula, the default value is blank which means that Logi JReport will decide whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object.
* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/4404889360919/btn_cut.gif)**Cut**  
   Cuts the selected text in the editing panel.
* **![Copy button](https://devnet.logianalytics.com/hc/article_attachments/4404889361175/btn_copy.gif)****Copy**  
   Copies the selected text in the editing panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/4404889361431/btn_paste.gif)**Paste**  
   Pastes the text that was previously cut or copied in the editing panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404893916951/btn_delete.gif)**Delete**  
   Deletes the selected text in the editing panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404893917207/btn_undo.gif)**Undo**  
   Undoes an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404893917463/btn_redo.gif)**Redo**  
   Cancels undoing an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404889283735/btn_fnd.gif)**Search**  
   Searches for text in the editing panel, and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404893838487/btn_check.gif)**Check**  
   Tests the syntax of your formula. If the syntax is incorrect, Logi JReport gives the opportunity to correct the errors.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404893838231/btn_bkmrk.gif)**Add Bookmark**  
   Adds a bookmark to a specific position.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404889361687/btn_prvs.gif)**Go to Previous Bookmark**  
   Goes to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404893917719/btn_nxt.gif)**Go to Next Bookmark**  
   Goes to the next bookmark.
* ![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4404893917975/btn_clear.gif)**Clear All Bookmarks**  
   Clears all of the bookmarks.
* ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4404893837975/btn_cmtuncmnt.gif)**Comment/Uncomment**  
   Adds or removes comments.
* ![Add Operators button](https://devnet.logianalytics.com/hc/article_attachments/4404893918231/btn_cmptdclmn.gif)**Add Operators**  
   Selects a general operator to be used in the editing panel.
* ![Color Converter button](https://devnet.logianalytics.com/hc/article_attachments/4404893918487/btn_color.gif)**Color Converter**  
   A color palette is provided for you to insert the HEX code of a color.

**Fields panel**

Displays a list of those fields that are available for formulas. Those fields may contain table columns, formulas, summaries, parameters and special fields. Select one field and double-click it to insert it into the editing panel at the insertion point.

**Functions panel**

Displays a list of Logi JReport functions and imported user defined formula functions that are available for formulas. When you select one function and double-click it, Logi JReport will insert the selected function into the editing panel at the insertion point completely with its required syntax items (parentheses, commas, and so on). For the usage of these functions, refer to section [Built-in Functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009568182-Built-in-Functions) and [User-defined Formula Functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009589721-User-Defined-Formula-Functions).

**Operators panel**

Displays a list of operators that are available for formulas. Select one operator and double-click it to insert the selected operator into the editing panel at the insertion point. For the usage of these operators, refer to section [Operators](https://devnet.logianalytics.com/hc/en-us/articles/1500009589581-Operators).

**Formula text panel**

In this panel, you can build and edit your formula. There are several ways to work with formula:

* Select formula components from the Fields, Functions and Operators panels on the top of Formula Editor, and then double-click the components, Logi JReport will then insert them in the formula;
* Type your formula in the editing panel directly;
* Use the above two methods together;
* Paste formula text from the text document of other programs.

The line numbers of the formula are marked in the left of the panel to help you check it easily.

**Related topics:**

> * [Creating a Formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula)
> * [Creating and Using Uynamic Formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic)
> * [Adding a View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009562642-Adding-and-Modifying-Elements#Element)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566242-Format-Wall-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587501-Geographic-Map-Wizard-Dialog-for-Library-Component-)
