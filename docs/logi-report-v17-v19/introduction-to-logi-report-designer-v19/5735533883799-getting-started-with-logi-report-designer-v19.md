---
title: "Getting Started with Logi Report Designer v19"
id: 5735533883799
section: "Introduction to Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735533883799-Getting-Started-with-Logi-Report-Designer-v19
updated_at: 2023-01-24T07:48:40Z
---

# Getting Started with Logi Report Designer v19

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735484077207-Logi-Report-Designer-Guide-v19-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516407191-System-Requirements)

# Getting Started with Logi Report Designer v19

There is a series of steps or tasks that you need to take before you can start using Logi Report Designer. This topic guides you through the tracks of action for getting started with Designer.

* [Reporting Development Environment Setup and Start-Up](#DevEnv)
* [Create a Catalog and Set Up Data Connections](#Connection)
* [Create Data Resources for Reports](#ReportData)
* [Start Creating Reports](#CreateRpt)
* [Publish and Export Reports](#Publish)

## Reporting Development Environment Setup and Start-Up

[Install and Start Designer - Check Requirements and Select a Method](#)

Before installing Designer, you need to check your system to make sure that it meets all the basic requirements. Designer can run on Windows, macOS, UNIX, and Linux platforms. You can use different methods to install and run Designer on each platform.

[Designer System Requirements](https://devnet.logianalytics.com/hc/en-us/articles/5735516407191-System-Requirements)

[Installing and Running Designer on Windows](https://devnet.logianalytics.com/hc/en-us/articles/5735568230167-Installing-and-Running-Designer-on-Windows)

[Installing and Running Designer on macOS](https://devnet.logianalytics.com/hc/en-us/articles/5735525675543-Installing-and-Running-Designer-on-macOS)

[Installing and Running Designer on UNIX](https://devnet.logianalytics.com/hc/en-us/articles/5735532262679-Installing-and-Running-Designer-on-UNIX-Linux)

[Starting Designer via Command Line](https://devnet.logianalytics.com/hc/en-us/articles/5735545183511-Starting-Designer-via-Command-Line)

[Get Familiar with the Designer Development Environment](#)

After you start Designer, it is recommended that you get a general idea about its window elements. The Designer development environment consists of the following parts:

[Ribbons](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs)

[Catalog Manager](https://devnet.logianalytics.com/hc/en-us/articles/5735570032407-Catalog-Manager)

[Data Panel](https://devnet.logianalytics.com/hc/en-us/articles/5735576969879-Data-Panel)

[Inspector Panel](https://devnet.logianalytics.com/hc/en-us/articles/5735570047895-Inspector-Panel)

[Components Panel](https://devnet.logianalytics.com/hc/en-us/articles/5735570024599-Components-Panel)

[Design/View Area](https://devnet.logianalytics.com/hc/en-us/articles/5735555805079-Design-View-Area)

## Create a Catalog and Set Up Data Connections

[Create a Catalog](#)

Before you can create reports in Designer, you need to first create a catalog and set up connections in the catalog to enable Designer to retrieve data from your data sources for the reports. You can use most of the current mainstream databases which support JDBC drivers, and XML data sources, JSON data sources, and Elasticsearch data sources.

[Knowing About Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/5735520312215-Knowing-About-Catalogs)

### Creating a Catalog

1. Select **File** > **New Catalog**. Designer displays the [New Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566792343-New-Catalog-Dialog-Box).

   ![New Catalog dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898458684311/nwctlg.gif)

   Designer may prompt you to save changes to the current open catalog. You can open only one catalog at a time.
2. In the **Name** text box, type the name for the catalog. The name must include the extension (.cat or .cat.xml).
3. In the **Data Source Name** text box, type the name for the data source to be created along with the catalog (when you create a catalog, you create a data source in the catalog at the same time by default). You can include spaces in the name but do not use special characters.
4. In the **Directory** text box, specify the path to save the catalog. You can also select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to browse to and select the directory. The directory you specify must not already contain a catalog file.
5. Select **OK**. Designer displays the Catalog Manager. You can now set up connections to connect the catalog data source with your databases.

### Saving a Catalog

To save a catalog, select **Save Catalog** on the Catalog Manager toolbar. You have specified the type, name, and location when you created the catalog.

[Connect to a JDBC Database](#)

Via specific JDBC drivers, you can create JDBC connections in a catalog to connect with different relational databases. You can also connect to relational databases stored in Hive data warehouses via JDBC connections.

[JDBC Databases Designer Supports](https://devnet.logianalytics.com/hc/en-us/articles/5735568258711-Supported-Report-Databases)

[Setting Up JDBC Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735521536663-Setting-Up-JDBC-Connections-in-a-Catalog)

[Getting Tables from the JDBC Database](https://devnet.logianalytics.com/hc/en-us/articles/5735521508887-Using-Tables-Views-Synonyms)

[Connect to a JSON Data Source](#)

You can create JSON connections in a catalog to transform JSON data sources to relational data.

[Setting Up JSON Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog#Set)

[Connect to an XML Data Source](#)

You can create XML connections in a catalog to transform XML data sources to relational data.

[Setting Up XML Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735499628183-Working-with-XML-Connections-in-a-Catalog#Set)

[Connect to a SOAP Web Service Data Source](#)

Web services provide a standard means of inter-operating between different software applications, running on a variety of platforms and/or frameworks. It is a way to connect to a remote application and request data directly from the application without going to a database. Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources. You can add SOAP Web Service data sources to a catalog by importing WSDL files.

[Setting Up SOAP Web Service Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735528205847-Accessing-Data-via-SOAP-Web-Service-Connections#Set)

[Connect to a MongoDB Database](#)

You can create MongoDB connections in a catalog to connect to MongoDB databases and transform the collections in the databases to relational schemas.

[Setting Up MongoDB Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735507864599-Working-with-MongoDB-Connections-in-a-Catalog#Set)

[Connect to a Elasticsearch Data Source](#)

You can create Elasticsearch connections in a catalog to connect to Elasticsearch data sources and transform the schemas in the data sources to relational schemas.

[Setting Up Elasticsearch Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735564552471-Accessing-Data-via-Elasticsearch-Connections#Set)

[Use User-Defined Data Sources](#)

Through the UDS API, developer users can also access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available.

[User Data Source API](https://devnet.logianalytics.com/hc/en-us/articles/5735521631127-User-Data-Source-API)

[Adding User-Defined Data Sources to a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735499573911-Adding-User-Defined-Data-Sources-to-a-Catalog)

## Create Data Resources for Reports

[Create a Query](#)

After you set up the connections in a catalog, Designer is now able to get data from your databases. You can use the data to create queries, which are the data resources you can use to create page reports in Designer. You can use queries to build various professional reports, and view, change, and analyze data in different ways.

[General Introduction to Queries](https://devnet.logianalytics.com/hc/en-us/articles/5735547176855-General-Introduction-to-Queries)

[Creating Queries in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog)

[Create a Business View](#)

Business views are the data resources for creating reports in both Designer and Server. They provide report designers and end users with an easily understood business-oriented view of their data.

[Benefits of Business Views](https://devnet.logianalytics.com/hc/en-us/articles/5735533912087-Benefits-of-Business-Views)

[Business View Elements](https://devnet.logianalytics.com/hc/en-us/articles/5735576528791-Business-View-Elements)

[Creating Business Views in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog)

[Create a Parameter](#)

You can use parameters to provide filters to pass to queries to dynamically control the report content at runtime.

[Creating Parameters in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735516481047-Creating-Parameters-in-a-Catalog)

[Create a Formula](#)

Formulas are objects that are computed at runtime, which enable you to manipulate field data by performing calculations on them. They control the data to display, and can even create new data that is not directly available from the database.

[Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels)

[Formula Syntax](https://devnet.logianalytics.com/hc/en-us/articles/5735532056855-Formula-Syntax)

[Creating Formulas in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735525453207-Creating-Formulas-in-a-Catalog)

[Create a Summary](#)

Summaries are a special kind of formulas. You can use summaries to generate aggregations for your data using aggregate functions such as Count, Average, Sum, and Standard Deviation.

[Creating Summaries in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries)

## Start Creating Reports

[Create, Save, and Preview a Report](#)

After connecting a catalog to your database and creating the necessary data resources such as queries, business views, formulas, and summaries in the catalog, you can use the data resources to design your reports. Logi Report supports these types of reports: Page Report, Web Report, and Library Component.

[Choosing the Report Type](https://devnet.logianalytics.com/hc/en-us/articles/5735534332951-Choosing-the-Report-Type)

[Creating Reports](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports)

[Saving Reports](https://devnet.logianalytics.com/hc/en-us/articles/5735586480535-Saving-Reports)

[Previewing Reports](https://devnet.logianalytics.com/hc/en-us/articles/5735555715607-Previewing-Reports)

[Use Different Components in a Report](#)

Components are the objects that you can place in a report. Logi Report provides a full set of components that enable you to present and control the report data and presentation in a wide variety of ways.

Logi Report classifies the components into the following categories:

* **Visual**: Chart, Map, KPI, and Rank
* **Grid**: Table, Crosstab, and Tabular
* **Basic**: Label, Text Box, Image, Subreport, and Banded Object
* **Web controls**: Filter Control, Parameter Control, Parameter Form Control, Navigation Control, Expand/Collapse Group, Radio Button, Checkbox, Drop-down List, List, Text Field, Password, Text Area, Button, Image Button, and Form
* **Fields**: DBField, Formula Field, Summary Field, and Parameter Field
* **Drawing objects**: Line, Arc, Box, Oval, and Round Box
* **Special fields**: Print Date, Print Time, Fetch Date, Fetch Time, Record Number, and many more
* **Others**: UDO, Barcode, and Multimedia Object (including Applet, RealMedia, and Windows Media)

You can use either the **Insert** ribbon or the **Components** panel to add components into a report.

* To create a component using the Insert ribbon, place the mouse pointer at the location where you want to add the component in the report, then select the option representing the component in the ribbon.
* To create a component using the Components panel, drag the icon representing the component from the panel to the location in the report design area.

Designer then adds the component in the report or displays the corresponding dialog box for you to define the component.

![Add Component to Report via Menu or Panel](https://devnet.logianalytics.com/hc/article_attachments/9898475720727/addcmpnt.gif)

[Inserting Charts in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735512245143-Inserting-Charts-in-a-Report)

[Inserting Tables in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735521199255-Inserting-Tables-in-a-Report)

[Inserting Crosstabs in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735527515799-Inserting-Crosstabs-in-a-Report)

[Inserting Banded Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735511901079-Inserting-Banded-Objects-in-a-Report)

[Inserting Geographic Maps in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735512449175-Inserting-Geographic-Maps-in-a-Report)

[Creating Shape Maps in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735521118231-Using-Shape-Maps)

[Using KPIs in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs)

[Using Labels in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels)

[Using DBFields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields)

[Using Parameter Fields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields)

[Using Formula Fields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields)

[Using Summary Fields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields)

[Using Special Fields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields)

[Using Tabulars in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735564433175-Working-with-Tabulars)

[Using Web Controls in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735564487575-Working-with-Web-Controls)

[Using Images in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images)

[Using Multimedia Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects)

[Using Text Boxes in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes)

[Using Subreports in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports)

[Using Drawing Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735512413207-Working-with-Drawing-Objects)

[Using User-Defined Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735507452311-Working-with-UDOs)

[Using Barcodes in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735498517911-Working-with-Barcodes)

[Using Ranks in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735564383767-Working-with-Ranks)

## Publish and Export Reports

[Publish Reports to Production Environment](#)

Designer, as a report design tool, enables you to publish your resources from it to a production environment. When you publish a resource such as a report template, Designer publishes all of the referenced report templates and additional resources such as images although they are not visible. This ensures that images and linked reports are available at runtime.

[Publishing Reports](https://devnet.logianalytics.com/hc/en-us/articles/5735576653207-Publishing-and-Downloading-Resources#PubReport)

[Export Reports to Different Formats](#)

As you develop reports in Designer, you can print or export the reports so that you can review the outputs at any time or share with others.

[Printing Reports](https://devnet.logianalytics.com/hc/en-us/articles/5735531983767-Printing-Reports)

[Exporting Reports to Mail](https://devnet.logianalytics.com/hc/en-us/articles/5735531881623-Exporting-Reports-to-Mail)

[Exporting Reports to Logi Report Result](https://devnet.logianalytics.com/hc/en-us/articles/5735525374615-Exporting-Reports-to-Logi-Report-Result)

[Exporting Reports to HTML](https://devnet.logianalytics.com/hc/en-us/articles/5735553350295-Exporting-Reports-to-HTML)

[Exporting Reports to PDF](https://devnet.logianalytics.com/hc/en-us/articles/5735531895447-Exporting-Reports-to-PDF)

[Exporting Reports to Excel](https://devnet.logianalytics.com/hc/en-us/articles/5735516034199-Exporting-Reports-to-Excel)

[Exporting Reports to Text](https://devnet.logianalytics.com/hc/en-us/articles/5735525405719-Exporting-Reports-to-Text)

[Exporting Reports to RTF](https://devnet.logianalytics.com/hc/en-us/articles/5735531933591-Exporting-Reports-to-RTF)

[Exporting Reports to XML](https://devnet.logianalytics.com/hc/en-us/articles/5735516111511-Exporting-Reports-to-XML)

[Exporting Reports to PostScript](https://devnet.logianalytics.com/hc/en-us/articles/5735531904791-Exporting-Reports-to-PostScript)

[Exporting Reports to Fax](https://devnet.logianalytics.com/hc/en-us/articles/5735553344535-Exporting-Reports-to-Fax)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735484077207-Logi-Report-Designer-Guide-v19-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516407191-System-Requirements)
