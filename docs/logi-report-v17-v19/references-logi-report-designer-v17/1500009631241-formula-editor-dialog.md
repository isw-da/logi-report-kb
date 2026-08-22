---
title: "Formula Editor Dialog"
id: 1500009631241
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631241-Formula-Editor-Dialog
updated_at: 2021-07-24T16:04:39Z
---

# Formula Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608702-Format-Wall-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608742-Geographic-Map-Wizard-Dialog)

# Formula Editor Dialog

The Formula Editor helps you to write a formula using the available resources, which may be [used generally in Logi Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009634201-Creating-Formulas-in-a-Catalog#Predefine), as a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula)  in the current report, or as a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009613122-Business-View-Elements#CA) in a business view, or edit an expression using the available resources to [control the value of a property](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties). It appears when you do one of the following:

* In the Catalog Manager, right-click the Formulas node, select New Formula from the shortcut menu, type a name for the new formula and then select OK, or right-click a formula and select Edit on its shortcut menu.
* Select the <New Formula…> or <Edit Expression...> item where a formula list is provided.
* Select the Settings button in the General tab of the [New View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009632741-New-View-Element-Dialog) dialog or [Edit View Element](https://devnet.logianalytics.com/hc/en-us/articles/1500009630941-Edit-View-Element-Dialog) dialog.

![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904223895/fmlaedtr.gif)

The following lists all the options that are provided in the editor. Some of them are not available depending on where the editor is opened.

**Menu**

* **File**
  + **New Formula**  
    Creates a new formula.
  + **New Summary**  
    Opens the [New Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009609362-New-Summary-Dialog) dialog to create a new summary.
  + **New Parameter**  
    Opens the [New Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009632681-New-Parameter-Dialog) dialog to create a new parameter.
  + **Import UDF Classes**  
     Opens the [UDF Classes](https://devnet.logianalytics.com/hc/en-us/articles/1500009610702-UDF-Classes-Dialog) dialog to import user defined formula classes.
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
    Brings out the [Find/Replace](https://devnet.logianalytics.com/hc/en-us/articles/1500009608722-Find-Replace-Dialog) dialog. You can then search for text in the editing panel, and replace the found text with different text.
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
    Tests the syntax of your formula. If the syntax is incorrect, Logi Report gives the opportunity to correct the errors.
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
    A [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) is provided for you to insert the HEX code of a color.
  + **Auto Finish**  
    Enables the automatic input of the other part of a sign pair right after you type in the first part when editing formulas.
  + **Formula References**  
    Shows the formulas that reference the selected UDF method in the Functions panel.
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
* **Fields Panel**  
  Specifies whether to show the Fields panel.
* **Functions Panel**  
  Specifies whether to show the Functions panel.
* **Operators Panel**  
  Specifies whether to show the Operators panel.
* **Help**  
  Displays the help document about this feature.
* **Use As**  
  Available when it is a dynamic formula. It specifies to use the formula as one of the following [view element types](https://devnet.logianalytics.com/hc/en-us/articles/1500009613122-Business-View-Elements): Group, Detail, or Aggregation. When you are creating a dynamic formula, the default value is blank which means that Logi Report will decide whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object.
* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/4404904233879/btn_cut.gif)**Cut**  
  Cuts the selected text in the editing panel.
* ![Copy button](https://devnet.logianalytics.com/hc/article_attachments/4404911675159/btn_copy.gif)**Copy**  
  Copies the selected text in the editing panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/4404911675415/btn_paste.gif)**Paste**  
   Pastes the text that was previously cut or copied in the editing panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404911675799/btn_delete.gif)**Delete**  
  Deletes the selected text in the editing panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404904234135/btn_undo.gif)**Undo**  
  Undoes an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404904234391/btn_redo.gif)**Redo**  
  Cancels undoing an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404904167319/btn_fnd.gif)**Search**  
  Searches for text in the editing panel, and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404911667223/btn_check.gif)**Check**  
   Tests the syntax of your formula. If the syntax is incorrect, Logi Report gives the opportunity to correct the errors.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404911666967/btn_bkmrk.gif)**Add Bookmark**  
   Adds a bookmark to a specific position.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404904234647/btn_prvs.gif)**Go to Previous Bookmark**  
  Goes to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404911676055/btn_nxt.gif)**Go to Next Bookmark**  
   Goes to the next bookmark.
* ![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4404904234903/btn_clear.gif)**Clear All Bookmarks**  
  Clears all of the bookmarks.
* ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4404911666583/btn_cmtuncmnt.gif)**Comment/Uncomment**  
   Adds or removes comments.
* ![Add Operators button](https://devnet.logianalytics.com/hc/article_attachments/4404911676311/btn_cmptdclmn.gif)**Add Operators**  
  Selects a general operator to be used in the editing panel.
* ![Color Converter button](https://devnet.logianalytics.com/hc/article_attachments/4404911676567/btn_color.gif)**Color Converter**  
  A color palette is provided for you to insert the HEX code of a color.

**Fields panel**

Displays a list of fields that are available to formulas. Those fields may contain table columns, business view elements, formulas, summaries, parameters and special fields. Select one field and double-click it to insert it into the editing panel at the insertion point.

**Functions panel**

Displays a list of the Logi Report built-in functions and user defined functions that are available to formulas. When you select one function and double-click it, Logi Report will insert the selected function into the editing panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

**Operators panel**

Displays a list of the operators that are available to formulas. Select one operator and double-click it to insert it into the editing panel at the insertion point.

**Formula text panel**

In this panel, you can build and edit your formula. There are several ways to work with formula:

* Select formula components from the Fields, Functions and Operators panels, and then double-click the components, Logi Report will then insert them in the formula;
* Type your formula in the editing panel directly;
* Use the above two methods together;
* Paste formula text from the text document of other programs.

The line numbers of the formula are marked in the left of the panel to help you check it easily.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608702-Format-Wall-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608742-Geographic-Map-Wizard-Dialog)
