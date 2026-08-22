---
title: "Formula Editor Dialog Box"
id: 5735565964055
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735565964055-Formula-Editor-Dialog-Box
updated_at: 2022-11-02T04:37:29Z
---

# Formula Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735551562647-Format-Wall-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514503703-Geographic-Map-Wizard-Dialog-Box)

# Formula Editor Dialog Box

You can use the Formula Editor dialog box to write a [formula in a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735525453207-Creating-Formulas-in-a-Catalog#Predefine), a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/5735576528791-Business-View-Elements#CA) in a business view, or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Formula) in the current report, to edit an expression to [control the value of a property](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties), ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")or to create the formula that defines how you want to fetch pagination data for a JSON schema. This topic describes the options in the dialog box.

Designer displays the Formula Editor dialog box when you do one of the following:

* In the Catalog Manager, right-click the Formulas node, select New Formula from the shortcut menu, type a name for the new formula and then select OK, or right-click a formula and select Edit from the shortcut menu.
* In the Data panel, right-click a formula and select Edit Formula from the shortcut menu.
* Select <New Formula…> or <Edit Expression...> where a formula list is available.
* Select Settings in the General tab of the [New View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530525975-New-View-Element-Dialog-Box) or [Edit View Element dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529270039-Edit-View-Element-Dialog-Box).
* ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")Select New Formula or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898405043607/btn_edit1.gif) in the Main Formula drop-down list in the Extract JSON Schema screen of the [JSON Connection Wizard dialog box.](https://devnet.logianalytics.com/hc/en-us/articles/5735566628631-JSON-Connection-Wizard-Dialog-Box)

![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/9898459791639/fmlaedtr.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The following describes all the options Designer provides in the Formula Editor dialog box. Some of them are not available depending on how you are going to use the formula.

**Menu**

* **File**
  + **New Formula**  
    Select to create another formula in the catalog or a dynamic formula in the current report.
  + **New Summary**  
    Select to open the [New Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524043927-New-Summary-Dialog-Box) to create a summary in the catalog.
  + **New Parameter**  
    Select to open the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box) to create a parameter in the catalog.
  + **Import UDF Classes**  
    Select to open the [UDF Classes dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567794839-UDF-Classes-Dialog-Box) to import user-defined formula classes.
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
    Select to cut the specified text in the formula expression panel.
  + **Copy**  
    Select to copy the specified text in the formula expression panel.
  + **Paste**  
    Select to paste the text that you cut or copied in the formula expression panel.
  + **Delete**  
    Select to delete the specified ted text in the formula expression panel.
  + **Search**  
    Select to open the [Find/Replace dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523419543-Find-Replace-Dialog-Box) to search for text in the formula expression panel and replace the found text with different text.
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
    Select to test the syntax of the formula.
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
    Select to add a general operator in the formula expression panel.
  + **Color Converter**  
    Select to open the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) to insert the HEX code of a color.
  + **Auto Finish**  
    Select to enable automatic insertion of the other part of a sign pair right after you type the first part when you edit the formula.
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
  Select to create another formula in the catalog or dynamic formula in the current report.
* **New Summary**  
  Select to create a summary in the catalog.
* **New Parameter**  
  Select to create a parameter in the catalog.
* **Save**  
  Select to save the formula.
* **Save As**  
  Select to save the formula as a new formula by specifying a new name.
* **Properties**  
  Select to edit properties of the formula in the Formula Properties dialog box.
  + **Data Type**  
    This property shows the data type of the formula's return value.
  + **Precision**  
    Specify the precision of the formula's return value. When you set the precision to 0, Logi Report Engine displays all characters of the return value; when you set it to N, Logi Report Engine only displays the first N characters.
  + **Scale**  
    Specify the number of digits to the right of the decimal point for the formula's return value.
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
  Designer displays this option when you use the dialog box for a dynamic formula. You can use it to specify to use the formula as one of the following [view element types](https://devnet.logianalytics.com/hc/en-us/articles/5735576528791-Business-View-Elements): Group, Detail, or Aggregation.

**Fields panel**

This panel displays the fields that you can reference in the formula, such as DBFields, parameters, other formulas, and special fields. These fields vary depending on how you are going to use the formula. Select one field and double-click it to insert the field into the formula expression panel at the insertion point.

**Functions panel**

This panel displays the [Logi Report built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions) and imported [user-defined formula functions](https://devnet.logianalytics.com/hc/en-us/articles/5735545091095-Using-User-Defined-Formula-Functions) that you can apply in the formula. Select one function and double-click it, Designer then inserts the function into the formula expression panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

**Operators panel**

This panel displays the [Logi Report built-in operators](https://devnet.logianalytics.com/hc/en-us/articles/5735511732247-Appendix-2-Formula-Operators) that you can apply in the formula. Select one operator and double-click it to insert the operator into the formula expression panel at the insertion point.

**Formula expression panel**

You can edit your formula in this panel. There are several ways to work with a formula:

* Select an object from the Fields, Functions, or Operators panel and double-click it, Designer then inserts the object in the formula.
* Type your formula in the panel directly.
* Use the preceding two methods together.
* Paste formula text from the text document of other programs.

The toolbar in this panel provides the following buttons that facilitate the process of composing a formula.

* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/9898477236631/btn_cut.gif)**Cut**  
  Select to cut the specified text in the panel.
* ![Copy button](https://devnet.logianalytics.com/hc/article_attachments/9898460197015/btn_copy.gif)**Copy**  
  Select to copy the specified text in the panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/9898477250583/btn_paste.gif)**Paste**  
  Select to paste the text that you cut or copied in the panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9898477280279/btn_delete.gif)**Delete**  
  Select to delete the specified text in the panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/9898477290263/btn_undo.gif)**Undo**  
  Select to undo an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/9898477298839/btn_redo.gif)**Redo**  
  Select to redo an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9898405034775/btn_fnd.gif)**Search**  
  Select to open the [Find/Replace dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523419543-Find-Replace-Dialog-Box) to search for text in the panel and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/9898477308823/btn_check.gif)**Check**  
  Select to test the syntax of the formula.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/9898477314839/btn_bkmrk.gif)**Add Bookmark**  
  Select to add a bookmark to a specific position.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/9898460252567/btn_prvs.gif)**Go to Previous Bookmark**  
  Select to go to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/9898477497751/btn_nxt.gif)**Go to Next Bookmark**  
  Select to go to the next bookmark.
* ![Clear All Bookmarks button](https://devnet.logianalytics.com/hc/article_attachments/9898477516951/btn_clear.gif)**Clear All Bookmarks**  
  Select to clear all of the bookmarks.
* ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/9898477526551/btn_cmtuncmnt.gif)**Comment/Uncomment**  
  Select to add or remove comments.
* ![Add Operators button](https://devnet.logianalytics.com/hc/article_attachments/9898460462999/btn_cmptdclmn.gif)**Add Operators**  
  Select to add a general operator in the panel.
* ![Color Converter button](https://devnet.logianalytics.com/hc/article_attachments/9898477556759/btn_color.gif)**Color Converter**  
  Select to open the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette) to insert the HEX code of a color.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735551562647-Format-Wall-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514503703-Geographic-Map-Wizard-Dialog-Box)
