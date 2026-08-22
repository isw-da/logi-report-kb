---
title: "Receive Message Dialog"
id: 1500009567242
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009567242-Receive-Message-Dialog
updated_at: 2021-07-24T05:54:55Z
---

# Receive Message Dialog

![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic[Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567282-Record-Level-Security-Information-Dialog)

# Receive Message Dialog

The Receive Message dialog appears when you right-click a table, chart, crosstab, KPI component, or geographic map in a library component and select Receive Message from the shortcut menu. It helps you to define the [messages](https://devnet.logianalytics.com/hc/en-us/articles/1500009570842-Delivering-Messages-Between-Library-Components) the data component is going to receive and specify the actions that will be triggered as a response to each of the messages it receives at runtime. [See the dialog](javascript:%20void(null)).

![Receive Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893811607/rcvmsg.gif)

The following are details about options in the dialog:

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a new message line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected message line.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected message line up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected message line down a step.

**Message ID**

Specifies the ID of the message to be received. You can select the ID from the drop-down list or input it into the text field manually. The item 0002 - Sort is not available to KPI component.

**Message Name**

Specifies the name of the message to be received.

**Message Info**

Available to the 0003 - Parameter message only. When Message ID is 0003 - Parameter, you need to choose a message type from the Message Info column: Automatic or Customized.

**Actions**

Specifies the action to respond to the message to be received.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog) dialog when you input a message ID in the Message ID column, or opens the corresponding dialog when you select a message ID from the Message ID drop-down list for you to specify the action you want to trigger when the message is received.

**OK**

Accepts the changes and closes this dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009588441-RealPlayer-Parameter-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567282-Record-Level-Security-Information-Dialog)
