---
title: "Parameter Dialog"
id: 1500010032082
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010032082-Parameter-Dialog
updated_at: 2021-07-24T10:38:31Z
---

# Parameter Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067381-Page-Setup-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032102-Parameter-Web-Action-Builder-Dialog)

# Parameter Dialog

The Parameter dialog helps you to define the parameter values with which you want to run a library component as [a response to the message the current data component receives](https://devnet.logianalytics.com/hc/en-us/articles/1500010034842-Delivering-Messages-Between-Library-Components-#Receive) at runtime. Options in the dialog vary according to where the dialog is opened.

If the dialog is opened by selecting 0003 - Parameter from the drop-down list of the Message ID column and selecting ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) in the Actions column of the [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500010032262-Receive-Message-Dialog) dialog, it is used for defining to [receive the built-in Parameter message](https://devnet.logianalytics.com/hc/en-us/articles/1500010034842-Delivering-Messages-Between-Library-Components-#BParameter) at runtime.

![Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909122199/prm2.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a line to specify parameter value. Not available to the Customized type of the built-in message 0003 - Parameter.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected parameter line. Not available to the Customized type of the built-in message 0003 - Parameter.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected parameter up a step. Not available to the Customized type of the built-in message 0003 - Parameter.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected parameter down a step. Not available to the Customized type of the built-in message 0003 - Parameter.

**Parameter Name**

Lists all the parameters used by the library component in which the data component that receives the message is. Select one from the drop-down list or input the parameter name by yourself.

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

If the dialog is opened when you select a user defined message from the drop-down list of the Message ID column, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) in the Actions column of the [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500010032262-Receive-Message-Dialog) dialog, and then select \*Parameter and select OK in the displayed [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500010068321-Web-Action-List-Dialog) dialog, it is used for defining to [receive the user defined Parameter message](https://devnet.logianalytics.com/hc/en-us/articles/1500010034842-Delivering-Messages-Between-Library-Components-#UParameter) at runtime.

![Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909122455/prm.gif)

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
     Searches for the desired library component. You can also enter the path and file name of the library component in the text box manually.
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

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a line to specify parameter value.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected parameter.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected parameter up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected parameter down a step.

**Parameter Name**

Lists all the parameters used by the specified library component. Select one from the drop-down list or input the parameter name by yourself.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067381-Page-Setup-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032102-Parameter-Web-Action-Builder-Dialog)
