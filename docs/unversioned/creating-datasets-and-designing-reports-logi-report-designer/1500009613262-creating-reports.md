---
title: "Creating Reports"
id: 1500009613262
section: "Creating Datasets and Designing Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports
updated_at: 2021-07-24T16:03:23Z
---

# Creating Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613242-Designing-Your-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613382-Opening-Reports)

# Creating Reports

This topic introduces how to create page and web reports. Before you can create reports in Logi Report Designer, you need to first [create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Create) to connect with your database or [open an exiting catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open).

In Logi Report Designer, the data resources that can be used to create different report types vary. Web reports and library components can only be created using [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009635921-Business-Views). For page reports, the following data resources are supported: business views, [queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries), [stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500009606802-Stored-Procedures), [imported SQLs](https://devnet.logianalytics.com/hc/en-us/articles/1500009606822-Creating-and-Importing-SQL-Statements), [imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/1500009606942-Imported-APEs), [user defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500009606982-User-Defined-Data-Sources)  and [hierarchical data sources.](https://devnet.logianalytics.com/hc/en-us/articles/1500009606722-Hierarchical-Data-Sources) In Logi Report Server, end users can create ad hoc web reports and page reports using business views via Web/Page Report Studio, and web reports and page reports created in Web/Page Report Studio can also be [downloaded to Logi Report Designer](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources#DownReport) for editing.

This topic includes the following sections:

* [Creating Page Reports](#Page)
* [Creating Page Report Tabs](#Tab)
* [Creating Web Reports](#Web)
* [Creating Library Components](#LC)
  + [Saving Data Components in a Web Report as Library Components](#BySave)
  + [Defining the Configuration Panel for Library Components](#Config)

## Creating Page Reports

Creating a page report will automatically create a report tab in the page report.

1. Select **Home**> **New** > **Page Report** or **File** > **New** > **Page Report**. The [Select Component for Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009633461-Select-Component-for-Page-Report-Dialog) dialog appears.

   ![Select Component for Page Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911627159/slctcmpntpgrpt.gif)
2. In the Report Title text box, specify the title of the first report tab in the page report.
3. Decide the data resource type for the page report. A page report can be created from either query resources or business views. To use business view as the data resource for the page report, select the **Create Using Business View** checkbox.
4. Select the component that is to be created in the first report tab in the page report.

## Creating Page Report Tabs

Before you can create report tabs, you first need to create a page report or [open an existing page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009613382-Opening-Reports). Then,

1. Do either of the following:
   * Select **Home** > **New** > **Page Report Tab**.
   * Select **File** > **New** > **Page Report Tab**.
   * On the report tab bar, right-click an existing report tab in the report and select **Insert** on the shortcut menu.

     ![Page Report Tab Bar](https://devnet.logianalytics.com/hc/article_attachments/4404904187287/rpt_crt_tab.gif)

   The [Select Component for Page Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009633501-Select-Component-for-Page-Report-Tab-Dialog) dialog appears.

   ![Select Component for Page Report Tab dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911627415/slctcmpntpgrpttb.gif)
2. In the Report Title text box, specify the title of the report tab. If you do not want a title, remove the text in the text box. The title is not used as the report tab name. For how to name a report tab, [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009613342-Managing-Page-Reports#Rename).
3. Select the component to add in the report tab.

   Logi Report provides you with the following component types to start a page report tab. The component types available for a report tab vary with the data resource type specified for the page report to which the report tab is to be added, which is determined at the time when the page report is created via the [Create Using Business View](#BV) option. Once defined, all the data components in the page report can only be created on the specified data resource type.

   * **Chart**  
      Creates a report tab containing a chart.
   * **Table (Group Above)**   
      Creates a report tab containing a table with group information above the detail row.
   * **Table (Group Left)**   
      Creates a report tab containing a table with group information left to the detail row.
   * **Table (Group Left Above)**   
      Creates a report tab containing a table with group information left above the detail row.
   * **Summary Table**  
      Creates a report tab containing a table with only group and summary information.
   * **Crosstab**  
      Creates a report tab containing a crosstab.
   * **Banded**  
      Creates a report tab containing a vertical banded object.
   * **Horizontal Banded**  
      Creates a report tab containing a horizontal banded object. Not available when creating a report tab in a page report that is based on business views.
   * **Mailing Label**  
      Creates a report tab containing a banded object, which is in the form of a mailing label layout. Not available when creating a report tab in a page report that is based on business views.
   * **Tabular**  
      Creates a report tab with a tabular which partitions the report page into several parts. Not available when creating a report tab in a page report that is based on business views.
   * **Blank**  
      Creates a report tab with nothing in it.
4. Select **OK**.
   * If the chart, table, crosstab or banded component type is selected, the corresponding wizard is displayed for you to create the data component. You can select the **Page Setup** button in the wizard to set the page settings for the report tab in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog. For details about how to define the data component, see the following topics:
     + [Inserting Charts in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009628941-Inserting-Charts-in-a-Report)
     + [Inserting Tables in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009629281-Inserting-Tables-in-a-Report-)
     + [Inserting Crosstabs in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009629041-Inserting-Crosstabs-in-a-Report)
     + [Inserting Banded Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009605502-Inserting-a-Banded-Object)   
        A banded object in a page report that is based on query resources can be a standard banded object, a horizontal banded object or a mailing label banded object. The steps for creating a banded object in any of the three layouts are mostly the same, just that the banded object is positioned differently in each layout: one in a vertical way, one horizontally and one in the form of mailing labels.

     When you create a report tab with a table, crosstab or banded object in it into a page report that is based on query resources, the Chart screen is available in the report wizard, using which you can create a chart together with the data component. The chart can only be defined based on the data fields that have been added to the data component.

     ![Chart Screen](https://devnet.logianalytics.com/hc/article_attachments/4404904192279/rpt_crt_cht.gif)

     **To define the chart:**

     1. Select a radio button to select the chart type you like.
     2. From the Category drop-down list, select the field to display on the category (X) axis of the chart. To define the chart based on a table or banded object, you can choose from the group-by fields of the table or banded object on which some summaries are added; to define on a crosstab, you can choose from all the fields added to the column and row headers of the crosstab.
     3. Choose the field to display on the series (Z) axis of the chart from the Series drop-down list. To define the chart based on a table or banded object, you can choose from all the group-by fields of the table or banded object; to define on a crosstab, you can choose from all the fields added to the column and row headers of the crosstab.
     4. From the Show Values drop-down list, select the field to display on the value (Y) axis of the chart. To define the chart based on a table or banded object, you can choose from the summaries which are calculated based on the field you specify to display on the category axis of the chart; to define on a crosstab, you can choose from the aggregate fields in the crosstab.

     When the report tab is created, the chart will be put in the report body together with the table or crosstab, or in the banded header panel of the banded object.
   * If Tabular is selected, the Tabular Wizard is displayed. Specify the number of rows and columns, and the border width and tabular width respectively. You can also select the **Page Setup** button to set the page settings for the report tab in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog. After the tabular is created, you can insert components and texts into the tabular cells and their layout will be controlled by the cells. A tabular helps you better design the report page. For details about how to work with tabulars, refer to [Tabulars](https://devnet.logianalytics.com/hc/en-us/articles/1500009629321-Tabulars).

     ![Tabular Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404904192535/tbulrwzd.gif)
   * If Blank is selected, the [Choose Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009607382-Choose-Data-Dialog) dialog is displayed, prompting you to select the data resource on which to create the report tab. Depending on the data resource type the page report to which the report tab is to be added is specified, you can choose either from query resources or business views in the current catalog. After the blank report tab is created, you can then insert the required objects into the report tab as described in [Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports).

     When selecting from query resources, if the given data resources are not what you want, you can select the first item in the corresponding resource node to create one. When a query is selected, you can select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog). Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report. If you want to use an existing dataset in the current page report for the page report tab, select the **More Options** button, then select the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog), or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report will still run the query separately for each dataset.

     ![Choose Data dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904192791/chsdt.gif)

## Creating Web Reports

1. Select **Home** > **New** > **Web Report** or **File** > **New** > **Web Report**.
2. A blank web report with a tabular of one cell is displayed. You can then split the [tabular](https://devnet.logianalytics.com/hc/en-us/articles/1500009629321-Tabulars) and insert components to the tabular cells. For details, see the corresponding topic about the specific component in [Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports).

## Creating Library Components

1. Select**Home** > **New** > **Library Component** or **File** > **New** > **Library Component**. The Select Component for Library Component dialog appears.

   ![Select Component for Library Component dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911627671/slctcmpntlc.gif)
2. Type a title for the library component in the Library Component Title text box.
3. Select the type for the first data component in the library component.
4. If Blank is selected, a blank library component is created; if a specific component type is selected, follow the wizard to create the data component in the library component. For details about how to define the data component, see the following topics:
   * [Inserting Charts in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009628941-Inserting-Charts-in-a-Report)
   * [Inserting Tables in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009629281-Inserting-Tables-in-a-Report-)
   * [Inserting Crosstabs in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009629041-Inserting-Crosstabs-in-a-Report)
5. You can insert more components, such as charts, crosstabs, tables, KPIs, web controls, and so on into the library component. For details, see the corresponding topic about the specific component in [Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports).

A library component in Logi Report Designer contains three parts:

* Wrapper defines some basic properties of the library component, such as the author, title and description of the library component. The title bar of a library component is included in the wrapper. You can edit these [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009613082-Wrapper-Properties) in the Report Inspector.
* [Configuration Panel](#Config) can be used at runtime to set parameter values for the library component, filter or sort the library component, or change properties of the components in the contents.
* Contents contains three objects: Body, Data Source and Page Panel. Body is the container that can hold a number of components such as charts, crosstabs, tables, geographic maps, labels, images, web controls, and so on. Data Source contains the [datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets) the data components in the body use and the [Refresh Object](https://devnet.logianalytics.com/hc/en-us/articles/1500011552882-Refresh-Object-Properties) of each business view on which the datasets are based. Page Panel controls the [page settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages#Setting) for printing and exporting the library component.

### Saving the Data Components in a Web Report as Library Components

Logi Report also supports saving the data components: tables, charts (including the KPI charts in KPIs), crosstabs, and geographic maps in a web report as library components, provided that all the objects in the data components can be supported by library components.

1. Open the web report which contains the data components you want to save as library components.
2. Right-click a data component and select **Save as Library Component** from the shortcut menu.
3. In the Save As dialog, specify the name for the library component in the File Name text box.
4. The library component file type (\*.lc) is the only default value in the Files of Type drop-down list.
5. Select **Save**. The Library Component Setting dialog appears.

   ![Library Component Setting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911627927/lcsting.gif)
6. Specify the title, author and the author's e-mail address in the Title text box, Author text box and Author Email text box respectively.
7. Select **OK** to save the selected data component as a library component with the specified name and title.
8. Repeat the above steps to save another data components in the web report as library components.

### Defining the Configuration Panel for Library Components

If you want the dashboard users to make use of the configuration panel at runtime, you need to configure the panel for each library component in Logi Report Designer.

To display the configuration panel of a library component, select the **Display Configuration Panel** checkbox on the top-right corner of the design area. The height of the configuration panel can be adjusted to the size of the contents, but its width is equal to the width of the library component and cannot be adjusted. You can resize its width only by resizing the width of the library component.

![Configuration Panel of Library Component](https://devnet.logianalytics.com/hc/article_attachments/4404904193047/rpt_crt_cfgpnl1.gif)

The initial configuration panel contains a checkbox and two buttons.

* The checkbox in the configuration panel is used to specify whether to show the panel by default when the library component is inserted into a dashboard in JDashboard. You can select the checkbox by setting the Default Show property of the configuration panel to true in the Report Inspector as well.
* All actions in the configuration panel are bound with the OK and Cancel buttons in it. You can select OK to apply the actions to the library component. The button Cancel is used to make this panel invisible and initialize the value of the web controls to the last values.The two buttons are built-in buttons so they cannot be deleted, cut, copied, or pasted, but their properties can be edited in the Report Inspector and they can be moved by dragging and dropping.

You can [insert labels](https://devnet.logianalytics.com/hc/en-us/articles/1500009606282-Labels#Insert) and [use web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009606662-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component) such as Text Field, Checkbox, List, nd Drop-down List in the configuration panel to filter or sort a library component, or change properties of objects in a library component.

When a library component contains parameters, the configuration panel will be automatically populated with all the parameters needed to run the library component, and web controls for the parameters will be created automatically in the panel. Therefore, the configuration panel can also be used to specify parameter values for a library component at runtime. The values of the parameters saved in the library component will be used as the default values.

![Configuration Panel of Library Conponent for Specifying Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/4404911628183/rpt_crt_cfgpnl2.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613242-Designing-Your-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613382-Opening-Reports)
