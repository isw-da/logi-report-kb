---
title: "Parameter - Web Action Builder Dialog Box"
id: 1500010098241
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010098241-Parameter-Web-Action-Builder-Dialog-Box
updated_at: 2021-07-23T19:15:50Z
---

# Parameter - Web Action Builder Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060162-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098221-Parameter-Order-Dialog-Box)

# Parameter - Web Action Builder Dialog Box

The Parameter-Web Action Builder dialog box helps you to [build a Parameter web action](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Parameter) on an object so as to run a specified report with the parameters defined in the dialog box when the event bound with the action is triggered at runtime. It appears when you select \*Parameter and select OK in the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box).

![Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856901399/prmwbactnbld.gif)

The following are details about options in the dialog box:

**Submit Action to Handler**

Specifies the handler to handle the action.

* **Default Handler in Current Server**  
   If selected, the action will be submitted to the current server to be handled.
* **Customized Path**  
  If selected, the action will be submitted to a customized path to be handled. For example, `http://127.0.0.1:8888/`.

**Get Input From**

Specifies where to get the object. You can select Form if you add some objects to a form. Otherwise, only the item Other in Report you can choose.

**Apply Action To**

* **Report**/**Library Component**  
   Specifies the report/library component which will be run with the parameters specified in the dialog box after the event bound with the action is triggered.
  + **Browse**  
    Searches for the desired report/library component. You can also type the path and file name of the report/library component in the text box manually.
  + **Web Control**  
    Specifies the web control from which the report/library component name is retrieved.
* **Target Frame**  
   Specifies the window or frame in which the report/library component will be opened.
  + **<Input>**  
    Allows you to type in the window or frame directly.
  + **Constant**
    - **blank** - Loads the report/library component into a new blank window. This window is not named.
    - **self** - Loads the report/library component into the window in which the link is selected (the active window).
    - **parent** - Loads the report/library component into the immediate parent window of the active window. If there is no parent window, the active window is used.
    - **top** - Loads the report/library component into the topmost window.
* **Refresh Current Report**/**Library Component**  
   If the option is selected, after the event bound with the action is triggered, the current report/library component will be re-run with the parameters specified in the dialog box.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a line to specify parameter value.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified parameter line.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified parameter line higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified parameter line lower in the list.

**Parameter Name**

Lists all the available parameters or web controls that can be selected to use as a parameter in the specified report/library component the action is applied to.

**Operator**

Shows the operator to compose the expression. It can only be =.

**Value**

Specifies the value for the parameter.

**OK**

Accepts the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060162-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098221-Parameter-Order-Dialog-Box)
