---
title: "Web Action List Dialog"
id: 1500009633961
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog
updated_at: 2021-07-24T16:04:01Z
---

# Web Action List Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610722-User-Defined-Group-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633981-Web-Behaviors-Dialog)

# Web Action List Dialog

The Web Action List dialog helps you to [bind web actions to an object](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#WebAction). It appears when you select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the Actions column in the Web Behaviors box of the [Display Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009630461-Display-Type-Dialog) dialog, in the [Web Behaviors](https://devnet.logianalytics.com/hc/en-us/articles/1500009633981-Web-Behaviors-Dialog) dialog, in the Behaviors tab of some chart formatting dialogs, or in the [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009610002-Receive-Message-Dialog) dialog when receiving a user defined message.

![Web Action List dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904233623/wbactnlst.gif)

The following are details about options in the dialog:

**Action Name**

Lists the names of actions. The actions that are available vary according to the report type.

* **Input an Action**  
  If selected, select OK to open the Input Action dialog to type in an action and its parameter and bind it to the object. Available to page reports created using query resources only.
* **\*Parameter**  
  If selected, select OK to open the [Parameter - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009609762-Parameter-Web-Action-Builder-Dialog) dialog or [Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009632921-Parameter-Dialog) dialog to build the Parameter web action to the object or to define the Parameter action to respond to a received message.
* **\*Filter**  
  If selected, select OK to open the [Filter - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009631221-Filter-Web-Action-Builder-Dialog) dialog or [Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009631201-Filter-Dialog) dialog to build the Filter web action to the object or to define the Filter action to respond to a received message.
* **\*Sort**  
  If selected, select OK to open the [Sort - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009610462-Sort-Web-Action-Builder-Dialog) dialog or [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009610442-Sort-Dialog) dialog to build the Sort web action to the object or to define the Sort action to respond to a received message.
* **\*Customized Control**  
  If selected, select OK to open the [Customized Control – Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009630321-Customized-Control-Web-Action-Builder-Dialog) dialog to bind a [customized control web action](https://devnet.logianalytics.com/hc/en-us/articles/1500009606462-Using-Customized-Controls-in-Tables).
* **\*Customized Control from Lib**   
  If selected, select OK to open the [Customized Control Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009632401-Manage-Customized-Controls-Dialog) dialog to reference a customized control file from the library.
* **\*Property**  
  If selected, select OK to open the [Change Property - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009629981-Change-Property-Web-Action-Builder-Dialog) dialog or [Change Property](https://devnet.logianalytics.com/hc/en-us/articles/1500009629961-Change-Property-Dialog) dialog to build the Change Property web action to the object or to define the Change Property action to respond to a received message. The action is not available to page reports.
* **\*Go Down**  
  If selected, select OK to open the [Go Down - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009631781-Go-Down-Web-Action-Builder-Dialog) dialog or [Go Down](https://devnet.logianalytics.com/hc/en-us/articles/1500009631761-Go-Down-Dialog) dialog to build the Go Down web action to the object or to define the Go Down action to respond to a received message. The action is not available to page reports.
* **\*Go Up**  
  If selected, select OK to open the [Go Up - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009608762-Go-Up-Web-Action-Builder-Dialog) dialog or [Go Up](https://devnet.logianalytics.com/hc/en-us/articles/1500009631841-Go-Up-Dialog) dialog to build the Go Up web action to the object or to define the Go Up action to respond to a received message. The action is not available to page reports.
* **\*Go To**  
  If selected, select OK to open the [Go To - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009631821-Go-To-Web-Action-Builder-Dialog) dialog or [Go To](https://devnet.logianalytics.com/hc/en-us/articles/1500009631801-Go-To-Dialog) dialog to build the Go To web action to the object or to define the Go To action to respond to a received message. The action is not available to page reports.
* **\*On-screen Filter**  
  If selected, select OK to open the [On-screen Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009632801-On-screen-Filter-Dialog) dialog to define the On-screen Filter web action to respond to a received message. The action is available to library components only when the dialog is opened from the [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009610002-Receive-Message-Dialog) dialog.
* **\*Remove Filter**  
  If selected, select OK to open the [Remove Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009633301-Remove-Filter-Dialog) dialog to define the Remove Filter web action to respond to a received message. The action is available to library components only when the dialog is opened from the [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009610002-Receive-Message-Dialog) dialog.
* **\*SendMessage**  
  If selected, select OK to open the [Send Message - Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009610422-Send-Message-Web-Action-Builder-Dialog) dialog to bind the Send Message web action to the object. The action is available to library components only.
* **User defined web action - without parameter**  
  If selected, select OK to bind the selected action to the web control. The action is available to page reports created using query resources only.
* **User defined web action - with parameter**  
  If selected, select OK and the Parameters dialog will appear for you to specify values of the parameters the selected web action requires. The action is available to page reports created using query resources only.

**Notes**

Displays tips about the specified action.

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Discards the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610722-User-Defined-Group-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633981-Web-Behaviors-Dialog)
