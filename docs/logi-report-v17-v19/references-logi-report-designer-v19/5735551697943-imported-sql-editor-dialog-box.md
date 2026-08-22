---
title: "Imported SQL Editor Dialog Box"
id: 5735551697943
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735551697943-Imported-SQL-Editor-Dialog-Box
updated_at: 2022-11-02T04:37:45Z
---

# Imported SQL Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735551708695-Import-from-Logi-Report-Server-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735523594007-Incremental-Condition-Dialog-Box)

# Imported SQL Editor Dialog Box

You can use the Imported SQL Editor dialog box to [create and edit imported SQLs in a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735507746711-Using-Imported-SQLs). This topic describes the options in the dialog box.

Designer displays the Imported SQL Editor dialog box when you do one of the following:

* In the Catalog Manager, right-click a JDBC connection node and select Add SQL from the shortcut menu.
* In the Catalog Manager, right-click an imported SQL under the Imported SQLs node and select Update from the shortcut menu.
* In the dialog box where an imported SQL list is available, expand the Imported SQLs node in a catalog data source that contains only one JDBC connection and select <Add SQL...>.

![Imported SQL Editor](https://devnet.logianalytics.com/hc/article_attachments/9898479300759/imptdsqledtr.gif)

Designer displays these options:

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

**Text panel**

You can write or edit your SQL statement in this panel. You can type the statement directly, paste it from another text editor, or import it from an SQL file.

The toolbar in this panel provides the following buttons that facilitate the process of composing the SQL statement.

* ![Cut button](https://devnet.logianalytics.com/hc/article_attachments/9898477236631/btn_cut.gif)**Cut**  
  Select to cut the specified text in the text panel.
* ![Copy button](https://devnet.logianalytics.com/hc/article_attachments/9898460197015/btn_copy.gif)**Copy**  
  Select to copy the specified text in the text panel.
* ![Paste button](https://devnet.logianalytics.com/hc/article_attachments/9898477250583/btn_paste.gif)**Paste**  
  Select to paste the text that you previously cut or copied in the text panel.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9898477280279/btn_delete.gif)**Delete**  
  Select to delete the specified text from the text panel.
* ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/9898477290263/btn_undo.gif)**Undo**  
  Select to undo an action.
* ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/9898477298839/btn_redo.gif)**Redo**  
  Select to cancel undoing an action.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9898405034775/btn_fnd.gif)**Search**  
  Select to search for text in the text panel, and replace the found text with different text.
* ![Check button](https://devnet.logianalytics.com/hc/article_attachments/9898477308823/btn_check.gif)**Check**  
  Select to check whether there are errors in the SQL statement.
* ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/9898477314839/btn_bkmrk.gif)**Add Bookmark**  
  Select to add a bookmark to a line.
* ![Go to Previous Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/9898460252567/btn_prvs.gif)**Go to Previous Bookmark**  
  Select to go to the previous bookmark.
* ![Go to Next Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/9898477497751/btn_nxt.gif)**Go to Next Bookmark**  
  Select to go to the next bookmark.
* ![Clear button](https://devnet.logianalytics.com/hc/article_attachments/9898477516951/btn_clear.gif)**Clear All Bookmarks**  
  Select to remove all the bookmarks.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735551708695-Import-from-Logi-Report-Server-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735523594007-Incremental-Condition-Dialog-Box)
