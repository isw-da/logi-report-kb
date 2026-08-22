---
title: "Customized Control \u2013 Web Action Builder Dialog"
id: 1500009586181
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586181-Customized-Control-Web-Action-Builder-Dialog
updated_at: 2021-07-24T05:55:31Z
---

# Customized Control – Web Action Builder Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586221-Customize-Dataset-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586201-Customized-Function-Dialog)

# Customized Control – Web Action Builder Dialog

The Customize Control-Web Action Builder dialog helps you to bind, create, or edit a [customized control](https://devnet.logianalytics.com/hc/en-us/articles/1500009584281-Using-Customized-Controls-in-a-Table). It is displayed when you do either of the following:

* Select Customized Control and then select OK in the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog) dialog.
* In the [Customized Control Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009587761-Manage-Customized-Controls-Dialog) dialog, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif). Then in the New Customized Control File dialog, provide a file name and select OK.
* In the Customized Control Manager dialog, right-click a customized control file and then select Edit from the shortcut menu.

[See the dialog](javascript:%20void(null)).

![Customized Control – Web Action Builder](https://devnet.logianalytics.com/hc/article_attachments/4404889372695/cstmzdctrlactn.gif)

The following are details about options in this dialog:

**Size**

Specifies the size of the customized control shown in the browser window at runtime.

* **Auto**  
   Specifies whether the control is automatically sized according to its contents.
* **Width**  
   Specifies the width of the control in pixels. Enabled when Auto is unchecked.
* **Height**  
   Specifies the height of the control in pixels. Enabled when Auto is unchecked.

**Position**

Specifies the position of the customized control in the browser window at runtime:

* **In the center of the browser window**  
   The customized control is placed in the center of the browser window at runtime.
* **According to mouse position**  
   The customized control is placed where the mouse is selected. The option is useful when the event is concerned with mouse action.
* **Relative to the trigger component**  
   The position of the customized control is placed where the trigger object is.
* **Absolute**  
   If the option is checked, you can further specify the following two options:
  + **Position X**  
     Specifies the absolute X position in pixels.
  + **Position Y**  
     Specifies the absolute Y position in pixels.

**Contents**

Input HTML fragment with JavaScript code. The HTML fragment should be plain text that is children DOM element of HTML Body.

**Save As**

Opens the [New Customized Control File](https://devnet.logianalytics.com/hc/en-us/articles/1500009587921-New-Customized-Control-File-Dialog) dialog to save the customized control properties into a file.

**OK**

* Saves the customized control properties into the web action and exits the current dialog if the dialog is opened after you select Customized Control and then select OK in the Web Action List dialog.
* Saves the customized control properties into the specified file and exits the current dialog if the dialog is opened after you select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) in the Customized Control Manger dialog and then provide a file name and select OK in the New Customized Control File dialog.
* Saves the changes to the customized control file if the dialog is opened after you right-click a customized control file and then select Edit from the shortcut menu in the Customized Control Manger dialog.

**Cancel**

Cancels the settings and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586221-Customize-Dataset-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586201-Customized-Function-Dialog)
