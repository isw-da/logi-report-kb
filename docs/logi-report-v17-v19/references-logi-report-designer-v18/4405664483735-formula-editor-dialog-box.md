---
title: "Formula Editor Dialog Box"
id: 4405664483735
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664483735-Formula-Editor-Dialog-Box
updated_at: 2022-01-27T20:38:22Z
---

# Formula Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661603607-Format-Wall-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664512151-Geographic-Map-Wizard-Dialog-Box)

# Formula Editor Dialog Box

You can use the Formula Editor dialog box to write a [formula in a catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661763223-Creating-Formulas-in-a-Catalog#Predefine), a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/4405661913239-Business-View-Elements#CA) in a business view, or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/4405661937559-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) in the current report; or use it to edit an expression to [control the value of a property](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties). This topic describes the options in the dialog box.

Designer displays the Formula Editor dialog box when you do one of the following:

* In the Catalog Manager, right-click the Formulas node, select New Formula from the shortcut menu, type a name for the new formula and then select OK, or right-click a formula and select Edit from the shortcut menu.
* In the Data panel, right-click a formula and select Edit Formula from the shortcut menu.
* Select <New Formula…> or <Edit Expression...> where a formula list is available.
* Select Settings in the General tab of the [New View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661660823-New-View-Element-Dialog-Box) or [Edit View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661533079-Edit-View-Element-Dialog-Box).

![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4420402380311/fmlaedtr.gif)

The following shows all the options that Designer provides in the dialog box. Some of them are not available depending on where you open the dialog box.

**Menu**

* **File**
  + **New Formula**  
    Select to create another formula.
  + **New Summary**  
    Select to open the [New Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664535575-New-Summary-Dialog-Box) to create a summary.
  + **New Parameter**  
    Select to open the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661658135-New-Parameter-Dialog-Box) to create a parameter.
  + **Import UDF Classes**  
    Select to open the [UDF Classes dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664590231-UDF-Classes-Dialog-Box) to import user-defined formula classes.
  + **Save**  
    Select to save the formula.
  + **Save As**  
    Select to save the formula with a different name.
  + **Close**  
    Select to close the dialog box.
* **Edit**
  + **Undo**  
    Select to undo an action.
  + **Redo**  
    Select to redo an action.
  + **Cut**  
    Select to cut the specified text in the editing panel.
  + **Copy**  
    Select to copy the specified text in the editing panel.
  + **Paste**  
    Select to paste the text that you cut or copied in the editing panel.
  + **Delete**  
    Select to delete the specified ted text in the editing panel.
  + **Search**  
    Select to open the [Find/Replace dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661604631-Find-Replace-Dialog-Box) to search for text in the editing panel and replace the found text with different text.
* **View**
  + **Fields Panel**  
    Select to show the Fields panel.
  + **Functions Panel**  
    Select to show the Functions panel.
  + **Operators Panel**  
    Select to show the Operators panel.
  + **Sort Tree**  
    Select to sort the functions in the Functions panel and fields in the Fields panel by names.
* **Formula**
  + **Check**  
    Select to test the syntax of your formula. If the syntax is incorrect, Designer gives the opportunity to correct the errors.
  + **Add Bookmark**  
    Select to add a bookmark to a specific position.
  + **Go to Previous Bookmark**  
    Select to go to the previous bookmark.
  + **Go to Next Bookmark**  
    Select to go to the next bookmark.
  + **Clear all Bookmarks**  
    Select to clear all of the bookmarks.
  + **Comment/Uncomment**  
    Select to add or remove comments.
  + **Add Operators**  
    Select to add a general operator in the editing panel.
  + **Color Converter**  
    Select to open the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) to insert the HEX code of a color.
  + **Auto Finish**  
    Select to enable the automatic input of the other part of a sign pair right after you type in the first part when editing the formula.
  + **Formula References**  
    Select to show the formulas that reference the selected UDF function in the Functions panel.
  + **Properties**  
    Select to show properties of the formula in the Formula Properties dialog box.
    - **Data Type**  
      This property shows the data type of the return value of the formula.
    - **Precision**  
      Specify the precision of the return value of the formula. If the precision is set to 0, all characters of the return value will be displayed; if it is set to N, only the first N characters will be displayed.
    - **Scale**  
      Specify the number of digits to the right of the decimal point for the return value of the formula.
* **Help**  
  Select to view information about the dialog box.

**Toolbar**

* **New Formula**  
  Select to create a formula.
* **New Summary**  
  Select to create a summary.
* **New Parameter**  
  Select to create a parameter.
* **Save**  
  Select to save the formula.
* **Save As**  
  Select to save the formula as a new formula by specifying a new name.
* **Properties**  
  Select to show properties of the formula in the Formula Properties dialog box.
  + **Data Type**  
    This property shows the data type of the return value of the formula.
  + **Precision**  
    Specify the precision of the return value of the formula. If the precision is set to 0, all characters of the return value will be displayed; if it is set to N, only the first N characters will be displayed.
  + **Scale**  
    Specify the number of digits to the right of the decimal point for the return value of the formula.
* **Sort Tree**  
  Select to sort the functions in the Functions panel and fields in the Fields panel by names.
* **Fields Panel**  
  Select to show the Fields panel.
* **Functions Panel**  
  Select to show the Functions panel.
* **Operators Panel**  
  Select to show the Operators panel.
* **Help**  
  Select to view information about the dialog box.
* **Use As**  
  Designer displays this option when you use the dialog box for a dynamic formula. You can use it to specify to use the formula as one of the following [view element types](https://devnet.logianalytics.com/hc/en-us/articles/4405661913239-Business-View-Elements): Group, Detail, or Aggregation.
* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/4420394717463/btn_cut.gif)**Cut**  
  Select to cut the specified text in the editing panel.
* ![Copy button](https://devnet.logianalytics.com/hc/article_attachments/4420402389271/btn_copy.gif)**Copy**  
  Select to copy the specified text in the editing panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/4420410654871/btn_paste.gif)**Paste**  
  Select to paste the text that you cut or copied in the editing panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420402389527/btn_delete.gif)**Delete**  
  Select to delete the specified text in the editing panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4420402389783/btn_undo.gif)**Undo**  
  Select to undo an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4420402390039/btn_redo.gif)**Redo**  
  Select to redo an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420394638743/btn_fnd.gif)**Search**  
  Select to open the [Find/Replace dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661604631-Find-Replace-Dialog-Box) to search for text in the editing panel and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4420402321943/btn_check.gif)**Check**  
  Select to test the syntax of the formula. If the syntax is incorrect, Designer gives you the opportunity to correct the errors.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4420394645143/btn_bkmrk.gif)**Add Bookmark**  
  Select to add a bookmark to a specific position.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4420410655255/btn_prvs.gif)**Go to Previous Bookmark**  
  Select to go to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4420402390423/btn_nxt.gif)**Go to Next Bookmark**  
  Select to go to the next bookmark.
* ![Clear All Bookmarks button](https://devnet.logianalytics.com/hc/article_attachments/4420394718231/btn_clear.gif)**Clear All Bookmarks**  
  Select to clear all of the bookmarks.
* ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4420394644887/btn_cmtuncmnt.gif)**Comment/Uncomment**  
  Select to add or remove comments.
* ![Add Operators button](https://devnet.logianalytics.com/hc/article_attachments/4420402390679/btn_cmptdclmn.gif)**Add Operators**  
  Select to add a general operator in the editing panel.
* ![Color Converter button](https://devnet.logianalytics.com/hc/article_attachments/4420394718487/btn_color.gif)**Color Converter**  
  Select to open the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) to insert the HEX code of a color.

**Fields panel**

This panel displays the fields that you can reference in the formula. These fields may contain table columns, business view elements, formulas, summaries, parameters, and special fields. Select one field and double-click it to insert it into the editing panel at the insertion point.

**Functions panel**

This panel displays the [Logi Report built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/4405664357143-Appendix-1-Formula-Functions) and imported [user-defined formula functions](https://devnet.logianalytics.com/hc/en-us/articles/4405661765527-Using-User-Defined-Formula-Functions) that you can use to compose formulas. When you select one function and double-click it, Designer inserts the selected function into the editing panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

**Operators panel**

This panel displays the [Logi Report built-in operators](https://devnet.logianalytics.com/hc/en-us/articles/4405661327255-Appendix-2-Formula-Operators) that you can use to compose formulas. Select one operator and double-click it to insert it into the editing panel at the insertion point.

**Formula text panel**

You can edit your formula in this panel. There are several ways to work with formula:

* Select an object from the Fields, Functions, and Operators panels, and then double-click the object, Designer then inserts it in the formula.
* Type your formula in the editing panel directly.
* Use the preceding two methods together.
* Paste formula text from the text document of other programs.

Designer marks the line numbers of the formula in the left of the panel to help you check it easily.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661603607-Format-Wall-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664512151-Geographic-Map-Wizard-Dialog-Box)
