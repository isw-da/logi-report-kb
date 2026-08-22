---
title: "Creating Reports"
id: 4405661926423
section: "Creating Datasets and Designing Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports
updated_at: 2022-01-27T20:34:54Z
---

# Creating Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664697239-Choosing-the-Report-Type)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664694551-Opening-Reports)

# Creating Reports

In Designer, you can use either query resources or business views to create reports depending on the type of the reports. Web reports and library components can only be based on [business views](https://devnet.logianalytics.com/hc/en-us/articles/4405664680215-Working-with-Business-Views); page report can apply both business views and [queries](https://devnet.logianalytics.com/hc/en-us/articles/4405661915543-Working-with-Queries) (including the data resources that function like queries, such as [stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/4405661423383-Using-Stored-Procedures), [imported SQLs](https://devnet.logianalytics.com/hc/en-us/articles/4405661424407-Using-Imported-SQLs), [imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/4405664418583-Using-Imported-APEs), [user-defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/4405661435031-Using-User-Defined-Data-Sources), and [hierarchical data sources](https://devnet.logianalytics.com/hc/en-us/articles/4405664410263-Using-Hierarchical-Data-Sources)). In Server, end users can create ad hoc reports using business views; report designers can [download](https://devnet.logianalytics.com/hc/en-us/articles/4405661923607-Publishing-and-Downloading-Resources#DownReport) the ad hoc reports to Designer for editing. This topic introduces how you can create reports of different types in Designer and bind data to the report body.

Before you can create reports, you need to first [create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs#Create) to connect with your database or [open an existing catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs#Open).

This topic contains the following sections:

* [Creating Page Reports](#Page)
* [Creating Page Report Tabs](#Tab)
* [Creating Web Reports](#Web)
* [Creating Library Components](#LC)
  + [Saving Data Components in a Web Report as Library Components](#BySave)
  + [Defining the Configuration Panel for Library Components](#Config)
* [Binding Data to the Report Body](#BindData)

## Creating Page Reports

Creating a page report automatically creates a report tab in the page report.

1. Select **Home** > **New** > **Page Report** or **File** > **New** > **Page Report**. Designer displays the [Select Component for Page Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664570647-Select-Component-for-Page-Report-Dialog-Box).

   ![Select Component for Page Report dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542080663/slctcmpntpgrpt.gif)
2. In the **Report Title** text box, specify the title of the first report tab in the page report.
3. Decide the data resource type for the page report. You can create a page report using either query resources or business views. To use business views for the page report, select **Create Using Business View**.
4. Select the component you want to create in the report tab.

## Creating Page Report Tabs

Before you can create page report tabs, you first need to create a page report or [open an existing page report](https://devnet.logianalytics.com/hc/en-us/articles/4405664694551-Opening-Reports).

1. Do any of the following:
   * Navigate to **Home** > **New** > **Page Report Tab**.
   * Navigate to **File** > **New** > **Page Report Tab**.
   * On the report tab bar, right-click an existing report tab in the report and select **Insert** on the shortcut menu.

     ![Page Report Tab Bar](https://devnet.logianalytics.com/hc/article_attachments/4420556100631/rpt_crt_tab.gif)

   Designer displays the [Select Component for Page Report Tab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661705367-Select-Component-for-Page-Report-Tab-Dialog-Box).

   ![Select Component for Page Report Tab dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542080919/slctcmpntpgrpttb.gif)
2. In the **Report Title** text box, specify the title of the report tab. If you do not want a title, remove the text in the text box. The title is not used as the report tab name. For how to name a report tab, [select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664693399-Managing-Page-Reports#Rename).
3. Select the component to add in the report tab.

   Designer provides you with the following component types to start a page report tab. The component types available for a report tab vary with the data resource type that you have selected for the page report to which you are adding the report tab, which is determined at the time when you create the page report by the [Create Using Business View](#BV) option. Once you have specified the resource type, all the data components in the page report can only use the specified data resource type.

   * **Chart**  
     Select to create a report tab containing a chart.
   * **Table (Group Above)**   
     Select to create a report tab containing a table with group information above the detail row.
   * **Table (Group Left)**   
     Select to create a report tab containing a table with group information left to the detail row.
   * **Table (Group Left Above)**   
     Select to create a report tab containing a table with group information left above the detail row.
   * **Summary Table**  
     Select to create a report tab containing a table with only group and summary information.
   * **Crosstab**  
     Select to create a report tab containing a crosstab.
   * **Banded**  
     Select to create a report tab containing a vertical banded object.
   * **Horizontal Banded**  
     Select to create a report tab containing a horizontal banded object. Designer does not provide this component type when you are creating a report tab in a business view-based page report.
   * **Mailing Label**  
     Select to create a report tab containing a banded object, which is in the form of a mailing label layout. Designer does not provide this component type when you are creating a report tab in a business view-based page report.
   * **Tabular**  
     Select to create a report tab with a tabular which partitions the report page into several parts. Designer does not provide this component type when you are creating a report tab in a business view-based page report.
   * **Blank**  
     Select to create a report tab with no component in it.
4. Select **OK**.
   * When you select the chart, table, crosstab, or banded component type, Designer displays the corresponding component wizard for you to create the data component. You can select **Page Setup** in the wizard to set the page settings for the report tab in the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664543511-Page-Setup-Dialog-Box). For more information about how to define the data component, select the following links:
     + [Inserting Charts in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664387479-Inserting-Charts-in-a-Report)
     + [Inserting Tables in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661401239-Inserting-Tables-in-a-Report)
     + [Inserting Crosstabs in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664394775-Inserting-Crosstabs-in-a-Report)
     + [Inserting Banded Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661347735-Inserting-Banded-Objects-in-a-Report)   
       A banded object in a query-based page report can be a standard banded object, a horizontal banded object, or a mailing label banded object. The steps for creating a banded object in any of the three layouts are mostly the same, just that the banded object is positioned differently in each layout: one in a vertical way, one horizontally, and one in the form of mailing labels.

     When you add a report tab with a table, crosstab, or banded object in it into a query-based page report, Designer displays the Chart screen in the component wizard, using which you can create a chart together with the data component. You can only define the chart based on the data fields that you have added to the data component.

     ![Chart Screen](https://devnet.logianalytics.com/hc/article_attachments/4420542081175/rpt_crt_cht.gif)

     **To define the chart**

     1. Select a radio button to specify the chart type you like.
     2. From the **Category** drop-down list, select the field to display on the category (X) axis of the chart. To define the chart based on a table or banded object, you can choose from the group-by fields of the table or banded object on which you have added summaries; to define on a crosstab, you can choose from all the column and row fields of the crosstab.
     3. Choose the field to display on the series (Z) axis of the chart from the **Series** drop-down list. To define the chart based on a table or banded object, you can choose from all the group-by fields of the table or banded object; to define on a crosstab, you can choose from all the column and row fields of the crosstab.
     4. From the **Show Values** drop-down list, select the field to display on the value (Y) axis of the chart. To define the chart based on a table or banded object, you can choose from the summaries which are calculated based on the field you specify to display on the category axis of the chart; to define on a crosstab, you can choose from the aggregate fields in the crosstab.

     When you finish creating the report tab, Designer puts the chart in the report body together with the table or crosstab, or in the banded header panel of the banded object.
   * When you select Tabular, Designer displays the [Tabular Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661738775-Tabular-Wizard-Dialog-Box). Specify the number of rows and columns, and the border width and tabular width, respectively. You can also select **Page Setup** to set the page settings for the report tab in the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664543511-Page-Setup-Dialog-Box).

     ![Tabular Wizard](https://devnet.logianalytics.com/hc/article_attachments/4420542081431/tbulrwzd.gif)

     After you create the tabular, you can insert components and text into the tabular cells. A tabular helps you better design the report page. For more information about how to work with tabulars, see [Tabulars](https://devnet.logianalytics.com/hc/en-us/articles/4405661404695-Working-with-Tabulars).
   * When you select Blank, Designer displays the [Choose Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661466135-Choose-Data-Dialog-Box), prompting you to select the data resource to bind to the report body. Depending on the data resource type you have specified for the page report, to which you are adding the report tab, you can choose either from query resources or business views in the current catalog.

     ![Choose Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550833943/chsdt.gif)

     When selecting from query resources, if the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one; if you select a query, you can select **Edit** to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog). Then, Designer automatically creates a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets) based on the selected data resource in the page report. If you want to use an existing dataset in the current page report for the page report tab, select **More Options**, then select **Existing Dataset** and select a dataset. You can select **Edit** to modify the selected dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box), or select **<New Dataset...>** to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report Engine still runs the query separately for each dataset.

     After you create the blank report tab, you can add components to it as described in [Components](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports). You can also [change the data resource bound to its report body](#BindData); however, for a query-based report tab, you need to be very careful if you want to do this, because changing the bound query resource could result in that the data components in the report tab that use the dataset created from the query resource fail to run.

## Creating Web Reports

1. Navigate to **Home** > **New** > **Web Report** or **File** > **New** > **Web Report**.
2. Designer creates a blank web report with a tabular of one cell in the report. You can then split the [tabular](https://devnet.logianalytics.com/hc/en-us/articles/4405661404695-Working-with-Tabulars) and insert components to the tabular cells. For more information, see the corresponding topic about the specific component in [Components](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports).

## Creating Library Components

1. Navigate to **Home** > **New** > **Library Component** or **File** > **New** > **Library Component**. Designer displays the [Select Component for Library Component dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661704215-Select-Component-for-Library-Component-Dialog-Box).

   ![Select Component for Library Component dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542081687/slctcmpntlc.gif)
2. Type a title for the library component in the **Library Component Title** text box.
3. Select the type for the first data component in the library component.
4. If you select Blank, Designer creates a blank library component; if you select a specific component type, follow the wizard to create the data component in the library component. For more information about how to define the data component, select the following links:
   * [Inserting Charts in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664387479-Inserting-Charts-in-a-Report)
   * [Inserting Tables in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661401239-Inserting-Tables-in-a-Report)
   * [Inserting Crosstabs in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664394775-Inserting-Crosstabs-in-a-Report)
5. You can insert more components, such as charts, crosstabs, tables, KPIs, and web controls into the library component. For more information, see the corresponding topic about the specific component in [Components](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports).

A library component in Designer contains three parts:

* Wrapper defines some basic properties of the library component, such as the author, title, and description of the library component. The title bar of a library component is included in the wrapper. You can edit these [properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661910295-Wrapper-Properties) in the Report Inspector.
* [Configuration panel](#Config) can be used at runtime to set parameter values for the library component, filter or sort the library component, or change properties of the components in the contents.
* Contents contains three objects: Body, Data Source, and Page Panel. Body is the container that can hold a number of components such as charts, crosstabs, tables, geographic maps, labels, images, and web controls. Data Source contains the [datasets](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets) the data components in the body use and the [Refresh Object](https://devnet.logianalytics.com/hc/en-us/articles/4405661885207-Refresh-Object-Properties) of each business view on which the datasets are based. Page Panel controls the [page settings](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Setting) for printing and exporting the library component.

### Saving the Data Components in a Web Report as Library Components

Designer also supports saving the data components: tables, charts (including the KPI charts in KPIs), crosstabs, and geographic maps in a web report as library components, provided that all the objects in the data components can be supported by library components.

**To save the data components in a web report as library components**

1. Open the web report which contains the data components you want to save as library components.
2. Right-click a data component and select **Save as Library Component** from the shortcut menu.
3. In the Save As dialog box, specify the name for the library component in the **File Name** text box.
4. The library component file type (\*.lc) is the only default value in the **Files of Type** drop-down list.
5. Select **Save**. Designer displays the Library Component Setting dialog box.

   ![Library Component Setting dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556103703/lcsting.gif)
6. Specify the title, author, and the author's email address in the **Title**, **Author**, and **Author E-mail** text boxes respectively.
7. Select **OK** to save the selected data component as a library component with the specified name and title.
8. Repeat the preceding steps to save another data components in the web report as library components.

### Defining the Configuration Panel for Library Components

If you want the dashboard users to use the configuration panel at runtime, you need to configure the panel for each library component in Designer.

To display the configuration panel of a library component, select **Display Configuration Panel** on the top-right corner of the design area. You can adjust the height of the configuration panel to the size of the contents, but its width is equal to the width of the library component and cannot be changed. You can resize its width only by resizing the width of the library component.

![Configuration Panel of Library Component](https://devnet.logianalytics.com/hc/article_attachments/4420556103959/rpt_crt_cfgpnl1.gif)

The initial configuration panel contains a checkbox and two buttons.

* You can use the checkbox in the configuration panel to specify whether to show the panel by default when users insert the library component into a dashboard in JDashboard. You can select the checkbox by setting the **Default Show** property of the configuration panel to "true" in the Report Inspector as well.
* All actions in the configuration panel are bound with the OK and Cancel buttons in it. In JDashboard, users can select OK to apply the actions to the library component, and use the Cancel button to hide the configuration panel and initialize the values of the web controls in the panel to the last values. The two buttons are built-in buttons so you cannot delete, cut, copy, or paste them, but you can edit their properties in the Report Inspector and move them by dragging and dropping.

You can [insert labels](https://devnet.logianalytics.com/hc/en-us/articles/4405661383575-Working-with-Labels#Insert) and [use web controls](https://devnet.logianalytics.com/hc/en-us/articles/4405661414679-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component) such as Text Field, Checkbox, List, and Drop-down List in the configuration panel to filter or sort a library component, or change properties of objects in a library component.

When a library component contains parameters, Designer automatically creates web controls for the parameters in the configuration panel. Therefore, dashboard users can also use the configuration panel to specify parameter values for a library component at runtime. The default values of the parameters are those saved in the library component.

![Configuration Panel of Library Conponent for Specifying Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/4420556104215/rpt_crt_cfgpnl2.gif)

## Binding Data to the Report Body

You can bind a data resource to the report body of a page report tab, web report, or library component, which you can use directly for other objects in the report.

**To bind data to the body of a report**

1. Switch to the web report, library component, or the report tab in a page report.
2. Navigate to **Report** > **Bind Data**, or right-click any blank area in the report body and select **Bind Data** from the shortcut menu. Designer displays the [Bind Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661458711-Bind-Data-Dialog-Box) for you to choose the data resource to bind to the report body. For a web report or library component, you can choose from the predefined business views in the current catalog; for a page report tab, depending on the data resource type that you have specified for the page report containing the report tab, you can choose either from query resources or business views.
   * To choose a business view, select the business view from the resource tree.

     ![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542081943/bddt_bv.gif)
   * To choose a query resource：

     ![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550834327/bddt.gif)

     Select **New Dataset** if you want to select a data resource and create a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets) based on it to bind to the report body, then in the resource tree, select the required data resource. If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one in the current catalog to use. When you select a query, you can select **Edit** to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog).

     You can also bind an existing dataset in the current page report to the report body.
     Select **Existing Dataset** and select a dataset. You can select **Edit** to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box), or select **<New Dataset...>** to [create a dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets#Create) in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report Engine still runs the query separately for each dataset.
3. Select **OK** to bind the data.
4. Select any blank area in the report body and you can locate the data resource bound to it in the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/4405661950871-Data-Panel).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Once you have bound a data resource to the report body of a query-based page report tab and created any data component in the report tab which inherits the dataset created from the data resource, if you change the bound data resource of the report body to another one but the new data resource does not contain the same DBFields as the original one, Designer marks the invalid fields with a red cross icon in the data component. You cannot run the report tab until you update the data component or the new data resource to fix all the unmatched fields.

![Unmatched Fields in Newly Bound Data](https://devnet.logianalytics.com/hc/article_attachments/4420550834711/rpt_crt_bddt.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664697239-Choosing-the-Report-Type)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664694551-Opening-Reports)
