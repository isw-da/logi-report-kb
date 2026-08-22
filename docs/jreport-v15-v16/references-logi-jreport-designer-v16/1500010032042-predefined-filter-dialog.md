---
title: "Predefined Filter Dialog"
id: 1500010032042
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010032042-Predefined-Filter-Dialog
updated_at: 2021-07-24T10:38:31Z
---

# Predefined Filter Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032022-Precision-Settings-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067441-Preview-Option-Dialog)

# Predefined Filter Dialog

The Predefined Filter dialog helps you to [add predefined filters to a business view](https://devnet.logianalytics.com/hc/en-us/articles/1500010034562-Creating-Business-Views-in-a-Catalog#Filter), which can be applied when creating/modifying reports based on the business view in Logi JReport Server by end users. It appears when you select Menu > Tools > Predefined Filter or Predefined Filter on the toolbar of the [Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010064841-Business-View-Editor-Dialog).

![Predefined Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901146263/prdfndfltr.gif)

The following are details about options in the dialog:

**Filters**

Lists all the predefined filters in the business view. You can modify a filter's name and description in the box.

* **New**  
   Creates a filter.
* **Delete**  
   Removes the selected filter.

**Condition**

Specifies the filter condition.

* **Add Condition**  
   Adds a new condition line.
* **Delete**  
   Deletes the selected condition line.
* **Group**  
   Makes the selected conditions in one group.
* **Ungroup**  
   Makes the selected condition ungrouped.
* **Up**  
   Moves the selected condition or group up to a higher level.
* **Down**  
   Moves the selected condition or group down to a lower level.
* **Logic**  
   Lists the logic operator.
  + **And**  
     Logic operator And which is applied to this and the next line or group.
  + **Or**  
     Logic operator Or which is applied to this and the next line or group.
* **Field**  
   Specifies the field to be filtered. You can either type in the field directly or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the text box to specify the field in the View Element Resources dialog.
* **Operator**  
   Specifies the operator to compose the filter expression.
  + **=**  
     Equal to
  + **>=**  
     Greater than or equal to
  + **>**  
     Greater than
  + **<**  
     Less than
  + **<=**  
     Less than or equal to
  + **!=**  
     Not equal to
  + **[not] in**  
     Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For the operator "in" or "not in", multiple values separated by comma (,) are allowed.
  + **[not] like**  
     Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
  + **[not] between**  
     Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", there are two value text boxes for inputting the same type of values.
  + **is [not] null**  
     It is used in WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", the value text box is hidden.
* **Value**  
   Specifies the value of how to filter the field. You can either type the value in the text box manually or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the text box to specify the value in the Values dialog.
* **SQL Statement**  
   Displays the SQL statement of the filter expressions.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032022-Precision-Settings-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067441-Preview-Option-Dialog)
