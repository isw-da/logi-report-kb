---
title: "Using Basic Web Controls"
id: 5735521282967
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735521282967-Using-Basic-Web-Controls
updated_at: 2022-11-02T04:28:51Z
---

# Using Basic Web Controls

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564487575-Working-with-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527852183-Using-Basic-Web-Controls-in-a-Report)

# Using Basic Web Controls

Basic web controls refer to the following: Text Field, Password, Text Area, Checkbox, Radio Button, Image Button, Button, Drop-down List, and List. This topic introduces how you can use each of the basic web controls to serve different reporting requirements.

The following describes the usage of each basic web control generally.

* A text field is a text box that displays information in one row. You can specify the number of characters to display and the maximum number of characters allowed in a text field.
* A password is a special text field in which the typed password displays as asterisks. You can specify the number of characters to display and the maximum number of characters allowed in a password.
* A text area is a text box that displays information in multiple rows. You can specify the maximum number of characters allowed in a text area. When the input text reaches the width of the text area, the following text auto wraps to the next row, and so on.
* A checkbox or a radio button is a button used to specify the value of a Boolean type option. When the button is selected, the option is enabled, and when cleared, the option is disabled. A checkbox can work alone while two or more radio buttons need to work together to enable only one from multiple options.
* An image button enables you to import an image from your local disk as a button.
* A button can be used for submitting or resetting a form.
* Lists and drop-down lists are generally called multivalued containers. They both provide a list of values for users to select from at runtime. A list displays values in a box with or without scroll bar and is suitable for showing just a few values. A drop-down list is a good choice for providing a long list of values while taking smaller room and presenting more values at the first sight.

In most cases, these basic web controls are not used independently. They are bound with some web actions, or put into a form. When a basic web control is bound with web actions which will be triggered on certain events, any of the events applied to the web control will perform the web actions. In query-based page reports, you can also add basic web controls into a form, and then define the form according to your requirements, so that the inputs at runtime can be submitted to Server.

Currently, Designer does not support basic web controls in business view-based page reports and their usages are limited when used in the configuration panel of library components.

The following topics discuss basic web controls in further detail:

* [Using Basic Web Controls in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735527852183-Using-Basic-Web-Controls-in-a-Report)
* [Using Basic Web Controls in Library Component Configuration Panel](https://devnet.logianalytics.com/hc/en-us/articles/5735512656535-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component)
* [Using Forms in a Page Report](https://devnet.logianalytics.com/hc/en-us/articles/5735564508951-Using-Forms-in-a-Page-Report)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564487575-Working-with-Web-Controls)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527852183-Using-Basic-Web-Controls-in-a-Report)
