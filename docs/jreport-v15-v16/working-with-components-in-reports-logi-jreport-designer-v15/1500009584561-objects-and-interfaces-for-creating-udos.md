---
title: "Objects and Interfaces for Creating UDOs"
id: 1500009584561
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584561-Objects-and-Interfaces-for-Creating-UDOs
updated_at: 2021-07-24T05:55:53Z
---

# Objects and Interfaces for Creating UDOs

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563782-UDOs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584501-Creating-a-UDO-Manually)

# Objects and Interfaces for Creating UDOs

The following objects and interfaces are necessary for creating a UDO. Refer to the corresponding class or interface in the Logi JReport Javadoc located at `<install_root>\help\api`.

* **Jet.report.JRObjectTemplate**  
   This is an object provided by the Logi JReport system, and is used to derive a UDO. The JRObjectTemplate contains several predefined properties of the standard Logi JReport Object used to compose a report, including: X, Y, Height and Width. You can add more properties (supported by Logi JReport system) to your own UDO. These properties can be viewed and modified by the Report Inspector at design time.

  **Note:** Only Logi JReport system properties or properties inherited from them can be added, such as JetNumber, JetColor, JetString, and JetEnumeration. See the jet.controls package.
* **jet.datastream.JRVisiableResult**  
   This is another object provided by the Logi JReport system. You will need to define an object inherited from this object, so that you can specify the methods for saving and restoring the UDO object. JRVisiableResult provides methods for saving and restoring UDOs.
* **jet.datastream.JRObjectResult**  
   If the UDO you define is not used for displaying, that is, it will not appear inside the report result on the screen or on paper, then it can be inherited from the JRObjectResult object.
* **jet.udo.JRObjectResultCreator**  
   This is an interface. It takes Logi JReport system's Logi JReport Record as input parameters and produces the UDO's JRObjectResult. A definition of the Logi JReport Record is in the jet.connect package.
* **jet.udo.JRObjectRender**  
   This is another interface. It provides a method used for painting the UDO to the report. The report can then be shown on the screen or printed on a printer.
* **jet.udo.JRObjectEditor**  
   This is an optional interface. If specified, the Logi JReport system will use it to handle interactive events (key events, mouse events, paint, and so on) at design time. If this interface is not implemented, the Logi JReport system will use the default one.
* **jet.udo.JRGroupListener**  
   This interface is used when you define a UDO with a value which is calculated based on a group of data.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563782-UDOs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584501-Creating-a-UDO-Manually)
