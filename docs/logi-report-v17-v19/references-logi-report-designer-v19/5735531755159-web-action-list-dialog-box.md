---
title: "Web Action List Dialog Box"
id: 5735531755159
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735531755159-Web-Action-List-Dialog-Box
updated_at: 2022-11-02T07:52:25Z
---

# Web Action List Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735544779031-User-Defined-Group-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735544817687-Web-Behaviors-Dialog-Box)

# Web Action List Dialog Box

You can use the Web Action List dialog box to [bind a web action to an object](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebAction). This topic describes the options in the dialog box.

Designer displays the Web Action List dialog box when you select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) in the Actions column in the Web Behaviors box of the [Display Type dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513570199-Display-Type-Dialog-Box), in the [Web Behaviors dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544817687-Web-Behaviors-Dialog-Box), in the Behaviors tab of some chart format dialog boxes, or in the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567115287-Receive-Message-Dialog-Box) when receiving a user-defined message.

![Web Action List dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898477209367/wbactnlst.gif)

Designer displays these options:

**Action Name**

This column shows the names of the actions that you can apply to the object. Designer displays different actions according to the report type.

* **Input an Action**  
  Designer displays this action for a query-based page report only. Select it to define an action by yourself.
* **\*Parameter**  
  Select to build the Parameter web action to the object or to define the Parameter action to respond to a received message. If you select the action, after you select OK in the dialog box, Designer displays the [Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524319767-Parameter-Web-Action-Builder-Dialog-Box) or [Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524288151-Parameter-Dialog-Box) for you to define the action.
* **\*Filter**  
  Select to build the Filter web action to the object or to define the Filter action to respond to a received message. If you select the action, after you select OK in the dialog box, Designer displays the [Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735500770711-Filter-Web-Action-Builder-Dialog-Box) or [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735509055895-Filter-Dialog-Box) for you to define the action.
* **\*Sort**  
  Select to build the Sort web action to the object or to define the Sort action to respond to a received message. If you select the action, after you select OK in the dialog box, Designer displays the [Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544459671-Sort-Web-Action-Builder-Dialog-Box) or [Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515567127-Sort-Dialog-Box) to for you to define the action.
* **\*Customized Control**  
  Select to bind a customized control web action to the object. If you select the action, after you select OK in the dialog box, Designer displays the [Customized Control – Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513478935-Customized-Control-Web-Action-Builder-Dialog-Box) for you to define the action.
* **\*Customized Control from Lib**  
  Select to reference a customized control file from the library for the object. If you select the action, after you select OK in the dialog box, Designer displays the [Manage Customized Controls dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566696983-Manage-Customized-Controls-Dialog-Box) for you to select the file.
* **\*Property**  
  Designer does not display this action for page reports. Select it to build the Change Property web action to the object or to define the Change Property action to respond to a received message. If you select the action, after you select OK in the dialog box, Designer displays the [Change Property - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508185111-Change-Property-Web-Action-Builder-Dialog-Box) or [Change Property dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565102615-Change-Property-Dialog-Box) for you to define the action.
* **\*Go Down**  
  Designer does not display this action for page reports. Select it to build the Go Down web action to the object or to define the Go Down action to respond to a received message. If you select the action, after you select OK in the dialog box, Designer displays the [Go Down - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735543300759-Go-Down-Web-Action-Builder-Dialog-Box) or [Go Down dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529999511-Go-Down-Dialog-Box) for you to define the action.
* **\*Go Up**  
  Designer does not display this action for page reports. Select it to build the Go Up web action to the object or to define the Go Up action to respond to a received message. If you select the action, after you select OK in the dialog box, Designer displays the [Go Up - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523517079-Go-Up-Web-Action-Builder-Dialog-Box) or [Go Up dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735514552215-Go-Up-Dialog-Box) for you to define the action.
* **\*Go To**  
  Designer does not display this action for page reports. Select it to build the Go To web action to the object or to define the Go To action to respond to a received message. If you select the action, after you select OK in the dialog box, Designer displays the [Go To - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566447127-Go-To-Web-Action-Builder-Dialog-Box) or [Go To dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523494423-Go-To-Dialog-Box) for your to define the action.
* **\*On-screen Filter**  
  Designer displays this action for library components and when you open the dialog box from the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567115287-Receive-Message-Dialog-Box) only. Select it to define the On-screen Filter web action to respond to a received message. If you select the action, after you select OK in the dialog box, Designer displays the [On-screen Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735543893271-On-screen-Filter-Dialog-Box) for you to define the action.
* **\*Remove Filter**  
  Designer displays this action for library components and when you open the dialog box from the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567115287-Receive-Message-Dialog-Box) only. Select it to define the Remove Filter web action to respond to a received message. If you select the action, after you select OK in the dialog box, Designer displays the [Remove Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515281559-Remove-Filter-Dialog-Box) for you to define the action.
* **\*SendMessage**  
  Designer displays this action for library components only. Select it to bind the Send Message web action to the object. If you select the action, after you select OK in the dialog box, Designer displays the [Send Message - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524850583-Send-Message-Web-Action-Builder-Dialog-Box) for you to define the action.
* **User-defined web action - without parameter**  
  Designer displays this type of actions for query-based page reports only. Select an action to bind it to the object.
* **User-defined web action - with parameter**  
  Designer displays this type of actions for query-based page reports only. When you select an action of this type, after you select OK in the dialog box, Designer displays the Parameters dialog box for you to specify values of the parameters the web action requires.

**Notes**

This column shows the tips about the actions.

**OK**

Select to apply the specified web action to the object and open the corresponding dialog box for building the action if there is any.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735544779031-User-Defined-Group-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735544817687-Web-Behaviors-Dialog-Box)
