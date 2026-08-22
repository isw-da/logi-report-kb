---
title: "Creating a Library Component"
id: 1500009592701
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component
updated_at: 2021-07-24T05:53:50Z
---

# Creating a Library Component

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592681-Library-Components)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570822-Using-the-Configuration-Panel)

# Creating a Library Component

The data resources that can be used to create library components are [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views). You can use dynamic resources and local parameters in a library component the same as you do in a web report. For details, see the [same topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) on web report.

Below is a list of the sections covered in this topic:

> * [Creating as a New Component](#New)
> * [Creating by Saving a Data Component in a Web Report](#Save)

## Creating as a New Component

1. Select**Home** > **New** > **Library Component** or **File** > **New** > **Library Component**. The Select Component for Library Component dialog appears.

   ![Select Component for Library Component dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893815063/slctcmpntlc.gif)
2. Input a title for the library component in the Library Component Title text box.
3. Select the type for the first data component in the library component.
4. If Blank is selected, a blank library component is created; if a specific component type is selected, follow the wizard to create the data component in the library component. For details about how to define the data component, see the following topics:
   * [Inserting a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009563242-Inserting-a-Chart)
   * [Insert a Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table)
   * [Insert a Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009583881-Inserting-a-Crosstab)
5. Insert other components, such as charts, crosstabs, tables, KPI components, web controls and so on into the library component if needed. For details, see the corresponding topic about the specific component in the [Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports) chapter.
6. If required, equip the library component with a [configuration panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009570822-Using-the-Configuration-Panel), which can be used to specify parameter values when there are parameters used in the library component, to filter or sort on the library component, or to change properties of the library component.

When a library component is created, you can also further modify it the same as you do with a page report. For details, see [Editing a Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report).

## Creating by Saving a Data Component in a Web Report

The data components: tables, charts (including the KPI charts in KPI components), crosstabs, and geographic maps, in a [web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports) can be saved as a library component, provided that all the objects in the data components can be supported by library components.

**To save a data component in a web report as a library component:**

1. Open the web report which contains the data component you want to save as a library component.
2. Right-click the data component and select **Save as Library Component** from the shortcut menu.
3. In the Save As dialog, specify the name for the library component in the File Name text box.
4. The library component file type (\*.lc) is the only default value in the Files of Type drop-down list.
5. Select **Save**. The Library Component Setting dialog appears.

   ![Library Component Setting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893815319/lcsting.gif)
6. Specify the title, author and the author's e-mail address in the Title text box, Author text box and Author Email text box respectively.
7. Select **OK** to save the selected data component as a library component with the specified name and title.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592681-Library-Components)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570822-Using-the-Configuration-Panel)
