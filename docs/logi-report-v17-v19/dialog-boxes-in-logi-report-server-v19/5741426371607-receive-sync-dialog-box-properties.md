---
title: "Receive Sync Dialog Box Properties"
id: 5741426371607
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741426371607-Receive-Sync-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:46Z
---

# Receive Sync Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741405058071-Real-time-Settings-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741405177239-Save-As-Dialog-Box-Properties)

# Receive Sync Dialog Box Properties

Use the Receive Sync dialog box to define the [synchronization messages](https://devnet.logianalytics.com/hc/en-us/articles/5741401855639-Synchronizing-the-Data-Components-in-a-Dashboard) that a data component is going to receive and specify the actions to trigger as a response to each of the messages. This topic describes how to receive synchronization messages.

Server displays the dialog box when you right-click any object in a data component of a dashboard and select **Receive Sync** from the shortcut menu.

![Receive Sync dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905737647255/rcvsync.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905736979863/btn_dshbrd_add1.gif)**Add button**

Select to add a new message line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9905758900887/btn_dshbrd_rmv1.gif)**Remove button**

Select to remove the selected message line.

**Enable**

Clear to disable a message.

* ![Lock button](https://devnet.logianalytics.com/hc/article_attachments/9905737486103/btn_dshbrd_lock.gif)**Lock button**  
   It indicates that the message is predefined in Logi Report Designer.

**Sync From**

Select the trigger object from which you want to send out the message.

**Message Name**

Select the message you want to receive.

**Action Description**

Double-click the text box, and then type the description for the action the user-defined message will respond.

**Actions**

Select the action to respond to the received user-defined message.

* **\*Filter**  
   Select **\*Filter** to perform the Filter action to respond to the received message. You can select the Edit button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905758829591/btn_dshbrd_edt1.gif) to open the [Web Action - Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741432475415-Web-Action-Filter-Dialog-Box-Properties) to edit the filter condition.
* **\*On-screen Filter**  
  Select **\*On-screen Filter** to perform the On-screen Filter action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905758829591/btn_dshbrd_edt1.gif) to open the [Web Action - On-screen Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741426659991-Web-Action-On-screen-Filter-Dialog-Box-Properties) to edit the filter condition.
* **\*Remove Filter**  
   Select **\*Remove Filter** to perform the Remove Filter action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905758829591/btn_dshbrd_edt1.gif) to open the [Web Action - Remove Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741405453207-Web-Action-Remove-Filter-Dialog-Box-Properties) to specify the filters to remove from the data component.
* **\*Sort**  
   Select **\*Sort** to perform the Sort action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905758829591/btn_dshbrd_edt1.gif) to open the [Web Action - Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741420349847-Web-Action-Sort-Dialog-Box-Properties) to edit the sort condition.
* **\*Parameter**  
   Select **\*Parameter** to perform the Parameter action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905758829591/btn_dshbrd_edt1.gif) to open the [Web Action - Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741413450647-Web-Action-Parameter-Dialog-Box-Properties) to edit the parameter values.
* **\*Property**  
   Select **\*Property** to perform the Property action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905758829591/btn_dshbrd_edt1.gif) to open the [Web Action - Change Property dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741405224215-Web-Action-Change-Property-Dialog-Box-Properties) to edit the properties.
* **\*Go Down**  
   Select **\*Go Down** to perform the Go Down action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905758829591/btn_dshbrd_edt1.gif) to open the [Web Action - Go Down dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741441980439-Web-Action-Go-Down-Dialog-Box-Properties) to edit the go-down condition.
* **\*Go Up**  
   Select **\*Go Up** to perform the Go Up action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905758829591/btn_dshbrd_edt1.gif) to open the [Web Action - Go Up dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741442048663-Web-Action-Go-Up-Dialog-Box-Properties) to edit the go-up condition.
* **\*Go To**  
   Select **\*Go To** to perform the Go To action to respond to the received message. You can select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905758829591/btn_dshbrd_edt1.gif) to open the [Web Action - Go To dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741442004887-Web-Action-Go-To-Dialog-Box-Properties) to edit the go-to condition.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741405058071-Real-time-Settings-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741405177239-Save-As-Dialog-Box-Properties)
