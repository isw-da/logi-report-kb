---
title: "Send Message - Web Action Builder Dialog"
id: 1500009610422
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009610422-Send-Message-Web-Action-Builder-Dialog
updated_at: 2021-07-24T16:04:08Z
---

# Send Message - Web Action Builder Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009633601-Send-Message-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633341-Series-Options-Dialog)

# Send Message - Web Action Builder Dialog

The Send Message-Web Action Builder dialog helps you to build a [Send Message web action](https://devnet.logianalytics.com/hc/en-us/articles/1500009613362-Delivering-Messages-Between-Library-Components-#Action) on an object so as to send out a message when the event bound with the action is triggered at runtime. It appears when you select \*Send Message and then select OK in the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog.

![Send Message - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904183703/sndmsgwbactnbld.gif)

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
* **0004 - On-screen Filter**  
   Specifies to send out the built-in On-screen Filter message, which will ask the data component who receives the message to filter itself based on the filter condition defined in the message.
* **User Defined**  
   Specifies to send out a user defined message.
  + **ID**  
     Specifies the ID of the message.
  + **Name**  
     Specifies the name of the message.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Adds a new message key-value line. Not available to built-in messages.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected message key-value line. Not available to built-in messages.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected message key-value line up a step. Not available to built-in messages.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009633601-Send-Message-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633341-Series-Options-Dialog)
