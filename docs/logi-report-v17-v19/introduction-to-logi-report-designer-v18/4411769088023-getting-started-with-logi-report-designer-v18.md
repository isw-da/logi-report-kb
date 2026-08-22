---
title: "Getting Started with Logi Report Designer v18"
id: 4411769088023
section: "Introduction to Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4411769088023-Getting-Started-with-Logi-Report-Designer-v18
updated_at: 2022-07-27T10:17:26Z
---

# Getting Started with Logi Report Designer v18

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664317847-Logi-Report-Designer-Guide-v18-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661785879-System-Requirements)

# Getting Started with Logi Report Designer v18

There is a series of steps or tasks that you need to take before you can start using Logi Report Designer. This topic guides you through the tracks of action for getting started with Designer.

* [Reporting Development Environment Setup and Start-up](#DevEnv)
* [Create a Catalog and Set Up Data Connections](#Connection)
* [Create Data Resources for Reports](#ReportData)
* [Start Creating Reports](#CreateRpt)
* [Publish and Export Reports](#Publish)

## Reporting Development Environment Setup and Start-up

[Install and Start Designer - Check Requirements and Select a Method](#)

Before installing Designer, you need to check your system to make sure that it meets all the basic requirements. Designer can run on Windows, macOS, UNIX, and Linux platforms. You can use different methods to install and run Designer on each platform.

[Designer System Requirements](https://devnet.logianalytics.com/hc/en-us/articles/4405661785879-System-Requirements)

[Installing and Running Designer on Windows](https://devnet.logianalytics.com/hc/en-us/articles/4405664605975-Installing-and-Running-Designer-on-Windows)

[Installing and Running Designer on macOS](https://devnet.logianalytics.com/hc/en-us/articles/4405661773847-Installing-and-Running-Designer-on-macOS)

[Installing and Running Designer on UNIX](https://devnet.logianalytics.com/hc/en-us/articles/4405661775895-Installing-and-Running-Designer-on-UNIX-Linux)

[Starting Designer via Command Line](https://devnet.logianalytics.com/hc/en-us/articles/4405661769495-Starting-Designer-via-Command-Line)

[Get Familiar with the Designer Development Environment](#)

After you start Designer, it is recommended that you get a general idea about its window elements. The Designer development environment consists of the following parts:

[Menu Tabs](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs)

[Catalog Manager](https://devnet.logianalytics.com/hc/en-us/articles/4405661949847-Catalog-Manager)

[Data Panel](https://devnet.logianalytics.com/hc/en-us/articles/4405661950871-Data-Panel)

[Inspector Panel](https://devnet.logianalytics.com/hc/en-us/articles/4405661951895-Inspector-Panel)

[Components Panel](https://devnet.logianalytics.com/hc/en-us/articles/4405664701079-Components-Panel)

[Design/View Area](https://devnet.logianalytics.com/hc/en-us/articles/4405661948695-Design-View-Area)

## Create a Catalog and Set Up Data Connections

[Create a Catalog](#)

Before you can create reports in Designer, you need to first create a catalog and set up connections in the catalog to enable Designer to retrieve data from your data sources for the reports. You can use most of the current mainstream databases which support JDBC drivers, and XML data sources, JSON data sources, and Elasticsearch data sources.

[Knowing About Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/4405661333143-Knowing-About-Catalogs)

### Creating a Catalog

1. Select **File** > **New Catalog**. Designer displays the [New Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664534679-New-Catalog-Dialog-Box).

   ![New Catalog dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402296727/nwctlg.gif)

   Designer may prompt you to save changes to the current open catalog. You can open only one catalog at a time.
2. In the **Name** text box, type the name for the catalog. The name must include the extension (.cat or .cat.xml).
3. In the **Data Source Name** text box, type the name for the data source to be created along with the catalog (when you create a catalog, you create a data source in the catalog at the same time by default). You can include spaces in the name but do not use special characters.
4. In the **Directory** text box, specify the path to save the catalog. You can also select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420402297111/btn_ellipsis2.gif) to browse to and select the directory. The directory you specify must not already contain a catalog file.
5. Select **OK** to create the catalog.

   Designer displays the Catalog Manager. You can then set up connections to connect the catalog data source with your databases.

### Saving a Catalog

To save a catalog, select **Save Catalog** on the Catalog Manager toolbar. You have specified the type, name, and location when you created the catalog.

[Connect to a JDBC Database](#)

Via specific JDBC drivers, you can create JDBC connections in a catalog to connect with different relational databases. You can also connect to relational databases stored in Hive data warehouses via JDBC connections.

[JDBC Databases Designer Supports](https://devnet.logianalytics.com/hc/en-us/articles/4405661784855-Supported-Report-Databases)

[Setting Up JDBC Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661427991-Setting-Up-JDBC-Connections-in-a-Catalog)

[Getting Tables from the JDBC Database](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms)

[Connect to a JSON Data Source](#)

You can create JSON connections in a catalog to transform JSON data sources to relational data.

[Setting Up JSON Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661432343-Working-with-JSON-Connections-in-a-Catalog#Set)

[Connect to an XML Data Source](#)

You can create XML connections in a catalog to transform XML data sources to relational data.

[Setting Up XML Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661442711-Working-with-XML-Connections-in-a-Catalog#Set)

[Connect to a SOAP Web Service Data Source](#)

Web services provide a standard means of inter-operating between different software applications, running on a variety of platforms and/or frameworks. It is a way to connect to a remote application and request data directly from the application without going to a DBMS. Designer supports SOAP Web Services defined by WSDL 1.1 or WSDL 2.0 as data sources. You can add SOAP Web Service data sources to a catalog by importing WSDL files.

[Setting Up SOAP Web Service Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661439639-Connecting-via-SOAP-Web-Service-Connections#Set)

[Connect to a MongoDB Database](#)

You can create MongoDB connections in a catalog to connect to MongoDB databases and transform the collections in the databases to relational schemas.

[Setting Up MongoDB Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405664420375-Working-with-MongoDB-Connections-in-a-Catalog#Set)

[Connect to a Elasticsearch Data Source](#)

You can create Elasticsearch connections in a catalog to connect to Elasticsearch data sources and transform the schemas in the data sources to relational schemas.

[Setting Up Elasticsearch Connections in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661418007-Connecting-via-Elasticsearch-Connections#Set)

[Use User-Defined Data Sources](#)

Through the UDS API, developer users can also access data from an external data source, such as a text file or Excel file, which is not stored in a database or when there is no JDBC driver available.

[User Data Source API](https://devnet.logianalytics.com/hc/en-us/articles/4405664421655-User-Data-Source-API)

[Adding User-Defined Data Sources to a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661436055-Adding-User-Defined-Data-Sources-to-a-Catalog)

## Create Data Resources for Reports

[Create a Query](#)

After you set up the connections in a catalog, Designer is now able to get data from your databases. You can use the data to create queries, which are the data resources you can use to create page reports in Designer. You can use queries to build various professional reports, and view, change, and analyze data in different ways.

[General Introduction to Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405661920535-General-Introduction-to-Queries)

[Creating Queries in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog)

[Create a Business View](#)

Business views are the data resources for creating reports in both Designer and Server. They provide report designers and end users with an easily understood business-oriented view of their data.

[Benefits of Business Views](https://devnet.logianalytics.com/hc/en-us/articles/4411774466967-Benefits-of-Business-Views)

[Business View Elements](https://devnet.logianalytics.com/hc/en-us/articles/4405661913239-Business-View-Elements)

[Creating Business Views in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog)

[Create a Parameter](#)

You can use parameters to provide filters to pass to queries to dynamically control the report content at runtime.

[Creating Parameters in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405664612887-Creating-Parameters-in-a-Catalog)

[Create a Formula](#)

Formulas are objects that are computed at runtime, which enable you to manipulate field data by performing calculations on them. They control the data to display, and can even create new data that is not directly available from the database.

[Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/4405664602263-Formula-Levels)

[Formula Syntax](https://devnet.logianalytics.com/hc/en-us/articles/4405661764503-Formula-Syntax)

[Creating Formulas in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661763223-Creating-Formulas-in-a-Catalog)

[Create a Summary](#)

Summaries are a special kind of formulas. You can use summaries to generate aggregations for your data using aggregate functions such as Count, Average, Sum, and Standard Deviation.

[Creating Summaries in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries)

## Start Creating Reports

[Create, Save, and Preview a Report](#)

After connecting a catalog to your database and creating the necessary data resources such as queries, business views, formulas, and summaries in the catalog, you can use the data resources to design your reports. Logi Report supports these types of reports: Page Report, Web Report, and Library Component.

[Choosing the Report Type](https://devnet.logianalytics.com/hc/en-us/articles/4405664697239-Choosing-the-Report-Type)

[Creating Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports)

[Saving Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405661938967-Saving-Reports)

[Previewing Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405664696343-Previewing-Reports)

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

You can use either the **Insert** menu tab or the **Components** panel to add components into a report.

* To create a component using the Insert menu tab, place the mouse pointer at the location where you want to add the component in the report, then select the option representing the component on the menu tab.
* To create a component using the Components panel, drag the icon representing the component from the panel to the desired location in the report design area.

Designer then adds the component in the report or displays the corresponding dialog box for you to define the component.

![Add Component to Report via Menu or Panel](https://devnet.logianalytics.com/hc/article_attachments/4420394626583/addcmpntv18.2.gif)

[Inserting Charts in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664387479-Inserting-Charts-in-a-Report)

[Inserting Tables in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661401239-Inserting-Tables-in-a-Report)

[Inserting Crosstabs in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664394775-Inserting-Crosstabs-in-a-Report)

[Inserting Banded Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661347735-Inserting-Banded-Objects-in-a-Report)

[Inserting Geographic Maps in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661387159-Inserting-Geographic-Maps-in-a-Report)

[Creating Shape Maps in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664397975-Using-Shape-Maps)

[Using KPIs in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661382551-Working-with-KPIs)

[Using Labels in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661383575-Working-with-Labels)

[Using DBFields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664395799-Working-with-DBFields)

[Using Parameter Fields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664399255-Working-with-Parameter-Fields)

[Using Formula Fields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661380119-Working-with-Formula-Fields)

[Using Summary Fields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661398551-Working-with-Summary-Fields)

[Using Special Fields in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields)

[Using Tabulars in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661404695-Working-with-Tabulars)

[Using Web Controls in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661409815-Working-with-Web-Controls)

[Using Images in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661381143-Working-with-Images)

[Using Multimedia Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661390743-Working-with-Multimedia-Objects)

[Using Text Boxes in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664406679-Working-with-Text-Boxes)

[Using Subreports in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664401431-Working-with-Subreports)

[Using Drawing Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661379095-Working-with-Drawing-Objects)

[Using User-Defined Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661407255-Working-with-UDOs)

[Using Barcodes in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661349911-Working-with-Barcodes)

[Using Ranks in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405664400279-Working-with-Ranks)

## Publish and Export Reports

[Publish Reports to Production Environment](#)

Designer, as a report design tool, enables you to publish your resources from it to a production environment. When you publish a resource such as a report template, Designer publishes all of the referenced report templates and additional resources such as images although they are not visible. This ensures that images and linked reports are available at runtime.

[Publishing Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405661923607-Publishing-and-Downloading-Resources#PubReport)

[Export Reports to Different Formats](#)

As you develop reports in Designer, you can print or export the reports so that you can review the outputs at any time or share with others.

[Printing Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405664599447-Printing-Report-Result)

[Exporting Reports to Mail](https://devnet.logianalytics.com/hc/en-us/articles/4405664597271-Exporting-to-Mail)

[Exporting Reports to Logi Report Result](https://devnet.logianalytics.com/hc/en-us/articles/4405664598551-Exporting-to-Logi-Report-Result)

[Exporting Reports to HTML](https://devnet.logianalytics.com/hc/en-us/articles/4405664596375--Exporting-to-HTML)

[Exporting Reports to PDF](https://devnet.logianalytics.com/hc/en-us/articles/4405661756567-Exporting-to-PDF)

[Exporting Reports to Excel](https://devnet.logianalytics.com/hc/en-us/articles/4405661753751-Exporting-to-Excel)

[Exporting Reports to Text](https://devnet.logianalytics.com/hc/en-us/articles/4405661760663-Exporting-to-Text)

[Exporting Reports to RTF](https://devnet.logianalytics.com/hc/en-us/articles/4405661759255-Exporting-to-RTF)

[Exporting Reports to XML](https://devnet.logianalytics.com/hc/en-us/articles/4405661761687-Exporting-to-XML)

[Exporting Reports to PostScript](https://devnet.logianalytics.com/hc/en-us/articles/4405661757591-Exporting-to-PostScript)

[Exporting Reports to Fax](https://devnet.logianalytics.com/hc/en-us/articles/4405661755031-Exporting-to-Fax)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664317847-Logi-Report-Designer-Guide-v18-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661785879-System-Requirements)
