---
title: "Receive Sync Dialog Box Properties"
id: 1500009745602
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745602-Receive-Sync-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:54Z
---

# Receive Sync Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745622-Real-time-Settings-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745682-Save-As-Dialog-Box-Properties)

# Receive Sync Dialog Box Properties

Use the Receive Sync dialog box to define the [synchronization messages](https://devnet.logianalytics.com/hc/en-us/articles/1500009771881-Synchronizing-the-Data-Components-in-a-Dashboard) that the data component is going to receive and specify the actions to trigger as a response to each of the messages. This topic describes how to receive synchronization messages.

JDashboard displays the dialog box when you right-click on any object in a data component of a dashboard and select Receive Sync from the shortcut menu.

![Receive Sync dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880438551/rcvsync.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404885517079/btn_dshbrd_add1.gif)

Select to add a new message line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404880430743/btn_dshbrd_rmv1.gif)

Select to remove the selected message line.

**Enable**

Clear the check box to disable a message.

* ![Lock button](https://devnet.logianalytics.com/hc/article_attachments/4404885520023/btn_dshbrd_lock.gif)  
   It indicates that the message is predefined in Logi Report Designer.

**Sync From**

Select the trigger object from which to send out the message.

**Message Name**

Select the message to receive.

**Action Description**

Double-click to type the description for the action the user-defined message will respond.

**Actions**

Select the action to respond to the received user-defined message.

* **\*Filter**  
   Select **\*Filter** to perform the Filter action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880429719/btn_dshbrd_edt1.gif) to open the [Web Action - Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009773701-Web-Action-Filter-Dialog-Box-Properties) dialog box to edit the filter condition.
* **\*On-screen Filter**  
  Select **\*On-screen Filter** to perform the On-screen Filter action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880429719/btn_dshbrd_edt1.gif) to open the [Web Action - On-screen Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009745742-Web-Action-On-screen-Filter-Dialog-Box-Properties) dialog box to edit the filter condition.
* **\*Remove Filter**  
   Select **\*Remove Filter** to perform the Remove Filter action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880429719/btn_dshbrd_edt1.gif) to open the [Web Action - Remove Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009773781-Web-Action-Remove-Filter-Dialog-Box-Properties) dialog box to specify the filters to remove from the data component.
* **\*Sort**  
   Select **\*Sort** to perform the Sort action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880429719/btn_dshbrd_edt1.gif) to open the [Web Action - Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009745802-Web-Action-Sort-Dialog-Box-Properties) dialog box to edit the sort condition.
* **\*Parameter**  
   Select **\*Parameter** to perform the Parameter action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880429719/btn_dshbrd_edt1.gif) to open the [Web Action - Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009745782-Web-Action-Parameter-Dialog-Box-Properties) dialog box to edit the parameter values.
* **\*Property**  
   Select **\*Property** to perform the Property action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880429719/btn_dshbrd_edt1.gif) to open the [Web Action - Change Property](https://devnet.logianalytics.com/hc/en-us/articles/1500009745702-Web-Action-Change-Property-Dialog-Box-Properties) dialog box to edit the properties.
* **\*Go Down**  
   Select **\*Go Down** to perform the Go Down action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880429719/btn_dshbrd_edt1.gif) to open the [Web Action - Go Down](https://devnet.logianalytics.com/hc/en-us/articles/1500009773721-Web-Action-Go-Down-Dialog-Box-Properties) dialog box to edit the go-down condition.
* **\*Go Up**  
   Select **\*Go Up** to perform the Go Up action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880429719/btn_dshbrd_edt1.gif) to open the [Web Action - Go Up](https://devnet.logianalytics.com/hc/en-us/articles/1500009773761-Web-Action-Go-Up-Dialog-Box-Properties) dialog box to edit the go-up condition.
* **\*Go To**  
   Select **\*Go To** to perform the Go To action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880429719/btn_dshbrd_edt1.gif) to open the [Web Action - Go To](https://devnet.logianalytics.com/hc/en-us/articles/1500009745722-Web-Action-Go-To-Dialog-Box-Properties) dialog box to edit the go-to condition.

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Receive Sync dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745622-Real-time-Settings-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745682-Save-As-Dialog-Box-Properties)
