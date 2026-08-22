---
title: "Receive Message Dialog Box"
id: 5735567115287
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735567115287-Receive-Message-Dialog-Box
updated_at: 2022-11-02T04:40:10Z
---

# Receive Message Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735552527511-RealPlayer-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735531031575-Record-Level-Security-Information-Dialog-Box)

# Receive Message Dialog Box

You can use the Receive Message dialog box to define [the messages the current data component is going to receive](https://devnet.logianalytics.com/hc/en-us/articles/5735576827671-Delivering-Messages-Between-Library-Components#Receive) at runtime and specify the actions to be triggered as a response to each of the messages. This topic describes the options in the dialog box.

Designer displays the Receive Message dialog box when you right-click a table, chart, crosstab, KPI, or geographic map in a library component and select Receive Message from the shortcut menu.

![Receive Message dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898423112087/rcvmsg.gif)

Designer displays these options:

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**

Select to add a new message line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified message line.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified message line higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified message line lower in the list.

**Message ID**

This column shows the ID of the messages that you add for the data component to receive. You can select the ID from the drop-down list or type it in the text box manually.

**Message Name**

This column shows the names of the messages that you add for the data component to receive.

**Message Info**

Designer enables this column when you select Message ID of "0003 - Parameter". You need to choose a message type from the Message Info column: Automatic or Customized.

**Actions**

This column shows the actions that you specify for the data component to respond for each message. To edit the conditions of an action, select in the column and select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif). Designer then displays different dialog box for you to edit the conditions of the action according to the specified message.

* When you select Message ID of "0001 - Filter", Designer displays the [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735509055895-Filter-Dialog-Box) for you to edit the filter conditions of the message.
* When you select Message ID of "0002 - Sort", Designer displays the [Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515567127-Sort-Dialog-Box) for you to edit the sort conditions of the message.
* When you select Message ID of "0003 - Parameter", Designer displays the [Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524288151-Parameter-Dialog-Box) for you to edit the parameter values in the message.
* When you select Message ID of "0004 - On-screen Filter", Designer displays the [On-screen Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735543893271-On-screen-Filter-Dialog-Box) for you to edit the on-screen filter conditions in the message.
* When you select a user-defined message, Designer displays the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735531755159-Web-Action-List-Dialog-Box) for you to specify the action you want to trigger first.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735552527511-RealPlayer-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735531031575-Record-Level-Security-Information-Dialog-Box)
