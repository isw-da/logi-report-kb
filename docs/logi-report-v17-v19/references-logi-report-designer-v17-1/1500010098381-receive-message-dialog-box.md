---
title: "Receive Message Dialog Box"
id: 1500010098381
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010098381-Receive-Message-Dialog-Box
updated_at: 2021-07-23T19:15:53Z
---

# Receive Message Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098441-RealPlayer-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098461-Record-Level-Security-Information-Dialog-Box)

# Receive Message Dialog Box

You can use the Receive Message dialog box to define [the messages the current data component is going to receive](https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components#Receive) at runtime and specify the actions to be triggered as a response to each of the messages. This topic describes the options in the dialog box.

Designer displays the Receive Message dialog box when you right-click a table, chart, crosstab, KPI, or geographic map in a library component and select Receive Message from the shortcut menu.

![Receive Message dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848404375/rcvmsg.gif)

You see the following options in the dialog box:

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new message line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified message line.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified message line higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified message line lower in the list.

**Message ID**

The column shows the ID of the messages that you add for the data component to receive. You can select the ID from the drop-down list or type it in the text box manually.

**Message Name**

The column shows the names of the messages that you add for the data component to receive.

**Message Info**

Designer enables this column when you select Message ID of "0003 - Parameter". You need to choose a message type from the Message Info column: Automatic or Customized.

**Actions**

The column shows the actions that you specify for the data component to respond for each message.

* ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif)**Ellipsis button**  
  Select to edit or specify the action to be triggered when the data component receives the message. Designer displays different dialog box when you select the button according to the ID of the message:
  + If you select Message ID of "0001 - Filter", Designer displays the [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096841-Filter-Dialog-Box) for you to edit the filter conditions of the message.
  + If you select Message ID of "0002 - Sort", Designer displays the [Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060522-Sort-Dialog-Box) for you to edit the sort conditions of the message.
  + If you select Message ID of "0003 - Parameter", Designer displays the [Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060162-Parameter-Dialog-Box) for you to edit the parameter values in the message.
  + If you select Message ID of "0004 - On-screen Filter", Designer displays the [On-screen Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060022-On-screen-Filter-Dialog-Box) for you to edit the on-screen filter conditions in the message.
  + If you select a user-defined message, Designer displays the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box) for you to specify the action you want to trigger first.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098441-RealPlayer-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098461-Record-Level-Security-Information-Dialog-Box)
