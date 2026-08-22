---
title: "Library Components"
id: 1500009592681
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592681-Library-Components
updated_at: 2021-07-24T05:53:50Z
---

# Library Components

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component)

# Library Components

Library components are created and edited in Logi JReport Designer, and then published along with their catalog to the component library in Logi JReport Server for use in dashboards (for details, see the JDashboard chapter in the *Logi JReport Server User's Guide*).

A library component contains three parts: wrapper, configuration and content.

* The wrapper defines some basic properties of the library component, such as the properties of the title and the CSS class that will be applied to the title bar. In addition, it also defines the auto-refresh rules, such as whether to enable auto refresh and the type of auto refresh. You can select the wrapper by selecting the Wrapper node in the Report Inspector.
* The configuration panel shows the title bar and the panel is used to set parameter values for the library component, filter or sort on the library component, or change properties of the library component in the content. You can display the configuration panel by checking the Display Configuration Panel checkbox on the top-right corner.
* The content contains a body and a page panel which has no page header or page footer. The body is a container that can hold a number of components such as charts, crosstabs, tables, geographic maps, labels, images, web controls and so on. The page panel is used to print or export the library component.

The content supports auto fit only when the library component is published into the component library in Logi JReport Server and is used in JDashboard. The style of the title bar, configuration panel and content borders are controlled by the JDashboard theme and the library component view in JDashboard is of the same style, which can only be edited in the CSS file instead of being edited individually. While, the body in the content and the components in the body, such as tables, charts, labels and so on can have their own formats and their properties that can be edited individually.

The following topics provide more information about what you can do with library components in Logi JReport Designer:

> * [Creating a Library Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component)
> * [Using the Configuration Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009570822-Using-the-Configuration-Panel)
> * [Delivering Messages Between Library Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009570842-Delivering-Messages-Between-Library-Components)
> * [Previewing a Library Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009592781-Previewing-a-Library-Component)
> * [Opening a Library Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009592761-Opening-a-Library-Component)
> * [Saving a Library Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009570882-Saving-a-Library-Component)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component)
