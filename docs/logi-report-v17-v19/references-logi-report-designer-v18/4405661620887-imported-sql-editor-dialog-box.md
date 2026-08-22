---
title: "Imported SQL Editor Dialog Box"
id: 4405661620887
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661620887-Imported-SQL-Editor-Dialog-Box
updated_at: 2022-01-27T20:38:13Z
---

# Imported SQL Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661621911-Import-from-Logi-Report-Server-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664520343-Incremental-Condition-Dialog-Box)

# Imported SQL Editor Dialog Box

You can use the Imported SQL Editor dialog box to [create and edit imported SQLs in a catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661424407-Using-Imported-SQLs). This topic describes the options in the dialog box.

Designer displays the Imported SQL Editor dialog box when you do one of the following:

* In the Catalog Manager, right-click a JDBC connection node and select Add SQL from the shortcut menu.
* In the Catalog Manager, right-click an imported SQL under the Imported SQLs node and select Update from the shortcut menu.
* In the dialog box where an imported SQL list is available, expand the Imported SQLs node in a catalog data source that contains only one JDBC connection and select <Add SQL...>.

![Imported SQL Editor](https://devnet.logianalytics.com/hc/article_attachments/4420542117783/imptdsqledtr.gif)

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

* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/4420556154391/btn_cut.gif)**Cut**  
  Select to cut the specified text in the text panel.
* ![Copy button](https://devnet.logianalytics.com/hc/article_attachments/4420550891671/btn_copy.gif)**Copy**  
  Select to copy the specified text in the text panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/4420542118551/btn_paste.gif)**Paste**  
  Select to paste the text that you previously cut or copied in the text panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420556155031/btn_delete.gif)**Delete**  
  Select to delete the specified text from the text panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4420556155543/btn_undo.gif)**Undo**  
  Select to undo an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4420550891927/btn_redo.gif)**Redo**  
  Select to cancel undoing an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420556086551/btn_fnd.gif)**Search**  
  Select to search for text in the text panel, and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4420556097687/btn_check.gif)**Check**  
  Select to check whether there are errors in the SQL statement.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4420542074903/btn_bkmrk.gif)**Add Bookmark**  
  Select to add a bookmark to a line.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4420542119063/btn_prvs.gif)**Go to Previous Bookmark**  
  Select to go to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4420556155927/btn_nxt.gif)**Go to Next Bookmark**  
  Select to go to the next bookmark.
* ![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4420556156567/btn_clear.gif)**Clear All Bookmarks**  
  Select to remove all the bookmarks.

**Text panel**

You can write or edit your SQL statement in this panel. You can type the statement directly, paste it from another text editor, or import it from an SQL file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661621911-Import-from-Logi-Report-Server-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664520343-Incremental-Condition-Dialog-Box)
