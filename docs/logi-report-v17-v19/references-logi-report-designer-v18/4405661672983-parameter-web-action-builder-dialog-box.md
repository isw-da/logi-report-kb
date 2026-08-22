---
title: "Parameter - Web Action Builder Dialog Box"
id: 4405661672983
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661672983-Parameter-Web-Action-Builder-Dialog-Box
updated_at: 2022-01-27T20:35:49Z
---

# Parameter - Web Action Builder Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661671831-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664549015-Parameter-Order-Dialog-Box)

# Parameter - Web Action Builder Dialog Box

You can use the Parameter - Web Action Builder dialog box to [build a Parameter web action](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report#Parameter) on an object so as to run a specified report with the parameters defined in the dialog box when the event bound with the action is triggered at runtime. This topic describes the options in the dialog box.

Designer displays the Parameter - Web Action Builder dialog box when you select \*Parameter and select OK in the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661744791-Web-Action-List-Dialog-Box).

![Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556132503/prmwbactnbld.gif)

You see the following options in the dialog box:

**Submit Action to Handler**

Specify the handler to receive the parameters of the web action.

* **Default Handler in Current Server**  
  Select to submit the action to the current server to handle.
* **Customized Path**  
  Select to submit the action to a customized path to handle, for example, `http://127.0.0.1:8888/`.

**Get Input From**

Select where to get the input.

**Apply Action To**

* **Report**  
  Specify the report to run with the parameters specified in the dialog box after the event bound with the action is triggered.
  + **Browse**  
    Select to specify the desired report. You can also type the path and file name of the report in the text box.
  + **Web Control**  
    Select to use a web control to retrieve the report name at runtime.
* **Target Frame**  
   Select the window or frame to open the report.
  + **<Input...>**  
    Select and type the window or frame name in the text box.
  + **Constant**
    - **blank**  
      Select to load the report into a new blank window. This window is not named.
    - **self**  
      Select to load the report into the window in which the link is selected (the active window).
    - **parent**  
      Select to load the report into the immediate parent window of the active window. If there is no parent window, the active window is used.
    - **top**  
      Select to load the report into the topmost window.
* **Refresh Current Report**  
  Select to rerun the current report using the parameter values defined in the dialog box when the event bound with the action is triggered.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif)**Add button**

Select to add a line to specify parameter value.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**

Select to delete the specified parameter line.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif)**Move Up button**

Select to move the specified parameter line higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif)**Move Down button**

Select to move the specified parameter line lower in the list.

**Parameter Name**

This column shows the parameters that you add to run the specified or current report with.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661671831-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664549015-Parameter-Order-Dialog-Box)
