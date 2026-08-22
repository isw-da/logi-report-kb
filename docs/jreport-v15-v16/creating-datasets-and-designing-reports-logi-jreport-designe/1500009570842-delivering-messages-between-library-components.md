---
title: "Delivering Messages Between Library Components"
id: 1500009570842
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570842-Delivering-Messages-Between-Library-Components
updated_at: 2021-07-24T05:53:51Z
---

# Delivering Messages Between Library Components

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570822-Using-the-Configuration-Panel)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570862-Sending-Messages)

# Delivering Messages Between Library Components

A message is a carrier of information that can be delivered between library components. It makes the runtime data synchronization possible. For example, you have two library components containing a crosstab and a table respectively, and both have the field Country. When you select any of the Country value in the crosstab at runtime, you want the crosstab and table to be filtered to show data of this country only. To achieve such synchronization, you can send out a filter message from the Country field in the crosstab and make the crosstab itself and the table receive the same message.

The messages that can be delivered between library components includes the built-in messages Filter, Sort, and Parameter, and user customized messages. A message consists of message ID, message name and message value set. A message ID is a natural number. Logi JReport reserves the IDs from 1 to 1000, which are used in built-in messages, so you can only use IDs beyond 1000 to identify user defined messages. A message name is the name of a message. A message value set is a set of key-value pairs. Each key-value pair has one key and one value. A key or a value can be static or dynamic. A key is of String type, and each value has its own data type, which can be Number, Integer, String, Date, Time, Date Time, Boolean or Currency.

Messages can also be defined at runtime in JDashboard. For details see Synchronizing Data Components in the *Logi JReport Server User's Guide*.

The following topics detail how to send or receive a message:

> * [Sending Messages](https://devnet.logianalytics.com/hc/en-us/articles/1500009570862-Sending-Messages)
> * [Receiving Messages](https://devnet.logianalytics.com/hc/en-us/articles/1500009592741-Receiving-Messages)
> * [Example of Delivering a Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009592721-Example-of-Delivering-a-Message)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570822-Using-the-Configuration-Panel)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570862-Sending-Messages)
