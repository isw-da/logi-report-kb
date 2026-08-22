---
title: "Crosstab Formula Editor Dialog Box"
id: 5735522106391
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735522106391-Crosstab-Formula-Editor-Dialog-Box
updated_at: 2022-11-02T08:16:30Z
---

# Crosstab Formula Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735508437271-Create-Table-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735528674583-Crosstab-Wizard-Dialog-Box)

# Crosstab Formula Editor Dialog Box

You can use the Crosstab Formula Editor dialog box to [compose crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735520960151-Using-Crosstab-Formulas), which you can use to apply custom aggregate functions in a crosstab in a page or ![This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898419617559/___newv19.1.png "New for version 19.1.")web report or control properties of the crosstab. This topic describes the options in the dialog box.

Designer displays the Crosstab Formula Editor dialog box when you do any of the following:

* In the Resources box of the crosstab wizard, select <New Crosstab Formula...> under the Crosstab Formulas node, type a name for the new crosstab formula and select OK.
* Select a crosstab component, then in the Data panel, select <New Crosstab Formula...> under the Crosstab Formulas node, type a name for the new crosstab formula and select OK.
* Right-click a crosstab formula in the Data panel and select Edit Formula on the shortcut menu.
* Select <New Crosstab Formula...> in the property value list when editing some properties of a crosstab or an object in the crosstab in the Report Inspector.

![Crosstab Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/9898532931991/crstbfmlaedtr.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The following describes all the options Designer provides in the Crosstab Formula Editor dialog box. Some of them are not available when you are working with a business view-based crosstab.

**Menu**

* **File**
  + **New Formula**  
    Select to create another formula in the catalog![This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898419617559/___newv19.1.png "New for version 19.1.")or dynamic formula in the current report.
  + **New Summary**  
    Select to open the [New Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524043927-New-Summary-Dialog-Box) to create a summary in the catalog.
  + **New Parameter**  
    Select to open the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box) to create a parameter in the catalog.
  + **Import UDF Classes**  
    Select to open the [UDF Classes dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567794839-UDF-Classes-Dialog-Box) to import user-defined formula classes.
  + **Save**  
    Select to save the crosstab formula.
  + **Save As**  
    Select to save the crosstab formula as a new crosstab formula by specifying a new name.
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
    Select to test the syntax of the crosstab formula.
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
    Select to enable automatic insertion of the other part of a sign pair right after you type the first part when you edit the crosstab formula.
  + **Formula References**  
    Select to show the formulas that reference the selected UDF function in the Functions panel.
  + **Properties**  
    Select to edit properties of the crosstab formula in the Formula Properties dialog box.
    - **Data Type**  
      This property shows the data type of the crosstab formula's return value.
    - **Precision**  
      Specify the precision of the crosstab formula's return value. When you set the precision to 0, Logi Report Engine displays all characters of the return value; when you set it to N, Logi Report Engine only displays the first N characters.
    - **Scale**  
      Specify the number of digits to the right of the decimal point for the crosstab formula's return value.
* **Help**  
  Select to view information about the dialog box.

**Toolbar**

* **New Formula**  
  Select to create another formula in the catalog![This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898419617559/___newv19.1.png "New for version 19.1.")or dynamic formula in the current report.
* **New Summary**  
  Select to create a summary in the catalog.
* **New Parameter**  
  Select to create a parameter in the catalog.
* **Save**  
  Select to save the crosstab formula.
* **Save As**  
  Select to save the crosstab formula as a new crosstab formula by specifying a new name.
* **Properties**  
  Select to show properties of the crosstab formula in the Formula Properties dialog box.
  + **Data Type**  
    This property shows the data type of the return value of the crosstab formula.
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

**Fields panel**

This panel displays the fields that you can reference in the crosstab formula, such as DBFields, parameters, other formulas, and special fields. These fields vary depending on the data resource type of the crosstab, query resource or business view. Select one field and double-click it to insert the field into the formula expression panel at the insertion point.

**Functions panel**

This panel displays the [Logi Report built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions) and imported [user-defined formula functions](https://devnet.logianalytics.com/hc/en-us/articles/5735545091095-Using-User-Defined-Formula-Functions) that you can apply in the crosstab formula. Select one function and double-click it, Designer then inserts the function into the formula expression panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

**Operators panel**

This panel displays the [Logi Report built-in operators](https://devnet.logianalytics.com/hc/en-us/articles/5735511732247-Appendix-2-Formula-Operators) that you can apply in the crosstab formula. Select one operator and double-click it to insert the operator into the formula expression panel at the insertion point.

**Formula expression panel**

You can edit your crosstab formula in this panel. There are several ways to work with a crosstab formula:

* Select an object from the Fields, Functions, or Operators panel and double-click it, Designer then inserts the object in the crosstab formula.
* Type your crosstab formula in the panel directly.
* Use the preceding two methods together.
* Paste crosstab formula text from the text document of other programs.

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
  Select to test the syntax of the crosstab formula.
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735508437271-Create-Table-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735528674583-Crosstab-Wizard-Dialog-Box)
