---
title: "Receive Message Dialog Box"
id: 4405664556951
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664556951-Receive-Message-Dialog-Box
updated_at: 2022-01-27T20:36:16Z
---

# Receive Message Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661691159-RealPlayer-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661692183-Record-Level-Security-Information-Dialog-Box)

# Receive Message Dialog Box

You can use the Receive Message dialog box to define [the messages the current data component is going to receive](https://devnet.logianalytics.com/hc/en-us/articles/4405661935255-Delivering-Messages-Between-Library-Components#Receive) at runtime and specify the actions to be triggered as a response to each of the messages. This topic describes the options in the dialog box.

Designer displays the Receive Message dialog box when you right-click a table, chart, crosstab, KPI, or geographic map in a library component and select Receive Message from the shortcut menu.

![Receive Message dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402325527/rcvmsg.gif)

You see the following options in the dialog box:

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif)**Add button**

Select to add a new message line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif)**Remove button**

Select to delete the specified message line.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified message line higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified message line lower in the list.

**Message ID**

This column shows the ID of the messages that you add for the data component to receive. You can select the ID from the drop-down list or type it in the text box manually.

**Message Name**

This column shows the names of the messages that you add for the data component to receive.

**Message Info**

Designer enables this column when you select Message ID of "0003 - Parameter". You need to choose a message type from the Message Info column: Automatic or Customized.

**Actions**

This column shows the actions that you specify for the data component to respond for each message. To edit the conditions of an action, select in the column and select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420410588951/btn_ellipsis1.gif). Designer then displays different dialog box for you to edit the conditions of the action according to the ID of the message:

* If you select Message ID of "0001 - Filter", Designer displays the [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664481303-Filter-Dialog-Box) for you to edit the filter conditions of the message.
* If you select Message ID of "0002 - Sort", Designer displays the [Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661719191-Sort-Dialog-Box) for you to edit the sort conditions of the message.
* If you select Message ID of "0003 - Parameter", Designer displays the [Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661671831-Parameter-Dialog-Box) for you to edit the parameter values in the message.
* If you select Message ID of "0004 - On-screen Filter", Designer displays the [On-screen Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664536727-On-screen-Filter-Dialog-Box) for you to edit the on-screen filter conditions in the message.
* If you select a user-defined message, Designer displays the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661744791-Web-Action-List-Dialog-Box) for you to specify the action you want to trigger first.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661691159-RealPlayer-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661692183-Record-Level-Security-Information-Dialog-Box)
