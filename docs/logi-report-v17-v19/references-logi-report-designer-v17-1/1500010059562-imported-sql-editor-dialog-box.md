---
title: "Imported SQL Editor Dialog Box"
id: 1500010059562
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059562-Imported-SQL-Editor-Dialog-Box
updated_at: 2021-07-23T19:15:37Z
---

# Imported SQL Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059582-Import-from-Logi-Report-Server-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097541-Incremental-Condition-Dialog-Box)

# Imported SQL Editor Dialog Box

You can use the Imported SQL Editor dialog box to [create and edit imported SQLs in a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010095181-Using-Imported-SQLs). This topic describes the options in the dialog box.

Designer displays the Imported SQL Editor dialog box when you do one of the following:

* In the Catalog Manager, right-click a JDBC connection node and select Add SQL from the shortcut menu.
* In the Catalog Manager, right-click an imported SQL under the Imported SQLs node and select Update from the shortcut menu.
* In the Choose Data dialog box or report wizard when working with a query-based page report, expand the Imported SQLs node in a data source that has a JDBC connection and select <Add SQL...>.

![Imported SQL Editor](https://devnet.logianalytics.com/hc/article_attachments/4404848525079/imptdsqledtr.gif)

You see the following options in the dialog box:

**SQL Name**

Specify the name of the imported SQL when you are adding it to the catalog.

**From DB Catalog**

Specify the catalog in the database which contains the tables/views/synonyms you want to use in the imported SQL.

**Save & Exit**

Select to save the SQL statement with the specified name as an imported SQL into the catalog and exit the editor if there are no errors in the SQL statement; otherwise, Designer prompts a warning message showing the errors. You need to correct all the errors to save the SQL statement.

**Import SQL**

Select to import the SQL statement from an SQL file.

**Export SQL**

Select to export the SQL statement to an SQL file.

**Help**

Select to view information about the dialog box.

**Toolbar**

The toolbar provides the following commands that facilitate the process of composing the SQL statement.

* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/4404856883351/btn_cut.gif)**Cut**  
  Select to cut the specified text in the text panel.
* ![Copy button](https://devnet.logianalytics.com/hc/article_attachments/4404848484631/btn_copy.gif)**Copy**  
  Select to copy the specified text in the text panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/4404848485015/btn_paste.gif)**Paste**  
  Select to paste the text that you previously cut or copied in the text panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404848485271/btn_delete.gif)**Delete**  
  Select to delete the specified text from the text panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404856883863/btn_undo.gif)**Undo**  
  Select to undo an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404856884119/btn_redo.gif)**Redo**  
  Select to cancel undoing an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404848376087/btn_fnd.gif)**Search**  
  Select to search for text in the text panel, and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404856870295/btn_check.gif)**Check**  
  Select to check whether there are errors in the SQL statement.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404856870039/btn_bkmrk.gif)**Add Bookmark**  
  Select to add a bookmark to a line.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404856887575/btn_prvs.gif)**Go to Previous Bookmark**  
  Select to go to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404848485655/btn_nxt.gif)**Go to Next Bookmark**  
  Select to go to the next bookmark.
* ![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4404848485911/btn_clear.gif)**Clear All Bookmarks**  
  Select to remove all the bookmarks.

**Text panel**

You can write or edit your SQL statement in this panel. You can type the statement directly, paste it from another text editor, or import it from an SQL file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059582-Import-from-Logi-Report-Server-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097541-Incremental-Condition-Dialog-Box)
