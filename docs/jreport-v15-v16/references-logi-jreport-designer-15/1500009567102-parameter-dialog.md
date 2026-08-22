---
title: "Parameter Dialog"
id: 1500009567102
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009567102-Parameter-Dialog
updated_at: 2021-07-24T05:54:57Z
---

# Parameter Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009588241-Parameter-Web-Action-Builder-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588201-Parameter-Order-Dialog)

# Parameter Dialog

The Parameter dialog helps you to define the parameter values with which you want to run a library component as a response to the [message](https://devnet.logianalytics.com/hc/en-us/articles/1500009570842-Delivering-Messages-Between-Library-Components) the current data component receives at runtime. Options in the dialog vary according to where the dialog is opened.

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

When the dialog is opened by selecting 0003 - Parameter from the drop-down list of the Message ID column and selecting ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the Actions column of the [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009567242-Receive-Message-Dialog) dialog, options in the dialog are as follows. [See the dialog](javascript:%20void(null)).

![Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889291799/prm2.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a line to specify parameter value. Not available to the Customized type of the built-in message 0003 - Parameter.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected parameter line. Not available to the Customized type of the built-in message 0003 - Parameter.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected parameter up a step. Not available to the Customized type of the built-in message 0003 - Parameter.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected parameter down a step. Not available to the Customized type of the built-in message 0003 - Parameter.

**Parameter Name**

Lists all the parameters used by the library component in which the data component that receives the message is. Select one from the drop-down list or input the parameter name by yourself.

**Operator**

Shows the operator to compose the expression. It can only be =.

**Value**

Specifies the value for the parameter.

When the dialog is opened by selecting \*Parameter and selecting OK in the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog) dialog, options in the dialog are as follows. [See the dialog](javascript:%20void(null)).

![Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893813399/prm.gif)

**Submit Action to Handler**

Specifies the handler to handle the action.

* **Default Handler in Current Server**  
   If selected, the action will be submitted to the current server to be handled.
* **Customized Path**  
   If selected, the action will be submitted to a customized path to be handled. For example, `http://127.0.0.1:8888/`.

**Get Input From**

Specifies where to get the object. Not supported here.

**Apply Action To**

* **Library Component**   
   Specifies the library component which will be run with the parameter values defined in the dialog when the message is received.
  + **Browse**  
     Searches for the desired library component. You can also enter the path and file name of the library component in the text field manually.
  + **Web Control**  
     Specifies the web control from which the report name is retrieved. Not supported here.
* **Target Frame**  
   Specifies the window or frame in which the library component will be opened.
  + **<Input>**  
     Allows you to input the window or frame directly.
  + **Constant**
    - **blank** - Loads the library component into a new blank window. This window is not named.
    - **self** - Loads the library component into the window in which the link is selected (the active window).
    - **parent** - Loads the library component into the immediate parent window of the active window. If there is no parent window, the active window is used.
    - **top** - Loads the library component into the topmost window.
* **Refresh Current Library Component**  
   If checked, the current library component will be re-run with the parameter values defined in the dialog when the message is received.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a line to specify parameter value.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected parameter.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected parameter up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected parameter down a step.

**Parameter Name**

Lists all the parameters used by the specified library component. Select one from the drop-down list or input the parameter name by yourself.

**Operator**

Shows the operator to compose the expression. It can only be =.

**Value**

Specifies the value for the parameter.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009588241-Parameter-Web-Action-Builder-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588201-Parameter-Order-Dialog)
