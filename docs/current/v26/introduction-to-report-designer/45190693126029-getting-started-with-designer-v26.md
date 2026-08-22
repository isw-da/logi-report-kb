---
title: "Getting Started with Designer v26"
id: 45190693126029
section: "Introduction to Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190693126029-Getting-Started-with-Designer-v26
updated_at: 2026-04-30T15:15:56Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Getting Started with Designer

There is a series of steps or tasks that you need to take before you can start using Report Designer. This topic guides you through the tracks of action for getting started with Designer.

- Reporting Development Environment Setup and Start-Up

- Create a Catalog and Set Up Data Connections

- Create Data Resources for Reports

- Start Creating Reports

- Publish and Export Reports

## 
Reporting Development Environment Setup and Start-Up

Install and Start Designer - Check Requirements and Select a Method
Before installing Designer, you need to check your system to make sure that it meets all the basic requirements. Designer can run on Windows, macOS, UNIX, and Linux platforms. You can use different methods to install and run Designer on each platform.

Designer System Requirements

Installing and Running Designer on Windows

Installing and Running Designer on macOS

Installing and Running Designer on UNIX

Starting Designer via Command Line

Get Familiar with the Designer Development Environment
After you start Designer, it is recommended that you get a general idea about its window elements. The Designer development environment consists of the following parts:

Ribbons

Catalog Manager

Data Panel

Inspector Panel

Components Panel

Design/View Area

## 
Create a Catalog and Set Up Data Connections

Create a Catalog
Before you can create reports in Designer, you need to first create a catalog and set up connections in the catalog to enable Designer to retrieve data from your data sources for the reports. You can use most of the current mainstream databases  which support JDBC drivers, and XML data sources, JSON data sources, and Elasticsearch data sources.

Knowing About Catalogs

### Creating a Catalog

- Select File > New Catalog. Designer displays the New Catalog dialog box.
    

Designer may prompt you to save changes to the current open catalog. You can open only one catalog at a time.

- In the Name text box, type the name for the catalog. The name must include the extension (.cat or .cat.xml).

- In the Data Source Name text box, type the name for the data source to be created along with the catalog (when you create a catalog, you create a data source in the catalog at the same time by default). You can include spaces in the name but do not use special characters. 

- In the Directory text box, specify the path to save the catalog. You can also select the ellipsis to browse to and select the directory. The directory you specify must not already contain a catalog file.

- Select OK. Designer displays the Catalog Manager. You can now set up connections to connect the catalog data source with your databases.

### Saving a Catalog

To save a catalog, select Save Catalog on the Catalog Manager toolbar. You have specified the type, name, and location  when you created the catalog. 

Connect to a JDBC Database
 Via specific JDBC drivers, you can create JDBC connections in a catalog to connect with different relational databases. You can also connect to  relational databases stored in Hive data warehouses via JDBC connections. 

JDBC Databases Designer Supports

Setting Up JDBC Connections in a Catalog

Getting Tables from the JDBC Database

Connect to a JSON Data Source
You can create JSON connections in a catalog to transform JSON data sources to relational data. 

Setting Up JSON Connections in a Catalog

Connect to an XML Data Source
You can create XML connections in a catalog to transform XML data sources to relational data. 

Setting Up XML Connections in a Catalog

Connect to a SOAP Web Service Data Source
Web services provide a standard means of inter-operating between different software applications, running on a variety of platforms and/or frameworks. It is a way to connect to a remote application and request data directly from the application without going to a database. Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources. You can add SOAP Web Service data sources to a catalog by importing WSDL files. 

Setting Up SOAP Web Service Connections in a Catalog

Connect to a MongoDB Database
You can create MongoDB connections in a catalog to connect to MongoDB databases and transform the collections in the databases to relational schemas.

Setting Up MongoDB Connections in a Catalog

Connect to a Elasticsearch Data Source
 You can create Elasticsearch connections in a catalog to connect to Elasticsearch data sources and transform the schemas in the data sources to relational schemas.

Setting Up Elasticsearch Connections in a Catalog

Use User-Defined Data Sources
Through the UDS  API, developer users can also access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available.

User Data Source API

Adding User-Defined Data Sources to a Catalog 

## 
Create Data Resources for Reports

Create a Query
After you set up the connections in a catalog, Designer is now able to get data from your databases. You can use the data to create queries, which are the data resources you can use to create page reports in Designer. You can use queries to build various professional reports, and view, change, and analyze data in different ways.

General Introduction to Queries

Creating Queries in a Catalog 

Create a Business View
Business views are the data resources for creating reports in both Designer and Server. They provide report designers and end users with an easily understood business-oriented view of their data.

Benefits of Business Views

Business View Elements

Creating Business Views in a Catalog 

Create a Parameter
You can use parameters to provide filters to pass to queries to dynamically control the report content at runtime. 

Creating Parameters in a Catalog

Create a Formula
 Formulas are objects that are computed at runtime, which enable you to manipulate field data by performing calculations on them. They control the data to display, and can even create new data that is not directly available from the database. 

Formula Levels

Formula Syntax

Creating Formulas in a Catalog

Create a Summary
Summaries are a special kind of formulas. You can use summaries to generate aggregations for your data using aggregate functions such as Count, Average, Sum, and Standard Deviation. 

Creating Summaries in a Catalog

## 
Start Creating Reports

Create, Save, and Preview a Report
After connecting a catalog to your database and creating the necessary data resources such as queries, business views, formulas, and summaries in the catalog, you can use the data resources to design your reports. Report supports these types of reports: Page Report, Web Report, and Library Component. 

Choosing the Report Type

Creating Reports

Saving Reports

Previewing Reports

Use Different Components in a Report
Components are the objects that you can place in a report. Report provides a full set of components that enable you to present and control the report data and presentation in a wide variety of ways. 

Report classifies the components into the following categories:

- 
Visual: Chart, Map, KPI, and Rank 

- 
Grid: Table, Crosstab, and Tabular

- 
Basic: Label, Text Box, Image, Subreport, and Banded Object

- 
Web controls: Filter Control, Parameter Control, Parameter Form Control, Navigation Control, Expand/Collapse Group, Radio Button, Checkbox, Drop-down List, List, Text Field, Password, Text Area, Button, Image Button, and Form

- 
Fields: DBField, Formula Field, Summary Field, and Parameter Field

- 
Drawing objects: Line, Arc, Box, Oval, and Round Box

- 
Special fields: Print Date, Print Time, Fetch Date, Fetch Time, Record Number, and many more

- 
Others: UDO, Barcode, and Multimedia Object (including Applet, RealMedia, and Windows Media) 

You can use either the Insert ribbon or the Components panel to add components into a report.

- To create a component using the Insert ribbon, place the mouse pointer at the location where you want to add the component in the report, then select the option representing the component in the ribbon.

- To create a component using the Components panel, drag the icon representing the component from the panel to the location in the report design area.

Designer then adds the component in the report or displays the corresponding dialog box for you to define the component.

Inserting Charts in a Report 

Inserting Tables in a Report 

Inserting Crosstabs in a Report

Inserting Banded Objects in a Report 

Inserting Geographic Maps in a Report

Creating Shape Maps in a Report

Using KPIs in a Report

Using Labels in a Report

Using DBFields in a Report

Using Parameter Fields in a Report

Using Formula Fields in a Report

Using Summary Fields in a Report

Using Special Fields in a Report

Using Tabulars in a Report

Using Web Controls in a Report

Using Images in a Report

Using Multimedia Objects in a Report

Using Text Boxes in a Report

Using Subreports in a Report

Using Drawing Objects in a Report

Using User-Defined Objects in a Report

Using Barcodes in a Report

Using Ranks in a Report

## 
Publish and Export Reports

Publish Reports to Production Environment
Designer, as a report design tool, enables you to publish your resources from it to a production environment. When you publish a resource such as a report template, Designer publishes all of the referenced report templates and additional resources such as images  although they are not visible. This ensures that images and linked reports are available at runtime. 

Publishing Reports

Export Reports to Different Formats
As you develop  reports in Designer, you can print or export the reports so that you can review the outputs at any time or share with others. 

Printing Reports

Exporting Reports to Mail

Exporting Reports to Logi Report Result

Exporting Reports to HTML

Exporting Reports to PDF

Exporting Reports to Excel

Exporting Reports to Text

Exporting Reports to RTF

Exporting Reports to XML

Exporting Reports to PostScript

Exporting Reports to Fax
