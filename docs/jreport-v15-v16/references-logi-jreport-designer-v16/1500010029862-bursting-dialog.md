---
title: "Bursting Dialog"
id: 1500010029862
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029862-Bursting-Dialog
updated_at: 2021-07-24T10:39:08Z
---

# Bursting Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029802-Bind-Data-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064841-Business-View-Editor-Dialog)

# Bursting Dialog

The Bursting dialog helps you to edit a normal page report to become a [bursting report](https://devnet.logianalytics.com/hc/en-us/articles/1500010070801-Creating-Bursting-Reports). It appears when you select Report > Bursting.

![Bursting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901138071/burst.gif)

The following are details about options in the dialog:

**Enable Bursting Report**

Specifies whether to enable the bursting options.

**Schema Name**

Lists the names of the bursting schemas for the report. Bursting schema defines how data is split and who receives a subset of the split data.

When a schema name is selected, the schema's bursting information is displayed in the Mapping and Recipient sections below. By selecting a schema name you can rename it.

**Add**

Creates a new bursting schema for the report. You need define the schema's Mapping and Recipient information.

**Remove**

Removes a selected schema from the Schema Name box.

**Mapping**

Specifies the relationship between the bursting key and recipient for the selected schema.

* **Bursting Key**
  + **Dataset**  
     Specifies a dataset used in the report based on which to set the bursting key. Multiple bursting schemas for a report can be based on same or different datasets in the report.
  + **Bursting Key**  
     Specifies data fields in the specified dataset according to which to split report data.
* **Recipient**
  + **Data Source**  
     Specifies the data source that contains the recipient query.
  + **Query**  
     Specifies the query from the selected data source which retrieves recipient addresses. Multiple bursting schemas for a report can be based on different recipient queries in the report.
  + **Recipient Mapping Identifier**  
     Specifies a unique data field to map to each bursting key field. The available values are data fields in the specified query of the same data type as the bursting key.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
   Adds a row to map another pair of bursting key and recipient.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Removes the row of mapping.

**Recipient**

Defines the formats of recipient addresses for the selected schema.

* **E-mail**  
   Specifies the data field that defines E-mail addresses.
* **FTP**  
   Specifies the data field that defines FTP addresses.
* **Disk**  
   Specifies the data field that defines file system directories.
* **Logi JReport Server Version**  
   Specifies the data field that defines resource directories in the Logi JReport Server resource system.
* **Logi JReport Server User**  
   Specifies the data field that defines user addresses in the Logi JReport Server security system.
  + **User E-mail**  
     If checked, the report result will be sent to e-mail addresses.
  + **User Private Folder**  
     If checked, the report result will be sent to the users' My Reports folders in the server resource tree and you are allowed to give a sub path.
    - **Sub Path**  
       If checked, specify a sub path in the My Reports folder and the report result will be sent to the sub path.
* **Logi JReport Server Group**  
   Specifies the data field that defines group addresses in the Logi JReport Server security system.
  + **User E-mail**  
     If checked, the report result will be sent to e-mail addresses.
  + **User Private Folder**  
     If checked, the report result will be sent to the group members' My Reports folders in the server resource tree and you are allowed to give a sub path.
    - **Sub Path**  
       If checked, specify a sub path in the My Reports folder and the report result will be sent to the sub path.
* **Logi JReport Server Role**  
   Specifies the data field that defines role addresses in the Logi JReport Server security system.
  + **User E-mail**  
     If checked, the report result will be sent to e-mail addresses.
  + **User Private Folder**  
     If checked, the report result will be sent to the role members' My Reports folders in the server resource tree and you are allowed to give a sub path.
    - **Sub Path**  
       If checked, specify a sub path in the My Reports folder and the report result will be sent to the sub path.

**E-mail Settings**

Enabled when E-mail or Logi JReport Server User/Group/Role > User E-mail is selected in the Recipient section. Select it to access the [E-mail Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500010065801-E-mail-Settings-Dialog) dialog to specify more e-mail information.

**OK**

Accepts all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029802-Bind-Data-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064841-Business-View-Editor-Dialog)
