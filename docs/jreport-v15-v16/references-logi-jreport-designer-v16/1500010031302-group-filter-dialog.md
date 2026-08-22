---
title: "Group Filter Dialog"
id: 1500010031302
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031302-Group-Filter-Dialog
updated_at: 2021-07-24T10:38:41Z
---

# Group Filter Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066801-Go-Up-Web-Action-Builder-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031322-Group-Options-Dialog)

# Group Filter Dialog

The Group Filter dialog helps you to create and modify [advanced filtering conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Filter) based on the selected group. It appears when you select the Group Filter button in the Group screen of the report wizard.

![Group Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901213335/grpfltr.gif)

The following are details about options in the dialog:

**Logic**

Specifies whether to evaluate the records that are not in the record aggregate.

**Functions**

Specifies the function to aggregate on a certain field.

* **Min**  
   Evaluates the records that have the lowest values for the selected field.
* **Max**  
   Evaluates the records that have the largest values for the selected field.
* **Exist**  
   Checks if there exists at least one qualified record.

**Field Name** (before Occur With)

Specifies the field you want to aggregate on.

**Field Name** (after Occur With)

Specifies the criteria of the filter.

Expression includes not only the DBField, but also formulas and parameters. You can manually type the strings supported by the database or select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) to select column names or fields values in the Expressions dialog.

Where,

* **+**  
   Adds numbers or fields together in the Expression menu.
* **-**  
   Subtracts numbers or fields together in the Expression menu.
* **\***  
   Multiplies numbers or fields together in the Expression menu.
* **/**  
   Divides numbers or fields together in the Expression menu.
* **=**  
   Equates fields together.
* **"**  
   Places quotations marks on long character strings or names that have blanks. For example, places quotes on values, such as "New York" and "Washington DC".
* **||**  
   Places fields together in the same Expression menu. For example: "New York" || "Washington DC".
* **( )**  
   Places the fields in parentheses.

**Operators**

Specifies the operator to compose the filter expression.

* **=**  
   Equal to
* **>**  
   Greater than
* **<**  
   Less than
* **>=**  
   Greater than or equal to
* **<=**  
   Less than or equal to
* **<>**  
   Not equal to

**Value**

Specifies the value used in the filter condition.

You can also use a parameter for runtime input. You can manually type the value or parameter name, or, for parameters, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) to select the parameter names in the Expressions dialog.

**More**

Lists some additional commands.

* **END**  
   Finishes entering the condition
* **And**  
   Inserts the logic operator AND which is applied to this line and the next line.
* **OR**  
   Inserts the logic operator OR which is applied to this line and the next line.
* **Insert Row**  
   Inserts a single Expression row.
* **Delete Row**  
   Deletes a single Expression row.

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Closes the dialog, leaving any changes unsaved.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066801-Go-Up-Web-Action-Builder-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031322-Group-Options-Dialog)
