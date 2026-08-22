---
title: "Send Sync Dialog Box Properties"
id: 1500009745662
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745662-Send-Sync-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:53Z
---

# Send Sync Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773641-Select-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773601-Share-Parameters-Setting-Dialog-Box-Properties)

# Send Sync Dialog Box Properties

Use the Send Sync dialog box to customize the [synchronization message](https://devnet.logianalytics.com/hc/en-us/articles/1500009771881-Synchronizing-the-Data-Components-in-a-Dashboard) to send out when selecting the object. This topic describes how to send synchronization message.

JDashboard displays the dialog box when you right-click an object in a data component of a dashboard and select Send Sync > Customize from the shortcut menu.

![Send Sync dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885519767/sndsync.gif)

**Sender**

Name of the trigger object from which to send out the synchronization message.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404885517079/btn_dshbrd_add1.gif)

Select to add a new message line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404880430743/btn_dshbrd_rmv1.gif)

Select to remove the selected message line.

**Enable**

Clear the check box to disable a message.

* ![Lock button](https://devnet.logianalytics.com/hc/article_attachments/4404885520023/btn_dshbrd_lock.gif)  
   It indicates that the message is predefined in Logi Report Designer.

**Message Name**

Type the name of a message.

**Message Type**

Select the type of the message to send out.

* **Filter**  
   Select **Filter** to send out the built-in Filter message, which will ask the data component who receives the message to filter itself according to the filter condition defined in the message.
  + **Column Name**  
     Select the field on which to filter the records. To make the condition dynamic, select the values under the **Dynamic Key** node.
  + **Operator**  
    Select the operator to compose the condition.
  + **Filter Value**  
    Select the value of the field. To make the condition dynamic, select the values under the **Dynamic Key** node.
* **Sort**  
   Select **Sort** to send out the built-in Sort message, which will ask the data component who receives the message to sort itself according to the sort condition defined in the message.
  + **Sort On**   
     Select the field on which to sort the records. To make the condition dynamic, select the values under the Dynamic Key node.
  + **Sort Order**   
     Select the **Ascending** or **Descending** order to sort the field.
* **Parameter**  
  Select **Parameter** to send out the built-in Parameter message, which will ask the library component which the data component that receives the message is in to re-run itself using the parameter value defined in the message.
  + **Parameter Name**   
     Select the name of the parameter. To make the condition dynamic, select the values under the Dynamic Key node.
  + **Parameter Value**   
     Select the value of the parameter. To make the condition dynamic, select the values under the Dynamic Key node.
* **On-screen Filter**  
   Select **On-screen Filter** to send out the built-in On-screen Filter message, which will ask the data component who receives the message to filter itself according to the filter condition defined in the message.
  + **Column Name**  
     Select the field on which to filter the records. To make the condition dynamic, select the values under the Dynamic Key node.
  + **Filter Value**  
     Select the value of the field. To make the condition dynamic, select the values under the Dynamic Key node.
* **User Defined**  
   Specifies to send out a user defined message.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404885517079/btn_dshbrd_add1.gif)  
     Select to add a message key-value line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404880430743/btn_dshbrd_rmv1.gif)  
     Select to remove the selected message key-value line.
  + **Key Name**  
     Select the key of the message.
  + **Value**  
     Select the value of the key.

**OK**

Select **OK** to send the message.

**Cancel**

Select **Cancel** to close the dialog box without sending the message.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Send Sync dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without sending the message.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773641-Select-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773601-Share-Parameters-Setting-Dialog-Box-Properties)
