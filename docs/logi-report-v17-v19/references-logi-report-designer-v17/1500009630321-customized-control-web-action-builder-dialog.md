---
title: "Customized Control \u2013 Web Action Builder Dialog"
id: 1500009630321
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630321-Customized-Control-Web-Action-Builder-Dialog
updated_at: 2021-07-24T16:04:52Z
---

# Customized Control – Web Action Builder Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607622-Customize-Gauge-Angle-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630341-Customized-Function-Dialog)

# Customized Control – Web Action Builder Dialog

The Customized Control-Web Action Builder dialog helps you to bind, create, or edit a [customized control](https://devnet.logianalytics.com/hc/en-us/articles/1500009606462-Using-Customized-Controls-in-Tables). It appears when you do one of the following:

* Select Customized Control and then select OK in the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog.
* In the [Customized Control Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009632401-Manage-Customized-Controls-Dialog) dialog, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif). Then in the New Customized Control File dialog, provide a file name and select OK.
* In the Customized Control Manager dialog, right-click a customized control file and then select Edit from the shortcut menu.

![Customized Control – Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904362519/cstmzdctrlactn.gif)

The following are details about options in this dialog:

**Size**

Specifies the size of the customized control shown in the browser window at runtime.

* **Auto**  
   Specifies whether the control is automatically sized according to its contents.
* **Width**  
   Specifies the width of the control in pixels. Enabled when Auto is unselected.
* **Height**  
   Specifies the height of the control in pixels. Enabled when Auto is unselected.

**Position**

Specifies the position of the customized control in the browser window at runtime:

* **In the center of the browser window**  
   The customized control is placed in the center of the browser window at runtime.
* **According to mouse position**  
   The customized control is placed where the mouse is selected. The option is useful when the event is concerned with mouse action.
* **Relative to the trigger component**  
   The position of the customized control is placed where the trigger object is.
* **Absolute**  
   If the option is selected, you can further specify the following two options:
  + **Position X**  
     Specifies the absolute X position in pixels.
  + **Position Y**  
     Specifies the absolute Y position in pixels.

**Contents**

Specifies HTML fragment with JavaScript code. The HTML fragment should be plain text that is children DOM element of HTML Body.

**Save As**

Opens the [New Customized Control File](https://devnet.logianalytics.com/hc/en-us/articles/1500009609202-New-Customized-Control-File-Dialog) dialog to save the customized control definition into a file.

**OK**

* Saves the customized control definition into the web action and exits the current dialog if the dialog is opened after you select Customized Control and then select OK in the Web Action List dialog.
* Saves the customized control definition into the specified file and exits the current dialog if the dialog is opened after you select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) in the Customized Control Manger dialog and then provide a file name and select OK in the New Customized Control File dialog.
* Saves the changes to the customized control file if the dialog is opened after you right-click a customized control file and then select Edit from the shortcut menu in the Customized Control Manger dialog.

**Cancel**

Cancels the settings and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607622-Customize-Gauge-Angle-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630341-Customized-Function-Dialog)
