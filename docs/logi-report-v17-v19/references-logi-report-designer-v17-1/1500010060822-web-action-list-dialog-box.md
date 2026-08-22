---
title: "Web Action List Dialog Box"
id: 1500010060822
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box
updated_at: 2021-07-23T19:16:08Z
---

# Web Action List Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099141-Web-Behaviors-Dialog-Box)

# Web Action List Dialog Box

The Web Action List dialog box helps you to [bind web actions to an object](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#WebAction). It appears when you select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the Actions column in the Web Behaviors box of the [Display Type dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box), in the [Web Behaviors dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099141-Web-Behaviors-Dialog-Box), in the Behaviors tab of some chart formatting dialog boxes, or in the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098381-Receive-Message-Dialog-Box) when receiving a user-defined message.

![Web Action List dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848483863/wbactnlst.gif)

The following are details about options in the dialog box:

**Action Name**

Lists the names of actions. The actions that are available vary according to the report type.

* **Input an Action**  
  If selected, select OK to open the Input Action dialog box to type in an action and its parameter and bind it to the object. Available to page reports created using query resources only.
* **\*Parameter**  
  If selected, select OK to open the [Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098241-Parameter-Web-Action-Builder-Dialog-Box) or [Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060162-Parameter-Dialog-Box) to build the Parameter web action to the object or to define the Parameter action to respond to a received message.
* **\*Filter**  
  If selected, select OK to open the [Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096901-Filter-Web-Action-Builder-Dialog-Box) or [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096841-Filter-Dialog-Box) to build the Filter web action to the object or to define the Filter action to respond to a received message.
* **\*Sort**  
  If selected, select OK to open the [Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098821-Sort-Web-Action-Builder-Dialog-Box) or [Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060522-Sort-Dialog-Box) to build the Sort web action to the object or to define the Sort action to respond to a received message.
* **\*Customized Control**  
  If selected, select OK to open the [Customized Control – Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096001-Customized-Control-Web-Action-Builder-Dialog-Box) to bind a [customized control web action](https://devnet.logianalytics.com/hc/en-us/articles/1500010057402-Using-Customized-Controls-in-Tables).
* **\*Customized Control from Lib**   
  If selected, select OK to open the [Manage Customized Controls dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097881-Manage-Customized-Controls-Dialog-Box) to reference a customized control file from the library.
* **\*Property**  
  If selected, select OK to open the [Change Property - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095661-Change-Property-Web-Action-Builder-Dialog-Box) or [Change Property dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058142-Change-Property-Dialog-Box) to build the Change Property web action to the object or to define the Change Property action to respond to a received message. The action is not available to page reports.
* **\*Go Down**  
  If selected, select OK to open the [Go Down - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059502-Go-Down-Web-Action-Builder-Dialog-Box) or [Go Down dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059482-Go-Down-Dialog-Box) to build the Go Down web action to the object or to define the Go Down action to respond to a received message. The action is not available to page reports.
* **\*Go Up**  
  If selected, select OK to open the [Go Up - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097441-Go-Up-Web-Action-Builder-Dialog-Box) or [Go Up dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097421-Go-Up-Dialog-Box) to build the Go Up web action to the object or to define the Go Up action to respond to a received message. The action is not available to page reports.
* **\*Go To**  
  If selected, select OK to open the [Go To - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097401-Go-To-Web-Action-Builder) or [Go To dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059522-Go-To-Dialog-Box) to build the Go To web action to the object or to define the Go To action to respond to a received message. The action is not available to page reports.
* **\*On-screen Filter**  
  If selected, select OK to open the [On-screen Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060022-On-screen-Filter-Dialog-Box) to define the On-screen Filter web action to respond to a received message. The action is available to library components only when the dialog box is opened from the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098381-Receive-Message-Dialog-Box).
* **\*Remove Filter**  
  If selected, select OK to open the [Remove Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060262-Remove-Filter-Dialog-Box) to define the Remove Filter web action to respond to a received message. The action is available to library components only when the dialog box is opened from the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098381-Receive-Message-Dialog-Box).
* **\*SendMessage**  
  If selected, select OK to open the [Send Message - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060502-Send-Message-Web-Action-Builder-Dialog-Box) to bind the Send Message web action to the object. The action is available to library components only.
* **User defined web action - without parameter**  
  If selected, select OK to bind the selected action to the web control. The action is available to page reports created using query resources only.
* **User defined web action - with parameter**  
  If selected, select OK and the Parameters dialog box will appear for you to specify values of the parameters the selected web action requires. The action is available to page reports created using query resources only.

**Notes**

Displays tips about the specified action.

**OK**

Accepts the changes and closes the dialog box.

**Cancel**

Discards the changes and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099141-Web-Behaviors-Dialog-Box)
