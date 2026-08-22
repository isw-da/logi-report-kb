---
title: "Parameter Dialog"
id: 1500009632921
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009632921-Parameter-Dialog
updated_at: 2021-07-24T16:04:17Z
---

# Parameter Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009609762-Parameter-Web-Action-Builder-Dialog)

# Parameter Dialog

The Parameter dialog helps you to define the parameter values with which you want to run a library component as [a response to the message the current data component receives](https://devnet.logianalytics.com/hc/en-us/articles/1500009613362-Delivering-Messages-Between-Library-Components-#Receive) at runtime.

The dialog varies according to different source it is opened from.

---

If the dialog is opened by selecting 0003 - Parameter from the drop-down list of the Message ID column and selecting ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the Actions column of the [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009610002-Receive-Message-Dialog) dialog, it is used for defining to [receive the built-in Parameter message](https://devnet.logianalytics.com/hc/en-us/articles/1500009613362-Delivering-Messages-Between-Library-Components-#BParameter) at runtime.

![Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904184471/prm2.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Adds a line to specify parameter value. Not available to the Customized type of the built-in message 0003 - Parameter.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected parameter line. Not available to the Customized type of the built-in message 0003 - Parameter.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected parameter up a step. Not available to the Customized type of the built-in message 0003 - Parameter.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected parameter down a step. Not available to the Customized type of the built-in message 0003 - Parameter.

**Parameter Name**

Lists all the parameters used by the library component in which the data component that receives the message is. Select one from the drop-down list or type in the parameter name by yourself.

**Operator**

Shows the operator to compose the expression. It can only be =.

**Value**

Specifies the value for the parameter.

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

---

If the dialog is opened when you select a user defined message from the drop-down list of the Message ID column, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the Actions column of the [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009610002-Receive-Message-Dialog) dialog, and then select \*Parameter and select OK in the displayed [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog, it is used for defining to [receive the user defined Parameter message](https://devnet.logianalytics.com/hc/en-us/articles/1500009613362-Delivering-Messages-Between-Library-Components-#UParameter) at runtime.

![Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904185111/prm.gif)

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
    Searches for the desired library component. You can also type the path and file name of the library component in the text box manually.
  + **Web Control**  
    Specifies the web control from which the report name is retrieved. Not supported here.
* **Target Frame**  
  Specifies the window or frame in which the library component will be opened.
  + **<Input>**  
    Allows you to type in the window or frame directly.
  + **Constant**
    - **blank** - Loads the library component into a new blank window. This window is not named.
    - **self** - Loads the library component into the window in which the link is selected (the active window).
    - **parent** - Loads the library component into the immediate parent window of the active window. If there is no parent window, the active window is used.
    - **top** - Loads the library component into the topmost window.
* **Refresh Current Library Component**  
   If the option is selected, the current library component will be re-run with the parameter values defined in the dialog when the message is received.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Adds a line to specify parameter value.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected parameter.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected parameter up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected parameter down a step.

**Parameter Name**

Lists all the parameters used by the specified library component. Select one from the drop-down list or type in the parameter name by yourself.

**Operator**

Shows the operator to compose the expression. It can only be =.

**Value**

Specifies the value for the parameter.

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009609762-Parameter-Web-Action-Builder-Dialog)
