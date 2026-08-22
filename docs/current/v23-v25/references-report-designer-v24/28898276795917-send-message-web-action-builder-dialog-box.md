---
title: "Send Message - Web Action Builder Dialog Box"
id: 28898276795917
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898276795917-Send-Message-Web-Action-Builder-Dialog-Box
updated_at: 2024-09-30T09:13:32Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Send Message - Web Action Builder Dialog Box

You can use the Send Message - Web Action Builder dialog box to build a Send Message web action on certain object in a library component, so as to send out a message when the event bound with the action happens on the object at runtime. This topic describes the options in the dialog box.
    

Designer displays the Send Message - Web Action Builder dialog box when you select *SendMessage and then select OK in the Web Action List dialog box.

Designer displays these options:

Message

Select the message to send out from the object.

- 
0001 - Filter
Select to send out the built-in Filter message.

- 
0002 - Sort
Select to send out the built-in Sort message.

- 
0003 - Parameter
Designer provides two types for this message:

- 
Automatic
Select to send out a Parameter message containing all parameter values of the current library component.

- 
Customized
Select to send out a Parameter message containing customized parameter values.

- 
0004 - On-screen Filter
Select to send out the built-in On-screen Filter message.
            

- 
User Defined
Select to send out a user-defined message.
      
- 
ID
Specify the ID of the message.

- 
Name
Specify the name of the message. 

Designer enables the following four buttons when you select User Defined from the Message drop-down list:

Add button

Select to add a new message key-value line. 

Remove button

Select to delete the specified message key-value line.

Move Up button

Select to move the specified message key-value line higher in the message list.

Move Down button

Select to move the specified message key-value line lower in the message list.

Key

This column shows the keys of the message. You cannot change the key for a built-in message.

Data Type

This column shows the data type for the values of the message. You cannot change the data type for a built-in message; for a user-defined message, you cannot change the data type if you select the value from the drop-down list in the Value column either.

Value

This column shows the values of the message.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
