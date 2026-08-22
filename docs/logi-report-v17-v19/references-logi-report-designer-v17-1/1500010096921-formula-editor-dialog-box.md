---
title: "Formula Editor Dialog Box"
id: 1500010096921
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096921-Formula-Editor-Dialog-Box
updated_at: 2021-12-28T11:39:55Z
---

# Formula Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097341-Format-Wall-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059462-Geographic-Map-Wizard-Dialog-Box)

# Formula Editor Dialog Box

You can use the Formula Editor dialog box to write a [formula in a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010060982-Creating-Formulas-in-a-Catalog#Predefine), a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500010101081-Business-View-Elements#CA) in a business view, or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) in the current report; or use it to edit an expression to [control the value of a property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties). This topic describes the options in the dialog box.

Designer displays the Formula Editor dialog box when you do one of the following:

* In the Catalog Manager, right-click the Formulas node, select New Formula from the shortcut menu, type a name for the new formula and then select OK, or right-click a formula and select Edit from the shortcut menu.
* In the Data panel, right-click a formula and select Edit Formula from the shortcut menu.
* Select the <New Formula…> or <Edit Expression...> item where a formula list is provided.
* Select the Settings button in the General tab of the [New View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098101-New-View-Element-Dialog-Box) or [Edit View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058882-Edit-View-Element-Dialog-Box).

![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404848471703/fmlaedtr.gif)

The following lists all the options that Designer provides in the dialog box. Some of them are not available depending on where you open the dialog box.

**Menu**

* **File**
  + **New Formula**  
    Select to create another formula.
  + **New Summary**  
    Select to open the [New Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098061-New-Summary-Dialog-Box) to create a summary.
  + **New Parameter**  
    Select to open the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098041-New-Parameter-Dialog-Box) to create a parameter.
  + **Import UDF Classes**  
    Select to open the [UDF Classes dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099081-UDF-Classes-Dialog-Box) to import user-defined formula classes.
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
    Select to open the [Find/Replace dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097361-Find-Replace-Dialog-Box). You can then search for text in the editing panel, and replace the found text with different text.
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
    Select to open the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) to insert the HEX code of a color.
  + **Auto Finish**  
    Select to enable the automatic input of the other part of a sign pair right after you type in the first part when editing the formula.
  + **Formula References**  
    Select to show the formulas that reference the selected UDF function in the Functions panel.
  + **Properties**  
    Select to show the properties of the formula in the Formula Properties dialog box.
    - **Data Type**  
      The property shows the data type of the return value of the formula.
    - **Precision**  
      Specify the precision of the return value of the formula. If the precision is set to 0, all characters of the return value will be displayed; if it is set to N, only the first N characters will be displayed.
    - **Scale**  
      Specify the number of digits to the right of the decimal point for the return value of the formula.
* **Help**  
  Select to view information about the dialog box.

**Toolbar**

* **New Formula**  
  Select to create a crosstab formula.
* **New Summary**  
  Select to create a summary.
* **New Parameter**  
  Select to create a parameter.
* **Save**  
  Select to save the formula.
* **Save As**  
  Select to save the formula as a new formula by specifying a new name.
* **Properties**  
  Select to show the properties of the crosstab formula in the Formula Properties dialog box.
  + **Data Type**  
    The property shows the data type of the return value of the crosstab formula.
  + **Precision**  
    Specify the precision of the return value of the crosstab formula. If the precision is set to 0, all characters of the return value will be displayed; if it is set to N, only the first N characters will be displayed.
  + **Scale**  
    Specify the number of digits to the right of the decimal point for the return value of the crosstab formula.
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
  Designer displays the option when you use the dialog box for a dynamic formula. You can use it to specify to use the formula as one of the following [view element types](https://devnet.logianalytics.com/hc/en-us/articles/1500010101081-Business-View-Elements): Group, Detail, or Aggregation. When you are creating a dynamic formula, the default value is blank which means that Designer decides whether the formula can be used as an aggregation object; if not, Designer uses the formula as a detail object.
* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/4404856883351/btn_cut.gif)**Cut**  
  Select to cut the specified text in the editing panel.
* ![Copy button](https://devnet.logianalytics.com/hc/article_attachments/4404848484631/btn_copy.gif)**Copy**  
  Select to copy the specified text in the editing panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/4404848485015/btn_paste.gif)**Paste**  
  Select to paste the text that you cut or copied in the editing panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404848485271/btn_delete.gif)**Delete**  
  Select to delete the specified text in the editing panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404856883863/btn_undo.gif)**Undo**  
  Select to undo an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404856884119/btn_redo.gif)**Redo**  
  Select to redo an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404848376087/btn_fnd.gif)**Search**  
  Select to open the Find/Replace dialog box to search for text in the editing panel, and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404856870295/btn_check.gif)**Check**  
  Select to test the syntax of the crosstab formula. If the syntax is incorrect, Designer gives you the opportunity to correct the errors.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404856870039/btn_bkmrk.gif)**Add Bookmark**  
  Select to add a bookmark to a specific position.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404856887575/btn_prvs.gif)**Go to Previous Bookmark**  
  Select to go to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404848485655/btn_nxt.gif)**Go to Next Bookmark**  
  Select to go to the next bookmark.
* ![Clear All Bookmarks button](https://devnet.logianalytics.com/hc/article_attachments/4404848485911/btn_clear.gif)**Clear All Bookmarks**  
  Select to clear all of the bookmarks.
* ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4404856869783/btn_cmtuncmnt.gif)**Comment/Uncomment**  
  Select to add or remove comments.
* ![Add Operators button](https://devnet.logianalytics.com/hc/article_attachments/4404848486295/btn_cmptdclmn.gif)**Add Operators**  
  Select to add a general operator in the editing panel.
* ![Color Converter button](https://devnet.logianalytics.com/hc/article_attachments/4404848486551/btn_color.gif)**Color Converter**  
  Select to open the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) to insert the HEX code of a color.

**Fields panel**

The panel displays a list of fields that are available to formulas. Those fields may contain table columns, business view elements, formulas, summaries, parameters, and special fields. Select one field and double-click it to insert it into the editing panel at the insertion point.

**Functions panel**

The panel displays a list of the [Logi Report built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions) and imported user [defined formula functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010099441-Using-User-Defined-Formula-Functions) that are available to formulas. When you select one function and double-click it, Designer inserts the selected function into the editing panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

**Operators panel**

The panel displays a list of the [Logi Report built-in operators](https://devnet.logianalytics.com/hc/en-us/articles/1500010093981-Appendix-2-Formula-Operators) that are available to formulas. Select one operator and double-click it to insert it into the editing panel at the insertion point.

**Formula text panel**

You can edit your formula in this panel. There are several ways to work with formula:

* Select formula components from the Fields, Functions, and Operators panels, and then double-click the components, Designer then inserts them in the formula.
* Type your formula in the editing panel directly.
* Use the above two methods together.
* Paste formula text from the text document of other programs.

Designer marks the line numbers of the formula in the left of the panel to help you check it easily.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097341-Format-Wall-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059462-Geographic-Map-Wizard-Dialog-Box)
