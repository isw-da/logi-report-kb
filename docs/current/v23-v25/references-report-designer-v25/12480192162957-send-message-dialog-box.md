---
title: "Send Message Dialog Box"
id: 12480192162957
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480192162957-Send-Message-Dialog-Box
updated_at: 2026-02-25T23:48:44Z
source_host: docs-report.zendesk.com
---
# 
Send Message Dialog Box

You can use the Send Message dialog box to customize the messages that you want to send out when specific events occur on certain object in a library component. This topic describes the options in the dialog box.
    

Designer displays the Send Message dialog box when you right-click some object in a library component and navigate to Send Message > Customize on the shortcut menu.

Designer displays these options:

Events

This box lists the events that you can use to trigger the messages. Select the checkbox ahead of an event and select on the event name to specify the message it is going to trigger. 

Message

Select the message that you want to send out when the specified event occurs on the object.

- 
0001 - Filter
Select to send out the built-in Filter message to ask the data component who receives the message to filter itself based on the filter condition defined in the message.

- 
0002 - Sort
Select to send out the built-in Sort message to ask the data component who receives the message to sort itself based on the sort condition defined in the message.

- 
0003 - Parameter
Designer provides two types for this message:
    
- 
Automatic
Select to send out the built-in Parameter message, which contains all the parameter values used in the current library component, to ask the library component in which the data component that receives the message is to rerun itself using the same parameter values.

- 
Customized
Select to send out the built-in Parameter message to ask the library component in which the data component that receives the message is to rerun itself using the parameter value defined in the message. If you select this Parameter message type, you need to define a parameter with a value.

 For compatibility with earlier versions, Designer converts the 0003 - Parameter message defined in an early version to the Customized type and 0004 - Parameters to the Automatic type.

- 
0004 - On-screen Filter
Select to send out the built-in On-screen Filter message to ask the data component who receives the message to filter itself based on the filter condition defined in the message.
            

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
