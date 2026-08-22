---
title: "Creating Reports"
id: 12480387474829
section: "Designing Your Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480387474829-Creating-Reports
updated_at: 2026-02-25T23:47:37Z
source_host: docs-report.zendesk.com
---
# 
Creating Reports

In Designer, you can use either query resources or business views to create reports depending on the type of the reports. Web reports and  library components can only be based on business views; page report can apply both business views and queries (including the data resources that function like queries, such as stored procedures, imported SQLs, imported APEs, user-defined data sources, and hierarchical data sources). In Server, end users can create ad hoc reports using business views; report designers can download the ad hoc reports to Designer for editing. This topic introduces how you can create reports of different types in Designer and bind data to the report body.

Before you can create reports, you need to first create a catalog to connect with your database or open an existing catalog.

This topic contains the following sections:

- Creating a Page Report

- Creating a Page Report Tab

- Creating a Web Report

- 
Creating a Library Component
- Saving Data Components in a Web Report as Library Components

- Defining the Configuration Panel for Library Components

## 
Creating a Page Report

When creating a page report, you also create a report tab in the page report.

- Select Home > New > Page Report or File > New > Page Report. Designer displays the Select Component for Page Report dialog box.
    

- In the Report Title text box, specify the title of the first report tab in the page report.

- 
Decide the data resource type for the page report. You can create a page report using either query resources or business views. To use business views for the page report, select Create Using Business View.

- Select the component you want to create in the report tab.

## 
Creating a Page Report Tab

Before you can create page report tabs, you first need to create a page report or open an existing page report.

To create a page report tab

- Do one of the following:
    
- Navigate to Home > New > Page Report Tab.

- Navigate to File > New > Page Report Tab.

- On the report tab bar, right-click an existing report tab in the report and select Insert on the shortcut menu.
        

Designer displays the Select Component for Page Report Tab dialog box.

- In the Report Title text box, specify the title of the report tab. If you do not want a title, remove the text in the text box. Designer does not applies this title as the report tab name. For how to name a report tab, see Renaming a Report Tab. 

- Select the component to add in the report tab. Designer provides you with the following component types to start a page report tab. The component types available for a report tab vary by the data resource type that you have selected for the page report to which you are adding the report tab, which is determined at the time when you create the page report by the Create Using Business View option. Once you have specified the resource type, all the data components in the page report can only use the specified data resource type.
    
- 
Chart
Select to create a report tab containing a chart.

- 
Table (Group Above) 
Select to create a report tab containing a table with group information above the detail row.

- 
Table (Group Left) 
Select to create a report tab containing a table with group information left to the detail row.

- 
Table (Group Left Above) 
Select to create a report tab containing a table with group information left above the detail row.

- 
Summary Table
Select to create a report tab containing a table with only group and summary information.

- 
Crosstab
Select to create a report tab containing a crosstab.

- 
Banded
Select to create a report tab containing a vertical banded object.

- 
Horizontal Banded
Select to create a report tab containing a horizontal banded object. Designer does not provide this component type when you are creating a report tab in a business view-based page report.

- 
Mailing Label
Select to create a report tab containing a banded object, which is in the form of a mailing label layout. Designer does not provide this component type when you are creating a report tab in a business view-based page report.

- 
Tabular
Select  to create a report tab with a tabular which partitions the report page into several parts. Designer does not provide this component type when you are creating a report tab in a business view-based page report.

- 
Blank
Select to create a report tab with no component in it.

- Select OK.
                
- When you select the chart, table, crosstab, or banded component type, Designer displays the corresponding component wizard for you to create the data component. You can select Page Setup in the wizard to set page settings for the report tab in the Page Setup dialog box. For more information about how to define the data component, select the following links:
                    
- Inserting Charts in a Report 

- Inserting Tables in a Report

- Inserting Crosstabs in a Report

- 
Inserting Banded Objects in a Report 
A banded object in a query-based page report can be a standard banded object, a horizontal banded object, or a mailing label banded object. The steps for creating a banded object in any of the three layouts are mostly the same, just that the banded object is positioned differently in each layout: one in a vertical way, one horizontally, and one in the form of mailing labels.

When you add a report tab with a table, crosstab, or banded object in it into a query-based page report, Designer displays the Chart screen in the component wizard, which you can use to create a chart together with the data component. You can only define the chart  based on the data fields that you have added to the data component.

To define the chart

- Select a radio button to specify the chart type you like.

- From the Category drop-down list, select the field to display on the category (X) axis of the chart. To define the chart based on a table or banded object, you can choose from the group-by fields of the table or banded object on which you have added summaries; to define on a crosstab, you can choose from all the column and row fields of the crosstab.   

-  Choose the field to display on the series (Z) axis of the chart from the Series drop-down list. To define the chart based on a table or banded object, you can choose from all the group-by fields of the table or banded object; to define on a crosstab, you can choose from all the column and row fields  of the crosstab.

- From the Show Values drop-down list, select the field to display on the value (Y) axis of the chart. To define the chart based on a table or banded object, you can choose from the summaries which are calculated based on the field you specify to display on the category axis of the chart; to define on a crosstab, you can choose from the aggregate fields in the crosstab.

When you finish creating the report tab, Designer puts the chart in the report body together with the table or crosstab, or in the banded header panel of the banded object.

- When you select Tabular, Designer displays the Tabular Wizard dialog box.   Specify the number of rows and columns, and the border width and tabular width, respectively. You can also select Page Setup to set page settings for the report tab in the Page Setup dialog box. After you create the tabular, you can insert components and text into the tabular cells. A tabular helps you better design the report page. For more information about how to work with tabulars, see Tabulars.

- 
When you select Blank, Designer displays the Choose Data dialog box, prompting you to select the dataset to bind to the report body.

## 
Creating a Web Report

- Navigate to Home > New > Web Report or File > New > Web Report.

- Designer creates a blank web report with a tabular of one cell in the report. You can then split the tabular and insert components to the tabular cells. For more information about using different components in a report, see Working with Components in Reports.

## 
Creating a Library Component

- Navigate to Home > New > Library Component or File > New > Library Component. Designer displays the Select Component for Library Component dialog box.
    

- Type a title for the library component in the Library Component Title text box.

- Select the type for the first data component in the library component.

- If you select Blank, Designer creates a blank library component; if you select a specific component type, follow the wizard to create the data component in the library component. For more information about how to define the data component, select the following links:
    
- Inserting Charts in a Report 

- Inserting Tables in a Report

- Inserting Crosstabs in a Report 

A library component in Designer contains three parts: 

- Wrapper defines some basic properties of the library component, such as the author, title, and description of the library component. The title bar of a library component is included in the wrapper. You can edit these properties in the Report Inspector. 

- 
Configuration panel can be used at runtime to set parameter values for the library component, filter or sort the library component, or change properties of the components in the library component.

- Contents contains three objects: Body, Data Source, and Page Panel. Body is the container that can hold a number of components such as charts, crosstabs, tables, geographic maps, labels, images, and web controls. Data Source contains the datasets the data components in the body use and the Refresh Object of each business view on which the datasets are based. Page Panel controls the page settings for printing and exporting the library component.

### 
Saving the Data Components in a Web Report as Library Components

Designer also supports saving the data components: tables, charts (including the KPI charts in KPIs), crosstabs, and geographic maps in a web report as library components, provided that all the objects in the data components can be supported by library components.

To save the data components in a web report as library components

- Open the web report which contains the data components you want to save as library components. 

- Right-click a data component and select Save as Library Component from the shortcut menu.

- In the Save As dialog box, specify the name for the library component in the File Name text box.

- The library component file type (*.lc) is the only default value in the Files of Type drop-down list.

- Select Save. Designer displays the Library Component Setting dialog box.
    

- Specify the title, author, and the author's email address in the Title, Author, and Author E-mail text boxes respectively.

- Select OK to save the selected data component as a library component with the specified name and title.

- Repeat the preceding steps to save another data components in the web report as library components.

### 
Defining the Configuration Panel for Library Components

If you want the dashboard users to use the configuration panel at runtime, you need to configure the panel for each library component in  Designer.

To display the configuration panel of a library component, select Display Configuration Panel on the top-right corner of the design area. You can adjust the height of the configuration panel to the size of the content, but its width is equal to the width of the library component and cannot be changed. You can resize its width only by resizing the width of the library component.

 The initial configuration panel contains a checkbox and two buttons.

- You can use the checkbox in the configuration panel to specify whether to show the panel by default when users insert the library component into a dashboard in JDashboard. You can select the checkbox by setting the Default Show property of the configuration panel to "true" in the Report Inspector as well. 

- All actions in the configuration panel are bound with the OK and Cancel buttons in it. In JDashboard, users can select OK to apply the actions to the library component, and use the Cancel button to hide the configuration panel and initialize the values of the web controls in the panel to the last values. The two buttons are built-in buttons so you cannot  delete, cut, copy, or paste them, but you can edit their properties  in the Report Inspector and move them by dragging and dropping.

You can insert labels and use web controls such as Text Field, Checkbox, List, and Drop-down List in the configuration panel to filter or sort a library component, or change properties of objects in a library component.

When a library component contains parameters, Designer automatically creates web controls for the parameters in the configuration panel. Therefore, dashboard users can also use the configuration panel to specify parameter values for a library component at runtime. The default values  of the parameters are those saved in the library component.
