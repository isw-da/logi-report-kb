---
title: "Crosstab Formula Editor Dialog"
id: 1500010030042
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010030042-Crosstab-Formula-Editor-Dialog
updated_at: 2021-07-24T10:39:05Z
---

# Crosstab Formula Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065141-Create-Table-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065081-Crosstab-Wizard-Dialog)

# Crosstab Formula Editor Dialog

The Crosstab Formula Editor helps you to create custom aggregate functions in a crosstab using c[rosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010063701-Using-Crosstab-Formulas). It appears when you select a crosstab component, on the Data panel select <New Crosstab Formula...> under the Crosstab Formulas node, enter a name for the new crosstab formula and then select OK, or right-click a crosstab formula and select Edit Formula on its shortcut menu.

![Crosstab Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404901287703/crstbfmlaedtr.gif)

The following are details about options in the editor:

**Menu**

* **File**
  + **New Formula**  
     Creates a new formula.
  + **New Summary**  
     Opens the [New Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010031922-New-Summary-Dialog) dialog to create a new summary.
  + **New Parameter**  
     Opens the [New Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010067241-New-Parameter-Dialog) dialog to create a new parameter.
  + **Import UDF Classes**  
     Opens the [UDF Classes](https://devnet.logianalytics.com/hc/en-us/articles/1500010032882-UDF-Classes-Dialog) dialog to import user defined formula classes.
  + **Save**  
     Saves the crosstab formula to the Formulas node.
  + **Save As**  
     Saves the crosstab formula as a new crosstab formula by specifying a new name.
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
* **Formula**
  + **Check**  
     Tests the syntax of your crosstab formula. If the syntax is incorrect, Logi JReport gives the opportunity to correct the errors.
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
     A [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) is provided for you to insert the HEX code of a color.
  + **Auto Finish**  
     Enables the automatic input of the other part of a sign pair right after you type in the first part when editing crosstab formula.
  + **Formula References**  
     Shows the formulas that reference the selected UDF function in the Functions panel.
  + **Properties**  
     Shows properties of the crosstab formula in the Formula Properties dialog.
    - **Data Type**  
       The data type of the returned value of the crosstab formula.
    - **Precision**  
       The precision of the returned value of the crosstab formula. If the precision is set to 0, all characters of the returned value will be displayed; if it is set to N, only the first N characters will be displayed.
    - **Scale**  
       The number of digits to the right of the decimal point for the returned value of the crosstab formula.
* **Help**  
   Displays the help document about this feature.

**Toolbar**

* **New Formula**  
   Creates a new crosstab formula.
* **New Summary**  
   Creates a new summary.
* **New Parameter**  
   Creates a new parameter.
* **Save**  
   Saves the formula to the Formulas node.
* **Save As**  
   Saves the formula as a new formula by specifying a new name.
* **Properties**  
   Specifies the precision and scale properties of the crosstab formula.
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
* **![Cut button](https://devnet.logianalytics.com/hc/article_attachments/4404901169943/btn_cut.gif) Cut**  
   Cuts the selected text in the editing panel.
* **![Copy button](https://devnet.logianalytics.com/hc/article_attachments/4404901170199/btn_copy.gif) Copy**  
   Copies the selected text in the editing panel.
* **![Paste button](https://devnet.logianalytics.com/hc/article_attachments/4404909152023/btn_paste.gif) Paste**  
   Pastes the text that was previously cut or copied in the editing panel.
* **![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404901170455/btn_delete.gif) Delete**  
   Deletes the selected text in the editing panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404909152279/btn_undo.gif)**Undo**  
   Undoes an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404901170967/btn_redo.gif)**Redo**  
   Cancels undoing an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404901116183/btn_fnd.gif)**Search**  
   Searches for text in the editing panel, and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404901161623/btn_check.gif)**Check**  
   Tests the syntax of your crosstab formula. If the syntax is incorrect, Logi JReport gives the opportunity to correct the errors.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404909145879/btn_bkmrk.gif)**Add Bookmark**  
   Adds a bookmark to a specific position.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404901171223/btn_prvs.gif)**Go to Previous Bookmark**  
   Goes to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404901171479/btn_nxt.gif)**Go to Next Bookmark**  
   Goes to the next bookmark.
* ![Clear All Bookmarks button](https://devnet.logianalytics.com/hc/article_attachments/4404901171735/btn_clear.gif)**Clear All Bookmarks**  
   Clears all of the bookmarks.
* ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4404901161367/btn_cmtuncmnt.gif)**Comment/Uncomment**  
   Adds or removes comments.
* ![Add Operators button](https://devnet.logianalytics.com/hc/article_attachments/4404901171991/btn_cmptdclmn.gif)**Add Operators**  
   Selects a general operator to be used in the editing panel.
* ![Color Converter button](https://devnet.logianalytics.com/hc/article_attachments/4404901172247/btn_color.gif)**Color Converter**  
   A color palette is provided for you to insert the HEX code of a color.

**Fields panel**

Displays a list of those fields that are available for crosstab formulas. Those fields contain table columns, formulas, parameters, special fields and other crosstab formulas. Select one field and double-click it to insert it into the editing panel at the insertion point.

**Functions panel**

Displays a list of the [Logi JReport built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010028442-Appendix-1-Formula-Functions) and imported user [defined formula functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010033242-User-Defined-Formula-Functions) that are available for crosstab formulas. When you select one function and double-click it, Logi JReport will insert the selected function into the editing panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

**Operators panel**

Displays a list of the [Logi JReport built-in operators](https://devnet.logianalytics.com/hc/en-us/articles/1500010063101-Appendix-2-Formula-Operators) that are available for crosstab formulas. Select one operator and double-click it to insert the selected operator into the editing panel at the insertion point.

**Formula text panel**

In this panel, you can build and edit your crosstab formula. There are several ways to work with crosstab formula:

* Select formula components from the Fields, Functions and Operators panels on the top of Crosstab Formula Editor, and then double-click the components, Logi JReport will then insert them in the crosstab formula;
* Type your crosstab formula in the editing panel directly;
* Use the above two methods together;
* Paste crosstab formula text from the text document of other programs.

The line numbers of the crosstab formula are marked in the left of the panel to help you check it easily.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065141-Create-Table-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065081-Crosstab-Wizard-Dialog)
