---
title: "Send Message - Web Action Builder Dialog Box"
id: 1500010060502
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010060502-Send-Message-Web-Action-Builder-Dialog-Box
updated_at: 2021-07-23T19:16:00Z
---

# Send Message - Web Action Builder Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098781-Send-Message-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098601-Series-Options-Dialog-Box)

# Send Message - Web Action Builder Dialog Box

The Send Message-Web Action Builder dialog box helps you to build a [Send Message web action](https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components#Action) on an object so as to send out a message when the event bound with the action is triggered at runtime. It appears when you select \*Send Message and then select OK in the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box).

![Send Message - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856823447/sndmsgwbactnbld.gif)

The following are details about options in the dialog box:

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
   Specifies to send out a user-defined message.
  + **ID**  
     Specifies the ID of the message.
  + **Name**  
     Specifies the name of the message.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)

Adds a new message key-value line. Not available to built-in messages.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)

Removes the selected message key-value line. Not available to built-in messages.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)

Moves the selected message key-value line higher in the message list. Not available to built-in messages.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)

Moves the selected message key-value line lower in the message list. Not available to built-in messages.

**Key**

Specifies the key of the message. For a built-in message, the key cannot be changed.

**Data Type**

Specifies the data type of the value. For a built-in message, the data type cannot be changed.

**Value**

Specifies the value of the key.

**OK**

Accepts the changes and closes this dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098781-Send-Message-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098601-Series-Options-Dialog-Box)
