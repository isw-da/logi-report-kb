---
title: "Send Message - Web Action Builder Dialog"
id: 1500009588761
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009588761-Send-Message-Web-Action-Builder-Dialog
updated_at: 2021-07-24T05:54:50Z
---

# Send Message - Web Action Builder Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567562-Select-Value-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588741-Send-Message-Dialog)

# Send Message - Web Action Builder Dialog

This dialog appears when you select \*Send Message and then select OK in the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog) dialog. It helps you to build a [Send Message web action](https://devnet.logianalytics.com/hc/en-us/articles/1500009570862-Sending-Messages#Action) on an object so as to send out a message when the event bound with the action is triggered at runtime. [See the dialog](javascript:%20void(null)).

![Send Message - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889291415/wbactnbldr_sndmsg.gif)

The following are details about options in the dialog:

**Message**

Specifies the message that will be sent out.

* **0001 - Filter**  
  Specifies to send out the built-in Filter message, which will ask the data component who receives the message to filter itself based on the filter condition defined in the message.
* **0002 - Sort**  
  Specifies to send out the built-in Sort message, which will ask the data component who receives the message to sort itself based on the sort condition defined in the message.
* **0003 - Parameter**  
  There are two types:
  + **Automatic**  
    Specifies to send out the built-in Parameter message with all the parameter values used in the current library component, which will ask the library component in which the data component that receives the message is to re-run itself using the same parameter values.
  + **Customized**  
    Specifies to send out the built-in Parameter message, which will ask the library component in which the data component that receives the message is to re-run itself using the parameter value defined in the message. In this case, you need to define a parameter with a value.

  For compatibility with earlier versions, the previous 0003 - Parameter message will be converted to the Customized type and 0004 - Parameters to the Automatic type.
* **User Defined**  
  Specifies to send out a user defined message.
  + **ID**  
    Specifies the ID of the message.
  + **Name**  
    Specifies the name of the message.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a new message key-value line. Not available to built-in messages.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected message key-value line. Not available to built-in messages.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected message key-value line up a step. Not available to built-in messages.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected message key-value line down a step. Not available to built-in messages.

**Key**

Specifies the key of the message. For a built-in message, the key cannot be changed.

**Data Type**

Specifies the data type of the value. For a built-in message, the data type cannot be changed.

**Value**

Specifies the value of the key.

**OK**

Accepts the changes and closes this dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567562-Select-Value-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588741-Send-Message-Dialog)
