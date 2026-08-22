---
title: "Send Message - Web Action Builder Dialog Box"
id: 4405661717911
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661717911-Send-Message-Web-Action-Builder-Dialog-Box
updated_at: 2022-01-27T20:38:15Z
---

# Send Message - Web Action Builder Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661716631-Send-Message-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661699223-Series-Options-Dialog-Box)

# Send Message - Web Action Builder Dialog Box

You can use the Send Message - Web Action Builder dialog box to build a [Send Message web action](https://devnet.logianalytics.com/hc/en-us/articles/4405661935255-Delivering-Messages-Between-Library-Components#Action) on certain object in a library component, so as to send out a message when the event bound with the action happens on the object at runtime. This topic describes the options in the dialog box.

Designer displays the Send Message - Web Action Builder dialog box when you select \*Send Message and then select OK in the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661744791-Web-Action-List-Dialog-Box).

![Send Message - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402325271/sndmsgwbactnbld.gif)

You see the following options in the dialog box:

**Message**

Select the message to send out from the object.

* **0001 - Filter**  
  Select to send out the built-in Filter message to ask the data component who receives the message to filter itself based on the filter condition defined in the message.
* **0002 - Sort**  
  Select to send out the built-in Sort message to ask the data component who receives the message to sort itself based on the sort condition defined in the message.
* **0003 - Parameter**  
  Designer provides two types for this message:
  + **Automatic**  
    Select to send out the built-in Parameter message, which contains all the parameter values used in the current library component, to ask the library component in which the data component that receives the message is to rerun itself using the same parameter values.
  + **Customized**  
    Select to send out the built-in Parameter message to ask the library component in which the data component that receives the message is to rerun itself using the parameter value defined in the message. If you select this Parameter message type, you need to define a parameter with a value.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) For compatibility with earlier versions, Designer converts the 0003 - Parameter message defined in an early version to the Customized type and 0004 - Parameters to the Automatic type.
* **0004 - On-screen Filter**  
  Select to send out the built-in On-screen Filter message to ask the data component who receives the message to filter itself based on the filter condition defined in the message.
* **User Defined**  
  Select to send out a user-defined message.
  + **ID**  
    Specify the ID of the message.
  + **Name**  
    Specify the name of the message.

Designer enables the following four buttons when you select User Defined from the Message drop-down list:

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif)**Add button**

Select to add a new message key-value line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif)**Remove button**

Select to delete the specified message key-value line.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified message key-value line higher in the message list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified message key-value line lower in the message list.

**Key**

This column shows the keys of the message. You cannot change the key for a built-in message.

**Data Type**

This column shows the data type for the values of the message. You cannot change the data type for a built-in message; for a user-defined message, you cannot change the data type if you select the value from the drop-down list in the Value column either.

**Value**

This column shows the values of the message.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661716631-Send-Message-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661699223-Series-Options-Dialog-Box)
