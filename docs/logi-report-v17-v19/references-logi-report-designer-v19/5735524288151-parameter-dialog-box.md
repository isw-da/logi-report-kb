---
title: "Parameter Dialog Box"
id: 5735524288151
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735524288151-Parameter-Dialog-Box
updated_at: 2022-11-02T07:53:22Z
---

# Parameter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735524319767-Parameter-Web-Action-Builder-Dialog-Box)

# Parameter Dialog Box

You can use the Parameter dialog box to define the parameter values using which to run a library component as a response to the message the current data component receives at runtime. This topic describes the options in the dialog box.

Designer displays different options in the dialog box according to the different sources where you open it.

---

If you open the Parameter dialog box by selecting 0003 - Parameter from the drop-down list of the Message ID column and selecting the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) in the Actions column of the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567115287-Receive-Message-Dialog-Box), you can use it to define [the built-in Parameter message](https://devnet.logianalytics.com/hc/en-us/articles/5735576827671-Delivering-Messages-Between-Library-Components#BParameter) for the current data component to receive at runtime.

![Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898423205399/prm2.gif)

Designer displays these options:

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**

Select to add a line to specify parameter value.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified parameter line.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified parameter line higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified parameter line lower in the list.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Designer disables the four buttons when you select the Customized type for the parameter message in the Receive Message dialog box.

**Parameter Name**

This column shows the parameters that you add to run the library component containing the data component with.

**Operator**

This column shows the operator to compose the parameter condition. It can only be "=".

**Value**

This column shows the values that you specify for the parameters.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

If you open the Parameter dialog box by selecting a user-defined message from the drop-down list of the Message ID column, selecting the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) in the Actions column of the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567115287-Receive-Message-Dialog-Box), and then selecting \*Parameter and selecting OK in the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735531755159-Web-Action-List-Dialog-Box), you can use it edit [the user-defined Parameter message](https://devnet.logianalytics.com/hc/en-us/articles/5735576827671-Delivering-Messages-Between-Library-Components#UParameter) for the current data component to receive at runtime.

![Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898473593879/prm.gif)

Designer displays these options:

**Submit Action to Handler**

Specify the handler to receive the parameters of the web action.

* **Default Handler in Current Server**  
  Select to submit the action to the current server to handle.
* **Customized Path**  
  Select to submit the action to a customized path to handle, for example, `http://127.0.0.1:8888/`.

**Get Input From**

Designer does not enable this option for defining a parameter message.

**Apply Action To**

Specify the target to which to apply the action involved in the message.

* **Library Component**   
  Select to run a specified library component using the parameter values defined in the dialog box when the data component receives the message. You can select **Browse** to the specify the library component or type the path and file name of the library component in the text box.
  + **Web Control**  
    Designer does not enable this option for defining a parameter message.
  + **Target Frame**  
    Select the window or frame to open the library component.
    - **<Input>**  
      Select and type the window or frame name in the text box.
    - **Constant**
      * **blank**  
        Select to load the library component into a new blank window. This window is not named.
      * **self**  
        Select to load the library component into the window from which the message is sent out (the active window).
      * **parent**  
        Select to load the library component into the immediate parent window of the active window. If there is no parent window, the active window is used.
      * **top**  
        Select to load the library component into the topmost window.
* **Refresh Current Library Component**  
  Select to rerun the current library component using the parameter values defined in the dialog box when the data component receives the message.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**

Select to add a line to specify parameter value.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified parameter line.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified parameter line higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified parameter line lower in the list.

**Parameter Name**

This column shows the parameters that you add to run the specified or current library component with.

**Operator**

This column shows the operator to compose the parameter condition. It can only be "=".

**Value**

This column shows the values that you specify for the parameters.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735524319767-Parameter-Web-Action-Builder-Dialog-Box)
